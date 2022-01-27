from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.utils import ClassUtils
from xsdata.codegen.validator import ClassValidator
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class ClassValidatorTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.validator = ClassValidator(container=self.container)

    @mock.patch.object(ClassValidator, "merge_global_types")
    @mock.patch.object(ClassValidator, "handle_duplicate_types")
    @mock.patch.object(ClassValidator, "remove_invalid_classes")
    def test_process(
        self,
        mock_remove_invalid_classes,
        mock_handle_duplicate_types,
        mock_merge_global_types,
    ):
        first = ClassFactory.create()
        second = first.clone()
        third = ClassFactory.create()

        self.container.extend([first, second, third])
        self.validator.process()

        mock_remove_invalid_classes.assert_called_once_with([first, second])
        mock_handle_duplicate_types.assert_called_once_with([first, second])
        mock_merge_global_types.assert_called_once_with([first, second])

    def test_remove_invalid_classes(self):
        first = ClassFactory.create(
            extensions=[
                ExtensionFactory.create(AttrTypeFactory.native(DataType.BOOLEAN)),
                ExtensionFactory.create(AttrTypeFactory.create(qname="foo")),
            ]
        )
        second = ClassFactory.create(
            extensions=[
                ExtensionFactory.create(AttrTypeFactory.native(DataType.BOOLEAN))
            ]
        )
        third = ClassFactory.create()

        self.validator.container.extend([first, second, third])

        classes = [first, second, third]
        self.validator.remove_invalid_classes(classes)
        self.assertEqual([second, third], classes)

    @mock.patch("xsdata.codegen.mappers.definitions.logger.warning")
    def test_handle_duplicate_types(self, mock_warning):
        one = ClassFactory.create(tag=Tag.ELEMENT)
        two = one.clone()
        three = one.clone()
        four = ClassFactory.create(tag=Tag.ATTRIBUTE)
        classes = [one, two, three, four]

        self.validator.handle_duplicate_types(classes)
        self.assertEqual([three, four], classes)
        mock_warning.assert_called_once_with(
            "Duplicate type %s, will keep the last defined",
            "{xsdata}class_B",
        )

    @mock.patch.object(ClassValidator, "merge_redefined_type")
    def test_handle_duplicate_types_with_redefined_type(
        self, mock_merge_redefined_type
    ):
        one = ClassFactory.create(tag=Tag.ELEMENT)
        two = one.clone()
        three = one.clone()
        four = ClassFactory.create(tag=Tag.ATTRIBUTE)
        one.container = Tag.REDEFINE
        classes = [one, two, three, four]

        self.validator.handle_duplicate_types(classes)
        self.assertEqual([one, four], classes)
        mock_merge_redefined_type.assert_has_calls(
            [mock.call(two, one), mock.call(three, one)]
        )

    def test_merge_global_types(self):
        one = ClassFactory.create(
            qname="foo",
            tag=Tag.ELEMENT,
            namespace="a",
            help="b",
            substitutions=["a", "b"],
        )
        two = ClassFactory.create(qname="foo", tag=Tag.COMPLEX_TYPE, substitutions=[])
        three = ClassFactory.create(qname="foo", tag=Tag.SIMPLE_TYPE)

        classes = [one, two, three]
        self.validator.merge_global_types(classes)
        self.assertEqual(3, len(classes))

        classes = [one, three]
        self.validator.merge_global_types(classes)
        self.assertEqual(2, len(classes))

        classes = [two, three]
        self.validator.merge_global_types(classes)
        self.assertEqual(2, len(classes))

        classes = [one, two, three]
        one.attrs.append(AttrFactory.create)
        one.extensions.append(ExtensionFactory.reference(two.qname))

        self.validator.merge_global_types(classes)
        self.assertEqual(3, len(classes))

        one.attrs.clear()
        one.extensions.append(ExtensionFactory.reference("foo"))
        self.validator.merge_global_types(classes)
        self.assertEqual(3, len(classes))

        one.extensions.pop()
        self.validator.merge_global_types(classes)
        self.assertEqual(2, len(classes))
        self.assertIn(two, classes)
        self.assertIn(three, classes)
        self.assertEqual(one.namespace, two.namespace)
        self.assertEqual(one.help, two.help)
        self.assertEqual(one.substitutions, two.substitutions)
        self.assertEqual(2, len(one.substitutions))

    @mock.patch.object(ClassUtils, "copy_extensions")
    @mock.patch.object(ClassUtils, "copy_attributes")
    def test_merge_redefined_type_with_circular_extension(
        self, mock_copy_attributes, mock_copy_extensions
    ):
        source = ClassFactory.create()
        target = source.clone()

        ext_a = ExtensionFactory.create(AttrTypeFactory.create(qname=source.name))
        ext_str = ExtensionFactory.create(AttrTypeFactory.create(qname="foo"))
        target.extensions.append(ext_str)
        target.extensions.append(ext_a)

        self.validator.merge_redefined_type(source, target)

        mock_copy_attributes.assert_called_once_with(source, target, ext_a)
        mock_copy_extensions.assert_called_once_with(source, target, ext_a)

    @mock.patch.object(ClassUtils, "copy_group_attributes")
    def test_merge_redefined_type_with_circular_group(self, mock_copy_group_attributes):
        source = ClassFactory.create()
        target = source.clone()
        target.container = Tag.REDEFINE
        first_attr = AttrFactory.create()
        second_attr = AttrFactory.create(name=source.name)
        target.attrs.extend((first_attr, second_attr))

        self.validator.merge_redefined_type(source, target)

        mock_copy_group_attributes.assert_called_once_with(source, target, second_attr)

    def test_select_winner(self):
        classes = ClassFactory.list(2)
        self.assertEqual(-1, self.validator.select_winner(classes))

        classes[0].container = Tag.OVERRIDE
        self.assertEqual(0, self.validator.select_winner(classes))

        classes[0].container = Tag.SCHEMA
        classes[1].container = Tag.REDEFINE
        self.assertEqual(1, self.validator.select_winner(classes))
