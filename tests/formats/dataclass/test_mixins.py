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
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.models.inspect import ClassMeta
from xsdata.models.inspect import ClassVar
from xsdata.models.inspect import Tag
from xsdata.utils import text


class ModelInspectTests(TestCase):
    def setUp(self) -> None:
        self.inspect = ModelInspect()
        super().setUp()

    @mock.patch.object(ModelInspect, "get_type_hints")
    def test_class_meta_build_vars(self, mock_get_type_hints):
        var = ClassVar(
            name="foo", qname=QName("foo", "bar"), types=[int], tag=Tag.ELEMENT
        )
        mock_get_type_hints.return_value = [var]

        result = self.inspect.class_meta(ItemsType, None)
        expected = ClassMeta(
            name="ItemsType",
            clazz=ItemsType,
            qname=QName("ItemsType"),
            mixed=False,
            nillable=False,
            vars={var.qname: var},
        )

        self.assertEqual(expected, result)
        mock_get_type_hints.assert_called_once_with(ItemsType, None)

    @mock.patch.object(ModelInspect, "get_type_hints", return_value=dict())
    def test_class_meta_with_meta_namespace(self, mock_get_type_hints):
        namespace = Product.Meta.namespace
        result = self.inspect.class_meta(Product, None)

        self.assertEqual(QName(namespace, "product"), result.qname)
        mock_get_type_hints.assert_called_once_with(Product, namespace)

    @mock.patch.object(ModelInspect, "get_type_hints", return_value=dict())
    def test_class_meta_with_parent_ns(self, mock_get_type_hints):
        result = self.inspect.class_meta(ProductType, "http://xsdata")

        self.assertEqual(QName("http://xsdata", "ProductType"), str(result.qname))
        mock_get_type_hints.assert_called_once_with(ProductType, "http://xsdata")

    @mock.patch.object(ModelInspect, "get_type_hints", return_value=dict())
    def test_class_meta_with_no_meta_name_and_name_generator(self, *args):
        inspect = ModelInspect(name_generator=lambda x: text.snake_case(x))
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

        result = self.inspect.class_meta(Foo)
        self.assertEqual("Foo", result.name)
        self.assertFalse(result.mixed)
        self.assertIsNone(result.namespace)

    @mock.patch.object(ModelInspect, "get_type_hints", return_value=dict())
    def test_class_meta_with_no_dataclass_raises_exception(self, *args):
        with self.assertRaises(ModelInspectionError) as cm:
            self.inspect.class_meta(int)

        self.assertEqual(f"Object {int} is not a dataclass.", str(cm.exception))

    def test_get_type_hints(self):
        result = self.inspect.get_type_hints(BookForm, None)
        self.assertIsInstance(result, Iterator)

        expected = [
            ClassVar(
                name="author", qname=QName("author"), types=[str], tag=Tag.ELEMENT,
            ),
            ClassVar(name="title", qname=QName("title"), types=[str], tag=Tag.ELEMENT),
            ClassVar(name="genre", qname=QName("genre"), types=[str], tag=Tag.ELEMENT),
            ClassVar(
                name="price", qname=QName("price"), types=[float], tag=Tag.ELEMENT,
            ),
            ClassVar(
                name="pub_date", qname=QName("pub_date"), types=[str], tag=Tag.ELEMENT,
            ),
            ClassVar(
                name="review", qname=QName("review"), types=[str], tag=Tag.ELEMENT,
            ),
            ClassVar(name="id", qname=QName("id"), types=[str], tag=Tag.ATTRIBUTE),
            ClassVar(
                name="lang",
                qname=QName("lang"),
                types=[str],
                tag=Tag.ATTRIBUTE,
                init=False,
                default="en",
            ),
        ]

        result = list(result)
        self.assertEqual(expected, result)
        for var in result:
            self.assertFalse(var.dataclass)
            self.assertIsNone(var.clazz)

    def test_get_type_hints_with_dataclass_list(self):
        result = list(self.inspect.get_type_hints(Books, None))

        expected = ClassVar(
            name="book",
            qname=QName("book"),
            types=[BookForm],
            dataclass=True,
            default=list,
            tag=Tag.ELEMENT,
        )

        self.assertTrue(expected.is_list)
        self.assertEqual(1, len(result))
        self.assertEqual(expected, result[0])
        self.assertTrue(result[0].dataclass)
        self.assertEqual(BookForm, result[0].clazz)

    def test_get_type_hints_with_wildcard_element(self):
        result = list(self.inspect.get_type_hints(TextType, None))

        expected = ClassVar(
            name="any_element",
            qname=QName(None, "any_element"),
            types=[object],
            tag=Tag.ANY_ELEMENT,
            init=True,
            nillable=False,
            dataclass=False,
            default=list,
            wild_ns=["##any"],
        )

        self.assertEqual(2, len(result))
        self.assertEqual(expected, result[0])

    def test_get_type_hints_with_no_dataclass(self):
        with self.assertRaises(TypeError):
            list(self.inspect.get_type_hints(self.__class__, None))

    def test_resolve_namespace(self):
        actual = self.inspect.resolve_namespace("##any", Tag.ANY_ELEMENT, "foo")
        self.assertIsNone(actual)

        actual = self.inspect.resolve_namespace("foo", Tag.ELEMENT, "bar")
        self.assertEqual("foo", actual)

        actual = self.inspect.resolve_namespace("", Tag.ELEMENT, "bar")
        self.assertIsNone(actual)

        actual = self.inspect.resolve_namespace(None, Tag.ELEMENT, "bar")
        self.assertEqual("bar", actual)

        actual = self.inspect.resolve_namespace(None, Tag.ATTRIBUTE, "bar")
        self.assertIsNone(actual)

    def test_wild_namespaces(self):
        tag = Tag.ATTRIBUTE
        actual = self.inspect.wild_namespaces(None, tag, "p")
        self.assertEqual([], actual)

        tag = Tag.ANY_ELEMENT
        actual = self.inspect.wild_namespaces(None, tag, "p")
        self.assertEqual(["##any"], actual)

        actual = self.inspect.wild_namespaces("##any", tag, "p")
        self.assertEqual(["##any"], actual)

        actual = self.inspect.wild_namespaces("##targetNamespace", tag, "")
        self.assertEqual(["##any"], actual)

        actual = self.inspect.wild_namespaces("##targetNamespace", tag, None)
        self.assertEqual(["##any"], actual)

        actual = self.inspect.wild_namespaces("##targetNamespace", tag, "p")
        self.assertEqual(["p"], actual)

        actual = self.inspect.wild_namespaces("##local", tag, "p")
        self.assertEqual([""], actual)

        actual = self.inspect.wild_namespaces("##other", tag, "p")
        self.assertEqual(["!p"], actual)

        actual = self.inspect.wild_namespaces("##other   ##local", tag, "p")
        self.assertEqual(["", "!p"], sorted(actual))

        actual = self.inspect.wild_namespaces("##targetNamespace   foo", tag, "p")
        self.assertEqual(["foo", "p"], sorted(actual))
