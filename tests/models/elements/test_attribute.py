from unittest import TestCase

from xsdata.models.elements import Attribute, Restriction, SimpleType


class AttributeTests(TestCase):
    def test_property_real_type(self):
        obj = Attribute.build()
        self.assertEqual("xs:string", obj.real_type)

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.real_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.real_type)

        obj.simple_type = SimpleType.build()
        self.assertIsNone(obj.real_type)

        obj.simple_type.restriction = Restriction.build(base="thug")
        self.assertEqual(obj.simple_type.restriction.base, obj.real_type)

    def test_property_real_name(self):
        obj = Attribute.build(ref="bar")
        self.assertEqual("bar", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(NotImplementedError):
            Attribute.build().real_name

    def test_get_restrictions(self):
        obj = Attribute.build()
        self.assertDictEqual({}, obj.get_restrictions())

        obj.use = "required"
        self.assertDictEqual(dict(required=1), obj.get_restrictions())

    def test_real_base_property(self):
        obj = Attribute.build()
        self.assertIsNone(obj.real_base)
