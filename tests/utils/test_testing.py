from unittest import TestCase

from tests.fixtures.books import BooksForm
from xsdata.utils.testing import load_class


class TestingTests(TestCase):
    def test_load(self):
        output = "Generating package: tests.fixtures.books.books"
        self.assertEqual(BooksForm, load_class(output, "BooksForm"))

    def test_load_class_raises_exception(self):
        output = "Generating package: generated.foo.bar"

        with self.assertRaises(ModuleNotFoundError):
            load_class(output, "foo")
