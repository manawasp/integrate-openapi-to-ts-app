"""
routes.errors
~~~~~~~~~~~~~~~~~~~~~~~

All routes related to recipe resources.
"""

from fastapi import (
    APIRouter,
    Response,
)

from routers.schemas.base import ERROR_RESPONSES

router = APIRouter(tags=["custom"])


@router.get(
    "/not_found",
    name="custom not found",
    status_code=404,
    responses={"404": ERROR_RESPONSES[404]},
)
async def get_not_found():
    """Returns a not found response"""
    return Response(status_code=404)


@router.get(
    "/unauthorized",
    name="custom unauthorized",
    status_code=401,
    responses={"401": ERROR_RESPONSES[401]},
)
async def patch_recipe():
    """Returns a unauthorized response"""
    return Response(status_code=401)
