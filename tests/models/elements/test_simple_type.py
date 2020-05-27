from unittest import TestCase

from xsdata.models.xsd import Enumeration
from xsdata.models.xsd import Length
from xsdata.models.xsd import List
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import SimpleType
from xsdata.models.xsd import Union


class SimpleTypeTests(TestCase):
    def test_property_real_name(self):
        obj = SimpleType.create()
        self.assertEqual("value", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

    def test_property_extends(self):
        obj = SimpleType.create()
        self.assertIsNone(obj.extends)

    def test_property_real_type(self):
        obj = SimpleType.create()
        self.assertIsNone(obj.real_type)

        obj.union = Union.create(member_types="thug")
        self.assertEqual("thug", obj.real_type)

        obj.list = List.create(item_type="foo")
        self.assertEqual("foo", obj.real_type)

        obj.restriction = Restriction.create(base="bar")
        self.assertEqual("bar", obj.real_type)

        obj = SimpleType.create(restriction=Restriction.create())
        obj.restriction.enumerations.append(Enumeration.create())
        self.assertIsNone(obj.real_type)

    def test_property_is_attribute(self):
        obj = SimpleType.create()
        self.assertTrue(obj.is_attribute)

    def test_property_is_enumeration(self):
        obj = SimpleType.create()
        self.assertFalse(obj.is_enumeration)

        obj.restriction = Restriction.create()
        self.assertFalse(obj.is_enumeration)

        obj.restriction.enumerations.append(Enumeration.create())
        self.assertTrue(obj.is_enumeration)

    def test_get_restrictions(self):
        obj = SimpleType.create()
        self.assertEqual({}, obj.get_restrictions())

        expected = dict(length=2)
        obj.restriction = Restriction.create(length=Length.create(value=2))
        self.assertEqual(expected, obj.get_restrictions())
