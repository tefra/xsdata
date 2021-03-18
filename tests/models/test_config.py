import tempfile
import warnings
from pathlib import Path
from unittest import TestCase

from pkg_resources import get_distribution

from xsdata.models.config import GeneratorConfig
from xsdata.models.config import GeneratorOutput


class GeneratorConfigTests(TestCase):
    def setUp(self) -> None:
        self.maxDiff = None

    def test_deprecation_warning(self):
        with warnings.catch_warnings(record=True) as w:
            output = GeneratorOutput(format="pydata")

        self.assertEqual(
            "Output format 'pydata' renamed to 'dataclasses'", str(w[-1].message)
        )
        self.assertEqual("dataclasses", output.format)

    def test_create(self):
        file_path = Path(tempfile.mktemp())
        version = get_distribution("xsdata").version
        obj = GeneratorConfig.create()
        with file_path.open("w") as fp:
            obj.write(fp, obj)

        expected = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<Config xmlns="http://pypi.org/project/xsdata" version="{version}">\n'
            '  <Output maxLineLength="79">\n'
            "    <Package>generated</Package>\n"
            "    <Format>dataclasses</Format>\n"
            "    <Structure>filenames</Structure>\n"
            "    <DocstringStyle>reStructuredText</DocstringStyle>\n"
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
        version = get_distribution("xsdata").version
        file_path = Path(tempfile.mktemp())
        file_path.write_text(existing, encoding="utf-8")
        config = GeneratorConfig.read(file_path)
        with file_path.open("w") as fp:
            GeneratorConfig.write(fp, config)

        expected = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<Config xmlns="http://pypi.org/project/xsdata" version="{version}">\n'
            '  <Output maxLineLength="79">\n'
            "    <Package>foo.bar</Package>\n"
            "    <Format>dataclasses</Format>\n"
            "    <Structure>filenames</Structure>\n"
            "    <DocstringStyle>reStructuredText</DocstringStyle>\n"
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
