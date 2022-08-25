"""
routes.recipes
~~~~~~~~~~~~~~~~~~~~~~~

All routes related to recipe resources.
"""

from random import randrange
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
    tags=["recipes"],
    responses={"403": ERROR_RESPONSES[403]}
)


@router.get(
    "/recipes",
    name="recipes list",
    status_code=200,
    response_model=ListRecipes,
)
async def get_recipes(
    request: Request,
    query: ListRecipesQuery = Depends(ListRecipesQuery),
):
    """Lists all recipes"""
    return {
        "meta": {"total": 2},
        "recipes": [
            {"id": 1, "name": "Bavarois aux fraises"},
            {"id": 2, "name": "Clafoutis aux poires"}
        ]
    }


@router.post(
    "/recipes",
    name="recipes create",
    status_code=201,
    response_model=Recipe,
)
async def post_recipe(
    request: Request,
    payload: PostRecipePayload,
):
    """Creates a new recipe."""
    return {"id": randrange(2, 100), "name": payload.name}


@router.get(
    "/recipes/{recipe_id}",
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
    return {"id": 1, "name": "Bavarois aux fraises"}


@router.patch(
    "/recipes/{recipe_id}",
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
    return {"id": 1, "name": "Bavarois aux fraises"}


@router.delete(
    "/recipes/{recipe_id}",
    name="recipes delete",
    status_code=204,
    responses={"404": ERROR_RESPONSES[404]},
)
async def delete_recipe(
    request: Request,
    recipe_id: int,
):
    """Deletes a recipe."""
    return Response(status_code=204)
