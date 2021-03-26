from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.codegen.sanitizer import ClassSanitizer
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class ClassSanitizerTest(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.sanitizer = ClassSanitizer(container=self.container)

    @mock.patch.object(ClassSanitizer, "resolve_conflicts")
    @mock.patch.object(ClassSanitizer, "process_class")
    def test_process(self, mock_process_class, mock_resolve_conflicts):
        classes = ClassFactory.list(2)
        self.container.extend(classes)
        self.sanitizer.process()

        mock_process_class.assert_has_calls(list(map(mock.call, classes)))
        mock_resolve_conflicts.assert_called_once_with()

    @mock.patch.object(ClassSanitizer, "process_duplicate_attribute_names")
    @mock.patch.object(ClassSanitizer, "process_attribute_sequence")
    @mock.patch.object(ClassSanitizer, "process_attribute_restrictions")
    @mock.patch.object(ClassSanitizer, "process_attribute_default")
    def test_process_class(
        self,
        mock_process_attribute_default,
        mock_process_attribute_restrictions,
        mock_process_attribute_sequence,
        mock_process_duplicate_attribute_names,
    ):
        target = ClassFactory.elements(2)
        inner = ClassFactory.elements(1)
        target.inner.append(inner)

        self.sanitizer.process_class(target)

        calls_with_target = [
            mock.call(target.inner[0], target.inner[0].attrs[0]),
            mock.call(target, target.attrs[0]),
            mock.call(target, target.attrs[1]),
        ]

        calls_without_target = [
            mock.call(target.inner[0].attrs[0]),
            mock.call(target.attrs[0]),
            mock.call(target.attrs[1]),
        ]

        mock_process_attribute_default.assert_has_calls(calls_with_target)
        mock_process_attribute_restrictions.assert_has_calls(calls_without_target)
        mock_process_attribute_sequence.assert_has_calls(calls_with_target)
        mock_process_duplicate_attribute_names.assert_has_calls(
            [mock.call(target.inner[0].attrs), mock.call(target.attrs)]
        )

    @mock.patch.object(ClassSanitizer, "group_compound_fields")
    def test_process_class_group_compound_fields(self, mock_group_compound_fields):
        target = ClassFactory.create()
        inner = ClassFactory.create()
        target.inner.append(inner)

        self.container.config.output.compound_fields = True
        self.sanitizer.process_class(target)

        mock_group_compound_fields.assert_has_calls(
            [
                mock.call(inner),
                mock.call(target),
            ]
        )

    def test_process_attribute_default_with_enumeration(self):
        target = ClassFactory.create()
        attr = AttrFactory.enumeration()
        attr.restrictions.max_occurs = 2
        attr.fixed = True

        self.sanitizer.process_attribute_default(target, attr)
        self.assertTrue(attr.fixed)

    def test_process_attribute_default_with_optional_field(self):
        target = ClassFactory.create()
        attr = AttrFactory.create(fixed=True, default=2)
        attr.restrictions.min_occurs = 0
        self.sanitizer.process_attribute_default(target, attr)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_process_attribute_default_with_xsi_type(self):
        target = ClassFactory.create()
        attr = AttrFactory.create(
            fixed=True, default=2, name="type", namespace=Namespace.XSI.uri
        )
        self.sanitizer.process_attribute_default(target, attr)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_process_attribute_default_with_valid_case(self):
        target = ClassFactory.create()
        attr = AttrFactory.create(fixed=True, default=2)
        self.sanitizer.process_attribute_default(target, attr)
        self.assertTrue(attr.fixed)
        self.assertEqual(2, attr.default)

    @mock.patch("xsdata.codegen.sanitizer.logger.warning")
    @mock.patch.object(ClassSanitizer, "find_enum")
    def test_process_attribute_default_enum(self, mock_find_enum, mock_logger_warning):
        enum_one = ClassFactory.enumeration(1, qname="{a}root")
        enum_one.attrs[0].default = "1"
        enum_one.attrs[0].name = "one"
        enum_two = ClassFactory.enumeration(1, qname="inner")
        enum_two.attrs[0].default = "2"
        enum_two.attrs[0].name = "two"
        enum_three = ClassFactory.enumeration(1, qname="missing_member")

        mock_find_enum.side_effect = [
            None,
            enum_one,
            None,
            enum_two,
            enum_three,
        ]

        target = ClassFactory.create(
            qname="target",
            attrs=[
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(),
                        AttrTypeFactory.create(qname="foo"),
                    ],
                    default="1",
                ),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(),
                        AttrTypeFactory.create(qname="bar", forward=True),
                    ],
                    default="2",
                ),
                AttrFactory.create(default="3"),
            ],
        )

        actual = []
        for attr in target.attrs:
            self.sanitizer.process_attribute_default(target, attr)
            actual.append(attr.default)

        self.assertEqual(["@enum@{a}root::one", "@enum@inner::two", None], actual)
        mock_logger_warning.assert_called_once_with(
            "No enumeration member matched %s.%s default value `%s`",
            target.name,
            target.attrs[2].local_name,
            "3",
        )

    def test_find_enum(self):
        native_type = AttrTypeFactory.create()
        matching_external = AttrTypeFactory.create("foo")
        missing_external = AttrTypeFactory.create("bar")
        enumeration = ClassFactory.enumeration(1, qname="foo")
        inner = ClassFactory.enumeration(1, qname="foobar")

        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    types=[
                        native_type,
                        matching_external,
                        missing_external,
                    ]
                )
            ],
            inner=[inner],
        )
        self.sanitizer.container.extend([target, enumeration])

        actual = self.sanitizer.find_enum(native_type)
        self.assertIsNone(actual)

        actual = self.sanitizer.find_enum(matching_external)
        self.assertEqual(enumeration, actual)

        actual = self.sanitizer.find_enum(missing_external)
        self.assertIsNone(actual)

    def test_process_attribute_restrictions(self):
        required = Restrictions(min_occurs=1, max_occurs=1)
        attr = AttrFactory.attribute(restrictions=required.clone())
        self.sanitizer.process_attribute_restrictions(attr)
        self.assertIsNone(attr.restrictions.min_occurs)
        self.assertIsNone(attr.restrictions.max_occurs)

        tokens = Restrictions(required=True, tokens=True, min_occurs=1, max_occurs=1)
        attr = AttrFactory.element(restrictions=tokens.clone())
        self.sanitizer.process_attribute_restrictions(attr)
        self.assertFalse(attr.restrictions.required)
        self.assertIsNone(attr.restrictions.min_occurs)
        self.assertIsNone(attr.restrictions.max_occurs)

        attr = AttrFactory.element(restrictions=tokens.clone())
        attr.restrictions.max_occurs = 2
        self.sanitizer.process_attribute_restrictions(attr)
        self.assertFalse(attr.restrictions.required)
        self.assertIsNotNone(attr.restrictions.min_occurs)
        self.assertIsNotNone(attr.restrictions.max_occurs)

        multiple = Restrictions(min_occurs=0, max_occurs=2)
        attr = AttrFactory.create(tag=Tag.EXTENSION, restrictions=multiple)
        self.sanitizer.process_attribute_restrictions(attr)
        self.assertTrue(attr.restrictions.required)
        self.assertIsNone(attr.restrictions.min_occurs)
        self.assertIsNone(attr.restrictions.max_occurs)

        multiple = Restrictions(max_occurs=2, required=True)
        attr = AttrFactory.element(restrictions=multiple, fixed=True)
        self.sanitizer.process_attribute_restrictions(attr)
        self.assertIsNone(attr.restrictions.required)
        self.assertEqual(0, attr.restrictions.min_occurs)
        self.assertFalse(attr.fixed)

        attr = AttrFactory.element(restrictions=required.clone())
        self.sanitizer.process_attribute_restrictions(attr)
        self.assertTrue(attr.restrictions.required)
        self.assertIsNone(attr.restrictions.min_occurs)
        self.assertIsNone(attr.restrictions.max_occurs)

        restrictions = Restrictions(required=True, min_occurs=0, max_occurs=1)
        attr = AttrFactory.element(restrictions=restrictions, default="A", fixed=True)
        self.sanitizer.process_attribute_restrictions(attr)
        self.assertIsNone(attr.restrictions.required)
        self.assertIsNone(attr.restrictions.min_occurs)
        self.assertIsNone(attr.restrictions.max_occurs)
        self.assertIsNone(attr.default)
        self.assertFalse(attr.fixed)

        attr = AttrFactory.element(restrictions=required.clone(), default="A")
        self.sanitizer.process_attribute_restrictions(attr)
        self.assertIsNone(attr.restrictions.required)

        attr = AttrFactory.element(restrictions=required.clone(), fixed=True)
        self.sanitizer.process_attribute_restrictions(attr)
        self.assertIsNone(attr.restrictions.required)

        attr = AttrFactory.element(restrictions=required.clone())
        attr.restrictions.nillable = True
        self.sanitizer.process_attribute_restrictions(attr)
        self.assertIsNone(attr.restrictions.required)

    def test_sanitize_duplicate_attribute_names(self):
        attrs = [
            AttrFactory.create(name="a", tag=Tag.ELEMENT),
            AttrFactory.create(name="a", tag=Tag.ATTRIBUTE),
            AttrFactory.create(name="b", tag=Tag.ATTRIBUTE),
            AttrFactory.create(name="c", tag=Tag.ATTRIBUTE),
            AttrFactory.create(name="c", tag=Tag.ELEMENT),
            AttrFactory.create(name="d", tag=Tag.ELEMENT),
            AttrFactory.create(name="d", tag=Tag.ELEMENT),
            AttrFactory.create(name="e", tag=Tag.ELEMENT, namespace="b"),
            AttrFactory.create(name="e", tag=Tag.ELEMENT),
            AttrFactory.create(name="f", tag=Tag.ELEMENT),
            AttrFactory.create(name="f", tag=Tag.ELEMENT, namespace="a"),
            AttrFactory.create(name="gA", tag=Tag.ENUMERATION),
            AttrFactory.create(name="g[A]", tag=Tag.ENUMERATION),
            AttrFactory.create(name="g_a", tag=Tag.ENUMERATION),
            AttrFactory.create(name="g_a_1", tag=Tag.ENUMERATION),
        ]

        self.sanitizer.process_duplicate_attribute_names(attrs)
        expected = [
            "a",
            "a_Attribute",
            "b",
            "c_Attribute",
            "c",
            "d_Element",
            "d",
            "b_e",
            "e",
            "f",
            "a_f",
            "gA",
            "g[A]_2",
            "g_a_3",
            "g_a_1",
        ]
        self.assertEqual(expected, [x.name for x in attrs])

    def test_sanitize_attribute_sequence(self):
        def len_sequential(target: Class):
            return len([attr for attr in target.attrs if attr.restrictions.sequential])

        restrictions = Restrictions(max_occurs=2, sequential=True)
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(restrictions=restrictions.clone()),
                AttrFactory.create(restrictions=restrictions.clone()),
            ]
        )

        attrs_clone = [attr.clone() for attr in target.attrs]

        self.sanitizer.process_attribute_sequence(target, target.attrs[0])
        self.assertEqual(2, len_sequential(target))

        target.attrs[0].restrictions.sequential = False
        self.sanitizer.process_attribute_sequence(target, target.attrs[0])
        self.assertEqual(1, len_sequential(target))

        self.sanitizer.process_attribute_sequence(target, target.attrs[1])
        self.assertEqual(0, len_sequential(target))

        target.attrs = attrs_clone
        target.attrs[1].restrictions.sequential = False
        self.sanitizer.process_attribute_sequence(target, target.attrs[0])
        self.assertEqual(0, len_sequential(target))

        target.attrs[0].restrictions.sequential = True
        target.attrs[0].restrictions.max_occurs = 0
        target.attrs[1].restrictions.sequential = True
        self.sanitizer.process_attribute_sequence(target, target.attrs[0])
        self.assertEqual(1, len_sequential(target))

    @mock.patch.object(ClassSanitizer, "rename_classes")
    def test_resolve_conflicts(self, mock_rename_classes):
        classes = [
            ClassFactory.create(qname="{foo}A"),
            ClassFactory.create(qname="{foo}a"),
            ClassFactory.create(qname="_a"),
            ClassFactory.create(qname="_b"),
            ClassFactory.create(qname="b"),
        ]
        self.sanitizer.container.extend(classes)
        self.sanitizer.resolve_conflicts()

        mock_rename_classes.assert_has_calls(
            [
                mock.call(classes[:2]),
                mock.call(classes[3:]),
            ]
        )

    @mock.patch.object(ClassSanitizer, "rename_class")
    def test_rename_classes(self, mock_rename_class):
        classes = [
            ClassFactory.create(qname="_a", tag=Tag.ELEMENT),
            ClassFactory.create(qname="_A", tag=Tag.ELEMENT),
            ClassFactory.create(qname="a", tag=Tag.COMPLEX_TYPE),
        ]
        self.sanitizer.rename_classes(classes)

        mock_rename_class.assert_has_calls(
            [
                mock.call(classes[0]),
                mock.call(classes[1]),
                mock.call(classes[2]),
            ]
        )

    @mock.patch.object(ClassSanitizer, "rename_class")
    def test_rename_classes_protects_single_element(self, mock_rename_class):
        classes = [
            ClassFactory.create(qname="_a", tag=Tag.ELEMENT),
            ClassFactory.create(qname="a", tag=Tag.COMPLEX_TYPE),
        ]
        self.sanitizer.rename_classes(classes)

        mock_rename_class.assert_called_once_with(classes[1])

    @mock.patch.object(ClassSanitizer, "rename_class_dependencies")
    def test_rename_class(self, mock_rename_class_dependencies):
        target = ClassFactory.create(qname="{foo}_a")
        self.sanitizer.container.add(target)
        self.sanitizer.container.add(ClassFactory.create())
        self.sanitizer.container.add(ClassFactory.create(qname="{foo}a_1"))
        self.sanitizer.container.add(ClassFactory.create(qname="{foo}A_2"))
        self.sanitizer.rename_class(target)

        self.assertEqual("{foo}_a_3", target.qname)
        self.assertEqual("_a", target.meta_name)

        mock_rename_class_dependencies.assert_has_calls(
            mock.call(item, "{foo}_a", "{foo}_a_3")
            for item in self.sanitizer.container.iterate()
        )

        self.assertEqual([target], self.container.data["{foo}_a_3"])
        self.assertEqual([], self.container.data["{foo}_a"])

    def test_rename_class_dependencies(self):
        attr_type = AttrTypeFactory.create("{foo}bar")

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

        self.sanitizer.rename_class_dependencies(target, "{foo}bar", "thug")
        dependencies = set(target.dependencies())
        self.assertNotIn("{foo}bar", dependencies)
        self.assertIn("thug", dependencies)

    def test_rename_attr_dependencies_with_default_enum(self):
        attr_type = AttrTypeFactory.create("{foo}bar")
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    types=[attr_type], default=f"@enum@{attr_type.qname}::member"
                ),
            ]
        )

        self.sanitizer.rename_class_dependencies(target, "{foo}bar", "thug")
        dependencies = set(target.dependencies())
        self.assertEqual("@enum@thug::member", target.attrs[0].default)
        self.assertNotIn("{foo}bar", dependencies)
        self.assertIn("thug", dependencies)

    def test_rename_attr_dependencies_with_choices(self):
        attr_type = AttrTypeFactory.create("{foo}bar")
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    choices=[
                        AttrFactory.create(types=[attr_type.clone()]),
                    ]
                )
            ]
        )

        self.sanitizer.rename_class_dependencies(target, "{foo}bar", "thug")
        dependencies = set(target.dependencies())
        self.assertNotIn("{foo}bar", dependencies)
        self.assertIn("thug", dependencies)

    @mock.patch.object(ClassSanitizer, "group_fields")
    def test_group_compound_fields(self, mock_group_fields):
        target = ClassFactory.elements(8)
        # First group repeating
        target.attrs[0].restrictions.choice = "1"
        target.attrs[1].restrictions.choice = "1"
        target.attrs[1].restrictions.max_occurs = 2
        # Second group repeating
        target.attrs[2].restrictions.choice = "2"
        target.attrs[3].restrictions.choice = "2"
        target.attrs[3].restrictions.max_occurs = 2
        # Third group optional
        target.attrs[4].restrictions.choice = "3"
        target.attrs[5].restrictions.choice = "3"

        self.sanitizer.group_compound_fields(target)
        mock_group_fields.assert_has_calls(
            [
                mock.call(target, target.attrs[0:2]),
                mock.call(target, target.attrs[2:4]),
            ]
        )

    def test_group_fields(self):
        target = ClassFactory.create(attrs=AttrFactory.list(2))
        target.attrs[0].restrictions.choice = "1"
        target.attrs[1].restrictions.choice = "1"
        target.attrs[0].restrictions.min_occurs = 10
        target.attrs[0].restrictions.max_occurs = 15
        target.attrs[1].restrictions.min_occurs = 5
        target.attrs[1].restrictions.max_occurs = 20

        expected = AttrFactory.create(
            name="attr_B_Or_attr_C",
            tag="Choice",
            index=0,
            types=[AttrTypeFactory.native(DataType.ANY_TYPE)],
            choices=[
                AttrFactory.create(
                    tag=target.attrs[0].tag,
                    name="attr_B",
                    types=target.attrs[0].types,
                ),
                AttrFactory.create(
                    tag=target.attrs[1].tag,
                    name="attr_C",
                    types=target.attrs[1].types,
                ),
            ],
        )
        expected_res = Restrictions(min_occurs=5, max_occurs=20)

        self.sanitizer.group_fields(target, list(target.attrs))
        self.assertEqual(1, len(target.attrs))
        self.assertEqual(expected, target.attrs[0])
        self.assertEqual(expected_res, target.attrs[0].restrictions)

    def test_group_fields_with_effective_choices_sums_occurs(self):
        target = ClassFactory.create(attrs=AttrFactory.list(2))
        target.attrs[0].restrictions.choice = "effective_1"
        target.attrs[1].restrictions.choice = "effective_1"
        target.attrs[0].restrictions.min_occurs = 1
        target.attrs[0].restrictions.max_occurs = 2
        target.attrs[1].restrictions.min_occurs = 3
        target.attrs[1].restrictions.max_occurs = 4

        expected_res = Restrictions(min_occurs=4, max_occurs=6)

        self.sanitizer.group_fields(target, list(target.attrs))
        self.assertEqual(1, len(target.attrs))
        self.assertEqual(expected_res, target.attrs[0].restrictions)

    def test_group_fields_limit_name(self):
        target = ClassFactory.create(attrs=AttrFactory.list(3))
        for attr in target.attrs:
            attr.restrictions.choice = "1"

        self.sanitizer.group_fields(target, list(target.attrs))

        self.assertEqual(1, len(target.attrs))
        self.assertEqual("attr_B_Or_attr_C_Or_attr_D", target.attrs[0].name)

        target = ClassFactory.create(attrs=AttrFactory.list(4))
        for attr in target.attrs:
            attr.restrictions.choice = "1"

        self.sanitizer.group_fields(target, list(target.attrs))
        self.assertEqual("choice", target.attrs[0].name)

        target = ClassFactory.create()
        attr = AttrFactory.element(restrictions=Restrictions(choice="1"))
        target.attrs.append(attr)
        target.attrs.append(attr.clone())
        self.sanitizer.group_fields(target, list(target.attrs))
        self.assertEqual("choice", target.attrs[0].name)

    def test_build_attr_choice(self):
        attr = AttrFactory.create(
            name="a", namespace="xsdata", default="123", help="help", fixed=True
        )
        attr.local_name = "aaa"
        attr.restrictions = Restrictions(
            required=True,
            prohibited=None,
            min_occurs=1,
            max_occurs=1,
            min_exclusive="1.1",
            min_inclusive="1",
            min_length=1,
            max_exclusive="1",
            max_inclusive="1.1",
            max_length=10,
            total_digits=333,
            fraction_digits=2,
            length=5,
            white_space="collapse",
            pattern=r"[A-Z]",
            explicit_timezone="+1",
            nillable=True,
            choice="abc",
            sequential=True,
        )
        expected_res = attr.restrictions.clone()
        expected_res.min_occurs = None
        expected_res.max_occurs = None
        expected_res.sequential = None

        actual = self.sanitizer.build_attr_choice(attr)

        self.assertEqual(attr.local_name, actual.name)
        self.assertEqual(attr.namespace, actual.namespace)
        self.assertEqual(attr.default, actual.default)
        self.assertEqual(attr.tag, actual.tag)
        self.assertEqual(attr.types, actual.types)
        self.assertEqual(expected_res, actual.restrictions)
        self.assertEqual(attr.help, actual.help)
        self.assertFalse(actual.fixed)
