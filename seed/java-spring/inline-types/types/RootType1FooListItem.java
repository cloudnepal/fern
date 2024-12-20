/**
 * This file was auto-generated by Fern from our API Definition.
 */

package types;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import core.ObjectMappers;
import java.lang.Object;
import java.lang.String;
import java.util.Objects;
import org.jetbrains.annotations.NotNull;

@JsonInclude(JsonInclude.Include.NON_ABSENT)
@JsonDeserialize(
    builder = RootType1FooListItem.Builder.class
)
public final class RootType1FooListItem {
  private final String foo;

  private final ReferenceType ref;

  private RootType1FooListItem(String foo, ReferenceType ref) {
    this.foo = foo;
    this.ref = ref;
  }

  /**
   * @return lorem ipsum
   */
  @JsonProperty("foo")
  public String getFoo() {
    return foo;
  }

  /**
   * @return lorem ipsum
   */
  @JsonProperty("ref")
  public ReferenceType getRef() {
    return ref;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof RootType1FooListItem && equalTo((RootType1FooListItem) other);
  }

  private boolean equalTo(RootType1FooListItem other) {
    return foo.equals(other.foo) && ref.equals(other.ref);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.foo, this.ref);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static FooStage builder() {
    return new Builder();
  }

  public interface FooStage {
    RefStage foo(@NotNull String foo);

    Builder from(RootType1FooListItem other);
  }

  public interface RefStage {
    _FinalStage ref(@NotNull ReferenceType ref);
  }

  public interface _FinalStage {
    RootType1FooListItem build();
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder implements FooStage, RefStage, _FinalStage {
    private String foo;

    private ReferenceType ref;

    private Builder() {
    }

    @java.lang.Override
    public Builder from(RootType1FooListItem other) {
      foo(other.getFoo());
      ref(other.getRef());
      return this;
    }

    /**
     * <p>lorem ipsum</p>
     * @return Reference to {@code this} so that method calls can be chained together.
     */
    @java.lang.Override
    @JsonSetter("foo")
    public RefStage foo(@NotNull String foo) {
      this.foo = Objects.requireNonNull(foo, "foo must not be null");
      return this;
    }

    /**
     * <p>lorem ipsum</p>
     * @return Reference to {@code this} so that method calls can be chained together.
     */
    @java.lang.Override
    @JsonSetter("ref")
    public _FinalStage ref(@NotNull ReferenceType ref) {
      this.ref = Objects.requireNonNull(ref, "ref must not be null");
      return this;
    }

    @java.lang.Override
    public RootType1FooListItem build() {
      return new RootType1FooListItem(foo, ref);
    }
  }
}
