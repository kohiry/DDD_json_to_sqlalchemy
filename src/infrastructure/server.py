from fastapi import FastAPI, APIRouter
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from src.core import settings
from src.api import api_v1_router
from src.domain.common import BaseServer


class FastAPIServer(BaseServer):
    __app: FastAPI = FastAPI()
    __routers: list[APIRouter] = [
        api_v1_router,
    ]

    def _add_routes(self):
        for router in self.__routers:
            self.__app.include_router(router)

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
