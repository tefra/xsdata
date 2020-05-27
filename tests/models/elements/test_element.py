from unittest import TestCase

from xsdata.exceptions import SchemaValueError
from xsdata.models.enums import DataType
from xsdata.models.xsd import Alternative
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import Length
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import SimpleType


class ElementTests(TestCase):
    def test_property_is_attribute(self):
        obj = Element.create()
        self.assertTrue(obj)

    def test_property_default_type(self):
        obj = Element.create()
        self.assertEqual(DataType.ANY_TYPE, obj.default_type)

    def test_property_raw_type(self):
        obj = Element.create()
        self.assertEqual("xs:anyType", obj.raw_type)

        obj.type = "foo"
        self.assertEqual("foo", obj.raw_type)

        obj.type = None
        obj.complex_type = ComplexType.create()
        self.assertIsNone(obj.raw_type)

    def test_property_real_name(self):
        obj = Element.create(ref="bar")
        self.assertEqual("bar", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(SchemaValueError):
            obj = Element.create()
            obj.real_name

    def test_property_real_type(self):
        obj = Element.create()
        self.assertIsNone(obj.real_type)

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

        obj.alternatives.append(Alternative.create(type="foo"))
        obj.alternatives.append(Alternative.create(type="bar"))
        obj.alternatives.append(Alternative.create(type="thug"))
        self.assertEqual("bar foo thug", obj.real_type)

    def test_property_extends(self):
        obj = Element.create()
        self.assertIsNone(obj.extends)

    def test_property_is_mixed(self):
        obj = Element.create()
        self.assertFalse(obj.is_mixed)

        obj.complex_type = ComplexType.create()
        self.assertFalse(obj.is_mixed)

        obj.complex_type.mixed = True
        self.assertTrue(obj.is_mixed)

    def test_property_substitutions(self):
        obj = Element.create()
        self.assertEqual([], obj.substitutions)

        obj.substitution_group = "foo   bar xs:any"
        self.assertEqual(["foo", "bar", "xs:any"], obj.substitutions)

    def test_get_restrictions(self):
        obj = Element.create(min_occurs=1, max_occurs=1)
        expected = {"min_occurs": 1, "max_occurs": 1}
        self.assertEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType.create(
            restriction=Restriction.create(length=Length.create(value=9))
        )
        expected.update({"length": 9})
        self.assertEqual(expected, obj.get_restrictions())

        obj.nillable = False
        self.assertEqual(expected, obj.get_restrictions())

        obj.nillable = True
        expected.update({"nillable": True})
        self.assertEqual(expected, obj.get_restrictions())
