use sea_query::{Expr, Query};

use crate::basic_sql::sea_query_utils::Users;
use crate::constants::{PoolEngine, Record, QUERY_ENGINE};

// def set(self, target: str, data: User) -> None: ...
pub async fn update_or_err(target: String, data: Record, pool: &PoolEngine) -> sqlx::Result<()> {
    let sql: String = Query::update()
        .table(Users::Table)
        .values([
            (Users::Password, data.0.into()),
            (Users::Email, data.1.into()),
            (Users::Name, data.2.into()),
        ])
        .and_where(Expr::col(Users::Id).eq(Expr::val(target)))
        .to_string(QUERY_ENGINE);

    sqlx::query(&sql).execute(pool).await?;
    Ok(())
}
