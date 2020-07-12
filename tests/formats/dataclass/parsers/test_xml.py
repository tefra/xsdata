from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from typing import List
from unittest import mock
from unittest.case import TestCase

from lxml.etree import Element
from lxml.etree import QName

from tests import fixtures_dir
from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.nodes import PrimitiveNode
from xsdata.formats.dataclass.parsers.nodes import RootNode
from xsdata.formats.dataclass.parsers.nodes import SkipNode
from xsdata.formats.dataclass.parsers.xml import XmlParser
from xsdata.models.enums import EventType


class XmlParserTests(TestCase):
    def setUp(self):
        super().setUp()
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
        var = XmlText(name="foo", qname=QName("foo"))
        primitive_node = PrimitiveNode(position=1, var=var)
        mock_next_node.return_value = primitive_node
        element = Element("{urn:books}books")
        config = ParserConfig()
        root_queue_item = RootNode(
            position=0, meta=self.parser.context.build(Books), config=config,
        )

        objects = []
        queue = []
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

        objects = []
        queue = []
        var = XmlText(name="foo", qname=QName("foo"))
        queue.append(PrimitiveNode(position=0, var=var))

        result = self.parser.dequeue(element, queue, objects)
        self.assertEqual("result", result)
        self.assertEqual(0, len(queue))
        self.assertEqual(("q", result), objects[-1])
        mock_parse_element.assert_called_once_with(element, objects)
        mock_emit_event.assert_called_once_with(
            EventType.END, element.tag, obj=result, element=element
        )

    @mock.patch.object(XmlParser, "emit_event")
    def test_dequeue_with_none_qname(self, mock_emit_event):
        element = Element("author", nsmap={"prefix": "uri"})
        element.text = "foobar"

        objects = []
        queue = [SkipNode(position=0)]

        result = self.parser.dequeue(element, queue, objects)
        self.assertIsNone(result)
        self.assertEqual(0, len(queue))
        self.assertEqual(0, len(objects))
        self.assertEqual(0, mock_emit_event.call_count)

    def test_emit_event(self):
        mock_func = mock.Mock()
        self.parser.foo_bar_element = mock_func

        self.parser.emit_event("foo", "{tns}barElement", a=1, b=2)

        mock_func.assert_called_once_with(a=1, b=2)
        self.assertEqual({"{tns}barElement": "bar_element"}, self.parser.event_names)


class XmlParserIntegrationTest(TestCase):
    def setUp(self):
        super().setUp()
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
                    price=33.95,
                    pub_date="2001-01-10",
                    review="A masterpiece of the fine art of gossiping.",
                ),
            ]
        )

    def test_parse(self):
        path = fixtures_dir.joinpath("books/books.xml")
        parser = XmlParser()
        actual = parser.from_path(path, Books)
        self.assertEqual(self.books, actual)
        self.assertEqual({"brk": "urn:books"}, parser.namespaces.ns_map)

    def test_parse_with_process_xinclude_true(self):
        path = fixtures_dir.joinpath("books/books-xinclude.xml")
        config = ParserConfig(process_xinclude=True)
        parser = XmlParser(config=config)
        actual = parser.from_path(path, Books)
        self.assertEqual(self.books, actual)

    def test_parse_from_memory_with_process_xinclude_true(self):
        path = fixtures_dir.joinpath("books/books-xinclude.xml")
        config = ParserConfig(process_xinclude=True, base_url=path.as_uri())
        parser = XmlParser(config=config)
        actual = parser.from_bytes(path.read_bytes(), Books)
        self.assertEqual(self.books, actual)

    def test_parse_with_fail_on_unknown_properties_false(self):
        path = fixtures_dir.joinpath("books/books.xml")

        @dataclass
        class Book:
            author: str = field(metadata=dict(type="Element"))

        @dataclass
        class MyBooks:
            class Meta:
                name = "books"

            book: List[Book] = field(
                default_factory=list, metadata=dict(type="Element")
            )

        config = ParserConfig(fail_on_unknown_properties=False)
        parser = XmlParser(config=config)
        actual = parser.from_path(path, MyBooks)
        expected = {
            "book": [{"author": "Hightower, Kim"}, {"author": "Nagata, Suanne"}]
        }
        self.assertEqual(expected, asdict(actual))
