use pyo3::prelude::*;

/*
 * in a near future add a:
 * - simple testing
 * - auto contians actions
 * - more documentation
 * - best error handlers
 * - optimizations for legibility
 * - best appointment (google translate) of functions, classes/structs and documents
 * - best use of types
 */

// i will not use sql directly or manually
mod i_users;
mod sql_conf;
mod structs;

// unique import area
use structs::UsersDb;

#[pymodule]
fn users_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<UsersDb>()?;
    // more extension of classes, LogginDb, AdminDb, SemiAdminDb, etc
    // but if add all classes here this function name must be changed
    // to coherent name for this parts:
    // [lib] name = need changes
    // [package] name = need changes
    // {name}/... where name == users_db = need changes
    // #[pymodule] fn {name} = need changes

    Ok(())
}
