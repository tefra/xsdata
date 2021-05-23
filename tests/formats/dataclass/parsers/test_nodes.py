import copy
from dataclasses import dataclass
from dataclasses import field
from dataclasses import make_dataclass
from typing import Any
from typing import List
from typing import Union
from unittest import mock
from unittest.case import TestCase

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.exceptions import ParserError
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.formats.dataclass.parsers.nodes import ElementNode
from xsdata.formats.dataclass.parsers.nodes import NodeParser
from xsdata.formats.dataclass.parsers.nodes import PrimitiveNode
from xsdata.formats.dataclass.parsers.nodes import SkipNode
from xsdata.formats.dataclass.parsers.nodes import StandardNode
from xsdata.formats.dataclass.parsers.nodes import UnionNode
from xsdata.formats.dataclass.parsers.nodes import WildcardNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames
from xsdata.models.mixins import attribute
from xsdata.utils.testing import FactoryTestCase
from xsdata.utils.testing import XmlMetaFactory
from xsdata.utils.testing import XmlVarFactory


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


def add_attr(x, *args):
    x["a"] = 1


def add_text(x, *args):
    x["b"] = 2
    return True


def add_child(x, *args):
    x["c"] = 3


def add_content(x, *args):
    x["content"] = 3


class ElementNodeTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.context = XmlContext()
        self.meta = XmlMetaFactory.create(clazz=Foo, qname="foo", wildcards=[])
        self.node = ElementNode(
            position=0,
            meta=self.meta,
            context=self.context,
            config=ParserConfig(),
            attrs={},
            ns_map={},
        )

    @mock.patch.object(ParserUtils, "bind_objects")
    @mock.patch.object(ParserUtils, "bind_wild_content")
    @mock.patch.object(ParserUtils, "bind_content")
    @mock.patch.object(ParserUtils, "bind_attrs")
    def test_bind(
        self,
        mock_bind_attrs,
        mock_bind_content,
        mock_bind_wild_content,
        mock_bind_objects,
    ):
        mock_bind_attrs.side_effect = add_attr
        mock_bind_content.side_effect = add_text
        mock_bind_objects.side_effect = add_child

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

        mock_bind_attrs.assert_called_once_with(
            mock.ANY, node.meta, node.attrs, node.ns_map
        )
        mock_bind_content.assert_called_once_with(
            mock.ANY, node.meta, "text", node.ns_map
        )
        mock_bind_objects.assert_called_once_with(mock.ANY, node.meta, 0, objects)
        self.assertEqual(0, mock_bind_wild_content.call_count)

    def test_bind_with_derived_element(self):
        a = make_dataclass("A", fields=[])
        node = ElementNode(
            position=0,
            meta=self.context.build(a),
            context=self.context,
            config=ParserConfig(),
            attrs={},
            ns_map={},
            derived=True,
        )

        objects = []

        self.assertTrue(node.bind("foo", None, None, objects))
        self.assertEqual("foo", objects[-1][0])
        self.assertEqual(DerivedElement("foo", a()), objects[-1][1])

    @mock.patch.object(XmlMeta, "find_any_wildcard")
    @mock.patch.object(ParserUtils, "bind_objects")
    @mock.patch.object(ParserUtils, "bind_wild_content")
    @mock.patch.object(ParserUtils, "bind_content")
    @mock.patch.object(ParserUtils, "bind_attrs")
    def test_bind_with_wildcard_var(
        self,
        mock_bind_attrs,
        mock_bind_content,
        mock_bind_wild_content,
        mock_bind_objects,
        mock_find_any_wildcard,
    ):
        mock_bind_attrs.side_effect = add_attr
        mock_bind_content.return_value = False
        mock_bind_wild_content.side_effect = add_text
        mock_bind_objects.side_effect = add_child
        mock_find_any_wildcard.return_value = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, qname="b", name="b"
        )

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

        mock_bind_attrs.assert_called_once_with(
            mock.ANY, node.meta, node.attrs, node.ns_map
        )
        mock_bind_content.assert_called_once_with(
            mock.ANY, node.meta, "text", node.ns_map
        )
        mock_bind_objects.assert_called_once_with(mock.ANY, node.meta, 0, objects)

    @mock.patch.object(ParserUtils, "bind_objects")
    @mock.patch.object(ParserUtils, "bind_content")
    @mock.patch.object(ParserUtils, "bind_attrs")
    def test_bind_with_mixed_flag_true(
        self, mock_bind_attrs, mock_bind_content, mock_bind_objects
    ):
        mock_bind_attrs.side_effect = add_attr
        mock_bind_content.side_effect = add_text
        mock_bind_objects.side_effect = add_child

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
        self.assertEqual(" tail ", objects[-1][1])

    @mock.patch.object(ParserUtils, "bind_mixed_objects")
    @mock.patch.object(ParserUtils, "bind_wild_content")
    @mock.patch.object(ParserUtils, "bind_attrs")
    def test_bind_with_mixed_content_var(
        self,
        mock_bind_attrs,
        mock_bind_wild_content,
        mock_bind_mixed_objects,
    ):
        mock_bind_attrs.side_effect = add_attr
        mock_bind_wild_content.side_effect = add_text
        mock_bind_mixed_objects.side_effect = add_content

        node = ElementNode(
            position=0,
            meta=self.context.build(FooMixed),
            context=self.context,
            config=ParserConfig(),
            attrs={"a": "b"},
            ns_map={"ns0": "xsdata"},
        )
        wildcard = node.meta.find_any_wildcard()
        objects = [1, 2, 3]

        self.assertTrue(node.bind("foo", "text", "tail", objects))

        self.assertEqual("foo", objects[-1][0])
        self.assertEqual(FooMixed(1, 2, 3), objects[-1][1])

        mock_bind_attrs.assert_called_once_with(
            mock.ANY, node.meta, node.attrs, node.ns_map
        )

        mock_bind_wild_content.assert_called_once_with(
            mock.ANY, wildcard, "text", "tail", node.attrs, node.ns_map
        )
        mock_bind_mixed_objects.assert_called_once_with(mock.ANY, wildcard, 0, objects)

    def test_child(self):
        var = XmlVarFactory.create(xml_type=XmlType.ELEMENT, qname="a", types=(Foo,))
        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        position = 1
        self.meta.elements[var.qname] = [var]

        actual = self.node.child("a", attrs, ns_map, position)
        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(position, actual.position)

    def test_child_with_unique_element(self):
        single = XmlVarFactory.create(xml_type=XmlType.ELEMENT, qname="a", types=(Foo,))
        wildcard = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, qname="a", types=(object,)
        )
        self.meta.elements[single.qname] = [single]
        self.meta.wildcards.append(wildcard)

        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        position = 1

        actual = self.node.child("a", attrs, ns_map, position)
        self.assertIsInstance(actual, ElementNode)
        self.assertIn(id(single), self.node.assigned)

        actual = self.node.child("a", attrs, ns_map, position)
        self.assertIsInstance(actual, WildcardNode)
        self.assertNotIn(id(wildcard), self.node.assigned)

    @mock.patch.object(ElementNode, "build_node")
    def test_child_when_failed_to_build_next_node(self, mock_build_node):
        mock_build_node.return_value = None
        element = XmlVarFactory.create(xml_type=XmlType.ELEMENT, qname="a")
        wildcard = XmlVarFactory.create(xml_type=XmlType.WILDCARD, qname="a")

        self.meta.elements[element.qname] = [element]
        self.meta.wildcards.append(wildcard)

        with self.assertRaises(ParserError) as cm:
            self.node.child("a", {}, {}, 0)

        self.assertEqual("Unknown property foo:a", str(cm.exception))

        self.node.config.fail_on_unknown_properties = False

        actual = self.node.child("foobar", {}, {}, 0)
        self.assertIsInstance(actual, SkipNode)

    def test_build_node_with_dataclass_union_var(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            qname="a",
            types=(Foo, FooMixed),
        )
        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        actual = self.node.build_node(var, attrs, ns_map, 10)

        self.assertIsInstance(actual, UnionNode)
        self.assertEqual(10, actual.position)
        self.assertIs(var, actual.var)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(0, actual.level)
        self.assertEqual(0, len(actual.events))

    @mock.patch.object(ParserUtils, "xsi_type", return_value="foo")
    @mock.patch.object(XmlContext, "fetch")
    def test_build_node_with_dataclass_var(self, mock_ctx_fetch, mock_xsi_type):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            qname="a",
            types=(Foo,),
            derived=True,
        )
        xsi_type = "foo"
        namespace = self.meta.namespace
        mock_ctx_fetch.return_value = self.meta
        mock_xsi_type.return_value = xsi_type

        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        actual = self.node.build_node(var, attrs, ns_map, 10)

        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(10, actual.position)
        self.assertTrue(actual.derived)
        self.assertIs(mock_ctx_fetch.return_value, actual.meta)

        mock_xsi_type.assert_called_once_with(attrs, ns_map)
        mock_ctx_fetch.assert_called_once_with(var.clazz, namespace, xsi_type)

    @mock.patch.object(XmlContext, "fetch")
    def test_build_node_with_dataclass_var_validates_nillable(self, mock_ctx_fetch):
        var = XmlVarFactory.create(xml_type=XmlType.ELEMENT, qname="a", types=(Foo,))
        ns_map = {}
        nillable_meta = copy.deepcopy(self.meta)
        nillable_meta.nillable = True
        mock_ctx_fetch.side_effect = [self.meta, self.meta, nillable_meta]
        attrs = {QNames.XSI_NIL: "false"}

        self.assertIsNotNone(self.node.build_node(var, attrs, ns_map, 10))

        attrs = {QNames.XSI_NIL: "true"}
        self.assertIsNotNone(self.node.build_node(var, attrs, ns_map, 10))

        attrs = {QNames.XSI_NIL: "false"}
        self.assertIsNone(self.node.build_node(var, attrs, ns_map, 10))

    def test_build_node_with_any_type_var_with_matching_xsi_type(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            qname="a",
            types=(object,),
            any_type=True,
        )
        attrs = {QNames.XSI_TYPE: "bk:books"}
        ns_map = {"bk": "urn:books"}
        actual = self.node.build_node(var, attrs, ns_map, 10)

        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(self.context.build(Books), actual.meta)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertFalse(actual.mixed)

    def test_build_node_with_any_type_var_with_datatype(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            qname="a",
            types=(object,),
            any_type=True,
        )
        attrs = {QNames.XSI_TYPE: "xs:hexBinary"}
        ns_map = {Namespace.XS.prefix: Namespace.XS.uri}
        actual = self.node.build_node(var, attrs, ns_map, 10)

        self.assertIsInstance(actual, StandardNode)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(DataType.HEX_BINARY, actual.datatype)
        self.assertEqual(var.derived, actual.derived)

    def test_build_node_with_any_type_var_with_no_matching_xsi_type(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            qname="a",
            types=(object,),
            any_type=True,
        )
        attrs = {QNames.XSI_TYPE: "noMatch"}
        actual = self.node.build_node(var, attrs, {}, 10)

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual({}, actual.ns_map)

    def test_build_node_with_any_type_var_with_no_xsi_type(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            qname="a",
            types=(object,),
            any_type=True,
        )
        attrs = {}
        actual = self.node.build_node(var, attrs, {}, 10)

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual({}, actual.ns_map)

    def test_build_node_with_wildcard_var(self):
        var = XmlVarFactory.create(xml_type=XmlType.WILDCARD, qname="a")

        actual = self.node.build_node(var, {}, {}, 10)

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)

    def test_build_node_with_primitive_var(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.TEXT, qname="a", types=(int,), default=100
        )
        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        actual = self.node.build_node(var, attrs, ns_map, 10)

        self.assertIsInstance(actual, PrimitiveNode)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(var, actual.var)


