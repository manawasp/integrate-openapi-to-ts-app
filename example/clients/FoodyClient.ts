/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { BaseHttpRequest } from './core/BaseHttpRequest';
import type { OpenAPIConfig } from './core/OpenAPI';
import { FetchHttpRequest } from './core/FetchHttpRequest';

import { CustomService } from './services/CustomService';
import { RecipesService } from './services/RecipesService';
import { RecipesCommentsService } from './services/RecipesCommentsService';

type HttpRequestConstructor = new (config: OpenAPIConfig) => BaseHttpRequest;

export class FoodyClient {

    public readonly custom: CustomService;
    public readonly recipes: RecipesService;
    public readonly recipesComments: RecipesCommentsService;

    public readonly request: BaseHttpRequest;

    constructor(config?: Partial<OpenAPIConfig>, HttpRequest: HttpRequestConstructor = FetchHttpRequest) {
        this.request = new HttpRequest({
            BASE: config?.BASE ?? '',
            VERSION: config?.VERSION ?? '0.0.1',
            WITH_CREDENTIALS: config?.WITH_CREDENTIALS ?? false,
            CREDENTIALS: config?.CREDENTIALS ?? 'include',
            TOKEN: config?.TOKEN,
            USERNAME: config?.USERNAME,
            PASSWORD: config?.PASSWORD,
            HEADERS: config?.HEADERS,
            ENCODE_PATH: config?.ENCODE_PATH,
        });

        this.custom = new CustomService(this.request);
        this.recipes = new RecipesService(this.request);
        this.recipesComments = new RecipesCommentsService(this.request);
    }
}

