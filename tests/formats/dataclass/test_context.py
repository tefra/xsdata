from dataclasses import dataclass
from typing import Iterator
from unittest import mock
from unittest import TestCase

from lxml.etree import QName

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter02.example0210 import Product
from tests.fixtures.defxmlschema.chapter05.chapter05prod import ProductType
from tests.fixtures.defxmlschema.chapter11.example1101 import TextType
from tests.fixtures.defxmlschema.chapter13.chapter13 import ItemsType
from xsdata.exceptions import ModelInspectionError
from xsdata.formats.dataclass.context import ModelContext
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.formats.dataclass.models.context import ClassMeta
from xsdata.formats.dataclass.models.context import XmlAttribute
from xsdata.formats.dataclass.models.context import XmlElement
from xsdata.formats.dataclass.models.context import XmlWildcard
from xsdata.utils import text


class ModelContextTests(TestCase):
    def setUp(self):
        self.ctx = ModelContext()
        super().setUp()

    @mock.patch.object(ModelContext, "get_type_hints")
    def test_class_meta_build_vars(self, mock_get_type_hints):
        var = XmlElement(name="foo", qname=QName("foo", "bar"), types=[int])
        mock_get_type_hints.return_value = [var]

        result = self.ctx.class_meta(ItemsType, None)
        expected = ClassMeta(
            name="ItemsType",
            clazz=ItemsType,
            qname=QName("ItemsType"),
            nillable=False,
            vars=[var],
        )

        self.assertEqual(expected, result)
        mock_get_type_hints.assert_called_once_with(ItemsType, None)

    @mock.patch.object(ModelContext, "get_type_hints", return_value=dict())
    def test_class_meta_with_meta_namespace(self, mock_get_type_hints):
        namespace = Product.Meta.namespace
        result = self.ctx.class_meta(Product, None)

        self.assertEqual(QName(namespace, "product"), result.qname)
        mock_get_type_hints.assert_called_once_with(Product, namespace)

    @mock.patch.object(ModelContext, "get_type_hints", return_value=dict())
    def test_class_meta_with_parent_ns(self, mock_get_type_hints):
        result = self.ctx.class_meta(ProductType, "http://xsdata")

        self.assertEqual(QName("http://xsdata", "ProductType"), str(result.qname))
        mock_get_type_hints.assert_called_once_with(ProductType, "http://xsdata")

    @mock.patch.object(ModelContext, "get_type_hints", return_value=dict())
    def test_class_meta_with_no_meta_name_and_name_generator(self, *args):
        inspect = ModelContext(name_generator=lambda x: text.snake_case(x))
        result = inspect.class_meta(ItemsType)

        self.assertEqual(QName("items_type"), str(result.qname))

    def test_class_meta_with_no_meta_not_inherit_from_parent(self):
        @dataclass
        class Bar:
            class Meta:
                name = "bar"

        @dataclass
        class Foo(Bar):
            pass

        result = self.ctx.class_meta(Foo)
        self.assertEqual("Foo", result.name)
        self.assertIsNone(result.namespace)

    @mock.patch.object(ModelContext, "get_type_hints", return_value=dict())
    def test_class_meta_with_no_dataclass_raises_exception(self, *args):
        with self.assertRaises(ModelInspectionError) as cm:
            self.ctx.class_meta(int)

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
        result = list(self.ctx.get_type_hints(TextType, None))

        expected = XmlWildcard(
            name="any_element",
            qname=QName(None, "any_element"),
            types=[object],
            init=True,
            nillable=False,
            dataclass=False,
            default=list,
            namespaces=["##any"],
        )

        self.assertEqual(2, len(result))
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
