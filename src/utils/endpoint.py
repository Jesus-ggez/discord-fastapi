from fastapi import APIRouter, Depends
from typing import Any


class EndPoint:
    def __init__(
        self,
        app: APIRouter,
        method: str = 'get',
        route: str = '/',
    ) -> None:
        self._method: str = method
        self._app: APIRouter = app
        self._route: str = route

        self._middlewares: list = []


    def endpoint(self) -> Any:
        """ Override for logic """
        ...


    def build(self) -> None:
        self._app.add_api_route(
            path=self._route,
            endpoint=self.endpoint,
            methods=[self._method.upper()],
            dependencies=[Depends(m) for m in self._middlewares],
        )


    def add_middleware(self, items: list) -> None:
        self._middlewares.extend(items)

