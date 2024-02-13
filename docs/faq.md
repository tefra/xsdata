# Frequently Asked Questions

## How can I compare output results between versions

See the [`--include-header`](codegen/config.md#includeheader) config.

## Why are elements out of order?

---

See the [`--compound-fields`](codegen/config.md#compoundfields) config.

## Why do I get a TypeError: requires a single type

```console
TypeError: typing.Optional requires a single type. Got Field(name=None,type=None,default=<dataclasses._MISSING_TYPE object at 0x7f79f4b0d700>,default_facto.
```

This error means the typing annotations for a model are ambiguous because they collide
with a class field. In order to resolve this issue you have to enable the
[`--postponed-annotations`](codegen/config.md#postponedannotations) config.

## Why non-nullable fields are marked as optional?

A TypeError is raised if a [dataclasses][] field without a default value follows a field
with a default value. If you are using >= Python 3.10 you can enable the `kwOnly` option
in the [format](codegen/config.md#format) config.

If you can't update just yet please check the
[attrs](https://pypi.org/project/xsdata-attrs/) plugin!
