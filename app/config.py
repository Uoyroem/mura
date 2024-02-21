import os
import typing
from dotenv import load_dotenv
load_dotenv()

DEBUG: typing.Final[bool] = os.getenv("DEBUG", "false").lower() == "true"
SQLALCHEMY_URL: typing.Final[str] = os.getenv("SQLALCHEMY_URL", "mura.sqlite3")
