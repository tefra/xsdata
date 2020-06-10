from unittest import TestCase

from xsdata.utils import collections


class CollectionsTests(TestCase):
    def test_find(self):
        self.assertEqual(-1, collections.find([0, 1], 2))
        self.assertEqual(1, collections.find([0, 1], 1))
