import sys
from unittest import TestCase

from xsdata.models.xsd import Group


class GroupTests(TestCase):
    def test_normalize_max_occurs(self) -> None:
        obj = Group(min_occurs=3, max_occurs=2)
        self.assertEqual(3, obj.max_occurs)
        self.assertEqual(3, obj.min_occurs)

        obj = Group(min_occurs=3, max_occurs="unbounded")
        self.assertEqual(sys.maxsize, obj.max_occurs)
        self.assertEqual(3, obj.min_occurs)

    def test_property_is_property(self) -> None:
        obj = Group()
        self.assertTrue(obj.is_property)

    def test_property_attr_types(self) -> None:
        obj = Group()
        self.assertEqual([], list(obj.attr_types))

        obj.ref = "foo"
        self.assertEqual(["foo"], list(obj.attr_types))

    def test_get_restrictions(self) -> None:
        obj = Group(min_occurs=1, max_occurs=2)
        self.assertEqual({"path": [("g", id(obj), 1, 2)]}, obj.get_restrictions())
