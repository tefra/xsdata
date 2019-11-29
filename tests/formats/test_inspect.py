from typing import Iterator
from unittest import TestCase

from tests.fixtures.books import BookForm, Books
from xsdata.formats.inspect import Field, ModelInspect


class ModelInspectTests(TestCase):
    def test_fields_with_dataclass(self):
        inspect = ModelInspect()
        result = inspect.fields(BookForm)
        self.assertIsInstance(result, Iterator)

        expected = [
            Field(
                name="author",
                local_name="author",
                type=str,
                is_list=False,
                is_attribute=False,
                default=None,
            ),
            Field(
                name="title",
                local_name="title",
                type=str,
                is_list=False,
                is_attribute=False,
                default=None,
            ),
            Field(
                name="genre",
                local_name="genre",
                type=str,
                is_list=False,
                is_attribute=False,
                default=None,
            ),
            Field(
                name="price",
                local_name="price",
                type=float,
                is_list=False,
                is_attribute=False,
                default=None,
            ),
            Field(
                name="pub_date",
                local_name="pub_date",
                type=str,
                is_list=False,
                is_attribute=False,
                default=None,
            ),
            Field(
                name="review",
                local_name="review",
                type=str,
                is_list=False,
                is_attribute=False,
                default=None,
            ),
            Field(
                name="id",
                local_name="id",
                type=str,
                is_list=False,
                is_attribute=True,
                default=None,
            ),
        ]

        self.assertEqual(expected, list(result))

    def test_fields_with_dataclass_list(self):
        inspect = ModelInspect()
        result = list(inspect.fields(Books))

        expected = Field(
            name="book",
            local_name="book",
            type=BookForm,
            is_list=True,
            is_attribute=False,
            default=list,
        )

        self.assertEqual(1, len(result))
        self.assertEqual(expected, result[0])

    def test_fields_with_no_dataclass(self):
        inspect = ModelInspect()
        with self.assertRaises(TypeError) as cm:
            list(inspect.fields(self.__class__))
        self.assertEqual(
            f"Object {self.__class__} is not a dataclass", str(cm.exception)
        )

    def test_get_type_hints(self):
        inspect = ModelInspect()
        inspect.cache[BookForm] = {"foo": str}

        self.assertEqual({"foo": str}, inspect.get_type_hints(BookForm))

    def test_is_dataclass(self):
        self.assertTrue(ModelInspect.is_dataclass(BookForm))
        self.assertFalse(ModelInspect.is_dataclass(str))
        self.assertFalse(ModelInspect.is_dataclass(self.__class__))


#
