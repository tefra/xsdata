from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple
from unittest import TestCase

from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.generators import AbstractGenerator
from xsdata.models.codegen import Class
from xsdata.models.elements import Schema
from xsdata.writer import writer


@dataclass
class FakeRenderer(AbstractGenerator):
    dir: Optional[TemporaryDirectory] = None

    def render(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[Path, str, str]]:
        path = Path(f"{self.dir}/test.txt")
        yield path, ".".join(path.with_suffix("").parts), "foobar"


class CodeWriterTests(TestCase):
    FAKE_NAME = "fake"

    def tearDown(self) -> None:
        writer.generators.pop(self.FAKE_NAME, False)

    def test_formats(self):
        expected = ["pydata", "plantuml"]
        self.assertEqual(expected, writer.formats)
        self.assertIsInstance(writer.get_renderer("pydata"), DataclassGenerator)

    def test_register_generator(self):
        writer.register_generator(self.FAKE_NAME, FakeRenderer())
        self.assertIn("fake", writer.formats)
        self.assertIsInstance(writer.get_renderer("fake"), FakeRenderer)

    def test_write(self):
        with TemporaryDirectory() as tmpdir:
            writer.register_generator(self.FAKE_NAME, FakeRenderer(tmpdir))
            writer.write(Schema.create(), [], "", "fake")
            self.assertEqual("foobar", Path(f"{tmpdir}/test.txt").read_text())
