from unittest import mock

from lxml.etree import Element

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import SimpleType


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
        self.assertEqual(
            [
                "AttributeGroupHandler",
                "ClassExtensionHandler",
                "AttributeEnumUnionHandler",
                "AttributeSubstitutionHandler",
                "AttributeTypeHandler",
                "AttributeMergeHandler",
                "AttributeMixedContentHandler",
                "AttributeMismatchHandler",
            ],
            [x.__class__.__name__ for x in container.processors],
        )

    @mock.patch.object(ClassContainer, "process_class")
    def test_find(self, mock_process_class):
        def process_class(x: Class):
            x.status = Status.PROCESSED

        class_a = ClassFactory.create(qname="a")
        class_b = ClassFactory.create(qname="b", status=Status.PROCESSED)
        class_c = ClassFactory.enumeration(2, qname="b", status=Status.PROCESSING)
        mock_process_class.side_effect = process_class
        self.container.extend([class_a, class_b, class_c])

        self.assertIsNone(self.container.find("nope"))
        self.assertEqual(class_a, self.container.find(class_a.qname))
        self.assertEqual(class_b, self.container.find(class_b.qname))
        self.assertEqual(
            class_c, self.container.find(class_b.qname, lambda x: x.is_enumeration)
        )
        mock_process_class.assert_called_once_with(class_a)

    @mock.patch.object(ClassContainer, "process_class")
    def test_find_inner(self, mock_process_class):
        obj = ClassFactory.create()
        first = ClassFactory.create(qname="{a}a")
        second = ClassFactory.enumeration(2, qname="{a}a")
        third = ClassFactory.create(qname="{c}c", status=Status.PROCESSED)
        fourth = ClassFactory.enumeration(2, qname="{d}d", status=Status.PROCESSING)
        obj.inner.extend((first, second, third, fourth))

        def process_class(x: Class):
            x.status = Status.PROCESSED

        def is_enum(x: Class):
            return x.is_enumeration

        mock_process_class.side_effect = process_class

        self.assertIsNone(self.container.find_inner(obj, "nope"))
        self.assertEqual(first, self.container.find_inner(obj, "a"))
        self.assertEqual(second, self.container.find_inner(obj, "a", is_enum))
        self.assertEqual(third, self.container.find_inner(obj, "c"))
        self.assertEqual(fourth, self.container.find_inner(obj, "d", is_enum))
        mock_process_class.assert_has_calls([mock.call(first), mock.call(second)])

    def test_process(self):
        target = ClassFactory.create(inner=ClassFactory.list(2))
        self.container.add(target)

        self.container.process_class(target)
        self.assertEqual(Status.PROCESSED, target.status)
        self.assertEqual(Status.PROCESSED, target.inner[0].status)
        self.assertEqual(Status.PROCESSED, target.inner[1].status)

    @mock.patch.object(Class, "should_generate", new_callable=mock.PropertyMock)
    def test_filter_classes(self, mock_class_should_generate):
        mock_class_should_generate.side_effect = [True, False, False, True, False]

        classes = ClassFactory.list(5)
        container = ClassContainer.from_list(classes)

        expected = [
            classes[0],
            classes[3],
        ]
        container.filter_classes()
        self.assertEqual(expected, container.class_list)

    @mock.patch.object(Class, "should_generate", new_callable=mock.PropertyMock)
    def test_filter_classes_with_only_simple_types(self, mock_class_should_generate):
        mock_class_should_generate.return_value = False
        classes = [ClassFactory.enumeration(2), ClassFactory.create(type=SimpleType)]
        container = ClassContainer.from_list(classes)
        container.filter_classes()

        self.assertEqual(classes, container.class_list)
