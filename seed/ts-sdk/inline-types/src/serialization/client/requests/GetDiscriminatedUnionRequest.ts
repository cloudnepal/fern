/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../index";
import * as SeedObject from "../../../api/index";
import * as core from "../../../core";
import { DiscriminatedUnion1 } from "../../types/DiscriminatedUnion1";

export const GetDiscriminatedUnionRequest: core.serialization.Schema<
    serializers.GetDiscriminatedUnionRequest.Raw,
    SeedObject.GetDiscriminatedUnionRequest
> = core.serialization.object({
    bar: DiscriminatedUnion1,
    foo: core.serialization.string(),
});

export declare namespace GetDiscriminatedUnionRequest {
    interface Raw {
        bar: DiscriminatedUnion1.Raw;
        foo: string;
    }
}
