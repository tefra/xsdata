import sys
from dataclasses import dataclass
from dataclasses import make_dataclass
from dataclasses import replace
from typing import get_type_hints
from typing import Iterator
from typing import List
from typing import Union
from unittest import mock
from unittest import TestCase

import pytest

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter03prod import Product
from tests.fixtures.defxmlschema.chapter05prod import ProductType
from tests.fixtures.defxmlschema.chapter13 import ItemsType
from tests.fixtures.defxmlschema.chapter16 import Umbrella
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.formats.dataclass.models.elements import XmlAttribute
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.models.elements import XmlWildcard
from xsdata.utils import text


class XmlContextTests(TestCase):
    def setUp(self):
        self.ctx = XmlContext()
        super().setUp()

    @mock.patch.object(XmlContext, "find_subclass")
    @mock.patch.object(XmlContext, "build")
    def test_fetch(self, mock_build, mock_find_subclass):
        meta = XmlMeta(
            name="ItemsType",
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
            name="ItemsType",
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
            name="ItemsType",
            clazz=ItemsType,
            qname="ItemsType",
            source_qname="ItemsType",
            nillable=False,
        )
        xsi_meta = replace(meta, name="XsiType")

        mock_build.side_effect = [meta, xsi_meta]
        mock_find_subclass.return_value = xsi_meta
        actual = self.ctx.fetch(ItemsType, xsi_type="foo")
        self.assertEqual(xsi_meta, actual)
        mock_find_subclass.assert_called_once_with(ItemsType, "foo")

    def test_find_subclass(self):
        a = make_dataclass("A", fields=[])
        b = make_dataclass("B", fields=[], bases=(a,))
        c = make_dataclass("C", fields=[], bases=(a,))

        self.assertEqual(b, self.ctx.find_subclass(a, "B"))
        self.assertEqual(b, self.ctx.find_subclass(c, "B"))
        self.assertEqual(a, self.ctx.find_subclass(b, "A"))
        self.assertEqual(a, self.ctx.find_subclass(c, "A"))
        self.assertIsNone(self.ctx.find_subclass(c, "What"))

    def test_match_class_name(self):
        # no meta name
        self.assertFalse(self.ctx.match_class_source_qname(ItemsType, "qname_foo"))
        self.assertTrue(self.ctx.match_class_source_qname(ItemsType, "ItemsType"))

        # with meta name
        product_qname = "{http://example.org/prod}product"
        self.assertFalse(self.ctx.match_class_source_qname(Product, "ItemsType"))
        self.assertTrue(self.ctx.match_class_source_qname(Product, product_qname))

        # not dataclass
        self.assertFalse(self.ctx.match_class_source_qname(object, "object"))
        self.assertFalse(self.ctx.match_class_source_qname(int, "int"))

    @mock.patch.object(XmlContext, "get_type_hints")
    def test_build_build_vars(self, mock_get_type_hints):
        var = XmlElement(name="foo", qname="{foo}bar", types=[int])
        mock_get_type_hints.return_value = [var]

        result = self.ctx.build(ItemsType, None)
        expected = XmlMeta(
            name="ItemsType",
            clazz=ItemsType,
            qname="ItemsType",
            source_qname="ItemsType",
            nillable=False,
            vars=[var],
        )

        self.assertEqual(expected, result)
        mock_get_type_hints.assert_called_once_with(ItemsType, None)

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_meta_namespace(self, mock_get_type_hints):
        namespace = Product.Meta.namespace
        result = self.ctx.build(Product, None)

        self.assertEqual(text.qname(namespace, "product"), result.qname)
        self.assertEqual(text.qname(namespace, "product"), result.source_qname)
        mock_get_type_hints.assert_called_once_with(Product, namespace)

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_parent_ns(self, mock_get_type_hints):
        result = self.ctx.build(ProductType, "http://xsdata")

        self.assertEqual(text.qname("http://xsdata", "ProductType"), str(result.qname))
        mock_get_type_hints.assert_called_once_with(ProductType, "http://xsdata")

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_no_meta_name_and_name_generator(self, *args):
        inspect = XmlContext(name_generator=lambda x: text.snake_case(x))
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
        self.assertEqual("Foo", result.name)
        self.assertEqual("Foo", result.qname)

        result = self.ctx.build(Thug)
        self.assertEqual("thug", result.name)
        self.assertEqual("thug", result.qname)

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_no_dataclass_raises_exception(self, *args):
        with self.assertRaises(XmlContextError) as cm:
            self.ctx.build(int)

        self.assertEqual(f"Object {int} is not a dataclass.", str(cm.exception))

    def test_get_type_hints(self):
        result = self.ctx.get_type_hints(BookForm, None)
        self.assertIsInstance(result, Iterator)

        expected = [
            XmlElement(name="author", qname="author", types=[str]),
            XmlElement(name="title", qname="title", types=[str]),
            XmlElement(name="genre", qname="genre", types=[str]),
            XmlElement(name="price", qname="price", types=[float]),
            XmlElement(name="pub_date", qname="pub_date", types=[str]),
            XmlElement(name="review", qname="review", types=[str]),
            XmlAttribute(name="id", qname="id", types=[str]),
            XmlAttribute(
                name="lang", qname="lang", types=[str], init=False, default="en"
            ),
        ]

        result = list(result)
        self.assertEqual(expected, result)
        for var in result:
            self.assertFalse(var.dataclass)
            self.assertIsNone(var.clazz)

    @pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python >= 3.7")
    def test_get_type_hints_with_union_types(self):
        @dataclass
        class Example:
            bool: bool
            int: int
            union: Union[int, bool]

        result = list(self.ctx.get_type_hints(Example, None))
        expected = [
            XmlText(name="bool", qname="bool", types=[bool]),
            XmlText(name="int", qname="int", types=[int]),
            XmlText(name="union", qname="union", types=[bool, int]),
        ]

        self.assertEqual(expected, result)

    def test_get_type_hints_with_dataclass_list(self):
        result = list(self.ctx.get_type_hints(Books, None))

        expected = XmlElement(
            name="book",
            qname="book",
            types=[BookForm],
            dataclass=True,
            default=list,
            list_element=True,
        )

        self.assertTrue(expected.is_list)
        self.assertEqual(1, len(result))
        self.assertEqual(expected, result[0])
        self.assertTrue(result[0].dataclass)
        self.assertEqual(BookForm, result[0].clazz)

    def test_get_type_hints_with_wildcard_element(self):
        result = list(self.ctx.get_type_hints(Umbrella, None))

        expected = XmlWildcard(
            name="any_element",
            qname="any_element",
            types=[object],
            init=True,
            mixed=False,
            nillable=False,
            dataclass=False,
            default=None,
            namespaces=["##any"],
        )

        self.assertEqual(1, len(result))
        self.assertEqual(expected, result[0])

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
