from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.utils import ClassUtils
from xsdata.codegen.validator import ClassValidator
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import SimpleType


class ClassValidatorTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.validator = ClassValidator(container=container)

    @mock.patch.object(ClassValidator, "update_abstract_classes")
    @mock.patch.object(ClassValidator, "merge_redefined_classes")
    @mock.patch.object(ClassValidator, "remove_invalid_classes")
    def test_handle_duplicate_classes(
        self,
        mock_remove_invalid_classes,
        mock_merge_redefined_classes,
        mock_update_abstract_classes,
    ):
        first = ClassFactory.create()
        second = first.clone()
        third = ClassFactory.create()

        self.validator.container.extend([first, second, third])
        self.validator.process()

        mock_remove_invalid_classes.assert_called_once_with([first, second])
        mock_merge_redefined_classes.assert_called_once_with([first, second])
        mock_update_abstract_classes.assert_called_once_with([first, second])

    def test_remove_invalid_classes(self):
        first = ClassFactory.create(
            extensions=[
                ExtensionFactory.create(type=AttrTypeFactory.xs_bool()),
                ExtensionFactory.create(type=AttrTypeFactory.create(name="foo")),
            ]
        )
        second = ClassFactory.create(
            extensions=[ExtensionFactory.create(type=AttrTypeFactory.xs_bool()),]
        )
        third = ClassFactory.create()

        self.validator.container.extend([first, second, third])

        classes = [first, second, third]
        self.validator.remove_invalid_classes(classes)
        self.assertEqual([second, third], classes)

    def test_update_abstract_classes(self):
        one = ClassFactory.create(name="foo", abstract=True, type=Element)
        two = ClassFactory.create(name="foo", type=Element)
        three = ClassFactory.create(name="foo", type=ComplexType)
        four = ClassFactory.create(name="foo", type=SimpleType)

        self.validator.update_abstract_classes([one, two, three, four])

        self.assertTrue(one.abstract)  # Was abstract already
        self.assertFalse(two.abstract)  # Is an element
        self.assertTrue(three.abstract)  # Marked as abstract
        self.assertFalse(four.abstract)  # Is common

    def test_merge_redefined_classes_selects_last_defined_class(self):
        class_a = ClassFactory.create()
        class_b = ClassFactory.create()
        class_c = class_a.clone()
        classes = [class_a, class_b, class_c]

        self.validator.merge_redefined_classes(classes)
        self.assertEqual(2, len(classes))
        self.assertIn(class_b, classes)
        self.assertIn(class_c, classes)

    @mock.patch.object(ClassUtils, "copy_extensions")
    @mock.patch.object(ClassUtils, "copy_attributes")
    def test_merge_redefined_classes_with_circular_extension(
        self, mock_copy_attributes, mock_copy_extensions
    ):
        class_a = ClassFactory.create()
        class_b = ClassFactory.create()
        class_c = class_a.clone()

        ext_a = ExtensionFactory.create(type=AttrTypeFactory.create(name=class_a.name))
        ext_str = ExtensionFactory.create(type=AttrTypeFactory.create(name="foo"))
        class_c.extensions.append(ext_str)
        class_c.extensions.append(ext_a)
        classes = [class_a, class_b, class_c]

        self.validator.merge_redefined_classes(classes)
        self.assertEqual(2, len(classes))

        mock_copy_attributes.assert_called_once_with(class_a, class_c, ext_a)
        mock_copy_extensions.assert_called_once_with(class_a, class_c, ext_a)

    @mock.patch.object(ClassUtils, "copy_group_attributes")
    def test_merge_redefined_classes_with_circular_group(
        self, mock_copy_group_attributes
    ):
        class_a = ClassFactory.create()
        class_c = class_a.clone()
        first_attr = AttrFactory.create()
        second_attr = AttrFactory.create(name=class_a.name)
        class_c.attrs.extend((first_attr, second_attr))

        classes = [class_a, class_c]
        self.validator.merge_redefined_classes(classes)
        self.assertEqual(1, len(classes))

        mock_copy_group_attributes.assert_called_once_with(
            class_a, class_c, second_attr
        )
