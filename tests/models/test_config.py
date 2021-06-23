import tempfile
from pathlib import Path
from unittest import TestCase

from xsdata import __version__
from xsdata.exceptions import ParserError
from xsdata.models.config import GeneratorConfig


class GeneratorConfigTests(TestCase):
    def setUp(self) -> None:
        self.maxDiff = None

    def test_create(self):
        file_path = Path(tempfile.mktemp())
        obj = GeneratorConfig.create()
        with file_path.open("w") as fp:
            obj.write(fp, obj)

        expected = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<Config xmlns="http://pypi.org/project/xsdata" version="{__version__}">\n'
            '  <Output maxLineLength="79">\n'
            "    <Package>generated</Package>\n"
            '    <Format frozen="false">dataclasses</Format>\n'
            "    <Structure>filenames</Structure>\n"
            "    <DocstringStyle>reStructuredText</DocstringStyle>\n"
            "    <RelativeImports>false</RelativeImports>\n"
            "    <CompoundFields>false</CompoundFields>\n"
            "  </Output>\n"
            "  <Conventions>\n"
            '    <ClassName case="pascalCase" safePrefix="type"/>\n'
            '    <FieldName case="snakeCase" safePrefix="value"/>\n'
            '    <ConstantName case="screamingSnakeCase" safePrefix="value"/>\n'
            '    <ModuleName case="snakeCase" safePrefix="mod"/>\n'
            '    <PackageName case="snakeCase" safePrefix="pkg"/>\n'
            "  </Conventions>\n"
            "  <Aliases>\n"
            '    <ClassName source="fooType" target="Foo"/>\n'
            '    <ClassName source="ABCSomething" target="ABCSomething"/>\n'
            '    <FieldName source="ChangeofGauge" target="change_of_gauge"/>\n'
            '    <PackageName source="http://www.w3.org/1999/xhtml" target="xtml"/>\n'
            '    <ModuleName source="2010.1" target="2020a"/>\n'
            "  </Aliases>\n"
            "</Config>\n"
        )
        self.assertEqual(expected, file_path.read_text())
        file_path.unlink()

    def test_read(self):
        existing = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<Config xmlns="http://pypi.org/project/xsdata" version="20.8">\n'
            '  <Output maxLineLength="79">\n'
            "    <Package>foo.bar</Package>\n"
            "  </Output>\n"
            "  <Conventions>\n"
            '    <ClassName case="pascalCase" safePrefix="type"/>\n'
            "  </Conventions>\n"
            "  <Aliases/>\n"
            "</Config>\n"
        )
        file_path = Path(tempfile.mktemp())
        file_path.write_text(existing, encoding="utf-8")
        config = GeneratorConfig.read(file_path)
        with file_path.open("w") as fp:
            GeneratorConfig.write(fp, config)

        expected = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<Config xmlns="http://pypi.org/project/xsdata" version="{__version__}">\n'
            '  <Output maxLineLength="79">\n'
            "    <Package>foo.bar</Package>\n"
            '    <Format frozen="false">dataclasses</Format>\n'
            "    <Structure>filenames</Structure>\n"
            "    <DocstringStyle>reStructuredText</DocstringStyle>\n"
            "    <RelativeImports>false</RelativeImports>\n"
            "    <CompoundFields>false</CompoundFields>\n"
            "  </Output>\n"
            "  <Conventions>\n"
            '    <ClassName case="pascalCase" safePrefix="type"/>\n'
            '    <FieldName case="snakeCase" safePrefix="value"/>\n'
            '    <ConstantName case="screamingSnakeCase" safePrefix="value"/>\n'
            '    <ModuleName case="snakeCase" safePrefix="mod"/>\n'
            '    <PackageName case="snakeCase" safePrefix="pkg"/>\n'
            "  </Conventions>\n"
            "  <Aliases/>\n"
            "</Config>\n"
        )
        self.assertEqual(expected, file_path.read_text())

    def test_read_with_wrong_value(self):
        existing = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<Config xmlns="http://pypi.org/project/xsdata" version="21.7">\n'
            '  <Output maxLineLength="79">\n'
            "    <Structure>unknown</Structure>\n"
            "  </Output>\n"
            "</Config>\n"
        )
        file_path = Path(tempfile.mktemp())
        file_path.write_text(existing, encoding="utf-8")
        with self.assertRaises(ParserError):
            GeneratorConfig.read(file_path)
