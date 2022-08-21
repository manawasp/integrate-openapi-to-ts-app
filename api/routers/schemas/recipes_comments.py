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


class ListRecipesCommentsQuery:
    def __init__(
        self,
        ob: str = Query(
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
        sf: str = Query(
            "name,description",
            min_length=1,
            title="Field(s) to filter on, comma separated",
            example="name,description",
        ),
        l: int = Query(  # noqa: E741
            20,
            min=5,
            max=200,
            title="Maximum number of items to return",
            example="20",  # noqa: E741
        ),
        p: int = Query(1, min=1, title="Current page number", example="1"),
    ):
        self.order_by = ob.split(",")
        self.limit = l
        self.page = p
        self.search = {column: s for column in sf.split(",")} if s is not None else {}

    def dict(self):
        """Dict representation of the current class."""
        return self.__dict__


class PostRecipeCommentPayload(BaseModel):
    message: str


class PatchRecipeCommentPayload(BaseModel):
    message: str


# output


class ListRecipesComments(ListGenericResponse):
    comments: List[RecipeComment]

    class Config:
        # to read the data even if it is not a dict but an orm model
        orm_mode = True