class WildcardNodeTests(TestCase):
    def test_bind(self):
        text = "\n "
        tail = "bar"
        attrs = {"id": "1"}
        ns_map = {"ns0": "xsdata"}

        generic = AnyElement(
            qname="foo",
            text="",
            tail="bar",
            attributes=attrs,
            children=[1, 2, 3],
        )

        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", qname="a")
        node = WildcardNode(position=0, var=var, attrs=attrs, ns_map=ns_map)
        objects = [("a", 1), ("b", 2), ("c", 3)]

        self.assertTrue(node.bind("foo", text, tail, objects))
        self.assertEqual(var.qname, objects[-1][0])
        self.assertEqual(generic, objects[-1][1])

        # Preserve whitespace if no children
        node.position = 1
        node.bind("foo", text, tail, objects)
        generic.text = text
        generic.children = []
        self.assertEqual(generic, objects[-1][1])

        # Not a wildcard, no tail/attrs/children skip wrapper
        tail = None
        text = "1"
        node.attrs = {}
        node.position = 2
        node.bind("a", text, tail, objects)
        self.assertEqual("1", objects[-1][1])

    def test_child(self):
        attrs = {"id": "1"}
        ns_map = {"ns0": "xsdata"}
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", qname="foo")
        node = WildcardNode(position=0, var=var, attrs={}, ns_map={})
        actual = node.child("foo", attrs, ns_map, 10)

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(attrs, actual.attrs)


