from unittest import TestCase

from xsdata.models.xsd import Group


class GroupTests(TestCase):
    def test_property_is_attribute(self):
        obj = Group()
        self.assertTrue(obj.is_attribute)

    def test_property_attr_types(self):
        obj = Group()
        self.assertEqual([], list(obj.attr_types))

        obj.ref = "foo"
        self.assertEqual(["foo"], list(obj.attr_types))

    def test_get_restrictions(self):
        obj = Group(min_occurs=1, max_occurs=2)
        self.assertEqual({"max_occurs": 2, "min_occurs": 1}, obj.get_restrictions())
