from unittest import mock

from lxml.etree import QName

from tests.factories import AttrFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeSubstitutionHandler
from xsdata.codegen.models import AttrType
from xsdata.codegen.utils import ClassUtils


class AttributeSubstitutionHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.processor = AttributeSubstitutionHandler(container=container)

    @mock.patch.object(AttributeSubstitutionHandler, "process_attribute")
    @mock.patch.object(AttributeSubstitutionHandler, "create_substitutions")
    def test_process(self, mock_create_substitutions, mock_process_attribute):
        def init_substitutions():
            self.processor.substitutions = {}

        mock_create_substitutions.side_effect = init_substitutions

        target = ClassFactory.create(
            attrs=[AttrFactory.enumeration(), AttrFactory.any(), AttrFactory.element(),]
        )

        self.processor.process(target)
        self.processor.process(ClassFactory.create())
        mock_process_attribute.assert_called_once_with(target, target.attrs[2])
        mock_create_substitutions.assert_called_once()

    @mock.patch.object(ClassUtils, "find_attribute")
    def test_process_attribute(self, mock_find_attribute):
        target = ClassFactory.elements(2)
        mock_find_attribute.side_effect = [-1, 2]

        first_attr = target.attrs[0]
        second_attr = target.attrs[1]
        first_attr.restrictions.max_occurs = 2

        attr_name = first_attr.name
        attr_qname = target.source_qname(attr_name)
        reference_attrs = AttrFactory.list(2)

        self.processor.create_substitutions()
        self.processor.substitutions[attr_qname] = reference_attrs
        self.processor.process_attribute(target, first_attr)

        self.assertEqual(4, len(target.attrs))

        self.assertEqual(reference_attrs[0], target.attrs[0])
        self.assertIsNot(reference_attrs[0], target.attrs[0])
        self.assertEqual(reference_attrs[1], target.attrs[3])
        self.assertIsNot(reference_attrs[1], target.attrs[3])
        self.assertEqual(2, target.attrs[0].restrictions.max_occurs)
        self.assertEqual(2, target.attrs[3].restrictions.max_occurs)

        self.processor.process_attribute(target, second_attr)
        self.assertEqual(4, len(target.attrs))

    @mock.patch.object(AttributeSubstitutionHandler, "create_substitution")
    def test_create_substitutions(self, mock_create_substitution):
        classes = [
            ClassFactory.create(substitutions=["foo", "bar"], abstract=True),
            ClassFactory.create(substitutions=["foo"], abstract=True),
        ]

        namespace = classes[0].source_namespace
        reference_attrs = AttrFactory.list(3)
        mock_create_substitution.side_effect = reference_attrs

        self.processor.container.extend(classes)
        self.processor.create_substitutions()

        expected = {
            QName(namespace, "foo"): [reference_attrs[0], reference_attrs[2]],
            QName(namespace, "bar"): [reference_attrs[1]],
        }
        self.assertEqual(expected, self.processor.substitutions)
        self.assertFalse(classes[0].abstract)
        self.assertFalse(classes[1].abstract)

        mock_create_substitution.assert_has_calls(
            [
                mock.call(classes[0], classes[0].source_qname("foo")),
                mock.call(classes[0], classes[0].source_qname("bar")),
                mock.call(classes[1], classes[1].source_qname("foo")),
            ]
        )

    def test_create_substitution(self):
        item = ClassFactory.elements(1)
        actual = self.processor.create_substitution(item, QName("foo"))

        expected = AttrFactory.create(
            name=item.name,
            index=0,
            default=None,
            types=[AttrType(name=f"{item.source_prefix}:{item.name}")],
            tag=item.type.__name__,
        )

        self.assertEqual(expected, actual)

        actual = self.processor.create_substitution(item, item.source_qname("foo"))
        self.assertEqual(item.name, actual.types[0].name)

        item.source_namespace = None
        actual = self.processor.create_substitution(item, QName("foo"))
        self.assertEqual(item.name, actual.types[0].name)
