import json
from unittest.case import TestCase

from lxml.etree import QName

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import Tag
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers import XmlParser


class JsonParserTests(TestCase):
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

        foo_field = ClassVar(name="foo", qname=QName("foo"), types=[str], tag=Tag.TEXT)
        bar_field = ClassVar(
            name="bar", qname=QName("bar"), types=[str], is_list=True, tag=Tag.ELEMENT,
        )

        self.assertEqual("bar", JsonParser.get_value(data, foo_field))
        self.assertEqual(["foo"], JsonParser.get_value(data, bar_field))
        self.assertIsNone(JsonParser.get_value({}, bar_field))


class XmlParserTests(TestCase):
    def setUp(self) -> None:
        super(XmlParserTests, self).setUp()
        self.books = Books(
            book=[
                BookForm(
                    id="bk001",
                    author="Hightower, Kim",
                    title="The First Book",
                    genre="Fiction",
                    price=44.95,
                    pub_date="2000-10-01",
                    review="An amazing story of nothing.",
                ),
                BookForm(
                    id="bk002",
                    author="Nagata, Suanne",
                    title="Becoming Somebody",
                    genre="Biography",
                    review="A masterpiece of the fine art of gossiping.",
                ),
            ]
        )

    def test_parse(self):
        xml = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<brk:books xmlns:brk="urn:books">\n'
            '  <book id="bk001">\n'
            "    <author>Hightower, Kim</author>\n"
            "    <title>The First Book</title>\n"
            "    <genre>Fiction</genre>\n"
            "    <price>44.95</price>\n"
            "    <pub_date>2000-10-01</pub_date>\n"
            "    <review>An amazing story of nothing.</review>\n"
            "  </book>\n"
            '  <book id="bk002">\n'
            "    <author>Nagata, Suanne</author>\n"
            "    <title>Becoming Somebody</title>\n"
            "    <genre>Biography</genre>\n"
            "    <review>A masterpiece of the fine art of gossiping.</review>\n"
            "  </book>\n"
            "</brk:books>\n"
        )
        actual = XmlParser().from_string(xml, Books)
        self.assertEqual(self.books, actual)
