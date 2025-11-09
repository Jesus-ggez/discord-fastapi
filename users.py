from fastapi import APIRouter, HTTPException
from nacl import pwhash


# ¿?
from users_db import UsersDb


from sutil import EndPoint
from model import User


class CreateUser(EndPoint):
    def __init__(self, app: APIRouter, database: UsersDb) -> None:
        super().__init__(
            method='post',
            app=app,
        )
        self.__database: UsersDb = database


    def endpoint(self, user: User) -> dict: # type: ignore

        try:
            user_db: dict = user.model_dump()
            user_db['password'] = pwhash.str(user_db['password'].encode()).hex()

            return {
                'iden': self.__database.append(
                    **user_db,
                )
            }

        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=404,
                detail='User already exists',
            )
