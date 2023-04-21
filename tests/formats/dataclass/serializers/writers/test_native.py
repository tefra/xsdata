from unittest import TestCase

from tests import fixtures_dir
from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter


class XmlEventWriterTests(TestCase):
    def setUp(self):
        config = SerializerConfig(pretty_print=True)
        self.serializer = XmlSerializer(config=config, writer=XmlEventWriter)

    def test_render(self):
        actual = self.serializer.render(books)
        expected = fixtures_dir.joinpath("books/books_auto_ns.xml").read_text()
        self.assertEqual(expected, actual)

    def test_render_with_provided_namespaces(self):
        actual = self.serializer.render(books, {"brk": "urn:books"})
        expected = fixtures_dir.joinpath("books/books.xml").read_text()
        self.assertEqual(expected, actual)

    def test_render_with_default_namespace_prefix(self):
        actual = self.serializer.render(books, {None: "urn:books"})
        expected = fixtures_dir.joinpath("books/books_default_ns.xml").read_text()
        self.assertEqual(expected, actual)

    def test_encoding(self):
        self.serializer.config.xml_version = "1.1"
        self.serializer.config.encoding = "US-ASCII"
        actual = self.serializer.render(books)
        xml_declaration, _ = actual.split("\n", 1)

        self.assertEqual('<?xml version="1.1" encoding="US-ASCII"?>', xml_declaration)

    def test_declaration_disabled(self):
        self.serializer.config.xml_declaration = False
        actual = self.serializer.render(books, {None: "urn:books"})
        expected = fixtures_dir.joinpath("books/books_default_ns.xml").read_text()
        xml_declaration, expected = expected.split("\n", 1)

        self.assertEqual(expected, actual)

    def test_pretty_print_false(self):
        self.serializer.config.pretty_print = False
        actual = self.serializer.render(books)
        expected = fixtures_dir.joinpath("books/books_auto_ns.xml").read_text()

        _, actual = actual.split("\n", 1)
        _, expected = expected.split("\n", 1)
        self.assertEqual(expected.replace("  ", "").replace("\n", ""), actual)

    def test_pretty_print_indent(self):
        self.serializer.config.pretty_print_indent = "    "
        actual = self.serializer.render(books)
        expected = fixtures_dir.joinpath("books/books_auto_ns.xml").read_text()

        _, actual = actual.split("\n", 1)
        _, expected = expected.split("\n", 1)
        self.assertEqual(expected.replace("  ", "    "), actual)
