from pydantic import BaseModel, StringConstraints
from validators import is_valid_password
from typing import Annotated

# exists only here for use in this unique context
MAX_LEN_PASSWORD: int = 64
MIN_LEN_PASSWORD: int = 8
MAX_LEN_NAME: int = 128
MIN_LEN_NAME: int = 3



class User(BaseModel):
    name: Annotated[str, StringConstraints(
        max_length=MAX_LEN_NAME,
        min_length=MIN_LEN_NAME,
        strip_whitespace=True,
        strict=True,
    )]
    password: Annotated[str, StringConstraints(
        max_length=MAX_LEN_PASSWORD,
        min_length=MIN_LEN_PASSWORD,
        strip_whitespace=True,
        strict=True,
    ), is_valid_password]
