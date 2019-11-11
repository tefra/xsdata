from unittest import TestCase

from xsdata.models.elements import (
    ComplexContent,
    ComplexType,
    Element,
    Extension,
    Length,
    Restriction,
    SimpleType,
)


class ElementTests(TestCase):
    def test_property_real_name(self):
        obj = Element.build(ref="bar")
        self.assertEqual("bar", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(NotImplementedError):
            Element.build().real_name

    def test_property_real_type(self):
        obj = Element.build()
        self.assertEqual("xs:string", obj.real_type)

        # Inner classes depend on the this to be None
        obj.complex_type = ComplexType.build()
        self.assertIsNone(obj.real_type)

        restriction = Restriction.build(base="xs:int")
        obj.simple_type = SimpleType.build(restriction=restriction)
        self.assertEqual(restriction.base, obj.real_type)

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.real_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.real_type)

    def test_property_extensions(self):
        obj = Element.build()
        self.assertEqual([], obj.extensions)

        obj.type = "foo_bar"
        self.assertEqual(["foo_bar"], obj.extensions)

        obj.complex_type = ComplexType.build()
        self.assertEqual([], obj.extensions)

        obj.complex_type.complex_content = ComplexContent.build(
            extension=Extension.build(base="thug_life")
        )
        self.assertEqual(["thug_life"], obj.extensions)

    def test_get_restrictions(self):
        obj = Element.build()
        expected = {"required": True}
        self.assertDictEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType.build(
            restriction=Restriction.build(length=Length.build(value=9))
        )
        expected.update({"length": 9})
        self.assertDictEqual(expected, obj.get_restrictions())
