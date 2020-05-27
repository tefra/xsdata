import logging
import os
from pathlib import Path
from unittest import mock
from unittest import TestCase

from click.testing import CliRunner

from xsdata import cli
from xsdata.codegen.transformer import SchemaTransformer
from xsdata.logger import logger

root = Path(__file__).parent.parent
fixtures = root.joinpath("tests/fixtures/defxmlschema")
os.chdir(root)


class CliTests(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        super().setUp()

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_default_output(self, mock_transformer_init, *args):
        source = fixtures.joinpath("chapter02.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo"])
        self.assertIsNone(result.exception)
        mock_transformer_init.assert_called_once_with(output="pydata", print=False)

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_custom_output(self, mock_transformer_init, *args):
        source = fixtures.joinpath("chapter02.xsd")
        result = self.runner.invoke(
            cli, [str(source), "--package", "foo", "--output", "plantuml"]
        )
        self.assertIsNone(result.exception)
        mock_transformer_init.assert_called_once_with(output="plantuml", print=False)

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_print_mode(self, mock_transformer_init, *args):
        source = fixtures.joinpath("chapter02.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo", "--print"])
        self.assertIsNone(result.exception)
        mock_transformer_init.assert_called_once_with(output="pydata", print=True)
        self.assertEqual(logging.ERROR, logger.getEffectiveLevel())

    @mock.patch.object(SchemaTransformer, "process")
    def test_with_single_source(self, mock_transformer_process):
        source = fixtures.joinpath("chapter01.xsd")
        result = self.runner.invoke(
            cli, [str(source.relative_to(root)), "--package", "foo"]
        )
        self.assertIsNone(result.exception)
        mock_transformer_process.assert_called_once_with([source.as_uri()], "foo")

    @mock.patch.object(SchemaTransformer, "process")
    def test_with_multiple_source(self, mock_transformer_process):
        first_source = fixtures.joinpath("chapter03.xsd")
        second_source = fixtures.joinpath("chapter04.xsd")
        third_source = "http://foo/bar.xsd"

        result = self.runner.invoke(
            cli,
            [
                str(first_source.relative_to(root)),
                str(second_source.relative_to(root)),
                third_source,
                "--package",
                "foo",
            ],
        )
        self.assertIsNone(result.exception)
        mock_transformer_process.assert_called_once_with(
            [first_source.as_uri(), second_source.as_uri(), third_source], "foo"
        )

    @mock.patch.object(SchemaTransformer, "process")
    def test_with_directory(self, mock_transformer_process):

        result = self.runner.invoke(cli, [str(fixtures), "--package", "foo"])
        self.assertIsNone(result.exception)

        schemas = [x.as_uri() for x in fixtures.glob("*.xsd")]
        mock_transformer_process.assert_called_once_with(schemas, "foo")
