from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.generators import AbstractGenerator
from xsdata.models.codegen import Class
from xsdata.utils import text
from xsdata.writer import writer


@dataclass
class FakeGenerator(AbstractGenerator):
    dir: Optional[TemporaryDirectory] = None

    def render(self, classes: List[Class]) -> Iterator[Tuple[Path, str, str]]:
        path = Path(f"{self.dir}/test.txt")
        yield path, ".".join(path.with_suffix("").parts), "foobar"

    def module_name(self, name):
        return text.snake_case(name)

    def package_name(self, name):
        return text.snake_case(name)


class CodeWriterTests(FactoryTestCase):
    FAKE_NAME = "fake"

    def tearDown(self) -> None:
        writer.generators.pop(self.FAKE_NAME, False)

    def test_formats(self):
        expected = ["pydata", "plantuml"]
        self.assertEqual(expected, writer.formats)
        self.assertIsInstance(writer.get_format("pydata"), DataclassGenerator)

    def test_register_generator(self):
        writer.register_format(self.FAKE_NAME, FakeGenerator())
        self.assertIn("fake", writer.formats)
        self.assertIsInstance(writer.get_format("fake"), FakeGenerator)

    def test_write(self):
        with TemporaryDirectory() as tmpdir:
            writer.register_format(self.FAKE_NAME, FakeGenerator(tmpdir))
            writer.write([], "fake")
            self.assertEqual("foobar", Path(f"{tmpdir}/test.txt").read_text())

    def test_designate(self):
        classes = ClassFactory.list(3)
        classes[2].package = "foo!"
        classes[2].module = "tests!"

        writer.register_format(self.FAKE_NAME, FakeGenerator())
        writer.designate(classes, "fake")

        self.assertEqual("foo", classes[0].package)
        self.assertEqual("foo", classes[1].package)
        self.assertEqual("foo", classes[2].package)

        self.assertEqual("tests", classes[0].module)
        self.assertEqual("tests", classes[1].module)
        self.assertEqual("tests_1", classes[2].module)
