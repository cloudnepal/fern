/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernOpenapiIr from "../../../../api";
import * as core from "../../../../core";

export const MultipartRequest: core.serialization.ObjectSchema<
    serializers.MultipartRequest.Raw,
    FernOpenapiIr.MultipartRequest
> = core.serialization
    .objectWithoutOptionalProperties({
        name: core.serialization.string().optional(),
        properties: core.serialization.list(
            core.serialization.lazyObject(async () => (await import("../../..")).MultipartRequestProperty)
        ),
    })
    .extend(core.serialization.lazyObject(async () => (await import("../../..")).WithDescription))
    .extend(core.serialization.lazyObject(async () => (await import("../../..")).WithSource));

export declare namespace MultipartRequest {
    interface Raw extends serializers.WithDescription.Raw, serializers.WithSource.Raw {
        name?: string | null;
        properties: serializers.MultipartRequestProperty.Raw[];
    }
}
