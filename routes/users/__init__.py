from fastapi import APIRouter


# ¿?
from users_db import UsersDb


from .create import CreateUser


USERS_DB: UsersDb = UsersDb()
users_router: APIRouter = APIRouter(
    prefix='/users'
)


CreateUser(
    app=users_router,
    database=USERS_DB,
).build()


