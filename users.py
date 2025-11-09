from fastapi import APIRouter


from sutil import EndPoint


class CreateUser(EndPoint):
    def __init__(self, app: APIRouter) -> None:
        super().__init__(
            method='post',
            app=app,
        )


    def endpoint(self, user: User) -> dict: # type: ignore
        ...
