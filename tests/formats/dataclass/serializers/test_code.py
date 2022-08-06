from unittest import TestCase

from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.serializers import PycodeSerializer
from xsdata.models.enums import Namespace


class PycodeSerializerTests(TestCase):
    def setUp(self) -> None:
        self.serializer = PycodeSerializer()

    def test_render(self):
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
            '            author="Hightower, Kim",\n'
            '            title="The First Book",\n'
            '            genre="Fiction",\n'
            "            price=44.95,\n"
            "            pub_date=XmlDate(2000, 10, 1),\n"
            '            review="An amazing story of nothing.",\n'
            '            id="bk001",\n'
            '            lang="en"\n'
            "        ),\n"
            "        BookForm(\n"
            '            author="Nagata, Suanne",\n'
            '            title="Becoming Somebody",\n'
            '            genre="Biography",\n'
            "            price=33.95,\n"
            "            pub_date=XmlDate(2001, 1, 10),\n"
            '            review="A masterpiece of the fine art of gossiping.",\n'
            '            id="bk002",\n'
            '            lang="en"\n'
            "        ),\n"
            "    ]\n"
            ")\n"
        )

        self.assertEqual(expected, result)

    def test_write_object_with_empty_array(self):
        iterator = self.serializer.write_object([], 0, set())
        self.assertEqual("[]", "".join(iterator))

        iterator = self.serializer.write_object((), 0, set())
        self.assertEqual("()", "".join(iterator))

        iterator = self.serializer.write_object(set(), 0, set())
        self.assertEqual("set()", "".join(iterator))

    def test_write_object_with_mapping(self):
        iterator = self.serializer.write_object({}, 0, set())
        self.assertEqual("{}", "".join(iterator))

        iterator = self.serializer.write_object({"foo": "bar"}, 0, set())
        self.assertEqual('{\n    "foo": "bar",\n}', "".join(iterator))

    def test_write_object_with_enum(self):
        iterator = self.serializer.write_object(Namespace.SOAP11, 0, set())
        self.assertEqual("Namespace.SOAP11", "".join(iterator))
