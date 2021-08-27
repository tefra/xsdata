import sys
from unittest.case import TestCase
from xml import etree

import pytest

from tests import fixtures_dir
from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from tests.fixtures.books.fixtures import books
from tests.fixtures.books.fixtures import events
from tests.fixtures.books.fixtures import events_default_ns
from xsdata.exceptions import ParserError
from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.bases import RecordParser
from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler
from xsdata.formats.dataclass.parsers.handlers.native import get_base_url


class XmlEventHandlerTests(TestCase):
    def setUp(self):
        self.parser = RecordParser(handler=XmlEventHandler)

    def test_parse(self):
        path = fixtures_dir.joinpath("books/books.xml")
        self.assertEqual(books, self.parser.from_path(path, Books))
        self.assertEqual({"brk": "urn:books"}, self.parser.ns_map)
        self.assertEqual(events, self.parser.events)

    def test_parse_with_default_ns(self):
        path = fixtures_dir.joinpath("books/books_default_ns.xml")
        self.assertEqual(books, self.parser.from_path(path, Books))
        self.assertEqual({None: "urn:books"}, self.parser.ns_map)
        self.assertEqual(events_default_ns, self.parser.events)

    def test_parse_context_with_unhandled_event(self):
        context = [("reverse", None)]
        handler = XmlEventHandler(parser=self.parser, clazz=Books)

        with self.assertRaises(XmlHandlerError) as cm:
            handler.process_context(context)

        self.assertEqual("Unhandled event: `reverse`.", str(cm.exception))

    def test_parse_with_xml_syntax_error(self):
        with self.assertRaises(ParserError):
            self.parser.from_string("<", Books)

    def test_parse_with_element_or_tree(self):
        path = fixtures_dir.joinpath("books/books.xml")
        tree = etree.ElementTree.parse(str(path))

        result = self.parser.parse(tree, Books)
        self.assertEqual(books, result)

        tree = etree.ElementTree.parse(str(path))
        result = self.parser.parse(tree.find(".//book"), BookForm)
        self.assertEqual(books.book[0], result)

    @pytest.mark.skipif(sys.platform == "win32", reason="urljoin + path sep")
    def test_parse_with_xinclude(self):
        path = fixtures_dir.joinpath("books/books-xinclude.xml")
        ns_map = {"ns0": "urn:books"}

        self.parser.config.process_xinclude = True
        self.assertEqual(books, self.parser.parse(str(path), Books))
        self.assertEqual(ns_map, self.parser.ns_map)

    @pytest.mark.skipif(sys.platform == "win32", reason="urljoin + path sep")
    def test_parse_with_xinclude_from_memory(self):
        path = fixtures_dir.joinpath("books/books-xinclude.xml")
        ns_map = {"ns0": "urn:books"}

        self.parser.config.process_xinclude = True
        self.parser.config.base_url = str(path)
        self.assertEqual(books, self.parser.from_string(path.read_text(), Books))
        self.assertEqual(ns_map, self.parser.ns_map)

    def test_get_base_url(self):
        self.assertIsNone(get_base_url(None, None))
        self.assertIsNone(get_base_url(None, None))
        self.assertEqual("config/", get_base_url("config/", "/tmp/foo.xml"))
