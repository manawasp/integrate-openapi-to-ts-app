/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ListRecipes } from '../models/ListRecipes';
import type { PatchRecipePayload } from '../models/PatchRecipePayload';
import type { PostRecipePayload } from '../models/PostRecipePayload';
import type { Recipe } from '../models/Recipe';

import type { CancelablePromise } from '../core/CancelablePromise';
import type { BaseHttpRequest } from '../core/BaseHttpRequest';

export class RecipesService {

    constructor(public readonly httpRequest: BaseHttpRequest) {}

    /**
     * Recipes List
     * Lists all recipes
     * @returns ListRecipes Successful Response
     * @throws ApiError
     */
    public recipesList({
        ob = '-created_at',
        s,
        sf = 'name',
        l = 20,
        p = 1,
    }: {
        ob?: string,
        s?: string,
        sf?: string,
        l?: number,
        p?: number,
    }): CancelablePromise<ListRecipes> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/recipes',
            query: {
                'ob': ob,
                's': s,
                'sf': sf,
                'l': l,
                'p': p,
            },
            errors: {
                403: `not enough privileges`,
                422: `Validation Error`,
            },
        });
    }

    /**
     * Recipes Create
     * Creates a new recipe.
     * @returns Recipe Successful Response
     * @throws ApiError
     */
    public recipesCreate({
        requestBody,
    }: {
        requestBody: PostRecipePayload,
    }): CancelablePromise<Recipe> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/recipes',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                403: `not enough privileges`,
                422: `Validation Error`,
            },
        });
    }

    /**
     * Recipes Retrieve
     * Gets a specific recipe's information.
     * @returns Recipe Successful Response
     * @throws ApiError
     */
    public recipesRetrieve({
        recipeId,
    }: {
        recipeId: number,
    }): CancelablePromise<Recipe> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/recipes/{recipe_id}',
            path: {
                'recipe_id': recipeId,
            },
            errors: {
                403: `not enough privileges`,
                404: `item not found`,
                422: `Validation Error`,
            },
        });
    }

    /**
     * Recipes Delete
     * Deletes a recipe.
     * @returns void
     * @throws ApiError
     */
    public recipesDelete({
        recipeId,
    }: {
        recipeId: number,
    }): CancelablePromise<void> {
        return this.httpRequest.request({
            method: 'DELETE',
            url: '/recipes/{recipe_id}',
            path: {
                'recipe_id': recipeId,
            },
            errors: {
                403: `not enough privileges`,
                404: `item not found`,
                422: `Validation Error`,
            },
        });
    }

    /**
     * Recipes Update
     * Updates a recipe.
     * @returns Recipe Successful Response
     * @throws ApiError
     */
    public recipesUpdate({
        recipeId,
        requestBody,
    }: {
        recipeId: number,
        requestBody: PatchRecipePayload,
    }): CancelablePromise<Recipe> {
        return this.httpRequest.request({
            method: 'PATCH',
            url: '/recipes/{recipe_id}',
            path: {
                'recipe_id': recipeId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                403: `not enough privileges`,
                404: `item not found`,
                409: `violation of unique constraint`,
                422: `Validation Error`,
            },
        });
    }

}
