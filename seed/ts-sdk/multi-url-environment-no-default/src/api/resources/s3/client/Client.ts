/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as environments from "../../../../environments";
import * as core from "../../../../core";
import * as SeedMultiUrlEnvironmentNoDefault from "../../../index";
import * as serializers from "../../../../serialization/index";
import urlJoin from "url-join";
import * as errors from "../../../../errors/index";

export declare namespace S3 {
    interface Options {
        environment: core.Supplier<
            | environments.SeedMultiUrlEnvironmentNoDefaultEnvironment
            | environments.SeedMultiUrlEnvironmentNoDefaultEnvironmentUrls
        >;
        token: core.Supplier<core.BearerToken>;
    }

    interface RequestOptions {
        /** The maximum time to wait for a response in seconds. */
        timeoutInSeconds?: number;
        /** The number of times to retry the request. Defaults to 2. */
        maxRetries?: number;
        /** A hook to abort the request. */
        abortSignal?: AbortSignal;
    }
}

export class S3 {
    constructor(protected readonly _options: S3.Options) {}

    /**
     * @param {SeedMultiUrlEnvironmentNoDefault.GetPresignedUrlRequest} request
     * @param {S3.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.s3.getPresignedUrl({
     *         s3Key: "s3Key"
     *     })
     */
    public getPresignedUrl(
        request: SeedMultiUrlEnvironmentNoDefault.GetPresignedUrlRequest,
        requestOptions?: S3.RequestOptions
    ): core.APIPromise<string> {
        return core.APIPromise.from(
            (async () => {
                const _response = await core.fetcher({
                    url: urlJoin((await core.Supplier.get(this._options.environment)).s3, "/s3/presigned-url"),
                    method: "POST",
                    headers: {
                        Authorization: await this._getAuthorizationHeader(),
                        "X-Fern-Language": "JavaScript",
                        "X-Fern-SDK-Name": "@fern/multi-url-environment-no-default",
                        "X-Fern-SDK-Version": "0.0.1",
                        "User-Agent": "@fern/multi-url-environment-no-default/0.0.1",
                        "X-Fern-Runtime": core.RUNTIME.type,
                        "X-Fern-Runtime-Version": core.RUNTIME.version,
                    },
                    contentType: "application/json",
                    requestType: "json",
                    body: serializers.GetPresignedUrlRequest.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
                    timeoutMs:
                        requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                    maxRetries: requestOptions?.maxRetries,
                    abortSignal: requestOptions?.abortSignal,
                });
                if (_response.ok) {
                    return {
                        ok: _response.ok,
                        body: serializers.s3.getPresignedUrl.Response.parseOrThrow(_response.body, {
                            unrecognizedObjectKeys: "passthrough",
                            allowUnrecognizedUnionMembers: true,
                            allowUnrecognizedEnumValues: true,
                            breadcrumbsPrefix: ["response"],
                        }),
                        headers: _response.headers,
                    };
                }
                if (_response.error.reason === "status-code") {
                    throw new errors.SeedMultiUrlEnvironmentNoDefaultError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.body,
                    });
                }
                switch (_response.error.reason) {
                    case "non-json":
                        throw new errors.SeedMultiUrlEnvironmentNoDefaultError({
                            statusCode: _response.error.statusCode,
                            body: _response.error.rawBody,
                        });
                    case "timeout":
                        throw new errors.SeedMultiUrlEnvironmentNoDefaultTimeoutError();
                    case "unknown":
                        throw new errors.SeedMultiUrlEnvironmentNoDefaultError({
                            message: _response.error.errorMessage,
                        });
                }
            })()
        );
    }

    protected async _getAuthorizationHeader(): Promise<string> {
        return `Bearer ${await core.Supplier.get(this._options.token)}`;
    }
}
