from logging import Logger
from nacl import pwhash
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


class CreateUser(EndPoint):
    def __init__(
        self,
        database: UsersDb,
        logger: Logger,
        app: APIRouter,
    ) -> None:
        self.__database: UsersDb = database
        self.__logger: Logger = logger

        super().__init__(
            method='post',
            app=app,
        )


    def endpoint(self, user: User) -> dict: # type: ignore
        hashed_user: Result = self.__create_hashed_user(
            user_dict=user.model_dump(),
        )

        if hashed_user.is_err():
            self.__logger.info(
                'Hashing password detail: %s',
                hashed_user.error,
            )

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Invalid Password',
            )

        iden_res: Result[str, str] = self.__create_record(hashed_user.value)

        if iden_res.is_err():
            self.__logger.info(
                'pyo3-maturin || sqlx-sea_query panic:  %s',
                hashed_user.error,
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error',
            )

        if not iden_res.value:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists',
            )

        return {
            'id': iden_res.value
        }


    @safe_exec
    def __create_hashed_user(self, user_dict: dict) -> Any:
        psw_bytes: bytes = user_dict['password'].encode()

        user_dict['password'] = pwhash.str(psw_bytes).decode()

        return user_dict


    @safe_exec
    def __create_record(self, data: dict) -> Any:
        return self.__database.append(**data)
