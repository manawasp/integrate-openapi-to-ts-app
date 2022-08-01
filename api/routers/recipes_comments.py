"""
routes.recipes_comments
~~~~~~~~~~~~~~~~~~~~~~~

All routes related to recipe comment resources.
"""

from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response,
)
from routers.schemas.recipes_comments import RecipeComment
from routers.schemas.base import ERROR_RESPONSES
from routers.schemas.recipes import (
    ListRecipesQuery,
    ListRecipes,
    PatchRecipePayload,
    PostRecipePayload,
)

router = APIRouter(
    prefix="/recipes/{recipe_id}/comments",
    tags=["recipesComments"],
    responses={"403": ERROR_RESPONSES[403]},
)


@router.get(
    "/",
    name="recipes comments list",
    status_code=200,
    response_model=ListRecipes,
)
async def get_recipe_comments(
    request: Request,
    recipe_id: int,
    query: ListRecipesQuery = Depends(ListRecipesQuery),
):
    """Lists all recipe comments"""
    return {"meta": {"total": 2}, "recipes": []}


@router.post(
    "/",
    name="recipes comments create",
    status_code=201,
    response_model=RecipeComment,
)
async def post_recipe_comment(
    request: Request,
    recipe_id: int,
    payload: PostRecipePayload,
):
    """Creates a new recipe comment."""
    return Response(status_code=204)


@router.get(
    "/{comment_id}",
    name="recipes comments retrieve",
    status_code=200,
    response_model=RecipeComment,
    responses={"404": ERROR_RESPONSES[404]},
)
async def get_recipe_comment(
    request: Request,
    recipe_id: int,
    comment_id: int,
):
    """Gets a specific recipe comment's information."""
    return Response(status_code=204)


@router.patch(
    "/{comment_id}",
    name="recipes comments update",
    status_code=200,
    response_model=RecipeComment,
    responses={
        "404": ERROR_RESPONSES[404],
    },
)
async def patch_recipe_comment(
    request: Request,
    recipe_id: int,
    comment_id: int,
    payload: PatchRecipePayload,
):
    """Updates a recipe comment."""
    return Response(status_code=204)


@router.delete(
    "/{comment_id}",
    name="recipes comments delete",
    status_code=200,
    response_model=None,
    responses={"404": ERROR_RESPONSES[404]},
)
async def delete_recipe_comment(
    request: Request,
    recipe_id: int,
    comment_id: int,
    id: int,
):
    """Deletes a recipe comment."""
    return Response(status_code=204)
