from io import StringIO
from unittest import TestCase
from xml.sax.saxutils import XMLGenerator

from xsdata.exceptions import XmlWriterError
from xsdata.formats.dataclass.serializers.mixins import XmlWriter
from xsdata.models.enums import DataType
from xsdata.models.enums import QNames


class XmlEventWriterTests(TestCase):
    def setUp(self) -> None:
        super().setUp()

        output = StringIO()
        self.writer = XmlWriter(output=output)
        self.writer.handler = XMLGenerator(
            output,  # type: ignore
            encoding="UTF-8",
            short_empty_elements=True,
        )

    def test_consume(self):
        events = iter(
            [
                (XmlWriter.START_TAG, "{http://www.w3.org/1999/xhtml}p"),
                (XmlWriter.ADD_ATTR, "class", "section"),
                (XmlWriter.SET_DATA, "total:"),
                (XmlWriter.SET_DATA, 105.22),
                (XmlWriter.START_TAG, "{http://www.w3.org/1999/xhtml}br"),
                (XmlWriter.END_TAG, "{http://www.w3.org/1999/xhtml}br"),
                (XmlWriter.END_TAG, "{http://www.w3.org/1999/xhtml}p"),
            ]
        )

        self.writer.write(events)

        lines = self.writer.output.getvalue().split("\n")

        self.assertEqual(2, len(lines))
        self.assertEqual('<?xml version="1.0" encoding="UTF-8"?>', lines[0])
        self.assertEqual(
            (
                '<xhtml:p xmlns:xhtml="http://www.w3.org/1999/xhtml" class="section">'
                "total:<xhtml:br/>105.22</xhtml:p>"
            ),
            lines[1],
        )

    def test_write_with_unhandled_event_raises_exception(self):
        events = iter([("reverse", "p")])

        with self.assertRaises(XmlWriterError) as cm:
            self.writer.write(events)

        self.assertEqual("Unhandled event: `reverse`", str(cm.exception))

    def test_write_removes_xsi_nil_if_necessary(self):
        events = iter(
            [
                (XmlWriter.START_TAG, "root"),
                (XmlWriter.START_TAG, "a"),
                (XmlWriter.ADD_ATTR, QNames.XSI_NIL, "true"),
                (XmlWriter.END_TAG, "a"),
                (XmlWriter.START_TAG, "a"),
                (XmlWriter.ADD_ATTR, QNames.XSI_NIL, "true"),
                (XmlWriter.SET_DATA, "0"),
                (XmlWriter.END_TAG, "a"),
                (XmlWriter.START_TAG, "a"),
                (XmlWriter.ADD_ATTR, QNames.XSI_NIL, "true"),
                (XmlWriter.SET_DATA, ""),
                (XmlWriter.END_TAG, "a"),
                (XmlWriter.START_TAG, "a"),
                (XmlWriter.ADD_ATTR, QNames.XSI_NIL, "true"),
                (XmlWriter.SET_DATA, None),
                (XmlWriter.END_TAG, "a"),
                (XmlWriter.START_TAG, "a"),
                (XmlWriter.ADD_ATTR, QNames.XSI_NIL, "true"),
                (XmlWriter.SET_DATA, [""]),
                (XmlWriter.END_TAG, "a"),
                (XmlWriter.END_TAG, "root"),
            ]
        )
        self.writer.write(events)

        lines = self.writer.output.getvalue().split("\n")
        expected = (
            "<root>"
            '<a xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>'
            "<a>0</a>"
            '<a xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>'
            '<a xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>'
            '<a xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>'
            "</root>"
        )

        self.assertEqual(expected, lines[1])

    def test_write_resets_default_namespace_for_unqualified_elements(self):
        events = iter(
            [
                (XmlWriter.START_TAG, "{a}a"),
                (XmlWriter.START_TAG, "b"),
                (XmlWriter.SET_DATA, "foo"),
                (XmlWriter.START_TAG, "b"),
                (XmlWriter.END_TAG, "{a}a"),
            ]
        )

        self.writer.ns_map = {None: "a"}
        self.writer.write(events)
        lines = self.writer.output.getvalue().split("\n")
        self.assertEqual('<a xmlns="a"><b xmlns="">foo<b/>', lines[1])

    def test_add_attribute(self):
        with self.assertRaises(XmlWriterError) as cm:
            self.writer.add_attribute("foo", "bar")

        self.assertEqual("Empty pending tag.", str(cm.exception))

        self.writer.start_tag("a")
        self.writer.add_attribute("a", "bar")
        self.writer.add_attribute("b", True)
        self.writer.add_attribute("c", "{")
        self.writer.add_attribute("d", "{a}b")
        self.writer.add_attribute(QNames.XSI_TYPE, DataType.STRING.qname)

        expected = {
            (None, "a"): "bar",
            (None, "b"): "true",
            (None, "c"): "{",
            (None, "d"): "ns0:b",
            ("http://www.w3.org/2001/XMLSchema-instance", "type"): "xs:string",
        }

        self.assertEqual(expected, self.writer.attrs)
