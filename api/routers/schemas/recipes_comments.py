"""
routes.schemas.recipes_comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All validation and response schemas related to recipes comments.
"""

from typing import (
    List,
    Optional,
)

from fastapi import Query
from pydantic import (
    BaseModel
)

from routers.schemas.base import (
    ListGenericResponse,
)

# partial schemas


class RecipeComment(BaseModel):
    id: int
    message: str


# input


class ListRecipesCommentsQuery(BaseModel):
    def __init__(
        self,
        ob: Optional[str] = Query(
            "-created_at",
            min=1,
            min_length=1,
            title="Field(s) to order by, comma separated, "
            'prefixed with "-" for descending search',
            example="-created_at",
        ),
        s: Optional[str] = Query(
            None,
            min_length=1,
            title="Optional search value (partial search)",
            example="some value",
        ),  # noqa: E741
        sf: Optional[str] = Query(
            "name,description",
            min_length=1,
            title="Field(s) to filter on, comma separated",
            example="name,description",
        ),
        l: Optional[int] = Query(  # noqa: E741
            20,
            min=5,
            max=200,
            title="Maximum number of items to return",
            example="20",  # noqa: E741
        ),
        p: Optional[int] = Query(1, min=1, title="Current page number", example="1"),
        **kwargs
    ):
        super().__init__(ob, s, sf, l, p, **kwargs)  # type: ignore


class PostRecipeCommentPayload(BaseModel):
    name: str


class PatchRecipeCommentPayload(BaseModel):
    name: str


# output


class ListRecipesComments(ListGenericResponse):
    objects: List[RecipeComment]

    class Config:
        # to read the data even if it is not a dict but an orm model
        orm_mode = True
