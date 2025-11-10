from logging import Logger
from typing import Any
from fastapi import (
    HTTPException,
    APIRouter,
    Depends,
    status,
)


# ¿?
from users_db import UsersDb


from src.middlewares.traceback_mw import get_reqwest_id
from src.model import User
from src.utils import (
    safe_exec,
    EndPoint,
    Result,
)


class Reader(EndPoint):
    def __init__(
        self,
        database: UsersDb,
        logger: Logger,
        app: APIRouter,
    ) -> None:
        self.__database: UsersDb = database
        self.__logger: Logger = logger

        super().__init__(
            method='get',
            app=app,
        )


    def endpoint(self, iden: str, req_iden: str = Depends(get_reqwest_id)) -> User: # type: ignore
        user: Result = self.__get_record(iden=iden)

        if user.is_err():
            self.__logger.warning(
                'pyo3-maturin || sqlx-sea_query panic:  %s',
                user.error,
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error',
            )

        if user.value is None:
            self.__logger.info(
                'suspicious entry, value: %s, req_iden: %s',
                iden,
                req_iden,
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='User not found',
            )

        data: tuple = user.value
        return User(
            password=data[0],
            email=data[1],
            name=data[2],
        )


    @safe_exec
    def __get_record(self, iden: str) -> Any:
        return self.__database.get(target=iden)
