from unittest import TestCase

from xsdata.models.elements import Attribute, Restriction, SimpleType


class AttributeTests(TestCase):
    def test_property_raw_type(self):
        obj = Attribute.build()
        self.assertEqual("xs:string", obj.raw_type)

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.raw_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.raw_type)

        obj.simple_type = SimpleType.build()
        self.assertIsNone(obj.raw_type)

        obj.simple_type.restriction = Restriction.build(base="thug")
        self.assertEqual(obj.simple_type.restriction.base, obj.raw_type)

    def test_property_raw_name(self):
        obj = Attribute.build(ref="bar")
        self.assertEqual("bar", obj.raw_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.raw_name)

        with self.assertRaises(NotImplementedError):
            Attribute.build().raw_name

    def test_get_restrictions(self):
        obj = Attribute.build()
        self.assertDictEqual({}, obj.get_restrictions())

        obj.use = "required"
        self.assertDictEqual(dict(required=1), obj.get_restrictions())

    def test_raw_base_property(self):
        obj = Attribute.build()
        self.assertIsNone(obj.raw_base)
