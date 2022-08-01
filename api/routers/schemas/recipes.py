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


class ListRecipesQuery(BaseModel):
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
    objects: List[Recipe]

    class Config:
        # to read the data even if it is not a dict but an orm model
        orm_mode = True
