import json
from unittest.case import TestCase

from tests.fixtures.books import BookForm, Books
from xsdata.formats.dataclass.serializers import DictFactory
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.json import JsonSerializer
from xsdata.models.datatype import XmlDate


class JsonSerializerTests(TestCase):
    def setUp(self) -> None:
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
                    price=29.95,
                    pub_date=XmlDate.from_string("2001-05-15"),
                    review="A masterpiece of the fine art of gossiping.",
                ),
            ]
        )

        self.expected = {
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
                    "price": 29.95,
                    "pub_date": "2001-05-15",
                    "review": "A masterpiece of the fine art of gossiping.",
                    "title": "Becoming Somebody",
                },
            ]
        }

    def test_render(self) -> None:
        serializer = JsonSerializer(dict_factory=DictFactory.FILTER_NONE)
        actual = serializer.render(self.books)

        self.assertEqual(self.expected, json.loads(actual))

    def test_indent(self) -> None:
        config = SerializerConfig(indent="    ")
        serializer = JsonSerializer(config=config)

        actual = serializer.render(self.books)
        expected = f"""{{
    "book": [
        {{
            "author": "{self.expected["book"][0]["author"]}",
            "title": "{self.expected["book"][0]["title"]}",
            "genre": "{self.expected["book"][0]["genre"]}",
            "price": {self.expected["book"][0]["price"]},
            "pub_date": "{self.expected["book"][0]["pub_date"]}",
            "review": "{self.expected["book"][0]["review"]}",
            "id": "{self.expected["book"][0]["id"]}",
            "lang": "en"
        }},
        {{
            "author": "{self.expected["book"][1]["author"]}",
            "title": "{self.expected["book"][1]["title"]}",
            "genre": "{self.expected["book"][1]["genre"]}",
            "price": {self.expected["book"][1]["price"]},
            "pub_date": "{self.expected["book"][1]["pub_date"]}",
            "review": "{self.expected["book"][1]["review"]}",
            "id": "{self.expected["book"][1]["id"]}",
            "lang": "en"
        }}
    ]
}}"""

        self.assertEqual(expected, actual)
