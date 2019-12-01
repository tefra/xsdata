import json
from unittest import TestCase

from tests.fixtures.books import BookForm, Books
from xsdata.formats.dict.parser import DictParser
from xsdata.formats.inspect import Field


class DictParserTests(TestCase):
    def setUp(self) -> None:
        self.data = {
            "book": [
                {
                    "author": "Hightower, Kim",
                    "title": "The First Book",
                    "genre": "Fiction",
                    "price": 44.95,
                    "pub_date": "2000-10-01",
                    "review": "An amazing story of nothing.",
                    "id": "bk001",
                },
                {
                    "author": "Nagata, Suanne",
                    "title": "Becoming Somebody",
                    "genre": "Biography",
                    "price": None,
                    "pub_date": None,
                    "review": "A masterpiece of the fine art of gossiping.",
                    "id": "bk002",
                },
            ]
        }

    def test_parser(self):
        parser = DictParser()
        books = parser.from_json(json.dumps(self.data), Books)

        self.assertIsInstance(books, Books)

        self.assertEqual(
            BookForm(
                author="Hightower, Kim",
                title="The First Book",
                genre="Fiction",
                price=44.95,
                pub_date="2000-10-01",
                review="An amazing story of nothing.",
                id="bk001",
            ),
            books.book[0],
        )

        self.assertEqual(
            BookForm(
                author="Nagata, Suanne",
                title="Becoming Somebody",
                genre="Biography",
                price=None,
                pub_date=None,
                review="A masterpiece of the fine art of gossiping.",
                id="bk002",
            ),
            books.book[1],
        )

    def test_parse_value(self):
        data = dict(foo="bar", bar="foo")

        foo_field = Field(name="", local_name="foo", type=str)
        bar_field = Field(name="", local_name="bar", type=str, is_list=True)

        self.assertEqual("bar", DictParser.parse_value(data, foo_field))
        self.assertEqual(["foo"], DictParser.parse_value(data, bar_field))

        none_field = Field(name="", local_name="nope", type=str, default=list)
        self.assertEqual([], DictParser.parse_value(data, none_field))

        none_field = Field(name="", local_name="nope", type=str, default=1)
        self.assertEqual(1, DictParser.parse_value(data, none_field))
