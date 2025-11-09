from fastapi import APIRouter, FastAPI


# ¿?
from users_db import UsersDb


from users import CreateUser

USERS_DB: UsersDb = UsersDb()


app: FastAPI = FastAPI()

users_router: APIRouter = APIRouter(
    prefix='/users'
)


CreateUser(
    app=users_router,
    database=USERS_DB,
).build()


app.include_router(router=users_router)


if __name__ == '__main__':
    from uvicorn import run

    run(
        app=app,
        port=8000,
    )
