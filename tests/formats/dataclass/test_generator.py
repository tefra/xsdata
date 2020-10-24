import random
from pathlib import Path
from unittest import mock

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.models.config import GeneratorConfig


class DataclassGeneratorTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        config = GeneratorConfig()
        self.generator = DataclassGenerator(config)

    @mock.patch.object(DataclassGenerator, "render_package")
    @mock.patch.object(DataclassGenerator, "render_module")
    def test_render(self, mock_render_module, mock_render_package):
        classes = [
            ClassFactory.create(package="foo.bar"),
            ClassFactory.create(package="bar.foo"),
            ClassFactory.create(package="thug.life"),
        ]

        mock_render_module.return_value = "module"
        mock_render_package.return_value = "package"

        iterator = self.generator.render(classes)

        cwd = Path.cwd()
        actual = [(out.path, out.title, out.source) for out in iterator]
        expected = [
            (cwd.joinpath("foo/bar/__init__.py"), "init", "package"),
            (cwd.joinpath("foo/__init__.py"), "init", "# nothing here\n"),
            (cwd.joinpath("bar/foo/__init__.py"), "init", "package"),
            (cwd.joinpath("bar/__init__.py"), "init", "# nothing here\n"),
            (cwd.joinpath("thug/life/__init__.py"), "init", "package"),
            (cwd.joinpath("thug/__init__.py"), "init", "# nothing here\n"),
            (cwd.joinpath("foo/bar/tests.py"), "foo.bar.tests", "module"),
            (cwd.joinpath("bar/foo/tests.py"), "bar.foo.tests", "module"),
            (cwd.joinpath("thug/life/tests.py"), "thug.life.tests", "module"),
        ]
        self.assertEqual(expected, actual)
        mock_render_package.assert_has_calls([mock.call([x]) for x in classes])
        mock_render_module.assert_has_calls([mock.call(mock.ANY, [x]) for x in classes])

    def test_render_package(self):
        classes = [
            ClassFactory.create(qname="a"),
            ClassFactory.create(qname="b"),
            ClassFactory.create(qname="c"),
            ClassFactory.create(qname="a", module="bar"),
        ]

        random.shuffle(classes)

        actual = self.generator.render_package(classes)
        expected = "\n".join(
            [
                "from foo.bar import A as BarA",
                "from foo.tests import (",
                "    A as TestsA,",
                "    B,",
                "    C,",
                ")",
                "",
            ]
        )
        self.assertEqual(expected, actual)

    def test_render_module(self):
        classes = [
            ClassFactory.enumeration(2),
            ClassFactory.elements(2),
            ClassFactory.service(2),
        ]
        resolver = DependenciesResolver()

        actual = self.generator.render_module(resolver, classes)
        expected = (
            "from dataclasses import dataclass, field\n"
            "from enum import Enum\n"
            "from typing import Optional\n\n"
            '__NAMESPACE__ = "xsdata"\n\n\n'
            "class ClassB(Enum):\n"
            '    """\n'
            "    :cvar ATTR_B:\n"
            "    :cvar ATTR_C:\n"
            '    """\n'
            "    ATTR_B = None\n"
            "    ATTR_C = None\n\n\n"
            "@dataclass\n"
            "class ClassC:\n"
            '    """\n'
            "    :ivar attr_d:\n"
            "    :ivar attr_e:\n"
            '    """\n'
            "    class Meta:\n"
            '        name = "class_C"\n\n'
            "    attr_d: Optional[str] = field(\n"
            "        default=None,\n"
            "        metadata={\n"
            '            "name": "attr_D",\n'
            '            "type": "Element",\n'
            "        }\n"
            "    )\n"
            "    attr_e: Optional[str] = field(\n"
            "        default=None,\n"
            "        metadata={\n"
            '            "name": "attr_E",\n'
            '            "type": "Element",\n'
            "        }\n"
            "    )\n\n\n"
            "class ClassD:\n"
            '    attr_f = "None"\n'
            '    attr_g = "None"\n'
        )

        self.assertEqual(expected, actual)

    def test_module_name(self):
        self.assertEqual("foo_bar", self.generator.module_name("fooBar"))
        self.assertEqual("foo_bar_wtf", self.generator.module_name("fooBar.wtf"))
        self.assertEqual("mod_1111", self.generator.module_name("1111"))
        self.assertEqual("xs_string", self.generator.module_name("xs:string"))
        self.assertEqual("foo_bar_bam", self.generator.module_name("foo:bar_bam"))
        self.assertEqual("bar_bam", self.generator.module_name("urn:bar_bam"))

    def test_package_name(self):
        self.assertEqual(
            "foo.bar_bar.pkg_1", self.generator.package_name("Foo.BAR_bar.1")
        )
