from xsdata.codegen.container import ClassContainer
from xsdata.codegen.container import Steps
from xsdata.codegen.handlers import ResetAttributeSequenceNumbers
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class ResetAttributeSequencesTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.config = GeneratorConfig()
        self.container = ClassContainer(config=self.config)
        self.container.step = Steps.FINALIZE
        self.processor = ResetAttributeSequenceNumbers(container=self.container)

    def test_process_without_sequence_fields(self):
        target = ClassFactory.elements(2)
        self.processor.process(target)

    def test_process_without_parent_class(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(restrictions=Restrictions(sequence=100)),
                AttrFactory.create(restrictions=Restrictions(sequence=100)),
                AttrFactory.create(),
                AttrFactory.create(restrictions=Restrictions(sequence=101)),
                AttrFactory.create(restrictions=Restrictions(sequence=101)),
            ]
        )
        self.processor.process(target)

        actual = [x.restrictions.sequence for x in target.attrs]
        expected = [1, 1, None, 2, 2]
        self.assertEqual(expected, actual)

    def test_process_with_parent_classes(self):
        target = ClassFactory.create(
            status=Status.FINALIZING,
            attrs=[
                AttrFactory.create(restrictions=Restrictions(sequence=100)),
                AttrFactory.create(restrictions=Restrictions(sequence=100)),
                AttrFactory.create(),
                AttrFactory.create(restrictions=Restrictions(sequence=101)),
                AttrFactory.create(restrictions=Restrictions(sequence=101)),
            ],
        )

        parent_a = ClassFactory.create(
            status=Status.RESOLVED,
            attrs=[
                AttrFactory.create(restrictions=Restrictions(sequence=102)),
            ],
        )

        parent_b = ClassFactory.create(
            status=Status.RESOLVED,
            attrs=[
                AttrFactory.create(restrictions=Restrictions(sequence=103)),
            ],
        )

        parent_a.extensions.append(ExtensionFactory.reference(parent_b.qname))
        target.extensions.append(ExtensionFactory.reference(parent_a.qname))

        self.container.add(target)
        self.container.add(parent_a)
        self.container.add(parent_b)
        self.processor.process(target)

        actual = [x.restrictions.sequence for x in target.attrs]
        expected = [3, 3, None, 4, 4]
        self.assertEqual(expected, actual)

        self.assertEqual(2, parent_a.attrs[0].restrictions.sequence)
        self.assertEqual(1, parent_b.attrs[0].restrictions.sequence)
