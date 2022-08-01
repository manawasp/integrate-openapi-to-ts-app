/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ListRecipes } from '../models/ListRecipes';
import type { PatchRecipePayload } from '../models/PatchRecipePayload';
import type { PostRecipePayload } from '../models/PostRecipePayload';
import type { RecipeComment } from '../models/RecipeComment';

import type { CancelablePromise } from '../core/CancelablePromise';
import type { BaseHttpRequest } from '../core/BaseHttpRequest';

export class RecipesCommentsService {

    constructor(public readonly httpRequest: BaseHttpRequest) {}

    /**
     * Recipes Comments List
     * Lists all recipe comments
     * @returns ListRecipes Successful Response
     * @throws ApiError
     */
    public recipesCommentsList({
        recipeId,
        ob = '-created_at',
        s,
        sf = 'name,description',
        l = 20,
        p = 1,
    }: {
        recipeId: number,
        ob?: string,
        s?: string,
        sf?: string,
        l?: number,
        p?: number,
    }): CancelablePromise<ListRecipes> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/recipes/{recipe_id}/comments/',
            path: {
                'recipe_id': recipeId,
            },
            query: {
                'ob': ob,
                's': s,
                'sf': sf,
                'l': l,
                'p': p,
            },
            errors: {
                403: `Not enough privileges`,
                422: `Validation Error`,
            },
        });
    }

    /**
     * Recipes Comments Create
     * Creates a new recipe comment.
     * @returns RecipeComment Successful Response
     * @throws ApiError
     */
    public recipesCommentsCreate({
        recipeId,
        requestBody,
    }: {
        recipeId: number,
        requestBody: PostRecipePayload,
    }): CancelablePromise<RecipeComment> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/recipes/{recipe_id}/comments/',
            path: {
                'recipe_id': recipeId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                403: `Not enough privileges`,
                422: `Validation Error`,
            },
        });
    }

    /**
     * Recipes Comments Retrieve
     * Gets a specific recipe comment's information.
     * @returns RecipeComment Successful Response
     * @throws ApiError
     */
    public recipesCommentsRetrieve({
        recipeId,
        commentId,
    }: {
        recipeId: number,
        commentId: number,
    }): CancelablePromise<RecipeComment> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/recipes/{recipe_id}/comments/{comment_id}',
            path: {
                'recipe_id': recipeId,
                'comment_id': commentId,
            },
            errors: {
                403: `Not enough privileges`,
                404: `Item not found`,
                422: `Validation Error`,
            },
        });
    }

    /**
     * Recipes Comments Delete
     * Deletes a recipe comment.
     * @returns any Successful Response
     * @throws ApiError
     */
    public recipesCommentsDelete({
        recipeId,
        commentId,
        id,
    }: {
        recipeId: number,
        commentId: number,
        id: number,
    }): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'DELETE',
            url: '/recipes/{recipe_id}/comments/{comment_id}',
            path: {
                'recipe_id': recipeId,
                'comment_id': commentId,
            },
            query: {
                'id': id,
            },
            errors: {
                403: `Not enough privileges`,
                404: `Item not found`,
                422: `Validation Error`,
            },
        });
    }

    /**
     * Recipes Comments Update
     * Updates a recipe comment.
     * @returns RecipeComment Successful Response
     * @throws ApiError
     */
    public recipesCommentsUpdate({
        recipeId,
        commentId,
        requestBody,
    }: {
        recipeId: number,
        commentId: number,
        requestBody: PatchRecipePayload,
    }): CancelablePromise<RecipeComment> {
        return this.httpRequest.request({
            method: 'PATCH',
            url: '/recipes/{recipe_id}/comments/{comment_id}',
            path: {
                'recipe_id': recipeId,
                'comment_id': commentId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                403: `Not enough privileges`,
                404: `Item not found`,
                422: `Validation Error`,
            },
        });
    }

}
