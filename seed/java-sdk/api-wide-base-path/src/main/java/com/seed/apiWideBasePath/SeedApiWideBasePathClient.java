/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.apiWideBasePath;

import com.seed.apiWideBasePath.core.ClientOptions;
import com.seed.apiWideBasePath.core.Suppliers;
import com.seed.apiWideBasePath.resources.service.ServiceClient;
import java.util.function.Supplier;

public class SeedApiWideBasePathClient {
    protected final ClientOptions clientOptions;

    protected final Supplier<ServiceClient> serviceClient;

    public SeedApiWideBasePathClient(ClientOptions clientOptions) {
        this.clientOptions = clientOptions;
        this.serviceClient = Suppliers.memoize(() -> new ServiceClient(clientOptions));
    }

    public ServiceClient service() {
        return this.serviceClient.get();
    }

    public static SeedApiWideBasePathClientBuilder builder() {
        return new SeedApiWideBasePathClientBuilder();
    }
}