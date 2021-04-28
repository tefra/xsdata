import sys
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from dataclasses import make_dataclass
from typing import get_type_hints
from typing import Iterator
from typing import List
from typing import Type
from unittest import mock
from unittest import TestCase

from tests.fixtures.books import BookForm
from tests.fixtures.defxmlschema.chapter03prod import Product
from tests.fixtures.defxmlschema.chapter05prod import ProductType
from tests.fixtures.defxmlschema.chapter13 import ItemsType
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.builders import XmlMetaBuilder
from xsdata.formats.dataclass.models.builders import XmlVarBuilder
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.models.datatype import XmlDate
from xsdata.utils import text
from xsdata.utils.constants import return_input
from xsdata.utils.constants import return_true
from xsdata.utils.namespaces import build_qname


class XmlMetaBuilderTests(TestCase):
    @mock.patch.object(XmlMetaBuilder, "build_vars")
    def test_build(self, mock_build_vars):
        var = XmlVar(element=True, name="foo", qname="{foo}bar", types=[int])
        mock_build_vars.return_value = [var]

        result = XmlMetaBuilder.build(ItemsType, None, return_input, return_input)
        expected = XmlMeta(
            clazz=ItemsType,
            qname="ItemsType",
            source_qname="ItemsType",
            nillable=False,
            vars=[var],
        )

        self.assertEqual(expected, result)
        mock_build_vars.assert_called_once_with(
            ItemsType, None, return_input, return_input
        )

    @mock.patch.object(XmlMetaBuilder, "build_vars", return_value=[])
    def test_build_when_class_has_namespace(self, mock_build_vars):
        namespace = Product.Meta.namespace
        result = XmlMetaBuilder.build(Product, None, return_input, return_input)

        self.assertEqual(build_qname(namespace, "product"), result.qname)
        self.assertEqual(build_qname(namespace, "product"), result.source_qname)
        mock_build_vars.assert_called_once_with(
            Product, namespace, return_input, return_input
        )

    @mock.patch.object(XmlMetaBuilder, "build_vars", return_value=[])
    def test_build_with_parent_namespace(self, mock_build_vars):
        result = XmlMetaBuilder.build(
            ProductType, "http://xsdata", return_input, return_input
        )

        self.assertEqual(build_qname("http://xsdata", "ProductType"), result.qname)
        mock_build_vars.assert_called_once_with(
            ProductType, "http://xsdata", return_input, return_input
        )

    @mock.patch.object(XmlMetaBuilder, "build_vars", return_value=[])
    def test_build_with_no_meta_name_and_name_generator(self, *args):
        result = XmlMetaBuilder.build(ProductType, None, text.snake_case, return_input)

        self.assertEqual("product_type", result.qname)

    def test_build_block_meta_inheritance(self):
        @dataclass
        class Bar:
            class Meta:
                name = "bar"

        @dataclass
        class Foo(Bar):
            pass

        @dataclass
        class Thug(Bar):
            class Meta:
                name = "thug"

        result = XmlMetaBuilder.build(Foo, None, return_input, return_input)
        self.assertEqual("Foo", result.qname)

        result = XmlMetaBuilder.build(Thug, None, return_input, return_input)
        self.assertEqual("thug", result.qname)

    def test_build_with_no_dataclass_raises_exception(self, *args):
        with self.assertRaises(XmlContextError) as cm:
            XmlMetaBuilder.build(int, None, return_input, return_input)

        self.assertEqual(f"Object {int} is not a dataclass.", str(cm.exception))

    def test_build_vars(self):
        result = XmlMetaBuilder.build_vars(BookForm, None, text.pascal_case, str.upper)
        self.assertIsInstance(result, Iterator)

        expected = [
            XmlVar(element=True, name="author", qname="Author", types=[str]),
            XmlVar(element=True, name="title", qname="Title", types=[str]),
            XmlVar(element=True, name="genre", qname="Genre", types=[str]),
            XmlVar(element=True, name="price", qname="Price", types=[float]),
            XmlVar(element=True, name="pub_date", qname="PubDate", types=[XmlDate]),
            XmlVar(element=True, name="review", qname="Review", types=[str]),
            XmlVar(attribute=True, name="id", qname="ID", types=[str]),
            XmlVar(
                attribute=True,
                name="lang",
                qname="LANG",
                types=[str],
                init=False,
                default="en",
            ),
        ]

        result = list(result)
        self.assertEqual(expected, result)
        for var in result:
            self.assertFalse(var.dataclass)
            self.assertIsNone(var.clazz)

    def test_default_xml_type(self):
        cls = make_dataclass("a", [("x", int)])
        self.assertEqual(XmlType.TEXT, XmlMetaBuilder.default_xml_type(cls))

        cls = make_dataclass("b", [("x", int), ("y", int)])
        self.assertEqual(XmlType.ELEMENT, XmlMetaBuilder.default_xml_type(cls))

        cls = make_dataclass(
            "c", [("x", int), ("y", int, field(metadata=dict(type="Text")))]
        )
        self.assertEqual(XmlType.ELEMENT, XmlMetaBuilder.default_xml_type(cls))

        cls = make_dataclass(
            "d", [("x", int), ("y", int, field(metadata=dict(type="Element")))]
        )
        self.assertEqual(XmlType.TEXT, XmlMetaBuilder.default_xml_type(cls))

        with self.assertRaises(XmlContextError) as cm:
            cls = make_dataclass(
                "e",
                [
                    ("x", int, field(metadata=dict(type="Text"))),
                    ("y", int, field(metadata=dict(type="Text"))),
                ],
            )
            XmlMetaBuilder.default_xml_type(cls)

        self.assertEqual(
            "Dataclass `e` includes more than one text node!", str(cm.exception)
        )


