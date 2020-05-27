import sys
from unittest import TestCase

from xsdata.models.xsd import List


class ListTests(TestCase):
    def test_is_attribute(self):
        obj = List.create()
        self.assertTrue(obj.is_attribute)

    def test_real_name(self):
        obj = List.create()
        self.assertEqual("value", obj.real_name)

    def test_real_type(self):
        obj = List.create()
        self.assertIsNone(obj.real_type)

        obj.item_type = "foo"
        self.assertEqual("foo", obj.real_type)

    def test_get_restrictions(self):
        obj = List.create()
        expected = dict(min_occurs=0, max_occurs=sys.maxsize)
        self.assertEqual(expected, obj.get_restrictions())
