from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.core import settings

__all__ = [
    "get_async_session",
]


DATABASE_URL = (
    f"{settings.POSTGRES_DRIVER_SQLALCHEMY}://{settings.POSTGRES_USER}"
    + f":{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}"
    + f"/{settings.POSTGRES_DB}"
)
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
