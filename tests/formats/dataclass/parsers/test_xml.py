from dataclasses import dataclass
from dataclasses import replace
from unittest import mock
from unittest.case import TestCase

from lxml.etree import Comment
from lxml.etree import Element
from lxml.etree import QName

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter08.example0803 import DressSize
from tests.fixtures.defxmlschema.chapter12.chapter12 import ProductType
from xsdata.formats.dataclass.models import AnyElement
from xsdata.formats.dataclass.parsers.xml import ClassQueueItem
from xsdata.formats.dataclass.parsers.xml import PrimitiveQueueItem
from xsdata.formats.dataclass.parsers.xml import SkipQueueItem
from xsdata.formats.dataclass.parsers.xml import WildcardQueueItem
from xsdata.formats.dataclass.parsers.xml import XmlParser
from xsdata.models.enums import EventType
from xsdata.models.enums import Namespace
from xsdata.models.inspect import ClassMeta
from xsdata.models.inspect import ClassVar
from xsdata.models.inspect import Tag


class XmlParserTests(TestCase):
    def setUp(self) -> None:
        self.parser = XmlParser()
        self.parser.index = 10
        self.parser.objects = [(QName(x), x) for x in "abcde"]

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(XmlParser, "create_skip_queue_item")
    def test_queue_node_with_skip_queue_item(
        self, mock_create_skip_queue_item, mock_emit_event
    ):
        expected_queue_item = SkipQueueItem(index=10, position=5)
        mock_create_skip_queue_item.return_value = expected_queue_item

        element = Element("{urn:books}books")
        last_in_queue_item = SkipQueueItem(index=0, position=0)
        self.parser.queue.append(last_in_queue_item)
        self.parser.queue_node(element)

        self.assertEqual(11, self.parser.index)
        self.assertEqual(2, len(self.parser.queue))
        self.assertEqual(last_in_queue_item, self.parser.queue[0])
        self.assertEqual(expected_queue_item, self.parser.queue[1])

        mock_emit_event.assert_called_once_with(
            EventType.START, element.tag, item=last_in_queue_item, element=element
        )

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(XmlParser, "create_skip_queue_item")
    def test_queue_node_with_wildcard_queue_item(
        self, mock_create_skip_queue_item, mock_emit_event
    ):
        expected_queue_item = WildcardQueueItem(index=10, position=5, qname="foo")
        mock_create_skip_queue_item.return_value = expected_queue_item

        element = Element("{urn:books}books")
        last_in_queue_item = WildcardQueueItem(index=0, position=0, qname="foo")
        self.parser.queue.append(last_in_queue_item)
        self.parser.queue_node(element)

        self.assertEqual(11, self.parser.index)
        self.assertEqual(2, len(self.parser.queue))
        self.assertEqual(last_in_queue_item, self.parser.queue[0])
        self.assertEqual(expected_queue_item, self.parser.queue[1])

        mock_emit_event.assert_called_once_with(
            EventType.START, element.tag, item=last_in_queue_item, element=element
        )

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(XmlParser, "create_skip_queue_item")
    def test_queue_node_with_primitive_queue_item(
        self, mock_create_skip_queue_item, mock_emit_event
    ):
        expected_queue_item = SkipQueueItem(index=10, position=5)
        mock_create_skip_queue_item.return_value = expected_queue_item

        element = Element("{urn:books}books")
        last_in_queue_item = PrimitiveQueueItem(index=0, position=0, types=[])
        self.parser.queue.append(last_in_queue_item)
        self.parser.queue_node(element)

        self.assertEqual(11, self.parser.index)
        self.assertEqual(2, len(self.parser.queue))
        self.assertEqual(last_in_queue_item, self.parser.queue[0])
        self.assertEqual(expected_queue_item, self.parser.queue[1])

        mock_emit_event.assert_called_once_with(
            EventType.START, element.tag, item=last_in_queue_item, element=element
        )

    @mock.patch.object(XmlParser, "emit_event")
    def test_queue_node_with_root(self, mock_emit_event):
        element = Element("{urn:books}books")
        root_queue_item = ClassQueueItem(
            index=0, position=0, meta=self.parser.class_meta(Books)
        )

        self.parser.index = 0
        self.parser.queue.append(root_queue_item)
        self.parser.queue_node(element)

        self.assertEqual(1, self.parser.index)
        self.assertEqual(1, len(self.parser.queue))
        self.assertEqual(root_queue_item, self.parser.queue[0])

        mock_emit_event.assert_called_once_with(
            EventType.START, element.tag, item=root_queue_item, element=element
        )

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(XmlParser, "create_wildcard_queue_item", return_value="yes")
    @mock.patch.object(ClassMeta, "get_var")
    def test_queue_node_with_wildcard_element(
        self, mock_get_var, mock_create_wildcard_queue_item, mock_emit_event
    ):
        element = Element("{urn:books}foobar")
        class_queue_item = ClassQueueItem(
            index=0, position=0, meta=self.parser.class_meta(Books)
        )
        mock_get_var.return_value = ClassVar(
            qname="{urn:books}:parent", types=[], name="", tag=Tag.ANY_ELEMENT
        )

        self.parser.queue.append(class_queue_item)
        self.parser.queue_node(element)

        self.assertEqual(11, self.parser.index)
        self.assertEqual(2, len(self.parser.queue))
        self.assertEqual(class_queue_item, self.parser.queue[0])
        self.assertEqual("yes", self.parser.queue[1])

        mock_create_wildcard_queue_item.assert_called_once_with("{urn:books}:parent")
        mock_emit_event.assert_called_once_with(
            EventType.START, element.tag, item=class_queue_item, element=element
        )

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(XmlParser, "create_class_queue_item", return_value="yes")
    def test_queue_node_with_dataclass_variable(
        self, mock_create_class_queue_item, mock_emit_event
    ):
        element = Element("book")
        meta = self.parser.class_meta(Books)
        class_queue_item = ClassQueueItem(index=0, position=0, meta=meta)
        self.parser.queue.append(class_queue_item)
        self.parser.queue_node(element)

        self.assertEqual(11, self.parser.index)
        self.assertEqual(2, len(self.parser.queue))
        self.assertEqual(class_queue_item, self.parser.queue[0])
        self.assertEqual("yes", self.parser.queue[1])

        mock_create_class_queue_item.assert_called_once_with(
            meta.vars[QName("book")], meta.qname
        )
        mock_emit_event.assert_called_once_with(
            EventType.START, element.tag, item=class_queue_item, element=element
        )

    def test_queue_node_with_unkown_element(self):
        element = Element("unknown")
        meta = self.parser.class_meta(Books)
        class_queue_item = ClassQueueItem(index=0, position=0, meta=meta)
        self.parser.queue.append(class_queue_item)

        with self.assertRaises(ValueError):
            self.parser.queue_node(element)

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(XmlParser, "create_primitive_queue_item", return_value="yes")
    def test_queue_node_with_primitive_variable(
        self, mock_create_primitive_queue_item, mock_emit_event
    ):
        element = Element("author")
        meta = self.parser.class_meta(BookForm)
        class_queue_item = ClassQueueItem(index=0, position=0, meta=meta)
        self.parser.queue.append(class_queue_item)
        self.parser.queue_node(element)

        self.assertEqual(11, self.parser.index)
        self.assertEqual(2, len(self.parser.queue))
        self.assertEqual(class_queue_item, self.parser.queue[0])
        self.assertEqual("yes", self.parser.queue[1])

        mock_create_primitive_queue_item.assert_called_once_with(meta.vars["author"])
        mock_emit_event.assert_called_once_with(
            EventType.START, element.tag, item=class_queue_item, element=element
        )

    def test_create_skip_queue_item(self):
        actual = self.parser.create_skip_queue_item()
        expected = SkipQueueItem(index=10, position=5)
        self.assertEqual(expected, actual)

    @mock.patch.object(XmlParser, "class_meta")
    def test_create_class_queue_item(self, mock_class_meta):
        mock_class_meta.return_value = "yes"
        class_var = ClassVar(
            qname="author",
            types=[BookForm],
            dataclass=True,
            name="",
            tag="",
            default=10,
        )

        qname = QName("{urn}book")
        actual = self.parser.create_class_queue_item(class_var, qname)
        expected = ClassQueueItem(index=10, position=5, default=10, meta="yes")
        self.assertEqual(expected, actual)
        mock_class_meta.assert_called_once_with(BookForm, qname.namespace)

    def test_create_primitive_queue_item(self):
        class_var = ClassVar(qname="", types=[int, str], name="", tag="", default=1)

        actual = self.parser.create_primitive_queue_item(class_var)
        expected = PrimitiveQueueItem(index=10, position=5, default=1, types=[int, str])
        self.assertEqual(expected, actual)

    def test_create_wildcard_queue_item(self):
        parent_qname = QName("parent")

        actual = self.parser.create_wildcard_queue_item(parent_qname)
        expected = WildcardQueueItem(index=10, position=5, qname=parent_qname)
        self.assertEqual(expected, actual)

    @mock.patch.object(XmlParser, "emit_event")
    def test_dequeue_node_with_skip_item(self, mock_emit_event):
        element = Element("author", nsmap={"foo": "bar"})
        element.text = "foobar"

        queue_item = SkipQueueItem(index=0, position=0)
        self.parser.queue.append(queue_item)

        result = self.parser.dequeue_node(element)
        self.assertIsNone(result)
        self.assertEqual(0, len(self.parser.queue))
        self.assertEqual(0, mock_emit_event.call_count)
        self.assertEqual({}, self.parser.namespaces.items)

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(XmlParser, "parse_value", return_value="result")
    def test_dequeue_node_with_primitive_item(self, mock_parse_value, mock_emit_event):
        element = Element("author", nsmap={"prefix": "uri"})
        element.text = "foobar"

        queue_item = PrimitiveQueueItem(index=0, position=0, types=[str], default=None)
        self.parser.queue.append(queue_item)

        result = self.parser.dequeue_node(element)
        self.assertEqual("result", result)
        self.assertEqual(0, len(self.parser.queue))
        self.assertEqual((QName(element.tag), result), self.parser.objects[-1])
        self.assertEqual({"prefix": "uri"}, self.parser.namespaces.ns_map)
        mock_parse_value.assert_called_once_with(
            queue_item.types, element.text, queue_item.default
        )
        mock_emit_event.assert_called_once_with(
            EventType.END, element.tag, obj=result, element=element
        )

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(XmlParser, "fetch_any_children", return_value=[1, 2, 3])
    @mock.patch.object(XmlParser, "parse_any_element")
    def test_dequeue_node_with_wildcard_item(
        self, mock_parse_any_element, mock_fetch_any_children, mock_emit_event
    ):
        obj = AnyElement()
        mock_parse_any_element.return_value = obj

        element = Element("author", nsmap={"prefix": "uri"})

        queue_item = WildcardQueueItem(index=0, position=0, qname=QName("parent"))
        self.parser.queue.append(queue_item)

        result = self.parser.dequeue_node(element)
        self.assertEqual(obj, result)
        self.assertEqual(0, len(self.parser.queue))
        self.assertEqual((queue_item.qname, result), self.parser.objects[-1])
        self.assertEqual([1, 2, 3], result.children)
        self.assertEqual({"prefix": "uri"}, self.parser.namespaces.ns_map)

        mock_parse_any_element.assert_called_once_with(element)
        mock_fetch_any_children.assert_called_once_with(queue_item)
        mock_emit_event.assert_called_once_with(
            EventType.END, element.tag, obj=result, element=element
        )

    @mock.patch.object(XmlParser, "emit_event")
    @mock.patch.object(XmlParser, "bind_element_wild_text")
    @mock.patch.object(XmlParser, "bind_element_children")
    @mock.patch.object(XmlParser, "bind_element_text")
    @mock.patch.object(XmlParser, "bind_element_attrs")
    def test_dequeue_node_with_class_item(
        self,
        mock_bind_element_attrs,
        mock_bind_element_text,
        mock_bind_element_children,
        mock_bind_element_wild_text,
        mock_emit_event,
    ):
        def bind_element_attrs(x, y, z):
            x["a"] = 1

        def bind_element_text(x, y, z):
            x["b"] = 2

        def bind_element_children(x, y, z):
            x["c"] = 3

        def bind_element_wild_text(x, y, z):
            x["d"] = 4

        mock_bind_element_attrs.side_effect = bind_element_attrs
        mock_bind_element_text.side_effect = bind_element_text
        mock_bind_element_children.side_effect = bind_element_children
        mock_bind_element_wild_text.side_effect = bind_element_wild_text
        element = Element("author", nsmap={"prefix": "uri"})

        @dataclass
        class Foo:
            a: int
            b: int
            c: int
            d: int

        meta = self.parser.class_meta(Foo)
        item = ClassQueueItem(index=0, position=0, meta=meta)
        self.parser.queue.append(item)

        result = self.parser.dequeue_node(element)
        self.assertEqual(Foo(1, 2, 3, 4), result)
        self.assertEqual(0, len(self.parser.queue))
        self.assertEqual((QName(element.tag), result), self.parser.objects[-1])
        self.assertEqual({"prefix": "uri"}, self.parser.namespaces.ns_map)

        mock_bind_element_attrs.assert_called_once_with(mock.ANY, meta, element)
        mock_bind_element_text.assert_called_once_with(mock.ANY, meta, element)
        mock_bind_element_children.assert_called_once_with(mock.ANY, item, element)
        mock_bind_element_wild_text.assert_called_once_with(mock.ANY, meta, element)
        mock_emit_event.assert_called_once_with(
            EventType.END, element.tag, obj=result, element=element
        )

    def test_dequeue_node_with_unknown_item(self):
        self.parser.queue.append(None)
        with self.assertRaises(ValueError):
            self.parser.dequeue_node(Element("foo"))

    def test_emit_event(self):
        mock_func = mock.Mock()
        self.parser.foo_bar_element = mock_func

        self.parser.emit_event("foo", "{tns}barElement", a=1, b=2)
        mock_func.assert_called_once_with(a=1, b=2)

    def test_fetch_any_children(self):
        queue_item = WildcardQueueItem(index=0, position=2, qname="foo")
        expected = [value for _, value in self.parser.objects[2:]]

        self.assertEqual(expected, self.parser.fetch_any_children(queue_item))

    @mock.patch.object(XmlParser, "parse_value")
    def test_bind_element_attrs(self, mock_parse_value):
        mock_parse_value.return_value = "2020-03-02"
        metadata = self.parser.class_meta(ProductType)
        eff_date = metadata.vars["effDate"]
        element = Element("foo")
        element.set("effDate", "2020-03-01")
        element.set("whatever", "foo")

        params = dict()
        self.parser.bind_element_attrs(params, metadata, element)
        expected = {"eff_date": "2020-03-02", "other_attributes": {"whatever": "foo"}}
        self.assertEqual(expected, params)
        mock_parse_value.assert_called_once_with(
            eff_date.types, "2020-03-01", eff_date.default,
        )

    def test_bind_elements_attrs_ignore_init_false_vars(self):
        metadata = self.parser.class_meta(ProductType)
        metadata.vars["effDate"] = replace(metadata.vars["effDate"], init=False)
        element = Element("foo")
        element.set("effDate", "2020-03-01")

        params = dict()
        self.parser.bind_element_attrs(params, metadata, element)
        self.assertEqual({}, params)

    def test_bind_element_text_with_no_text_var(self):
        element = Element("foo")
        element.text = "foo"

        params = dict()
        metadata = self.parser.class_meta(Books)
        self.parser.bind_element_text(params, metadata, element)
        self.assertEqual({}, params)

    @mock.patch.object(XmlParser, "parse_value", return_value="yes!")
    def test_bind_element_text_with_text_var(self, mock_parse_value):
        element = Element("foo")
        params = dict()
        metadata = self.parser.class_meta(DressSize)
        self.parser.bind_element_text(params, metadata, element)
        self.assertEqual({}, params)

        element.text = "foo"
        self.parser.bind_element_text(params, metadata, element)
        self.assertEqual({"value": "yes!"}, params)
        mock_parse_value.assert_called_once_with(
            metadata.any_text.types, element.text, metadata.any_text.default
        )

    def test_parse_any_element(self):
        comment = Comment("foo")
        self.assertIsNone(XmlParser.parse_any_element(comment))

        element = Element("foo")
        element.set("a", "1")
        element.set("b", "2")
        element.set(
            QName(Namespace.XSI.uri, "type").text, QName(Namespace.XS.uri, "float").text
        )
        element.text = "yes"
        element.tail = "no"

        actual = XmlParser.parse_any_element(element)
        expected = AnyElement(
            qname=element.tag,
            text="yes",
            tail="no",
            attributes={
                "a": "1",
                "b": "2",
                QName(Namespace.XSI.uri, "type"): QName(Namespace.XS.uri, "float"),
            },
            nsmap=element.nsmap,
        )
        self.assertEqual(expected, actual)
        actual = XmlParser.parse_any_element(element, False)
        self.assertIsNone(actual.qname)

    def test_element_text_and_tail(self):
        element = Element("foo")

        text, tail = XmlParser.element_text_and_tail(element)
        self.assertIsNone(text)
        self.assertIsNone(tail)

        element.text = " \n "
        element.tail = " \n  "
        text, tail = XmlParser.element_text_and_tail(element)
        self.assertIsNone(text)
        self.assertIsNone(tail)

        element.text = " foo "
        element.tail = " bar "
        text, tail = XmlParser.element_text_and_tail(element)
        self.assertEqual("foo", text)
        self.assertEqual("bar", tail)


class XmlParserIntegrationTest(TestCase):
    def setUp(self) -> None:
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
