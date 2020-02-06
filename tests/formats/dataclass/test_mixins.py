from typing import Iterator
from unittest import mock
from unittest import TestCase

from lxml.etree import QName

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter02.example0210 import Product
from tests.fixtures.defxmlschema.chapter13.chapter13 import ItemsType
from tests.fixtures.defxmlschema.chapter13.chapter13 import ProductType
from xsdata.formats.dataclass.mixins import ClassMeta
from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.dataclass.mixins import Tag
from xsdata.utils import text


class ModelInspectTests(TestCase):
    @mock.patch.object(ModelInspect, "get_type_hints")
    def test_class_meta_build_vars(self, mock_get_type_hints):
        var = ClassVar(name="foo", qname=QName("foo", "bar"), type=int, tag=Tag.ELEMENT)
        mock_get_type_hints.return_value = [var]

        inspect = ModelInspect()
        result = inspect.class_meta(ItemsType, None)
        expected = ClassMeta(
            name="ItemsType",
            qname=QName("ItemsType"),
            mixed=False,
            vars={var.qname: var},
        )
        self.assertEqual(expected, result)
        mock_get_type_hints.assert_called_once_with(ItemsType, None)

    @mock.patch.object(ModelInspect, "get_type_hints", return_value=dict())
    def test_class_meta_with_meta_namespace(self, mock_get_type_hints):
        inspect = ModelInspect()
        result = inspect.class_meta(Product, None)
        self.assertEqual(QName("http://datypic.com/prod", "product"), result.qname)
        mock_get_type_hints.assert_called_once_with(Product, "http://datypic.com/prod")

    @mock.patch.object(ModelInspect, "get_type_hints", return_value=dict())
    def test_class_meta_with_parent_ns(self, mock_get_type_hints):
        inspect = ModelInspect()
        result = inspect.class_meta(ProductType, "http://parent.ns")
        self.assertEqual(QName("http://parent.ns", "ProductType"), str(result.qname))
        mock_get_type_hints.assert_called_once_with(ProductType, "http://parent.ns")

    @mock.patch.object(ModelInspect, "get_type_hints", return_value=dict())
    def test_class_meta_with_no_meta_name_and_name_generator(self, *args):
        inspect = ModelInspect(name_generator=lambda x: text.snake_case(x))
        result = inspect.class_meta(ItemsType)
        self.assertEqual(QName("items_type"), str(result.qname))

    @mock.patch.object(ModelInspect, "get_type_hints", return_value=dict())
    def test_class_meta_with_no_dataclass_raises_exception(self, *args):
        with self.assertRaises(TypeError) as cm:
            ModelInspect().class_meta(int)

        self.assertEqual(f"Object {int} is not a dataclass.", str(cm.exception))

    def test_get_type_hints(self):
        inspect = ModelInspect()
        result = inspect.get_type_hints(BookForm, None)
        self.assertIsInstance(result, Iterator)

        expected = [
            ClassVar(name="author", qname=QName("author"), type=str, tag=Tag.ELEMENT,),
            ClassVar(name="title", qname=QName("title"), type=str, tag=Tag.ELEMENT,),
            ClassVar(name="genre", qname=QName("genre"), type=str, tag=Tag.ELEMENT,),
            ClassVar(name="price", qname=QName("price"), type=float, tag=Tag.ELEMENT,),
            ClassVar(
                name="pub_date", qname=QName("pub_date"), type=str, tag=Tag.ELEMENT,
            ),
            ClassVar(name="review", qname=QName("review"), type=str, tag=Tag.ELEMENT,),
            ClassVar(name="id", qname=QName("id"), type=str, tag=Tag.ATTRIBUTE),
        ]

        self.assertEqual(expected, list(result))

    def test_get_type_hints_with_dataclass_list(self):
        inspect = ModelInspect()
        result = list(inspect.get_type_hints(Books, None))

        expected = ClassVar(
            name="book",
            qname=QName("book"),
            type=BookForm,
            is_list=True,
            is_dataclass=True,
            default=list,
            tag=Tag.ELEMENT,
        )

        self.assertEqual(1, len(result))
        self.assertEqual(expected, result[0])

    def test_get_type_hints_with_no_dataclass(self):
        inspect = ModelInspect()
        with self.assertRaises(TypeError):
            list(inspect.get_type_hints(self.__class__, None))
