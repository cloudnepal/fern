/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernDocsConfig from "../../../../api";
import * as core from "../../../../core";

export const Role: core.serialization.Schema<serializers.Role.Raw, FernDocsConfig.Role> =
    core.serialization.undiscriminatedUnion([
        core.serialization.lazy(async () => (await import("../../..")).RoleId),
        core.serialization.list(core.serialization.lazy(async () => (await import("../../..")).RoleId)),
    ]);

export declare namespace Role {
    type Raw = serializers.RoleId.Raw | serializers.RoleId.Raw[];
}
