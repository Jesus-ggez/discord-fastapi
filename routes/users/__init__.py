from fastapi import APIRouter

import logging


# ¿?
from users_db import UsersDb

from src.middlewares import create_id_request
from .create import CreateUser
from .reader import ReaderUser


# add more configs after
# as utilities
# pyrefly linting
# etc
logger: logging.Logger = logging.getLogger(__name__)
USERS_DB: UsersDb = UsersDb()
users_router: APIRouter = APIRouter(
    prefix='/users',
    # more configs in future updates
)

creator: CreateUser = CreateUser(
    database=USERS_DB,
    app=users_router,
    logger=logger,
)
creator.add_middleware(
    items=[
    ]
)
creator.build()

reader: ReaderUser = ReaderUser(
    database=USERS_DB,
    app=users_router,
    logger=logger,
)
reader.build()
# ModifierUser().build()
# DeleterUser().build()
