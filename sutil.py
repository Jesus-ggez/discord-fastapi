from fastapi import APIRouter
from typing import Any


class EndPoint:
    def __init__(self, app: APIRouter, route: str = '/', method: str = 'get') -> None:
        self._method: str = method.upper()
        self._app: APIRouter = app
        self._route: str = route
        self._middlewares: list = []


    def endpoint(self) -> Any:
        """ Override for logic """
        ...


    def _subscribe(self) -> None:
        self._app.add_api_route(
            path=self._route,
            endpoint=self.endpoint,
            methods=[self._method],
            dependencies=self._middlewares,
        )


    def add_middleware(self, items: list) -> None:
        self._middlewares.extend(items)
