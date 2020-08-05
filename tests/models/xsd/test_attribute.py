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

    def test_property_real_type(self):
        obj = Attribute()
        self.assertEqual("", obj.real_type)

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.real_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.real_type)

        obj.simple_type = SimpleType()
        self.assertEqual("", obj.real_type)

        obj.simple_type.restriction = Restriction(base="thug")
        self.assertEqual(obj.simple_type.restriction.base, obj.real_type)

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
        expected = {"max_occurs": 1, "min_occurs": 1, "required": True}
        self.assertEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType(restriction=Restriction(length=Length(value=1)))
        expected["length"] = 1
        self.assertEqual(expected, obj.get_restrictions())

        obj.type = "NMTOKENS"
        expected["tokens"] = True
        self.assertEqual(expected, obj.get_restrictions())

    def test_property_extensions(self):
        obj = Attribute()
        self.assertEqual([], list(obj.extensions))
