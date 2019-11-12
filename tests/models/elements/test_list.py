import sys
from unittest import TestCase

from xsdata.models.elements import Length, List, Restriction, SimpleType


class ListTests(TestCase):
    def test_real_type(self):
        obj = List.build()
        self.assertIsNone(obj.real_type)

        obj.simple_type = SimpleType.build()
        self.assertEqual("xs:string", obj.real_type)

        obj.item_type = "foo"
        self.assertEqual("foo", obj.real_type)

    def test_get_restrictions(self):
        obj = List.build()
        expected = dict(min_occurs=0, max_occurs=sys.maxsize)
        self.assertDictEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType.build(
            restriction=Restriction.build(length=Length.build(value=1))
        )
        expected.update(dict(length=1))
        self.assertDictEqual(expected, obj.get_restrictions())
