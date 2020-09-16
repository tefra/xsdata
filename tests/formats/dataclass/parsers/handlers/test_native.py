from unittest import mock
from unittest.case import TestCase

from tests import fixtures_dir
from tests.fixtures.books import Books
from tests.fixtures.books.fixtures import books
from tests.fixtures.books.fixtures import events
from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler
from xsdata.formats.dataclass.parsers.handlers import XmlSaxHandler
from xsdata.formats.dataclass.parsers.nodes import RecordParser


class XmlEventHandlerTests(TestCase):
    def setUp(self):
        self.parser = RecordParser(handler=XmlEventHandler)
        self.fixture = fixtures_dir.joinpath("books/books.xml")

    def test_parse(self):
        self.assertEqual(books, self.parser.from_path(self.fixture, Books))
        self.assertEqual({"brk": "urn:books"}, self.parser.ns_map)
        self.assertEqual(events, self.parser.events)

    def test_parse_with_xinclude_raises_exception(self):
        self.parser.config.process_xinclude = True

        with self.assertRaises(XmlHandlerError) as cm:
            self.parser.from_path(self.fixture, Books)

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
        self.fixture = fixtures_dir.joinpath("books/books.xml")

    def test_parse(self):
        self.assertEqual(books, self.parser.from_path(self.fixture, Books))
        self.assertEqual({"brk": "urn:books"}, self.parser.ns_map)
        self.assertEqual(events, self.parser.events)

    @mock.patch.object(RecordParser, "end")
    @mock.patch.object(RecordParser, "start")
    def test_parse_returns_none_if_objects_empty(self, mock_start, mock_end):
        handler = XmlSaxHandler(parser=self.parser, clazz=Books)
        self.assertIsNone(handler.parse(self.fixture.as_uri()))

    def test_parse_with_xinclude_raises_exception(self):
        self.parser.config.process_xinclude = True

        with self.assertRaises(XmlHandlerError) as cm:
            self.parser.from_path(self.fixture, Books)

        self.assertEqual(
            "XmlSaxHandler doesn't support xinclude elements.", str(cm.exception)
        )
