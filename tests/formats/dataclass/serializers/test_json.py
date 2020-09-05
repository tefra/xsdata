import json
from decimal import Decimal
from unittest.case import TestCase
from xml.etree.ElementTree import QName

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.formats.dataclass.serializers import DictFactory
from xsdata.formats.dataclass.serializers.json import asdict
from xsdata.formats.dataclass.serializers.json import JsonEncoder
from xsdata.formats.dataclass.serializers.json import JsonSerializer
from xsdata.models.enums import FormType


class JsonEncoderTests(TestCase):
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

    def test_encode_qname(self):
        actual = json.dumps({"qname": QName("a", "b")}, cls=JsonEncoder)
        self.assertEqual('{"qname": "{a}b"}', actual)

    def test_encode_enum(self):
        actual = json.dumps({"enum": FormType.QUALIFIED}, cls=JsonEncoder)
        self.assertEqual('{"enum": "qualified"}', actual)

    def test_encode_decimal(self):
        actual = json.dumps({"decimal": Decimal(10.5)}, cls=JsonEncoder)
        self.assertEqual('{"decimal": "10.5"}', actual)

    def test_default_raises_exceptions(self):
        with self.assertRaises(TypeError):
            json.dumps({"string": object()}, cls=JsonEncoder)

    def test_asdict_qname_clone(self):
        self.assertEqual("{a}b", asdict(QName("a", "b")))
