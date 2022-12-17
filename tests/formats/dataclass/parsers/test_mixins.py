from unittest.case import TestCase

from tests.fixtures.books import Books
from tests.fixtures.books.fixtures import books
from tests.fixtures.books.fixtures import events
from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.bases import RecordParser
from xsdata.formats.dataclass.parsers.mixins import EventsHandler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler


class XmlHandlerTests(TestCase):
    def test_process(self):
        parser = RecordParser()
        handler = XmlHandler(clazz=Books, parser=parser)

        self.assertEqual([], handler.queue)
        self.assertEqual([], handler.objects)

        with self.assertRaises(NotImplementedError):
            handler.parse(None)


class EventsHandlerTests(TestCase):
    def setUp(self) -> None:
        self.parser = RecordParser(handler=EventsHandler)

    def test_parse(self):
        self.assertEqual(books, self.parser.parse(events, Books))
        self.assertEqual({"brk": "urn:books"}, self.parser.ns_map)

    def test_parse_with_unhandled_event(self):
        with self.assertRaises(XmlHandlerError) as cm:
            self.parser.parse([("reverse", "")], Books)

        self.assertEqual("Unhandled event: `reverse`.", str(cm.exception))
