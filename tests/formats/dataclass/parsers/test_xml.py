from unittest import mock
from unittest.case import TestCase

from lxml.etree import Element
from lxml.etree import QName

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers.nodes import PrimitiveNode
from xsdata.formats.dataclass.parsers.nodes import RootNode
from xsdata.formats.dataclass.parsers.xml import XmlParser
from xsdata.models.enums import EventType


class XmlParserTests(TestCase):
    def setUp(self):
        super(XmlParserTests, self).setUp()
        self.parser = XmlParser()
        self.parser.index = 10
        self.parser.objects = [(QName(x), x) for x in "abcde"]

    def test_parse_context_raises_exception(self):
        with self.assertRaises(ParserError) as cm:
            self.parser.parse_context([], Books)

        self.assertEqual("Failed to create target class `Books`", str(cm.exception))

    def test_add_namespace(self):
        self.parser.add_namespace(("foo", "bar"))
        self.assertEqual({"foo": "bar"}, self.parser.namespaces.ns_map)

    @mock.patch.object(RootNode, "next_node")
    @mock.patch.object(XmlParser, "emit_event")
    def test_queue(self, mock_emit_event, mock_next_node):
        primitive_node = PrimitiveNode(position=1, types=[int])
        mock_next_node.return_value = primitive_node
        element = Element("{urn:books}books")
        root_queue_item = RootNode(
            position=0, meta=self.parser.context.build(Books), default=None,
        )

        objects = list()
        queue = list()
        queue.append(root_queue_item)
        self.parser.queue(element, queue, objects)

        self.assertEqual(2, len(queue))
        self.assertEqual(root_queue_item, queue[0])
        self.assertEqual(primitive_node, queue[1])

        mock_emit_event.assert_called_once_with(
            EventType.START, element.tag, item=root_queue_item, element=element
        )

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(PrimitiveNode, "parse_element", return_value=("q", "result"))
    def test_dequeue(self, mock_parse_element, mock_emit_event):
        element = Element("author", nsmap={"prefix": "uri"})
        element.text = "foobar"

        objects = list()
        queue = list()
        queue.append(PrimitiveNode(position=0, types=[str], default=None))

        result = self.parser.dequeue(element, queue, objects)
        self.assertEqual("result", result)
        self.assertEqual(0, len(queue))
        self.assertEqual(("q", result), objects[-1])
        mock_parse_element.assert_called_once_with(element, objects)
        mock_emit_event.assert_called_once_with(
            EventType.END, element.tag, obj=result, element=element
        )

    def test_emit_event(self):
        mock_func = mock.Mock()
        self.parser.foo_bar_element = mock_func

        self.parser.emit_event("foo", "{tns}barElement", a=1, b=2)

        mock_func.assert_called_once_with(a=1, b=2)
        self.assertEqual({"{tns}barElement": "bar_element"}, self.parser.event_names)


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

        parser = XmlParser()
        actual = parser.from_string(xml, Books)
        self.assertEqual(self.books, actual)
        self.assertEqual({"brk": "urn:books"}, parser.namespaces.ns_map)
