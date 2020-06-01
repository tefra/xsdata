from unittest import TestCase

from xsdata.models.xsd import Enumeration


class EnumerationTests(TestCase):
    def test_property_is_attribute(self):
        obj = Enumeration()
        self.assertTrue(obj)

    def test_property_real_name(self):
        obj = Enumeration(value="foo")
        self.assertEqual("foo", obj.real_name)

    def test_property_real_type(self):
        obj = Enumeration()
        self.assertIsNone(obj.real_type)

    def test_property_default(self):
        obj = Enumeration(value="foo")
        self.assertEqual("foo", obj.default)

    def test_get_restrictions(self):
        obj = Enumeration()
        self.assertEqual({}, obj.get_restrictions())
