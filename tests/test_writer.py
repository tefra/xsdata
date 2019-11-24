import copy
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator, List, Optional, Tuple
from unittest import TestCase

from xsdata.codegen.generator import AbstractGenerator
from xsdata.codegen.python.dataclass.generator import DataclassGenerator
from xsdata.models.codegen import Class
from xsdata.models.elements import Schema
from xsdata.writer import writer


@dataclass
class FakeRenderer(AbstractGenerator):
    dir: Optional[TemporaryDirectory] = None

    def render(self, *args, **kwargs) -> Iterator[Tuple[Path, str]]:
        yield Path(f"{self.dir}/test.txt"), "foobar"

    def print(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[str, Class]]:
        pass


class CodeWriterTests(TestCase):
    def setUp(self) -> None:
        super(CodeWriterTests, self).setUp()
        self.generators = copy.deepcopy(writer.generators)

    def tearDown(self) -> None:
        writer.generators = self.generators

    def test_formats(self):
        expected = ["pydata"]
        self.assertEqual(expected, writer.formats)
        self.assertIsInstance(
            writer.get_renderer("pydata"), DataclassGenerator
        )

    def test_register_generator(self):
        writer.register_generator("fake", FakeRenderer())
        self.assertIn("fake", writer.formats)
        self.assertIsInstance(writer.get_renderer("fake"), FakeRenderer)

    def test_write(self):
        with TemporaryDirectory() as tmpdir:
            writer.register_generator("fake", FakeRenderer(tmpdir))
            writer.write(Schema.create(), [], "", "fake")
            self.assertEqual("foobar", Path(f"{tmpdir}/test.txt").read_text())
