from os import environ as env_vars
from dotenv import load_dotenv
from fastapi import FastAPI


from routes.users import users_router
from src.middlewares import (
    create_basic_middlewares,
    create_rate_limiting,
)


load_dotenv()
app: FastAPI = FastAPI()


# security
if not env_vars.get('test'):
    create_basic_middlewares(app=app)
    create_rate_limiting(app=app)


app.include_router(router=users_router)


if __name__ == '__main__':
    from uvicorn import run

    # impl in futures updates use of custom ssl or custom e2e using
    # curve25519, poly1315 (.?) and xsalsa20

    run(
        app=app,
        port=8000,
    )
