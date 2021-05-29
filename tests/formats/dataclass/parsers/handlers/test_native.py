from unittest import mock
from unittest.case import TestCase

from tests import fixtures_dir
from tests.fixtures.books import Books
from tests.fixtures.books.fixtures import books
from tests.fixtures.books.fixtures import events
from tests.fixtures.books.fixtures import events_default_ns
from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler
from xsdata.formats.dataclass.parsers.handlers import XmlSaxHandler
from xsdata.formats.dataclass.parsers.nodes import RecordParser


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

    def test_parse_with_xinclude_raises_exception(self):
        self.parser.config.process_xinclude = True
        path = fixtures_dir.joinpath("books/books.xml")

        with self.assertRaises(XmlHandlerError) as cm:
            self.parser.from_path(path, Books)

        self.assertEqual(
            "XmlEventHandler doesn't support xinclude elements.", str(cm.exception)
        )

    def test_parse_context_with_unhandled_event(self):
        context = [("reverse", None)]
        handler = XmlEventHandler(parser=self.parser, clazz=Books)

        with self.assertRaises(XmlHandlerError) as cm:
            handler.process_context(context)

        self.assertEqual("Unhandled event: `reverse`.", str(cm.exception))


class SaxHandlerTests(TestCase):
    def setUp(self):
        self.parser = RecordParser(handler=XmlSaxHandler)

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

    @mock.patch.object(RecordParser, "end")
    @mock.patch.object(RecordParser, "start")
    def test_parse_returns_none_if_objects_empty(self, mock_start, mock_end):
        path = fixtures_dir.joinpath("books/books.xml")
        handler = XmlSaxHandler(parser=self.parser, clazz=Books)
        self.assertIsNone(handler.parse(path.as_uri()))

    def test_parse_with_xinclude_raises_exception(self):
        self.parser.config.process_xinclude = True
        path = fixtures_dir.joinpath("books/books.xml")

        with self.assertRaises(XmlHandlerError) as cm:
            self.parser.from_path(path, Books)

        self.assertEqual(
            "XmlSaxHandler doesn't support xinclude elements.", str(cm.exception)
        )
