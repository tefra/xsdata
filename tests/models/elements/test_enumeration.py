from unittest import TestCase

from xsdata.models.elements import Enumeration


class EnumerationTests(TestCase):
    def test_property_is_attribute(self):
        obj = Enumeration.create()
        self.assertTrue(obj)

    def test_property_real_name(self):
        obj = Enumeration.create(value="foo")
        self.assertEqual("foo", obj.real_name)

    def test_property_real_type(self):
        obj = Enumeration.create()
        self.assertEqual("xs:string", obj.real_type)

    def test_property_default(self):
        obj = Enumeration.create(value="foo")
        self.assertEqual("foo", obj.default)

    def test_property_namespace(self):
        obj = Enumeration.create()
        self.assertIsNone(obj.namespace)

    def test_get_restrictions(self):
        obj = Enumeration.create()
        self.assertEqual({}, obj.get_restrictions())
