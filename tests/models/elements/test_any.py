from unittest import TestCase

from xsdata.models.elements import Any


class AnyTests(TestCase):
    def test_is_attribute(self):
        obj = Any.create()
        self.assertTrue(obj.is_attribute)

    def test_property_real_name(self):
        obj = Any.create()
        self.assertEqual("elements", obj.real_name)

    def test_property_real_type(self):
        obj = Any.create()
        self.assertEqual("xml:object", obj.real_type)

    def test_get_restrictions(self):
        obj = Any.create(min_occurs=1, max_occurs=2)
        self.assertEqual({"max_occurs": 2, "min_occurs": 1}, obj.get_restrictions())
