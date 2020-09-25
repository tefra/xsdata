from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator
from typing import List
from unittest import mock

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.models import Class
from xsdata.codegen.writer import CodeWriter
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.mixins import GeneratorResult
from xsdata.formats.plantuml.generator import PlantUmlGenerator
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import OutputFormat


class NoneGenerator(AbstractGenerator):
    def __init__(self):
        pass

    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        pass


class CodeWriterTests(FactoryTestCase):
    def setUp(self):
        generator = NoneGenerator()
        self.writer = CodeWriter(generator)

    @mock.patch.object(NoneGenerator, "render")
    @mock.patch.object(NoneGenerator, "designate")
    def test_write(self, mock_designate, mock_render):
        classes = ClassFactory.list(2)
        with TemporaryDirectory() as tmpdir:
            mock_render.return_value = [
                GeneratorResult(Path(f"{tmpdir}/foo/a.py"), "file", "aAa"),
                GeneratorResult(Path(f"{tmpdir}/bar/b.py"), "file", "bBb"),
                GeneratorResult(Path(f"{tmpdir}/c.py"), "file", " "),
            ]
            self.writer.write(classes)

            self.assertEqual("aAa", Path(f"{tmpdir}/foo/a.py").read_text())
            self.assertEqual("bBb", Path(f"{tmpdir}/bar/b.py").read_text())
            self.assertFalse(Path(f"{tmpdir}/c.py").exists())
            mock_designate.assert_called_once_with(classes)

    @mock.patch.object(NoneGenerator, "render")
    @mock.patch.object(NoneGenerator, "designate")
    @mock.patch("builtins.print")
    def test_print(self, mock_print, mock_designate, mock_render):
        classes = ClassFactory.list(2)
        mock_render.return_value = [
            GeneratorResult(Path(f"foo/a.py"), "file", "aAa"),
            GeneratorResult(Path(f"bar/b.py"), "file", "bBb"),
            GeneratorResult(Path(f"c.py"), "file", ""),
        ]
        self.writer.print(classes)

        mock_designate.assert_called_once_with(classes)
        mock_print.assert_has_calls(
            [mock.call("aAa", end=""), mock.call("bBb", end="")]
        )

    def test_from_config(self):
        config = GeneratorConfig()
        config.output.format = OutputFormat.DATACLASS

        writer = CodeWriter.from_config(config)
        self.assertIsInstance(writer.generator, DataclassGenerator)

        config.output.format = OutputFormat.PLANTUML
        writer = CodeWriter.from_config(config)
        self.assertIsInstance(writer.generator, PlantUmlGenerator)
