from abc import ABCMeta, abstractmethod
from typing import Any

from app.core.common import BaseRepository, BaseSchema

__all__ = [
    "BaseRouter",
]


class BaseRouter(metaclass=ABCMeta):
    repository: BaseRepository

    @abstractmethod
    async def get(self, query: BaseSchema, *args, **kwargs):
        pass

    @abstractmethod
    async def post(self, query: BaseSchema, *args, **kwargs):
        pass

    @abstractmethod
    async def delete(self, query: BaseSchema, *args, **kwargs):
        pass

    @abstractmethod
    async def put(self, query: BaseSchema, *args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def get_routers() -> Any:
        pass
