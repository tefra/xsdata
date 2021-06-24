from unittest import TestCase

from xsdata.exceptions import SchemaValueError
from xsdata.models.enums import Namespace
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
        self.assertEqual({"max_occurs": 1, "min_occurs": 0}, obj.get_restrictions())

        obj.default = "foo"
        self.assertEqual({"max_occurs": 1, "min_occurs": 1}, obj.get_restrictions())
        obj.default = None
        obj.fixed = "foo"
        self.assertEqual({"max_occurs": 1, "min_occurs": 1}, obj.get_restrictions())

        obj.fixed = None
        obj.use = UseType.REQUIRED
        expected = {"max_occurs": 1, "min_occurs": 1}
        self.assertEqual(expected, obj.get_restrictions())

        obj.use = UseType.PROHIBITED
        expected = {"max_occurs": 0, "min_occurs": 0}
        self.assertEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType(restriction=Restriction(length=Length(value=1)))
        expected["length"] = 1
        self.assertEqual(expected, obj.get_restrictions())

    def test_property_bases(self):
        obj = Attribute()
        obj.ns_map["xs"] = Namespace.XS.uri
        self.assertEqual(["xs:string"], list(obj.bases))

        obj.simple_type = SimpleType()
        self.assertEqual([], list(obj.bases))

        obj.type = "foo"
        obj.simple_type = None
        self.assertEqual(["foo"], list(obj.bases))
