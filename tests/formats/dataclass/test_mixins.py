from typing import Iterator
from unittest import TestCase

from tests.fixtures.books import BookForm, Books
from xsdata.formats.dataclass.mixins import Field, ModelInspect


class ModelInspectTests(TestCase):
    def test_get_type_hints(self):
        inspect = ModelInspect()
        result = inspect.get_type_hints(BookForm)
        self.assertIsInstance(result, Iterator)

        expected = [
            Field(name="author", local_name="author", type=str),
            Field(name="title", local_name="title", type=str),
            Field(name="genre", local_name="genre", type=str),
            Field(name="price", local_name="price", type=float),
            Field(name="pub_date", local_name="pub_date", type=str),
            Field(name="review", local_name="review", type=str),
            Field(name="id", local_name="id", type=str, is_attribute=True),
        ]

        self.assertEqual(expected, list(result))

    def test_get_type_hints_with_dataclass_list(self):
        inspect = ModelInspect()
        result = list(inspect.get_type_hints(Books))

        expected = Field(
            name="book",
            local_name="book",
            type=BookForm,
            is_list=True,
            is_dataclass=True,
            default=list,
        )

        self.assertEqual(1, len(result))
        self.assertEqual(expected, result[0])

    def test_get_type_hints_with_no_dataclass(self):
        inspect = ModelInspect()
        with self.assertRaises(TypeError):
            list(inspect.get_type_hints(self.__class__))

    def test_fields(self):
        inspect = ModelInspect()
        inspect.cache[BookForm] = {"foo": str}

        self.assertEqual({"foo": str}, inspect.fields(BookForm))

    def test_is_dataclass(self):
        self.assertTrue(ModelInspect.is_dataclass(BookForm))
        self.assertFalse(ModelInspect.is_dataclass(str))
        self.assertFalse(ModelInspect.is_dataclass(self.__class__))
