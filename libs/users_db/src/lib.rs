use pyo3::prelude::*;

mod init_sql;
mod structs;
mod users_i;

use structs::UsersDb;

#[pymodule]
fn users_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<UsersDb>()?;

    Ok(())
}
