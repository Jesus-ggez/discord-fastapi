use std::collections::HashMap;

use pyo3::prelude::*;

#[pyclass]
pub struct UsersDb {}

#[pymethods]
impl UsersDb {
    fn append(&self, user: HashMap<String, String>) -> PyResult<String> {
        Ok("".into())
    }
}
