from dataclasses import make_dataclass
from unittest import TestCase

import lxml

from tests import fixtures_dir
from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.serializers import TreeSerializer, XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import (
    LxmlEventWriter,
)


class LxmlEventWriterTests(TestCase):
    def setUp(self):
        config = SerializerConfig(indent="  ")
        self.serializer = XmlSerializer(config=config, writer=LxmlEventWriter)

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

        xml_declaration, actual = actual.split("\n", 1)
        _, expected = expected.split("\n", 1)

        self.assertEqual(expected, actual)

    def test_encoding(self):
        self.serializer.config.encoding = "ISO-8859-1"
        x = make_dataclass("x", [("value", str)])
        obj = x("á, é, í, ó")
        actual = self.serializer.render(obj)
        expected = '<?xml version="1.0" encoding="ISO-8859-1"?>\n<x>á, é, í, ó</x>\n'
        self.assertEqual(expected, actual)

    def test_declaration_disabled(self):
        self.serializer.config.xml_declaration = False
        actual = self.serializer.render(books, {None: "urn:books"})
        expected = fixtures_dir.joinpath("books/books_default_ns.xml").read_text()
        xml_declaration, expected = expected.split("\n", 1)

        self.assertEqual(expected, actual)

    def test_no_indent(self):
        self.serializer.config.indent = None
        actual = self.serializer.render(books)
        expected = fixtures_dir.joinpath("books/books_auto_ns.xml").read_text()

        _, actual = actual.split("\n", 1)
        _, expected = expected.split("\n", 1)
        self.assertEqual(expected.replace("  ", "").replace("\n", ""), actual)


class LxmlTreeBuilderTests(TestCase):
    def setUp(self):
        super().setUp()
        self.serializer = TreeSerializer()
        self.serializer.config.indent = "  "

    def test_render(self):
        tree = self.serializer.render(books)

        actual = lxml.etree.tostring(tree).decode()

        expected = fixtures_dir.joinpath("books/books_auto_ns.xml").read_text()
        expected = "\n".join(expected.splitlines()[1:])
        self.assertEqual(expected, actual)

    def test_render_with_no_indent(self):
        self.serializer.config.indent = ""
        tree = self.serializer.render(books)

        lxml.etree.indent(tree, "  ")
        actual = lxml.etree.tostring(tree).decode()

        expected = fixtures_dir.joinpath("books/books_auto_ns.xml").read_text()
        expected = "\n".join(expected.splitlines()[1:])
        self.assertEqual(expected, actual)
