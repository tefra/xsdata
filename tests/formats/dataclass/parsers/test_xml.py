from unittest import mock
from unittest.case import TestCase

from lxml.etree import Element
from lxml.etree import QName

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.formats.dataclass.parsers.nodes import PrimitiveNode
from xsdata.formats.dataclass.parsers.nodes import RootNode
from xsdata.formats.dataclass.parsers.nodes import SkipNode
from xsdata.formats.dataclass.parsers.xml import XmlParser
from xsdata.models.enums import EventType


class XmlParserTests(TestCase):
    def setUp(self):
        self.parser = XmlParser()
        self.parser.index = 10
        self.parser.objects = [(QName(x), x) for x in "abcde"]

    @mock.patch.object(RootNode, "next_node")
    @mock.patch.object(XmlParser, "emit_event")
    def test_queue_node(self, mock_emit_event, mock_next_node):
        skip_node = SkipNode(index=1, position=1)
        mock_next_node.return_value = skip_node
        element = Element("{urn:books}books")
        root_queue_item = RootNode(
            index=0, position=0, meta=self.parser.context.build(Books), default=None,
        )

        self.parser.index = 0
        self.parser.queue.append(root_queue_item)
        self.parser.queue_node(element)

        self.assertEqual(1, self.parser.index)
        self.assertEqual(2, len(self.parser.queue))
        self.assertEqual(root_queue_item, self.parser.queue[0])
        self.assertEqual(skip_node, self.parser.queue[1])

        mock_emit_event.assert_called_once_with(
            EventType.START, element.tag, item=root_queue_item, element=element
        )

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(PrimitiveNode, "parse_element", return_value=("q", "result"))
    def test_dequeue_node_with_primitive_item(
        self, mock_parse_element, mock_emit_event
    ):
        element = Element("author", nsmap={"prefix": "uri"})
        element.text = "foobar"

        queue_item = PrimitiveNode(index=0, position=0, types=[str], default=None)
        self.parser.queue.append(queue_item)

        result = self.parser.dequeue_node(element)
        self.assertEqual("result", result)
        self.assertEqual(0, len(self.parser.queue))
        self.assertEqual(("q", result), self.parser.objects[-1])
        self.assertEqual({"prefix": "uri"}, self.parser.namespaces.ns_map)
        mock_parse_element.assert_called_once_with(element, self.parser.objects)
        mock_emit_event.assert_called_once_with(
            EventType.END, element.tag, obj=result, element=element
        )

    def test_emit_event(self):
        mock_func = mock.Mock()
        self.parser.foo_bar_element = mock_func

        self.parser.emit_event("foo", "{tns}barElement", a=1, b=2)
        mock_func.assert_called_once_with(a=1, b=2)


class XmlParserIntegrationTest(TestCase):
    def setUp(self):
        super(XmlParserIntegrationTest, self).setUp()
        self.books = Books(
            book=[
                BookForm(
                    id="bk001",
                    author="Hightower, Kim",
                    title="The First Book",
                    genre="Fiction",
                    price=44.95,
                    pub_date="2000-10-01",
                    review="An amazing story of nothing.",
                ),
                BookForm(
                    id="bk002",
                    author="Nagata, Suanne",
                    title="Becoming Somebody",
                    genre="Biography",
                    review="A masterpiece of the fine art of gossiping.",
                ),
            ]
        )

    def test_parse(self):
        xml = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<brk:books xmlns:brk="urn:books">\n'
            '  <book id="bk001">\n'
            "    <author>Hightower, Kim</author>\n"
            "    <title>The First Book</title>\n"
            "    <genre>Fiction</genre>\n"
            "    <price>44.95</price>\n"
            "    <pub_date>2000-10-01</pub_date>\n"
            "    <review>An amazing story of nothing.</review>\n"
            "  </book>\n"
            '  <book id="bk002">\n'
            "    <author>Nagata, Suanne</author>\n"
            "    <title>Becoming Somebody</title>\n"
            "    <genre>Biography</genre>\n"
            "    <review>A masterpiece of the fine art of gossiping.</review>\n"
            "  </book>\n"
            "</brk:books>\n"
        )
        actual = XmlParser().from_string(xml, Books)
        self.assertEqual(self.books, actual)
