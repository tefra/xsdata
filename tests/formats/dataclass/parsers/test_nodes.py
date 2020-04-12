from dataclasses import dataclass
from dataclasses import replace
from unittest import mock
from unittest.case import TestCase

from lxml.etree import Element
from lxml.etree import QName

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.models.elements import XmlWildcard
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.nodes import ElementNode
from xsdata.formats.dataclass.parsers.nodes import PrimitiveNode
from xsdata.formats.dataclass.parsers.nodes import RootNode
from xsdata.formats.dataclass.parsers.nodes import SkipNode
from xsdata.formats.dataclass.parsers.nodes import WildcardNode
from xsdata.formats.dataclass.parsers.nodes import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils


@dataclass
class Foo:
    a: int
    b: int
    c: int
    d: int


class XmlNodeTests(TestCase):
    def test_next_node(self):
        ctx = XmlContext()
        with self.assertRaises(NotImplementedError):
            XmlNode(0, 0).next_node(QName("foo"), 1, 0, ctx)

    def test_parse_element(self):
        element = Element("foo")
        with self.assertRaises(NotImplementedError):
            XmlNode(0, 0).parse_element(element, [])


class ElementNodeTests(TestCase):
    @mock.patch.object(ParserUtils, "bind_element_wild_text")
    @mock.patch.object(ParserUtils, "bind_element_children")
    @mock.patch.object(ParserUtils, "bind_element_text")
    @mock.patch.object(ParserUtils, "bind_element_attrs")
    def test_parse_element(
        self,
        mock_bind_element_attrs,
        mock_bind_element_text,
        mock_bind_element_children,
        mock_bind_element_wild_text,
    ):
        def add_attr(x, *args):
            x["a"] = 1

        def add_text(x, *args):
            x["b"] = 2

        def add_child(x, *args):
            x["c"] = 3

        def add_wild_text(x, *args):
            x["d"] = 4

        mock_bind_element_attrs.side_effect = add_attr
        mock_bind_element_text.side_effect = add_text
        mock_bind_element_children.side_effect = add_child
        mock_bind_element_wild_text.side_effect = add_wild_text

        ctx = XmlContext()
        meta = ctx.build(Foo)

        ele = Element("foo")
        pool = [1, 2, 3]

        node = ElementNode(index=0, position=0, meta=meta, default=None)
        qname, obj = node.parse_element(ele, pool)

        self.assertEqual(QName(ele.tag), qname)
        self.assertEqual(Foo(1, 2, 3, 4), obj)

        mock_bind_element_attrs.assert_called_once_with(mock.ANY, meta, ele)
        mock_bind_element_text.assert_called_once_with(mock.ANY, meta, ele)
        mock_bind_element_children.assert_called_once_with(mock.ANY, meta, 0, pool)
        mock_bind_element_wild_text.assert_called_once_with(mock.ANY, meta, ele)

    @mock.patch.object(XmlContext, "build")
    def test_next_node_when_given_qname_matches_dataclass_var(self, mock_ctx_build):

        ctx = XmlContext()
        var = XmlElement(
            name="a", qname=QName("a"), types=[Foo], dataclass=True, default=Foo,
        )
        meta = XmlMeta(
            name="foo", clazz=None, qname=QName("foo"), nillable=False, vars=[var],
        )
        mock_ctx_build.return_value = replace(meta)
        node = ElementNode(index=0, position=0, meta=meta, default=None)

        actual = node.next_node(var.qname, 1, 10, ctx)
        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(1, actual.index)
        self.assertEqual(10, actual.position)
        self.assertIs(mock_ctx_build.return_value, actual.meta)
        self.assertEqual(Foo, actual.default)

    def test_next_node_when_given_qname_matches_any_element_var(self):
        ctx = XmlContext()
        var = XmlWildcard(name="a", qname=QName("a"), types=[], dataclass=False,)
        meta = XmlMeta(
            name="foo", clazz=None, qname=QName("foo"), nillable=False, vars=[var],
        )
        node = ElementNode(index=0, position=0, meta=meta, default=None)

        actual = node.next_node(var.qname, 1, 10, ctx)
        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(1, actual.index)
        self.assertEqual(10, actual.position)
        self.assertEqual(var.qname, actual.qname)

    def test_next_node_when_given_qname_matches_primitive_var(self):
        ctx = XmlContext()
        var = XmlText(name="a", qname=QName("a"), types=[int], default=100)
        meta = XmlMeta(
            name="foo", clazz=None, qname=QName("foo"), nillable=False, vars=[var]
        )
        node = ElementNode(index=0, position=0, meta=meta, default=None)

        actual = node.next_node(var.qname, 1, 10, ctx)
        self.assertIsInstance(actual, PrimitiveNode)
        self.assertEqual(1, actual.index)
        self.assertEqual(10, actual.position)
        self.assertEqual([int], actual.types)
        self.assertEqual(100, actual.default)
        self.assertEqual(var.is_tokens, actual.tokens)

    def test_next_node_when_given_qname_does_not_match_any_var(self):
        ctx = XmlContext()
        meta = XmlMeta(name="foo", clazz=None, qname=QName("foo"), nillable=False)
        node = ElementNode(index=0, position=0, meta=meta, default=None)

        with self.assertRaises(XmlContextError) as cm:
            node.next_node("nope", 1, 10, ctx)

        self.assertEqual("foo does not support mixed content: nope", str(cm.exception))


