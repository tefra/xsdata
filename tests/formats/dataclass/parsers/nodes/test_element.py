import copy
from dataclasses import make_dataclass
from unittest import mock

from tests.fixtures.books import Books
from tests.fixtures.models import (
    AttrsType,
    ExtendedListType,
    ExtendedType,
    FixedType,
    NillableType,
    Paragraph,
    SequentialType,
    Span,
    TypeA,
    TypeB,
    TypeC,
)
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.generics import AnyElement, DerivedElement
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.nodes import (
    ElementNode,
    PrimitiveNode,
    SkipNode,
    StandardNode,
    UnionNode,
    WildcardNode,
)
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import DataType, Namespace, QNames
from xsdata.utils.testing import FactoryTestCase, XmlMetaFactory, XmlVarFactory


class ElementNodeTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.context = XmlContext()
        self.meta = XmlMetaFactory.create(clazz=TypeC, qname="foo", wildcards=[])
        self.node = ElementNode(
            position=0,
            meta=self.meta,
            context=self.context,
            config=ParserConfig(),
            attrs={},
            ns_map={},
        )

    def test_bind(self) -> None:
        node = ElementNode(
            position=0,
            meta=self.context.build(SequentialType),
            context=self.context,
            config=ParserConfig(),
            attrs={"a": "b", "a0": "0"},
            ns_map={"ns0": "xsdata"},
        )

        objects = [("x1", 1), ("x2", 2), ("x2", 3)]
        expected = SequentialType(a0="0", a1={"a": "b"}, x0=1, x1=[1], x2=[2, 3])

        self.assertTrue(node.bind("foo", "1", "tail", objects))
        self.assertListEqual(objects, [("foo", expected), (None, "tail")])

    def test_bind_nil_value(self) -> None:
        self.node.xsi_nil = True
        objects = []

        self.assertTrue(self.node.bind("foo", None, None, objects))
        self.assertEqual(("foo", None), objects[-1])

    def test_bind_nillable_type(self) -> None:
        self.node.meta = self.context.build(NillableType)
        self.node.xsi_nil = True

        objects = []
        self.assertTrue(self.node.bind("foo", None, None, objects))
        self.assertEqual(("foo", NillableType(None)), objects[-1])

    def test_bind_fixed_value(self) -> None:
        self.node.meta = self.context.build(FixedType)

        objects = []
        self.assertTrue(self.node.bind("foo", "abc", None, objects))
        self.assertEqual(("foo", FixedType()), objects[-1])

    def test_bind_with_derived_element(self) -> None:
        self.node.meta = self.context.build(TypeA)
        self.node.derived_factory = DerivedElement

        objects = []
        self.assertTrue(self.node.bind("foo", "2", None, objects))
        self.assertEqual("foo", objects[-1][0])
        self.assertEqual(DerivedElement("foo", TypeA(2)), objects[-1][1])

    def test_bind_with_wildcard_var(self) -> None:
        self.node.meta = self.context.build(ExtendedType)
        self.node.attrs = {"a": "b"}
        self.node.ns_map = {"ns0": "xsdata"}

        objects = [("a", "1"), ("b", "2")]
        expected = ExtendedType(
            a="1",
            wildcard=AnyElement(
                text="text",
                tail="tail",
                children=[AnyElement(qname="b", text="2")],
                attributes={"a": "b"},
            ),
        )

        self.assertTrue(self.node.bind("foo", "text", "tail", objects))
        self.assertEqual("foo", objects[-1][0])
        self.assertEqual(expected, objects[-1][1])

    def test_bind_with_mixed_flag_true(self) -> None:
        self.node.meta = self.context.build(TypeB)
        self.node.attrs = {"a": "b"}
        self.node.ns_map = {"ns0": "xsdata"}
        self.node.mixed = True

        objects = [("x", 1), ("y", "a")]
        self.assertTrue(self.node.bind("foo", "text", "   ", objects))
        self.assertEqual(1, len(objects))
        self.assertEqual(TypeB(x=1, y="a"), objects[-1][1])

        objects = [("x", 1), ("y", "a")]
        self.assertTrue(self.node.bind("foo", "text", " tail ", objects))
        self.assertEqual(2, len(objects))
        self.assertEqual(None, objects[-1][0])
        self.assertEqual(" tail ", objects[-1][1])

    def test_bind_with_mixed_content_var(self) -> None:
        self.node.meta = self.context.build(Paragraph)
        self.node.attrs = {"a": "b"}
        self.node.ns_map = {"ns0": "xsdata"}

        objects = [("a", 1)]
        expected = Paragraph(content=["text", AnyElement(qname="a", text="1")])

        self.assertTrue(self.node.bind("foo", "text", "tail", objects))
        self.assertListEqual([("foo", expected), (None, "tail")], objects)

    def test_bind_wild_text(self) -> None:
        self.node.meta = self.context.build(ExtendedType)
        var = self.node.meta.wildcards[0]

        params = {}
        self.node.bind_wild_text(params, var, None, None)
        self.assertEqual(0, len(params))

        params = {}
        self.node.bind_wild_text(params, var, "txt", "tail")
        expected = AnyElement(text="txt", tail="tail")
        self.assertEqual({"wildcard": expected}, params)

        self.node.attrs = {"a": "b"}
        self.node.ns_map = {"ns0": "a"}
        self.node.bind_wild_text(params, var, "txt", "tail")
        expected = AnyElement(
            text="txt", tail="tail", children=[expected], attributes=self.node.attrs
        )
        self.assertEqual({"wildcard": expected}, params)

        self.node.meta = self.context.build(ExtendedListType)
        var = self.node.meta.wildcards[0]

        params = {}
        self.node.bind_wild_text(params, var, "txt", "tail")
        self.assertEqual({"wildcard": ["txt"]}, params)

        self.node.bind_wild_text(params, var, None, "tail")
        self.assertEqual({"wildcard": [None, "txt"]}, params)

        self.node.bind_wild_text(params, var, "first", None)
        self.assertEqual({"wildcard": ["first", None, "txt"]}, params)

    def test_bind_attrs(self) -> None:
        self.node.meta = self.context.build(AttrsType)
        self.node.attrs = {
            "index": "0",
            "fixed": "ignored",
            "{what}ever": "qname",
            "extended": "attr",
        }

        params = {}
        self.node.bind_attrs(params)

        expected = {"attrs": {"extended": "attr", "{what}ever": "qname"}, "index": 0}
        self.assertEqual(expected, params)

    def test_bind_attrs_with_fail_on_unknown_attributes(self) -> None:
        self.node.meta = self.context.build(AttrsType)
        self.node.config.fail_on_unknown_attributes = True
        self.node.attrs = {
            "index": "0",
            "fixed": "ignored",
            "{what}ever": "qname",
            "extended": "attr",
        }

        params = {}
        self.node.bind_attrs(params)

        expected = {"attrs": {"extended": "attr", "{what}ever": "qname"}, "index": 0}
        self.assertEqual(expected, params)

    def test_bind_with_fail_on_unknown_attributes(self) -> None:
        self.node.meta = self.context.build(ExtendedType)
        self.node.config.fail_on_unknown_attributes = True
        self.node.attrs = {"a": "b"}

        objects = [("a", "1")]
        with self.assertRaises(ParserError) as cm:
            self.node.bind("foo", "text", "tail", objects)

        self.assertEqual("Unknown attribute ExtendedType:a", str(cm.exception))

    def test_bind_with_fail_on_unknown_attributes_ignores_xsi_attributes(self) -> None:
        self.node.meta = self.context.build(ExtendedType)
        self.node.config.fail_on_unknown_attributes = True
        self.node.attrs = {QNames.XSI_TYPE: "b"}

        objects = []
        self.node.bind("foo", "text", "tail", objects)
        self.assertEqual(1, len(objects))

    @mock.patch("xsdata.formats.dataclass.parsers.nodes.element.logger.warning")
    def test_bind_objects(self, mock_warning) -> None:
        self.node.meta = self.context.build(TypeC)

        objects = [("x", 1), ("x", 2), ("z", 3.0), ("fixed", "bar")]

        params = {}
        self.node.bind_objects(params, objects)
        self.assertEqual({"x": 1, "z": 3.0}, params)

        mock_warning.assert_called_once_with("Unassigned parsed object %s", "x")

    def test_bind_wild_var(self) -> None:
        self.node.meta = self.context.build(ExtendedType)
        x = make_dataclass("x", [("value", int)])

        params = {}
        objects = [("x", x(1)), ("y", 2), ("z", 3.0)]
        self.node.bind_objects(params, objects)
        expected = {
            "wildcard": AnyElement(
                children=[
                    x(1),
                    AnyElement(qname="y", text="2"),
                    AnyElement(qname="z", text="3.0"),
                ]
            )
        }
        self.assertEqual(expected, params)

    def test_bind_wild_list_var(self) -> None:
        self.node.meta = self.context.build(ExtendedListType)

        params = {}
        objects = [("x", 1), ("x", 2), ("z", 3.0)]
        self.node.bind_objects(params, objects)
        expected = {
            "wildcard": [
                AnyElement(qname="x", text="1"),
                AnyElement(qname="x", text="2"),
                AnyElement(qname="z", text="3.0"),
            ]
        }
        self.assertEqual(expected, params)

    def test_prepare_generic_value(self) -> None:
        actual = self.node.prepare_generic_value(None, 1)
        self.assertEqual(1, actual)

        actual = self.node.prepare_generic_value("a", 1)
        expected = AnyElement(qname="a", text="1")
        self.assertEqual(expected, actual)

        actual = self.node.prepare_generic_value("a", "foo")
        expected = AnyElement(qname="a", text="foo")
        self.assertEqual(expected, actual)

        fixture = make_dataclass("Fixture", [("content", str)])
        actual = self.node.prepare_generic_value("a", fixture("foo"))
        self.assertEqual(fixture("foo"), actual)

    def test_bind_tail_of_non_wildcard_attaches_to_wildcard_parent(self) -> None:
        self.node.meta = self.context.build(Paragraph)
        expected_inner_node = Span(content="This is a note inside the paragraph.")
        expected_first_text = "This is before the note."
        expected_tail = "This is after the note."
        expected_outer_node = Paragraph(
            content=[expected_first_text, expected_inner_node, expected_tail]
        )
        objects = []

        inner_node = ElementNode(
            position=0,
            meta=self.context.build(Span),
            context=self.context,
            config=ParserConfig(),
            attrs={},
            ns_map={},
        )

        self.assertTrue(
            inner_node.bind(
                qname="span",
                text=expected_inner_node.content,
                tail=expected_tail,
                objects=objects,
            )
        )

        self.assertListEqual(
            objects, [("span", expected_inner_node), (None, expected_tail)]
        )

        outer_node = ElementNode(
            position=0,
            meta=self.context.build(Paragraph),
            context=self.context,
            config=ParserConfig(),
            attrs={},
            ns_map={},
        )
        self.assertTrue(
            outer_node.bind(
                qname="p",
                text=expected_first_text,
                tail=None,
                objects=objects,
            )
        )

        self.assertListEqual(objects, [("p", expected_outer_node)])

    def test_bind_tail_of_wildcard_attaches_to_wildcard_parent(self) -> None:
        self.node.meta = self.context.build(Paragraph)
        subparagraph = Paragraph(
            content=["This is a subparagraph inside the paragraph."],
        )
        objects = [
            (None, "This is before the subparagraph."),
            ("p", subparagraph),
            (None, "This is after the subparagraph."),
        ]
        self.assertTrue(self.node.bind("foo", None, None, objects))
        result = objects[-1][1]
        expected = Paragraph(
            content=[
                "This is before the subparagraph.",
                subparagraph,
                "This is after the subparagraph.",
            ]
        )
        self.assertEqual(result, expected)

    def test_child(self) -> None:
        var = XmlVarFactory.create(xml_type=XmlType.ELEMENT, name="a", types=(TypeC,))
        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        position = 1
        self.meta.elements[var.qname] = [var]

        actual = self.node.child("a", attrs, ns_map, position)
        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(position, actual.position)

    def test_child_with_unique_element(self) -> None:
        single = XmlVarFactory.create(
            index=1, xml_type=XmlType.ELEMENT, name="cc", types=(TypeC,)
        )
        wildcard = XmlVarFactory.create(
            index=2, xml_type=XmlType.WILDCARD, name="cc", types=(object,)
        )
        self.meta.elements[single.qname] = [single]
        self.meta.wildcards.append(wildcard)

        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        position = 1

        actual = self.node.child("cc", attrs, ns_map, position)
        self.assertIsInstance(actual, ElementNode)
        self.assertIn(single.index, self.node.assigned)

        actual = self.node.child("cc", attrs, ns_map, position)
        self.assertIsInstance(actual, WildcardNode)
        self.assertNotIn(wildcard.index, self.node.assigned)

    @mock.patch.object(ElementNode, "build_node")
    def test_child_when_failed_to_build_next_node(self, mock_build_node) -> None:
        mock_build_node.return_value = None
        element = XmlVarFactory.create(xml_type=XmlType.ELEMENT, name="a")
        wildcard = XmlVarFactory.create(xml_type=XmlType.WILDCARD, name="a")

        self.meta.elements[element.qname] = [element]
        self.meta.wildcards.append(wildcard)

        with self.assertRaises(ParserError) as cm:
            self.node.child("a", {}, {}, 0)

        self.assertEqual("Unknown property foo:a", str(cm.exception))

        self.node.config.fail_on_unknown_properties = False

        actual = self.node.child("foobar", {}, {}, 0)
        self.assertIsInstance(actual, SkipNode)

    def test_build_node_with_dataclass_union_var(self) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            types=(TypeC, TypeB),
        )
        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        actual = self.node.build_node(var.qname, var, attrs, ns_map, 10)

        self.assertIsInstance(actual, UnionNode)
        self.assertEqual(10, actual.position)
        self.assertIs(var, actual.var)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(0, actual.level)
        self.assertEqual(0, len(actual.events))

    @mock.patch.object(ParserUtils, "xsi_type", return_value="foo")
    @mock.patch.object(XmlContext, "fetch")
    def test_build_node_with_dataclass_var(self, mock_ctx_fetch, mock_xsi_type) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            types=(TypeC,),
        )
        xsi_type = "foo"
        namespace = self.meta.namespace
        mock_ctx_fetch.return_value = self.meta
        mock_xsi_type.return_value = xsi_type

        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        actual = self.node.build_node(var.qname, var, attrs, ns_map, 10)

        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(10, actual.position)
        self.assertIs(mock_ctx_fetch.return_value, actual.meta)

        mock_xsi_type.assert_called_once_with(attrs, ns_map)
        mock_ctx_fetch.assert_called_once_with(var.clazz, namespace, xsi_type)

    @mock.patch.object(ParserUtils, "xsi_type", return_value="foo")
    @mock.patch.object(XmlContext, "fetch")
    def test_build_node_with_dataclass_var_and_mismatch_xsi_type(
        self, mock_ctx_fetch, mock_xsi_type
    ) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            types=(TypeB,),
            derived=False,
        )
        xsi_type = "foo"
        namespace = self.meta.namespace
        mock_ctx_fetch.return_value = self.meta
        mock_xsi_type.return_value = xsi_type

        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        actual = self.node.build_node(var.qname, var, attrs, ns_map, 10)

        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(DerivedElement, actual.derived_factory)
        self.assertIs(mock_ctx_fetch.return_value, actual.meta)

        mock_xsi_type.assert_called_once_with(attrs, ns_map)
        mock_ctx_fetch.assert_called_once_with(var.clazz, namespace, xsi_type)

    @mock.patch.object(XmlContext, "fetch")
    def test_build_node_with_dataclass_var_validates_nillable(
        self, mock_ctx_fetch
    ) -> None:
        var = XmlVarFactory.create(xml_type=XmlType.ELEMENT, name="a", types=(TypeC,))
        ns_map = {}
        nillable_meta = copy.deepcopy(self.meta)
        nillable_meta.nillable = True
        mock_ctx_fetch.side_effect = [self.meta, self.meta, nillable_meta]
        attrs = {QNames.XSI_NIL: "false"}

        self.assertIsNotNone(self.node.build_node(var.qname, var, attrs, ns_map, 10))

        attrs = {QNames.XSI_NIL: "true"}
        self.assertIsNone(self.node.build_node(var.qname, var, attrs, ns_map, 10))

        attrs = {QNames.XSI_NIL: "false"}
        self.assertIsNone(self.node.build_node(var.qname, var, attrs, ns_map, 10))

    def test_build_node_with_any_type_var_with_matching_xsi_type(self) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            types=(object,),
            any_type=True,
        )
        attrs = {QNames.XSI_TYPE: "bk:books"}
        ns_map = {"bk": "urn:books"}
        actual = self.node.build_node(var.qname, var, attrs, ns_map, 10)

        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(self.context.build(Books), actual.meta)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertFalse(actual.mixed)

    def test_build_node_with_any_type_var_with_datatype(self) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            types=(object,),
            any_type=True,
        )
        attrs = {QNames.XSI_TYPE: "xs:hexBinary"}
        ns_map = {Namespace.XS.prefix: Namespace.XS.uri}
        actual = self.node.build_node(var.qname, var, attrs, ns_map, 10)

        self.assertIsInstance(actual, StandardNode)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(DataType.HEX_BINARY, actual.datatype)
        self.assertIsNone(actual.derived_factory)

    def test_build_node_with_any_type_var_with_no_matching_xsi_type(self) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            local_name="aaa",
            types=(object,),
            any_type=True,
        )
        attrs = {QNames.XSI_TYPE: "noMatch"}
        actual = self.node.build_node(var.qname, var, attrs, {}, 10)

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual({}, actual.ns_map)

    def test_build_node_with_any_type_var_with_no_xsi_type(self) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            local_name="aaaa",
            types=(object,),
            any_type=True,
        )
        attrs = {}
        actual = self.node.build_node(var.qname, var, attrs, {}, 10)

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual({}, actual.ns_map)

    def test_build_node_with_any_type_var_with_no_xsi_type_and_type_exists(
        self,
    ) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="a",
            local_name="a",
            types=(object,),
            any_type=True,
        )
        attrs = {}
        a = make_dataclass("a", [("a", int)])
        actual = self.node.build_node(var.qname, var, attrs, {}, 10)

        self.assertIsInstance(actual, ElementNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(self.context.build(a), actual.meta)
        self.assertEqual(attrs, actual.attrs)
        self.assertEqual({}, actual.ns_map)
        self.assertFalse(actual.mixed)

    def test_build_node_with_wildcard_var(self) -> None:
        var = XmlVarFactory.create(xml_type=XmlType.WILDCARD, local_name="aaaaa")
        var.process_contents = "skip"

        actual = self.node.build_node(var.qname, var, {}, {}, 10)

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)

    def test_build_node_with_primitive_var(self) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.TEXT, name="a", types=(int,), default=100
        )
        attrs = {"a": "b"}
        ns_map = {"ns0": "xsdata"}
        actual = self.node.build_node(var.qname, var, attrs, ns_map, 10)

        self.assertIsInstance(actual, PrimitiveNode)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(self.meta, actual.meta)
        self.assertEqual(var, actual.var)
