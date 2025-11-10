from logging import Logger
from fastapi import (
    HTTPException,
    APIRouter,
    status,
)


# ¿?
from users_db import UsersDb


from src.sutil import EndPoint
from src.model import User


class ReaderUser(EndPoint):
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


    def endpoint(self, iden: str) -> User: # type: ignore
        try:
            if user := self.__database.get_by_id(iden=iden):
                return User(
                    password=user[0],
                    email=user[1],
                    name=user[2],
                )

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='User not found',
            )

        except Exception as error:
            self.__logger.error(
                msg=f'sqlx-pyo3 Err: {error}',
            )

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Identifier invalid'
            )
