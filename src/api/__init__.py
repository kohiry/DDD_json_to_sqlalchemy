from fastapi import APIRouter

from src.api.v1.endpoints.tariffs import tariff_router

api_v1_router = APIRouter(prefix='/api/v1')
api_v1_router.include_router(tariff_router)
__all__ = [
    "api_v1_router",
]