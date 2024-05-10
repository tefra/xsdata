from unittest import TestCase

from tests.fixtures.artists import Artist
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.nodes import StandardNode
from xsdata.models.enums import DataType
from xsdata.utils.testing import XmlMetaFactory, XmlVarFactory


class StandardNodeTests(TestCase):
    def setUp(self):
        super().setUp()
        self.meta = XmlMetaFactory.create(clazz=Artist)
        self.var = XmlVarFactory.create()

    def test_bind_simple(self):
        datatype = DataType.INT
        node = StandardNode(self.meta, self.var, datatype, {}, False, False)
        objects = []

        self.assertTrue(node.bind("a", "13", None, objects))
        self.assertEqual(("a", 13), objects[-1])

    def test_bind_derived(self):
        datatype = DataType.INT
        node = StandardNode(self.meta, self.var, datatype, {}, False, DerivedElement)
        objects = []

        self.assertTrue(node.bind("a", "13", None, objects))
        self.assertEqual(("a", DerivedElement("a", 13)), objects[-1])

    def test_bind_wrapper_type(self):
        datatype = DataType.HEX_BINARY
        node = StandardNode(self.meta, self.var, datatype, {}, False, DerivedElement)
        objects = []

        self.assertTrue(node.bind("a", "13", None, objects))
        self.assertEqual(("a", DerivedElement(qname="a", value=b"\x13")), objects[-1])

    def test_bind_nillable(self):
        datatype = DataType.STRING
        node = StandardNode(self.meta, self.var, datatype, {}, True, None)
        objects = []

        self.assertTrue(node.bind("a", None, None, objects))
        self.assertEqual(("a", None), objects[-1])

        node.nillable = False
        self.assertTrue(node.bind("a", None, None, objects))
        self.assertEqual(("a", ""), objects[-1])

    def test_child(self):
        datatype = DataType.STRING
        node = StandardNode(self.meta, self.var, datatype, {}, False, False)

        with self.assertRaises(XmlContextError):
            node.child("foo", {}, {}, 0)
