from unittest import TestCase

from xsdata.models.elements import (
    ComplexType,
    Element,
    Length,
    Restriction,
    SimpleType,
)


class ElementTests(TestCase):
    def test_property_is_attribute(self):
        obj = Element.create()
        self.assertTrue(obj)

    def test_property_real_name(self):
        obj = Element.create(ref="bar")
        self.assertEqual("bar", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(NotImplementedError):
            obj = Element.create()
            obj.real_name

    def test_property_real_type(self):
        obj = Element.create()
        self.assertEqual("xs:string", obj.real_type)

        # Inner classes depend on the this to be None
        obj.complex_type = ComplexType.create()
        self.assertIsNone(obj.real_type)

        restriction = Restriction.create(base="xs:int")
        obj.simple_type = SimpleType.create(restriction=restriction)
        self.assertEqual(restriction.base, obj.real_type)

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.real_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.real_type)

    def test_property_extends(self):
        obj = Element.create()
        self.assertIsNone(obj.extends)

    def test_get_restrictions(self):
        obj = Element.create()
        expected = {"required": True}
        self.assertEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType.create(
            restriction=Restriction.create(length=Length.create(value=9))
        )
        expected.update({"length": 9})
        self.assertEqual(expected, obj.get_restrictions())
