import json
import warnings
from unittest.case import TestCase
from unittest.mock import ANY
from unittest.mock import call
from unittest.mock import Mock

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

    def test_indent_deprecation(self):
        dump_factory = Mock(json.dump)

        with warnings.catch_warnings(record=True) as w:
            serializer = JsonSerializer(dump_factory=dump_factory)
            serializer.render(self.books)

            serializer.config.pretty_print = True
            serializer.render(self.books)

            serializer.indent = 4
            serializer.render(self.books)

        dump_factory.assert_has_calls(
            [
                call(ANY, ANY, indent=None),
                call(ANY, ANY, indent=2),
                call(ANY, ANY, indent=4),
            ]
        )

        self.assertEqual(
            "JsonSerializer indent property is deprecated, use SerializerConfig",
            str(w[-1].message),
        )

    def test_next_value(self):
        book = self.books.book[0]
        serializer = JsonSerializer()

        actual = [name for name, value in serializer.next_value(book)]
        expected = [
            "author",
            "title",
            "genre",
            "price",
            "pub_date",
            "review",
            "id",
            "lang",
        ]
        self.assertEqual(expected, actual)

        serializer.config.ignore_default_attributes = True
        expected = expected[:-1]
        actual = [name for name, value in serializer.next_value(book)]
        self.assertEqual(expected, actual)

    def test_pretty_print_indent(self):
        serializer = JsonSerializer()
        serializer.config.pretty_print = True
        serializer.config.pretty_print_indent = "    "

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
            "price": null,
            "pub_date": null,
            "review": "{self.expected["book"][1]["review"]}",
            "id": "{self.expected["book"][1]["id"]}",
            "lang": "en"
        }}
    ]
}}"""

        self.assertEqual(expected, actual)
