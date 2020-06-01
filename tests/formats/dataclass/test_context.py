from dataclasses import dataclass
from dataclasses import make_dataclass
from dataclasses import replace
from typing import Iterator
from unittest import mock
from unittest import TestCase

from lxml.etree import QName

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
            qname=QName("ItemsType"),
            source_qname=QName("ItemsType"),
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
            qname=QName("ItemsType"),
            source_qname=QName("ItemsType"),
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
            qname=QName("ItemsType"),
            source_qname=QName("ItemsType"),
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
        qname_foo = QName("qname_foo")
        qname_items = QName("ItemsType")
        qname_product = QName("http://example.org/prod", "product")
        qname_object = QName("object")
        qname_int = QName("int")

        # no meta name
        self.assertFalse(self.ctx.match_class_source_qname(ItemsType, qname_foo))
        self.assertTrue(self.ctx.match_class_source_qname(ItemsType, qname_items))

        # with meta name
        self.assertFalse(self.ctx.match_class_source_qname(Product, qname_items))
        self.assertTrue(self.ctx.match_class_source_qname(Product, qname_product))

        # not dataclass
        self.assertFalse(self.ctx.match_class_source_qname(object, qname_object))
        self.assertFalse(self.ctx.match_class_source_qname(int, qname_int))

    @mock.patch.object(XmlContext, "get_type_hints")
    def test_build_build_vars(self, mock_get_type_hints):
        var = XmlElement(name="foo", qname=QName("foo", "bar"), types=[int])
        mock_get_type_hints.return_value = [var]

        result = self.ctx.build(ItemsType, None)
        expected = XmlMeta(
            name="ItemsType",
            clazz=ItemsType,
            qname=QName("ItemsType"),
            source_qname=QName("ItemsType"),
            nillable=False,
            vars=[var],
        )

        self.assertEqual(expected, result)
        mock_get_type_hints.assert_called_once_with(ItemsType, None)

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_meta_namespace(self, mock_get_type_hints):
        namespace = Product.Meta.namespace
        result = self.ctx.build(Product, None)

        self.assertEqual(QName(namespace, "product"), result.qname)
        self.assertEqual(QName(namespace, "product"), result.source_qname)
        mock_get_type_hints.assert_called_once_with(Product, namespace)

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_parent_ns(self, mock_get_type_hints):
        result = self.ctx.build(ProductType, "http://xsdata")

        self.assertEqual(QName("http://xsdata", "ProductType"), str(result.qname))
        mock_get_type_hints.assert_called_once_with(ProductType, "http://xsdata")

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_no_meta_name_and_name_generator(self, *args):
        inspect = XmlContext(name_generator=lambda x: text.snake_case(x))
        result = inspect.build(ItemsType)

        self.assertEqual(QName("items_type"), str(result.qname))

    def test_build_with_no_meta_not_inherit_from_parent(self):
        @dataclass
        class Bar:
            class Meta:
                name = "bar"

        @dataclass
        class Foo(Bar):
            pass

        result = self.ctx.build(Foo)
        self.assertEqual("Foo", result.name)
        self.assertIsNone(result.qname.namespace)

    @mock.patch.object(XmlContext, "get_type_hints", return_value={})
    def test_build_with_no_dataclass_raises_exception(self, *args):
        with self.assertRaises(XmlContextError) as cm:
            self.ctx.build(int)

        self.assertEqual(f"Object {int} is not a dataclass.", str(cm.exception))

    def test_get_type_hints(self):
        result = self.ctx.get_type_hints(BookForm, None)
        self.assertIsInstance(result, Iterator)

        expected = [
            XmlElement(name="author", qname=QName("author"), types=[str],),
            XmlElement(name="title", qname=QName("title"), types=[str]),
            XmlElement(name="genre", qname=QName("genre"), types=[str]),
            XmlElement(name="price", qname=QName("price"), types=[float],),
            XmlElement(name="pub_date", qname=QName("pub_date"), types=[str],),
            XmlElement(name="review", qname=QName("review"), types=[str],),
            XmlAttribute(name="id", qname=QName("id"), types=[str]),
            XmlAttribute(
                name="lang", qname=QName("lang"), types=[str], init=False, default="en",
            ),
        ]

        result = list(result)
        self.assertEqual(expected, result)
        for var in result:
            self.assertFalse(var.dataclass)
            self.assertIsNone(var.clazz)

    def test_get_type_hints_with_dataclass_list(self):
        result = list(self.ctx.get_type_hints(Books, None))

        expected = XmlElement(
            name="book",
            qname=QName("book"),
            types=[BookForm],
            dataclass=True,
            default=list,
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
            qname=QName(None, "any_element"),
            types=[object],
            init=True,
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
