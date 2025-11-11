use sea_query::{ColumnDef, Expr, Table};

use crate::constants::{PoolEngine, QUERY_ENGINE};

pub mod sea_query_utils {
    use sea_query::Iden;

    #[derive(Iden)]
    pub enum Users {
        Id,
        Table,
        Name,
        Password,
        Email,
        CreatedAt,
    }
}

pub async fn init_database_or_exit(pool: &PoolEngine) {
    use crate::basic_sql::sea_query_utils::Users;
    let sql: String = Table::create()
        .table(Users::Table)
        .if_not_exists()
        .col(ColumnDef::new(Users::Password).text().not_null())
        .col(ColumnDef::new(Users::Name).text().not_null())
        .col(
            ColumnDef::new(Users::Id)
                .text()
                .unique_key()
                .not_null()
                .primary_key(),
        )
        .col(ColumnDef::new(Users::Email).text().unique_key().not_null())
        .col(
            ColumnDef::new(Users::CreatedAt)
                .text()
                .not_null()
                .default(Expr::current_timestamp()),
        )
        .to_string(QUERY_ENGINE);

    sqlx::query(&sql).execute(pool).await.unwrap_or_else(|_| {
        eprint!("Error initiaizing the database");
        std::process::exit(1)
    });
}
