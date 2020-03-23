from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from tests.factories import RestrictionsFactory
from xsdata.models.codegen import Restrictions
from xsdata.models.enums import TagType
from xsdata.utils.codegen import ClassUtils


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
                AttrFactory.create(name="c"),
                AttrFactory.create(name="a"),
                AttrFactory.create(name="boo:b"),
                AttrFactory.create(name="d"),
            ]
        )
        extension = ExtensionFactory.create(type=AttrTypeFactory.create(name="foo:foo"))
        target.extensions.append(extension)

        ClassUtils.copy_attributes(source, target, extension)

        self.assertEqual(["c", "foo:a", "b", "d"], [attr.name for attr in target.attrs])
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
            local_type=TagType.EXTENSION,
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
            name="##any_element",
            index=0,
            wildcard=True,
            default=None,
            types=[extension.type.clone()],
            local_type=TagType.ANY,
            restrictions=Restrictions(min_occurs=1, max_occurs=1, required=True),
        )

        self.assertEqual(1, len(item.attrs))
        self.assertEqual(0, len(item.extensions))
        self.assertEqual(expected, item.attrs[0])
