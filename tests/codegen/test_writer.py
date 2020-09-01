from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator
from typing import List
from typing import Optional
from unittest import mock

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.models import Class
from xsdata.codegen.writer import writer
from xsdata.exceptions import CodeGenerationError
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.mixins import GeneratorResult
from xsdata.utils import text


@dataclass
class FakeGenerator(AbstractGenerator):
    dir: Optional[TemporaryDirectory] = None

    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        for obj in classes:
            assert obj.package is not None
            yield GeneratorResult(
                path=Path(f"{self.dir}/{obj.name}.txt"),
                title=obj.package,
                source=obj.name,
            )

    @classmethod
    def module_name(cls, name):
        return text.snake_case(name)

    @classmethod
    def package_name(cls, name):
        return text.snake_case(name)


@dataclass
class EmptyGenerator(FakeGenerator):
    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        for obj in classes:
            yield GeneratorResult(
                path=Path(f"{self.dir}/{obj.name}.txt"), title="Empty", source=""
            )


class CodeWriterTests(FactoryTestCase):
    FAKE_NAME = "fake"

    def tearDown(self):
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
        classes = ClassFactory.list(2)
        with TemporaryDirectory() as tmpdir:
            writer.register_format(self.FAKE_NAME, FakeGenerator(tmpdir))
            writer.write(classes, "fake")

            for obj in classes:
                self.assertEqual(obj.name, Path(f"{tmpdir}/{obj.name}.txt").read_text())

    def test_write_skip_empty_output(self):
        cls = ClassFactory.create()
        with TemporaryDirectory() as tmpdir:
            writer.register_format(self.FAKE_NAME, EmptyGenerator(tmpdir))
            writer.write([cls], "fake")

            self.assertFalse(Path(f"{tmpdir}/{cls.name}.txt").exists())

    @mock.patch("builtins.print")
    def test_print(self, mock_print):
        classes = ClassFactory.list(2)
        writer.register_format(self.FAKE_NAME, FakeGenerator())
        writer.print(classes, "fake")

        mock_print.assert_has_calls([mock.call(obj.name, end="") for obj in classes])

    def test_designate(self):
        classes = ClassFactory.list(3)
        classes[2].package = "foo!"
        classes[2].module = "tests!"

        writer.register_format(self.FAKE_NAME, FakeGenerator())
        writer.designate(classes, "fake", "", False)

        self.assertEqual("foo", classes[0].package)
        self.assertEqual("foo", classes[1].package)
        self.assertEqual("foo", classes[2].package)

        self.assertEqual("tests", classes[0].module)
        self.assertEqual("tests", classes[1].module)
        self.assertEqual("tests", classes[2].module)

        classes = ClassFactory.list(1, package=None)
        with self.assertRaises(CodeGenerationError) as cm:
            writer.designate(classes, "fake", "", False)

        self.assertEqual(
            "Class `class_E` has not been assign to a package.", str(cm.exception)
        )

        classes = ClassFactory.list(2, package=None)
        writer.designate(classes, "fake", "bar", True)
        self.assertEqual("bar", classes[0].package)
        self.assertEqual("bar", classes[1].package)

        self.assertEqual("xsdata", classes[0].module)
        self.assertEqual("xsdata", classes[1].module)

        classes = ClassFactory.list(1, qname="foo")
        with self.assertRaises(CodeGenerationError) as cm:
            writer.designate(classes, "fake", "foo", True)

        self.assertEqual(
            ("Class `foo` target namespace is empty, " "avoid option `--ns-struct`"),
            str(cm.exception),
        )
