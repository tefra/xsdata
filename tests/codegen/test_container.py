from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import Tag
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
        container = ClassContainer(config=GeneratorConfig())
        container.extend(classes)

        expected = {
            "{xsdata}foo": classes[:2],
            "{xsdata}foobar": classes[2:],
        }

        self.assertEqual(2, len(container.data))
        self.assertEqual(expected, container.data)
        self.assertEqual(
            [
                "AttributeGroupHandler",
                "ClassExtensionHandler",
                "ClassEnumerationHandler",
                "AttributeSubstitutionHandler",
                "AttributeTypeHandler",
                "AttributeMergeHandler",
                "AttributeMixedContentHandler",
                "AttributeDefaultValidateHandler",
                "AttributeOverridesHandler",
                "AttributeEffectiveChoiceHandler",
            ],
            [x.__class__.__name__ for x in container.pre_processors],
        )

        self.assertEqual(
            [
                "AttributeDefaultValueHandler",
                "AttributeRestrictionsHandler",
                "AttributeNameConflictHandler",
                "ClassBareInnerHandler",
            ],
            [x.__class__.__name__ for x in container.post_processors],
        )

        config = GeneratorConfig()
        config.output.compound_fields = True
        container = ClassContainer(config=config)

        self.assertEqual(
            [
                "AttributeCompoundChoiceHandler",
                "AttributeDefaultValueHandler",
                "AttributeRestrictionsHandler",
                "AttributeNameConflictHandler",
                "ClassBareInnerHandler",
            ],
            [x.__class__.__name__ for x in container.post_processors],
        )

    @mock.patch.object(ClassContainer, "pre_process_class")
    def test_find(self, mock_pre_process_class):
        def pre_process_class(x: Class):
            x.status = Status.PROCESSED

        class_a = ClassFactory.create(qname="a")
        class_b = ClassFactory.create(qname="b", status=Status.PROCESSED)
        class_c = ClassFactory.enumeration(2, qname="b", status=Status.PROCESSING)
        mock_pre_process_class.side_effect = pre_process_class
        self.container.extend([class_a, class_b, class_c])

        self.assertIsNone(self.container.find("nope"))
        self.assertEqual(class_a, self.container.find(class_a.qname))
        self.assertEqual(class_b, self.container.find(class_b.qname))
        self.assertEqual(
            class_c, self.container.find(class_b.qname, lambda x: x.is_enumeration)
        )
        mock_pre_process_class.assert_called_once_with(class_a)

    @mock.patch.object(ClassContainer, "pre_process_class")
    def test_find_inner(self, mock_pre_process_class):
        obj = ClassFactory.create()
        first = ClassFactory.create(qname="{a}a")
        second = ClassFactory.create(qname="{a}b", status=Status.PROCESSED)
        obj.inner.extend((first, second))

        def pre_process_class(x: Class):
            x.status = Status.PROCESSED

        mock_pre_process_class.side_effect = pre_process_class

        self.assertEqual(first, self.container.find_inner(obj, "{a}a"))
        self.assertEqual(second, self.container.find_inner(obj, "{a}b"))
        mock_pre_process_class.assert_called_once_with(first)

    def test_pre_process_class(self):
        target = ClassFactory.create(
            inner=[ClassFactory.elements(2), ClassFactory.elements(1)]
        )
        self.container.add(target)

        self.container.process()
        self.assertEqual(Status.PROCESSED, target.status)
        self.assertEqual(Status.PROCESSED, target.inner[0].status)
        self.assertEqual(Status.PROCESSED, target.inner[1].status)

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
        self.assertEqual(expected, container.class_list)

    @mock.patch.object(Class, "should_generate", new_callable=mock.PropertyMock)
    def test_filter_classes_with_only_simple_types(self, mock_class_should_generate):
        mock_class_should_generate.return_value = False
        classes = [ClassFactory.enumeration(2), ClassFactory.simple_type()]
        container = ClassContainer(config=GeneratorConfig())
        container.extend(classes)
        container.filter_classes()

        self.assertEqual(classes, container.class_list)
