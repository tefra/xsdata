from unittest import TestCase

from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.nodes import WildcardNode
from xsdata.utils.testing import XmlVarFactory


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
        node = WildcardNode(
            position=0, var=var, attrs=attrs, ns_map=ns_map, factory=AnyElement
        )
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
        node = WildcardNode(
            position=0, var=var, attrs={}, ns_map={}, factory=AnyElement
        )
        actual = node.child("foo", attrs, ns_map, 10)

        self.assertIsInstance(actual, WildcardNode)
        self.assertEqual(10, actual.position)
        self.assertEqual(var, actual.var)
        self.assertEqual(ns_map, actual.ns_map)
        self.assertEqual(attrs, actual.attrs)

    def test_fetch_any_children(self):
        objects = [(x, x) for x in "abc"]
        self.assertEqual(["b", "c"], WildcardNode.fetch_any_children(1, objects))
