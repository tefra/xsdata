import sys
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from dataclasses import make_dataclass
from dataclasses import replace
from datetime import datetime
from typing import Generator
from typing import get_type_hints
from typing import Iterator
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union
from unittest import mock
from unittest import TestCase

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from tests.fixtures.books import BooksForm
from tests.fixtures.defxmlschema.chapter03prod import Product
from tests.fixtures.defxmlschema.chapter05prod import ProductType
from tests.fixtures.defxmlschema.chapter13 import ItemsType
from tests.fixtures.defxmlschema.chapter16 import Umbrella
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.models.datatype import XmlDate
from xsdata.models.enums import DataType
from xsdata.utils import text
from xsdata.utils.constants import return_input
from xsdata.utils.constants import return_true
from xsdata.utils.namespaces import build_qname


class XmlContextTests(TestCase):
    def setUp(self):
        self.ctx = XmlContext()
        super().setUp()

    @mock.patch.object(XmlContext, "find_subclass")
    @mock.patch.object(XmlContext, "build")
    def test_fetch(self, mock_build, mock_find_subclass):
        meta = XmlMeta(
            clazz=ItemsType,
            qname="ItemsType",
            source_qname="ItemsType",
            nillable=False,
        )
        mock_build.return_value = meta
        actual = self.ctx.fetch(ItemsType, "foo")
        self.assertEqual(meta, actual)
        self.assertEqual(0, mock_find_subclass.call_count)
        mock_build.assert_called_once_with(ItemsType, "foo")

    @mock.patch.object(XmlContext, "find_subclass")
    @mock.patch.object(XmlContext, "build")
    def test_fetch_with_xsi_type_and_subclass_not_found(
        self, mock_build, mock_find_subclass
    ):
        meta = XmlMeta(
            clazz=ItemsType,
            qname="ItemsType",
            source_qname="ItemsType",
            nillable=False,
        )

        mock_build.return_value = meta
        mock_find_subclass.return_value = None
        actual = self.ctx.fetch(ItemsType, xsi_type="foo")
        self.assertEqual(meta, actual)
        mock_find_subclass.assert_called_once_with(ItemsType, "foo")

    @mock.patch.object(XmlContext, "find_subclass")
    @mock.patch.object(XmlContext, "build")
    def test_fetch_with_xsi_type_and_subclass_found(
        self, mock_build, mock_find_subclass
    ):
        meta = XmlMeta(
            clazz=ItemsType,
            qname="ItemsType",
            source_qname="ItemsType",
            nillable=False,
        )
        xsi_meta = replace(meta, qname="XsiType")

        mock_build.side_effect = [meta, xsi_meta]
        mock_find_subclass.return_value = xsi_meta
        actual = self.ctx.fetch(ItemsType, xsi_type="foo")
        self.assertEqual(xsi_meta, actual)
        mock_find_subclass.assert_called_once_with(ItemsType, "foo")

    def test_find(self):
        self.assertIsNone(self.ctx.find_type(str(DataType.FLOAT)))
        self.assertEqual(BookForm, self.ctx.find_type("{urn:books}BookForm"))

        self.ctx.xsi_cache["{urn:books}BookForm"].append(BooksForm)
        self.assertEqual(BooksForm, self.ctx.find_type("{urn:books}BookForm"))

    def test_find_type_by_fields(self):
        field_names = {f.name for f in fields(BookForm)}
        self.assertEqual(BookForm, self.ctx.find_type_by_fields(field_names))
        self.assertIsNone(self.ctx.find_type_by_fields({"please", "dont", "exist"}))

    def test_find_subclass(self):
        a = make_dataclass("A", fields=[])
        b = make_dataclass("B", fields=[], bases=(a,))
        c = make_dataclass("C", fields=[], bases=(a,))
        other = make_dataclass("Other", fields=[])

        self.assertEqual(b, self.ctx.find_subclass(a, "B"))
        self.assertEqual(b, self.ctx.find_subclass(c, "B"))
        self.assertEqual(a, self.ctx.find_subclass(b, "A"))
        self.assertEqual(a, self.ctx.find_subclass(c, "A"))
        self.assertIsNone(self.ctx.find_subclass(c, "Unknown"))
        self.assertIsNone(self.ctx.find_subclass(c, "Other"))

    @mock.patch.object(XmlContext, "get_type_hints")
    def test_build_build_vars(self, mock_get_type_hints):
        var = XmlVar(element=True, name="foo", qname="{foo}bar", types=[int])
        mock_get_type_hints.return_value = [var]

        result = self.ctx.build(ItemsType, None)
        expected = XmlMeta(
            clazz=ItemsType,
            qname="ItemsType",
            source_qname="ItemsType",
            nillable=False,
            vars=[var],
        )

        self.assertEqual(expected, result)
        mock_get_type_hints.assert_called_once_with(
            ItemsType, None, return_input, return_input
        )

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_meta_namespace(self, mock_get_type_hints):
        namespace = Product.Meta.namespace
        result = self.ctx.build(Product, None)

        self.assertEqual(build_qname(namespace, "product"), result.qname)
        self.assertEqual(build_qname(namespace, "product"), result.source_qname)
        mock_get_type_hints.assert_called_once_with(
            Product, namespace, return_input, return_input
        )

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_parent_ns(self, mock_get_type_hints):
        result = self.ctx.build(ProductType, "http://xsdata")

        self.assertEqual(build_qname("http://xsdata", "ProductType"), str(result.qname))
        mock_get_type_hints.assert_called_once_with(
            ProductType, "http://xsdata", return_input, return_input
        )

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_no_meta_name_and_name_generator(self, *args):
        inspect = XmlContext(element_name_generator=lambda x: text.snake_case(x))
        result = inspect.build(ItemsType)

        self.assertEqual("items_type", result.qname)

    def test_build_with_no_meta_not_inherit_from_parent(self):
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

        result = self.ctx.build(Foo)
        self.assertEqual("Foo", result.qname)

        result = self.ctx.build(Thug)
        self.assertEqual("thug", result.qname)

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_no_dataclass_raises_exception(self, *args):
        with self.assertRaises(XmlContextError) as cm:
            self.ctx.build(int)

        self.assertEqual(f"Object {int} is not a dataclass.", str(cm.exception))

    def test_get_type_hints(self):
        result = self.ctx.get_type_hints(BookForm, None, text.pascal_case, str.upper)
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

    def test_get_type_hints_with_union_types(self):
        @dataclass
        class Example:
            bool: bool
            int: int
            union: Union[int, bool]

        result = list(
            self.ctx.get_type_hints(Example, None, return_input, return_input)
        )
        expected = [
            XmlVar(element=True, name="bool", qname="bool", types=[bool]),
            XmlVar(element=True, name="int", qname="int", types=[int]),
            XmlVar(element=True, name="union", qname="union", types=[int, bool]),
        ]

        if sys.version_info < (3, 7):
            expected[2].types.remove(bool)

        self.assertEqual(expected, result)

    def test_get_type_hints_with_dataclass_list(self):
        result = list(self.ctx.get_type_hints(Books, None, return_input, return_input))

        expected = XmlVar(
            element=True,
            name="book",
            qname="book",
            types=[BookForm],
            dataclass=True,
            default=list,
            list_element=True,
        )

        self.assertTrue(expected.list_element)
        self.assertEqual(1, len(result))
        self.assertEqual(expected, result[0])
        self.assertTrue(result[0].dataclass)
        self.assertEqual(BookForm, result[0].clazz)

    def test_get_type_hints_with_wildcard_element(self):
        actual = self.ctx.get_type_hints(Umbrella, None, return_input, return_input)

        expected = XmlVar(
            wildcard=True,
            name="any_element",
            qname="any_element",
            types=[object],
            default=None,
            namespaces=["##any"],
        )

        self.assertEqual([expected], list(actual))

    def test_get_type_hints_with_undefined_types(self):
        @dataclass
        class Currency:
            id: int = field(metadata=dict(type="Attribute", name="ID"))
            iso_code: str = field(metadata=dict(name="CharCode"))
            nominal: int = field(metadata=dict(name="Nominal"))

        @dataclass
        class Currencies:
            name: str = field(metadata=dict(type="Attribute"))
            updated: datetime = field(metadata=dict(type="Attribute", format="%M-%D"))
            values: List[Currency] = field(default_factory=list)

        expected = [
            XmlVar(attribute=True, name="id", qname="ID", types=[int]),
            XmlVar(element=True, name="iso_code", qname="CharCode", types=[str]),
            XmlVar(element=True, name="nominal", qname="Nominal", types=[int]),
        ]
        actual = self.ctx.get_type_hints(Currency, None, return_input, return_input)
        self.assertEqual(expected, list(actual))

        expected = [
            XmlVar(attribute=True, name="name", qname="name", types=[str]),
            XmlVar(
                attribute=True,
                name="updated",
                qname="updated",
                types=[datetime],
                format="%M-%D",
            ),
            XmlVar(
                element=True,
                name="values",
                qname="values",
                dataclass=True,
                list_element=True,
                default=list,
                types=[Currency],
            ),
        ]

        actual = self.ctx.get_type_hints(Currencies, None, return_input, return_input)
        self.assertEqual(expected, list(actual))

    def test_get_type_hints_with_choices(self):
        actual = self.ctx.get_type_hints(Node, "bar", return_input, return_input)
        self.assertIsInstance(actual, Generator)
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
                    types=[Node],
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
        self.assertEqual(expected, list(actual)[0])

    def test_get_type_hints_with_typevars(self):

        A = TypeVar("A", str, int)
        B = TypeVar("B", bound=object)

        foo = make_dataclass("Foo", [("a", A), ("b", B), ("c", List[B])])

        actual = self.ctx.get_type_hints(foo, None, return_input, return_input)
        expected = [
            XmlVar(name="a", qname="a", element=True, types=[int, str]),
            XmlVar(name="b", qname="b", any_type=True, element=True, types=[object]),
            XmlVar(
                name="c",
                qname="c",
                any_type=True,
                list_element=True,
                element=True,
                types=[object],
            ),
        ]

        self.assertEqual(expected, list(actual))

    def test_get_type_hints_with_no_dataclass(self):
        with self.assertRaises(TypeError):
            list(self.ctx.get_type_hints(self.__class__, None))

    def test_resolve_namespaces(self):
        self.assertEqual(
            ["foo"], self.ctx.resolve_namespaces(XmlType.ELEMENT, "foo", "bar")
        )

        self.assertEqual([], self.ctx.resolve_namespaces(XmlType.ELEMENT, "", "bar"))

        self.assertEqual(
            ["bar"], self.ctx.resolve_namespaces(XmlType.ELEMENT, None, "bar")
        )

        self.assertEqual(
            [], self.ctx.resolve_namespaces(XmlType.ATTRIBUTE, None, "bar")
        )

        self.assertEqual(
            ["p"], self.ctx.resolve_namespaces(XmlType.WILDCARD, None, "p")
        )

        self.assertEqual(
            ["##any"], self.ctx.resolve_namespaces(XmlType.WILDCARD, "##any", "p")
        )

        self.assertEqual(
            ["##any"],
            self.ctx.resolve_namespaces(XmlType.WILDCARD, "##targetNamespace", ""),
        )

        self.assertEqual(
            ["##any"],
            self.ctx.resolve_namespaces(XmlType.WILDCARD, "##targetNamespace", None),
        )

        self.assertEqual(
            ["p"],
            self.ctx.resolve_namespaces(XmlType.WILDCARD, "##targetNamespace", "p"),
        )

        self.assertEqual(
            [""], self.ctx.resolve_namespaces(XmlType.WILDCARD, "##local", "p")
        )

        self.assertEqual(
            ["!p"], self.ctx.resolve_namespaces(XmlType.WILDCARD, "##other", "p")
        )

        self.assertEqual(
            ["", "!p"],
            sorted(
                self.ctx.resolve_namespaces(XmlType.WILDCARD, "##other   ##local", "p")
            ),
        )

        self.assertEqual(
            ["foo", "p"],
            sorted(
                self.ctx.resolve_namespaces(
                    XmlType.WILDCARD, "##targetNamespace   foo", "p"
                )
            ),
        )

    def test_is_derived(self):
        a = make_dataclass("A", fields=[])
        b = make_dataclass("B", fields=[], bases=(a,))
        c = make_dataclass("C", fields=[], bases=(a,))
        d = make_dataclass("D", fields=[])

        self.assertTrue(self.ctx.is_derived(c(), b))
        self.assertTrue(self.ctx.is_derived(b(), c))
        self.assertTrue(self.ctx.is_derived(a(), b))
        self.assertTrue(self.ctx.is_derived(a(), c))
        self.assertTrue(self.ctx.is_derived(a(), a))
        self.assertFalse(self.ctx.is_derived(a(), d))
        self.assertFalse(self.ctx.is_derived(None, d))

    def test_is_element_list(self):
        @dataclass
        class Fixture:
            list_int: List[int]
            list_list_int: List[List[int]]

        type_hints = get_type_hints(Fixture)

        self.assertTrue(self.ctx.is_element_list(type_hints["list_int"], False))
        self.assertFalse(self.ctx.is_element_list(type_hints["list_int"], True))

        self.assertTrue(self.ctx.is_element_list(type_hints["list_list_int"], False))
        self.assertTrue(self.ctx.is_element_list(type_hints["list_list_int"], True))

    def test_default_xml_type(self):
        cls = make_dataclass("a", [("x", int)])
        self.assertEqual(XmlType.TEXT, self.ctx.default_xml_type(cls))

        cls = make_dataclass("b", [("x", int), ("y", int)])
        self.assertEqual(XmlType.ELEMENT, self.ctx.default_xml_type(cls))

        cls = make_dataclass(
            "c", [("x", int), ("y", int, field(metadata=dict(type="Text")))]
        )
        self.assertEqual(XmlType.ELEMENT, self.ctx.default_xml_type(cls))

        cls = make_dataclass(
            "d", [("x", int), ("y", int, field(metadata=dict(type="Element")))]
        )
        self.assertEqual(XmlType.TEXT, self.ctx.default_xml_type(cls))

        with self.assertRaises(XmlContextError) as cm:
            cls = make_dataclass(
                "e",
                [
                    ("x", int, field(metadata=dict(type="Text"))),
                    ("y", int, field(metadata=dict(type="Text"))),
                ],
            )
            self.ctx.default_xml_type(cls)

        self.assertEqual(
            "Dataclass `e` includes more than one text node!", str(cm.exception)
        )


@dataclass
class Node:

    compound: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {"name": "node", "type": Type["Node"], "namespace": "foo"},
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
