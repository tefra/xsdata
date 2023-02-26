from dataclasses import asdict
from unittest import mock
from unittest import TestCase

from tests import fixtures_dir
from xsdata.codegen.parsers.dtd import DtdParser
from xsdata.exceptions import ParserError
from xsdata.models.dtd import DtdAttributeDefault
from xsdata.models.dtd import DtdAttributeType
from xsdata.models.dtd import DtdContentOccur
from xsdata.models.dtd import DtdContentType
from xsdata.models.dtd import DtdElementType
from xsdata.models.enums import Namespace


class DtdParserTests(TestCase):
    @classmethod
    def parse(cls, file_name: str):
        file_path = fixtures_dir.joinpath(file_name)
        return DtdParser.parse(file_path.read_bytes(), str(file_path.resolve()))

    @mock.patch("lxml.etree.DTD")
    def test_parse_requires_lxml(self, mock_lxml):
        mock_lxml.side_effect = ImportError()
        with self.assertRaises(ParserError) as cm:
            DtdParser.parse(b"", "/file/path/def.dtd")

        self.assertEqual("DtdParser requires lxml to run.", str(cm.exception))

    def test_build_element(self):
        dtd = self.parse("dtd/complete_example.dtd")
        self.assertEqual(8, len(dtd.elements))

        element = dtd.elements[1]
        self.assertEqual(4, len(element.attributes))
        self.assertIsNotNone(element.content)
        self.assertEqual(4, len(element.ns_map))

        element.attributes = []
        element.content = None
        element.ns_map = {}

        expected = {
            "attributes": [],
            "content": None,
            "name": "Post",
            "ns_map": {},
            "prefix": None,
            "type": DtdElementType.ELEMENT,
        }

        self.assertEqual(expected, asdict(dtd.elements[1]))

    def test_build_content(self):
        dtd = self.parse("dtd/complete_example.dtd")
        post = next(el for el in dtd.elements if el.name == "Post")

        actual = asdict(post.content)
        expected = {
            "left": {
                "left": {
                    "left": None,
                    "name": "Origin",
                    "occur": DtdContentOccur.ONCE,
                    "right": None,
                    "type": DtdContentType.ELEMENT,
                },
                "name": None,
                "occur": DtdContentOccur.MULT,
                "right": {
                    "left": None,
                    "name": "Source",
                    "occur": DtdContentOccur.ONCE,
                    "right": None,
                    "type": DtdContentType.ELEMENT,
                },
                "type": DtdContentType.OR,
            },
            "name": None,
            "occur": DtdContentOccur.ONCE,
            "right": {
                "left": {
                    "left": None,
                    "name": "Title",
                    "occur": DtdContentOccur.ONCE,
                    "right": None,
                    "type": DtdContentType.ELEMENT,
                },
                "name": None,
                "occur": DtdContentOccur.ONCE,
                "right": {
                    "left": {
                        "left": None,
                        "name": "Body",
                        "occur": DtdContentOccur.ONCE,
                        "right": None,
                        "type": DtdContentType.ELEMENT,
                    },
                    "name": None,
                    "occur": DtdContentOccur.ONCE,
                    "right": {
                        "left": None,
                        "name": "Tags",
                        "occur": DtdContentOccur.ONCE,
                        "right": None,
                        "type": DtdContentType.ELEMENT,
                    },
                    "type": DtdContentType.SEQ,
                },
                "type": DtdContentType.SEQ,
            },
            "type": DtdContentType.SEQ,
        }
        self.assertEqual(expected, actual)

    def test_build_attribute(self):
        dtd = self.parse("dtd/complete_example.dtd")
        post = next(el for el in dtd.elements if el.name == "Post")

        self.assertEqual(4, len(post.attributes))

        # The order doesn't match the definition...
        actual = {attr.name: asdict(attr) for attr in post.attributes}
        expected = {
            "author": {
                "default": DtdAttributeDefault.REQUIRED,
                "default_value": None,
                "name": "author",
                "prefix": None,
                "type": DtdAttributeType.CDATA,
                "values": [],
            },
            "created_at": {
                "default": DtdAttributeDefault.REQUIRED,
                "default_value": None,
                "name": "created_at",
                "prefix": None,
                "type": DtdAttributeType.CDATA,
                "values": [],
            },
            "lang": {
                "default": DtdAttributeDefault.NONE,
                "default_value": "en",
                "name": "lang",
                "prefix": "xml",
                "type": DtdAttributeType.NMTOKEN,
                "values": [],
            },
            "status": {
                "default": DtdAttributeDefault.NONE,
                "default_value": "draft",
                "name": "status",
                "prefix": None,
                "type": DtdAttributeType.ENUMERATION,
                "values": ["draft", "published"],
            },
        }
        self.assertEqual(expected, actual)

    def test_build_ns_map(self):
        dtd = self.parse("dtd/complete_example.dtd")
        expected = {ns.prefix: ns.uri for ns in Namespace.common()}
        for element in dtd.elements:
            self.assertEqual(expected, element.ns_map)

    def test_with_prefix_namespace(self):
        dtd = self.parse("dtd/prefix_namespace.dtd")

        self.assertEqual(2, len(dtd.elements))

        self.assertEqual("ns", dtd.elements[0].prefix)
        self.assertEqual("ns", dtd.elements[1].prefix)

        self.assertIn("ns", dtd.elements[0].ns_map)
        self.assertEqual("http://www.example.com/", dtd.elements[0].ns_map["ns"])
        self.assertNotIn("ns", dtd.elements[1].ns_map)

    def test_with_default_namespace(self):
        dtd = self.parse("dtd/default_namespace.dtd")

        self.assertEqual(2, len(dtd.elements))

        self.assertIsNone(dtd.elements[0].prefix)
        self.assertIsNone(dtd.elements[1].prefix)

        self.assertIn(None, dtd.elements[0].ns_map)
        self.assertEqual("http://www.example.com/", dtd.elements[0].ns_map[None])
        self.assertNotIn(None, dtd.elements[1].ns_map)
