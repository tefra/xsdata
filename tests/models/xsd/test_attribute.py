from unittest import TestCase

from xsdata.exceptions import SchemaValueError
from xsdata.models.enums import UseType
from xsdata.models.xsd import Attribute
from xsdata.models.xsd import Length
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import SimpleType


class AttributeTests(TestCase):
    def test_property_is_attribute(self):
        obj = Attribute()
        self.assertTrue(obj)

    def test_property_attr_types(self):
        obj = Attribute()
        self.assertEqual([], list(obj.attr_types))

        obj.ref = "foo"
        self.assertEqual([obj.ref], list(obj.attr_types))

        obj.type = "bar"
        self.assertEqual([obj.type], list(obj.attr_types))

        obj.simple_type = SimpleType()
        self.assertEqual([], list(obj.attr_types))

        obj.simple_type.restriction = Restriction(base="thug")
        self.assertEqual([obj.simple_type.restriction.base], list(obj.attr_types))

    def test_property_real_name(self):
        obj = Attribute(ref="bar")
        self.assertEqual("bar", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(SchemaValueError):
            Attribute().real_name

    def test_get_restrictions(self):
        obj = Attribute()
        self.assertEqual({}, obj.get_restrictions())

        obj.use = UseType.REQUIRED
        expected = {"required": True}
        self.assertEqual(expected, obj.get_restrictions())

        obj.use = UseType.PROHIBITED
        expected = {"prohibited": True}
        self.assertEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType(restriction=Restriction(length=Length(value=1)))
        expected["length"] = 1
        self.assertEqual(expected, obj.get_restrictions())

    def test_property_bases(self):
        obj = Attribute()
        self.assertEqual([], list(obj.bases))

        obj.type = "foo"
        self.assertEqual(["foo"], list(obj.bases))
