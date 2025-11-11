from logging import Logger
from nacl import pwhash
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
from src.model import ModUser
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


    def endpoint(self, user: ModUser, iden: str, req_iden: str = Depends(get_reqwest_id)) -> dict: # type: ignore
        old_user: Result = self.__get_old_user(iden=iden)

        if old_user.is_err():
            self.__logger.warning(
                'pyo3-maturin || sqlx-sea_query panic:  %s',
                old_user.error,
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error',
            )

        if old_user.value is None:
            self.__logger.info(
                'suspicious entry, value: %s, req_iden: %s',
                iden,
                req_iden,
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User not found',
            )

        update_user: dict = self.__create_update_user(
            new=user.model_dump(),
            old=old_user.value,
        )

        if ( err := self.__update_record(
            data=update_user,
            iden=iden,
        ) ).is_err():
            self.__logger.warning(
                'pyo3-maturin || sqlx-sea_query panic:  %s',
                err.error,
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error',
            )

        update_user.update(
            {
                'target': iden,
            }
        )

        return update_user


    @safe_exec
    def __get_old_user(self, iden: str) -> Any:
        return self.__database.get(target=iden)


    def __create_update_user(self, old: tuple, new: dict) -> dict:
        password: str = old[0]

        if ( psw := new.get('password') ): # exists psw only
            password = pwhash.str(
                psw.encode(),
            ).decode()

        return {
            'email': new.get('email', old[1]),
            'name': new.get('email', old[2]),
            'password': password,
        }


    @safe_exec
    def __update_record(self, data: dict, iden: str) -> Any:
        return self.__database.set(
            target=iden,
            data=(
                data['email'],
                data['name'],
                data['password'],
            ),
        )
