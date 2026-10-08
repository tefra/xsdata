from dataclasses import dataclass, field
from unittest import TestCase

from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


@dataclass
class Country:
    code: str = field(metadata={"type": "Attribute"})


@dataclass
class Address:
    country: Country | None = field(
        default=None, metadata={"type": "Element", "nillable": True}
    )


class XmlSerializerTests(TestCase):
    def setUp(self) -> None:
        config = SerializerConfig(indent="  ")
        self.serializer = XmlSerializer(config=config)
        super().setUp()

    def test_render(self) -> None:
        result = self.serializer.render(books, ns_map={None: "urn:books"})
        expected = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<books xmlns="urn:books">\n'
            '  <book xmlns="" id="bk001" lang="en">\n'
            "    <author>Hightower, Kim</author>\n"
            "    <title>The First Book</title>\n"
            "    <genre>Fiction</genre>\n"
            "    <price>44.95</price>\n"
            "    <pub_date>2000-10-01</pub_date>\n"
            "    <review>An amazing story of nothing.</review>\n"
            "  </book>\n"
            '  <book xmlns="" id="bk002" lang="en">\n'
            "    <author>Nagata, Suanne</author>\n"
            "    <title>Becoming Somebody</title>\n"
            "    <genre>Biography</genre>\n"
            "    <price>33.95</price>\n"
            "    <pub_date>2001-01-10</pub_date>\n"
            "    <review>A masterpiece of the fine art of gossiping.</review>\n"
            "  </book>\n"
            "</books>\n"
        )

        self.assertEqual(expected, result)

    def test_render_nillable_field_with_attributes_only_type(self) -> None:
        serializer = XmlSerializer(config=SerializerConfig(xml_declaration=False))
        present = serializer.render(Address(country=Country(code="DE")))
        absent = serializer.render(Address())

        self.assertEqual('<Address><country code="DE"/></Address>', present)
        self.assertEqual(
            "<Address>"
            '<country xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>'
            "</Address>",
            absent,
        )
        parser = XmlParser()
        self.assertEqual(
            Country(code="DE"), parser.from_string(present, Address).country
        )
        self.assertIsNone(parser.from_string(absent, Address).country)
