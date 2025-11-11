use sea_query::{Expr, Query};

use crate::basic_sql::sea_query_utils::Users;
use crate::constants::{PoolEngine, QUERY_ENGINE};

pub async fn discard_or_null(target: String, pool: &PoolEngine) -> sqlx::Result<Option<String>> {
    let sql: String = Query::delete()
        .from_table(Users::Table)
        .and_where(Expr::col(Users::Id).eq(Expr::val(target.clone())))
        .to_string(QUERY_ENGINE);

    dbg!(sql.clone());
    let res = sqlx::query(&sql).execute(pool).await?;

    if res.rows_affected() != 0 {
        return Ok(Some(target));
    }
    Ok(None)
}
