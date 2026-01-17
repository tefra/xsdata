from dataclasses import make_dataclass
from unittest import TestCase

from tests import fixtures_dir
from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter


class XmlEventWriterTests(TestCase):
    def setUp(self) -> None:
        config = SerializerConfig(indent="  ")
        self.serializer = XmlSerializer(config=config, writer=XmlEventWriter)

    def test_render(self) -> None:
        actual = self.serializer.render(books)
        expected = fixtures_dir.joinpath("books/books_auto_ns.xml").read_text()
        self.assertEqual(expected, actual)

    def test_render_with_provided_namespaces(self) -> None:
        actual = self.serializer.render(books, {"brk": "urn:books"})
        expected = fixtures_dir.joinpath("books/books.xml").read_text()
        self.assertEqual(expected, actual)

    def test_render_with_default_namespace_prefix(self) -> None:
        actual = self.serializer.render(books, {None: "urn:books"})
        expected = fixtures_dir.joinpath("books/books_default_ns.xml").read_text()
        self.assertEqual(expected, actual)

    def test_encoding(self) -> None:
        self.serializer.config.encoding = "ISO-8859-1"
        x = make_dataclass("x", [("value", str)])
        obj = x("á, é, í, ó")
        actual = self.serializer.render(obj)
        expected = '<?xml version="1.0" encoding="ISO-8859-1"?>\n<x>á, é, í, ó</x>\n'
        self.assertEqual(expected, actual)

    def test_declaration_disabled(self) -> None:
        self.serializer.config.xml_declaration = False
        actual = self.serializer.render(books, {None: "urn:books"})
        expected = fixtures_dir.joinpath("books/books_default_ns.xml").read_text()
        _xml_declaration, expected = expected.split("\n", 1)

        self.assertEqual(expected, actual)

    def test_no_indent(self) -> None:
        self.serializer.config.indent = None
        actual = self.serializer.render(books)
        expected = fixtures_dir.joinpath("books/books_auto_ns.xml").read_text()

        _, actual = actual.split("\n", 1)
        _, expected = expected.split("\n", 1)
        self.assertEqual(expected.replace("  ", "").replace("\n", ""), actual)
