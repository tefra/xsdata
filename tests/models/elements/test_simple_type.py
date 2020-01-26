from unittest import TestCase

from xsdata.models.elements import Length, List, Restriction, SimpleType, Union
from xsdata.models.enums import XSDType


class SimpleTypeTests(TestCase):
    def test_property_real_name(self):
        obj = SimpleType.create(name="foo")
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(NotImplementedError):
            obj = SimpleType.create()
            self.assertFalse(hasattr(obj, "ref"))
            obj.real_name

    def test_property_extends(self):
        obj = SimpleType.create()
        self.assertIsNone(obj.extends)

    def test_property_real_type(self):
        obj = SimpleType.create()
        self.assertIsNone(obj.real_type)

        obj.union = Union.create(member_types="thug")
        self.assertEqual("thug", obj.real_type)

        obj.list = List.create(item_type="foo")
        self.assertEqual(XSDType.STRING.code, obj.real_type)

        obj.restriction = Restriction.create(base="bar")
        self.assertEqual("bar", obj.real_type)

    def test_get_restrictions(self):
        obj = SimpleType.create()
        self.assertEqual({}, obj.get_restrictions())

        expected = dict(length=2)
        obj.restriction = Restriction.create(length=Length.create(value=2))
        self.assertEqual(expected, obj.get_restrictions())
