from typing import Iterator
from typing import List
from unittest import mock

from xsdata.codegen.models import Class
from xsdata.exceptions import CodeGenerationError
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.mixins import GeneratorResult
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class NoneGenerator(AbstractGenerator):
    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        """Do nothing."""


class AbstractGeneratorTests(FactoryTestCase):
    def setUp(self):
        config = GeneratorConfig()
        self.generator = NoneGenerator(config)
        super().setUp()

    def test_module_name(self):
        self.assertEqual("a", self.generator.module_name("a"))

    def test_package_name(self):
        self.assertEqual("a", self.generator.package_name("a"))

    @mock.patch.object(NoneGenerator, "module_name", return_value="mod")
    @mock.patch.object(NoneGenerator, "package_name", return_value="pck")
    def test_normalize_packages(self, *args):
        classes = [
            ClassFactory.create(qname="{a}a", package="bar"),
            ClassFactory.create(qname="{a}b", package="bar"),
            ClassFactory.create(qname="b", package="bar"),
        ]

        self.generator.normalize_packages(classes)
        self.assertEqual("pck", classes[0].package)
        self.assertEqual("pck", classes[1].package)
        self.assertEqual("pck", classes[2].package)

        self.assertEqual("mod", classes[0].module)
        self.assertEqual("mod", classes[1].module)
        self.assertEqual("mod", classes[2].module)

        with self.assertRaises(CodeGenerationError) as cm:
            self.generator.normalize_packages(ClassFactory.list(1))

        self.assertEqual(
            "Class `class_B` has not been assigned to a package", str(cm.exception)
        )
