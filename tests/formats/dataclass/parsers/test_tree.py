from unittest import TestCase

from tests import fixtures_dir
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.tree import TreeParser


class TreeParserTests(TestCase):
    def test_parser(self):
        parser = TreeParser()
        path = fixtures_dir.joinpath("books/bk001.xml")

        actual = parser.from_path(path)
        expected = AnyElement(
            qname="book",
            text="",
            children=[
                AnyElement(qname="author", text="Hightower, Kim"),
                AnyElement(qname="title", text="The First Book"),
                AnyElement(qname="genre", text="Fiction"),
                AnyElement(qname="price", text="44.95"),
                AnyElement(qname="pub_date", text="2000-10-01"),
                AnyElement(qname="review", text="An amazing story of nothing."),
            ],
            attributes={"id": "bk001"},
        )

        self.assertEqual(expected, actual)
