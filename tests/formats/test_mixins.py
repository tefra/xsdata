from typing import Iterator
from typing import List

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.models import Class
from xsdata.exceptions import CodeGenerationError
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.mixins import GeneratorResult
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import OutputStructure


class NoneGenerator(AbstractGenerator):
    def __init__(self, config: GeneratorConfig):
        self.config = config

    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        pass


class AbstractGeneratorTests(FactoryTestCase):
    def setUp(self):
        config = GeneratorConfig()
        self.generator = NoneGenerator(config)
        super().setUp()

    def test_module_name(self):
        self.assertEqual("a", self.generator.module_name("a"))

    def test_package_name(self):
        self.assertEqual("a", self.generator.package_name("a"))

    def test_designate_with_filename_structure(self):
        classes = ClassFactory.list(3, package="foo", module="tests")

        self.generator.designate(classes)

        self.assertEqual("foo", classes[0].package)
        self.assertEqual("foo", classes[1].package)
        self.assertEqual("foo", classes[2].package)

        self.assertEqual("tests", classes[0].module)
        self.assertEqual("tests", classes[1].module)
        self.assertEqual("tests", classes[2].module)

        classes = ClassFactory.list(1, package=None)
        with self.assertRaises(CodeGenerationError) as cm:
            self.generator.designate(classes)

        self.assertEqual(
            "Class `class_E` has not been assign to a package.", str(cm.exception)
        )

    def test_designate_with_namespaces_structure(self):
        classes = ClassFactory.list(2, package=None)
        self.generator.config.output.structure = OutputStructure.NAMESPACES
        self.generator.config.output.package = "bar"

        self.generator.designate(classes)
        self.assertEqual("bar", classes[0].package)
        self.assertEqual("bar", classes[1].package)

        self.assertEqual("xsdata", classes[0].module)
        self.assertEqual("xsdata", classes[1].module)

        classes = ClassFactory.list(1, qname="foo")
        with self.assertRaises(CodeGenerationError) as cm:
            self.generator.designate(classes)

        self.assertEqual(
            ("Class `foo` target namespace is empty, " "avoid option `--ns-struct`"),
            str(cm.exception),
        )
