from dataclasses import make_dataclass
from unittest.case import TestCase

from tests import fixtures_dir
from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlElements
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.json import JsonParser


class JsonParserTests(TestCase):
    def test_parser(self):
        path = fixtures_dir.joinpath("books/books.json")
        parser = JsonParser()
        books = parser.from_path(path, Books)

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

        foo_field = XmlText(name="foo", qname="foo", types=[str])
        bar_field = XmlElement(name="bar", qname="bar", types=[str], list_element=True)

        self.assertEqual("bar", JsonParser.get_value(data, foo_field))
        self.assertEqual(["foo"], JsonParser.get_value(data, bar_field))
        self.assertIsNone(JsonParser.get_value({}, bar_field))

    def test_bind_choice_with_raw_primitive_value(self):
        var = XmlElements(qname="compound", name="compound")
        parser = JsonParser()
        self.assertEqual(1, parser.bind_choice(1, var))

    def test_bind_choice_with_raw_dict(self):
        a = make_dataclass("a", [("x", int)])
        b = make_dataclass("b", [("x", int), ("y", str)])

        var = XmlElements(
            qname="compound",
            name="compound",
            choices=[
                XmlElement(qname="c", name="c", types=[int]),
                XmlElement(qname="a", name="a", types=[a], dataclass=True),
                XmlElement(qname="b", name="b", types=[b], dataclass=True),
            ],
        )

        parser = JsonParser()
        self.assertEqual(a(1), parser.bind_choice({"x": 1}, var))
        self.assertEqual(b(1, "2"), parser.bind_choice({"x": 1, "y": "2"}, var))

        with self.assertRaises(ParserError) as cm:
            parser.bind_choice({"x": 1, "y": "2", "z": 3}, var)

        self.assertEqual(
            "XmlElements undefined choice: `compound` for `{'x': 1, 'y': '2', 'z': 3}`",
            str(cm.exception),
        )

    def test_bind_choice_with_derived_value(self):
        var = XmlElements(
            qname="compound",
            name="compound",
            choices=[
                XmlElement(name="a", qname="a", types=[int]),
                XmlElement(name="b", qname="b", types=[float]),
            ],
        )

        parser = JsonParser()
        self.assertEqual(
            DerivedElement(qname="a", value=1),
            parser.bind_choice({"qname": "a", "value": 1}, var),
        )

    def test_bind_choice_with_generic_value(self):
        var = XmlElements(
            qname="compound",
            name="compound",
            choices=[
                XmlElement(name="a", qname="a", types=[int]),
                XmlElement(name="b", qname="b", types=[float]),
            ],
        )

        parser = JsonParser()
        self.assertEqual(
            AnyElement(qname="a", text=1),
            parser.bind_choice({"qname": "a", "text": 1}, var),
        )

    def test_bind_choice_with_unknown_qname(self):
        var = XmlElements(qname="compound", name="compound")

        parser = JsonParser()
        with self.assertRaises(ParserError) as cm:
            parser.bind_choice({"qname": "foo", "text": 1}, var)

        self.assertEqual(
            "XmlElements undefined choice: `compound` for qname `foo`",
            str(cm.exception),
        )
