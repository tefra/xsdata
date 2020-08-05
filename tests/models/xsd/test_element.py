from unittest import TestCase

from xsdata.exceptions import SchemaValueError
from xsdata.models.enums import Namespace
from xsdata.models.xsd import Alternative
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import Length
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import SimpleType


class ElementTests(TestCase):
    def test_property_is_attribute(self):
        obj = Element()
        self.assertTrue(obj)

    def test_property_default_type(self):
        obj = Element()
        self.assertEqual("anyType", obj.default_type)

        obj = Element()
        obj.ns_map["foo"] = Namespace.XS.uri
        self.assertEqual("foo:anyType", obj.default_type)

    def test_property_raw_type(self):
        obj = Element()
        obj.ns_map["xs"] = Namespace.XS.uri
        self.assertEqual("xs:anyType", obj.raw_type)

        obj.type = "foo"
        self.assertEqual("foo", obj.raw_type)

        obj.type = None
        obj.complex_type = ComplexType()
        self.assertIsNone(obj.raw_type)

    def test_property_real_name(self):
        obj = Element(ref="bar")
        self.assertEqual("bar", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(SchemaValueError):
            obj = Element()
            obj.real_name

    def test_property_real_type(self):
        obj = Element()
        self.assertEqual("", obj.real_type)

        # Inner classes depend on the this to be None
        obj.complex_type = ComplexType()
        self.assertEqual("", obj.real_type)

        restriction = Restriction(base="xs:int")
        obj.simple_type = SimpleType(restriction=restriction)
        self.assertEqual(restriction.base, obj.real_type)

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.real_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.real_type)

        obj.alternatives.append(Alternative(type="foo"))
        obj.alternatives.append(Alternative(type="bar"))
        obj.alternatives.append(Alternative(type="thug"))
        self.assertEqual("bar foo thug", obj.real_type)

    def test_property_extensions(self):
        obj = Element()
        self.assertEqual([], list(obj.extensions))

    def test_property_is_mixed(self):
        obj = Element()
        self.assertFalse(obj.is_mixed)

        obj.complex_type = ComplexType()
        self.assertFalse(obj.is_mixed)

        obj.complex_type.mixed = True
        self.assertTrue(obj.is_mixed)

    def test_property_substitutions(self):
        obj = Element()
        self.assertEqual([], obj.substitutions)

        obj.substitution_group = "foo   bar xs:any"
        self.assertEqual(["foo", "bar", "xs:any"], obj.substitutions)

    def test_get_restrictions(self):
        obj = Element(min_occurs=1, max_occurs=1)
        expected = {"min_occurs": 1, "max_occurs": 1}
        self.assertEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType(restriction=Restriction(length=Length(value=9)))
        expected["length"] = 9
        self.assertEqual(expected, obj.get_restrictions())

        obj.nillable = False
        self.assertEqual(expected, obj.get_restrictions())

        obj.nillable = True
        expected["nillable"] = True
        self.assertEqual(expected, obj.get_restrictions())

        obj.type = "NMTOKENS"
        expected["tokens"] = True
        self.assertEqual(expected, obj.get_restrictions())
