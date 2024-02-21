import typing

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


async def user(token: typing.Annotated[str, Depends(oauth2_scheme)]):
    pass
