from unittest import TestCase

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.nodes import StandardNode
from xsdata.models.enums import DataType


class StandardNodeTests(TestCase):
    def test_bind_simple(self):
        var = DataType.INT
        node = StandardNode(var, {}, False, False)
        objects = []

        self.assertTrue(node.bind("a", "13", None, objects))
        self.assertEqual(("a", 13), objects[-1])

    def test_bind_derived(self):
        var = DataType.INT
        node = StandardNode(var, {}, False, DerivedElement)
        objects = []

        self.assertTrue(node.bind("a", "13", None, objects))
        self.assertEqual(("a", DerivedElement("a", 13)), objects[-1])

    def test_bind_wrapper_type(self):
        var = DataType.HEX_BINARY
        node = StandardNode(var, {}, False, DerivedElement)
        objects = []

        self.assertTrue(node.bind("a", "13", None, objects))
        self.assertEqual(("a", DerivedElement(qname="a", value=b"\x13")), objects[-1])

    def test_bind_nillable(self):
        var = DataType.STRING
        node = StandardNode(var, {}, True, None)
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
