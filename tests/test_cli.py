import logging
from unittest import mock
from unittest import TestCase

from click.testing import CliRunner

from tests import fixtures_dir
from xsdata.cli import cli
from xsdata.cli import resolve_source
from xsdata.codegen.transformer import SchemaTransformer
from xsdata.exceptions import CodeGenerationError
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import OutputFormat
from xsdata.models.config import OutputStructure


class CliTests(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        super().setUp()

    @mock.patch.object(SchemaTransformer, "process_schemas")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_default_output(self, mock_init, mock_process_schemas):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo"])
        config = mock_init.call_args[1]["config"]

        self.assertIsNone(result.exception)
        self.assertFalse(mock_init.call_args[1]["print"])
        self.assertEqual("foo", config.output.package)
        self.assertEqual(OutputFormat.DATACLASS, config.output.format)
        self.assertEqual(OutputStructure.FILENAMES, config.output.structure)
        self.assertEqual([source.as_uri()], mock_process_schemas.call_args[0][0])

    @mock.patch.object(SchemaTransformer, "process_schemas")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_custom_output(self, mock_init, mock_process_schemas):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(
            cli, [str(source), "--package", "foo", "--output", "plantuml"]
        )
        config = mock_init.call_args[1]["config"]

        self.assertIsNone(result.exception)
        self.assertEqual([source.as_uri()], mock_process_schemas.call_args[0][0])
        self.assertFalse(mock_init.call_args[1]["print"])
        self.assertEqual("foo", config.output.package)
        self.assertEqual(OutputFormat.PLANTUML, config.output.format)
        self.assertEqual(OutputStructure.FILENAMES, config.output.structure)

    @mock.patch.object(SchemaTransformer, "process_schemas")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_print_mode(self, mock_init, mock_process_schemas):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo", "--print"])

        self.assertIsNone(result.exception)
        self.assertEqual([source.as_uri()], mock_process_schemas.call_args[0][0])
        self.assertEqual(logging.ERROR, logger.getEffectiveLevel())
        self.assertTrue(mock_init.call_args[1]["print"])

    @mock.patch.object(SchemaTransformer, "process_schemas")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_ns_struct_mode(self, mock_init, mock_process_schemas):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(
            cli, [str(source), "--package", "foo", "--ns-struct"]
        )
        config = mock_init.call_args[1]["config"]

        self.assertIsNone(result.exception)
        self.assertEqual([source.as_uri()], mock_process_schemas.call_args[0][0])
        self.assertFalse(mock_init.call_args[1]["print"])
        self.assertEqual("foo", config.output.package)
        self.assertEqual(OutputFormat.DATACLASS, config.output.format)
        self.assertEqual(OutputStructure.NAMESPACES, config.output.structure)

    @mock.patch.object(SchemaTransformer, "process_definitions")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_wsdl_mode(self, mock_init, mock_process_definitions):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo", "--wsdl"])

        self.assertIsNone(result.exception)
        mock_process_definitions.assert_called_once_with(
            source.as_uri(),
        )

    def test_resolve_source(self):
        file = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        url = "http://www.xsdata/schema.xsd"

        self.assertEqual([file.as_uri()], list(resolve_source(str(file), wsdl=False)))
        self.assertEqual([url], list(resolve_source(url, wsdl=False)))
        self.assertEqual(
            [x.as_uri() for x in fixtures_dir.glob("*.xsd")],
            list(resolve_source(str(fixtures_dir), wsdl=False)),
        )

        with self.assertRaises(CodeGenerationError) as cm:
            list(resolve_source(str(fixtures_dir), wsdl=True))

        self.assertEqual(
            "WSDL mode doesn't support scanning directories.", str(cm.exception)
        )
