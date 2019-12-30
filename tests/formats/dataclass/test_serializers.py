from unittest.case import TestCase

from tests.fixtures.books import BookForm, Books
from xsdata.formats.dataclass.serializers import (
    DictFactory,
    DictSerializer,
    XmlSerializer,
)
from xsdata.models.enums import TagType


class DictSerializerTests(TestCase):
    def setUp(self) -> None:
        super(DictSerializerTests, self).setUp()
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
        serializer = DictSerializer(dict_factory=DictFactory.FILTER_NONE)
        actual = serializer.render(self.books)

        expected = {
            "book": [
                {
                    "author": "Hightower, Kim",
                    "genre": "Fiction",
                    "id": "bk001",
                    "price": 44.95,
                    "pub_date": "2000-10-01",
                    "review": "An amazing story of nothing.",
                    "title": "The First Book",
                },
                {
                    "author": "Nagata, Suanne",
                    "genre": "Biography",
                    "id": "bk002",
                    "review": "A masterpiece of the fine art of gossiping.",
                    "title": "Becoming Somebody",
                },
            ]
        }
        self.assertEqual(expected, actual)


class XmlSerializerTests(TestCase):
    def setUp(self) -> None:
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
            "<books>\n"
            '  <book id="bk001">\n'
            "    <author>Hightower, Kim</author>\n"
            "    <title>The First Book</title>\n"
            "    <genre>Fiction</genre>\n"
            "    <price>44.95</price>\n"
            "    <pub_date>2000-10-01</pub_date>\n"
            "    <review>An amazing story of nothing.</review>\n"
            "  </book>\n"
            '  <book id="bk002">\n'
            "    <author>Nagata, Suanne</author>\n"
            "    <title>Becoming Somebody</title>\n"
            "    <genre>Biography</genre>\n"
            "    <review>A masterpiece of the fine art of gossiping.</review>\n"
            "  </book>\n"
            "</books>\n"
        )
        self.assertEqual(expected, actual)

    def test_render_no_dataclass(self):
        with self.assertRaises(TypeError) as cm:
            XmlSerializer().render(self)
        self.assertEqual(
            f"Object {self} is not a dataclass.", str(cm.exception)
        )

    def test_render_value(self):
        self.assertEqual("1", XmlSerializer.render_value(1))
        self.assertEqual("1.5", XmlSerializer.render_value(1.5))
        self.assertEqual("true", XmlSerializer.render_value(True))
        self.assertEqual("false", XmlSerializer.render_value(False))
        self.assertEqual("all", XmlSerializer.render_value(TagType.ALL))
