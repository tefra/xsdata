from unittest import TestCase

from xsdata.formats.dataclass.parsers.nodes import SkipNode


class SKipNodeTests(TestCase):
    def test_child(self):
        node = SkipNode()
        actual = node.child("foo", {}, {}, 1)

        self.assertIs(node, actual)

    def test_bind(self):
        node = SkipNode()
        self.assertEqual(False, node.bind("foo", None, None, []))
