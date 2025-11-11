use pyo3::{exceptions::PyValueError, prelude::*};
use tokio::runtime::Runtime;

use crate::{
    basic_sql::init_database_or_exit,
    constants::{get_pool, PoolEngine, Record},
    logic::{
        create_or_null::create_or_null, discard_or_null::discard_or_null, get_or_null::get_or_null,
        update_or_err::update_or_err,
    },
    structs::UsersDb,
};

#[pymethods]
// class UsersDb:
impl UsersDb {
    // type User = tuple[str, str, str]
    // type UUID = str
    #[new]
    fn new() -> PyResult<Self> {
        let runtime: Runtime =
            Runtime::new().map_err(|err| PyValueError::new_err(err.to_string()))?;

        let pool: PoolEngine = runtime
            .block_on(get_pool())
            .map_err(|err| PyValueError::new_err(err.to_string()))?;

        runtime.block_on(init_database_or_exit(&pool));

        Ok(UsersDb {
            rt_sync: runtime,
            pool: pool,
        })
    }

    // def append(self, password: str, email: str, name: str) -> Optional[UUID]: ...
    pub fn append(
        &self,
        password: String,
        email: String,
        name: String,
    ) -> PyResult<Option<String>> {
        Ok(self
            .rt_sync
            .block_on(create_or_null((password, email, name), &self.pool))
            .map_err(|err| PyValueError::new_err(err.to_string()))?)
    }

    // def discard(self, target: str) -> Optional[UUID]: ...
    pub fn discard(&self, target: String) -> PyResult<Option<String>> {
        Ok(self
            .rt_sync
            .block_on(discard_or_null(target, &self.pool))
            .map_err(|err| PyValueError::new_err(err.to_string()))?)
    }

    // def get(self, target: str) -> Optional[User]: ...
    pub fn get(&self, target: String) -> PyResult<Option<Record>> {
        Ok(self
            .rt_sync
            .block_on(get_or_null(target, &self.pool))
            .map_err(|err| PyValueError::new_err(err.to_string()))?)
    }

    // def set(self, target: str, data: dict) -> None: ...
    pub fn set(&self, target: String, data: Record) -> PyResult<()> {
        self.rt_sync
            .block_on(update_or_err(target, data, &self.pool))
            .map_err(|err| PyValueError::new_err(err.to_string()))?;
        Ok(())
    }
}
