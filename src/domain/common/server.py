from abc import ABCMeta, abstractmethod


__all__ = ["BaseServer"]

from app.core.common import BaseRouter


class BaseServer(metaclass=ABCMeta):
    """The base abstract class."""

    __app: object
    __routers: list[BaseRouter]

    @abstractmethod
    def _add_routes(self):
        """The abstract method adding all router to app."""
        pass

    @abstractmethod
    def _add_cors(self):
        """The abstract method adding middleware."""
        pass

    @abstractmethod
    async def run(self):
        """The abstract method running app."""
        pass
