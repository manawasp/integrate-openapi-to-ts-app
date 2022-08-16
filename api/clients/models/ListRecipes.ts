/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { ListMetaResponse } from './ListMetaResponse';
import type { Recipe } from './Recipe';

export type ListRecipes = {
    meta: ListMetaResponse;
    recipes: Array<Recipe>;
};

