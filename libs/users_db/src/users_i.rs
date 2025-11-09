// built in
use std::collections::HashMap;

// dependences
use pyo3::prelude::*;
use sea_query::Query;

// local imports
use crate::init_sql::{init_database, QUERY_ENGINE};
use crate::structs::UsersDb;

#[pymethods]
impl UsersDb {
    #[new]
    fn new() -> Self {
        init_database();
        UsersDb {}
    }

    fn append(&self, user: HashMap<String, String>) -> PyResult<String> {
        let sql: String = Query::insert()
            .into_table(_)
            .columns([])
            .values([])
            .unwrap()
            .to_string(QUERY_ENGINE);
        Ok("".into())
    }
}
