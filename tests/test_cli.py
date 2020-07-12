import logging
import os
from pathlib import Path
from unittest import mock
from unittest import TestCase

from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from tests.conftest import load_class
from xsdata import cli
from xsdata.cli import resolve_source
from xsdata.codegen.transformer import SchemaTransformer
from xsdata.exceptions import CodeGenerationError
from xsdata.logger import logger

os.chdir(root)


class CliTests(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        super().setUp()

    def test_schema_integration(self):
        schema = fixtures_dir.joinpath("books/schema.xsd")
        package = "tests.fixtures.books"
        runner = CliRunner()
        result = runner.invoke(cli, [str(schema), "--package", package, "--ns-struct"])

        if result.exception:
            raise result.exception

        clazz = load_class(result.output, "Books")
        self.assertEqual("books", clazz.Meta.name)
        self.assertEqual("urn:books", clazz.Meta.namespace)

    def test_definitions_integration(self):
        schema = fixtures_dir.joinpath("calculator/services.wsdl")
        package = "tests.fixtures.calculator"
        runner = CliRunner()
        result = runner.invoke(cli, [str(schema), "--package", package, "--wsdl"])

        if result.exception:
            raise result.exception

        clazz = load_class(result.output, "CalculatorSoapMultiplyOutput")
        self.assertEqual("Envelope", clazz.Meta.name)

    @mock.patch.object(SchemaTransformer, "process_schemas")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_default_output(self, mock_init, mock_process_schemas):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo"])
        self.assertIsNone(result.exception)
        mock_init.assert_called_once_with(output="pydata", print=False, ns_struct=False)

        self.assertEqual([source.as_uri()], mock_process_schemas.call_args[0][0])
        self.assertEqual("foo", mock_process_schemas.call_args[0][1])

    @mock.patch.object(SchemaTransformer, "process_schemas")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_custom_output(self, mock_init, mock_process_schemas):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(
            cli, [str(source), "--package", "foo", "--output", "plantuml"]
        )
        self.assertIsNone(result.exception)
        self.assertEqual([source.as_uri()], mock_process_schemas.call_args[0][0])
        self.assertEqual("foo", mock_process_schemas.call_args[0][1])

        mock_init.assert_called_once_with(
            output="plantuml", print=False, ns_struct=False
        )

    @mock.patch.object(SchemaTransformer, "process_schemas")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_print_mode(self, mock_init, mock_process_schemas):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo", "--print"])

        self.assertIsNone(result.exception)
        self.assertEqual([source.as_uri()], mock_process_schemas.call_args[0][0])
        self.assertEqual("foo", mock_process_schemas.call_args[0][1])
        self.assertEqual(logging.ERROR, logger.getEffectiveLevel())

        mock_init.assert_called_once_with(output="pydata", print=True, ns_struct=False)

    @mock.patch.object(SchemaTransformer, "process_schemas")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_ns_struct_mode(self, mock_init, mock_process_schemas):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(
            cli, [str(source), "--package", "foo", "--ns-struct"]
        )

        self.assertIsNone(result.exception)
        self.assertEqual([source.as_uri()], mock_process_schemas.call_args[0][0])
        self.assertEqual("foo", mock_process_schemas.call_args[0][1])

        mock_init.assert_called_once_with(output="pydata", print=False, ns_struct=True)

    @mock.patch.object(SchemaTransformer, "process_definitions")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_wsdl_mode(self, mock_init, mock_process_definitions):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo", "--wsdl"])

        self.assertIsNone(result.exception)
        self.assertEqual(source.as_uri(), mock_process_definitions.call_args[0][0])
        self.assertEqual("foo", mock_process_definitions.call_args[0][1])

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
