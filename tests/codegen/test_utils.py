import sys
from typing import Generator
from unittest import mock

from xsdata.codegen.models import Restrictions
from xsdata.codegen.utils import ClassUtils
from xsdata.exceptions import CodeGenerationError
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class ClassUtilsTests(FactoryTestCase):
    @mock.patch.object(ClassUtils, "clean_inner_classes")
    def test_remove_attribute(self, mock_clean_inner_classes):

        target = ClassFactory.elements(1)
        attr = target.attrs[0]

        ClassUtils.remove_attribute(target, attr)
        self.assertEqual(0, len(target.attrs))

        mock_clean_inner_classes.assert_called_once_with(target)

    @mock.patch.object(ClassUtils, "is_orphan_inner")
    def test_clean_inner_classes(self, mock_is_orphan_inner):
        mock_is_orphan_inner.side_effect = [True, False, True]

        target = ClassFactory.create()
        target.inner.extend(ClassFactory.list(3))
        survivor = target.inner[1]

        ClassUtils.clean_inner_classes(target)

        self.assertEqual(1, len(target.inner))
        self.assertEqual(survivor, target.inner[0])

    def test_is_orphan_inner(self):

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
    def test_copy_attributes(self, mock_clone_attribute, mock_copy_inner_classes):
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
    def test_copy_group_attributes(self, mock_clone_attribute, mock_copy_inner_classes):
        mock_clone_attribute.side_effect = lambda x, y: x.clone()
        source = ClassFactory.elements(2)
        source.inner.append(ClassFactory.create())
        target = ClassFactory.elements(3)
        attrs = list(target.attrs)
        attrs[1].name = "bar"

        ClassUtils.copy_group_attributes(source, target, target.attrs[1])

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

    def test_copy_extensions(self):
        target = ClassFactory.create(extensions=ExtensionFactory.list(1))
        source = ClassFactory.create(extensions=ExtensionFactory.list(2))
        link_extension = ExtensionFactory.create()
        link_extension.restrictions.max_occurs = 2

        ClassUtils.copy_extensions(source, target, link_extension)

        self.assertEqual(3, len(target.extensions))
        self.assertEqual(2, target.extensions[1].restrictions.max_occurs)
        self.assertEqual(2, target.extensions[2].restrictions.max_occurs)

    def test_clone_attribute(self):
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
    def test_copy_inner_classes(self, mock_copy_inner_class):
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr = AttrFactory.create(types=AttrTypeFactory.list(3))

        ClassUtils.copy_inner_classes(source, target, attr)

        mock_copy_inner_class.assert_has_calls(
            [
                mock.call(source, target, attr, attr.types[0]),
                mock.call(source, target, attr, attr.types[1]),
                mock.call(source, target, attr, attr.types[2]),
            ]
        )

    def test_copy_inner_class(self):
        source = ClassFactory.create()
        inner = ClassFactory.create(qname="a", module="b", package="c")
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create(forward=True, qname=inner.qname)

        source.inner.append(inner)
        ClassUtils.copy_inner_class(source, target, attr, attr_type)

        self.assertEqual(1, len(target.inner))
        self.assertIsNot(inner, target.inner[0])
        self.assertEqual(target.package, target.inner[0].package)
        self.assertEqual(target.module, target.inner[0].module)
        self.assertEqual(inner.qname, target.inner[0].qname)

    def test_copy_inner_class_rename_simple_inner_type(self):
        source = ClassFactory.create()
        inner = ClassFactory.create(qname="{a}@value", module="b", package="c")
        target = ClassFactory.create()
        attr = AttrFactory.create(name="simple")
        attr_type = AttrTypeFactory.create(forward=True, qname=inner.qname)

        source.inner.append(inner)
        ClassUtils.copy_inner_class(source, target, attr, attr_type)

        self.assertEqual(1, len(target.inner))
        self.assertIsNot(inner, target.inner[0])
        self.assertEqual(target.package, target.inner[0].package)
        self.assertEqual(target.module, target.inner[0].module)
        self.assertEqual("{a}simple", target.inner[0].qname)
        self.assertEqual("{a}simple", attr_type.qname)

    def test_copy_inner_class_skip_non_forward_reference(self):
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create()
        ClassUtils.copy_inner_class(source, target, attr, attr_type)

        self.assertFalse(attr_type.circular)
        self.assertEqual(0, len(target.inner))

    def test_copy_inner_class_check_circular_reference(self):
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create(forward=True, qname=target.qname)
        source.inner.append(target)

        ClassUtils.copy_inner_class(source, target, attr, attr_type)
        self.assertTrue(attr_type.circular)
        self.assertEqual(0, len(target.inner))

    def test_copy_inner_class_with_missing_inner(self):
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create(forward=True, qname=target.qname)

        with self.assertRaises(CodeGenerationError):
            ClassUtils.copy_inner_class(source, target, attr, attr_type)

    def test_find_inner(self):
        obj = ClassFactory.create(qname="{a}parent")
        first = ClassFactory.create(qname="{a}a")
        second = ClassFactory.create(qname="{c}c")
        third = ClassFactory.enumeration(2, qname="{d}d")
        obj.inner.extend((first, second, third))

        with self.assertRaises(CodeGenerationError) as cm:
            self.assertIsNone(ClassUtils.find_inner(obj, "nope"))

        self.assertEqual("Missing inner class {a}parent.nope", str(cm.exception))
        self.assertEqual(first, ClassUtils.find_inner(obj, "{a}a"))
        self.assertEqual(second, ClassUtils.find_inner(obj, "{c}c"))
        self.assertEqual(third, ClassUtils.find_inner(obj, "{d}d"))

    def test_flatten(self):
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
            self.assertEqual("xsdata", obj.module)

        for attr in target.attrs:
            self.assertEqual(1, len(attr.types))
            self.assertFalse(attr.types[0].forward)

    @mock.patch.object(ClassUtils, "merge_attributes")
    def test_reduce(self, mock_merge_attributes):
        first = ClassFactory.elements(2)
        second = first.clone()
        second.attrs.append(AttrFactory.create())
        third = second.clone()
        third.attrs.append(AttrFactory.create())
        fourth = ClassFactory.create()

        actual = ClassUtils.reduce([first, second, third, fourth])

        self.assertEqual([third, fourth], list(actual))
        mock_merge_attributes.assert_has_calls(
            [
                mock.call(third, first),
                mock.call(third, second),
            ]
        )

    def test_merge_attributes(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(name="a", index=10),
                AttrFactory.element(name="b", index=1),
                AttrFactory.element(name="c", index=2),
                AttrFactory.attribute(name="id", index=0),
            ]
        )

        source = target.clone()

        target.attrs[0].restrictions.min_occurs = 2
        target.attrs[0].restrictions.max_occurs = 3

        source.attrs[1].restrictions.min_occurs = 3
        source.attrs[1].restrictions.max_occurs = 4
        source.attrs[3].restrictions.min_occurs = 3
        source.attrs[3].restrictions.max_occurs = 4
        source.attrs.append(AttrFactory.enumeration(name="d", index=4))

        ClassUtils.merge_attributes(target, source)

        names = ["id", "b", "c", "d", "a"]
        min_occurs = [0, 0, 0, None, 0]
        max_occurs = [4, 4, 1, None, 3]

        self.assertEqual(names, [x.name for x in target.attrs])
        self.assertEqual(min_occurs, [x.restrictions.min_occurs for x in target.attrs])
        self.assertEqual(max_occurs, [x.restrictions.max_occurs for x in target.attrs])

    def test_rename_attribute_by_preference(self):
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
