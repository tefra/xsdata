from collections import namedtuple
from typing import Iterator
from unittest import TestCase

from xsdata.utils import collections


class CollectionsTests(TestCase):
    def test_find(self):
        self.assertEqual(-1, collections.find([0, 1], 2))
        self.assertEqual(1, collections.find([0, 1], 1))

    def test_prepend(self):
        target = [1, 2, 3]
        prepend_values = [4, 5, 6]
        collections.prepend(target, *prepend_values)

        self.assertEqual([4, 5, 6, 1, 2, 3], target)

    def test_remove(self):
        self.assertEqual([1, 3], collections.remove([1, 2, 2, 3], lambda x: x == 2))

        self.assertEqual([2, 2, 3], collections.remove([1, 2, 2, 3], lambda x: x == 1))

        self.assertEqual([3], collections.remove([1, 2, 2, 3], lambda x: x < 3))

    def test_is_array(self):
        fixture = namedtuple("fixture", ["a", "b"])

        self.assertFalse(collections.is_array(1))
        self.assertFalse(collections.is_array(fixture(1, 2)))
        self.assertTrue(collections.is_array([]))
        self.assertTrue(collections.is_array(tuple()))
        self.assertTrue(collections.is_array(frozenset()))

    def test_connected_components(self):
        lists = [[1, 2, 3], [4], [3, 4], [6]]
        actual = collections.connected_components(lists)

        self.assertIsInstance(actual, Iterator)
        self.assertEqual([[1, 2, 3, 4], [6]], list(actual))

    def test_find_connected_component(self):
        groups = [[1, 2, 3], [4, 5, 6]]

        actual = collections.find_connected_component(groups, 1)
        self.assertEqual(0, actual)

        actual = collections.find_connected_component(groups, 2)
        self.assertEqual(0, actual)

        actual = collections.find_connected_component(groups, 4)
        self.assertEqual(1, actual)

        actual = collections.find_connected_component(groups, 100)
        self.assertEqual(-1, actual)
