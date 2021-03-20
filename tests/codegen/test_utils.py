import sys
from unittest import mock

from xsdata.codegen.models import Restrictions
from xsdata.codegen.utils import ClassUtils
from xsdata.exceptions import CodeGenerationError
from xsdata.models.enums import DataType
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class ClassUtilsTests(FactoryTestCase):
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
