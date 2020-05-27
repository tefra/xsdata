from unittest import mock

from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Restrictions
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

        self.validator.merge_redefined_classes(classes)
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

        self.validator.merge_redefined_classes(classes)
        self.assertEqual(1, len(classes))
        self.assertEqual(1, len(classes[0].extensions))
        self.assertEqual(expected, classes[0].extensions[0].restrictions.asdict())
