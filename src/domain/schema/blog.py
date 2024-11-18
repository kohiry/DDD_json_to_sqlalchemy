from datetime import datetime
from typing import Annotated
from fastapi import Path, Query
from app.core.common import BaseSchema


__all__ = [
    "PostsSchema",
    "CreatePostsSchema",
    "UpdatePostsSchema",
    "BasePostsSchema",
    "GetPostsByIDSchema",
    "DeletePostsByIDSchema",
]


# Base schema for shared properties, if any are added in the future
class BasePostsSchema(BaseSchema):
    pass


class GetPostsByIDSchema(BasePostsSchema):
    id: Annotated[int, Path()]


class CreatePostsSchema(BasePostsSchema):
    title: str
    content: str


class UpdatePostsSchema(GetPostsByIDSchema, CreatePostsSchema):
    pass


class DeletePostsByIDSchema(GetPostsByIDSchema):
    pass


class PostsSchema(GetPostsByIDSchema):
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    views: int


class GetPostsPagination(BasePostsSchema):
    page: Annotated[int, Query()]
    page_size: Annotated[int, Query()]


class GetPosts(BasePostsSchema):
    posts: list[PostsSchema]
