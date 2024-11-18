import json
from asyncio import gather

from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import get_logger

__all__ = [
    "tariff_router",
]
from src.domain.repository.tariff_repo import TariffRepository
from src.domain.schema import CreateTariffSchema
from src.infrastructure.database.session import get_async_session
from src.services.tariff_service import cast_from_json_to_schema

logger = get_logger()
repository: TariffRepository = TariffRepository()
tariff_router = APIRouter(prefix="/traffic", tags=["Traffic"])


@tariff_router.post("/")  # в идеале написать это как воркер, с брокером сообщений
async def post(
        file: UploadFile = File(...),
        session: AsyncSession = Depends(get_async_session),
):
    """
        Если бы я делал через брокер сообщений паттерн простой:
            1) тут я буду сохранять файл в контейнере с прокинутым volume
            2) и отправлять сообщение на его обработку
            3) на ручке просто верну "Ok", либо намутить уведомления через websocket
            4) когда worker получивший сообщение от брокера,
                обработает файл, отправлю уведомление
    """

    try:
        content = await file.read()
        data = json.loads(content)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid JSON")
    try:
        validated_data = cast_from_json_to_schema(data)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
    await repository.create(validated_data, session)
    return {'status': 'ok'}

#
# @posts_router.get("/")
# async def get_all(
#     query: GetPostsPagination = Depends(),
#     session: AsyncSession = Depends(get_async_session),
# ):
#     result = await repository.get_posts(query, session)
#     if result is None:
#         logger.error(f"404, posts not found with page {query.page}")
#         raise HTTPException(status_code=404, detail="Posts not Found!")
#     logger.info(f"Find posts with page {query.page}!")
#     return result
#
# @posts_router.get("/{id:int}")
# async def get(
#     query: GetPostsByIDSchema = Depends(),
#     session: AsyncSession = Depends(get_async_session),
# ):
#     result = await repository.get_by_id(query, session)
#     if result is None:
#         logger.error(f"404, post not found with id {query.id}")
#         raise HTTPException(status_code=404, detail="Post not Found!")
#     logger.info(f"Find post with id {result.id} with views {result.views}!!")
#     return result

#
# @posts_router.delete("/{id:int}")
# async def delete(
#     query: DeletePostsByIDSchema = Depends(),
#     session: AsyncSession = Depends(get_async_session),
# ):
#     result = await repository.delete_by_id(cmd=query, session=session)
#     if result is None:
#         logger.error(f"404, post not found with id {query.id}")
#         raise HTTPException(status_code=404, detail="Post not found!")
#     logger.info(f"Delete post by id {query.id}")
#     return result
#
# @posts_router.put("/{id:int}")
# async def put(
#     query: UpdatePostsSchema = Depends(),
#     session: AsyncSession = Depends(get_async_session),
# ):
#     logger.info(query)
#     result = await repository.update_by_id(cmd=query, session=session)
#     if result is None:
#         logger.error(f"404, post not found with id {query.id}")
#         raise HTTPException(status_code=404, detail="Post not found!")
#     logger.info(f"Update Post by id {query.id}")
#     return result
#
#
# @posts_router.post('/calculate')
# def calculate():
#     query = Depends(),
#     session: AsyncSession = Depends(get_async_session),
# )
#
