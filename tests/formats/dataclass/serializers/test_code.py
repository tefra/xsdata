from unittest import TestCase

from tests.fixtures.books import BookForm, Books
from tests.fixtures.books.fixtures import books
from tests.fixtures.models import Parent
from xsdata.formats.dataclass.serializers import PycodeSerializer
from xsdata.models.datatype import XmlDate
from xsdata.models.enums import Namespace


class PycodeSerializerTests(TestCase):
    def setUp(self) -> None:
        self.serializer = PycodeSerializer()

    def test_render(self) -> None:
        result = self.serializer.render(books, var_name="books")

        expected = (
            "from tests.fixtures.books.books import BookForm\n"
            "from tests.fixtures.books.books import Books\n"
            "from xsdata.models.datatype import XmlDate\n"
            "\n"
            "\n"
            "books = Books(\n"
            "    book=[\n"
            "        BookForm(\n"
            "            author='Hightower, Kim',\n"
            "            title='The First Book',\n"
            "            genre='Fiction',\n"
            "            price=44.95,\n"
            "            pub_date=XmlDate(2000, 10, 1),\n"
            "            review='An amazing story of nothing.',\n"
            "            id='bk001'\n"
            "        ),\n"
            "        BookForm(\n"
            "            author='Nagata, Suanne',\n"
            "            title='Becoming Somebody',\n"
            "            genre='Biography',\n"
            "            price=33.95,\n"
            "            pub_date=XmlDate(2001, 1, 10),\n"
            "            review='A masterpiece of the fine art of gossiping.',\n"
            "            id='bk002'\n"
            "        ),\n"
            "    ]\n"
            ")\n"
        )

        self.assertEqual(expected, result)

    def test_write_class_with_default_values(self) -> None:
        books = Books(
            book=[
                BookForm(
                    author="me",
                    title="My Book",
                    genre="Fiction",
                    price=9.99,
                    pub_date=XmlDate.from_string("2020-01-01"),
                    review="Great!",
                )
            ]
        )
        result = self.serializer.render(books, var_name="books")
        expected = (
            "from tests.fixtures.books.books import BookForm\n"
            "from tests.fixtures.books.books import Books\n"
            "from xsdata.models.datatype import XmlDate\n"
            "\n"
            "\n"
            "books = Books(\n"
            "    book=[\n"
            "        BookForm(\n"
            "            author='me',\n"
            "            title='My Book',\n"
            "            genre='Fiction',\n"
            "            price=9.99,\n"
            "            pub_date=XmlDate(2020, 1, 1),\n"
            "            review='Great!'\n"
            "        ),\n"
            "    ]\n"
            ")\n"
        )
        self.assertEqual(expected, result)

    def test_write_string_with_unicode_characters(self) -> None:
        books = Books(
            book=[
                BookForm(
                    author="Backslashes \\ One Two \x12 Three",
                    title="Test",
                    genre="Test",
                    price=1.0,
                    pub_date=XmlDate.from_string("2020-01-01"),
                    review="Test",
                )
            ]
        )
        result = self.serializer.render(books, var_name="books")
        expected = (
            "from tests.fixtures.books.books import BookForm\n"
            "from tests.fixtures.books.books import Books\n"
            "from xsdata.models.datatype import XmlDate\n"
            "\n"
            "\n"
            "books = Books(\n"
            "    book=[\n"
            "        BookForm(\n"
            "            author='Backslashes \\\\ One Two \\x12 Three',\n"
            "            title='Test',\n"
            "            genre='Test',\n"
            "            price=1.0,\n"
            "            pub_date=XmlDate(2020, 1, 1),\n"
            "            review='Test'\n"
            "        ),\n"
            "    ]\n"
            ")\n"
        )
        self.assertEqual(expected, result)

    def test_write_object_with_empty_array(self) -> None:
        iterator = self.serializer.repr_object([], 0, set())
        self.assertEqual("[]", "".join(iterator))

        iterator = self.serializer.repr_object((), 0, set())
        self.assertEqual("()", "".join(iterator))

        iterator = self.serializer.repr_object(set(), 0, set())
        self.assertEqual("set()", "".join(iterator))

    def test_write_object_with_mapping(self) -> None:
        iterator = self.serializer.repr_object({}, 0, set())
        self.assertEqual("{}", "".join(iterator))

        iterator = self.serializer.repr_object({"foo": "bar"}, 0, set())
        self.assertEqual("{\n    'foo': 'bar',\n}", "".join(iterator))

    def test_write_object_with_enum(self) -> None:
        iterator = self.serializer.repr_object(Namespace.SOAP11, 0, set())
        self.assertEqual("Namespace.SOAP11", "".join(iterator))

    def test_build_imports_with_nested_types(self) -> None:
        expected = "from tests.fixtures.models import Parent\n"
        actual = self.serializer.build_imports({Parent.Inner})
        self.assertEqual(expected, actual)
