import json
from unittest.case import TestCase

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from tests.fixtures.datatypes import Telephone
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.serializers.json import DictFactory
from xsdata.formats.dataclass.serializers.json import JsonSerializer
from xsdata.models.datatype import XmlDate
from xsdata.models.xsd import Attribute
from xsdata.utils.testing import XmlVarFactory


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
                    "review": "A masterpiece of the fine art of gossiping.",
                    "title": "Becoming Somebody",
                },
            ]
        }

    def test_render(self):
        serializer = JsonSerializer(dict_factory=DictFactory.FILTER_NONE)
        actual = serializer.render(self.books)

        self.assertEqual(self.expected, json.loads(actual))

    def test_render_a_none_dataclass_object(self):
        with self.assertRaises(XmlContextError):
            JsonSerializer().render(1)

    def test_render_list_of_objects(self):
        serializer = JsonSerializer(dict_factory=DictFactory.FILTER_NONE)
        actual = serializer.render(self.books.book)
        self.assertEqual(self.expected["book"], json.loads(actual))

    def test_render_with_enum(self):
        obj = Attribute()
        serializer = JsonSerializer(dict_factory=DictFactory.FILTER_NONE)
        actual = json.loads(serializer.render(obj))

        self.assertEqual("optional", actual["use"])

    def test_convert_namedtuple(self):
        var = XmlVarFactory.create(types=(Telephone,))
        serializer = JsonSerializer(dict_factory=DictFactory.FILTER_NONE)
        actual = serializer.convert(Telephone(30, 234, 56783), var)
        self.assertEqual("30-234-56783", actual)
