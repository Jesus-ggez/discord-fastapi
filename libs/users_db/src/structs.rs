use pyo3::pyclass;
use tokio::runtime::Runtime;

use crate::sql_conf::PoolEngine;

/// this is a main import of structs
/// is more flexible to order and develop
/// if you dont have a full struct of schema
#[pyclass]
pub struct UsersDb {
    pub pool: PoolEngine,
    pub sync: Runtime,
}
