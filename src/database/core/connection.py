from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker
    )


SessionFactoryType = async_sessionmaker[AsyncSession]


def create_engine(url_obj: URL | str) -> AsyncEngine:
    return create_async_engine(url_obj)


def create_async_session_maker(engine: AsyncEngine) -> SessionFactoryType:
    return async_sessionmaker(engine, class_=AsyncSession)
