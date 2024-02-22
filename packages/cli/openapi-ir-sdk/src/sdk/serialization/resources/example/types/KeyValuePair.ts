/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernOpenapiIr from "../../../../api";
import * as core from "../../../../core";

export const KeyValuePair: core.serialization.ObjectSchema<serializers.KeyValuePair.Raw, FernOpenapiIr.KeyValuePair> =
    core.serialization.objectWithoutOptionalProperties({
        key: core.serialization.lazy(async () => (await import("../../..")).PrimitiveExample),
        value: core.serialization.lazy(async () => (await import("../../..")).FullExample),
    });

export declare namespace KeyValuePair {
    interface Raw {
        key: serializers.PrimitiveExample.Raw;
        value: serializers.FullExample.Raw;
    }
}