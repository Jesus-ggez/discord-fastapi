from nacl import pwhash
from fastapi import (
    HTTPException,
    APIRouter,
    status,
)


# ¿?
from users_db import UsersDb


from src.sutil import EndPoint
from src.model import User


class CreateUser(EndPoint):
    def __init__(self, app: APIRouter, database: UsersDb) -> None:
        super().__init__(
            method='post',
            app=app,
        )
        self.__database: UsersDb = database


    def endpoint(self, user: User) -> dict: # type: ignore
        try:
            return {
                'iden': self.__database.append(
                    **self.create_secure_user(
                        user=user.model_dump()
                    )
                )
            }

        except Exception as e:
            # logging using e

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists',
            )


    def create_secure_user(self, user: dict) -> dict:
        user['password'] = pwhash.str(user['password'].encode()).hex()
        return user
