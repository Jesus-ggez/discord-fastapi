from dotenv import load_dotenv
from fastapi import FastAPI

import os


from routes.users import users_router
from src.middlewares import (
    create_basic_middlewares,
    create_rate_limiting,
)


load_dotenv()
app: FastAPI = FastAPI()

# security
if not os.environ.get('test', ''):
    create_basic_middlewares(app=app)
    create_rate_limiting(app=app)


app.include_router(router=users_router)


if __name__ == '__main__':
    from uvicorn import run

    run(
        app=app,
        port=8000,
    )
