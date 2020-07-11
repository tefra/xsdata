import logging
import os
from pathlib import Path
from unittest import mock
from unittest import TestCase

from click.testing import CliRunner

from tests.conftest import load_class
from xsdata import cli
from xsdata.cli import resolve_source
from xsdata.codegen.transformer import SchemaTransformer
from xsdata.logger import logger

root = Path(__file__).parent.parent
fixtures = root.joinpath("tests/fixtures/defxmlschema")
os.chdir(root)


class CliTests(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        super().setUp()

    def test_schema_integration(self):
        schema = Path("tests/fixtures/books/schema.xsd")
        package = "tests.fixtures.books"
        runner = CliRunner()
        result = runner.invoke(cli, [str(schema), "--package", package, "--ns-struct"])

        if result.exception:
            raise result.exception

        clazz = load_class(result.output, "Books")
        self.assertEqual("books", clazz.Meta.name)
        self.assertEqual("urn:books", clazz.Meta.namespace)

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_default_output(self, mock_init, mock_process):
        source = fixtures.joinpath("chapter03.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo"])
        self.assertIsNone(result.exception)
        mock_init.assert_called_once_with(output="pydata", print=False, ns_struct=False)

        self.assertEqual([source.as_uri()], mock_process.call_args[0][0])
        self.assertEqual("foo", mock_process.call_args[0][1])

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_custom_output(self, mock_init, mock_process):
        source = fixtures.joinpath("chapter03.xsd")
        result = self.runner.invoke(
            cli, [str(source), "--package", "foo", "--output", "plantuml"]
        )
        self.assertIsNone(result.exception)
        self.assertEqual([source.as_uri()], mock_process.call_args[0][0])
        self.assertEqual("foo", mock_process.call_args[0][1])

        mock_init.assert_called_once_with(
            output="plantuml", print=False, ns_struct=False
        )

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_print_mode(self, mock_init, mock_process):
        source = fixtures.joinpath("chapter03.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo", "--print"])

        self.assertIsNone(result.exception)
        self.assertEqual([source.as_uri()], mock_process.call_args[0][0])
        self.assertEqual("foo", mock_process.call_args[0][1])
        self.assertEqual(logging.ERROR, logger.getEffectiveLevel())

        mock_init.assert_called_once_with(output="pydata", print=True, ns_struct=False)

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_ns_struct_mode(self, mock_init, mock_process):
        source = fixtures.joinpath("chapter03.xsd")
        result = self.runner.invoke(
            cli, [str(source), "--package", "foo", "--ns-struct"]
        )

        self.assertIsNone(result.exception)
        self.assertEqual([source.as_uri()], mock_process.call_args[0][0])
        self.assertEqual("foo", mock_process.call_args[0][1])

        mock_init.assert_called_once_with(output="pydata", print=False, ns_struct=True)

    def test_resolve_source(self):
        file = fixtures.joinpath("chapter03.xsd")
        url = "http://www.xsdata/schema.xsd"

        self.assertEqual([file.as_uri()], list(resolve_source(str(file))))
        self.assertEqual([url], list(resolve_source(url)))
        self.assertEqual(
            [x.as_uri() for x in fixtures.glob("*.xsd")],
            list(resolve_source(str(fixtures))),
        )
