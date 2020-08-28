from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Union
from unittest import mock
from unittest.case import TestCase

from lxml import etree

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
from xsdata.formats.dataclass.parsers.nodes import ElementParser
from xsdata.formats.dataclass.parsers.nodes import EventParser
from xsdata.formats.dataclass.parsers.nodes import PrimitiveNode
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
    def test_child(self):
        with self.assertRaises(NotImplementedError):
            XmlNode().child("foo", {}, {}, 0)

    def test_bind(self):
        with self.assertRaises(NotImplementedError):
            XmlNode().bind("foo", None, None, [])


class ElementNodeTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.context = XmlContext()
        self.meta = XmlMeta(
            name="foo", clazz=Foo, qname="foo", source_qname="foo", nillable=False,
        )
        self.node = ElementNode(
            position=0,
            meta=self.meta,
            context=self.context,
            config=ParserConfig(),
            attrs={},
            ns_map={},
        )

    @mock.patch.object(ParserUtils, "bind_element_children")
    @mock.patch.object(ParserUtils, "bind_element")
    @mock.patch.object(ParserUtils, "bind_element_attrs")
    def test_bind(
        self, mock_bind_element_attrs, mock_bind_element, mock_bind_element_children,
    ):
        def add_attr(x, *args):
            x["a"] = 1

        def add_text(x, *args):
            x["b"] = 2

        def add_child(x, *args):
            x["c"] = 3

        mock_bind_element_attrs.side_effect = add_attr
        mock_bind_element.side_effect = add_text
        mock_bind_element_children.side_effect = add_child

        node = ElementNode(
            position=0,
            meta=self.context.build(Foo),
            context=self.context,
            config=ParserConfig(),
            attrs={"a": "b"},
            ns_map={"ns0": "xsdata"},
        )

        objects = [1, 2, 3]

        self.assertTrue(node.bind("foo", "text", "tail", objects))
        self.assertEqual("foo", objects[-1][0])
        self.assertEqual(Foo(1, 2, 3), objects[-1][1])

        mock_bind_element_attrs.assert_called_once_with(
            mock.ANY, node.meta, node.attrs, node.ns_map
        )
        mock_bind_element.assert_called_once_with(
            mock.ANY, node.meta, "text", "tail", node.attrs, node.ns_map
        )
        mock_bind_element_children.assert_called_once_with(
            mock.ANY, node.meta, 0, objects
        )

    @mock.patch.object(ParserUtils, "bind_element_children")
    @mock.patch.object(ParserUtils, "bind_element")
    @mock.patch.object(ParserUtils, "bind_element_attrs")
    def test_bind_with_mixed_flag_true(
        self, mock_bind_element_attrs, mock_bind_element, mock_bind_element_children,
    ):
        def add_attr(x, *args):
            x["a"] = 1

        def add_text(x, *args):
            x["b"] = 2

        def add_child(x, *args):
            x["c"] = 3

        mock_bind_element_attrs.side_effect = add_attr
        mock_bind_element.side_effect = add_text
        mock_bind_element_children.side_effect = add_child

        node = ElementNode(
            position=0,
            meta=self.context.build(Foo),
            context=self.context,
            config=ParserConfig(),
            attrs={"a": "b"},
            ns_map={"ns0": "xsdata"},
        )

        node = ElementNode(
            position=0,
            meta=self.context.build(Foo),
            context=self.context,
            config=ParserConfig(),
            attrs={"a": "b"},
            ns_map={"ns0": "xsdata"},
            mixed=True,
        )

        objects = []
        self.assertTrue(node.bind("foo", "text", "   ", objects))
        self.assertEqual(1, len(objects))

        objects = []
        self.assertTrue(node.bind("foo", "text", " tail ", objects))
        self.assertEqual(2, len(objects))
        self.assertEqual(None, objects[-1][0])
        self.assertEqual("tail", objects[-1][1])

    @mock.patch.object(ParserUtils, "bind_mixed_content")
    @mock.patch.object(ParserUtils, "bind_wildcard_element")
    @mock.patch.object(ParserUtils, "bind_element_attrs")
    def test_bind_with_mixed_content_var(
        self,
        mock_bind_element_attrs,
        mock_bind_wildcard_element,
        mock_bind_mixed_content,
    ):
        def add_attr(x, *args):
            x["a"] = 1

        def add_text(x, *args):
            x["b"] = 2

        def add_child(x, *args):
            x["content"] = 3

        mock_bind_element_attrs.side_effect = add_attr
        mock_bind_wildcard_element.side_effect = add_text
        mock_bind_mixed_content.side_effect = add_child

        node = ElementNode(
            position=0,
            meta=self.context.build(FooMixed),
            context=self.context,
            config=ParserConfig(),
            attrs={"a": "b"},
            ns_map={"ns0": "xsdata"},
        )
        objects = [1, 2, 3]

        self.assertTrue(node.bind("foo", "text", "tail", objects))

        self.assertEqual("foo", objects[-1][0])
        self.assertEqual(FooMixed(1, 2, 3), objects[-1][1])

        mock_bind_element_attrs.assert_called_once_with(
            mock.ANY, node.meta, node.attrs, node.ns_map
        )
        mock_bind_wildcard_element.assert_called_once_with(
            mock.ANY, node.meta.vars[2], "text", "tail", node.attrs, node.ns_map
        )
        mock_bind_mixed_content.assert_called_once_with(
            mock.ANY, node.meta.vars[2], 0, objects
        )

    @mock.patch.object(ParserUtils, "parse_xsi_type", return_value="foo")
    @mock.patch.object(XmlContext, "fetch")
    def test_child_when_given_qname_matches_dataclass_var(
        self, mock_ctx_fetch, mock_parse_xsi_type
    ):
        var = XmlElement(name="a", qname="a", types=[Foo], dataclass=True)
        self.meta.vars.append(var)
        xsi_type = "foo"
        namespace = self.meta.namespace
        mock_ctx_fetch.return_value = self.meta
        mock_parse_xsi_type.return_value = xsi_type

        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        actual = self.node.child("a", attrs, ns_map, 10)

        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(10, actual.position)
        self.assertIs(mock_ctx_fetch.return_value, actual.meta)

        mock_parse_xsi_type.assert_called_once_with(attrs, ns_map)
        mock_ctx_fetch.assert_called_once_with(var.clazz, namespace, xsi_type)

    def test_child_when_given_qname_matches_var_clazz_union(self):
        var = XmlElement(name="a", qname="a", types=[Foo, FooMixed], dataclass=True)
        self.meta.vars.append(var)

        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        actual = self.node.child("a", attrs, ns_map, 10)

        self.assertIsInstance(actual, UnionNode)
        self.assertEqual(10, actual.position)
        self.assertIs(var, actual.var)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(0, actual.level)
        self.assertEqual(0, len(actual.events))

    def test_child_when_given_qname_matches_any_element_var(self):
        var = XmlWildcard(name="a", qname="a", types=[], dataclass=False)
        self.meta.vars.append(var)

        actual = self.node.child("a", {}, {}, 10)

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)

    def test_child_when_given_qname_matches_primitive_var(self):
        var = XmlText(name="a", qname="a", types=[int], default=100)
        self.meta.vars.append(var)
        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        actual = self.node.child("a", attrs, ns_map, 10)

        self.assertIsInstance(actual, PrimitiveNode)
        self.assertEqual(var, actual.var)
        self.assertEqual(ns_map, actual.ns_map)

    def test_child_when_given_qname_does_not_match_any_var(self):
        with self.assertRaises(ParserError) as cm:
            self.node.child("unknown", {}, {}, 10)

        self.assertEqual("Unknown property foo:unknown", str(cm.exception))

    def test_child_when_config_fail_on_unknown_properties_is_false(self):
        self.node.config.fail_on_unknown_properties = False
        self.assertEqual(SkipNode(), self.node.child("unknown", {}, {}, 10))


