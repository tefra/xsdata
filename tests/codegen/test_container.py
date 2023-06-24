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

        self.assertEqual(2, len(container.data))
        self.assertEqual(3, len(list(container)))
        self.assertEqual(classes, list(container))

        actual = {
            step: [processor.__class__.__name__ for processor in processors]
            for step, processors in container.processors.items()
        }

        expected = {
            10: [
                "FlattenAttributeGroups",
            ],
            20: [
                "CalculateAttributePaths",
                "FlattenClassExtensions",
                "SanitizeEnumerationClass",
                "UpdateAttributesEffectiveChoice",
                "UnnestInnerClasses",
                "AddAttributeSubstitutions",
                "ProcessAttributeTypes",
                "MergeAttributes",
                "ProcessMixedContentClass",
            ],
            30: [
                "ResetAttributeSequences",
                "RenameDuplicateAttributes",
                "SanitizeAttributesDefaultValue",
            ],
            40: ["ValidateAttributesOverrides"],
            50: [
                "VacuumInnerClasses",
                "CreateCompoundFields",
                "ResetAttributeSequenceNumbers",
            ],
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
        self.container.step = Steps.FLATTEN

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
        self.container.step = Steps.FLATTEN

        self.assertEqual(first, self.container.find_inner(obj, "{a}a"))
        self.assertEqual(second, self.container.find_inner(obj, "{a}b"))
        mock_process_class.assert_called_once_with(first, Steps.FLATTEN)

    def test_first(self):
        obj = ClassFactory.create()
        self.container.add(obj)
        self.assertEqual(obj, self.container.first(obj.qname))

        with self.assertRaises(KeyError) as cm:
            self.container.first("aa")

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
            attrs=[AttrFactory.reference("enumeration", forward=True)],
            inner=[ClassFactory.enumeration(2, qname="enumeration")],
        )

        self.container.add(target)
        self.container.process_classes(Steps.FLATTEN)
        self.assertEqual(2, len(list(self.container)))

        for obj in self.container:
            self.assertEqual(Status.FLATTENED, obj.status)

    def test_filter_classes(self):
        complex_type = ClassFactory.elements(1)
        enum_1 = ClassFactory.enumeration(2)
        complex_type.attrs[0].types[0].reference = enum_1.ref

        simple_type = ClassFactory.simple_type()
        enum_2 = ClassFactory.enumeration(3)
        simple_type.attrs[0].types[0].reference = enum_2.ref

        element = ClassFactory.create(tag=Tag.ELEMENT, abstract=True)

        container = ClassContainer(config=GeneratorConfig())
        container.extend([complex_type, enum_1, enum_2, simple_type, element])

        expected = [complex_type, enum_1]
        container.filter_classes()
        self.assertEqual(expected, list(container))

    def test_remove_groups(self):
        classes = [
            ClassFactory.create(tag=Tag.ATTRIBUTE_GROUP),
            ClassFactory.create(tag=Tag.GROUP),
            ClassFactory.create(tag=Tag.ELEMENT),
        ]

        self.container.extend(classes)
        self.container.remove_groups()
        self.assertEqual(1, len(list(self.container)))
