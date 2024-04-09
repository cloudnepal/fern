/**
 * This file was auto-generated by Fern from our API Definition.
 */

import { SeedBearerTokenEnvironmentVariableClient } from "../src/Client";

const client = new SeedBearerTokenEnvironmentVariableClient({
    environment: process.env.TESTS_BASE_URL || "test",
    apiKey: process.env.COURIER_API_KEY || "test",
});

describe("Service", () => {
    test("constructor", () => {
        expect(client.service).toBeDefined();
    });
});
