use std::env;

use dotenvy::dotenv;

use sea_query::{ColumnDef, Expr, Iden, SqliteQueryBuilder, Table};

// dev
use sqlx::{Pool, Sqlite, SqlitePool};

// pub const QUERY_ENGINE: SqliteQueryBuilder = SqliteQueryBuilder;
pub const QUERY_ENGINE: SqliteQueryBuilder = SqliteQueryBuilder;
pub type PoolEngine = Pool<Sqlite>;

#[derive(Iden)]
pub enum UsersTable {
    Id,
    Table,
    Name,
    Password,
    Email,
    CreatedAt,
}

pub async fn get_pool() -> Result<PoolEngine, sqlx::Error> {
    dotenv().ok();
    let DATABASE_URL = &env::var("DATABASE_URL").unwrap();
    SqlitePool::connect(DATABASE_URL).await
}

pub async fn init_database(pool: &PoolEngine) {
    let sql: String = Table::create()
        .table(UsersTable::Table)
        .if_not_exists()
        .col(ColumnDef::new(UsersTable::Password).text().not_null())
        .col(ColumnDef::new(UsersTable::Name).text().not_null())
        .col(
            ColumnDef::new(UsersTable::Id)
                .text()
                .unique_key()
                .not_null()
                .primary_key(),
        )
        .col(
            ColumnDef::new(UsersTable::Email)
                .text()
                .unique_key()
                .not_null(),
        )
        .col(
            ColumnDef::new(UsersTable::CreatedAt)
                .text()
                .not_null()
                .default(Expr::current_timestamp()),
        )
        .to_string(QUERY_ENGINE);

    sqlx::query(&sql).execute(pool).await.unwrap();
}
