"""
routes.recipes
~~~~~~~~~~~~~~~~~~~~~~~

All routes related to recipe resources.
"""

from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response,
)

from routers.schemas.base import ERROR_RESPONSES
from routers.schemas.recipes import (
    ListRecipesQuery,
    ListRecipes,
    PatchRecipePayload,
    PostRecipePayload,
    Recipe,
)

router = APIRouter(
    prefix="/recipes", tags=["recipes"], responses={"403": ERROR_RESPONSES[403]}
)


@router.get(
    "/",
    name="recipes list",
    status_code=200,
    response_model=ListRecipes,
)
async def get_recipes(
    request: Request,
    query: ListRecipesQuery = Depends(ListRecipesQuery),
):
    """Lists all recipes"""
    return {"meta": {"total": 2}, "recipes": []}


@router.post(
    "/",
    name="recipes create",
    status_code=201,
    response_model=Recipe,
)
async def post_rreccipe(
    request: Request,
    payload: PostRecipePayload,
):
    """Creates a new recipe."""
    return Response(status_code=204)


@router.get(
    "/{recipe_id}",
    name="recipes retrieve",
    status_code=200,
    response_model=Recipe,
    responses={"404": ERROR_RESPONSES[404]},
)
async def get_recipe(
    request: Request,
    recipe_id: int,
):
    """Gets a specific recipe's information."""
    return Response(status_code=204)


@router.patch(
    "/{recipe_id}",
    name="recipes update",
    status_code=200,
    response_model=Recipe,
    responses={
        "409": ERROR_RESPONSES[409],
        "404": ERROR_RESPONSES[404],
    },
)
async def patch_recipe(
    request: Request,
    recipe_id: int,
    payload: PatchRecipePayload,
):
    """Updates a recipe."""
    return Response(status_code=204)


@router.delete(
    "/{recipe_id}",
    name="recipes delete",
    status_code=200,
    response_model=None,
    responses={"404": ERROR_RESPONSES[404]},
)
async def delete_recipe(
    request: Request,
    recipe_id: int,
):
    """Deletes a recipe."""
    return Response(status_code=204)
