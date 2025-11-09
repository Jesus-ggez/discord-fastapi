use pyo3::prelude::*;

mod i_req_iden;
mod sql_conf;
mod structs;

use structs::UsersDb;

#[pymodule]
fn users_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<ReqIdDb>()?;

    Ok(())
}
