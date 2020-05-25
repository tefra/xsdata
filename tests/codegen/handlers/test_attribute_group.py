from unittest import mock

from tests.factories import AttrFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeGroupHandler
from xsdata.codegen.models import Attr
from xsdata.codegen.utils import ClassUtils
from xsdata.exceptions import AnalyzerError


class AttributeGroupHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.processor = AttributeGroupHandler(container=container)

    @mock.patch.object(Attr, "is_group", new_callable=mock.PropertyMock)
    @mock.patch.object(AttributeGroupHandler, "process_attribute")
    def test_process(self, mock_process_attribute, mock_is_group):
        mock_is_group.side_effect = [
            False,
            True,
            False,
            True,
            True,
            True,
            False,
            False,
            False,
        ]
        target = ClassFactory.elements(2)

        self.processor.process(target)
        self.assertEqual(9, mock_is_group.call_count)

        mock_process_attribute.assert_has_calls(
            [mock.call(target, target.attrs[1]), mock.call(target, target.attrs[0]),]
        )

    @mock.patch.object(ClassUtils, "clone_attribute")
    @mock.patch.object(ClassContainer, "find")
    def test_process_attribute(self, mock_container_find, mock_clone_attribute):
        source = ClassFactory.elements(2)
        group_attr = AttrFactory.attribute_group(name="foo:bar")
        target = ClassFactory.create()
        target.attrs.append(group_attr)

        mock_container_find.return_value = source
        mock_clone_attribute.side_effect = lambda x, y, z: x.clone()

        self.processor.process_attribute(target, group_attr)

        self.assertEqual(2, len(target.attrs))
        self.assertIsNot(source.attrs[0], target.attrs[0])
        self.assertIsNot(source.attrs[1], target.attrs[1])
        self.assertNotIn(group_attr, target.attrs)

        mock_clone_attribute.assert_has_calls(
            [
                mock.call(source.attrs[0], group_attr.restrictions, "foo"),
                mock.call(source.attrs[1], group_attr.restrictions, "foo"),
            ]
        )

    @mock.patch.object(ClassContainer, "find")
    def test_process_attribute_with_circular_reference(self, mock_container_find):
        group_attr = AttrFactory.attribute_group(name="foo:bar")
        target = ClassFactory.create()
        target.attrs.append(group_attr)
        mock_container_find.return_value = target

        self.processor.process_attribute(target, group_attr)
        self.assertFalse(group_attr in target.attrs)

    def test_process_attribute_with_unknown_source(self):
        group_attr = AttrFactory.attribute_group(name="foo:bar")
        target = ClassFactory.create()
        target.attrs.append(group_attr)

        with self.assertRaises(AnalyzerError) as cm:
            self.processor.process_attribute(target, group_attr)

        self.assertEqual("Group attribute not found: `{foo}bar`", str(cm.exception))
