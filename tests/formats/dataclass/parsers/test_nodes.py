from dataclasses import dataclass
from dataclasses import replace
from unittest import mock
from unittest.case import TestCase

from lxml.etree import Element
from lxml.etree import QName
from lxml.etree import SubElement

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.elements import XmlWildcard
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.config import ParserConfig
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
            XmlNode(0).next_node(QName("foo"), 0, ctx)

    def test_parse_element(self):
        ele = Element("foo")
        with self.assertRaises(NotImplementedError):
            XmlNode(0).parse_element(ele, [])


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

        node = ElementNode(position=0, meta=meta, config=ParserConfig())
        qname, obj = node.parse_element(ele, pool)

        self.assertEqual(QName(ele.tag), qname)
        self.assertEqual(Foo(1, 2, 3, 4), obj)

        mock_bind_element_attrs.assert_called_once_with(mock.ANY, meta, ele)
        mock_bind_element_text.assert_called_once_with(mock.ANY, meta, ele)
        mock_bind_element_children.assert_called_once_with(mock.ANY, meta, 0, pool)
        mock_bind_element_wild_text.assert_called_once_with(mock.ANY, meta, ele)

    @mock.patch.object(ParserUtils, "parse_xsi_type", return_value=QName("foo"))
    @mock.patch.object(XmlContext, "fetch")
    def test_next_node_when_given_qname_matches_dataclass_var(
        self, mock_ctx_fetch, mock_element_xsi_type
    ):
        ele = Element("a")
        ctx = XmlContext()
        cfg = ParserConfig()
        var = XmlElement(name="a", qname=QName("a"), types=[Foo], dataclass=True)
        meta = XmlMeta(
            name="foo",
            clazz=None,
            qname=QName("foo"),
            source_qname=QName("foo"),
            nillable=False,
            vars=[var],
        )
        xsi_type = QName("foo")
        namespace = meta.qname.namespace
        mock_ctx_fetch.return_value = replace(meta)
        mock_element_xsi_type.return_value = xsi_type
        node = ElementNode(position=0, meta=meta, config=cfg)

        actual = node.next_node(ele, 10, ctx)
        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(10, actual.position)
        self.assertIs(mock_ctx_fetch.return_value, actual.meta)
        mock_ctx_fetch.assert_called_once_with(var.clazz, namespace, xsi_type)

    def test_next_node_when_given_qname_matches_any_element_var(self):
        ele = Element("a")
        ctx = XmlContext()
        cfg = ParserConfig()
        var = XmlWildcard(name="a", qname=QName("a"), types=[], dataclass=False)
        meta = XmlMeta(
            name="foo",
            clazz=None,
            qname=QName("foo"),
            source_qname=QName("foo"),
            nillable=False,
            vars=[var],
        )
        node = ElementNode(position=0, meta=meta, config=cfg)

        actual = node.next_node(ele, 10, ctx)
        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var.qname, actual.qname)

    def test_next_node_when_given_qname_matches_primitive_var(self):
        ele = Element("a")
        ctx = XmlContext()
        cfg = ParserConfig()
        var = XmlText(name="a", qname=QName("a"), types=[int], default=100)
        meta = XmlMeta(
            name="foo",
            clazz=None,
            qname=QName("foo"),
            source_qname=QName("foo"),
            nillable=False,
            vars=[var],
        )
        node = ElementNode(position=0, meta=meta, config=cfg)

        actual = node.next_node(ele, 10, ctx)
        self.assertIsInstance(actual, PrimitiveNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)

    def test_next_node_when_given_qname_does_not_match_any_var(self):
        ele = Element("nope")
        ctx = XmlContext()
        cfg = ParserConfig()
        meta = XmlMeta(
            name="foo",
            clazz=None,
            qname=QName("foo"),
            source_qname=QName("foo"),
            nillable=False,
        )
        node = ElementNode(position=0, meta=meta, config=cfg)

        with self.assertRaises(XmlContextError) as cm:
            node.next_node(ele, 10, ctx)

        self.assertEqual("foo does not support mixed content: nope", str(cm.exception))

    def test_next_node_when_config_fail_on_unknown_properties_is_false(self):
        ele = Element("nope")
        ctx = XmlContext()
        cfg = ParserConfig(fail_on_unknown_properties=False)
        meta = XmlMeta(
            name="foo",
            clazz=None,
            qname=QName("foo"),
            source_qname=QName("foo"),
            nillable=False,
        )
        node = ElementNode(position=0, meta=meta, config=cfg)
        actual = node.next_node(ele, 10, ctx)
        self.assertEqual(SkipNode(position=10), actual)


class RootNodeTests(TestCase):
    def test_next_node_return_self_on_root_element(self):
        ele = Element("foo")
        ctx = XmlContext()
        cfg = ParserConfig()
        meta = ctx.build(Foo)
        node = RootNode(position=0, meta=meta, config=cfg)
        self.assertIs(node, node.next_node(ele, 0, ctx))

    def test_next_node_return_next_node(self):
        root = Element("a")
        ele = SubElement(root, "b")

        ctx = XmlContext()
        cfg = ParserConfig()
        meta = ctx.build(Foo)
        node = RootNode(position=0, meta=meta, config=cfg)
        actual = node.next_node(ele, 0, ctx)

        self.assertIsInstance(actual, PrimitiveNode)
        self.assertIsNot(actual, node)


class WildcardNodeTests(TestCase):
    @mock.patch.object(ParserUtils, "fetch_any_children")
    @mock.patch.object(ParserUtils, "parse_any_element")
    def test_parse_element(self, mock_parse_any_element, mock_fetch_any_children):
        generic = AnyElement()
        mock_parse_any_element.return_value = generic
        mock_fetch_any_children.return_value = ["a", "b"]

        node = WildcardNode(position=0, qname="a")
        ele = Element("foo")
        actual = node.parse_element(ele, [1, 2, 3])

        self.assertEqual(("a", generic), actual)
        self.assertEqual(["a", "b"], generic.children)
        mock_parse_any_element.assert_called_once_with(ele)
        mock_fetch_any_children.assert_called_once_with(0, [1, 2, 3])

    def test_next_node(self):
        ele = Element("foo")
        node = WildcardNode(position=0, qname="a")
        actual = node.next_node(ele, 10, XmlContext())

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual("a", actual.qname)


class PrimitiveNodeTests(TestCase):
    @mock.patch.object(ParserUtils, "parse_value")
    def test_parse_element(self, mock_parse_value):
        mock_parse_value.return_value = 13
        var = XmlText(name="foo", qname=QName("foo"), default=100)
        node = PrimitiveNode(position=0, var=var)
        ele = Element("foo", nsmap={"foo": "bar"})
        ele.text = "13"

        self.assertEqual((QName("foo"), 13), node.parse_element(ele, []))
        mock_parse_value.assert_called_once_with(
            var.types, ele.text, var.default, ele.nsmap, var.is_tokens
        )

    def test_next_node(self):
        ele = Element("foo")
        node = PrimitiveNode(position=0, var=XmlText(name="foo", qname=QName("foo")))

        with self.assertRaises(XmlContextError):
            node.next_node(ele, 10, XmlContext())


class SKipNodeTests(TestCase):
    def test_next_node(self):
        ele = Element("foo")
        node = SkipNode(position=0)
        expected = SkipNode(position=1)

        self.assertEqual(expected, node.next_node(ele, 1, XmlContext()))

    def test_parse_element(self):
        ele = Element("foo")
        node = SkipNode(position=0)
        objects = []

        self.assertEqual((None, None), node.parse_element(ele, objects))
        self.assertEqual(0, len(objects))