class UnionNodeTests(TestCase):
    def test_child(self):
        attrs = {"id": "1"}
        ns_map = {"ns0": "xsdata"}
        ctx = XmlContext()
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", qname="foo")
        node = UnionNode(position=0, var=var, context=ctx, attrs={}, ns_map={})
        self.assertEqual(node, node.child("foo", attrs, ns_map, 10))

        self.assertEqual(1, node.level)
        self.assertEqual([("start", "foo", attrs, ns_map)], node.events)
        self.assertIsNot(attrs, node.events[0][2])

    def test_bind_appends_end_event_when_level_not_zero(self):
        ctx = XmlContext()
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", qname="foo")
        node = UnionNode(position=0, var=var, context=ctx, attrs={}, ns_map={})
        node.level = 1
        objects = []

        self.assertFalse(node.bind("bar", "text", "tail", objects))
        self.assertEqual(0, len(objects))
        self.assertEqual(0, node.level)
        self.assertEqual([("end", "bar", "text", "tail")], node.events)

    def test_bind_returns_best_matching_object(self):
        item = make_dataclass(
            "Item", [("value", str), ("a", int, attribute()), ("b", int, attribute())]
        )
        item2 = make_dataclass("Item2", [("a", int, attribute())])
        root = make_dataclass("Root", [("item", Union[str, int, item2, item])])

        ctx = XmlContext()
        meta = ctx.build(root)
        var = meta.find_elements("item")[0]
        attrs = {"a": "1", "b": 2}
        ns_map = {}
        node = UnionNode(position=0, var=var, context=ctx, attrs=attrs, ns_map=ns_map)
        objects = []

        self.assertTrue(node.bind("item", "1", None, objects))
        self.assertIsInstance(objects[-1][1], item)
        self.assertEqual(1, objects[-1][1].a)
        self.assertEqual(2, objects[-1][1].b)
        self.assertEqual("1", objects[-1][1].value)
        self.assertEqual("item", objects[-1][0])

        self.assertEqual(2, len(node.events))
        self.assertEqual(("start", "item", attrs, ns_map), node.events[0])
        self.assertEqual(("end", "item", "1", None), node.events[1])
        self.assertIsNot(node.attrs, node.events[0][2])
        self.assertIs(node.ns_map, node.events[0][3])

        node.events.clear()
        node.attrs.clear()
        self.assertTrue(node.bind("item", "1", None, objects))
        self.assertEqual(1, objects[-1][1])

        self.assertTrue(node.bind("item", "a", None, objects))
        self.assertEqual("a", objects[-1][1])

    def test_bind_raises_parser_error_on_failure(self):
        item = make_dataclass("Item", [("value", str)])
        root = make_dataclass("Root", [("item", Union[int, item])])

        ctx = XmlContext()
        meta = ctx.build(root)
        var = meta.find_elements("item")[0]

        node = UnionNode(position=0, var=var, context=ctx, attrs={}, ns_map={})

        with self.assertRaises(ParserError) as cm:
            node.bind("item", None, None, [])

        self.assertEqual("Failed to parse union node: item", str(cm.exception))


