from unittest import TestCase

from xsdata.formats.dataclass.filters import format_arguments


class AttributeMetadataTests(TestCase):
    def test_format_arguments(self):
        data = dict(
            num=1, text="foo", text_two="fo'o", text_three='fo"o', pattern="foo"
        )

        expected = '''num=1,
text="foo",
text_two="fo'o",
text_three="fo'o",
pattern=r"foo"'''
        self.assertEqual(expected, format_arguments(data))
