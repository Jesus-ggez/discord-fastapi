use std::env;

use dotenvy::dotenv;
use sea_query::{ColumnDef, Iden, SqliteQueryBuilder, Table};
use sqlx::{Connection, SqliteConnection};

pub const QUERY_ENGINE: SqliteQueryBuilder = SqliteQueryBuilder;

#[derive(Iden)]
pub enum UsersTable {
    Id,
    Table,
    Name,
    Password,
    Email,
}

pub async fn get_pool() -> SqliteConnection {
    dotenv().ok();

    let database_url: String = env::var("DATABASE_URL").unwrap();
    SqliteConnection::connect(database_url).await
}

pub async fn init_database() {
    let pool = get_pool().await;
    let sql: String = Table::create()
        .table(UsersTable::Table)
        .if_not_exists()
        .col(ColumnDef::new(UsersTable::Password).string().not_null())
        .col(ColumnDef::new(UsersTable::Name).string().not_null())
        .col(
            ColumnDef::new(UsersTable::Id)
                .string()
                .unique_key()
                .not_null()
                .primary_key(),
        )
        .col(
            ColumnDef::new(UsersTable::Email)
                .string()
                .unique_key()
                .not_null(),
        )
        .to_string(QUERY_ENGINE);

    sqlx::query(&sql).execute(&pool).await?;
}
