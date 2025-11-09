use pyo3::prelude::*;

mod users_i;

#[pymodule]
fn users_db(m: &Bound<'_, PyModule>) -> Result<()> {
    m.add_class::<users_i::UsersDb>()?;
    Ok(())
}
