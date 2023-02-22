from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator
from typing import List
from unittest import mock

from xsdata.codegen.models import Class
from xsdata.codegen.writer import CodeWriter
from xsdata.exceptions import CodeGenerationError
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.mixins import GeneratorResult
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class NoneGenerator(AbstractGenerator):
    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        pass


class CodeWriterTests(FactoryTestCase):
    def setUp(self):
        config = GeneratorConfig()
        generator = NoneGenerator(config)
        self.writer = CodeWriter(generator)

    @mock.patch.object(NoneGenerator, "render_header")
    @mock.patch.object(NoneGenerator, "render")
    @mock.patch.object(NoneGenerator, "normalize_packages")
    def test_write(self, mock_normalize_packages, mock_render, mock_render_header):
        classes = ClassFactory.list(2)
        with TemporaryDirectory() as tmpdir:
            mock_render.return_value = [
                GeneratorResult(Path(f"{tmpdir}/foo/a.py"), "file", "aAa"),
                GeneratorResult(Path(f"{tmpdir}/bar/b.py"), "file", "bBb"),
                GeneratorResult(Path(f"{tmpdir}/c.py"), "file", " "),
            ]
            mock_render_header.return_value = "// Head\n"
            self.writer.write(classes)

            self.assertEqual("// Head\naAa", Path(f"{tmpdir}/foo/a.py").read_text())
            self.assertEqual("// Head\nbBb", Path(f"{tmpdir}/bar/b.py").read_text())
            self.assertFalse(Path(f"{tmpdir}/c.py").exists())
            mock_normalize_packages.assert_called_once_with(classes)

    @mock.patch.object(NoneGenerator, "render")
    @mock.patch.object(NoneGenerator, "normalize_packages")
    @mock.patch("builtins.print")
    def test_print(self, mock_print, mock_normalize_packages, mock_render):
        classes = ClassFactory.list(2)
        mock_render.return_value = [
            GeneratorResult(Path("foo/a.py"), "file", "aAa"),
            GeneratorResult(Path("bar/b.py"), "file", "bBb"),
            GeneratorResult(Path("c.py"), "file", ""),
        ]
        self.writer.print(classes)

        mock_normalize_packages.assert_called_once_with(classes)
        mock_print.assert_has_calls(
            [mock.call("aAa", end=""), mock.call("bBb", end="")]
        )

    def test_from_config(self):
        CodeWriter.unregister_generator("dataclasses")
        config = GeneratorConfig()

        with self.assertRaises(CodeGenerationError) as cm:
            CodeWriter.from_config(config)

        self.assertEqual("Unknown output format: 'dataclasses'", str(cm.exception))

        CodeWriter.register_generator("dataclasses", DataclassGenerator)
        writer = CodeWriter.from_config(config)
        self.assertIsInstance(writer.generator, DataclassGenerator)
