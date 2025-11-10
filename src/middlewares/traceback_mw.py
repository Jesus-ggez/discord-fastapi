from fastapi import FastAPI, Request
from uuid import uuid4


def create_id_request(app: FastAPI) -> None:
    app.middleware('http')(create_id_request_mw)


# app.middleware ...
async def create_id_request_mw(req: Request, call_next):
    if not hasattr(req.state, 'reqwest_id'):
        req.state.reqwest_id = str(uuid4())

    response = await call_next(req)
    return response


def get_reqwest_id(req: Request) -> str:
    if not hasattr(req.state, 'reqwest_id'):
        req.state.reqwest_id = str(uuid4())

    return req.state.reqwest_id

