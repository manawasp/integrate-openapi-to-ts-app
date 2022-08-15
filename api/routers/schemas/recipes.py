"""
routes.schemas.recipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All validation and response schemas related to recipes.
"""

from typing import (
    List,
    Optional,
)

from fastapi import Query
from pydantic import (
    BaseModel,
    Field,
)

from routers.schemas.base import (
    ListGenericResponse,
)

# partial schemas


class Recipe(BaseModel):
    id: int
    name: str

    class Config:
        use_enum_values = True


# input


class ListRecipesQuery:
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
            "name",
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


class PostRecipePayload(BaseModel):
    name: str

    class Config:
        use_enum_values = True


class PatchRecipePayload(BaseModel):
    name: str

    class Config:
        use_enum_values = True


# output


class ListRecipes(ListGenericResponse):
    recipes: List[Recipe]

    class Config:
        # to read the data even if it is not a dict but an orm model
        orm_mode = True
