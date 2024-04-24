import sys
from unittest import TestCase
from xml.etree import ElementTree

import pytest

from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.serializers import XmlTreeSerializer


class XmlTreeSerializerTests(TestCase):
    @pytest.mark.skipif(sys.version_info < (3, 9), reason="requires python3.9")
    def test_render(self):
        serializer = XmlTreeSerializer()
        result = serializer.render(books)

        ElementTree.indent(result)
        actual = ElementTree.tostring(result)
        expected = (
            '<ns0:books xmlns:ns0="urn:books">\n'
            '  <book id="bk001" lang="en">\n'
            "    <author>Hightower, Kim</author>\n"
            "    <title>The First Book</title>\n"
            "    <genre>Fiction</genre>\n"
            "    <price>44.95</price>\n"
            "    <pub_date>2000-10-01</pub_date>\n"
            "    <review>An amazing story of nothing.</review>\n"
            "  </book>\n"
            '  <book id="bk002" lang="en">\n'
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
