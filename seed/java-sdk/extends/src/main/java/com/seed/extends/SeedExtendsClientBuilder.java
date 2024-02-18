/**
 * This file was auto-generated by Fern from our API Definition.
 */

package com.seed.extends;

import com.seed.extends.core.ClientOptions;
import com.seed.extends.core.Environment;
import java.lang.String;

public final class SeedExtendsClientBuilder {
  private ClientOptions.Builder clientOptionsBuilder = ClientOptions.builder();

  private Environment environment;

  public SeedExtendsClientBuilder url(String url) {
    this.environment = Environment.custom(url);
    return this;
  }

  public SeedExtendsClient build() {
    clientOptionsBuilder.environment(this.environment);
    return new SeedExtendsClient(clientOptionsBuilder.build());
  }
}