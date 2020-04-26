import logging
import os
from pathlib import Path
from unittest import mock
from unittest import TestCase

from click.testing import CliRunner

from xsdata import cli
from xsdata.logger import logger
from xsdata.transformer import SchemaTransformer

root = Path(__file__).parent.parent
fixtures = root.joinpath("tests/fixtures/defxmlschema")
os.chdir(root)


class CliTests(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        super(CliTests, self).setUp()

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_default_output(self, mock_transformer_init, *args):
        source = fixtures.joinpath("chapter02/example0202.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo"])
        self.assertIsNone(result.exception)
        mock_transformer_init.assert_called_once_with(output="pydata", print=False)

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_custom_output(self, mock_transformer_init, *args):
        source = fixtures.joinpath("chapter02/example0202.xsd")
        result = self.runner.invoke(
            cli, [str(source), "--package", "foo", "--output", "plantuml"]
        )
        self.assertIsNone(result.exception)
        mock_transformer_init.assert_called_once_with(output="plantuml", print=False)

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_print_mode(self, mock_transformer_init, *args):
        source = fixtures.joinpath("chapter02/example0202.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo", "--print"])
        self.assertIsNone(result.exception)
        mock_transformer_init.assert_called_once_with(output="pydata", print=True)
        self.assertEqual(logging.ERROR, logger.getEffectiveLevel())

    @mock.patch.object(SchemaTransformer, "process")
    def test_with_single_definition(self, mock_transformer_process):
        source = fixtures.joinpath("chapter02/example0202.xsd")
        result = self.runner.invoke(
            cli, [str(source.relative_to(root)), "--package", "foo"]
        )
        self.assertIsNone(result.exception)
        mock_transformer_process.assert_called_once_with([source], "foo")

    @mock.patch.object(SchemaTransformer, "process")
    def test_with_multiple_definitions(self, mock_transformer_process):
        first_source = fixtures.joinpath("chapter02/example0202.xsd")
        second_source = fixtures.joinpath("chapter02/example0206.xsd")

        result = self.runner.invoke(
            cli,
            [
                str(first_source.relative_to(root)),
                str(second_source.relative_to(root)),
                "--package",
                "foo",
            ],
        )
        self.assertIsNone(result.exception)
        mock_transformer_process.assert_called_once_with(
            [first_source, second_source], "foo"
        )

    @mock.patch.object(SchemaTransformer, "process")
    def test_with_directory(self, mock_transformer_process):
        first_source = fixtures.joinpath("chapter01")
        second_source = fixtures.joinpath("chapter02/example0206.xsd")

        result = self.runner.invoke(
            cli, [str(first_source), str(second_source), "--package", "foo"]
        )
        self.assertIsNone(result.exception)

        schemas = list(first_source.glob("*.xsd"))
        schemas.append(second_source)

        mock_transformer_process.assert_called_once_with(schemas, "foo")
