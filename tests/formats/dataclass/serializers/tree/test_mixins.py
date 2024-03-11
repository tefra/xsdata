from unittest import TestCase, mock
from xml.etree.ElementTree import TreeBuilder

from tests.fixtures.books.fixtures import books
from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.serializers.tree.mixins import TreeSerializer


class TreeSerializerTests(TestCase):
    @mock.patch.object(TreeSerializer, "generate")
    def test_build_with_unknown_event(self, mock_generate):
        mock_generate.return_value = [
            ("foobar", True),
        ]

        builder = TreeBuilder()
        serializer = TreeSerializer()
        with self.assertRaises(XmlHandlerError) as cm:
            serializer.build(books, builder)

        self.assertEqual("Unhandled event: `foobar`.", str(cm.exception))
