from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import RenameDuplicateClasses
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import StructureStyle
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class RenameDuplicateClassesTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.processor = RenameDuplicateClasses(container=self.container)

    @mock.patch.object(RenameDuplicateClasses, "rename_classes")
    def test_run(self, mock_rename_classes):
        classes = [
            ClassFactory.create(qname="{foo}A"),
            ClassFactory.create(qname="{foo}a"),
            ClassFactory.create(qname="_a"),
            ClassFactory.create(qname="_b"),
            ClassFactory.create(qname="b", location="!@#$"),
        ]
        self.container.extend(classes)
        self.processor.run()

        mock_rename_classes.assert_has_calls(
            [
                mock.call(classes[:2], False),
                mock.call(classes[3:], False),
            ]
        )

    @mock.patch.object(RenameDuplicateClasses, "rename_classes")
    def test_run_with_single_package_structure(self, mock_rename_classes):
        classes = [
            ClassFactory.create(qname="{foo}a"),
            ClassFactory.create(qname="{bar}a"),
            ClassFactory.create(qname="a"),
        ]
        self.container.extend(classes)
        self.processor.run()

        mock_rename_classes.assert_called_once_with(classes, True)

    @mock.patch.object(RenameDuplicateClasses, "rename_classes")
    def test_run_with_single_location_source(self, mock_rename_classes):
        classes = [
            ClassFactory.create(qname="{foo}a"),
            ClassFactory.create(qname="{bar}a"),
            ClassFactory.create(qname="a"),
        ]

        self.container.config.output.structure_style = StructureStyle.SINGLE_PACKAGE
        self.container.extend(classes)
        self.processor.run()

        mock_rename_classes.assert_called_once_with(classes, True)

    @mock.patch.object(RenameDuplicateClasses, "rename_classes")
    def test_run_with_clusters_structure(self, mock_rename_classes):
        classes = [
            ClassFactory.create(qname="{foo}a"),
            ClassFactory.create(qname="{bar}a"),
            ClassFactory.create(qname="a"),
        ]
        self.container.config.output.structure_style = StructureStyle.CLUSTERS
        self.container.extend(classes)
        self.processor.run()

        mock_rename_classes.assert_called_once_with(classes, True)

    @mock.patch.object(RenameDuplicateClasses, "rename_class")
    def test_rename_classes(self, mock_rename_class):
        classes = [
            ClassFactory.create(qname="_a", tag=Tag.ELEMENT),
            ClassFactory.create(qname="_A", tag=Tag.ELEMENT),
            ClassFactory.create(qname="a", tag=Tag.COMPLEX_TYPE),
        ]
        self.processor.rename_classes(classes, False)
        self.processor.rename_classes(classes, True)

        mock_rename_class.assert_has_calls(
            [
                mock.call(classes[1], False),
                mock.call(classes[0], False),
                mock.call(classes[2], False),
                mock.call(classes[1], True),
                mock.call(classes[0], True),
                mock.call(classes[2], True),
            ]
        )

    @mock.patch.object(RenameDuplicateClasses, "rename_class")
    def test_rename_classes_protects_single_element(self, mock_rename_class):
        classes = [
            ClassFactory.create(qname="_a", tag=Tag.ELEMENT),
            ClassFactory.create(qname="a", tag=Tag.COMPLEX_TYPE),
        ]
        self.processor.rename_classes(classes, False)

        mock_rename_class.assert_called_once_with(classes[1], False)

    @mock.patch.object(RenameDuplicateClasses, "rename_class_dependencies")
    def test_rename_class(self, mock_rename_class_dependencies):
        target = ClassFactory.create(qname="{foo}_a")
        self.processor.container.add(target)
        self.processor.container.add(ClassFactory.create(qname="{foo}a_1"))
        self.processor.container.add(ClassFactory.create(qname="{foo}A_2"))
        self.processor.container.add(ClassFactory.create(qname="{bar}a_3"))
        self.processor.rename_class(target, False)

        self.assertEqual("{foo}_a_3", target.qname)
        self.assertEqual("_a", target.meta_name)

        mock_rename_class_dependencies.assert_has_calls(
            mock.call(item, id(target), "{foo}_a_3")
            for item in self.processor.container
        )

        self.assertEqual([target], self.container.data["{foo}_a_3"])
        self.assertEqual([], self.container.data["{foo}_a"])

    @mock.patch.object(RenameDuplicateClasses, "rename_class_dependencies")
    def test_rename_class_by_name(self, mock_rename_class_dependencies):
        target = ClassFactory.create(qname="{foo}_a")
        self.processor.container.add(target)
        self.processor.container.add(ClassFactory.create(qname="{bar}a_1"))
        self.processor.container.add(ClassFactory.create(qname="{thug}A_2"))
        self.processor.container.add(ClassFactory.create(qname="{bar}a_3"))
        self.processor.rename_class(target, True)

        self.assertEqual("{foo}_a_4", target.qname)
        self.assertEqual("_a", target.meta_name)

        mock_rename_class_dependencies.assert_has_calls(
            mock.call(item, id(target), "{foo}_a_4")
            for item in self.processor.container
        )

        self.assertEqual([target], self.container.data["{foo}_a_4"])
        self.assertEqual([], self.container.data["{foo}_a"])

    def test_rename_class_dependencies(self):
        attr_type = AttrTypeFactory.create(qname="{foo}bar", reference=1)

        target = ClassFactory.create(
            extensions=[
                ExtensionFactory.create(),
                ExtensionFactory.create(attr_type.clone()),
            ],
            attrs=[
                AttrFactory.create(),
                AttrFactory.create(types=[AttrTypeFactory.create(), attr_type.clone()]),
            ],
            inner=[
                ClassFactory.create(
                    extensions=[ExtensionFactory.create(attr_type.clone())],
                    attrs=[
                        AttrFactory.create(),
                        AttrFactory.create(
                            types=[AttrTypeFactory.create(), attr_type.clone()]
                        ),
                    ],
                )
            ],
        )

        self.processor.rename_class_dependencies(target, 1, "thug")
        dependencies = set(target.dependencies())
        self.assertNotIn("{foo}bar", dependencies)
        self.assertIn("thug", dependencies)

    def test_rename_attr_dependencies_with_default_enum(self):
        attr_type = AttrTypeFactory.create(qname="{foo}bar", reference=1)
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    types=[attr_type],
                    default=f"@enum@{attr_type.qname}::member",
                ),
            ]
        )

        self.processor.rename_class_dependencies(target, 1, "thug")
        dependencies = set(target.dependencies())
        self.assertEqual("@enum@thug::member", target.attrs[0].default)
        self.assertNotIn("{foo}bar", dependencies)
        self.assertIn("thug", dependencies)

    def test_rename_attr_dependencies_with_choices(self):
        attr_type = AttrTypeFactory.create(qname="foo", reference=1)
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    choices=[
                        AttrFactory.create(types=[attr_type.clone()]),
                    ]
                )
            ]
        )

        self.processor.rename_class_dependencies(target, 1, "bar")
        dependencies = set(target.dependencies())
        self.assertNotIn("foo", dependencies)
        self.assertIn("bar", dependencies)
