from unittest import TestCase

from xsdata.models.elements import List
from xsdata.models.enums import XSDType


class ListTests(TestCase):
    def test_is_attribute(self):
        obj = List.create()
        self.assertTrue(obj.is_attribute)

    def test_real_name(self):
        obj = List.create()
        self.assertEqual("value", obj.real_name)

    def test_real_type(self):
        obj = List.create()
        self.assertEqual(XSDType.STRING.code, obj.real_type)

    def test_get_restrictions(self):
        obj = List.create()
        self.assertEqual(dict(), obj.get_restrictions())
