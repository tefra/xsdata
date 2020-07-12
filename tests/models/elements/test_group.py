from unittest import TestCase

from xsdata.models.xsd import Group


class GroupTests(TestCase):
    def test_property_is_attribute(self):
        obj = Group()
        self.assertTrue(obj.is_attribute)

    def test_property_real_type(self):
        obj = Group()
        self.assertEqual("", obj.real_type)

        obj.ref = "foo"
        self.assertEqual("foo", obj.real_type)

    def test_get_restrictions(self):
        obj = Group(min_occurs=1, max_occurs=2)
        self.assertEqual({"max_occurs": 2, "min_occurs": 1}, obj.get_restrictions())
