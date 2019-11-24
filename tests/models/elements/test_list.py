import sys
from unittest import TestCase

from xsdata.models.elements import Length, List, Restriction, SimpleType


class ListTests(TestCase):
    def test_real_type(self):
        obj = List.create()
        self.assertIsNone(obj.real_type)

        obj.simple_type = SimpleType.create()
        self.assertEqual("xs:string", obj.real_type)

        obj.item_type = "foo"
        self.assertEqual("foo", obj.real_type)

    def test_get_restrictions(self):
        obj = List.create()
        expected = dict(min_occurs=0, max_occurs=sys.maxsize)
        self.assertEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType.create(
            restriction=Restriction.create(length=Length.create(value=1))
        )
        expected.update(dict(length=1))
        self.assertEqual(expected, obj.get_restrictions())
