from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.container import Steps
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class ClassContainerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())

    def test_initialize(self):
        classes = [
            ClassFactory.create(qname="{xsdata}foo", tag=Tag.ELEMENT),
            ClassFactory.create(qname="{xsdata}foo", tag=Tag.COMPLEX_TYPE),
            ClassFactory.create(qname="{xsdata}foobar", tag=Tag.COMPLEX_TYPE),
        ]
        config = GeneratorConfig()
        container = ClassContainer(config)
        container.extend(classes)

        expected = {
            "{xsdata}foo": classes[:2],
            "{xsdata}foobar": classes[2:],
        }

        self.assertEqual(2, len(container.data))
        self.assertEqual(3, len(list(container)))
        self.assertEqual(classes, list(container))

        actual = {
            step: [processor.__class__.__name__ for processor in processors]
            for step, processors in container.processors.items()
        }

        expected = {
            10: [
                "AttributeGroupHandler",
                "ClassExtensionHandler",
                "ClassEnumerationHandler",
                "AttributeSubstitutionHandler",
                "AttributeTypeHandler",
                "AttributeMergeHandler",
                "AttributeMixedContentHandler",
                "AttributeDefaultValidateHandler",
            ],
            20: [
                "AttributeEffectiveChoiceHandler",
                "AttributeDefaultValueHandler",
            ],
            30: [
                "AttributeOverridesHandler",
                "AttributeNameConflictHandler",
            ],
            40: ["ClassInnersHandler", "AttributeCompoundChoiceHandler"],
        }

        self.assertEqual(expected, actual)

    @mock.patch.object(ClassContainer, "process_class")
    def test_find(self, mock_process_class):
        def process_class(x: Class, step: int):
            x.status = Status.FLATTENED

        class_a = ClassFactory.create(qname="a")
        class_b = ClassFactory.create(qname="b", status=Status.FLATTENED)
        class_c = ClassFactory.enumeration(2, qname="b", status=Status.FLATTENING)
        mock_process_class.side_effect = process_class
        self.container.extend([class_a, class_b, class_c])

        self.assertIsNone(self.container.find("nope"))
        self.assertEqual(class_a, self.container.find(class_a.qname))
        self.assertEqual(class_b, self.container.find(class_b.qname))
        self.assertEqual(
            class_c, self.container.find(class_b.qname, lambda x: x.is_enumeration)
        )
        mock_process_class.assert_called_once_with(class_a, Steps.FLATTEN)

    @mock.patch.object(ClassContainer, "process_class")
    def test_find_inner(self, mock_process_class):
        obj = ClassFactory.create()
        first = ClassFactory.create(qname="{a}a")
        second = ClassFactory.create(qname="{a}b", status=Status.FLATTENED)
        obj.inner.extend((first, second))

        def process_class(x: Class, step: int):
            x.status = Status.FLATTENED

        mock_process_class.side_effect = process_class

        self.assertEqual(first, self.container.find_inner(obj, "{a}a"))
        self.assertEqual(second, self.container.find_inner(obj, "{a}b"))
        mock_process_class.assert_called_once_with(first, Steps.FLATTEN)

    def test_process_class(self):
        target = ClassFactory.create(
            inner=[ClassFactory.elements(2), ClassFactory.elements(1)]
        )
        self.container.add(target)

        self.container.process()
        self.assertEqual(Status.FINALIZED, target.status)
        self.assertEqual(Status.FINALIZED, target.inner[0].status)
        self.assertEqual(Status.FINALIZED, target.inner[1].status)

    def test_process_classes(self):
        target = ClassFactory.create(
            attrs=[AttrFactory.reference("enumeration")],
            inner=[ClassFactory.enumeration(2, qname="enumeration")],
        )

        self.container.add(target)
        self.container.process_classes(Steps.FLATTEN)
        self.assertEqual(2, len(list(self.container)))

        for obj in self.container:
            self.assertEqual(Status.FLATTENED, obj.status)

    @mock.patch.object(Class, "should_generate", new_callable=mock.PropertyMock)
    def test_filter_classes(self, mock_class_should_generate):
        mock_class_should_generate.side_effect = [True, False, False, True, False]

        classes = ClassFactory.list(5)
        container = ClassContainer(config=GeneratorConfig())
        container.extend(classes)

        expected = [
            classes[0],
            classes[3],
        ]
        container.filter_classes()
        self.assertEqual(expected, list(container))

    @mock.patch.object(Class, "should_generate", new_callable=mock.PropertyMock)
    def test_filter_classes_with_only_simple_types(self, mock_class_should_generate):
        mock_class_should_generate.return_value = False
        classes = [ClassFactory.enumeration(2), ClassFactory.simple_type()]
        container = ClassContainer(config=GeneratorConfig())
        container.extend(classes)
        container.filter_classes()

        self.assertEqual(classes, list(container))
