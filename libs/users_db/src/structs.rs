use pyo3::prelude::*;
use tokio::runtime::Runtime;

use crate::constants::PoolEngine;

#[pyclass]
pub struct UsersDb {
    pub pool: PoolEngine,
    pub rt_sync: Runtime,
}
