from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_logger
from app.core.common import BaseRouter
from app.domain.repository import PostsRepository
from app.pkg.schema import (
    GetPostsByIDSchema,
    CreatePostsSchema,
    DeletePostsByIDSchema,
    UpdatePostsSchema,
)
from app.pkg.schema.blog import GetPostsPagination
from app.pkg.session import get_async_session

# from app.pkg.utils import StaticMeta

__all__ = [
    "PostsRouter",
]

logger = get_logger()


class PostsRouter(BaseRouter):  # , metaclass=StaticMeta):
    repository: PostsRepository = PostsRepository()
    posts_router = APIRouter(prefix="/posts", tags=["Post"])

    @staticmethod
    @posts_router.get("/")
    async def get_all_posts(
        query: GetPostsPagination = Depends(),
        session: AsyncSession = Depends(get_async_session),
    ):
        result = await PostsRouter.repository.get_posts(query, session)
        if result is None:
            logger.error(f"404, posts not found with page {query.page}")
            raise HTTPException(status_code=404, detail="Posts not Found!")
        logger.info(f"Find posts with page {query.page}!")
        return result

    @staticmethod
    @posts_router.get("/{id:int}")
    async def get(
        query: GetPostsByIDSchema = Depends(),
        session: AsyncSession = Depends(get_async_session),
    ):
        result = await PostsRouter.repository.get_by_id(query, session)
        if result is None:
            logger.error(f"404, post not found with id {query.id}")
            raise HTTPException(status_code=404, detail="Post not Found!")
        logger.info(f"Find post with id {result.id} with views {result.views}!!")
        return result

    @staticmethod
    @posts_router.post("/")
    async def post(
        query: CreatePostsSchema,
        session: AsyncSession = Depends(get_async_session),
    ):
        result = await PostsRouter.repository.create(cmd=query, session=session)
        if result is None:
            logger.error(f"Find same row in base")
            raise HTTPException(status_code=400, detail="Post already exist!")
        logger.info(f"Create Post {query}")
        return result, 201

    @staticmethod
    @posts_router.delete("/{id:int}")
    async def delete(
        query: DeletePostsByIDSchema = Depends(),
        session: AsyncSession = Depends(get_async_session),
    ):
        result = await PostsRouter.repository.delete_by_id(cmd=query, session=session)
        if result is None:
            logger.error(f"404, post not found with id {query.id}")
            raise HTTPException(status_code=404, detail="Post not found!")
        logger.info(f"Delete post by id {query.id}")
        return result

    @staticmethod
    @posts_router.put("/{id:int}")
    async def put(
        query: UpdatePostsSchema = Depends(),
        session: AsyncSession = Depends(get_async_session),
    ):
        logger.info(query)
        result = await PostsRouter.repository.update_by_id(cmd=query, session=session)
        if result is None:
            logger.error(f"404, post not found with id {query.id}")
            raise HTTPException(status_code=404, detail="Post not found!")
        logger.info(f"Update Post by id {query.id}")
        return result

    @staticmethod
    def get_routers() -> APIRouter:

        return PostsRouter.posts_router
