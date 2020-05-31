from unittest import mock

from lxml.etree import Element
from lxml.etree import QName

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.models.xsd import ComplexType


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
        class_b = ClassFactory.create(name="b", status=Status.PROCESSED)
        class_c = ClassFactory.enumeration(2, name="b", status=Status.PROCESSING)

        self.container.extend([class_a, class_b, class_c])

        self.assertIsNone(self.container.find(QName("nope")))
        self.assertEqual(class_a, self.container.find(class_a.source_qname()))
        self.assertEqual(class_b, self.container.find(class_b.source_qname()))
        self.assertEqual(
            class_c,
            self.container.find(class_b.source_qname(), lambda x: x.is_enumeration),
        )
        mock_process_class.assert_called_once_with(class_a)

    @mock.patch.object(ClassContainer, "process_class")
    def test_find_repeat_on_condition_and_not_processed(self, mock_process_class):
        first = ClassFactory.elements(2, name="a")
        second = ClassFactory.elements(2, name="a")
        self.container.extend([first, second])

        def process_class(x: Class):
            x.status = Status.PROCESSED
            if x is first:
                first.attrs.clear()

        mock_process_class.side_effect = process_class

        self.assertEqual(
            second,
            self.container.find(first.source_qname(), lambda x: len(x.attrs) == 2),
        )
