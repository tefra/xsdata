from unittest import TestCase, mock

from tests.fixtures.artists import Artist
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.nodes import PrimitiveNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.utils.testing import XmlMetaFactory, XmlVarFactory


class PrimitiveNodeTests(TestCase):
    def setUp(self):
        super().setUp()
        self.meta = XmlMetaFactory.create(clazz=Artist)
        self.config = ParserConfig()

    @mock.patch.object(ParserUtils, "parse_var")
    def test_bind(self, mock_parse_var):
        mock_parse_var.return_value = 13
        var = XmlVarFactory.create(
            xml_type=XmlType.TEXT, name="foo", types=(int,), format="Nope"
        )
        ns_map = {"foo": "bar"}
        node = PrimitiveNode(self.meta, var, ns_map, self.config)
        objects = []

        self.assertTrue(node.bind("foo", "13", "Impossible", objects))
        self.assertEqual(("foo", 13), objects[-1])

        mock_parse_var.assert_called_once_with(
            meta=self.meta, var=var, config=self.config, value="13", ns_map=ns_map
        )

    def test_bind_nillable_content(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.TEXT, name="foo", types=(str,), nillable=False
        )
        ns_map = {"foo": "bar"}
        node = PrimitiveNode(self.meta, var, ns_map, self.config)
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
        node = PrimitiveNode(self.meta, var, ns_map, self.config)
        objects = []

        self.assertTrue(node.bind("foo", None, None, objects))
        self.assertEqual(b"", objects[-1][1])

        var.nillable = True
        self.assertTrue(node.bind("foo", None, None, objects))
        self.assertIsNone(objects[-1][1])

    def test_bind_mixed_with_tail_content(self):
        self.meta.mixed_content = True
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", types=(int,))
        node = PrimitiveNode(self.meta, var, {}, self.config)
        objects = []

        self.assertTrue(node.bind("foo", "13", "tail", objects))
        self.assertEqual((None, "tail"), objects[-1])
        self.assertEqual(13, objects[-2][1])

    def test_bind_mixed_without_tail_content(self):
        self.meta.mixed_content = True
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", types=(int,))
        node = PrimitiveNode(self.meta, var, {}, self.config)
        objects = []

        self.assertTrue(node.bind("foo", "13", "", objects))
        self.assertEqual(13, objects[-1][1])

    def test_child(self):
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo")
        node = PrimitiveNode(self.meta, var, {}, self.config)

        with self.assertRaises(XmlContextError):
            node.child("foo", {}, {}, 0)
