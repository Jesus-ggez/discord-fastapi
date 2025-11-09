use pyo3::pyclass;
use tokio::runtime::Runtime;

use crate::sql_conf::PoolEngine;

#[pyclass]
pub struct UsersDb {
    pub pool: PoolEngine,
    pub sync: Runtime,
}
