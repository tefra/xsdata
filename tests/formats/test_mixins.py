from tests.factories import FactoryTestCase
from xsdata.formats.mixins import AbstractGenerator


class AbstractGeneratorTests(FactoryTestCase):
    def test_module_name(self):
        self.assertEqual("a", AbstractGenerator.module_name("a"))

    def test_package_name(self):
        self.assertEqual("a", AbstractGenerator.package_name("a"))
