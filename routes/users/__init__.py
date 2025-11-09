from fastapi import APIRouter


# ¿?
from users_db import UsersDb


from .create import CreateUser


# add more configs after
# as middlewares
# as utilities
# pyrefly linting
# etc
USERS_DB: UsersDb = UsersDb()
users_router: APIRouter = APIRouter(
    prefix='/users',
    # more configs in future updates
)


CreateUser(
    app=users_router,
    database=USERS_DB,
).build()

# future impl
# ReaderUser().build()
# ModifierUser().build()
# DeleterUser().build()
