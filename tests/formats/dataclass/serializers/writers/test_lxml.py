from unittest import TestCase

from tests import fixtures_dir
from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.writers import LxmlEventWriter


class LxmlEventWriterTests(TestCase):
    def setUp(self):
        self.serializer = XmlSerializer(pretty_print=True, writer=LxmlEventWriter)

    def test_render(self):
        actual = self.serializer.render(books)
        expected = fixtures_dir.joinpath("books/books_auto_ns.xml").read_text()

        xml_declaration, actual = actual.split("\n", 1)
        _, expected = expected.split("\n", 1)

        self.assertEqual(expected, actual)
        self.assertEqual("<?xml version='1.0' encoding='UTF-8'?>", xml_declaration)

    def test_render_with_provided_namespaces(self):
        actual = self.serializer.render(books, {"brk": "urn:books"})
        expected = fixtures_dir.joinpath("books/books.xml").read_text()

        xml_declaration, actual = actual.split("\n", 1)
        _, expected = expected.split("\n", 1)

        self.assertEqual(expected, actual)

    def test_render_with_default_namespace_prefix(self):
        actual = self.serializer.render(books, {None: "urn:books"})
        expected = fixtures_dir.joinpath("books/books_default_ns.xml").read_text()

        xml_declaration, actual = actual.split("\n", 1)
        _, expected = expected.split("\n", 1)

        self.assertEqual(expected, actual)

    def test_encoding(self):
        self.serializer.encoding = "US-ASCII"
        actual = self.serializer.render(books)
        xml_declaration, _ = actual.split("\n", 1)

        self.assertEqual("<?xml version='1.0' encoding='US-ASCII'?>", xml_declaration)

    def test_pretty_print_false(self):
        self.serializer.pretty_print = False
        actual = self.serializer.render(books)
        expected = fixtures_dir.joinpath("books/books_auto_ns.xml").read_text()

        _, actual = actual.split("\n", 1)
        _, expected = expected.split("\n", 1)
        self.assertEqual(expected.replace("  ", "").replace("\n", ""), actual)