class RootNodeTests(TestCase):
    def test_next_node_return_self_on_zero_index(self):
        ctx = XmlContext()
        meta = ctx.build(Foo)
        node = RootNode(index=0, position=0, meta=meta, default=None)
        self.assertIs(node, node.next_node("foo", 0, 0, ctx))

    def test_next_node_return_next_node(self):
        ctx = XmlContext()
        meta = ctx.build(Foo)
        node = RootNode(index=0, position=0, meta=meta, default=None)
        actual = node.next_node("a", 1, 0, ctx)

        self.assertIsInstance(actual, PrimitiveNode)
        self.assertIsNot(actual, node)


class WildcardNodeTests(TestCase):
    @mock.patch.object(ParserUtils, "fetch_any_children")
    @mock.patch.object(ParserUtils, "parse_any_element")
    def test_parse_element(self, mock_parse_any_element, mock_fetch_any_children):
        generic = AnyElement()
        mock_parse_any_element.return_value = generic
        mock_fetch_any_children.return_value = ["a", "b"]

        node = WildcardNode(index=0, position=0, qname="a")
        ele = Element("foo")
        actual = node.parse_element(ele, [1, 2, 3])

        self.assertEqual(("a", generic), actual)
        self.assertEqual(["a", "b"], generic.children)
        mock_parse_any_element.assert_called_once_with(ele)
        mock_fetch_any_children.assert_called_once_with(0, [1, 2, 3])

    def test_next_node(self):
        node = WildcardNode(index=0, position=0, qname="a")
        actual = node.next_node("b", 2, 10, XmlContext())

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(2, actual.index)
        self.assertEqual(10, actual.position)
        self.assertEqual("a", actual.qname)


class SkipNodeTests(TestCase):
    def test_parse_element(self):
        node = SkipNode(index=0, position=0)
        ele = Element("foo")

        actual = node.parse_element(ele, [])
        self.assertEqual((None, None), actual)

    def test_next_node(self):
        node = SkipNode(index=0, position=0)
        actual = node.next_node("b", 2, 10, XmlContext())

        self.assertIsInstance(actual, SkipNode)
        self.assertEqual(2, actual.index)
        self.assertEqual(10, actual.position)


class PrimitiveNodeTests(TestCase):
    @mock.patch.object(ParserUtils, "parse_value")
    def test_parse_element(self, mock_parse_value):
        mock_parse_value.return_value = 13
        node = PrimitiveNode(index=0, position=0, types=[int], default=100)
        ele = Element("foo", nsmap={"foo": "bar"})
        ele.text = "13"

        self.assertEqual((QName("foo"), 13), node.parse_element(ele, []))
        self.assertFalse(node.tokens)
        mock_parse_value.assert_called_once_with(
            node.types, ele.text, 100, ele.nsmap, node.tokens
        )

    def test_next_node(self):
        node = PrimitiveNode(index=0, position=0, types=[])
        actual = node.next_node("b", 2, 10, XmlContext())

        self.assertIsInstance(actual, SkipNode)
        self.assertEqual(2, actual.index)
        self.assertEqual(10, actual.position)
