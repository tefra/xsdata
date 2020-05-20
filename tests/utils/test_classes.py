import sys
from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from tests.factories import RestrictionsFactory
from xsdata.models.codegen import Restrictions
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
                AttrTypeFactory.create(name=target.name, forward=True),
                AttrTypeFactory.create(name=target.name, forward=False),
                AttrTypeFactory.create(name="foobar"),
            ]
        )
        target.attrs.append(attr)

        ClassUtils.copy_inner_classes(source, target)  # Inner class matches target
        self.assertEqual(2, len(target.inner))

        for inner in target.inner:
            self.assertEqual(target.package, inner.package)
            self.assertEqual(target.module, inner.module)

        self.assertTrue(attr.types[0].circular)
        self.assertFalse(attr.types[1].circular)
        self.assertFalse(attr.types[2].circular)

    def test_copy_extension_type(self):
        extension = ExtensionFactory.create()
        target = ClassFactory.elements(2)
        target.extensions.append(extension)

        ClassUtils.copy_extension_type(target, extension)

        self.assertEqual(extension.type, target.attrs[0].types[1])
        self.assertEqual(extension.type, target.attrs[1].types[1])
        self.assertEqual(0, len(target.extensions))