class WildcardNodeTests(TestCase):
    def test_bind(self):
        text = "\n "
        tail = "bar"
        attrs = {"id": "1"}
        ns_map = {"ns0": "xsdata"}

        generic = AnyElement(
            qname="foo",
            text=None,
            tail="bar",
            ns_map=ns_map,
            attributes=attrs,
            children=[1, 2, 3],
        )

        var = XmlText(name="foo", qname="a")
        node = WildcardNode(position=0, var=var, attrs=attrs, ns_map=ns_map)
        objects = [("a", 1), ("b", 2), ("c", 3)]

        self.assertTrue(node.bind("foo", text, tail, objects))
        self.assertEqual(var.qname, objects[-1][0])
        self.assertEqual(generic, objects[-1][1])

    def test_child(self):
        attrs = {"id": "1"}
        ns_map = {"ns0": "xsdata"}
        var = XmlText(name="foo", qname="foo")
        node = WildcardNode(position=0, var=var, attrs={}, ns_map={})
        actual = node.child("foo", attrs, ns_map, 10)

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(attrs, actual.attrs)


class UnionNodeTests(TestCase):
    def test__post_init(self):
        attrs = {"id": "1"}
        ns_map = {"ns0": "xsdata"}
        ctx = XmlContext()
        var = XmlText(name="foo", qname="foo")
        node = UnionNode(position=0, var=var, context=ctx, attrs=attrs, ns_map=ns_map)

        self.assertEqual(0, node.level)
        self.assertEqual(attrs, node.attrs)
        self.assertIsNot(attrs, node.attrs)

    def test_child(self):
        attrs = {"id": "1"}
        ns_map = {"ns0": "xsdata"}
        ctx = XmlContext()
        var = XmlText(name="foo", qname="foo")
        node = UnionNode(position=0, var=var, context=ctx, attrs={}, ns_map={})
        self.assertEqual(node, node.child("foo", attrs, ns_map, 10))

        self.assertEqual(1, node.level)
        self.assertEqual([("start", "foo", attrs, ns_map)], node.events)
        self.assertIsNot(attrs, node.events[0][2])

    def test_bind_appends_end_event_when_level_not_zero(self):
        ctx = XmlContext()
        var = XmlText(name="foo", qname="foo")
        node = UnionNode(position=0, var=var, context=ctx, attrs={}, ns_map={})
        node.level = 1
        objects = []

        self.assertFalse(node.bind("bar", "text", "tail", objects))
        self.assertEqual(0, len(objects))
        self.assertEqual(0, node.level)
        self.assertEqual([("end", "bar", "text", "tail")], node.events)

    def test_bind_returns_best_matching_dataclass(self):
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
        var = meta.vars[0]
        attrs = {"a": "1", "b": 2}
        ns_map = {}
        node = UnionNode(position=0, var=var, context=ctx, attrs=attrs, ns_map=ns_map)
        objects = []

        self.assertTrue(node.bind("item", "foo", None, objects))
        self.assertIsInstance(objects[-1][1], Item)
        self.assertEqual(1, objects[-1][1].a)
        self.assertEqual(2, objects[-1][1].b)
        self.assertEqual("foo", objects[-1][1].value)
        self.assertEqual("item", objects[-1][0])

    def test_bind_raises_parser_error_on_failure(self):
        @dataclass
        class Item:
            value: str = field()

        @dataclass
        class Root:
            item: Union[int, Item] = element()

        ctx = XmlContext()
        meta = ctx.build(Root)
        meta.vars[0]

        node = UnionNode(position=0, var=meta.vars[0], context=ctx, attrs={}, ns_map={})

        with self.assertRaises(ParserError) as cm:
            node.bind("item", None, None, [])

        self.assertEqual("Failed to parse union node: item", str(cm.exception))


