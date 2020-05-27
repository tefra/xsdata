from unittest import TestCase

from xsdata.exceptions import SchemaValueError
from xsdata.models.enums import UseType
from xsdata.models.xsd import Attribute
from xsdata.models.xsd import Length
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import SimpleType


class AttributeTests(TestCase):
    def test_property_is_attribute(self):
        obj = Attribute.create()
        self.assertTrue(obj)

    def test_property_real_type(self):
        obj = Attribute.create()
        self.assertIsNone(obj.real_type)

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.real_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.real_type)

        obj.simple_type = SimpleType.create()
        self.assertIsNone(obj.real_type)

        obj.simple_type.restriction = Restriction.create(base="thug")
        self.assertEqual(obj.simple_type.restriction.base, obj.real_type)

    def test_property_real_name(self):
        obj = Attribute.create(ref="bar")
        self.assertEqual("bar", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(SchemaValueError):
            Attribute.create().real_name

    def test_get_restrictions(self):
        obj = Attribute.create()
        self.assertEqual({}, obj.get_restrictions())

        obj.use = UseType.REQUIRED
        expected = {"max_occurs": 1, "min_occurs": 1, "required": True}
        self.assertEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType.create(
            restriction=Restriction.create(length=Length.create(value=1))
        )
        expected.update(dict(length=1))
        self.assertEqual(expected, obj.get_restrictions())

    def test_property_extends(self):
        obj = Attribute.create()
        self.assertIsNone(obj.extends)
