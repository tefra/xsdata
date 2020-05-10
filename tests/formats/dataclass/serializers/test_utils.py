from unittest import mock
from unittest.case import TestCase

from lxml.etree import Element
from lxml.etree import QName
from lxml.etree import SubElement

from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.formats.dataclass.serializers.utils import SerializeUtils
from xsdata.models.enums import QNames


class SerializeUtilsTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.namespaces = Namespaces()
        self.element = Element("root")

    @mock.patch.object(SerializeUtils, "set_attribute")
    def test_set_attributes(self, mock_set_attribute):
        values = dict(a=1, b=2)
        SerializeUtils.set_attributes(self.element, values, self.namespaces)
        mock_set_attribute.assert_has_calls(
            [
                mock.call(self.element, "a", 1, self.namespaces),
                mock.call(self.element, "b", 2, self.namespaces),
            ]
        )

    @mock.patch("xsdata.formats.dataclass.serializers.utils.to_xml", return_value="val")
    def test_set_attribute(self, mock_to_xml):
        SerializeUtils.set_attribute(self.element, "key", "value", self.namespaces)
        self.assertEqual("val", self.element.attrib["key"])
        self.assertEqual(0, len(self.namespaces.ns_map))
        mock_to_xml.assert_called_once_with("value", self.namespaces)

    @mock.patch("xsdata.formats.dataclass.serializers.utils.to_xml", return_value="")
    def test_set_attribute_when_value_empty(self, mock_to_xml):
        SerializeUtils.set_attribute(self.element, "key", "value", self.namespaces)
        self.assertNotIn("key", self.element.attrib)
        self.assertEqual(0, len(self.namespaces.ns_map))
        mock_to_xml.assert_called_once_with("value", self.namespaces)

    @mock.patch("xsdata.formats.dataclass.serializers.utils.to_xml", return_value="val")
    def test_set_attribute_with_qname_key(self, mock_to_xml):
        key = QName("foo", "bar")
        SerializeUtils.set_attribute(self.element, key, "value", self.namespaces)
        self.assertEqual("val", self.element.attrib[key])
        self.assertEqual({"ns0": "foo"}, self.namespaces.ns_map)
        mock_to_xml.assert_called_once_with("value", self.namespaces)

    def test_set_attribute_with_qname_xsi_nil(self):
        SerializeUtils.set_attribute(
            self.element, QNames.XSI_NIL, True, self.namespaces
        )
        self.assertEqual("true", self.element.attrib[QNames.XSI_NIL])

    def test_set_attribute_with_qname_xsi_nil_and_element_has_text(self):
        self.element.text = "foo"

        SerializeUtils.set_attribute(
            self.element, QNames.XSI_NIL, True, self.namespaces
        )
        self.assertNotIn(QNames.XSI_NIL, self.element.attrib)

    def test_set_attribute_with_qname_xsi_nil_and_element_has_children(self):
        SubElement(self.element, "bar")

        SerializeUtils.set_attribute(
            self.element, QNames.XSI_NIL, True, self.namespaces
        )
        self.assertNotIn(QNames.XSI_NIL, self.element.attrib)

    def test_set_nil_attribute(self):
        SerializeUtils.set_nil_attribute(self.element, False, self.namespaces)
        self.assertNotIn(QNames.XSI_NIL, self.element.attrib)

        self.element.text = "foo"
        SerializeUtils.set_nil_attribute(self.element, True, self.namespaces)
        self.assertNotIn(QNames.XSI_NIL, self.element.attrib)

        self.element.text = None
        sub_element = SubElement(self.element, "foo")
        SerializeUtils.set_nil_attribute(self.element, True, self.namespaces)
        self.assertNotIn(QNames.XSI_NIL, self.element.attrib)

        self.element.remove(sub_element)
        SerializeUtils.set_nil_attribute(self.element, True, self.namespaces)
        self.assertEqual("true", self.element.attrib[QNames.XSI_NIL])

    def test_set_text(self):
        SerializeUtils.set_text(self.element, 1, self.namespaces)
        self.assertEqual("1", self.element.text)

        SerializeUtils.set_text(self.element, "", self.namespaces)
        self.assertIsNone(self.element.text)

    def test_set_tail(self):
        SerializeUtils.set_tail(self.element, 1, self.namespaces)
        self.assertEqual("1", self.element.tail)

        SerializeUtils.set_tail(self.element, "", self.namespaces)
        self.assertIsNone(self.element.tail)
