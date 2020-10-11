from io import StringIO
from unittest import TestCase
from xml.sax.saxutils import XMLGenerator

from xsdata.exceptions import XmlWriterError
from xsdata.formats.dataclass.serializers.mixins import XmlWriter
from xsdata.formats.dataclass.serializers.mixins import XmlWriterEvent
from xsdata.models.enums import DataType
from xsdata.models.enums import QNames


class XmlEventWriterTests(TestCase):
    def setUp(self) -> None:
        super().setUp()

        output = StringIO()
        self.writer = XmlWriter(output=output)
        self.writer.handler = XMLGenerator(
            output,
            encoding="UTF-8",
            short_empty_elements=True,
        )

    def test_consume(self):
        events = iter(
            [
                (XmlWriterEvent.START, "{http://www.w3.org/1999/xhtml}p"),
                (XmlWriterEvent.ATTR, "class", "section"),
                (XmlWriterEvent.DATA, "total:"),
                (XmlWriterEvent.DATA, 105.22),
                (XmlWriterEvent.START, "{http://www.w3.org/1999/xhtml}br"),
                (XmlWriterEvent.END, "{http://www.w3.org/1999/xhtml}br"),
                (XmlWriterEvent.END, "{http://www.w3.org/1999/xhtml}p"),
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
                (XmlWriterEvent.START, "root"),
                (XmlWriterEvent.START, "a"),
                (XmlWriterEvent.ATTR, QNames.XSI_NIL, "true"),
                (XmlWriterEvent.END, "a"),
                (XmlWriterEvent.START, "a"),
                (XmlWriterEvent.ATTR, QNames.XSI_NIL, "true"),
                (XmlWriterEvent.DATA, "0"),
                (XmlWriterEvent.END, "a"),
                (XmlWriterEvent.START, "a"),
                (XmlWriterEvent.ATTR, QNames.XSI_NIL, "true"),
                (XmlWriterEvent.DATA, ""),
                (XmlWriterEvent.END, "a"),
                (XmlWriterEvent.START, "a"),
                (XmlWriterEvent.ATTR, QNames.XSI_NIL, "true"),
                (XmlWriterEvent.DATA, None),
                (XmlWriterEvent.END, "a"),
                (XmlWriterEvent.START, "a"),
                (XmlWriterEvent.ATTR, QNames.XSI_NIL, "true"),
                (XmlWriterEvent.DATA, [""]),
                (XmlWriterEvent.END, "a"),
                (XmlWriterEvent.END, "root"),
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
                (XmlWriterEvent.START, "{a}a"),
                (XmlWriterEvent.START, "b"),
                (XmlWriterEvent.DATA, "foo"),
                (XmlWriterEvent.START, "b"),
                (XmlWriterEvent.END, "{a}a"),
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
