use sea_query::{Expr, Query};

use crate::basic_sql::sea_query_utils::Users;
use crate::constants::{PoolEngine, Record, QUERY_ENGINE};

pub async fn get_or_null(target: String, pool: &PoolEngine) -> sqlx::Result<Option<Record>> {
    let sql: String = Query::select()
        .from(Users::Table)
        .and_where(Expr::col(Users::Id).eq(Expr::val(target)))
        .to_string(QUERY_ENGINE);

    let data: Option<(String, String, String)> = sqlx::query_as::<_, Record>(&sql)
        .fetch_optional(pool)
        .await?;

    Ok(data)
}
