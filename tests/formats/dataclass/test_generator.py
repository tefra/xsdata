import random
from pathlib import Path
from unittest import mock

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from tests.factories import PackageFactory
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.resolver import DependenciesResolver


class DataclassGeneratorTests(FactoryTestCase):
    @mock.patch.object(DependenciesResolver, "process")
    @mock.patch.object(DataclassGenerator, "render_package")
    @mock.patch.object(DataclassGenerator, "render_module")
    @mock.patch.object(DataclassGenerator, "render_classes")
    @mock.patch.object(DataclassGenerator, "prepare_imports")
    def test_render(
        self,
        mock_prepare_imports,
        mock_render_classes,
        mock_render_module,
        mock_render_package,
        mock_resolver_process,
    ):
        classes = ClassFactory.list(3)

        mock_render_module.return_value = "module"
        mock_render_package.return_value = "package"
        mock_prepare_imports.return_value = [
            PackageFactory.create(name="foo", source="bar")
        ]
        mock_render_classes.return_value = "classes"

        iterator = DataclassGenerator().render(classes)

        actual = [out for out in iterator]
        self.assertEqual(2, len(actual))

        self.assertEqual(3, len(actual[0]))
        self.assertEqual("init", actual[0][1])
        self.assertEqual("foo/__init__.py", str(actual[0][0].relative_to(Path.cwd())))
        self.assertEqual(mock_render_package.return_value, actual[0][2])

        self.assertEqual(3, len(actual[1]))
        self.assertIsInstance(actual[1][0], Path)
        self.assertTrue(actual[1][0].is_absolute())
        self.assertEqual("foo.tests", actual[1][1])
        self.assertEqual("foo/tests.py", str(actual[1][0].relative_to(Path.cwd())))
        self.assertEqual(mock_render_module.return_value, actual[1][2])

        mock_resolver_process.assert_called_once_with(classes)

        mock_prepare_imports.assert_called_once()
        mock_prepare_imports.render_classes()
        mock_render_module.assert_called_once_with(
            imports=mock_prepare_imports.return_value,
            output=mock_render_classes.return_value,
        )

    def test_render_package(self):
        classes = ClassFactory.list(3)
        random.shuffle(classes)

        actual = DataclassGenerator().render_package(classes)
        expected = "\n".join(
            [
                "from foo.tests import ClassB",
                "from foo.tests import ClassC",
                "from foo.tests import ClassD",
                "",
            ]
        )
        self.assertEqual(expected, actual)

    @mock.patch.object(DataclassGenerator, "render_class")
    @mock.patch.object(DataclassGenerator, "process_class")
    def test_render_classes(self, mock_process_class, mock_render_class):
        renders = [" does it matter?", " white space "]
        classes = ClassFactory.list(2)
        mock_process_class.side_effect = ClassFactory.list(2)
        mock_render_class.side_effect = renders
        output = "\n".join(renders).strip()

        actual = DataclassGenerator().render_classes(classes)
        self.assertEqual(f"\n\n{output}\n", actual)

    @mock.patch.object(DataclassGenerator, "process_import")
    def test_prepare_imports(self, mock_process_import):
        packages = [
            PackageFactory.create(name="foo", source="omg"),
            PackageFactory.create(name="bar", source="omg"),
            PackageFactory.create(name="thug", source="life"),
        ]
        processed = [
            PackageFactory.create(name="aaa", source="a"),
            PackageFactory.create(name="bbb", source="b"),
            PackageFactory.create(name="ccc", source="c"),
        ]

        mock_process_import.side_effect = processed

        expected = {"omg": processed[:2], "life": processed[2:]}

        actual = DataclassGenerator().prepare_imports(packages)
        self.assertEqual(expected, actual)

    def test_module_name(self):
        generator = DataclassGenerator()
        self.assertEqual("foo_bar", generator.module_name("fooBar"))
        self.assertEqual("foo_bar_wtf", generator.module_name("fooBar.wtf"))
