/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernDocsConfig from "../../../../api";
import * as core from "../../../../core";

export const MetadataConfig: core.serialization.ObjectSchema<
    serializers.MetadataConfig.Raw,
    FernDocsConfig.MetadataConfig
> = core.serialization.object({
    ogSiteName: core.serialization.property("og:site_name", core.serialization.string().optional()),
    ogTitle: core.serialization.property("og:title", core.serialization.string().optional()),
    ogDescription: core.serialization.property("og:description", core.serialization.string().optional()),
    ogUrl: core.serialization.property("og:url", core.serialization.string().optional()),
    ogImage: core.serialization.property("og:image", core.serialization.string().optional()),
    ogImageWidth: core.serialization.property("og:image:width", core.serialization.number().optional()),
    ogImageHeight: core.serialization.property("og:image:height", core.serialization.number().optional()),
    ogLocale: core.serialization.property("og:locale", core.serialization.string().optional()),
    ogLogo: core.serialization.property("og:logo", core.serialization.string().optional()),
    twitterTitle: core.serialization.property("twitter:title", core.serialization.string().optional()),
    twitterDescription: core.serialization.property("twitter:description", core.serialization.string().optional()),
    twitterHandle: core.serialization.property("twitter:handle", core.serialization.string().optional()),
    twitterImage: core.serialization.property("twitter:image", core.serialization.string().optional()),
    twitterSite: core.serialization.property("twitter:site", core.serialization.string().optional()),
    twitterUrl: core.serialization.property("twitter:url", core.serialization.string().optional()),
    twitterCard: core.serialization.property(
        "twitter:card",
        core.serialization.lazy(async () => (await import("../../..")).TwitterCardSetting).optional()
    ),
});

export declare namespace MetadataConfig {
    interface Raw {
        "og:site_name"?: string | null;
        "og:title"?: string | null;
        "og:description"?: string | null;
        "og:url"?: string | null;
        "og:image"?: string | null;
        "og:image:width"?: number | null;
        "og:image:height"?: number | null;
        "og:locale"?: string | null;
        "og:logo"?: string | null;
        "twitter:title"?: string | null;
        "twitter:description"?: string | null;
        "twitter:handle"?: string | null;
        "twitter:image"?: string | null;
        "twitter:site"?: string | null;
        "twitter:url"?: string | null;
        "twitter:card"?: serializers.TwitterCardSetting.Raw | null;
    }
}