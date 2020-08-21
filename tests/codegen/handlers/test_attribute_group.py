from unittest import mock

from tests.factories import AttrFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeGroupHandler
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.exceptions import AnalyzerValueError
from xsdata.models.xsd import AttributeGroup
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Group


class AttributeGroupHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.processor = AttributeGroupHandler(container=container)

    @mock.patch.object(Attr, "is_group", new_callable=mock.PropertyMock)
    @mock.patch.object(AttributeGroupHandler, "process_attribute")
    def test_process(self, mock_process_attribute, mock_is_group):
        mock_is_group.side_effect = [
            True,
            False,
            True,
            True,
            False,
            False,
        ]
        target = ClassFactory.elements(2)

        self.processor.process(target)
        self.assertEqual(6, mock_is_group.call_count)

        mock_process_attribute.assert_has_calls(
            [
                mock.call(target, target.attrs[0]),
                mock.call(target, target.attrs[0]),
                mock.call(target, target.attrs[1]),
            ]
        )

    @mock.patch.object(ClassUtils, "copy_group_attributes")
    def test_process_attribute_with_group(self, mock_copy_group_attributes):
        complex_bar = ClassFactory.create(qname="bar", type=ComplexType)
        group_bar = ClassFactory.create(qname="bar", type=Group)
        group_attr = AttrFactory.attribute_group(name="bar")
        target = ClassFactory.create()
        target.attrs.append(group_attr)

        self.processor.container.add(complex_bar)
        self.processor.container.add(group_bar)
        self.processor.container.add(target)

        self.processor.process_attribute(target, group_attr)
        mock_copy_group_attributes.assert_called_once_with(
            group_bar, target, group_attr
        )

    @mock.patch.object(ClassUtils, "copy_group_attributes")
    def test_process_attribute_with_attribute_group(self, mock_copy_group_attributes):
        complex_bar = ClassFactory.create(qname="bar", type=ComplexType)
        group_bar = ClassFactory.create(qname="bar", type=AttributeGroup)
        group_attr = AttrFactory.attribute_group(name="bar")
        target = ClassFactory.create()
        target.attrs.append(group_attr)

        self.processor.container.add(complex_bar)
        self.processor.container.add(group_bar)
        self.processor.container.add(target)

        self.processor.process_attribute(target, group_attr)
        mock_copy_group_attributes.assert_called_once_with(
            group_bar, target, group_attr
        )

    def test_process_attribute_with_circular_reference(self):
        group_attr = AttrFactory.attribute_group(name="bar")
        target = ClassFactory.create(qname="bar", type=Group)
        target.attrs.append(group_attr)

        target.status = Status.PROCESSING
        self.processor.container.add(target)

        self.processor.process_attribute(target, group_attr)
        self.assertFalse(group_attr in target.attrs)

    def test_process_attribute_with_unknown_source(self):
        group_attr = AttrFactory.attribute_group(name="bar")
        target = ClassFactory.create()
        target.attrs.append(group_attr)

        with self.assertRaises(AnalyzerValueError) as cm:
            self.processor.process_attribute(target, group_attr)

        self.assertEqual("Group attribute not found: `bar`", str(cm.exception))
