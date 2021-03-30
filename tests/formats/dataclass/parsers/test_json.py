from dataclasses import make_dataclass
from unittest.case import TestCase
from xml.etree.ElementTree import QName

from tests import fixtures_dir
from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.json import JsonParser
from xsdata.models.datatype import XmlDate


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
                pub_date=XmlDate.from_string("2000-10-01"),
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

    def test_parser_entry_points(self):
        path = fixtures_dir.joinpath("books/books.json")

        books = self.parser.from_string(path.read_text(), Books)
        self.assertIsInstance(books, Books)

        books = self.parser.from_bytes(path.read_bytes(), Books)
        self.assertIsInstance(books, Books)

        books = self.parser.parse(str(path), Books)
        self.assertIsInstance(books, Books)

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
        var = XmlVar(attributes=True, name="a", qname="a")
        value = {"a": 1}
        actual = self.parser.bind_value(var, value)
        self.assertEqual(value, actual)
        self.assertIsNot(value, actual)

    def test_bind_dataclass_union(self):
        a = make_dataclass("a", [("x", int), ("y", str)])
        b = make_dataclass("b", [("x", int), ("y", str), ("z", float)])
        c = make_dataclass("c", [("x", int), ("y", str), ("z", str)])
        d = make_dataclass("d", [("x", int)])
        var = XmlVar(
            element=True,
            name="union",
            qname="union",
            types=[a, b, c, int],
            dataclass=True,
        )

        data = {"x": 1, "y": "foo", "z": "foo"}
        actual = self.parser.bind_value(var, data)

        self.assertIsInstance(actual, c)

    def test_bind_type_union(self):
        a = make_dataclass("a", [("x", int), ("y", str)])
        var = XmlVar(
            element=True,
            name="union",
            qname="union",
            types=[a, int, float],
            dataclass=True,
        )

        data = "1.1"
        self.assertEqual(1.1, self.parser.bind_value(var, data))

    def test_bind_choice_simple(self):
        var = XmlVar(
            elements=True,
            qname="compound",
            name="compound",
            choices=[
                XmlVar(element=True, qname="int", name="int", types=[int]),
                XmlVar(
                    element=True,
                    qname="tokens",
                    name="tokens",
                    types=[int],
                    tokens=True,
                ),
                XmlVar(element=True, qname="generic", name="generic", dataclass=True),
                XmlVar(element=True, qname="float", name="float", types=[float]),
                XmlVar(element=True, qname="qname", name="qname", types=[QName]),
            ],
        )
        self.assertEqual(1.0, self.parser.bind_choice("1.0", var))
        self.assertEqual(1, self.parser.bind_choice(1, var))
        self.assertEqual([1], self.parser.bind_choice(["1"], var))

        actual = self.parser.bind_choice("a", var)
        self.assertEqual(QName("a"), actual)
        self.assertIsInstance(actual, QName)

        actual = self.parser.bind_choice("{a}b", var)
        self.assertIsInstance(actual, QName)
        self.assertEqual(QName("{a}b"), actual)

        actual = self.parser.bind_choice("!NotQName", var)
        self.assertIsInstance(actual, str)
        self.assertEqual("!NotQName", actual)

    def test_bind_choice_dataclass(self):
        a = make_dataclass("a", [("x", int)])
        b = make_dataclass("b", [("x", int), ("y", str)])

        var = XmlVar(
            elements=True,
            qname="compound",
            name="compound",
            choices=[
                XmlVar(element=True, qname="c", name="c", types=[int]),
                XmlVar(element=True, qname="a", name="a", types=[a], dataclass=True),
                XmlVar(element=True, qname="b", name="b", types=[b], dataclass=True),
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
        var = XmlVar(
            elements=True,
            qname="compound",
            name="compound",
            choices=[
                XmlVar(element=True, name="a", qname="a", types=[int]),
                XmlVar(element=True, name="b", qname="b", types=[float]),
            ],
        )
        data = {"qname": "a", "value": 1, "substituted": True}

        self.assertEqual(
            DerivedElement(qname="a", value=1, substituted=True),
            self.parser.bind_choice(data, var),
        )

    def test_bind_choice_generic_with_wildcard(self):
        var = XmlVar(
            elements=True,
            qname="compound",
            name="compound",
            choices=[
                XmlVar(element=True, name="a", qname="a", types=[int]),
                XmlVar(element=True, name="b", qname="b", types=[float]),
            ],
        )

        self.assertEqual(
            AnyElement(qname="a", text="1"),
            self.parser.bind_choice({"qname": "a", "text": 1}, var),
        )

    def test_bind_choice_generic_with_unknown_qname(self):
        var = XmlVar(elements=True, qname="compound", name="compound")

        with self.assertRaises(ParserError) as cm:
            self.parser.bind_choice({"qname": "foo", "text": 1}, var)

        self.assertEqual(
            "XmlElements undefined choice: `compound` for qname `foo`",
            str(cm.exception),
        )

    def test_bind_wildcard_with_any_element(self):
        var = XmlVar(
            wildcard=True,
            name="any_element",
            qname="any_element",
            types=[object],
        )

        self.assertEqual(
            AnyElement(qname="a", text="1"),
            self.parser.bind_value(var, {"qname": "a", "text": 1}),
        )

    def test_bind_wildcard_with_derived_element(self):
        var = XmlVar(
            any_type=True,
            name="a",
            qname="a",
            types=[object],
        )
        actual = DerivedElement(qname="a", value=Books(book=[]), substituted=True)
        data = {"qname": "a", "value": {"book": []}, "substituted": True}

        self.assertEqual(actual, self.parser.bind_value(var, data))

    def test_bind_wildcard_with_no_matching_value(self):
        var = XmlVar(
            any_type=True,
            name="a",
            qname="a",
            types=[object],
        )

        data = {"test_bind_wildcard_with_no_matching_value": False}
        self.assertEqual(data, self.parser.bind_value(var, data))
        self.assertEqual(1, self.parser.bind_value(var, 1))
