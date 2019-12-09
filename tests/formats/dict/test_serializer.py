from unittest import TestCase

from tests.fixtures.books import BookForm, Books
from xsdata.formats.dict.serializer import DictSerializer


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
        actual = DictSerializer().render(
            self.books, dict_factory=DictSerializer.filter_none
        )
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
