from pathlib import Path
from unittest import TestCase

from xsdata.models.elements import Import, Schema
from xsdata.writer import CodeWriter


class CodeWriterTests(TestCase):
    def test_adjust_target_without_imports(self):
        target = Path("/project/target/")
        xsd_path = Path("/somewhere/name/version/subfolder/here.xsd")
        schema = Schema.build()

        actual = CodeWriter.adjust_target(target, xsd_path, schema)
        self.assertEqual(target, actual)

    def test_adjust_target_with_one_import(self):
        target = Path("/project/target/")
        xsd_path = Path("/somewhere/name/version/subfolder/here.xsd")
        schema = Schema.build(
            imports=[Import.build(schema_location="../common/common.xsd")]
        )

        actual = CodeWriter.adjust_target(target, xsd_path, schema)
        expected = target.joinpath("subfolder")
        self.assertEqual(expected, actual)

    def test_adjust_target_with_imports_from_different_levels(self):
        target = Path("/project/target/")
        xsd_path = Path("/somewhere/name/version/subfolder/here.xsd")
        schema = Schema.build(
            imports=[
                Import.build(schema_location="../common/common.xsd"),
                Import.build(schema_location="../../back/common.xsd"),
            ]
        )

        actual = CodeWriter.adjust_target(target, xsd_path, schema)
        expected = target.joinpath("version/subfolder")
        self.assertEqual(expected, actual)
