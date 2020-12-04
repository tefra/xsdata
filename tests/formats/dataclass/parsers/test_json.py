from dataclasses import make_dataclass
from unittest.case import TestCase

from tests import fixtures_dir
from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.models.elements import XmlAttributes
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlElements
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.json import JsonParser


class JsonParserTests(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.parser = JsonParser()

    def test_parser(self):
        path = fixtures_dir.joinpath("books/books.json")
        books = self.parser.from_path(path, Books)

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

    def test_parser_with_unknown_class(self):
        path = fixtures_dir.joinpath("books/books.json")
        books = self.parser.from_path(path)
        self.assertIsInstance(books, Books)
        self.assertEqual(2, len(books.book))

        with self.assertRaises(ParserError) as cm:
            self.parser.from_string('{"please": 1, "dont": 1, "exists": 2}')

        self.assertEqual(
            "No class found matching the document keys(['please', 'dont', 'exists'])",
            str(cm.exception),
        )

    def test_parser_with_non_iterable_value(self):
        with self.assertRaises(ParserError) as cm:
            self.parser.from_string('{"book": 1}')

        self.assertEqual("Key `book` value is not iterable", str(cm.exception))

    def test_bind_value_with_attributes_var(self):
        var = XmlAttributes(name="a", qname="a")
        value = {"a": 1}
        actual = self.parser.bind_value(var, value)
        self.assertEqual(value, actual)
        self.assertIsNot(value, actual)

    def test_bind_dataclass_union(self):
        a = make_dataclass("a", [("x", int), ("y", str)])
        b = make_dataclass("b", [("x", int), ("y", str), ("z", float)])
        c = make_dataclass("c", [("x", int)])
        var = XmlElement(name="union", qname="union", types=[a, b, c], dataclass=True)

        data = {"x": 1, "y": "foo", "z": 1.0}
        actual = self.parser.bind_value(var, data)

        self.assertIsInstance(actual, b)

    def test_bind_choice_simple(self):
        var = XmlElements(
            qname="compound",
            name="compound",
            choices=[
                XmlElement(qname="int", name="int", types=[int]),
                XmlElement(qname="tokens", name="tokens", types=[int], tokens=True),
                XmlElement(qname="generic", name="generic", dataclass=True),
                XmlElement(qname="float", name="float", types=[float]),
            ],
        )
        self.assertEqual(1.0, self.parser.bind_choice("1.0", var))
        self.assertEqual(1, self.parser.bind_choice(1, var))
        self.assertEqual([1], self.parser.bind_choice(["1"], var))
        self.assertEqual("a", self.parser.bind_choice("a", var))

    def test_bind_choice_dataclass(self):
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

        self.assertEqual(a(1), self.parser.bind_choice({"x": 1}, var))
        self.assertEqual(b(1, "2"), self.parser.bind_choice({"x": 1, "y": "2"}, var))

        with self.assertRaises(ParserError) as cm:
            self.parser.bind_choice({"x": 1, "y": "2", "z": 3}, var)

        self.assertEqual(
            "XmlElements undefined choice: `compound` for `{'x': 1, 'y': '2', 'z': 3}`",
            str(cm.exception),
        )

    def test_bind_choice_generic_with_derived(self):
        var = XmlElements(
            qname="compound",
            name="compound",
            choices=[
                XmlElement(name="a", qname="a", types=[int]),
                XmlElement(name="b", qname="b", types=[float]),
            ],
        )

        self.assertEqual(
            DerivedElement(qname="a", value=1),
            self.parser.bind_choice({"qname": "a", "value": 1}, var),
        )

    def test_bind_choice_generic_with_wildcard(self):
        var = XmlElements(
            qname="compound",
            name="compound",
            choices=[
                XmlElement(name="a", qname="a", types=[int]),
                XmlElement(name="b", qname="b", types=[float]),
            ],
        )

        self.assertEqual(
            AnyElement(qname="a", text="1"),
            self.parser.bind_choice({"qname": "a", "text": 1}, var),
        )

    def test_bind_choice_generic_with_unknown_qname(self):
        var = XmlElements(qname="compound", name="compound")

        with self.assertRaises(ParserError) as cm:
            self.parser.bind_choice({"qname": "foo", "text": 1}, var)

        self.assertEqual(
            "XmlElements undefined choice: `compound` for qname `foo`",
            str(cm.exception),
        )
