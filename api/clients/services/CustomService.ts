/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import type { BaseHttpRequest } from '../core/BaseHttpRequest';

export class CustomService {

    constructor(public readonly httpRequest: BaseHttpRequest) {}

    /**
     * Custom Not Found
     * Returns a not found response
     * @returns void
     * @throws ApiError
     */
    public customNotFound(): CancelablePromise<void> {
        return this.httpRequest.request({
            method: 'GET',
            url: 'not_found',
            errors: {
                404: `item not found`,
            },
        });
    }

    /**
     * Custom Unauthorized
     * Returns a unauthorized response
     * @returns void
     * @throws ApiError
     */
    public customUnauthorized(): CancelablePromise<void> {
        return this.httpRequest.request({
            method: 'GET',
            url: 'unauthorized',
            errors: {
                401: `unauthorized`,
            },
        });
    }

}
