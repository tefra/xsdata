from unittest import mock

from lxml.etree import Element
from lxml.etree import QName

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.models.elements import ComplexType


class ClassContainerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.container = ClassContainer()

    def test_from_list(self):
        classes = [
            ClassFactory.create(type=Element, name="foo"),
            ClassFactory.create(type=ComplexType, name="foo"),
            ClassFactory.create(type=ComplexType, name="foobar"),
        ]
        container = ClassContainer.from_list(classes)

        expected = {
            "{xsdata}foo": classes[:2],
            "{xsdata}foobar": classes[2:],
        }

        self.assertEqual(2, len(container))
        self.assertEqual(expected, container)

    @mock.patch.object(ClassContainer, "process_class")
    def test_find(self, mock_process_class):
        class_a = ClassFactory.create(name="a")
        class_b = ClassFactory.create(name="b", processed=True)
        class_c = ClassFactory.enumeration(2, name="b", processed=True)

        self.container.extend([class_a, class_b, class_c])

        self.assertIsNone(self.container.find(QName("nope")))
        self.assertEqual(class_a, self.container.find(class_a.source_qname()))
        self.assertEqual(class_b, self.container.find(class_b.source_qname()))
        self.assertEqual(
            class_c,
            self.container.find(class_b.source_qname(), lambda x: x.is_enumeration),
        )
        mock_process_class.assert_called_once_with(class_a)
