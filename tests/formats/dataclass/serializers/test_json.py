import json
from unittest.case import TestCase

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.serializers.json import DictFactory
from xsdata.formats.dataclass.serializers.json import JsonSerializer
from xsdata.models.datatype import XmlDate


class JsonSerializerTests(TestCase):
    def setUp(self):
        super().setUp()
        self.books = Books(
            book=[
                BookForm(
                    id="bk001",
                    author="Hightower, Kim",
                    title="The First Book",
                    genre="Fiction",
                    price=44.95,
                    pub_date=XmlDate.from_string("2000-10-01"),
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
        serializer = JsonSerializer(dict_factory=DictFactory.FILTER_NONE)
        actual = serializer.render(self.books)

        expected = {
            "book": [
                {
                    "author": "Hightower, Kim",
                    "genre": "Fiction",
                    "id": "bk001",
                    "lang": "en",
                    "price": 44.95,
                    "pub_date": "2000-10-01",
                    "review": "An amazing story of nothing.",
                    "title": "The First Book",
                },
                {
                    "author": "Nagata, Suanne",
                    "genre": "Biography",
                    "id": "bk002",
                    "lang": "en",
                    "review": "A masterpiece of the fine art of gossiping.",
                    "title": "Becoming Somebody",
                },
            ]
        }
        self.assertEqual(expected, json.loads(actual))

    def test_render_a_none_dataclass_object(self):
        with self.assertRaises(XmlContextError):
            JsonSerializer().render([])
