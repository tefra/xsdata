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
    def test_property_raw_name(self):
        obj = Element.build(ref="bar")
        self.assertEqual("bar", obj.raw_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.raw_name)

        with self.assertRaises(NotImplementedError):
            Element.build().raw_name

    def test_property_raw_type(self):
        obj = Element.build()
        self.assertEquals("xs:string", obj.raw_type)

        # Inner classes depend on the this to be None
        obj.complex_type = ComplexType.build()
        self.assertIsNone(obj.raw_type)

        restriction = Restriction.build(base="xs:int")
        obj.simple_type = SimpleType.build(restriction=restriction)
        self.assertEqual(restriction.base, obj.raw_type)

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.raw_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.raw_type)

    def test_property_raw_base(self):
        obj = Element.build()
        self.assertIsNone(obj.raw_base)

        obj.type = "foo_bar"
        self.assertEqual("foo_bar", obj.raw_base)

        obj.complex_type = ComplexType.build()
        self.assertIsNone(obj.raw_base)

        obj.complex_type.complex_content = ComplexContent.build(
            extension=Extension.build(base="thug_life")
        )
        self.assertEqual("thug_life", obj.raw_base)

    def test_get_restrictions(self):
        obj = Element.build()
        expected = {"required": True}
        self.assertDictEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType.build(
            restriction=Restriction.build(length=Length.build(value=9))
        )
        expected.update({"length": 9})
        self.assertDictEqual(expected, obj.get_restrictions())
