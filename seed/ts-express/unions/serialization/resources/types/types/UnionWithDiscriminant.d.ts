/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../..";
import * as SeedUnions from "../../../../api";
import * as core from "../../../../core";
export declare const UnionWithDiscriminant: core.serialization.Schema<serializers.UnionWithDiscriminant.Raw, SeedUnions.UnionWithDiscriminant>;
export declare namespace UnionWithDiscriminant {
    type Raw = UnionWithDiscriminant.Foo | UnionWithDiscriminant.Bar;
    interface Foo {
        _type: "foo";
        foo: serializers.Foo.Raw;
    }
    interface Bar {
        _type: "bar";
        bar: serializers.Bar.Raw;
    }
}