from dataclasses import dataclass
from dataclasses import field
from dataclasses import replace
from typing import List
from typing import Union
from unittest import mock
from unittest.case import TestCase

from lxml import etree
from lxml.etree import Element
from lxml.etree import QName
from lxml.etree import SubElement

from tests import fixtures_dir
from tests.fixtures.books import Books
from xsdata.exceptions import ParserError
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.models.elements import XmlWildcard
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.nodes import ElementNode
from xsdata.formats.dataclass.parsers.nodes import NodeParser
from xsdata.formats.dataclass.parsers.nodes import PrimitiveNode
from xsdata.formats.dataclass.parsers.nodes import RootNode
from xsdata.formats.dataclass.parsers.nodes import SkipNode
from xsdata.formats.dataclass.parsers.nodes import UnionNode
from xsdata.formats.dataclass.parsers.nodes import WildcardNode
from xsdata.formats.dataclass.parsers.nodes import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.mixins import attribute
from xsdata.models.mixins import element


@dataclass
class Foo:
    a: int
    b: int
    c: int


@dataclass
class FooMixed:
    a: int
    b: int
    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807,
        ),
    )


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
    @mock.patch.object(ParserUtils, "bind_element_children")
    @mock.patch.object(ParserUtils, "bind_element_text")
    @mock.patch.object(ParserUtils, "bind_element_attrs")
    def test_parse_element(
        self,
        mock_bind_element_attrs,
        mock_bind_element_text,
        mock_bind_element_children,
    ):
        def add_attr(x, *args):
            x["a"] = 1

        def add_text(x, *args):
            x["b"] = 2

        def add_child(x, *args):
            x["c"] = 3

        mock_bind_element_attrs.side_effect = add_attr
        mock_bind_element_text.side_effect = add_text
        mock_bind_element_children.side_effect = add_child

        ctx = XmlContext()
        meta = ctx.build(Foo)

        ele = Element("foo")
        pool = [1, 2, 3]

        node = ElementNode(position=0, meta=meta, config=ParserConfig())
        qname, obj = node.parse_element(ele, pool)

        self.assertEqual(QName(ele.tag), qname)
        self.assertEqual(Foo(1, 2, 3), obj)

        mock_bind_element_attrs.assert_called_once_with(mock.ANY, meta, ele)
        mock_bind_element_text.assert_called_once_with(mock.ANY, meta, ele)
        mock_bind_element_children.assert_called_once_with(mock.ANY, meta, 0, pool)

    @mock.patch.object(ParserUtils, "bind_mixed_content")
    @mock.patch.object(ParserUtils, "bind_wildcard_text")
    @mock.patch.object(ParserUtils, "bind_element_attrs")
    def test_parse_element_with_mixed_content(
        self, mock_bind_element_attrs, mock_bind_wildcard_text, mock_bind_mixed_content,
    ):
        def add_attr(x, *args):
            x["a"] = 1

        def add_text(x, *args):
            x["b"] = 2

        def add_child(x, *args):
            x["content"] = 3

        mock_bind_element_attrs.side_effect = add_attr
        mock_bind_wildcard_text.side_effect = add_text
        mock_bind_mixed_content.side_effect = add_child

        ctx = XmlContext()
        meta = ctx.build(FooMixed)

        ele = Element("foo")
        pool = [1, 2, 3]

        node = ElementNode(position=0, meta=meta, config=ParserConfig())
        qname, obj = node.parse_element(ele, pool)

        self.assertEqual(QName(ele.tag), qname)
        self.assertEqual(FooMixed(1, 2, 3), obj)

        mock_bind_element_attrs.assert_called_once_with(mock.ANY, meta, ele)
        mock_bind_wildcard_text.assert_called_once_with(mock.ANY, meta.vars[2], ele)
        mock_bind_mixed_content.assert_called_once_with(mock.ANY, meta.vars[2], 0, pool)

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

    def test_next_node_when_given_qname_matches_var_clazz_union(self):
        ele = Element("a")
        ctx = XmlContext()
        cfg = ParserConfig()
        var = XmlElement(
            name="a", qname=QName("a"), types=[Foo, FooMixed], dataclass=True
        )
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

        self.assertIsInstance(actual, UnionNode)
        self.assertEqual(10, actual.position)
        self.assertIs(var, actual.var)
        self.assertIs(ctx, actual.ctx)

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
        self.assertEqual(var, actual.var)

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

        with self.assertRaises(ParserError) as cm:
            node.next_node(ele, 10, ctx)

        self.assertEqual("Unknown property foo:nope", str(cm.exception))

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

        ele = Element("foo")
        var = XmlText(name="foo", qname=QName("a"))
        node = WildcardNode(position=0, var=var)
        actual = node.parse_element(ele, [1, 2, 3])

        self.assertEqual((var.qname, generic), actual)
        self.assertEqual(["a", "b"], generic.children)
        mock_parse_any_element.assert_called_once_with(ele)
        mock_fetch_any_children.assert_called_once_with(0, [1, 2, 3])

    def test_next_node(self):
        ele = Element("foo")
        var = XmlText(name="foo", qname=QName("foo"))
        node = WildcardNode(position=0, var=var)
        actual = node.next_node(ele, 10, XmlContext())

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)


class UnionNodeTests(TestCase):
    def test_next_node(self):
        ele = Element("foo")
        ctx = XmlContext()
        var = XmlText(name="foo", qname=QName("foo"))
        node = UnionNode(position=0, var=var, ctx=ctx)
        self.assertEqual(SkipNode(position=2), node.next_node(ele, 2, ctx))

    def test_parse_element_returns_best_matching_dataclass(self):
        root = Element("root")
        item = SubElement(root, "item")
        item.set("a", "1")
        item.set("b", "2")
        item.text = "foo"

        @dataclass
        class Item:
            value: str = field()
            a: int = attribute()
            b: int = attribute()

        @dataclass
        class Item2:
            a: int = attribute()

        @dataclass
        class Root:
            item: Union[str, int, Item2, Item] = element()

        ctx = XmlContext()
        meta = ctx.build(Root)

        node = UnionNode(position=0, var=meta.vars[0], ctx=ctx)
        qname, obj = node.parse_element(item, [])
        self.assertIsInstance(obj, Item)
        self.assertEqual(1, obj.a)
        self.assertEqual(2, obj.b)
        self.assertEqual("foo", obj.value)

    def test_parse_element_raises_parser_error_on_failure(self):
        root = Element("root")

        @dataclass
        class Item:
            value: str = field()

        @dataclass
        class Root:
            item: Union[int, Item] = element()

        ctx = XmlContext()
        meta = ctx.build(Root)

        node = UnionNode(position=0, var=meta.vars[0], ctx=ctx)

        with self.assertRaises(ParserError) as cm:
            node.parse_element(root, [])

        self.assertEqual("Failed to parse union node: item", str(cm.exception))


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


class NodeParserTests(TestCase):
    def test_parse_from_tree(self):
        path = fixtures_dir.joinpath("books/books.xml")
        tree = etree.parse(path.resolve().as_uri())

        parser = NodeParser()
        actual = parser.parse(tree, Books)
        self.assertEqual(2, len(actual.book))

        # The tree will not be modified
        self.assertEqual(2, len(tree.getroot()))
