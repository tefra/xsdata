from unittest import mock

from lxml.etree import Element

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
            ClassFactory.create(qname="{xsdata}foo", type=Element),
            ClassFactory.create(qname="{xsdata}foo", type=ComplexType),
            ClassFactory.create(qname="{xsdata}foobar", type=ComplexType),
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
        class_a = ClassFactory.create(qname="a")
        class_b = ClassFactory.create(qname="b", status=Status.PROCESSED)
        class_c = ClassFactory.enumeration(2, qname="b", status=Status.PROCESSING)

        self.container.extend([class_a, class_b, class_c])

        self.assertIsNone(self.container.find("nope"))
        self.assertEqual(class_a, self.container.find(class_a.qname))
        self.assertEqual(class_b, self.container.find(class_b.qname))
        self.assertEqual(
            class_c, self.container.find(class_b.qname, lambda x: x.is_enumeration)
        )
        mock_process_class.assert_called_once_with(class_a)

    @mock.patch.object(ClassContainer, "process_class")
    def test_find_repeat_on_condition_and_not_processed(self, mock_process_class):
        first = ClassFactory.elements(2, qname="a")
        second = ClassFactory.elements(2, qname="a")
        self.container.extend([first, second])

        def process_class(x: Class):
            x.status = Status.PROCESSED
            if x is first:
                first.attrs.clear()

        mock_process_class.side_effect = process_class

        self.assertEqual(
            second, self.container.find(first.qname, lambda x: len(x.attrs) == 2)
        )