class PrimitiveNodeTests(TestCase):
    @mock.patch.object(ParserUtils, "parse_value")
    def test_bind(self, mock_parse_value):
        mock_parse_value.return_value = 13
        var = XmlVarFactory.create(
            xml_type=XmlType.TEXT, name="foo", qname="foo", types=(int,), format="Nope"
        )
        ns_map = {"foo": "bar"}
        node = PrimitiveNode(var, ns_map)
        objects = []

        self.assertTrue(node.bind("foo", "13", "Impossible", objects))
        self.assertEqual(("foo", 13), objects[-1])

        mock_parse_value.assert_called_once_with(
            "13", var.types, var.default, ns_map, var.tokens, var.format
        )

    def test_bind_derived_mode(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.TEXT, name="foo", qname="foo", types=(int,), derived=True
        )
        ns_map = {"foo": "bar"}
        node = PrimitiveNode(var, ns_map)
        objects = []

        self.assertTrue(node.bind("foo", "13", "Impossible", objects))
        self.assertEqual(DerivedElement("foo", 13), objects[-1][1])

    def test_bind_nillable_content(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.TEXT, name="foo", qname="foo", types=(str,), nillable=False
        )
        ns_map = {"foo": "bar"}
        node = PrimitiveNode(var, ns_map)
        objects = []

        self.assertTrue(node.bind("foo", None, None, objects))
        self.assertEqual("", objects[-1][1])

        var.nillable = True
        self.assertTrue(node.bind("foo", None, None, objects))
        self.assertIsNone(objects[-1][1])

    def test_child(self):
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", qname="foo")
        node = PrimitiveNode(var, {})

        with self.assertRaises(XmlContextError):
            node.child("foo", {}, {}, 0)


