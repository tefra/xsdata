from unittest import TestCase, mock

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.parsers.nodes import PrimitiveNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.utils.testing import XmlVarFactory


class PrimitiveNodeTests(TestCase):
    @mock.patch.object(ParserUtils, "parse_value")
    def test_bind(self, mock_parse_value):
        mock_parse_value.return_value = 13
        var = XmlVarFactory.create(
            xml_type=XmlType.TEXT, name="foo", types=(int,), format="Nope"
        )
        ns_map = {"foo": "bar"}
        node = PrimitiveNode(var, ns_map, False)
        objects = []

        self.assertTrue(node.bind("foo", "13", "Impossible", objects))
        self.assertEqual(("foo", 13), objects[-1])

        mock_parse_value.assert_called_once_with(
            value="13",
            types=var.types,
            default=var.default,
            ns_map=ns_map,
            tokens_factory=var.tokens_factory,
            format=var.format,
        )

    def test_bind_nillable_content(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.TEXT, name="foo", types=(str,), nillable=False
        )
        ns_map = {"foo": "bar"}
        node = PrimitiveNode(var, ns_map, False)
        objects = []

        self.assertTrue(node.bind("foo", None, None, objects))
        self.assertEqual("", objects[-1][1])

        var.nillable = True
        self.assertTrue(node.bind("foo", None, None, objects))
        self.assertIsNone(objects[-1][1])

    def test_bind_nillable_bytes_content(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.TEXT,
            name="foo",
            types=(bytes,),
            nillable=False,
        )
        ns_map = {"foo": "bar"}
        node = PrimitiveNode(var, ns_map, False)
        objects = []

        self.assertTrue(node.bind("foo", None, None, objects))
        self.assertEqual(b"", objects[-1][1])

        var.nillable = True
        self.assertTrue(node.bind("foo", None, None, objects))
        self.assertIsNone(objects[-1][1])

    def test_bind_mixed_with_tail_content(self):
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", types=(int,))
        node = PrimitiveNode(var, {}, True)
        objects = []

        self.assertTrue(node.bind("foo", "13", "tail", objects))
        self.assertEqual((None, "tail"), objects[-1])
        self.assertEqual(13, objects[-2][1])

    def test_bind_mixed_without_tail_content(self):
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", types=(int,))
        node = PrimitiveNode(var, {}, True)
        objects = []

        self.assertTrue(node.bind("foo", "13", "", objects))
        self.assertEqual(13, objects[-1][1])

    def test_child(self):
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo")
        node = PrimitiveNode(var, {}, False)

        with self.assertRaises(XmlContextError):
            node.child("foo", {}, {}, 0)
