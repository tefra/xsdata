import sys
import tempfile
import warnings
from pathlib import Path
from unittest import TestCase

from xsdata import __version__
from xsdata.exceptions import GeneratorConfigError
from xsdata.exceptions import ParserError
from xsdata.models.config import ExtensionType
from xsdata.models.config import GeneratorAlias
from xsdata.models.config import GeneratorAliases
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import GeneratorExtension
from xsdata.models.config import GeneratorOutput
from xsdata.models.config import ObjectType
from xsdata.models.config import OutputFormat


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
            '  <Output maxLineLength="79" subscriptableTypes="false" unionType="false">\n'
            "    <Package>generated</Package>\n"
            '    <Format repr="true" eq="true" order="false" unsafeHash="false" frozen="false" slots="false" kwOnly="false">dataclasses</Format>\n'
            "    <Structure>filenames</Structure>\n"
            "    <DocstringStyle>reStructuredText</DocstringStyle>\n"
            "    <FilterStrategy>allGlobals</FilterStrategy>\n"
            "    <RelativeImports>false</RelativeImports>\n"
            '    <CompoundFields defaultName="choice" forceDefaultName="false">false</CompoundFields>\n'
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
            '    <Substitution type="class" search="(.*)Class$" replace="\\1Type"/>\n'
            "  </Substitutions>\n"
            "  <Extensions/>\n"
            "</Config>\n"
        )
        self.assertEqual(expected, file_path.read_text())
        file_path.unlink()

    def test_read(self):
        existing = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<Config xmlns="http://pypi.org/project/xsdata" version="20.8">\n'
            '  <Output maxLineLength="79" subscriptableTypes="false" unionType="false">\n'
            "    <Package>foo.bar</Package>\n"
            "  </Output>\n"
            "  <Conventions>\n"
            '    <ClassName case="pascalCase" safePrefix="type"/>\n'
            "  </Conventions>\n"
            "  <Aliases/>\n"
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
            '  <Output maxLineLength="79" subscriptableTypes="false" unionType="false">\n'
            "    <Package>foo.bar</Package>\n"
            '    <Format repr="true" eq="true" order="false" unsafeHash="false"'
            ' frozen="false" slots="false" kwOnly="false">dataclasses</Format>\n'
            "    <Structure>filenames</Structure>\n"
            "    <DocstringStyle>reStructuredText</DocstringStyle>\n"
            "    <FilterStrategy>allGlobals</FilterStrategy>\n"
            "    <RelativeImports>false</RelativeImports>\n"
            '    <CompoundFields defaultName="choice" forceDefaultName="false">false</CompoundFields>\n'
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
            "  <Aliases/>\n"
            "  <Substitutions/>\n"
            "  <Extensions/>\n"
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

    def test_format_with_invalid_state(self):
        with self.assertRaises(GeneratorConfigError) as cm:
            OutputFormat(eq=False, order=True)

        self.assertEqual("eq must be true if order is true", str(cm.exception))

    def test_subscriptable_types_requires_390(self):
        if sys.version_info < (3, 9):
            with warnings.catch_warnings(record=True) as w:
                self.assertFalse(
                    GeneratorOutput(subscriptable_types=True).subscriptable_types
                )

            self.assertEqual(
                "Generics PEP 585 requires python >= 3.9, reverting...",
                str(w[-1].message),
            )

        else:
            self.assertTrue(
                GeneratorOutput(subscriptable_types=True).subscriptable_types
            )

    def test_use_union_type_requires_310(self):
        if sys.version_info < (3, 10):
            with warnings.catch_warnings(record=True) as w:
                self.assertFalse(GeneratorOutput(union_type=True).union_type)

            self.assertEqual(
                "UnionType PEP 604 requires python >= 3.10, reverting...",
                str(w[-1].message),
            )

        else:
            self.assertTrue(GeneratorOutput(union_type=True).union_type)

    def test_format_slots_requires_310(self):
        if sys.version_info < (3, 10):
            self.assertTrue(OutputFormat(slots=True, value="attrs").slots)

            with warnings.catch_warnings(record=True) as w:
                self.assertFalse(OutputFormat(slots=True).slots)

            self.assertEqual(
                "slots requires python >= 3.10, reverting...", str(w[-1].message)
            )

        else:
            self.assertIsNotNone(OutputFormat(slots=True))

    def test_format_kw_only_requires_310(self):
        if sys.version_info < (3, 10):
            self.assertTrue(OutputFormat(kw_only=True, value="attrs").kw_only)

            with warnings.catch_warnings(record=True) as w:
                self.assertFalse(OutputFormat(kw_only=True).kw_only)

            self.assertEqual(
                "kw_only requires python >= 3.10, reverting...", str(w[-1].message)
            )

        else:
            self.assertIsNotNone(OutputFormat(kw_only=True))

    def test_postponed_annotations_requires_37(self):
        # We need to confuse pyupgrade into not discarding Python version checks,
        # which are needed to know when the warning is triggered or not
        # Extracting the version in a local variable before performing the check is
        # sufficient for that purpose.
        v = sys.version_info
        if v < (3, 7):
            with warnings.catch_warnings(record=True) as w:
                self.assertFalse(
                    GeneratorOutput(postponed_annotations=True).postponed_annotations
                )
                self.assertEqual(
                    "postponed annotations requires python >= 3.7, reverting...",
                    str(w[-1].message),
                )

        if v >= (3, 7):
            self.assertTrue(
                GeneratorOutput(postponed_annotations=True).postponed_annotations
            )

    def test_init_config_with_aliases(self):
        config = GeneratorConfig(
            aliases=GeneratorAliases(
                class_name=[GeneratorAlias(source="a", target="b")],
                field_name=[GeneratorAlias(source="c", target="d")],
                package_name=[GeneratorAlias(source="e", target="f")],
                module_name=[GeneratorAlias(source="g", target="h")],
            )
        )

        self.assertEqual(4, len(config.substitutions.substitution))
        self.assertEqual(ObjectType.CLASS, config.substitutions.substitution[0].type)
        self.assertEqual(ObjectType.FIELD, config.substitutions.substitution[1].type)
        self.assertEqual(ObjectType.PACKAGE, config.substitutions.substitution[2].type)
        self.assertEqual(ObjectType.MODULE, config.substitutions.substitution[3].type)

        output = tempfile.mktemp()
        output_path = Path(output)
        config.substitutions = None
        with output_path.open("w") as fp:
            config.write(fp, config)

        config = GeneratorConfig.read(output_path)
        self.assertIsNone(config.aliases)
        self.assertEqual(4, len(config.substitutions.substitution))

    def test_extension_with_invalid_import_string(self):
        cases = [None, "", "bar"]
        for case in cases:
            with self.assertRaises(GeneratorConfigError) as cm:
                GeneratorExtension(type=ExtensionType.DECORATOR, import_string=case)

            self.assertEqual(f"Invalid extension import '{case}'", str(cm.exception))

    def test_extension_with_invalid_class_name_pattern(self):
        with self.assertRaises(GeneratorConfigError) as cm:
            GeneratorExtension(
                type=ExtensionType.DECORATOR, import_string="a.b", class_name="*Foo"
            )

        self.assertEqual(f"Failed to compile pattern '*Foo'", str(cm.exception))
