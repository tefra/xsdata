import itertools
from typing import Generator
from typing import Hashable
from unittest import TestCase

from xsdata.utils import collections


class CollectionsTests(TestCase):
    def test_find(self):
        self.assertEqual(-1, collections.find([0, 1], 2))
        self.assertEqual(1, collections.find([0, 1], 1))

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
