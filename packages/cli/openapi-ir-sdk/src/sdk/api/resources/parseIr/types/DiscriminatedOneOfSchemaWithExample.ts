/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernOpenapiIr from "../../..";

export interface DiscriminatedOneOfSchemaWithExample
    extends FernOpenapiIr.WithDescription,
        FernOpenapiIr.WithName,
        FernOpenapiIr.WithSdkGroupName,
        FernOpenapiIr.WithAvailability,
        FernOpenapiIr.WithSource {
    discriminantProperty: string;
    commonProperties: FernOpenapiIr.CommonPropertyWithExample[];
    schemas: Record<string, FernOpenapiIr.SchemaWithExample>;
}
