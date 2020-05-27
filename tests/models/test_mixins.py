from typing import Iterator
from typing import Optional
from unittest import TestCase

from xsdata.exceptions import SchemaValueError
from xsdata.models.enums import DataType
from xsdata.models.enums import FormType
from xsdata.models.enums import Namespace
from xsdata.models.mixins import ElementBase
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element


class ElementBaseTests(TestCase):
    def test_property_class_name(self):
        class Foo(ElementBase):
            pass

        self.assertEqual("Foo", Foo().class_name)

    def test_property_default_type(self):
        element = ElementBase()
        self.assertEqual(DataType.STRING, element.default_type)

    def test_property_default_value(self):
        element = ElementBase()
        self.assertIsNone(element.default_value)

        element.fixed = "foo"
        self.assertEqual("foo", element.default_value)

        element.default = "bar"
        self.assertEqual("bar", element.default_value)

        element.default = ""
        self.assertEqual("", element.default_value)

        element.default = None
        element.fixed = ""
        self.assertEqual("", element.default_value)

    def test_property_display_help(self):
        element = ElementBase()
        self.assertIsNone(element.display_help)

    def test_property_extends(self):
        element = ElementBase()
        self.assertIsNone(element.extends)

    def test_property_extensions(self):
        element = ElementBase()
        self.assertIsInstance(element.extensions, Iterator)
        self.assertEqual([], list(element.extensions))

        class Foo(ElementBase):
            @property
            def extends(self) -> Optional[str]:
                return "a b   c"

        self.assertEqual(["a", "b", "c"], list(Foo().extensions))

    def test_property_has_children(self):
        element = ElementBase()
        self.assertFalse(element.has_children)

        element = Element.create()
        self.assertFalse(element.has_children)

        element.complex_type = ComplexType.create()
        self.assertTrue(element.has_children)

    def test_property_has_form(self):
        element = ElementBase()
        self.assertFalse(element.has_form)

        element.form = None
        self.assertTrue(element.has_form)

    def test_property_is_abstract(self):
        element = ElementBase()
        self.assertFalse(element.is_abstract)

        element.abstract = False
        self.assertFalse(element.is_abstract)

        element.abstract = True
        self.assertTrue(element.is_abstract)

    def test_property_is_attribute(self):
        element = ElementBase()
        self.assertFalse(element.is_attribute)

    def test_property_is_fixed(self):
        element = ElementBase()
        self.assertFalse(element.is_fixed)

        element.fixed = None
        self.assertFalse(element.is_fixed)

        element.fixed = "foo"
        self.assertTrue(element.is_fixed)

    def test_property_is_mixed(self):
        element = ElementBase()
        self.assertFalse(element.is_mixed)

    def test_property_is_qualified(self):
        element = ElementBase()
        self.assertFalse(element.is_qualified)

        element.form = None
        self.assertFalse(element.is_qualified)

        element.form = FormType.UNQUALIFIED
        self.assertFalse(element.is_qualified)

        element.form = FormType.QUALIFIED
        self.assertTrue(element.is_qualified)

        element = ElementBase()
        element.form = FormType.UNQUALIFIED
        element.ref = None
        self.assertFalse(element.is_qualified)

        element.ref = "foo"
        self.assertTrue(element.is_qualified)

    def test_property_is_wildcard(self):
        element = ElementBase()
        self.assertFalse(element.is_wildcard)

    def test_property_prefix(self):
        element = ElementBase()
        self.assertIsNone(element.prefix)

        element.ref = "foo"
        self.assertIsNone(element.prefix)

        element.ref = "foo:bar"
        self.assertEqual("foo", element.prefix)

    def test_property_raw_namespace(self):
        element = ElementBase()
        self.assertIsNone(element.raw_namespace)

        element.target_namespace = "tns"
        self.assertEqual("tns", element.raw_namespace)

    def test_property_raw_type(self):
        element = ElementBase()
        self.assertIsNone(element.raw_namespace)

        element.type = "xs:int"
        self.assertEqual("xs:int", element.raw_type)

    def test_property_real_name(self):
        element = ElementBase()

        with self.assertRaises(SchemaValueError):
            element.real_name

        element.ref = "foo"
        self.assertEqual("foo", element.real_name)

        element.name = "bar"
        self.assertEqual("bar", element.real_name)

    def test_property_real_type(self):
        element = ElementBase()
        with self.assertRaises(SchemaValueError):
            element.real_type

    def test_property_substitutions(self):
        element = ElementBase()
        self.assertEqual([], element.substitutions)

    def test_schema_prefix(self):
        element = ElementBase()

        self.assertIsNone(element.schema_prefix())

        element = ElementBase(ns_map=dict(a="b", c=Namespace.XS.uri))
        self.assertEqual("c", element.schema_prefix())
