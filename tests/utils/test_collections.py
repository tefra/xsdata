from typing import Generator
from typing import Hashable
from unittest import TestCase

from xsdata.utils import collections
from xsdata.utils.collections import Immutable


class CollectionsTests(TestCase):
    def test_find(self):
        self.assertEqual(-1, collections.find([0, 1], 2))
        self.assertEqual(1, collections.find([0, 1], 1))

    def test_concat(self):
        def generator():
            yield 7
            yield 8
            yield 9

        result = collections.concat((1, 2, 3), [4, 5, 6], generator())
        self.assertIsInstance(result, Generator)
        self.assertEqual(list(range(1, 10)), list(result))

    def test_map_key(self):
        dictionary = {"a": "b"}

        self.assertIsNone(collections.map_key(dictionary, "x"))
        self.assertEqual("a", collections.map_key(dictionary, "b"))

    def test_prepend(self):
        target = [1, 2, 3]
        prepend_values = [4, 5, 6]
        collections.prepend(target, *prepend_values)

        self.assertEqual([4, 5, 6, 1, 2, 3], target)

    def test_remove(self):
        self.assertEqual([1, 3], collections.remove([1, 2, 2, 3], lambda x: x == 2))

        self.assertEqual([2, 2, 3], collections.remove([1, 2, 2, 3], lambda x: x == 1))

        self.assertEqual([3], collections.remove([1, 2, 2, 3], lambda x: x < 3))


class ImmutableImpl(Immutable):
    __slots__ = ("a", "b", "_c")

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._c = "private"
        self._hashcode = -1


class ImmutableTests(TestCase):
    def setUp(self) -> None:
        self.obj = ImmutableImpl(1, 2)

    def test_immutable(self):
        with self.assertRaises(TypeError) as cm:
            self.obj.a = 2

        self.assertEqual("ImmutableImpl is immutable", str(cm.exception))

        with self.assertRaises(TypeError) as cm:
            del self.obj.a

        self.assertEqual("ImmutableImpl is immutable", str(cm.exception))

    def test_comparisons(self):
        self.assertEqual(ImmutableImpl(1, 2), self.obj)
        self.assertNotEqual(ImmutableImpl(2, 2), self.obj)
        self.assertNotEqual("a", self.obj)

        self.assertLess(ImmutableImpl(1, 1), self.obj)
        self.assertLessEqual(ImmutableImpl(1, 1), self.obj)
        self.assertLessEqual(ImmutableImpl(1, 2), self.obj)

        self.assertGreater(self.obj, ImmutableImpl(1, 1))
        self.assertGreaterEqual(self.obj, ImmutableImpl(1, 1))
        self.assertGreaterEqual(self.obj, ImmutableImpl(1, 2))

        with self.assertRaises(AssertionError):
            self.assertEqual(self.obj, 1)

        with self.assertRaises(TypeError):
            self.assertLess(self.obj, 1)

        with self.assertRaises(TypeError):
            self.assertLessEqual(self.obj, 1)

        with self.assertRaises(TypeError):
            self.assertGreater(self.obj, 1)

        with self.assertRaises(TypeError):
            self.assertGreaterEqual(self.obj, 1)

    def test_hash(self):
        self.assertEqual(-1, self.obj._hashcode)
        self.assertIsInstance(self.obj, Hashable)

        hash(self.obj)
        self.assertNotEqual(-1, self.obj._hashcode)
        self.assertEqual(self.obj._hashcode, hash(self.obj))

    def test_iter(self):
        self.assertEqual([1, 2], list(self.obj))

    def test_init(self):
        obj = ImmutableImpl(1, 2)
        self.assertEqual({"a": 1, "b": 2}, obj.as_dict())
