import sys
from unittest import mock

from lxml.etree import QName

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from tests.factories import RestrictionsFactory
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Restrictions
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import SimpleType
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.classes import ClassUtils


class ClassUtilsTests(FactoryTestCase):
    def test_compare_attributes(self):
        source = ClassFactory.elements(2)
        self.assertEqual(2, ClassUtils.compare_attributes(source, source))

        target = ClassFactory.create()
        self.assertEqual(0, ClassUtils.compare_attributes(source, target))

        target.attrs = [attr.clone() for attr in source.attrs]
        self.assertEqual(2, ClassUtils.compare_attributes(source, target))

        source.attrs.append(AttrFactory.element())
        self.assertEqual(1, ClassUtils.compare_attributes(source, target))

        source.attrs = AttrFactory.list(3)
        self.assertEqual(0, ClassUtils.compare_attributes(source, target))

        self.assertEqual(0, ClassUtils.INCLUDES_NONE)
        self.assertEqual(1, ClassUtils.INCLUDES_SOME)
        self.assertEqual(2, ClassUtils.INCLUDES_ALL)

    @mock.patch.object(ClassUtils, "sanitize_attribute_name")
    @mock.patch.object(ClassUtils, "sanitize_attribute_sequence")
    @mock.patch.object(ClassUtils, "sanitize_restrictions")
    @mock.patch.object(ClassUtils, "sanitize_attribute")
    def test_sanitize_attributes(
        self,
        mock_sanitize_attribute,
        mock_sanitize_restrictions,
        mock_sanitize_attribute_sequence,
        mock_sanitize_attribute_name,
    ):

        target = ClassFactory.elements(3)
        inner = ClassFactory.elements(2)
        target.inner.append(inner)

        ClassUtils.sanitize_attributes(target)
        ClassUtils.sanitize_attributes(ClassFactory.create())

        self.assertEqual(5, mock_sanitize_attribute.call_count)
        mock_sanitize_attribute.assert_has_calls(
            [
                mock.call(target.attrs[0]),
                mock.call(target.attrs[1]),
                mock.call(target.attrs[2]),
                mock.call(target.inner[0].attrs[0]),
                mock.call(target.inner[0].attrs[1]),
            ]
        )
        mock_sanitize_restrictions.assert_has_calls(
            [
                mock.call(target.attrs[0].restrictions),
                mock.call(target.attrs[1].restrictions),
                mock.call(target.attrs[2].restrictions),
                mock.call(target.inner[0].attrs[0].restrictions),
                mock.call(target.inner[0].attrs[1].restrictions),
            ]
        )

        expected_second = [
            mock.call(target.attrs, 0),
            mock.call(target.attrs, 1),
            mock.call(target.attrs, 2),
            mock.call(target.inner[0].attrs, 0),
            mock.call(target.inner[0].attrs, 1),
        ]
        mock_sanitize_attribute_sequence.assert_has_calls(expected_second)
        mock_sanitize_attribute_name.assert_has_calls(expected_second)

    def test_sanitize_attribute(self):
        attr = AttrFactory.create(fixed=True)

        ClassUtils.sanitize_attribute(attr)
        self.assertTrue(attr.fixed)

        attr.restrictions.max_occurs = 2
        ClassUtils.sanitize_attribute(attr)
        self.assertFalse(attr.fixed)

        attr.restrictions.max_occurs = 1
        attr.restrictions.min_occurs = 0
        attr.fixed = True
        attr.default = "foo"
        ClassUtils.sanitize_attribute(attr)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

        xsi_attr = AttrFactory.xsi_type(default="xsi:integer", fixed=True)
        ClassUtils.sanitize_attribute(xsi_attr)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_sanitize_restrictions(self):
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
            ClassUtils.sanitize_restrictions(res)
            self.assertEqual(expected[idx], res.asdict())

    def test_sanitize_attribute_sequence(self):
        def len_sequential(target):
            return len([attr for attr in attrs if attr.restrictions.sequential])

        restrictions = Restrictions(max_occurs=2, sequential=True)
        attrs = [
            AttrFactory.create(restrictions=restrictions.clone()),
            AttrFactory.create(restrictions=restrictions.clone()),
        ]
        attrs_clone = [attr.clone() for attr in attrs]

        ClassUtils.sanitize_attribute_sequence(attrs, 0)
        self.assertEqual(2, len_sequential(attrs))

        attrs[0].restrictions.sequential = False
        ClassUtils.sanitize_attribute_sequence(attrs, 0)
        self.assertEqual(1, len_sequential(attrs))

        ClassUtils.sanitize_attribute_sequence(attrs, 1)
        self.assertEqual(0, len_sequential(attrs))

        attrs_clone[1].restrictions.sequential = False
        ClassUtils.sanitize_attribute_sequence(attrs_clone, 0)
        self.assertEqual(0, len_sequential(attrs_clone))

    def test_sanitize_attribute_name(self):
        attr_a = AttrFactory.create(name="kou:bar")
        attr_b = attr_a.clone()
        attr_a.namespace = "foo"

        ClassUtils.sanitize_attribute_name([attr_a, attr_b], 0)
        self.assertEqual("foo_bar", attr_a.name)

        ClassUtils.sanitize_attribute_name([attr_a, attr_b], 1)
        self.assertEqual("bar", attr_b.name)

        attr_c = attr_b.clone()
        ClassUtils.sanitize_attribute_name([attr_a, attr_b, attr_c], 2)
        self.assertEqual("bar", attr_b.name)

    def test_merge_duplicate_attributes(self):
        one = AttrFactory.attribute(fixed=True)
        one_clone = one.clone()
        restrictions = Restrictions(min_occurs=10, max_occurs=15)
        two = AttrFactory.element(restrictions=restrictions, fixed=True)
        two_clone = two.clone()
        two_clone.restrictions.min_occurs = 5
        two_clone.restrictions.max_occurs = 5
        two_clone_two = two.clone()
        two_clone_two.restrictions.min_occurs = 4
        two_clone_two.restrictions.max_occurs = 4
        three = AttrFactory.element()
        four = AttrFactory.enumeration()
        four_clone = four.clone()
        five = AttrFactory.element()
        five_clone = five.clone()
        five_clone_two = five.clone()

        target = ClassFactory.create(
            attrs=[
                one,
                one_clone,
                two,
                two_clone,
                two_clone_two,
                three,
                four,
                four_clone,
                five,
                five_clone,
                five_clone_two,
            ]
        )

        winners = [one, two, three, four, five]

        ClassUtils.merge_duplicate_attributes(target)
        self.assertEqual(winners, target.attrs)

        self.assertTrue(one.fixed)
        self.assertIsNone(one.restrictions.min_occurs)
        self.assertIsNone(one.restrictions.max_occurs)
        self.assertFalse(two.fixed)
        self.assertEqual(4, two.restrictions.min_occurs)
        self.assertEqual(24, two.restrictions.max_occurs)
        self.assertIsNone(three.restrictions.min_occurs)
        self.assertIsNone(three.restrictions.max_occurs)
        self.assertIsNone(four.restrictions.min_occurs)
        self.assertIsNone(four.restrictions.max_occurs)
        self.assertEqual(0, five.restrictions.min_occurs)
        self.assertEqual(3, five.restrictions.max_occurs)

    @mock.patch.object(ClassUtils, "copy_inner_classes")
    @mock.patch.object(ClassUtils, "clone_attribute")
    def test_copy_attributes(self, mock_clone_attribute, mock_copy_inner_classes):
        mock_clone_attribute.side_effect = lambda x, y, z: x.clone()
        target = ClassFactory.create(
            attrs=[AttrFactory.create(name="foo:a"), AttrFactory.create(name="b")]
        )
        source = ClassFactory.create(
            attrs=[
                AttrFactory.create(name="c", index=sys.maxsize),
                AttrFactory.create(name="a"),
                AttrFactory.create(name="boo:b"),
                AttrFactory.create(name="d"),
            ]
        )
        extension = ExtensionFactory.create(type=AttrTypeFactory.create(name="foo:foo"))
        target.extensions.append(extension)

        ClassUtils.copy_attributes(source, target, extension)

        self.assertEqual(["foo:a", "b", "d", "c"], [attr.name for attr in target.attrs])
        mock_copy_inner_classes.assert_called_once_with(source, target)
        mock_clone_attribute.assert_has_calls(
            [
                mock.call(source.attrs[0], extension.restrictions, "foo"),
                mock.call(source.attrs[3], extension.restrictions, "foo"),
            ]
        )

    def test_clone_attribute(self):
        attr = AttrFactory.create(
            restrictions=RestrictionsFactory.create(length=1),
            types=[
                AttrTypeFactory.create(name="foo:x"),
                AttrTypeFactory.create(name="y"),
                AttrTypeFactory.xs_int(),
            ],
        )
        restrictions = RestrictionsFactory.create(length=2)
        prefix = "foo"

        clone = ClassUtils.clone_attribute(attr, restrictions, prefix)

        self.assertEqual(["foo:x", "foo:y", "integer"], [x.name for x in clone.types])
        self.assertEqual(2, clone.restrictions.length)
        self.assertIsNot(attr, clone)

    def test_create_mixed_attribute(self):
        item = ClassFactory.create()
        ClassUtils.create_mixed_attribute(item)
        self.assertEqual(0, len(item.attrs))

        item = ClassFactory.elements(2, mixed=True)
        ClassUtils.create_mixed_attribute(item)
        expected = AttrFactory.create(
            name="content",
            index=0,
            types=[AttrType(name=DataType.ANY_TYPE.code, native=True)],
            tag=Tag.ANY,
            namespace="##any",
        )

        self.assertEqual(expected, item.attrs[0])
        self.assertEqual(3, len(item.attrs))

        ClassUtils.create_mixed_attribute(item)
        self.assertEqual(3, len(item.attrs))

    def test_create_default_attribute(self):
        extension = ExtensionFactory.create()
        item = ClassFactory.create(extensions=[extension])

        ClassUtils.create_default_attribute(item, extension)
        expected = AttrFactory.create(
            name="value",
            index=0,
            default=None,
            types=[extension.type],
            tag=Tag.EXTENSION,
        )

        self.assertEqual(1, len(item.attrs))
        self.assertEqual(0, len(item.extensions))
        self.assertEqual(expected, item.attrs[0])

    def test_create_default_attribute_with_any_type(self):
        extension = ExtensionFactory.create(
            type=AttrTypeFactory.xs_any(),
            restrictions=Restrictions(min_occurs=1, max_occurs=1, required=True),
        )
        item = ClassFactory.create(extensions=[extension])

        ClassUtils.create_default_attribute(item, extension)
        expected = AttrFactory.create(
            name="any_element",
            index=0,
            default=None,
            types=[extension.type.clone()],
            tag=Tag.ANY,
            namespace="##any",
            restrictions=Restrictions(min_occurs=1, max_occurs=1, required=True),
        )

        self.assertEqual(1, len(item.attrs))
        self.assertEqual(0, len(item.extensions))
        self.assertEqual(expected, item.attrs[0])

    def test_create_reference_attribute(self):
        item = ClassFactory.elements(1)
        actual = ClassUtils.create_reference_attribute(item, QName("foo"))

        expected = AttrFactory.create(
            name=item.name,
            index=0,
            default=None,
            types=[AttrType(name=f"{item.source_prefix}:{item.name}")],
            tag=item.type.__name__,
        )

        self.assertEqual(expected, actual)

        actual = ClassUtils.create_reference_attribute(item, item.source_qname("foo"))
        self.assertEqual(item.name, actual.types[0].name)

        item.source_namespace = None
        actual = ClassUtils.create_reference_attribute(item, QName("foo"))
        self.assertEqual(item.name, actual.types[0].name)

    @mock.patch.object(ClassUtils, "copy_inner_classes")
    def test_merge_attribute_type(self, mock_copy_inner_classes):
        source = ClassFactory.elements(1, name="Foobar")
        source.attrs[0].restrictions.max_length = 100
        source.attrs[0].restrictions.min_length = 1

        target = ClassFactory.elements(1)
        attr = target.attrs[0]
        attr.restrictions.min_length = 2
        attr.types.clear()
        attr.types.append(AttrTypeFactory.create(name=source.name))

        self.assertEqual("Foobar", attr.types[0].name)
        ClassUtils.merge_attribute_type(source, target, attr, attr.types[0])

        self.assertEqual("string", attr.types[0].name)
        self.assertEqual(Restrictions(min_length=2, max_length=100), attr.restrictions)
        mock_copy_inner_classes.assert_called_once_with(source, target)

    @mock.patch("xsdata.analyzer.logger.warning")
    def test_merge_attribute_type_when_source_attrs_is_not_one(
        self, mock_logger_warning
    ):
        source = ClassFactory.create()
        target = ClassFactory.elements(1)
        attr = target.attrs[0]
        ClassUtils.merge_attribute_type(source, target, attr, attr.types[0])

        self.assertEqual("string", attr.types[0].name)
        mock_logger_warning.assert_called_once_with(
            "Missing implementation: %s", source.type.__name__
        )

        attr.types = [AttrTypeFactory.create(name="foo")]
        source.attrs = AttrFactory.list(2)
        ClassUtils.merge_attribute_type(source, target, attr, attr.types[0])
        self.assertEqual("string", attr.types[0].name)

    def test_merge_redefined_classes_with_unique_classes(self):
        classes = ClassFactory.list(2)
        ClassUtils.merge_redefined_classes(classes)
        self.assertEqual(2, len(classes))

    @mock.patch.object(ClassUtils, "copy_attributes")
    def test_merge_redefined_classes_copies_attributes(self, mock_copy_attributes):
        class_a = ClassFactory.create()
        class_b = ClassFactory.create()
        class_c = class_a.clone()

        ext_a = ExtensionFactory.create(type=AttrTypeFactory.create(name=class_a.name))
        ext_str = ExtensionFactory.create(type=AttrTypeFactory.create(name="foo"))
        class_c.extensions.append(ext_a)
        class_c.extensions.append(ext_str)
        classes = [class_a, class_b, class_c]

        ClassUtils.merge_redefined_classes(classes)
        self.assertEqual(2, len(classes))

        mock_copy_attributes.assert_called_once_with(class_a, class_c, ext_a)

    def test_merge_redefined_classes_copies_extensions(self):
        class_a = ClassFactory.create()
        class_c = class_a.clone()

        type_int = AttrTypeFactory.xs_int()

        ext_a = ExtensionFactory.create(
            type=type_int,
            restrictions=Restrictions(max_inclusive=10, min_inclusive=1, required=True),
        )
        ext_c = ExtensionFactory.create(
            type=AttrTypeFactory.create(name=class_a.name),
            restrictions=Restrictions(max_inclusive=0, min_inclusive=-10),
        )

        class_a.extensions.append(ext_a)
        class_c.extensions.append(ext_c)
        classes = [class_a, class_c]
        expected = {"max_inclusive": 0, "min_inclusive": -10, "required": True}

        ClassUtils.merge_redefined_classes(classes)
        self.assertEqual(1, len(classes))
        self.assertEqual(1, len(classes[0].extensions))
        self.assertEqual(expected, classes[0].extensions[0].restrictions.asdict())

    def test_mark_abstract_duplicate_classes(self):
        one = ClassFactory.create(name="foo", abstract=True, type=Element)
        two = ClassFactory.create(name="foo", type=Element)
        three = ClassFactory.create(name="foo", type=ComplexType)
        four = ClassFactory.create(name="foo", type=SimpleType)

        ClassUtils.update_abstract_classes([one, two, three, four])

        self.assertTrue(one.abstract)  # Was abstract already
        self.assertFalse(two.abstract)  # Is an element
        self.assertTrue(three.abstract)  # Marked as abstract
        self.assertFalse(four.abstract)  # Is common
