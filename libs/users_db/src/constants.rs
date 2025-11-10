use dotenvy::dotenv;
use sea_query::SqliteQueryBuilder;
use sqlx::{Pool, Sqlite, SqlitePool};
use std::env;

pub const QUERY_ENGINE: SqliteQueryBuilder = SqliteQueryBuilder;
pub type PoolEngine = Pool<Sqlite>;
pub type Record = (String, String, String);

fn get_database_url_or_exit() -> String {
    env::var("DATABASE_URL").unwrap_or_else(|_| {
        eprint!("Missing `DATABASE_URL` and not found");
        std::process::exit(1)
    })
}

pub async fn get_pool() -> Result<PoolEngine, sqlx::Error> {
    dotenv().ok();
    SqlitePool::connect(&get_database_url_or_exit()).await
}