class StandardNodeTests(TestCase):
    def test_bind_simple(self):
        var = DataType.INT
        node = StandardNode(var, {}, False, False)
        objects = []

        self.assertTrue(node.bind("a", "13", None, objects))
        self.assertEqual(("a", 13), objects[-1])

    def test_bind_derived(self):
        var = DataType.INT
        node = StandardNode(var, {}, True, False)
        objects = []

        self.assertTrue(node.bind("a", "13", None, objects))
        self.assertEqual(("a", DerivedElement("a", 13)), objects[-1])

    def test_bind_wrapper_type(self):
        var = DataType.HEX_BINARY
        node = StandardNode(var, {}, True, False)
        objects = []

        self.assertTrue(node.bind("a", "13", None, objects))
        self.assertEqual(("a", DerivedElement(qname="a", value=b"\x13")), objects[-1])

    def test_bind_nillable(self):
        var = DataType.STRING
        node = StandardNode(var, {}, False, True)
        objects = []

        self.assertTrue(node.bind("a", None, None, objects))
        self.assertEqual(("a", None), objects[-1])

        node.nillable = False
        self.assertTrue(node.bind("a", None, None, objects))
        self.assertEqual(("a", ""), objects[-1])

    def test_child(self):
        node = StandardNode(DataType.STRING, {}, False, False)

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


