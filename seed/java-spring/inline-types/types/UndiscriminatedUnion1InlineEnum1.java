/**
 * This file was auto-generated by Fern from our API Definition.
 */

package types;

import com.fasterxml.jackson.annotation.JsonValue;
import java.lang.String;

public enum UndiscriminatedUnion1InlineEnum1 {
  SUNNY("SUNNY"),

  CLOUDY("CLOUDY"),

  RAINING("RAINING"),

  SNOWING("SNOWING");

  private final String value;

  UndiscriminatedUnion1InlineEnum1(String value) {
    this.value = value;
  }

  @JsonValue
  @java.lang.Override
  public String toString() {
    return this.value;
  }
}
