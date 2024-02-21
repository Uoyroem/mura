import os
import pathlib
import typing
from dotenv import load_dotenv

PROJECT_DIRECTORY: pathlib.Path = pathlib.Path(__file__).parent.parent
load_dotenv(PROJECT_DIRECTORY / ".env", override=True)
DEBUG: typing.Final[bool] = os.getenv("DEBUG", "false").lower() == "true"
SQLALCHEMY_URL: typing.Final[str] = os.getenv("SQLALCHEMY_URL", "sqlite+aiosqlite:///mura.sqlite3")
print(SQLALCHEMY_URL)