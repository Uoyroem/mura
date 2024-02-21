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
    email: str = sqlalchemy.orm.mapped_column(sqlalchemy.String(512))
    password_hash: str
