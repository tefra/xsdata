from unittest import TestCase

from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


class XmlSerializerTests(TestCase):
    def setUp(self):
        config = SerializerConfig(indent="  ")
        self.serializer = XmlSerializer(config=config)
        super().setUp()

    def test_render(self):
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