class NodeParserTests(TestCase):
    def setUp(self):
        self.parser = NodeParser()

    def test_parse(self):
        @dataclass
        class TestHandler(XmlHandler):
            def parse(self, source: Any) -> Any:
                return Books()

        self.parser.handler = TestHandler
        self.assertEqual(Books(), self.parser.parse([], Books))

    def test_parse_when_result_type_is_wrong(self):
        parser = self.parser
        with self.assertRaises(ParserError) as cm:
            parser.parse([], Books)

        self.assertEqual("Failed to create target class `Books`", str(cm.exception))

    def test_start(self):
        queue = []
        objects = []

        attrs = {"k": "v"}
        ns_map = {"a": "b"}
        self.parser.start(Books, queue, objects, "{urn:books}books", attrs, ns_map)
        actual = queue[0]

        self.assertEqual(1, len(queue))
        self.assertEqual(0, actual.position)
        self.assertEqual(self.parser.context, actual.context)
        self.assertEqual(self.parser.context.build(Books), actual.meta)
        self.assertEqual(self.parser.config, actual.config)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertFalse(actual.mixed)
        self.assertFalse(actual.derived)
        self.assertIsNone(actual.xsi_type)

        self.parser.start(Books, queue, objects, "book", {}, {})
        actual = queue[1]

        self.assertEqual(2, len(queue))
        self.assertEqual(0, actual.position)
        self.assertEqual(self.parser.context, actual.context)
        self.assertEqual(self.parser.context.build(BookForm), actual.meta)
        self.assertEqual(self.parser.config, actual.config)
        self.assertEqual({}, actual.attrs)
        self.assertEqual({}, actual.ns_map)
        self.assertFalse(actual.mixed)
        self.assertFalse(actual.derived)
        self.assertIsNone(actual.xsi_type)

    def test_start_with_undefined_class(self):
        parser = self.parser
        queue = []
        objects = []

        attrs = {"k": "v"}
        ns_map = {"a": "b"}
        parser.start(None, queue, objects, "{urn:books}books", attrs, ns_map)
        actual = queue[0]

        self.assertEqual(1, len(queue))
        self.assertEqual(0, actual.position)
        self.assertEqual(self.parser.context, actual.context)
        self.assertEqual(self.parser.context.build(Books), actual.meta)
        self.assertEqual(self.parser.config, actual.config)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertFalse(actual.mixed)
        self.assertFalse(actual.derived)
        self.assertIsNone(actual.xsi_type)

        with self.assertRaises(ParserError) as cm:
            parser.start(None, [], [], "{unknown}hopefully", {}, {})

        self.assertEqual(
            "No class found matching root: {unknown}hopefully", str(cm.exception)
        )

    def test_start_with_any_type_root(self):
        parser = self.parser
        queue = []
        objects = []

        attrs = {QNames.XSI_TYPE: "bk:books"}
        ns_map = {"bk": "urn:books", "xsi": Namespace.XSI.uri}
        parser.start(None, queue, objects, "doc", attrs, ns_map)
        actual = queue[0]

        self.assertEqual(1, len(queue))
        self.assertEqual(0, actual.position)
        self.assertEqual(self.parser.context, actual.context)
        self.assertEqual(self.parser.context.build(Books), actual.meta)
        self.assertEqual(self.parser.config, actual.config)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertFalse(actual.mixed)
        self.assertTrue(actual.derived)
        self.assertEqual("{urn:books}books", actual.xsi_type)

    def test_start_with_derived_class(self):
        a = make_dataclass("a", fields=[])
        b = make_dataclass("b", fields=[], bases=(a,))

        parser = NodeParser()
        queue = []
        objects = []

        attrs = {QNames.XSI_TYPE: "b"}
        ns_map = {}
        parser.start(a, queue, objects, "a", attrs, ns_map)

        actual = queue[0]

        self.assertEqual(1, len(queue))
        self.assertEqual(0, actual.position)
        self.assertEqual(parser.context, actual.context)
        self.assertEqual(parser.context.build(b), actual.meta)
        self.assertEqual(parser.config, actual.config)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual({}, actual.ns_map)
        self.assertFalse(actual.mixed)
        self.assertTrue(actual.derived)
        self.assertEqual("b", actual.xsi_type)

    @mock.patch.object(PrimitiveNode, "bind", return_value=True)
    def test_end(self, mock_assemble):
        parser = NodeParser()
        objects = [("q", "result")]
        queue = []
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", qname="foo")
        queue.append(PrimitiveNode(var, ns_map={}))

        result = parser.end(queue, objects, "author", "foobar", None)
        self.assertEqual("result", result)
        self.assertEqual(0, len(queue))
        self.assertEqual(("q", result), objects[-1])
        mock_assemble.assert_called_once_with("author", "foobar", None, objects)

    def test_end_with_no_result(self):
        parser = NodeParser()
        objects = [("q", "result")]
        queue = [SkipNode()]

        result = parser.end(queue, objects, "author", "foobar", None)
        self.assertIsNone(result)
        self.assertEqual(0, len(queue))

    def test_start_prefix_mapping(self):
        parser = NodeParser()
        parser.start_prefix_mapping("bar", "foo")
        parser.start_prefix_mapping("bar", "exists")
        self.assertEqual({"bar": "foo"}, parser.ns_map)

        parser.start_prefix_mapping(None, "a")
        self.assertEqual({"bar": "foo", None: "a"}, parser.ns_map)

        parser.start_prefix_mapping(None, "b")
        self.assertEqual({"bar": "foo", None: "a"}, parser.ns_map)
