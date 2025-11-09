use pyo3::prelude::*;

mod i_users;
mod sql_conf;
mod structs;

use structs::UsersDb;

#[pymodule]
fn users_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<UsersDb>()?;

    Ok(())
}
