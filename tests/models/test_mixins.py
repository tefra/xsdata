from collections.abc import Generator, Iterator
from unittest import TestCase

from xsdata.codegen.exceptions import CodegenError
from xsdata.models.enums import FormType, Namespace
from xsdata.models.mixins import ElementBase
from xsdata.models.xsd import Alternative, ComplexType, Element, SimpleType


class ElementBaseTests(TestCase):
    def test_property_class_name(self) -> None:
        class Foo(ElementBase):
            pass

        self.assertEqual("Foo", Foo().class_name)

    def test_property_default_type(self) -> None:
        element = ElementBase()
        self.assertEqual("string", element.default_type)

        element = ElementBase()
        element.ns_map["xsd"] = Namespace.XS.uri
        self.assertEqual("xsd:string", element.default_type)

    def test_property_default_value(self) -> None:
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

    def test_property_display_help(self) -> None:
        element = ElementBase()
        self.assertIsNone(element.display_help)

    def test_property_bases(self) -> None:
        element = ElementBase()
        self.assertIsInstance(element.bases, Iterator)
        self.assertEqual([], list(element.bases))

    def test_property_has_children(self) -> None:
        element = ElementBase()
        self.assertFalse(element.has_children)

        element = Element()
        self.assertFalse(element.has_children)

        element.complex_type = ComplexType()
        self.assertTrue(element.has_children)

    def test_property_has_form(self) -> None:
        element = ElementBase()
        self.assertFalse(element.has_form)

        element.form = None
        self.assertTrue(element.has_form)

    def test_property_is_abstract(self) -> None:
        element = ElementBase()
        self.assertFalse(element.is_abstract)

        element.abstract = False
        self.assertFalse(element.is_abstract)

        element.abstract = True
        self.assertTrue(element.is_abstract)

    def test_property_is_property(self) -> None:
        element = ElementBase()
        self.assertFalse(element.is_property)

    def test_property_is_fixed(self) -> None:
        element = ElementBase()
        self.assertFalse(element.is_fixed)

        element.fixed = None
        self.assertFalse(element.is_fixed)

        element.fixed = "foo"
        self.assertTrue(element.is_fixed)

    def test_property_is_mixed(self) -> None:
        element = ElementBase()
        self.assertFalse(element.is_mixed)

    def test_property_is_nillable(self) -> None:
        element = ElementBase()
        self.assertFalse(element.is_nillable)

        element.nillable = True
        self.assertTrue(element.is_nillable)

    def test_property_is_qualified(self) -> None:
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

    def test_property_is_wildcard(self) -> None:
        element = ElementBase()
        self.assertFalse(element.is_wildcard)

    def test_property_prefix(self) -> None:
        element = ElementBase()
        self.assertIsNone(element.prefix)

        element.ref = "foo"
        self.assertIsNone(element.prefix)

        element.ref = "foo:bar"
        self.assertEqual("foo", element.prefix)

    def test_property_raw_namespace(self) -> None:
        element = ElementBase()
        self.assertIsNone(element.raw_namespace)

        element.target_namespace = "tns"
        self.assertEqual("tns", element.raw_namespace)

    def test_property_real_name(self) -> None:
        element = ElementBase()

        with self.assertRaises(CodegenError):
            element.real_name

        element.ref = "bar:foo"
        self.assertEqual("foo", element.real_name)

        element.name = "foo:bar"
        self.assertEqual("bar", element.real_name)

    def test_property_attr(self) -> None:
        element = ElementBase()
        self.assertIsInstance(element.attr_types, Iterator)
        self.assertEqual([], list(element.attr_types))

    def test_property_substitutions(self) -> None:
        element = ElementBase()
        self.assertEqual([], element.substitutions)

    def test_property_xs_prefix(self) -> None:
        element = ElementBase()
        self.assertIsNone(element.xs_prefix)

        element.ns_map = {"a": "a", "foo": Namespace.XS.uri}
        self.assertEqual("foo", element.xs_prefix)

    def test_children(self) -> None:
        one = SimpleType(id="1")
        two = ComplexType(id="10")
        three = Alternative(id="11")
        four = Alternative(id="12")

        element = Element(
            name="super",
            complex_type=two,
            simple_type=one,
            alternatives=[three, four],
        )

        children = element.children()

        self.assertIsInstance(children, Generator)
        self.assertEqual([one, two, three, four], list(children))

        children = list(element.children(lambda x: x.id == "10"))
        self.assertEqual([two], children)

        children = list(element.children(lambda x: x.id == "12"))
        self.assertEqual([four], children)

        children = list(element.children(lambda x: int(x.id) % 2 == 0))
        self.assertEqual([two, four], children)
