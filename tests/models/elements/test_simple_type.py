import sys
from unittest import TestCase

from xsdata.models.elements import Length, List, Restriction, SimpleType, Union


class SimpleTypeTests(TestCase):
    def test_property_real_name(self):
        obj = SimpleType.build(name="foo")
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(NotImplementedError):
            obj = SimpleType.build()
            self.assertFalse(hasattr(obj, "ref"))
            obj.real_name

    def test_property_extensions(self):
        self.assertEqual([], SimpleType.build().extensions)

    def test_property_real_type(self):
        obj = SimpleType.build()
        self.assertEqual("xs:string", obj.real_type)

        obj.union = Union.build()
        self.assertEqual("xs:string", obj.real_type)

        obj.list = List.build(item_type="foo")
        self.assertEqual("foo", obj.real_type)

        obj.restriction = Restriction.build(base="bar")
        self.assertEqual("bar", obj.real_type)

    def test_get_restrictions(self):
        obj = SimpleType.build()
        self.assertDictEqual({}, obj.get_restrictions())

        expected = dict(min_occurs=0, max_occurs=sys.maxsize)
        obj.list = List.build()
        self.assertDictEqual(expected, obj.get_restrictions())

        expected = dict(length=2)
        obj.restriction = Restriction.build(length=Length.build(value=2))
        self.assertDictEqual(expected, obj.get_restrictions())
