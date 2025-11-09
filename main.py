from fastapi import APIRouter, FastAPI


from users import CreateUser


app: FastAPI = FastAPI()

users_router: APIRouter = APIRouter(
    prefix='/users'
)


CreateUser(app=users_router).build()


app.include_router(router=users_router)


if __name__ == '__main__':
    from uvicorn import run

    run(
        app=app,
        port=8000,
    )
