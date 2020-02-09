from unittest import TestCase

from xsdata.models.elements import AnyAttribute


class AnyAttributeTests(TestCase):
    def test_is_attribute(self):
        obj = AnyAttribute.create()
        self.assertTrue(obj.is_attribute)

    def test_property_real_name(self):
        obj = AnyAttribute.create()
        self.assertEqual("attributes", obj.real_name)

    def test_property_real_type(self):
        obj = AnyAttribute.create()
        self.assertEqual("xml:qmap", obj.real_type)

    def get_restrictions(self):
        obj = AnyAttribute.create()
        self.assertEqual(dict(), obj.get_restrictions())
