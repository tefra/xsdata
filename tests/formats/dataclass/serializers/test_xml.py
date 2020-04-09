from unittest.case import TestCase

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.exceptions import ModelInspectionError
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.formats.dataclass.serializers import XmlSerializer


class XmlSerializerTests(TestCase):
    def setUp(self):
        super(XmlSerializerTests, self).setUp()
        self.books = Books(
            book=[
                BookForm(
                    id="bk001",
                    author="Hightower, Kim",
                    title="The First Book",
                    genre="Fiction",
                    price=44.95,
                    pub_date="2000-10-01",
                    review="An amazing story of nothing.",
                ),
                BookForm(
                    id="bk002",
                    author="Nagata, Suanne",
                    title="Becoming Somebody",
                    genre="Biography",
                    review="A masterpiece of the fine art of gossiping.",
                ),
            ]
        )

    def test_render(self):
        serializer = XmlSerializer(pretty_print=True)
        actual = serializer.render(self.books)

        expected = (
            "<?xml version='1.0' encoding='UTF-8'?>\n"
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
            "    <review>A masterpiece of the fine art of gossiping.</review>\n"
            "  </book>\n"
            "</ns0:books>\n"
        )
        self.assertEqual(expected, actual)

    def test_render_with_provided_namespaces(self):
        serializer = XmlSerializer(pretty_print=True)
        namespaces = Namespaces()
        namespaces.add("urn:books", "burn")
        actual = serializer.render(self.books, namespaces)

        expected = (
            "<?xml version='1.0' encoding='UTF-8'?>\n"
            '<burn:books xmlns:burn="urn:books">\n'
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
            "    <review>A masterpiece of the fine art of gossiping.</review>\n"
            "  </book>\n"
            "</burn:books>\n"
        )
        self.assertEqual(expected, actual)

    def test_render_no_dataclass(self):
        with self.assertRaises(ModelInspectionError) as cm:
            XmlSerializer().render(self)
        self.assertEqual(
            f"Object {self.__class__} is not a dataclass.", str(cm.exception)
        )
