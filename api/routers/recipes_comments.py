"""
routes.recipes_comments
~~~~~~~~~~~~~~~~~~~~~~~

All routes related to recipe comment resources.
"""

from random import randrange
from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response,
)
from routers.schemas.recipes_comments import ListRecipesComments, ListRecipesCommentsQuery, PatchRecipeCommentPayload, PostRecipeCommentPayload, RecipeComment
from routers.schemas.base import ERROR_RESPONSES


router = APIRouter(
    tags=["recipesComments"],
    responses={"403": ERROR_RESPONSES[403]},
)


@router.get(
    "/recipes/{recipe_id}/comments",
    name="recipes comments list",
    status_code=200,
    response_model=ListRecipesComments,
)
async def get_recipe_comments(
    request: Request,
    recipe_id: int,
    query: ListRecipesCommentsQuery = Depends(ListRecipesCommentsQuery),
):
    """Lists all recipe comments"""
    return {
        "meta": {"total": 2},
        "comments": [
            {"id": 1, "message": "Amazing !"},
            {"id": 2, "message": "Love it 10/10 !!"}
        ]
    }


@router.post(
    "/recipes/{recipe_id}/comments",
    name="recipes comments create",
    status_code=201,
    response_model=RecipeComment,
)
async def post_recipe_comment(
    request: Request,
    recipe_id: int,
    payload: PostRecipeCommentPayload,
):
    """Creates a new recipe comment."""
    return {"id": randrange(2, 100), "message": payload.message}


@router.get(
    "/recipes/{recipe_id}/comments/{comment_id}",
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
    return {"id": 2, "message": "Love it 10/10 !!"}


@router.patch(
    "/recipes/{recipe_id}/comments/{comment_id}",
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
    payload: PatchRecipeCommentPayload,
):
    """Updates a recipe comment."""
    return {"id": 2, "message": "Love it 10/10 !!"}


@router.delete(
    "/recipes/{recipe_id}/comments/{comment_id}",
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
