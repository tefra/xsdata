import sys
from collections.abc import Generator
from unittest import mock

from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.models import Restrictions, Status
from xsdata.codegen.utils import ClassUtils
from xsdata.models.enums import DataType, Tag
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    ExtensionFactory,
    FactoryTestCase,
)


class ClassUtilsTests(FactoryTestCase):
    def test_find_value_attr(self) -> None:
        target = ClassFactory.create()
        with self.assertRaises(CodegenError):
            ClassUtils.find_value_attr(target)

        target.attrs.append(AttrFactory.element())
        with self.assertRaises(CodegenError):
            ClassUtils.find_value_attr(target)

        target.attrs.append(AttrFactory.extension())
        actual = ClassUtils.find_value_attr(target)
        self.assertEqual(target.attrs[1], actual)

    def test_remove_attribute(self) -> None:
        target = ClassFactory.elements(1)
        attr = target.attrs[0]

        ClassUtils.remove_attribute(target, attr)
        self.assertEqual(0, len(target.attrs))

    @mock.patch.object(ClassUtils, "is_orphan_inner")
    def test_clean_inner_classes(self, mock_is_orphan_inner) -> None:
        mock_is_orphan_inner.side_effect = [True, False, True]

        target = ClassFactory.create()
        target.inner.extend(ClassFactory.list(3))
        survivor = target.inner[1]

        ClassUtils.clean_inner_classes(target)

        self.assertEqual(1, len(target.inner))
        self.assertEqual(survivor, target.inner[0])

    def test_is_orphan_inner(self) -> None:
        inner = ClassFactory.create(qname="thug")
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(qname="bar"),
                        AttrTypeFactory.create(qname="foo"),
                    ]
                )
            ]
        )
        self.assertTrue(ClassUtils.is_orphan_inner(target, inner))

        target.attrs[0].types[1].qname = "thug"
        target.attrs[0].types[1].forward = True

        self.assertFalse(ClassUtils.is_orphan_inner(target, inner))

    @mock.patch.object(ClassUtils, "copy_inner_classes")
    @mock.patch.object(ClassUtils, "clone_attribute")
    def test_copy_attributes(
        self, mock_clone_attribute, mock_copy_inner_classes
    ) -> None:
        mock_clone_attribute.side_effect = lambda x, y: x.clone()
        target = ClassFactory.create(
            attrs=[AttrFactory.create(name="a"), AttrFactory.create(name="b")]
        )
        source = ClassFactory.create(
            attrs=[
                AttrFactory.create(name="c", index=sys.maxsize),
                AttrFactory.create(name="a"),
                AttrFactory.create(name="b"),
                AttrFactory.create(name="d"),
            ]
        )
        extension = ExtensionFactory.create(AttrTypeFactory.create(qname="foo"))
        target.extensions.append(extension)

        ClassUtils.copy_attributes(source, target, extension)

        self.assertEqual(["a", "b", "d", "c"], [attr.name for attr in target.attrs])

        mock_copy_inner_classes.assert_has_calls(
            [
                mock.call(source, target, source.attrs[0]),
                mock.call(source, target, source.attrs[3]),
            ]
        )
        mock_clone_attribute.assert_has_calls(
            [
                mock.call(source.attrs[0], extension.restrictions),
                mock.call(source.attrs[3], extension.restrictions),
            ]
        )

    @mock.patch.object(ClassUtils, "copy_inner_classes")
    @mock.patch.object(ClassUtils, "clone_attribute")
    def test_copy_group_attributes(
        self, mock_clone_attribute, mock_copy_inner_classes
    ) -> None:
        mock_clone_attribute.side_effect = lambda x, y: x.clone()
        source = ClassFactory.elements(2)
        source.inner.append(ClassFactory.create())
        target = ClassFactory.elements(3)
        attrs = target.attrs.copy()
        attrs[1].name = "bar"
        attr = target.attrs[1]

        ClassUtils.copy_group_attributes(source, target, attr)

        self.assertEqual(4, len(target.attrs))
        self.assertEqual(source.attrs[0], target.attrs[1])
        self.assertEqual(source.attrs[1], target.attrs[2])

        mock_copy_inner_classes.assert_has_calls(
            [
                mock.call(source, target, source.attrs[0]),
                mock.call(source, target, source.attrs[1]),
            ]
        )
        mock_clone_attribute.assert_has_calls(
            [
                mock.call(source.attrs[0], attrs[1].restrictions),
                mock.call(source.attrs[1], attrs[1].restrictions),
            ]
        )

    def test_copy_extensions(self) -> None:
        target = ClassFactory.create(extensions=ExtensionFactory.list(1))
        source = ClassFactory.create(extensions=ExtensionFactory.list(2))
        link_extension = ExtensionFactory.create()
        link_extension.restrictions.max_occurs = 2

        ClassUtils.copy_extensions(source, target, link_extension)

        self.assertEqual(3, len(target.extensions))
        self.assertEqual(2, target.extensions[1].restrictions.max_occurs)
        self.assertEqual(2, target.extensions[2].restrictions.max_occurs)

    def test_clone_attribute(self) -> None:
        attr = AttrFactory.create(
            restrictions=Restrictions(length=1),
            types=[
                AttrTypeFactory.create(qname="x"),
                AttrTypeFactory.create(qname="y"),
                AttrTypeFactory.native(DataType.INT),
            ],
        )
        restrictions = Restrictions(length=2)

        clone = ClassUtils.clone_attribute(attr, restrictions)

        self.assertEqual(2, clone.restrictions.length)
        self.assertIsNot(attr, clone)

    @mock.patch.object(ClassUtils, "copy_inner_class")
    def test_copy_inner_classes(self, mock_copy_inner_class) -> None:
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr = AttrFactory.create(types=AttrTypeFactory.list(3))

        ClassUtils.copy_inner_classes(source, target, attr)

        mock_copy_inner_class.assert_has_calls(
            [
                mock.call(source, target, attr.types[0]),
                mock.call(source, target, attr.types[1]),
                mock.call(source, target, attr.types[2]),
            ]
        )

    def test_copy_inner_class(self) -> None:
        source = ClassFactory.create()
        inner = ClassFactory.create(
            qname="a", module="b", package="c", status=Status.FLATTENED
        )
        target = ClassFactory.create()
        attr_type = AttrTypeFactory.create(forward=True, qname=inner.qname)

        source.inner.append(inner)
        ClassUtils.copy_inner_class(source, target, attr_type)

        self.assertEqual(1, len(target.inner))
        self.assertIsNot(inner, target.inner[0])
        self.assertEqual(target.package, target.inner[0].package)
        self.assertEqual(target.module, target.inner[0].module)
        self.assertEqual(inner.qname, target.inner[0].qname)
        self.assertIs(Status.RAW, target.inner[0].status)
        self.assertIs(Status.FLATTENED, inner.status)

    def test_copy_inner_class_check_circular_reference(self) -> None:
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr_type = AttrTypeFactory.create(forward=True, qname=target.qname)
        source.inner.append(target)

        ClassUtils.copy_inner_class(source, target, attr_type)
        self.assertTrue(attr_type.circular)
        self.assertEqual(0, len(target.inner))

    def test_copy_inner_class_with_missing_inner(self) -> None:
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr_type = AttrTypeFactory.create(forward=True, qname=target.qname)

        with self.assertRaises(CodegenError):
            ClassUtils.copy_inner_class(source, target, attr_type)

    def test_flatten(self) -> None:
        target = ClassFactory.create(
            qname="{xsdata}root", attrs=AttrFactory.list(3), inner=ClassFactory.list(2)
        )

        for attr in target.attrs:
            attr.types.extend([x.clone() for x in attr.types])
            for tp in attr.types:
                tp.forward = True

        result = ClassUtils.flatten(target, "xsdata")
        actual = list(result)

        self.assertIsInstance(result, Generator)
        self.assertEqual(3, len(actual))

        for obj in actual:
            self.assertEqual("xsdata", obj.location)

        for attr in target.attrs:
            self.assertEqual(1, len(attr.types))
            self.assertFalse(attr.types[0].forward)

    def test_reduce_classes(self) -> None:
        class_a = ClassFactory.elements(3)
        class_a_clone = class_a.clone()
        class_a_clone.mixed = True
        class_a.attrs.pop()
        class_b = ClassFactory.elements(2)

        result = ClassUtils.reduce_classes([class_a, class_b, class_a_clone])

        self.assertEqual(2, len(result))
        self.assertTrue(result[0].mixed)

        self.assertEqual(
            ["attr_B", "attr_C", "attr_D"], [x.name for x in result[0].attrs]
        )
        self.assertEqual(["attr_E", "attr_F"], [x.name for x in result[1].attrs])

    def test_reduce_attributes(self) -> None:
        restrictions = Restrictions(min_occurs=1, max_occurs=1)
        attr_a = AttrFactory.create(name="a", restrictions=restrictions.clone())
        attr_b = AttrFactory.create(name="b", restrictions=restrictions.clone())
        attr_c = AttrFactory.create(name="c", restrictions=restrictions.clone())
        attr_d = AttrFactory.create(name="d", restrictions=restrictions.clone())

        first = ClassFactory.create(qname="alphabet", attrs=[attr_b, attr_c, attr_d])
        second = ClassFactory.create(qname="alphabet", attrs=[attr_a, attr_b])

        result = ClassUtils.reduce_attributes([first, second])
        expected_names = ["a", "b", "c", "d"]
        self.assertEqual(expected_names, [x.name for x in result])

        self.assertEqual(0, result[0].restrictions.min_occurs)
        self.assertEqual(1, result[1].restrictions.min_occurs)
        self.assertEqual(0, result[2].restrictions.min_occurs)
        self.assertEqual(0, result[3].restrictions.min_occurs)

    def test_merge_attributes(self) -> None:
        a = AttrFactory.native(DataType.INT, name="a")
        c = AttrFactory.native(DataType.FLOAT, name="c")

        ClassUtils.merge_attributes(a, c)
        self.assertEqual(["int", "float"], [x.name for x in a.types])

        self.assertEqual(0, a.restrictions.min_occurs)
        self.assertEqual(1, a.restrictions.max_occurs)
        self.assertIsNone(a.restrictions.sequence)

        c.restrictions.min_occurs = 2
        a.restrictions.sequence = 1
        a.restrictions.max_occurs = 4

        ClassUtils.merge_attributes(c, a)
        self.assertEqual(0, c.restrictions.min_occurs)
        self.assertEqual(4, c.restrictions.max_occurs)
        self.assertEqual(1, c.restrictions.sequence)

    def test_rename_duplicate_attributes(self) -> None:
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
        target = ClassFactory.create(attrs=attrs)

        ClassUtils.rename_duplicate_attributes(target)
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

    def test_rename_attribute_by_preference(self) -> None:
        one = AttrFactory.create(name="a", tag=Tag.ELEMENT)
        two = AttrFactory.create(name="a", tag=Tag.ATTRIBUTE)

        ClassUtils.rename_attribute_by_preference(one, two)
        self.assertEqual("a", one.name)
        self.assertEqual("a_Attribute", two.name)

        one = AttrFactory.create(name="a", tag=Tag.ELEMENT)
        two = AttrFactory.create(name="a", tag=Tag.ELEMENT, namespace="foo")
        ClassUtils.rename_attribute_by_preference(one, two)
        self.assertEqual("a", one.name)
        self.assertEqual("foo_a", two.name)

        one = AttrFactory.create(name="a", tag=Tag.ELEMENT, namespace="foo")
        two = AttrFactory.create(name="a", tag=Tag.ELEMENT)
        ClassUtils.rename_attribute_by_preference(one, two)
        self.assertEqual("foo_a", one.name)
        self.assertEqual("a", two.name)

        one = AttrFactory.create(name="a", tag=Tag.ELEMENT)
        two = AttrFactory.create(name="a", tag=Tag.ELEMENT)
        ClassUtils.rename_attribute_by_preference(one, two)
        self.assertEqual("a_Element", one.name)
        self.assertEqual("a", two.name)

    def test_filter_types(self) -> None:
        xs_string = AttrTypeFactory.native(DataType.STRING)
        xs_error = AttrTypeFactory.native(DataType.ERROR)
        xs_any = AttrTypeFactory.native(DataType.ANY_TYPE)

        types = [
            xs_string.clone(),
            xs_string.clone(),
            xs_string.clone(),
            xs_error.clone(),
        ]

        actual = ClassUtils.filter_types(types)

        self.assertEqual(1, len(actual))

        types.append(xs_any)
        actual = ClassUtils.filter_types(types)
        self.assertEqual(1, len(actual))
        self.assertEqual(xs_string, actual[0])

        actual = ClassUtils.filter_types([])
        self.assertEqual(xs_string, actual[0])

        types = [xs_any]
        actual = ClassUtils.filter_types(types)
        self.assertEqual(1, len(actual))

    def test_find_nested(self) -> None:
        a = ClassFactory.create(qname="a")
        b = ClassFactory.create(qname="b")
        c = ClassFactory.create(qname="c")

        a.inner.append(b)
        b.inner.append(c)
        c.parent = b
        b.parent = a

        self.assertEqual(a, ClassUtils.find_nested(a, "a"))
        self.assertEqual(b, ClassUtils.find_nested(a, "b"))
        self.assertEqual(b, ClassUtils.find_nested(c, "b"))
        self.assertEqual(a, ClassUtils.find_nested(c, "a"))

        a2 = ClassFactory.create(qname="a")
        c.inner.append(a2)
        a2.parent = c

        # Breadth-first search
        self.assertEqual(a2, ClassUtils.find_nested(c, "a"))

        with self.assertRaises(CodegenError):
            ClassUtils.find_nested(a, "nope")
