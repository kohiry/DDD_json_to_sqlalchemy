from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, update

from src.core import get_logger
from src.domain.models.models import TariffModel, CargoModel
from src.domain.schema.tariffs import TariffSchema, CreateTariffSchema, GetTariffSchema

logger = get_logger()

__all__ = [
    "TariffRepository",
]


class TariffRepository:
    @staticmethod
    async def _check_exist_by_date(
        query: GetTariffSchema,
        session: AsyncSession,
    ) -> bool:
        result = await session.execute(
            select(TariffModel).where(TariffModel.date == query.date)
        )
        blog_message = result.scalar_one_or_none()
        return blog_message is not None

    async def create(
            self, cmd: list[TariffSchema], session: AsyncSession
    ) -> list[TariffSchema] | None:
        try:
            async with session.begin():
                models = []
                for tariff in cmd:
                    existing_tariff = await self._check_exist_by_date(tariff,
                                                                      session)
                    if existing_tariff:
                        continue

                    # Создаём модель для тарифа
                    model = TariffModel(
                        date=tariff.date,
                        cargos=[
                            CargoModel(cargo_type=cargo.cargo_type, rate=cargo.rate)
                            for cargo in tariff.cargos
                        ],
                    )
                    models.append(model)

                if not models:
                    return None

                session.add_all(models)

                await session.commit()

                return cmd

        except IntegrityError:
            # В случае ошибки откатываем транзакцию
            await session.rollback()
            return None

    # @staticmethod
    # async def _check_exist_by_title_content_index(
    #     query: CreatePostsSchema,
    #     session: AsyncSession,
    # ) -> PostsModel | None:
    #     result = await session.execute(
    #         select(PostsModel).where(
    #             (PostsModel.title == query.title)
    #             & (PostsModel.content == query.content)
    #         )
    #     )
    #     blog_message = result.scalar_one_or_none()
    #     if blog_message is None:
    #         return None
    #     return blog_message
    #
    # @staticmethod
    # async def get_posts(
    #     query: GetPostsPagination,
    #     session: AsyncSession,
    # ) -> GetPosts | None:
    #     offset_value = (query.page - 1) * query.page_size
    #
    #     result = await session.execute(
    #         select(PostsModel).offset(offset_value).limit(query.page_size)
    #     )
    #     posts = result.scalars().all()
    #     if posts is None:
    #         return None
    #     return GetPosts(posts=list(map(lambda x: PostsSchema.model_validate(x), posts)))
    #
    # async def get_by_id(
    #     self,
    #     query: GetPostsByIDSchema,
    #     session: AsyncSession,
    # ) -> PostsSchema | None:
    #     blog_message = await self._check_exist_by_id(query, session)
    #     if blog_message is None:
    #         return None
    #     await self._upd_views(blog_message, session)
    #     return PostsSchema.model_validate(blog_message)
    #

# v
#     async def delete_by_id(
#         self,
#         cmd: DeletePostsByIDSchema,
#         session: AsyncSession,
#     ) -> DeletePostsByIDSchema | None:
#         result_check = await self._check_exist_by_id(cmd, session)
#         if result_check is None:
#             return None
#         result = delete(PostsModel).where(PostsModel.id == cmd.id)
#         await session.execute(result)
#         await session.commit()
#         return cmd
#
#     async def update_by_id(
#         self,
#         cmd: UpdatePostsSchema,
#         session: AsyncSession,
#     ) -> GetPostsByIDSchema | None:
#         result_check = await self._check_exist_by_id(cmd, session)
#         if result_check is None:
#             return None
#         stmt = (
#             update(PostsModel)
#             .where(PostsModel.id == cmd.id)
#             .values(title=cmd.title, content=cmd.content)
#         )
#         await session.execute(stmt)
#         await session.commit()
#         return GetPostsByIDSchema.model_validate(cmd)
