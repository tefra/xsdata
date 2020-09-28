import tempfile
from pathlib import Path
from unittest import TestCase

from tests import fixtures_dir
from xsdata.utils.testing import read_root_name


class TestingTests(TestCase):
    def test_read_root_name(self):
        schema_path = fixtures_dir.joinpath("books/schema.xsd")
        self.assertEqual("Schema", read_root_name(schema_path))

    def test_read_root_name_return_empty_string_on_exception(self):
        file_path = Path(tempfile.mktemp())
        self.assertEqual("", read_root_name(file_path))
        self.assertFalse(file_path.exists())
