from unittest import mock

from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.models import Class
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.models.enums import DataType
from xsdata.utils.namespaces import build_qname
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    ExtensionFactory,
    FactoryTestCase,
    PackageFactory,
)


class DependenciesResolverTest(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.resolver = DependenciesResolver({})

    @mock.patch.object(DependenciesResolver, "resolve_imports")
    @mock.patch.object(DependenciesResolver, "create_class_list")
    @mock.patch.object(DependenciesResolver, "create_class_map")
    def test_process(
        self, mock_create_class_map, create_class_list, mock_resolve_imports
    ) -> None:
        classes = ClassFactory.list(3)

        mock_create_class_map.return_value = {"b": classes[0]}
        create_class_list.return_value = classes[::-1]

        self.resolver.imports.append(PackageFactory.create(name="foo", source="bar"))
        self.resolver.aliases = {"a": "a"}

        self.resolver.process(classes)
        self.assertEqual([], self.resolver.imports)
        self.assertEqual({}, self.resolver.aliases)

        self.assertEqual(mock_create_class_map.return_value, self.resolver.class_map)
        self.assertEqual(create_class_list.return_value, self.resolver.class_list)

        mock_resolve_imports.assert_called_once_with()

    def test_sorted_imports(self) -> None:
        packages = [
            PackageFactory.create(name=x, alias=None, source="foo") for x in "cab"
        ]
        self.resolver.imports = packages

        result = self.resolver.sorted_imports()
        self.assertIsNot(packages, result)

        self.assertEqual(packages[1], result[0])
        self.assertEqual(packages[2], result[1])
        self.assertEqual(packages[0], result[2])

    @mock.patch.object(DependenciesResolver, "apply_aliases")
    def test_sorted_classes(self, mock_apply_aliases) -> None:
        mock_apply_aliases.side_effect = lambda x: x

        self.resolver.class_list = ["a", "b", "c", "d"]
        self.resolver.class_map = {x: ClassFactory.create(qname=x) for x in "ca"}

        result = self.resolver.sorted_classes()
        expected = [self.resolver.class_map[x] for x in "ac"]

        self.assertEqual(expected, result)
        mock_apply_aliases.assert_has_calls([mock.call(x) for x in expected])

    def test_apply_aliases(self) -> None:
        self.resolver.aliases = {
            build_qname("xsdata", "d"): "IamD",
            build_qname("xsdata", "a"): "IamA",
        }
        type_a = AttrTypeFactory.create(qname="{xsdata}a")
        type_b = AttrTypeFactory.create(qname="{xsdata}b")
        type_c = AttrTypeFactory.create(qname="{xsdata}c")
        type_d = AttrTypeFactory.create(qname="{xsdata}d")

        obj = ClassFactory.create(
            qname="a",
            attrs=[
                AttrFactory.create(name="a", types=[type_a]),
                AttrFactory.create(name="b", types=[type_b]),
                AttrFactory.create(name="c", types=[type_a, type_d]),
            ],
            inner=[
                ClassFactory.create(
                    qname="b",
                    attrs=[
                        AttrFactory.create(name="c", types=[type_c]),
                        AttrFactory.create(name="d", types=[type_d]),
                        AttrFactory.create(
                            name="compound",
                            types=[AttrTypeFactory.native(DataType.ANY_TYPE)],
                            choices=[
                                AttrFactory.create(name="a", types=[type_a, type_d]),
                            ],
                        ),
                    ],
                )
            ],
            extensions=[ExtensionFactory.create(type_a)],
        )

        self.resolver.apply_aliases(obj)

        self.assertEqual(3, len(obj.attrs))
        self.assertEqual(1, len(obj.attrs[0].types))
        self.assertEqual(1, len(obj.attrs[1].types))
        self.assertEqual(2, len(obj.attrs[2].types))

        self.assertEqual("IamA", obj.attrs[0].types[0].alias)
        self.assertIsNone(obj.attrs[1].types[0].alias)
        self.assertEqual("IamA", obj.attrs[2].types[0].alias)
        self.assertEqual("IamD", obj.attrs[2].types[1].alias)
        self.assertEqual("IamA", obj.extensions[0].type.alias)

        self.assertEqual(1, len(obj.inner))
        self.assertEqual(3, len(obj.inner[0].attrs))
        self.assertEqual(1, len(obj.inner[0].attrs[0].types))
        self.assertEqual(1, len(obj.inner[0].attrs[1].types))

        self.assertEqual("IamA", obj.inner[0].attrs[2].choices[0].types[0].alias)
        self.assertEqual("IamD", obj.inner[0].attrs[2].choices[0].types[1].alias)

        self.assertIsNone(obj.inner[0].attrs[0].types[0].alias)
        self.assertEqual("IamD", obj.inner[0].attrs[1].types[0].alias)

    @mock.patch.object(DependenciesResolver, "set_aliases")
    @mock.patch.object(DependenciesResolver, "resolve_conflicts")
    @mock.patch.object(DependenciesResolver, "get_class_module")
    @mock.patch.object(DependenciesResolver, "import_classes")
    def test_resolve_imports(
        self,
        mock_import_classes,
        mock_get_class_module,
        mock_resolve_conflicts,
        mock_set_aliases,
    ) -> None:
        class_life = ClassFactory.create(qname="life")
        import_names = [
            "foo_1",  # cool
            "bar",  # cool
            "{another}foo1",  # another foo
            "{thug}life",  # life class exists add alias
            "{common}type",  # type class doesn't exist add just the name
        ]
        self.resolver.class_map = {class_life.qname: class_life}
        mock_import_classes.return_value = import_names
        mock_get_class_module.side_effect = [
            "first",
            "second",
            "third",
            "forth",
            "fifth",
        ]

        self.resolver.resolve_imports()
        mock_resolve_conflicts.assert_called_once_with(
            self.resolver.imports, {class_life.slug}
        )
        mock_set_aliases.assert_called_once_with()

    def test_resolve_conflicts(self) -> None:
        imports = [
            PackageFactory.create(qname="{a}a", source="models.aa"),
            PackageFactory.create(qname="{b}a", source="models.ba"),
            PackageFactory.create(qname="{c}root", source="models.common"),
            PackageFactory.create(qname="{c}penalty", source="models.common"),
        ]

        protected = {"penalty"}
        self.resolver.resolve_conflicts(imports, protected)

        self.assertEqual("aa:a", imports[0].alias)
        self.assertEqual("ba:a", imports[1].alias)
        self.assertEqual(None, imports[2].alias)
        self.assertEqual("common:penalty", imports[3].alias)

    def test_set_aliases(self) -> None:
        self.resolver.imports = [
            PackageFactory.create(qname="{a}a", alias="aa"),
            PackageFactory.create(qname="{b}a", alias="ba"),
            PackageFactory.create(qname="{c}a"),
        ]
        self.resolver.set_aliases()
        self.assertEqual({"{a}a": "aa", "{b}a": "ba"}, self.resolver.aliases)

    def test_get_class_module(self) -> None:
        class_a = ClassFactory.create()
        self.resolver.registry[class_a.qname] = "foo.bar"

        self.assertEqual("foo.bar", self.resolver.get_class_module(class_a.qname))
        with self.assertRaises(CodegenError):
            self.resolver.get_class_module("nope")

    def test_import_classes(self) -> None:
        self.resolver.class_list = list("abcdefg")
        self.resolver.class_map = {x: x for x in "bdg"}
        self.assertEqual(["a", "c", "e", "f"], self.resolver.import_classes())

    def test_create_class_map(self) -> None:
        classes = [ClassFactory.create(qname=name) for name in "ab"]
        expected = {obj.qname: obj for obj in classes}
        self.assertEqual(expected, self.resolver.create_class_map(classes))

    def test_create_class_map_for_duplicate_classes(self) -> None:
        classes = ClassFactory.list(2, qname="a")
        with self.assertRaises(CodegenError):
            self.resolver.create_class_map(classes)

    @mock.patch.object(Class, "dependencies")
    def test_create_class_list(self, mock_dependencies) -> None:
        classes = ClassFactory.list(3)
        mock_dependencies.side_effect = [
            {build_qname("xsdata", "class_C"), "b"},
            {"c", "d"},
            {"e", "d"},
        ]

        actual = self.resolver.create_class_list(classes)
        expected = [
            "b",
            "c",
            "d",
            "e",
            "{xsdata}class_C",
            "{xsdata}class_D",
            "{xsdata}class_B",
        ]
        self.assertEqual(expected, list(map(str, actual)))
