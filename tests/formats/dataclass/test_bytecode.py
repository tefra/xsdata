from unittest import TestCase

from jinja2 import Environment
from jinja2.bccache import Bucket

from xsdata.formats.dataclass.bytecode import MemoryBytecodeCache


class MemoryBytecodeCacheTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.env = Environment()
        self.cache = MemoryBytecodeCache()

    def test_load_bytecode_with_empty_cache(self) -> None:
        bucket = Bucket(self.env, "foo", "abc")
        self.cache.load_bytecode(bucket)

        self.assertIsNone(bucket.code)

    def test_load_bytecode_after_dump(self) -> None:
        bucket = Bucket(self.env, "foo", "abc")
        bucket.code = self.env.compile("{{ bar }}")
        self.cache.dump_bytecode(bucket)

        other = Bucket(self.env, "foo", "abc")
        self.cache.load_bytecode(other)

        self.assertEqual(bucket.code, other.code)

    def test_load_bytecode_with_changed_checksum(self) -> None:
        bucket = Bucket(self.env, "foo", "abc")
        bucket.code = self.env.compile("{{ bar }}")
        self.cache.dump_bytecode(bucket)

        other = Bucket(self.env, "foo", "xyz")
        self.cache.load_bytecode(other)

        self.assertIsNone(other.code)

    def test_clear(self) -> None:
        bucket = Bucket(self.env, "foo", "abc")
        bucket.code = self.env.compile("{{ bar }}")
        self.cache.dump_bytecode(bucket)
        self.cache.clear()

        self.assertEqual({}, self.cache.store)
