use pyo3::exceptions::PyValueError;
// dependences
use pyo3::prelude::*;
use sea_query::Query;
use tokio::runtime::Runtime;
use uuid::Uuid;

// local imports
use crate::sql_conf::{get_pool, init_database, PoolEngine, UsersTable, QUERY_ENGINE};
use crate::structs::UsersDb;

#[pymethods]
impl UsersDb {
    #[new]
    fn new() -> PyResult<Self> {
        let rt: Runtime = Runtime::new().map_err(|e| PyValueError::new_err(e.to_string()))?;
        let pool: PoolEngine = rt
            .block_on(get_pool())
            .map_err(|e| PyValueError::new_err(e.to_string()))?;

        rt.block_on(init_database(&pool));

        Ok(UsersDb {
            pool: pool,
            sync: rt,
        })
    }

    fn append(&self, password: String, email: String, name: String) -> PyResult<String> {
        let last_id: String = Uuid::new_v4().to_string();

        let sql: String = Query::insert()
            .into_table(UsersTable::Table)
            .columns([
                UsersTable::Id,
                UsersTable::Password,
                UsersTable::Email,
                UsersTable::Name,
            ])
            .values_panic([
                last_id.clone().into(),
                password.into(),
                email.into(),
                name.into(),
            ])
            .to_string(QUERY_ENGINE);

        self.sync
            .block_on(sqlx::query(&sql).execute(&self.pool))
            .map_err(|e| PyValueError::new_err(e.to_string()))?;

        Ok(last_id)
    }
}
