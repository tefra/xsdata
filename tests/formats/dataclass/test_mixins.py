from typing import Iterator
from unittest import TestCase

from lxml.etree import QName

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.dataclass.mixins import Tag


class ModelInspectTests(TestCase):
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
