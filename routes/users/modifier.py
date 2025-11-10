from logging import Logger
from typing import Any
from fastapi import (
    HTTPException,
    APIRouter,
    status,
)


# ¿?
from users_db import UsersDb


from src.model import User
from src.utils import (
    safe_exec,
    EndPoint,
    Result,
)


class Modifier(EndPoint):
    def __init__(
        self,
        database: UsersDb,
        logger: Logger,
        app: APIRouter,
    ) -> None:
        self.__database: UsersDb = database
        self.__logger: Logger = logger

        super().__init__(
            method='put',
            app=app,
        )


    def endpoint(self, user: User, iden: str) -> User: # type: ignore
        ...
