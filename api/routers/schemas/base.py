"""
routes.schemas.base
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generic validation and response schemas.
"""
from collections import namedtuple
from typing import Optional

from fastapi import Query
from pydantic import (
    BaseModel,
    Field,
)

# inputs


class ListGenericQuery(BaseModel):
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


# outputs


class ListMetaResponse(BaseModel):
    total: int = Field(
        ...,
        title="Total number of available resources",
        example=260,
    )


class ListGenericResponse(BaseModel):
    meta: ListMetaResponse


class GenericHttpError(BaseModel):
    detail: str


ERROR_RESPONSES = {
    400: {"model": GenericHttpError, "description": "validation error"},
    401: {"model": GenericHttpError, "description": "unauthorized"},
    403: {"model": GenericHttpError, "description": "not enough privileges"},
    404: {"model": GenericHttpError, "description": "item not found"},
    409: {"model": GenericHttpError, "description": "violation of unique constraint"},
}
