import json
from decimal import Decimal
from unittest.case import TestCase

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.formats.dataclass.serializers import DictFactory
from xsdata.formats.dataclass.serializers import DictSerializer
from xsdata.formats.dataclass.serializers.json import JsonEncoder
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace


class DictSerializerTests(TestCase):
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
        self.assertEqual(expected, actual)


class JsonEncoderTests(TestCase):
    def test_encode_enum(self):
        actual = json.dumps({"enum": Namespace.XS}, cls=JsonEncoder)
        self.assertEqual('{"enum": "http://www.w3.org/2001/XMLSchema"}', actual)

    def test_encode_decimal(self):
        actual = json.dumps({"decimal": Decimal(10.5)}, cls=JsonEncoder)
        self.assertEqual('{"decimal": "10.5"}', actual)
