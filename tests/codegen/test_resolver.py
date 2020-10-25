from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from tests.factories import PackageFactory
from xsdata.codegen.models import Class
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.exceptions import ResolverValueError
from xsdata.utils.namespaces import build_qname


class DependenciesResolverTest(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.resolver = DependenciesResolver()

    @mock.patch.object(DependenciesResolver, "resolve_imports")
    @mock.patch.object(DependenciesResolver, "create_class_list")
    @mock.patch.object(DependenciesResolver, "create_class_map")
    def test_process(
        self, mock_create_class_map, create_class_list, mock_resolve_imports
    ):
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

    def test_sorted_imports(self):
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
    def test_sorted_classes(self, mock_apply_aliases):
        mock_apply_aliases.side_effect = lambda x: x

        self.resolver.class_list = ["a", "b", "c", "d"]
        self.resolver.class_map = {x: ClassFactory.create(qname=x) for x in "ca"}

        result = self.resolver.sorted_classes()
        expected = [self.resolver.class_map[x] for x in "ac"]

        self.assertEqual(expected, result)
        mock_apply_aliases.assert_has_calls([mock.call(x) for x in expected])

    def test_apply_aliases(self):
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
                    ],
                )
            ],
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

        self.assertEqual(1, len(obj.inner))
        self.assertEqual(2, len(obj.inner[0].attrs))
        self.assertEqual(1, len(obj.inner[0].attrs[0].types))
        self.assertEqual(1, len(obj.inner[0].attrs[1].types))
        self.assertIsNone(obj.inner[0].attrs[0].types[0].alias)
        self.assertEqual("IamD", obj.inner[0].attrs[1].types[0].alias)

    @mock.patch.object(DependenciesResolver, "add_import")
    @mock.patch.object(DependenciesResolver, "find_package")
    @mock.patch.object(DependenciesResolver, "import_classes")
    def test_resolve_imports(
        self, mock_import_classes, mock_find_package, mock_add_import
    ):
        class_life = ClassFactory.create(qname="life")
        import_names = [
            "foo",  # cool
            "bar",  # cool
            "{another}foo",  # another foo
            "{thug}life",  # life class exists add alias
            "{common}type",  # type class doesn't exist add just the name
        ]
        self.resolver.class_map = {class_life.qname: class_life}
        mock_import_classes.return_value = import_names
        mock_find_package.side_effect = ["first", "second", "third", "forth", "fifth"]

        self.resolver.resolve_imports()
        mock_add_import.assert_has_calls(
            [
                mock.call(qname=import_names[0], package="first", exists=False),
                mock.call(qname=import_names[1], package="second", exists=False),
                mock.call(qname=import_names[2], package="third", exists=True),
                mock.call(qname=import_names[3], package="forth", exists=True),
                mock.call(qname=import_names[4], package="fifth", exists=False),
            ]
        )

    def test_add_import(self):
        self.assertEqual(0, len(self.resolver.imports))

        package = "here.there"
        foo_qname = "foo"
        bar_qname = "bar"

        self.resolver.add_import(foo_qname, package, False)
        self.resolver.add_import(bar_qname, package, True)

        first = PackageFactory.create(name="foo", source=package, alias=None)
        second = PackageFactory.create(name="bar", source=package, alias="there:bar")

        self.assertEqual(2, len(self.resolver.imports))
        self.assertEqual(first, self.resolver.imports[0])
        self.assertEqual(second, self.resolver.imports[1])
        self.assertEqual({bar_qname: "there:bar"}, self.resolver.aliases)

    def test_find_package(self):
        class_a = ClassFactory.create()
        self.resolver.packages[class_a.qname] = "foo.bar"

        self.assertEqual("foo.bar", self.resolver.find_package(class_a.qname))
        with self.assertRaises(ResolverValueError):
            self.resolver.find_package("nope")

    def test_import_classes(self):
        self.resolver.class_list = [x for x in "abcdefg"]
        self.resolver.class_map = {x: x for x in "bdg"}
        self.assertEqual(["a", "c", "e", "f"], self.resolver.import_classes())

    def test_create_class_map(self):
        classes = [ClassFactory.create(qname=name) for name in "ab"]
        expected = {obj.qname: obj for obj in classes}
        self.assertEqual(expected, self.resolver.create_class_map(classes))

    def test_create_class_map_for_duplicate_classes(self):
        classes = ClassFactory.list(2, qname="a")
        with self.assertRaises(ResolverValueError) as cm:
            self.resolver.create_class_map(classes)

        self.assertEqual("Duplicate class: `a`", str(cm.exception))

    @mock.patch.object(Class, "dependencies")
    def test_create_class_list(self, mock_dependencies):
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
