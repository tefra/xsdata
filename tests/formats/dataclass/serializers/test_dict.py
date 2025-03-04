from unittest.case import TestCase

from tests.fixtures.books import BookForm, Books
from tests.fixtures.datatypes import Telephone
from tests.fixtures.wrapper import Wrapper
from xsdata.formats.dataclass.models.generics import AnyElement, DerivedElement
from xsdata.formats.dataclass.serializers import DictEncoder, DictFactory
from xsdata.models.datatype import XmlDate
from xsdata.models.xsd import Attribute
from xsdata.utils.testing import XmlVarFactory


class DictEncoderTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.encoder = DictEncoder(dict_factory=DictFactory.FILTER_NONE)
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

    def test_encode(self) -> None:
        actual = self.encoder.encode(self.books)
        self.assertEqual(self.expected, actual)

    def test_encode_list_of_objects(self) -> None:
        actual = self.encoder.encode(self.books.book)
        self.assertEqual(self.expected["book"], actual)

    def test_encode_with_enum(self) -> None:
        obj = Attribute()
        actual = self.encoder.encode(obj)

        self.assertEqual("optional", actual["use"])

    def test_convert_namedtuple(self) -> None:
        var = XmlVarFactory.create(types=(Telephone,))
        actual = self.encoder.encode(Telephone(30, 234, 56783), var)
        self.assertEqual("30-234-56783", actual)

    def test_convert_wrapper(self) -> None:
        obj = Wrapper(alpha=["value"])
        value = self.encoder.encode(obj)
        expected = {
            "alphas": {"alpha": ["value"]},
            "bravos": {"bravo": []},
            "charlies": {"charlie": []},
        }

        self.assertEqual(expected, value)

    def test_next_value(self) -> None:
        book = self.books.book[0]

        actual = [name for name, value in self.encoder.next_value(book)]
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

        self.encoder.config.ignore_default_attributes = True
        expected = expected[:-1]
        actual = [name for name, value in self.encoder.next_value(book)]
        self.assertEqual(expected, actual)

    def test_generics(self) -> None:
        self.obj = AnyElement(
            children=[
                AnyElement(qname="foo", text="bar"),
                DerivedElement(qname="bar", value="1"),
                DerivedElement(qname="bar", value=2),
            ]
        )
        result = self.encoder.encode(self.obj)
        expected = {
            "attributes": {},
            "children": [
                {"attributes": {}, "children": [], "qname": "foo", "text": "bar"},
                {"qname": "bar", "value": "1"},
                {"qname": "bar", "value": 2},
            ],
        }

        self.assertEqual(expected, result)
