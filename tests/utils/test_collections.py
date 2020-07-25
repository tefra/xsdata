from typing import Generator
from unittest import TestCase

from xsdata.utils import collections


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
