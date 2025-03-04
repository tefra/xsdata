import sys
from unittest import TestCase

from xsdata.codegen.exceptions import CodegenError
from xsdata.models.enums import Namespace
from xsdata.models.xsd import (
    Alternative,
    ComplexType,
    Element,
    Length,
    Restriction,
    SimpleType,
)


class ElementTests(TestCase):
    def test_normalize_max_occurs(self) -> None:
        obj = Element(min_occurs=3, max_occurs=2)
        self.assertEqual(3, obj.max_occurs)
        self.assertEqual(3, obj.min_occurs)

        obj = Element(min_occurs=3, max_occurs="unbounded")
        self.assertEqual(sys.maxsize, obj.max_occurs)
        self.assertEqual(3, obj.min_occurs)

    def test_property_is_property(self) -> None:
        obj = Element()
        self.assertTrue(obj)

    def test_property_default_type(self) -> None:
        obj = Element()
        self.assertEqual("anyType", obj.default_type)

        obj = Element()
        obj.ns_map["foo"] = Namespace.XS.uri
        self.assertEqual("foo:anyType", obj.default_type)

        obj.fixed = "aa"
        self.assertEqual("foo:string", obj.default_type)

    def test_property_bases(self) -> None:
        obj = Element()
        obj.ns_map["xs"] = Namespace.XS.uri
        self.assertEqual(["xs:anyType"], list(obj.bases))

        obj.type = "foo"
        self.assertEqual(["foo"], list(obj.bases))

        obj.type = None
        obj.complex_type = ComplexType()
        self.assertEqual([], list(obj.bases))

    def test_property_real_name(self) -> None:
        obj = Element(ref="bar")
        self.assertEqual("bar", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(CodegenError):
            obj = Element()
            obj.real_name

    def test_property_attr_types(self) -> None:
        obj = Element()
        self.assertEqual([], list(obj.attr_types))

        # Inner classes depend on the this to be None
        obj.complex_type = ComplexType()
        self.assertEqual([], list(obj.attr_types))

        restriction = Restriction(base="xs:int")
        obj.simple_type = SimpleType(restriction=restriction)
        self.assertEqual([restriction.base], list(obj.attr_types))

        obj.ref = "foo"
        self.assertEqual([obj.ref], list(obj.attr_types))

        obj.type = "bar"
        self.assertEqual([obj.type], list(obj.attr_types))

        obj.alternatives.append(Alternative(type="foo"))
        obj.alternatives.append(Alternative(type="bar"))
        obj.alternatives.append(Alternative(type="thug"))
        self.assertEqual(["bar", "foo", "bar", "thug"], list(obj.attr_types))

    def test_property_is_mixed(self) -> None:
        obj = Element()
        self.assertFalse(obj.is_mixed)

        obj.complex_type = ComplexType()
        self.assertFalse(obj.is_mixed)

        obj.complex_type.mixed = True
        self.assertTrue(obj.is_mixed)

    def test_property_substitutions(self) -> None:
        obj = Element()
        self.assertEqual([], obj.substitutions)

        obj.substitution_group = "foo   bar xs:any"
        self.assertEqual(["foo", "bar", "xs:any"], obj.substitutions)

    def test_get_restrictions(self) -> None:
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
