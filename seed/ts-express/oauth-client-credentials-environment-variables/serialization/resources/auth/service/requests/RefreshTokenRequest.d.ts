/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../../../index";
import * as SeedOauthClientCredentialsEnvironmentVariables from "../../../../../api/index";
import * as core from "../../../../../core";
export declare const RefreshTokenRequest: core.serialization.Schema<serializers.RefreshTokenRequest.Raw, SeedOauthClientCredentialsEnvironmentVariables.RefreshTokenRequest>;
export declare namespace RefreshTokenRequest {
    interface Raw {
        client_id: string;
        client_secret: string;
        refresh_token: string;
        audience: "https://api.example.com";
        grant_type: "refresh_token";
        scope?: string | null;
    }
}