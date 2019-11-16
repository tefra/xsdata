import sys
from unittest import TestCase

from xsdata.models.elements import Length, List, Restriction, SimpleType, Union


class SimpleTypeTests(TestCase):
    def test_property_real_name(self):
        obj = SimpleType.create(name="foo")
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(NotImplementedError):
            obj = SimpleType.create()
            self.assertFalse(hasattr(obj, "ref"))
            obj.real_name

    def test_property_extensions(self):
        self.assertEqual([], SimpleType.create().extensions)

    def test_property_real_type(self):
        obj = SimpleType.create()
        self.assertEqual("xs:string", obj.real_type)

        obj.union = Union.create()
        self.assertEqual("xs:string", obj.real_type)

        obj.list = List.create(item_type="foo")
        self.assertEqual("foo", obj.real_type)

        obj.restriction = Restriction.create(base="bar")
        self.assertEqual("bar", obj.real_type)

    def test_get_restrictions(self):
        obj = SimpleType.create()
        self.assertDictEqual({}, obj.get_restrictions())

        expected = dict(min_occurs=0, max_occurs=sys.maxsize)
        obj.list = List.create()
        self.assertDictEqual(expected, obj.get_restrictions())

        expected = dict(length=2)
        obj.restriction = Restriction.create(length=Length.create(value=2))
        self.assertDictEqual(expected, obj.get_restrictions())
