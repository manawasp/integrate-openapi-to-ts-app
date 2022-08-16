/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { ListMetaResponse } from './ListMetaResponse';
import type { RecipeComment } from './RecipeComment';

export type ListRecipesComments = {
    meta: ListMetaResponse;
    comments: Array<RecipeComment>;
};

