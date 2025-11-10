use pyo3::{exceptions::PyValueError, prelude::*};
use tokio::runtime::Runtime;

use crate::{
    basic_sql::init_database_or_exit,
    constants::{get_pool, PoolEngine, Record},
    structs::UsersDb,
};

#[pymethods]
impl UsersDb {
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
    /*
    type User = tuple[str, str, str]
    type UUID = str


    class UsersDb:
        def append(self, password: str, email: str, name: str) -> Optional[UUID]: ...

        def discard(self, target: str) -> Optional[UUID]: ...

        def get(self, target: str) -> Optional[User]: ...

        def set(self, target: str, data: dict) -> None: ...

    */
    pub fn append(
        &self,
        password: String,
        email: String,
        name: String,
    ) -> PyResult<Option<String>> {
        todo!()
    }

    pub fn discard(&self, target: String) -> PyResult<Option<String>> {
        todo!()
    }

    pub fn get(&self, target: String) -> PyResult<Option<String>> {
        todo!()
    }

    pub fn set(&self, target: String, data: Record) -> PyResult<()> {
        todo!()
    }
}
