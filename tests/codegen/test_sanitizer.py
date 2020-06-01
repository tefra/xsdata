from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.codegen.sanitizer import ClassSanitizer
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag


class ClassSanitizerTest(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.sanitizer = ClassSanitizer(container=container)

    @mock.patch.object(ClassSanitizer, "process_class")
    def test_sanitize_classes(self, mock_process_class):
        classes = ClassFactory.list(2)
        self.sanitizer.container.extend(classes)
        self.sanitizer.process()
        mock_process_class.assert_has_calls(list(map(mock.call, classes)))

    @mock.patch.object(ClassSanitizer, "process_duplicate_attribute_names")
    @mock.patch.object(ClassSanitizer, "process_attribute_sequence")
    @mock.patch.object(ClassSanitizer, "process_attribute_name")
    @mock.patch.object(ClassSanitizer, "process_attribute_restrictions")
    @mock.patch.object(ClassSanitizer, "process_attribute_default")
    def test_process_class(
        self,
        mock_process_attribute_default,
        mock_process_attribute_restrictions,
        mock_process_attribute_name,
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
        mock_process_attribute_name.assert_has_calls(calls_without_target)
        mock_process_attribute_sequence.assert_has_calls(calls_with_target)
        mock_process_duplicate_attribute_names.assert_has_calls(
            [mock.call(target.inner[0].attrs), mock.call(target.attrs)]
        )

    def test_process_attribute_default_with_list_field(self):
        target = ClassFactory.create()
        attr = AttrFactory.create(fixed=True)
        attr.restrictions.max_occurs = 2
        self.sanitizer.process_attribute_default(target, attr)
        self.assertFalse(attr.fixed)

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
            fixed=True, default=2, name="xsi:type", namespace=Namespace.XSI.uri
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
    @mock.patch.object(ClassSanitizer, "promote_inner_class")
    @mock.patch.object(ClassSanitizer, "find_enum")
    def test_process_attribute_default_enum(
        self, mock_find_enum, mock_promote_inner_class, mock_logger_warning
    ):
        enum_one = ClassFactory.enumeration(1, name="root")
        enum_one.attrs[0].default = "1"
        enum_one.attrs[0].name = "one"
        enum_two = ClassFactory.enumeration(1, name="inner")
        enum_two.attrs[0].default = "2"
        enum_two.attrs[0].name = "two"
        enum_three = ClassFactory.enumeration(1, name="missing_member")

        mock_find_enum.side_effect = [
            None,
            enum_one,
            None,
            enum_two,
            enum_three,
        ]

        target = ClassFactory.create(
            name="target",
            attrs=[
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(),
                        AttrTypeFactory.create(name="foo"),
                    ],
                    default="1",
                ),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(),
                        AttrTypeFactory.create(name="bar", forward=True),
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

        self.assertEqual(["@enum@root::one", "@enum@inner::two", None], actual)
        mock_promote_inner_class.assert_called_once_with(target, enum_two)
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
        matching_inner = AttrTypeFactory.create("foobar", forward=True)
        missing_inner = AttrTypeFactory.create("barfoo", forward=True)
        enumeration = ClassFactory.enumeration(1, name="foo")
        inner = ClassFactory.enumeration(1, name="foobar")

        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    types=[
                        native_type,
                        matching_external,
                        missing_external,
                        matching_inner,
                        missing_inner,
                    ]
                )
            ],
            inner=[inner],
        )
        self.sanitizer.container.extend([target, enumeration])

        actual = self.sanitizer.find_enum(target, native_type)
        self.assertIsNone(actual)

        actual = self.sanitizer.find_enum(target, matching_external)
        self.assertEqual(enumeration, actual)

        actual = self.sanitizer.find_enum(target, missing_external)
        self.assertIsNone(actual)

        actual = self.sanitizer.find_enum(target, matching_inner)
        self.assertEqual(inner, actual)

        actual = self.sanitizer.find_enum(target, missing_inner)
        self.assertIsNone(actual)

    def test_process_attribute_restrictions(self):
        restrictions = [
            Restrictions(min_occurs=0, max_occurs=0, required=True),
            Restrictions(min_occurs=0, max_occurs=1, required=True),
            Restrictions(min_occurs=1, max_occurs=1, required=False),
            Restrictions(max_occurs=2, required=True),
            Restrictions(min_occurs=2, max_occurs=2, required=True),
        ]
        expected = [
            {},
            {},
            {"required": True},
            {"max_occurs": 2, "min_occurs": 0},
            {"max_occurs": 2, "min_occurs": 2},
        ]

        for idx, res in enumerate(restrictions):
            attr = AttrFactory.create(restrictions=res)
            self.sanitizer.process_attribute_restrictions(attr)
            self.assertEqual(expected[idx], res.asdict())

    def test_process_attribute_name(self):
        attr = AttrFactory.create(name="foo:a")

        self.sanitizer.process_attribute_name(attr)
        self.assertEqual("a", attr.name)

        attr.name = "1"
        self.sanitizer.process_attribute_name(attr)
        self.assertEqual("value_1", attr.name)

        attr.name = "foo_+-bar"
        self.sanitizer.process_attribute_name(attr)
        self.assertEqual("foo   bar", attr.name)

        attr.name = "+ -  *"
        self.sanitizer.process_attribute_name(attr)
        self.assertEqual("value", attr.name)

        attr = AttrFactory.enumeration(default="-20.55")
        self.sanitizer.process_attribute_name(attr)
        self.assertEqual("value_minus_-20.55", attr.name)

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
            AttrFactory.create(name="g", tag=Tag.ENUMERATION),
            AttrFactory.create(name="g", tag=Tag.ENUMERATION),
            AttrFactory.create(name="G", tag=Tag.ENUMERATION),
            AttrFactory.create(name="g_1", tag=Tag.ENUMERATION),
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
            "g",
            "g_2",
            "g_3",
            "g_1",
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

    def test_find_inner(self):
        inner_a = ClassFactory.create(name="a")
        inner_b = ClassFactory.enumeration(2)
        target = ClassFactory.create(inner=[inner_a, inner_b])

        self.assertEqual(
            inner_a,
            self.sanitizer.find_inner(target, condition=lambda x: x.name == "a"),
        )
        self.assertEqual(
            inner_b,
            self.sanitizer.find_inner(target, condition=lambda x: x.is_enumeration),
        )
        self.assertIsNone(
            self.sanitizer.find_inner(
                target, condition=lambda x: x.name == "a" and x.is_enumeration
            )
        )
