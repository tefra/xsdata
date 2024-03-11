from unittest import TestCase

from lxml import etree

from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.serializers import LxmlTreeSerializer


class LxmlTreeSerializerTests(TestCase):
    def test_render(self):
        serializer = LxmlTreeSerializer()
        result = serializer.render(books)

        etree.indent(result)
        actual = etree.tostring(result)
        expected = (
            '<ns0:books xmlns:ns0="urn:books">\n'
            "  <book>\n"
            "    <author>Hightower, Kim</author>\n"
            "    <title>The First Book</title>\n"
            "    <genre>Fiction</genre>\n"
            "    <price>44.95</price>\n"
            "    <pub_date>2000-10-01</pub_date>\n"
            "    <review>An amazing story of nothing.</review>\n"
            "  </book>\n"
            "  <book>\n"
            "    <author>Nagata, Suanne</author>\n"
            "    <title>Becoming Somebody</title>\n"
            "    <genre>Biography</genre>\n"
            "    <price>33.95</price>\n"
            "    <pub_date>2001-01-10</pub_date>\n"
            "    <review>A masterpiece of the fine art of gossiping.</review>\n"
            "  </book>\n"
            "</ns0:books>"
        )
        self.assertEqual(expected, actual.decode())
