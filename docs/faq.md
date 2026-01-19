# Frequently Asked Questions

## How can I compare output results between versions?

See the [`--include-header`](codegen/config.md#includeheader) config.

## Why are elements out of order?

See the [`--compound-fields`](codegen/config.md#compoundfields) config.

## Why are non-nullable fields marked as optional?

A TypeError is raised if a [dataclasses][] field without a default value follows a field
with a default value. Since Python 3.10+ is required, xsdata always generates
dataclasses with `kw_only=True`, which resolves this issue.
