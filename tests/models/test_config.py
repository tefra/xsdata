import sys
import tempfile
import warnings
from pathlib import Path
from unittest import TestCase

from xsdata import __version__
from xsdata.codegen.exceptions import CodegenError
from xsdata.exceptions import ParserError
from xsdata.models.config import (
    ExtensionType,
    GeneratorConfig,
    GeneratorExtension,
    GeneratorOutput,
    OutputFormat,
)


class GeneratorConfigTests(TestCase):
    def setUp(self) -> None:
        self.maxDiff = None

    def test_create(self) -> None:
        file_path = Path(tempfile.mktemp())
        obj = GeneratorConfig.create()
        with file_path.open("w") as fp:
            obj.write(fp, obj)

        expected = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<Config xmlns="http://pypi.org/project/xsdata" version="{__version__}">\n'
            '  <Output maxLineLength="79" genericCollections="false" unionType="false">\n'
            "    <Package>generated</Package>\n"
            '    <Format repr="true" eq="true" order="false" unsafeHash="false" frozen="false" slots="false" kwOnly="false">dataclasses</Format>\n'
            "    <Structure>filenames</Structure>\n"
            "    <DocstringStyle>reStructuredText</DocstringStyle>\n"
            "    <RelativeImports>false</RelativeImports>\n"
            '    <CompoundFields defaultName="choice" useSubstitutionGroups="false" forceDefaultName="false" maxNameParts="3">false</CompoundFields>\n'
            "    <WrapperFields>false</WrapperFields>\n"
            "    <PostponedAnnotations>false</PostponedAnnotations>\n"
            "    <UnnestClasses>false</UnnestClasses>\n"
            "    <IgnorePatterns>false</IgnorePatterns>\n"
            "    <IncludeHeader>false</IncludeHeader>\n"
            "  </Output>\n"
            "  <Conventions>\n"
            '    <ClassName case="pascalCase" safePrefix="type"/>\n'
            '    <FieldName case="snakeCase" safePrefix="value"/>\n'
            '    <ConstantName case="screamingSnakeCase" safePrefix="value"/>\n'
            '    <ModuleName case="snakeCase" safePrefix="mod"/>\n'
            '    <PackageName case="snakeCase" safePrefix="pkg"/>\n'
            "  </Conventions>\n"
            "  <Substitutions>\n"
            '    <Substitution type="package" search="http://www.w3.org/2001/XMLSchema" replace="xs"/>\n'
            '    <Substitution type="package" search="http://www.w3.org/XML/1998/namespace" replace="xml"/>\n'
            '    <Substitution type="package" search="http://www.w3.org/2001/XMLSchema-instance" replace="xsi"/>\n'
            '    <Substitution type="package" search="http://www.w3.org/1998/Math/MathML" replace="mathml3"/>\n'
            '    <Substitution type="package" search="http://www.w3.org/1999/xlink" replace="xlink"/>\n'
            '    <Substitution type="package" search="http://www.w3.org/1999/xhtml" replace="xhtml"/>\n'
            '    <Substitution type="package" search="http://schemas.xmlsoap.org/wsdl/soap/" replace="soap"/>\n'
            '    <Substitution type="package" search="http://schemas.xmlsoap.org/wsdl/soap12/" replace="soap12"/>\n'
            '    <Substitution type="package" search="http://schemas.xmlsoap.org/soap/envelope/" replace="soapenv"/>\n'
            '    <Substitution type="package" search="http://schemas.xmlsoap.org/soap/encoding/" replace="soapenc"/>\n'
            '    <Substitution type="class" search="(.*)Class$" replace="\\1Type"/>\n'
            "  </Substitutions>\n"
            "  <Extensions/>\n"
            "</Config>\n"
        )
        self.assertEqual(expected, file_path.read_text())
        file_path.unlink()

    def test_read(self) -> None:
        existing = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<Config xmlns="http://pypi.org/project/xsdata" version="20.8">\n'
            '  <Output maxLineLength="79" unionType="false">\n'
            "    <Package>foo.bar</Package>\n"
            "  </Output>\n"
            "  <Conventions>\n"
            '    <ClassName case="pascalCase" safePrefix="type"/>\n'
            "  </Conventions>\n"
            "  <Substitutions/>\n"
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
            '  <Output maxLineLength="79" genericCollections="false" unionType="false">\n'
            "    <Package>foo.bar</Package>\n"
            '    <Format repr="true" eq="true" order="false" unsafeHash="false"'
            ' frozen="false" slots="false" kwOnly="false">dataclasses</Format>\n'
            "    <Structure>filenames</Structure>\n"
            "    <DocstringStyle>reStructuredText</DocstringStyle>\n"
            "    <RelativeImports>false</RelativeImports>\n"
            '    <CompoundFields defaultName="choice" useSubstitutionGroups="false" forceDefaultName="false" maxNameParts="3">false</CompoundFields>\n'
            "    <WrapperFields>false</WrapperFields>\n"
            "    <PostponedAnnotations>false</PostponedAnnotations>\n"
            "    <UnnestClasses>false</UnnestClasses>\n"
            "    <IgnorePatterns>false</IgnorePatterns>\n"
            "    <IncludeHeader>false</IncludeHeader>\n"
            "  </Output>\n"
            "  <Conventions>\n"
            '    <ClassName case="pascalCase" safePrefix="type"/>\n'
            '    <FieldName case="snakeCase" safePrefix="value"/>\n'
            '    <ConstantName case="screamingSnakeCase" safePrefix="value"/>\n'
            '    <ModuleName case="snakeCase" safePrefix="mod"/>\n'
            '    <PackageName case="snakeCase" safePrefix="pkg"/>\n'
            "  </Conventions>\n"
            "  <Substitutions/>\n"
            "  <Extensions/>\n"
            "</Config>\n"
        )
        self.assertEqual(expected, file_path.read_text())

    def test_read_with_wrong_value(self) -> None:
        existing = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<Config xmlns="http://pypi.org/project/xsdata" version="21.7">\n'
            '  <Output maxLineLength="79">\n'
            "    <Structure>unknown</Structure>\n"
            "  </Output>\n"
            "</Config>\n"
        )
        file_path = Path(tempfile.mktemp())
        file_path.write_text(existing, encoding="utf-8")
        with self.assertRaises(ParserError):
            GeneratorConfig.read(file_path)

    def test_format_with_invalid_eq_config(self) -> None:
        with warnings.catch_warnings(record=True) as w:
            OutputFormat(eq=False, order=True)

        self.assertEqual("Enabling eq because order is true", str(w[-1].message))

    def test_use_union_type_requires_310_and_postponed_annotations(self) -> None:
        if sys.version_info < (3, 10):
            with warnings.catch_warnings(record=True) as w:
                self.assertFalse(GeneratorOutput(union_type=True).union_type)

            self.assertEqual(
                "UnionType PEP 604 requires python >= 3.10, reverting...",
                str(w[-1].message),
            )
        else:
            with warnings.catch_warnings(record=True) as w:
                output = GeneratorOutput(union_type=True)
                self.assertTrue(output.postponed_annotations)

                self.assertEqual(
                    "Enabling postponed annotations, because `union_type==True`",
                    str(w[-1].message),
                )

    def test_generic_collections_requires_frozen_false(self) -> None:
        with warnings.catch_warnings(record=True) as w:
            output = GeneratorOutput(
                generic_collections=True, format=OutputFormat(frozen=True)
            )
            self.assertFalse(output.generic_collections)

            self.assertEqual(
                "Generic Collections, requires frozen=False, reverting...",
                str(w[-1].message),
            )

    def test_format_slots_requires_310(self) -> None:
        if sys.version_info < (3, 10):
            self.assertTrue(OutputFormat(slots=True, value="attrs").slots)

            with warnings.catch_warnings(record=True) as w:
                self.assertFalse(OutputFormat(slots=True).slots)

            self.assertEqual(
                "slots requires python >= 3.10, reverting...", str(w[-1].message)
            )

        else:
            self.assertIsNotNone(OutputFormat(slots=True))

    def test_format_kw_only_requires_310(self) -> None:
        if sys.version_info < (3, 10):
            self.assertTrue(OutputFormat(kw_only=True, value="attrs").kw_only)

            with warnings.catch_warnings(record=True) as w:
                self.assertFalse(OutputFormat(kw_only=True).kw_only)

            self.assertEqual(
                "kw_only requires python >= 3.10, reverting...", str(w[-1].message)
            )

        else:
            self.assertIsNotNone(OutputFormat(kw_only=True))

    def test_extension_with_invalid_import_string(self) -> None:
        cases = [None, "", "bar"]
        for case in cases:
            with self.assertRaises(CodegenError):
                GeneratorExtension(type=ExtensionType.DECORATOR, import_string=case)

    def test_extension_with_invalid_class_name_pattern(self) -> None:
        with self.assertRaises(CodegenError):
            GeneratorExtension(
                type=ExtensionType.DECORATOR, import_string="a.b", class_name="*Foo"
            )
