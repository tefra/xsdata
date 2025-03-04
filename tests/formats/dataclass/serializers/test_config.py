import unittest
import warnings

from xsdata.formats.dataclass.serializers.config import SerializerConfig


class SerializerConfigTest(unittest.TestCase):
    def test_deprecated_fields(self) -> None:
        with warnings.catch_warnings(record=True) as w:
            config = SerializerConfig(pretty_print=True)
            self.assertEqual("  ", config.indent)

            config = SerializerConfig(pretty_print_indent="\t")
            self.assertEqual("\t", config.indent)

        expected = [
            "Setting `pretty_print` is deprecated, use `indent` instead",
            "Setting `pretty_print_indent` is deprecated, use `indent` instead",
        ]
        self.assertEqual(expected, [str(m.message) for m in w])

        with warnings.catch_warnings(record=True) as w:
            config = SerializerConfig()
            config.pretty_print = True
            self.assertTrue("  ", config.indent)

            config.pretty_print_indent = "\t"
            self.assertTrue("\t", config.indent)

        expected = [
            "Setting `pretty_print` is deprecated, use `indent` instead",
            "Setting `pretty_print_indent` is deprecated, use `indent` instead",
        ]
        self.assertEqual(expected, [str(m.message) for m in w])
