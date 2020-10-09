import sys
from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.models import Restrictions
from xsdata.codegen.utils import ClassUtils


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
        extension = ExtensionFactory.create(type=AttrTypeFactory.create(qname="foo"))
        target.extensions.append(extension)

        ClassUtils.copy_attributes(source, target, extension)

        self.assertEqual(["a", "b", "d", "c"], [attr.name for attr in target.attrs])
        mock_copy_inner_classes.assert_called_once_with(source, target)
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
        mock_copy_inner_classes.assert_called_once_with(source, target)
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
                AttrTypeFactory.xs_int(),
            ],
        )
        restrictions = Restrictions(length=2)

        clone = ClassUtils.clone_attribute(attr, restrictions)

        self.assertEqual(2, clone.restrictions.length)
        self.assertIsNot(attr, clone)

    def test_copy_inner_classes(self):
        source = ClassFactory.create(
            inner=ClassFactory.list(2, package="a", module="b")
        )
        target = ClassFactory.create()

        ClassUtils.copy_inner_classes(source, target)  # All good copy all
        self.assertEqual(2, len(target.inner))

        ClassUtils.copy_inner_classes(source, target)  # Inner classes exist skip
        self.assertEqual(2, len(target.inner))

        source.inner.append(target)

        attr = AttrFactory.create(
            types=[
                AttrTypeFactory.create(qname=target.name, forward=False),
                AttrTypeFactory.create(qname=target.name, forward=True),
                AttrTypeFactory.create(qname="foobar"),
            ]
        )
        target.attrs.append(attr)

        ClassUtils.copy_inner_classes(source, target)  # Inner class matches target
        self.assertEqual(2, len(target.inner))

        for inner in target.inner:
            self.assertEqual(target.package, inner.package)
            self.assertEqual(target.module, inner.module)

        self.assertFalse(attr.types[0].circular)
        self.assertTrue(attr.types[1].circular)
        self.assertFalse(attr.types[2].circular)
