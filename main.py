from fastapi import APIRouter, FastAPI


# ¿?
from users_db import UsersDb


from users import CreateUser
from middlewares import (
    create_basic_middlewares,
    create_rate_limiting,
)


app: FastAPI = FastAPI()

# security
create_basic_middlewares(app=app)
create_rate_limiting(app=app)


# separe and use in `routes/users/__init__.py` using unique router
# begin users/__init__.py
USERS_DB: UsersDb = UsersDb()
users_router: APIRouter = APIRouter(
    prefix='/users'
)

CreateUser(
    app=users_router,
    database=USERS_DB,
).build()

# end users/__init__.py
app.include_router(router=users_router)


if __name__ == '__main__':
    from uvicorn import run

    run(
        app=app,
        port=8000,
    )