class XmlVarBuilderTests(TestCase):
    def setUp(self) -> None:
        self.builder = XmlVarBuilder(
            default_xml_type=XmlType.ELEMENT,
            parent_ns=None,
            element_name_generator=return_input,
            attribute_name_generator=return_input,
        )

        super().setUp()

    def test_build_with_choice_field(self):
        globalns = sys.modules[CompoundFieldExample.__module__].__dict__
        type_hints = get_type_hints(CompoundFieldExample)
        class_field = fields(CompoundFieldExample)[0]

        builder = XmlVarBuilder(XmlType.ELEMENT, "bar", return_input, return_input)

        actual = builder.build(
            "compound",
            type_hints["compound"],
            class_field.metadata,
            True,
            list,
            globalns,
        )
        expected = XmlVar(
            elements=True,
            name="compound",
            qname="compound",
            list_element=True,
            any_type=True,
            default=list,
            choices=[
                XmlVar(
                    element=True,
                    name="compound",
                    qname="{foo}node",
                    dataclass=True,
                    types=[CompoundFieldExample],
                    namespaces=["foo"],
                    derived=False,
                ),
                XmlVar(
                    element=True,
                    name="compound",
                    qname="{bar}x",
                    tokens=True,
                    types=[str],
                    namespaces=["bar"],
                    derived=False,
                    default=return_true,
                    format="Nope",
                ),
                XmlVar(
                    element=True,
                    name="compound",
                    qname="{bar}y",
                    nillable=True,
                    types=[int],
                    namespaces=["bar"],
                    derived=False,
                ),
                XmlVar(
                    element=True,
                    name="compound",
                    qname="{bar}z",
                    nillable=False,
                    types=[int],
                    namespaces=["bar"],
                    derived=True,
                ),
                XmlVar(
                    element=True,
                    name="compound",
                    qname="{bar}o",
                    nillable=False,
                    types=[object],
                    namespaces=["bar"],
                    derived=True,
                    any_type=True,
                ),
                XmlVar(
                    element=True,
                    name="compound",
                    qname="{bar}p",
                    types=[float],
                    namespaces=["bar"],
                    default=1.1,
                ),
                XmlVar(
                    wildcard=True,
                    name="compound",
                    qname="{http://www.w3.org/1999/xhtml}any",
                    types=[object],
                    namespaces=["http://www.w3.org/1999/xhtml"],
                    derived=True,
                    any_type=False,
                ),
            ],
            types=[object],
        )
        self.assertEqual(expected, actual)

    def test_resolve_namespaces(self):
        func = self.builder.resolve_namespaces
        self.builder.parent_ns = "bar"

        self.assertEqual(["foo"], func(XmlType.ELEMENT, "foo"))
        self.assertEqual([], func(XmlType.ELEMENT, ""))
        self.assertEqual(["bar"], func(XmlType.ELEMENT, None))

        self.assertEqual([], func(XmlType.ATTRIBUTE, None))

        self.assertEqual(["bar"], func(XmlType.WILDCARD, None))
        self.assertEqual(["##any"], func(XmlType.WILDCARD, "##any"))

        self.builder.parent_ns = ""
        self.assertEqual(["##any"], func(XmlType.WILDCARD, "##targetNamespace"))

        self.builder.parent_ns = None
        self.assertEqual(["##any"], func(XmlType.WILDCARD, "##targetNamespace"))

        self.builder.parent_ns = "p"
        self.assertEqual(["p"], func(XmlType.WILDCARD, "##targetNamespace"))
        self.assertEqual([""], func(XmlType.WILDCARD, "##local"))
        self.assertEqual(["!p"], func(XmlType.WILDCARD, "##other"))
        self.assertEqual(
            ["", "!p"], sorted(func(XmlType.WILDCARD, "##other   ##local"))
        )

        self.assertEqual(
            ["foo", "p"], sorted(func(XmlType.WILDCARD, "##targetNamespace   foo"))
        )

    def test_analyze_types(self):
        actual = self.builder.analyze_types((list, list, int, str))
        self.assertEqual((list, list, [int, str]), actual)

        actual = self.builder.analyze_types((int, str))
        self.assertEqual((None, None, [int, str]), actual)

        actual = self.builder.analyze_types((dict, int, str))
        self.assertEqual((dict, None, [int, str]), actual)

        with self.assertRaises(XmlContextError):
            self.builder.analyze_types((dict, list, list, int, str))

    def test_build_xml_type(self):
        self.builder.default_xml_type = XmlType.WILDCARD
        self.assertEqual(XmlType.WILDCARD, self.builder.build_xml_type(None, False))
        self.assertEqual(XmlType.ELEMENT, self.builder.build_xml_type("", True))
        self.assertEqual(XmlType.TEXT, self.builder.build_xml_type(XmlType.TEXT, True))


@dataclass
class CompoundFieldExample:

    compound: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "node",
                    "type": Type["CompoundFieldExample"],
                    "namespace": "foo",
                },
                {
                    "name": "x",
                    "type": List[str],
                    "tokens": True,
                    "default_factory": return_true,
                    "format": "Nope",
                },
                {"name": "y", "type": List[int], "nillable": True},
                {"name": "z", "type": List[int]},
                {"name": "o", "type": object},
                {"name": "p", "type": float, "fixed": True, "default": 1.1},
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )
