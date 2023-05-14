import logging
import platform
import sys
import tempfile
from pathlib import Path
from unittest import mock
from unittest import TestCase

from click.testing import CliRunner

from tests import fixtures_dir
from xsdata import __version__
from xsdata.cli import cli
from xsdata.cli import resolve_source
from xsdata.codegen.transformer import SchemaTransformer
from xsdata.codegen.writer import CodeWriter
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import StructureStyle
from xsdata.utils.downloader import Downloader

CodeWriter.register_generator("testing", DataclassGenerator)


class CliTests(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        super().setUp()

    @classmethod
    def setUpClass(cls):
        CodeWriter.register_generator("testing", DataclassGenerator)

    @classmethod
    def tearDownClass(cls):
        CodeWriter.unregister_generator("testing")

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_generate(self, mock_init, mock_process):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo"])
        config = mock_init.call_args[1]["config"]

        self.assertIsNone(result.exception)
        self.assertFalse(mock_init.call_args[1]["print"])
        self.assertEqual("foo", config.output.package)
        self.assertEqual("dataclasses", config.output.format.value)
        self.assertFalse(config.output.relative_imports)
        self.assertEqual(StructureStyle.FILENAMES, config.output.structure_style)
        self.assertEqual([source.as_uri()], mock_process.call_args[0][0])

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_generate_with_configuration_file(self, mock_init, mock_process):
        file_path = Path(tempfile.mktemp())
        config = GeneratorConfig()
        config.output.package = "foo.bar"
        config.output.structure_style = StructureStyle.NAMESPACES
        with file_path.open("w") as fp:
            config.write(fp, config)

        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(
            cli,
            [str(source), "--config", str(file_path), "--no-eq"],
            catch_exceptions=False,
        )
        config = mock_init.call_args[1]["config"]

        self.assertIsNone(result.exception)
        self.assertFalse(mock_init.call_args[1]["print"])
        self.assertEqual("foo.bar", config.output.package)
        self.assertEqual("dataclasses", config.output.format.value)
        self.assertFalse(config.output.format.eq)
        self.assertEqual(StructureStyle.NAMESPACES, config.output.structure_style)
        self.assertEqual([source.as_uri()], mock_process.call_args[0][0])
        file_path.unlink()

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_generate_with_print_mode(self, mock_init, mock_process):
        source = fixtures_dir.joinpath("defxmlschema/chapter03.xsd")
        result = self.runner.invoke(cli, [str(source), "--package", "foo", "--print"])

        self.assertIsNone(result.exception)
        self.assertEqual([source.as_uri()], mock_process.call_args[0][0])
        self.assertTrue(mock_init.call_args[1]["print"])

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "__init__", return_value=None)
    def test_generate_with_debug_mode(self, *args):
        self.runner.invoke(cli, ["foo.xsd", "--package", "foo", "--debug"])
        self.assertEqual(logging.DEBUG, logger.level)

    @mock.patch("xsdata.cli.logger.info")
    def test_init_config(self, mock_info):
        output = tempfile.mktemp()
        output_path = Path(output)
        result = self.runner.invoke(cli, ["init-config", str(output_path)])

        self.assertIsNone(result.exception)
        self.assertEqual(GeneratorConfig.create(), GeneratorConfig.read(output_path))
        mock_info.assert_has_calls(
            [
                mock.call(
                    "========= xsdata v%s / Python %s / Platform %s =========\n",
                    __version__,
                    platform.python_version(),
                    sys.platform,
                ),
                mock.call("Initializing configuration file %s", str(output_path)),
            ]
        )
        output_path.unlink()

    @mock.patch("xsdata.cli.logger.info")
    def test_init_config_when_file_exists(self, mock_info):
        output = tempfile.mktemp()
        output_path = Path(output).resolve()

        config = GeneratorConfig.create()
        config.version = "20.8"

        with output_path.open("w") as fp:
            config.write(fp, config)

        result = self.runner.invoke(cli, ["init-config", str(output_path)])

        self.assertIsNone(result.exception)
        self.assertNotEqual("20.8", GeneratorConfig.read(output_path))
        mock_info.assert_has_calls(
            [
                mock.call(
                    "========= xsdata v%s / Python %s / Platform %s =========\n",
                    __version__,
                    platform.python_version(),
                    sys.platform,
                ),
                mock.call("Updating configuration file %s", str(output_path)),
            ]
        )
        output_path.unlink()

    def test_init_config_with_print_mode(self):
        result = self.runner.invoke(cli, ["init-config", "--print"])

        self.assertIsNone(result.exception)
        self.assertIn('<Config xmlns="http://pypi.org/project/xsdata"', result.output)

    @mock.patch.object(Downloader, "wget")
    @mock.patch.object(Downloader, "__init__", return_value=None)
    def test_download(self, mock_init, mock_wget):
        uri = "http://www.w3.org/2009/01/xml.xsd"
        result = self.runner.invoke(cli, ["download", uri])

        self.assertIsNone(result.exception)
        mock_init.assert_called_once_with(output=Path.cwd())
        mock_wget.assert_called_once_with(uri)

    @mock.patch.object(Downloader, "wget")
    @mock.patch.object(Downloader, "__init__", return_value=None)
    def test_download_with_custom_output(self, mock_init, mock_wget):
        uri = "http://www.w3.org/2009/01/xml.xsd"

        result = self.runner.invoke(cli, ["download", uri, "--output", "here/schemas"])

        self.assertIsNone(result.exception)
        mock_init.assert_called_once_with(output=Path("here/schemas").resolve())
        mock_wget.assert_called_once_with(uri)

    def test_resolve_source(self):
        hello_path = fixtures_dir.joinpath("hello")

        file = hello_path.joinpath("hello.xsd")
        url = "http://www.xsdata/schema.xsd"

        self.assertEqual([file.as_uri()], list(resolve_source(str(file), False)))
        self.assertEqual([url], list(resolve_source(url, False)))
        self.assertEqual(5, len(list(resolve_source(str(hello_path), False))))

        def_xml_path = fixtures_dir.joinpath("calculator")
        self.assertEqual(3, len(list(resolve_source(str(def_xml_path), False))))

        actual = list(resolve_source(str(fixtures_dir), True))
        self.assertEqual(39, len(actual))