class PrimitiveNodeTests(TestCase):
    @mock.patch.object(ParserUtils, "parse_value")
    def test_bind(self, mock_parse_value):
        mock_parse_value.return_value = 13
        var = XmlText(name="foo", qname="foo", default=100)
        ns_map = {"foo": "bar"}
        node = PrimitiveNode(var=var, ns_map=ns_map)
        objects = []

        self.assertTrue(node.bind("foo", "13", "Impossible", objects))
        self.assertEqual(("foo", 13), objects[-1])

        mock_parse_value.assert_called_once_with(
            "13", var.types, var.default, ns_map, var.tokens
        )

    def test_child(self):
        node = PrimitiveNode(var=XmlText(name="foo", qname="foo"), ns_map={})

        with self.assertRaises(XmlContextError):
            node.child("foo", {}, {}, 0)


class SKipNodeTests(TestCase):
    def test_child(self):
        node = SkipNode()
        actual = node.child("foo", {}, {}, 1)

        self.assertIs(node, actual)

    def test_bind(self):
        node = SkipNode()
        self.assertEqual(False, node.bind("foo", None, None, []))


class ElementParserTests(TestCase):
    def test_parse_from_tree(self):
        path = fixtures_dir.joinpath("books/books.xml")
        tree = etree.parse(path.resolve().as_uri())

        parser = ElementParser()
        actual = parser.parse(tree, Books)
        self.assertEqual(2, len(actual.book))

        # The tree will cleared
        self.assertEqual(0, len(tree.getroot()))

    def test_parse_context_unhandled_event(self):
        context = [("escape", None)]
        with self.assertRaises(ParserError):
            parser = ElementParser()
            parser.parse_context(context, Books)


class EventParserTests(TestCase):
    def test_parse_unhandled_event(self):
        source = [("escape", None)]
        with self.assertRaises(ParserError):
            parser = EventParser()
            parser.parse(source, Books)
