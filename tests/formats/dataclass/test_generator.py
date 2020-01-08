from pathlib import Path
from unittest import mock

from tests.factories import ClassFactory, FactoryTestCase, PackageFactory
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.models.elements import Schema
from xsdata.resolver import DependenciesResolver


class DataclassGeneratorTests(FactoryTestCase):
    @mock.patch.object(DependenciesResolver, "process")
    @mock.patch.object(DataclassGenerator, "render_module")
    @mock.patch.object(DataclassGenerator, "render_classes")
    @mock.patch.object(DataclassGenerator, "prepare_imports")
    def test_render(
        self,
        mock_prepare_imports,
        mock_render_classes,
        mock_render_module,
        mock_resolved_process,
    ):
        schema = Schema.create(location=Path("foo.xsd"))
        package = "some.Foo.Some.ThugLife"
        classes = ClassFactory.list(3)

        mock_render_module.return_value = "module"
        mock_prepare_imports.return_value = [
            PackageFactory.create(name="foo", source="bar")
        ]
        mock_render_classes.return_value = "classes"

        iterator = DataclassGenerator().render(schema, classes, package)

        actual = [(file, output) for file, output in iterator]
        self.assertEqual(1, len(actual))
        self.assertEqual(2, len(actual[0]))
        self.assertIsInstance(actual[0][0], Path)
        self.assertTrue(actual[0][0].is_absolute())
        self.assertEqual(
            "some/foo/some/thug_life/foo.py",
            str(actual[0][0].relative_to(Path.cwd())),
        )
        self.assertEqual(mock_render_module.return_value, actual[0][1])

        mock_resolved_process.assert_called_once_with(
            classes=classes,
            schema=schema,
            package="some.foo.some.thug_life.foo",
        )

        mock_prepare_imports.assert_called_once()
        mock_prepare_imports.render_classes()
        mock_render_module.assert_called_once_with(
            imports=mock_prepare_imports.return_value,
            output=mock_render_classes.return_value,
        )

    @mock.patch.object(DataclassGenerator, "render_class")
    @mock.patch.object(DataclassGenerator, "process_class")
    @mock.patch.object(DependenciesResolver, "sorted_classes")
    def test_render_classes(
        self, mock_sorted_classes, mock_process_class, mock_render_class
    ):
        renders = [" does it matter?", " white space "]
        mock_sorted_classes.return_value = ClassFactory.list(2)
        mock_process_class.side_effect = ClassFactory.list(2)
        mock_render_class.side_effect = renders
        output = "\n".join(renders).strip()

        actual = DataclassGenerator().render_classes()
        self.assertEqual(f"\n\n{output}\n", actual)

    @mock.patch.object(DataclassGenerator, "process_import")
    @mock.patch.object(DependenciesResolver, "sorted_imports")
    def test_prepare_imports(self, mock_sorted_imports, mock_process_import):
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

        mock_sorted_imports.return_value = packages
        mock_process_import.side_effect = processed

        expected = {"omg": processed[:2], "life": processed[2:]}

        actual = DataclassGenerator().prepare_imports()
        self.assertEqual(expected, actual)
