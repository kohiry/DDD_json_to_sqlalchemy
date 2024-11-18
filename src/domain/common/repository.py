from abc import ABCMeta, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.common import BaseSchema


__all__ = [
    "BaseRepository",
]

from app.core.common.model import BaseModel


class BaseRepository(metaclass=ABCMeta):
    """Abstract class of pattern repository."""

    @abstractmethod
    async def get_by_id(
        self, query: BaseSchema, session: AsyncSession
    ) -> BaseSchema | None:
        """Abstract method for getting by name."""
        pass

    @abstractmethod
    async def _check_exist_by_id(
        self,
        query: BaseSchema,
        session: AsyncSession,
    ) -> BaseModel | None:
        pass

    @abstractmethod
    async def create(
        self,
        cmd: BaseSchema,
        session: AsyncSession,
    ) -> BaseSchema | None:
        """Abstract method for create entity."""
        pass

    @abstractmethod
    async def delete_by_id(
        self,
        cmd: BaseSchema,
        session: AsyncSession,
    ) -> BaseSchema | None:
        """Abstract method for delete entity."""
        pass

    @abstractmethod
    async def update_by_id(
        self,
        cmd: BaseSchema,
        session: AsyncSession,
    ) -> BaseSchema | None:
        """Abstract method for update entity."""
        pass
