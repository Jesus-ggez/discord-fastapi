use pyo3::prelude::*;

/*
 * in a near future add a:
 * - simple testing
 * - best error handlers
 */

mod basic_sql;
mod constants;
mod i_users;
mod logic;
mod structs;

use structs::UsersDb;

#[pymodule]
fn users_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<UsersDb>()?;
    Ok(())
}
