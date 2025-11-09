use dotenvy::dotenv;
use std::env;

use sea_query::{ColumnDef, Expr, Iden, SqliteQueryBuilder, Table};

// dev, change to pgsql
use sqlx::{Pool, Sqlite, SqlitePool};

/// QUERY_ENGINE is a simple alias to move at SqliteQueryBuilder to PGQueryBuilder
pub const QUERY_ENGINE: SqliteQueryBuilder = SqliteQueryBuilder;

/// PoolEngine is a simple alias to move at Sql engines, ez change from Sqlite to pgsql
pub type PoolEngine = Pool<Sqlite>;

/// basic struct of Table, is possible renamed UsersTable to Users but
/// it exists this way for simplicity
#[derive(Iden)]
pub enum UsersTable {
    Id,
    Table,
    Name,
    Password,
    Email,
    CreatedAt,
}

/// not continue if not exists DATABASE_URL
fn get_database_url() -> String {
    env::var("DATABASE_URL").unwrap_or_else(|_| {
        eprint!("Missing `DATABASE_URL` and not found");
        std::process::exit(1)
    })
}

/// this fn not use custom handler errs here, is for simplicity
/// and compatibility with pyo3 and maturin
/// but is possible convert sqlx::Error to simple error
/// and convert signature to
/// `Result<PoolEngine, String>`
/// which is compatible with pyo3
pub async fn get_pool() -> Result<PoolEngine, sqlx::Error> {
    dotenv().ok();
    SqlitePool::connect(&get_database_url()).await
}

pub async fn init_database(pool: &PoolEngine) {
    // i refuse to write sql manually
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

    sqlx::query(&sql).execute(pool).await.unwrap_or_else(|_| {
        eprint!("Error initiaizing the database");
        std::process::exit(1)
    });
}
