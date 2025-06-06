from unittest import TestCase

from xsdata.models.xsd import Enumeration, Length, List, Restriction, SimpleType, Union


class SimpleTypeTests(TestCase):
    def test_property_real_name(self) -> None:
        obj = SimpleType()
        self.assertEqual("value", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

    def test_property_attr_types(self) -> None:
        obj = SimpleType()
        self.assertEqual([], list(obj.attr_types))

        obj.union = Union(member_types="thug")
        self.assertEqual(["thug"], list(obj.attr_types))

        obj.list = List(item_type="foo")
        self.assertEqual(["foo"], list(obj.attr_types))

        obj.restriction = Restriction(base="bar")
        self.assertEqual(["bar"], list(obj.attr_types))

        obj = SimpleType(restriction=Restriction())
        obj.restriction.enumerations.append(Enumeration())
        self.assertEqual([], list(obj.attr_types))

    def test_property_is_property(self) -> None:
        obj = SimpleType()
        self.assertTrue(obj.is_property)

    def test_property_is_enumeration(self) -> None:
        obj = SimpleType()
        self.assertFalse(obj.is_enumeration)

        obj.restriction = Restriction()
        self.assertFalse(obj.is_enumeration)

        obj.restriction.enumerations.append(Enumeration())
        self.assertTrue(obj.is_enumeration)

    def test_get_restrictions(self) -> None:
        obj = SimpleType()
        self.assertEqual({}, obj.get_restrictions())

        obj.list = List()
        self.assertEqual({"tokens": True}, obj.get_restrictions())

        expected = {"length": 2}
        obj.restriction = Restriction(length=Length(value=2))
        self.assertEqual(expected, obj.get_restrictions())
