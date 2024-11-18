from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.internal.routers import PostsRouter
from app.core.common import BaseServer, BaseRouter


class FastAPIServer(BaseServer):
    __app: FastAPI = FastAPI()
    __routers: list[type[BaseRouter]] = [
        PostsRouter,
    ]

    def _add_routes(self):
        for router in self.__routers:
            self.__app.include_router(router.get_routers())

    def _add_cors(self):
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    async def run(self):
        self._add_cors()
        self._add_routes()
        config = uvicorn.Config(
            self.__app,
            host=settings.API_HOST,
            port=settings.API_PORT,
            log_level=settings.LOG_LEVEL.lower(),
            reload=True,
        )
        server = uvicorn.Server(config)
        await server.serve()
