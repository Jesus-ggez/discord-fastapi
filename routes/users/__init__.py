from fastapi import APIRouter

import logging


# ¿?
from users_db import UsersDb


from .modifier import Modifier
from .deleter import Deleter
from .create import Creator
from .reader import Reader


logger: logging.Logger = logging.getLogger(__name__)
USERS_DB: UsersDb = UsersDb()
users_router: APIRouter = APIRouter(
    prefix='/users',
)


creator: Creator = Creator(
    database=USERS_DB,
    app=users_router,
    logger=logger,
)
creator.build()

reader: Reader = Reader(
    database=USERS_DB,
    app=users_router,
    logger=logger,
)
reader.build()

modifier: Modifier = Modifier(
    database=USERS_DB,
    app=users_router,
    logger=logger,
)
modifier.build()

deleter: Deleter = Deleter(
    database=USERS_DB,
    app=users_router,
    logger=logger,
)
deleter.build()
