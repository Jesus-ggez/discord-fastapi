from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from slowapi.middleware import SlowAPIASGIMiddleware
from slowapi.util import get_remote_address
from slowapi import Limiter


def create_rate_limiting(app: FastAPI) -> None:
    LIMITER: Limiter = Limiter(
        key_func=get_remote_address,
    )

    app.state.limiter = LIMITER
    app.add_middleware(SlowAPIASGIMiddleware)


def create_basic_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=['localhost'], # modify or dyn acl
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['localhost'], # modify or dyn acl
        allow_credentials=True,
        allow_methods=['POST'],
        allow_headers=['*'],
    )


def create_id_request() -> None:
    raise NotImplementedError(
        '- create a request iden',
        '- save iden in db',
        '- create header in request `req-id` or similar',
        '- return request',
    )
