import sys
from unittest import TestCase

from xsdata.models.xsd import All


class AllTests(TestCase):
    def test_normalize_max_occurs(self):
        obj = All(min_occurs=3, max_occurs=2)
        self.assertEqual(3, obj.max_occurs)
        self.assertEqual(3, obj.min_occurs)

        obj = All(min_occurs=3, max_occurs="unbounded")
        self.assertEqual(sys.maxsize, obj.max_occurs)
        self.assertEqual(3, obj.min_occurs)

    def test_get_restrictions(self):
        obj = All(min_occurs=1, max_occurs=2)
        self.assertEqual({"path": [("a", id(obj), 1, 2)]}, obj.get_restrictions())
