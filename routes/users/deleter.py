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
from src.utils import (
    safe_exec,
    EndPoint,
    Result,
)


class Deleter(EndPoint):
    def __init__(
        self,
        database: UsersDb,
        logger: Logger,
        app: APIRouter,
    ) -> None:
        self.__database: UsersDb = database
        self.__logger: Logger = logger

        super().__init__(
            method='delete',
            app=app,
        )


    def endpoint( # type: ignore
        self,
        iden: str,
        req_iden: str = Depends(get_reqwest_id)
    ) -> dict:
        # the iden comes from the implementation your prefer
        removed: Result = self.__remove_record(iden=iden)

        if removed.is_err():
            self.__logger.warning(
                'pyo3-maturin || sqlx-sea_query panic:  %s',
                removed.error,
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error',
            )

        if removed.value is None:
            self.__logger.warning(
                'suspicious entry, value: %s, req_iden: %s',
                iden,
                req_iden,
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='User not exists',
            )

        return {
            'message': f'User with iden: {iden} has deleted successfully',
        }


    @safe_exec
    def __remove_record(self, iden: str) -> Any:
        return self.__database.discard(target=iden)
