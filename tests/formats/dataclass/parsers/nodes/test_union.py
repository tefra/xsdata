from dataclasses import make_dataclass
from typing import Union
from unittest import TestCase

from tests.fixtures.models import UnionType
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.nodes import UnionNode
from xsdata.models.mixins import attribute
from xsdata.utils.testing import XmlVarFactory


class UnionNodeTests(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.context = XmlContext()
        self.config = ParserConfig()

    def test_child(self):
        attrs = {"id": "1"}
        ns_map = {"ns0": "xsdata"}
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", qname="foo")
        node = UnionNode(
            position=0,
            var=var,
            config=self.config,
            context=self.context,
            attrs={},
            ns_map={},
        )
        self.assertEqual(node, node.child("foo", attrs, ns_map, 10))

        self.assertEqual(1, node.level)
        self.assertEqual([("start", "foo", attrs, ns_map)], node.events)
        self.assertIsNot(attrs, node.events[0][2])

    def test_bind_appends_end_event_when_level_not_zero(self):
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", qname="foo")
        node = UnionNode(
            position=0,
            var=var,
            config=self.config,
            context=self.context,
            attrs={},
            ns_map={},
        )
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

        meta = self.context.build(root)
        var = next(meta.find_children("item"))
        attrs = {"a": "1", "b": 2}
        ns_map = {}
        node = UnionNode(
            position=0,
            var=var,
            config=self.config,
            context=self.context,
            attrs=attrs,
            ns_map=ns_map,
        )
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
        meta = self.context.build(UnionType)
        var = next(meta.find_children("element"))

        node = UnionNode(
            position=0,
            var=var,
            config=self.config,
            context=self.context,
            attrs={},
            ns_map={},
        )

        with self.assertRaises(ParserError) as cm:
            node.bind("element", None, None, [])

        self.assertEqual("Failed to parse union node: element", str(cm.exception))
