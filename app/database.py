import datetime

import sqlalchemy
import sqlalchemy.ext.asyncio
import sqlalchemy.orm

from . import config

async_engine = sqlalchemy.ext.asyncio.create_async_engine(
    config.SQLALCHEMY_URL, echo=True
)
AsyncSession = sqlalchemy.ext.asyncio.async_sessionmaker(async_engine)


async def get_async_session() -> sqlalchemy.ext.asyncio.AsyncSession:
    with AsyncSession() as async_session:
        return async_session


class Base(sqlalchemy.orm.DeclarativeBase, sqlalchemy.ext.asyncio.AsyncAttrs):
    pass


class User(Base):
    __tablename__ = "users"
    id: sqlalchemy.orm.Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True, autoincrement=True)
    email: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(sqlalchemy.String(512))
    password: sqlalchemy.orm.Mapped[str]
    first_name: sqlalchemy.orm.Mapped[str | None] = sqlalchemy.orm.mapped_column(sqlalchemy.String(128))
    last_name: sqlalchemy.orm.Mapped[str | None] = sqlalchemy.orm.mapped_column(sqlalchemy.String(128))
    address: sqlalchemy.orm.Mapped[str | None]
    birthday: sqlalchemy.orm.Mapped[datetime.date | None]


class Product(Base):
    __tablename__ = "products"
    id: sqlalchemy.orm.Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True, autoincrement=True)


class Book(Base):
    __tablename__ = "books"
    id: sqlalchemy.orm.Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True, autoincrement=True)

