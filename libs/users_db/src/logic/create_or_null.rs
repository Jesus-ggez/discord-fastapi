use sea_query::Query;
use uuid::Uuid;

use crate::basic_sql::sea_query_utils::Users;
use crate::constants::{PoolEngine, Record, QUERY_ENGINE};

pub async fn create_or_null(data: Record, pool: &PoolEngine) -> sqlx::Result<Option<String>> {
    let iden: String = Uuid::new_v4().to_string();
    let sql: String = Query::insert()
        .into_table(Users::Table)
        .columns([Users::Id, Users::Password, Users::Email, Users::Name])
        .values_panic([
            iden.clone().into(),
            data.0.into(),
            data.1.into(),
            data.2.into(),
        ])
        .to_string(QUERY_ENGINE);

    sqlx::query(&sql).execute(pool).await?;

    return Ok(Some(iden));
}
