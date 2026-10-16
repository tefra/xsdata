from jinja2.bccache import Bucket, BytecodeCache


class MemoryBytecodeCache(BytecodeCache):
    """In-memory jinja2 bytecode cache.

    Every generator instance creates its own environment, because the
    filters depend on the generator config. Sharing the compiled
    templates across environments skips parsing and compiling them
    on every code generation run in the same process.

    Buckets are keyed by the template name and filename, and jinja2
    discards cached bytecode when the template source checksum changes.
    """

    __slots__ = ("store",)

    def __init__(self) -> None:
        self.store: dict[str, bytes] = {}

    def load_bytecode(self, bucket: Bucket) -> None:
        """Load the cached bytecode into the bucket, if any."""
        code = self.store.get(bucket.key)
        if code is not None:
            bucket.bytecode_from_string(code)

    def dump_bytecode(self, bucket: Bucket) -> None:
        """Store the bucket bytecode."""
        self.store[bucket.key] = bucket.bytecode_to_string()

    def clear(self) -> None:
        """Clear the cache."""
        self.store.clear()
