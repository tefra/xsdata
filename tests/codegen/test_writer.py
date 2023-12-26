from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator, List
from unittest import mock

from xsdata.codegen.models import Class
from xsdata.codegen.writer import CodeWriter
from xsdata.exceptions import CodeGenerationError
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.mixins import AbstractGenerator, GeneratorResult
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import ClassFactory, FactoryTestCase


class NoneGenerator(AbstractGenerator):
    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        pass


class CodeWriterTests(FactoryTestCase):
    def setUp(self):
        config = GeneratorConfig()
        generator = NoneGenerator(config)
        self.writer = CodeWriter(generator)

    @mock.patch.object(CodeWriter, "ruff_code")
    @mock.patch.object(NoneGenerator, "render_header")
    @mock.patch.object(NoneGenerator, "render")
    @mock.patch.object(NoneGenerator, "normalize_packages")
    def test_write(
        self, mock_normalize_packages, mock_render, mock_render_header, mock_ruff_code
    ):
        classes = ClassFactory.list(2)
        mock_ruff_code.side_effect = lambda x, y: x
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

    @mock.patch.object(CodeWriter, "ruff_code")
    @mock.patch.object(NoneGenerator, "render_header")
    @mock.patch.object(NoneGenerator, "render")
    @mock.patch.object(NoneGenerator, "normalize_packages")
    @mock.patch("builtins.print")
    def test_print(
        self,
        mock_print,
        mock_normalize_packages,
        mock_render,
        mock_render_header,
        mock_ruff_code,
    ):
        classes = ClassFactory.list(2)
        mock_render.return_value = [
            GeneratorResult(Path("foo/a.py"), "file", "aAa"),
            GeneratorResult(Path("bar/b.py"), "file", "bBb"),
            GeneratorResult(Path("c.py"), "file", ""),
        ]
        mock_render_header.return_value = "# H\n"
        mock_ruff_code.side_effect = lambda x, y: x

        self.writer.print(classes)

        mock_normalize_packages.assert_called_once_with(classes)
        mock_print.assert_has_calls(
            [mock.call("# H\naAa", end=""), mock.call("# H\nbBb", end="")]
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

    def test_ruff_code(self):
        src_code = (
            "\n"
            "import sys\n"
            "@dataclass\n"
            "\n"
            "class MyType:\n"
            "\n"
            '    value: Optional[str] = field(default=None, metadata={"type": "Element", "required": True})\n'
            "\n"
            "\n"
            "        "
        )

        self.writer.generator.config.output.max_line_length = 55
        actual = self.writer.ruff_code(src_code, Path(__file__))
        expected = (
            "import sys\n"
            "\n"
            "\n"
            "@dataclass\n"
            "class MyType:\n"
            "    value: Optional[str] = field(\n"
            "        default=None,\n"
            '        metadata={"type": "Element", "required": True},\n'
            "    )\n"
        )
        self.assertEqual(expected, actual)

    def test_format_with_invalid_code(self):
        src_code = """a = "1"""
        file_path = Path(__file__)

        self.writer.generator.config.output.max_line_length = 55
        with self.assertRaises(CodeGenerationError) as cm:
            self.writer.ruff_code(src_code, file_path)

        self.assertIn("Ruff failed", str(cm.exception))
