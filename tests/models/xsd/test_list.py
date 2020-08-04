import sys
from unittest import TestCase

from xsdata.models.xsd import List


class ListTests(TestCase):
    def test_is_attribute(self):
        obj = List()
        self.assertTrue(obj.is_attribute)

    def test_real_name(self):
        obj = List()
        self.assertEqual("value", obj.real_name)

    def test_real_type(self):
        obj = List()
        self.assertEqual("", obj.real_type)

        obj.item_type = "foo"
        self.assertEqual("foo", obj.real_type)

    def test_get_restrictions(self):
        obj = List()
        self.assertEqual({"tokens": True}, obj.get_restrictions())
