import json
from unittest.case import TestCase

from lxml.etree import QName

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.parsers.json import JsonParser


class JsonParserTests(TestCase):
    def setUp(self):
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
        parser = JsonParser()
        books = parser.from_string(json.dumps(self.data), Books)

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

    def test_get_value(self):
        data = dict(foo="bar", bar="foo")

        foo_field = XmlText(name="foo", qname=QName("foo"), types=[str])
        bar_field = XmlElement(
            name="bar", qname=QName("bar"), types=[str], default=list
        )

        self.assertEqual("bar", JsonParser.get_value(data, foo_field))
        self.assertEqual(["foo"], JsonParser.get_value(data, bar_field))
        self.assertIsNone(JsonParser.get_value({}, bar_field))
