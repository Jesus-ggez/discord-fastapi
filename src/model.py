from typing import Annotated, Optional
from pydantic import (
    StringConstraints,
    BaseModel,
    EmailStr,
)


from .validators import is_valid_password


# exists only here for use in this unique context
MAX_LEN_PASSWORD: int = 64
MIN_LEN_PASSWORD: int = 8
MAX_LEN_NAME: int = 128
MIN_LEN_NAME: int = 3

NameStr = Annotated[str, StringConstraints(
    max_length=MAX_LEN_NAME,
    min_length=MIN_LEN_NAME,
    strip_whitespace=True,
    strict=True,
)]

PasswordStr = Annotated[str, StringConstraints(
    max_length=MAX_LEN_PASSWORD,
    min_length=MIN_LEN_PASSWORD,
    strip_whitespace=True,
    strict=True,
), is_valid_password]

EmailStrClean = Annotated[str, StringConstraints(
    strip_whitespace=True,
    strict=True,
), EmailStr]


class User(BaseModel):
    name: NameStr
    password: PasswordStr
    email: EmailStrClean


class ModUser(BaseModel):
    name: Optional[NameStr] = None
    password: Optional[PasswordStr] = None
    email: Optional[EmailStrClean] = None
