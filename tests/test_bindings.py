from typing import Optional
from typing import Type
from unittest import mock
from unittest import TestCase

from lxml.etree import Element

from tests.fixtures.books import Books
from xsdata.exceptions import ParserError
from xsdata.formats.bindings import AbstractParser
from xsdata.formats.bindings import AbstractXmlParser


class AbstractParserTests(TestCase):
    @mock.patch("xsdata.formats.bindings.to_python", return_value=2)
    def test_parse_value(self, mock_to_python):
        self.assertEqual(1, AbstractParser.parse_value([int], None, 1))
        self.assertIsNone(AbstractParser.parse_value([int], None, lambda: 1))

        self.assertTrue(2, AbstractParser.parse_value([int], "1", None))
        mock_to_python.assert_called_once_with([int], "1")


class XmlParser(AbstractXmlParser):
    def queue_node(self, element: Element):
        pass

    def dequeue_node(self, element: Element) -> Optional[Type]:
        return None


class AbstractXmlParserTests(TestCase):
    def test_parse_context_throws_exception(self):
        with self.assertRaises(ParserError) as cm:
            parser = XmlParser()
            parser.parse_context([], Books)

        self.assertEqual("Failed to create target class `Books`", str(cm.exception))
