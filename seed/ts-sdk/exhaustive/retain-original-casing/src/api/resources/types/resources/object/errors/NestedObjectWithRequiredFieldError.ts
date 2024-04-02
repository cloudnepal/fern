/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as errors from "../../../../../../errors";
import * as SeedExhaustive from "../../../../..";

export class NestedObjectWithRequiredFieldError extends errors.SeedExhaustiveError {
    constructor(body: SeedExhaustive.types.NestedObjectWithRequiredField) {
        super({
            message: "NestedObjectWithRequiredFieldError",
            statusCode: 400,
            body: body,
        });
        Object.setPrototypeOf(this, NestedObjectWithRequiredFieldError.prototype);
    }
}
