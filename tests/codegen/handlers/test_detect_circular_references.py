from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers.detect_circular_references import DetectCircularReferences
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    FactoryTestCase,
)


class DetectCircularReferencesTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        config = GeneratorConfig()
        self.container = ClassContainer(config=config)
        self.processor = DetectCircularReferences(self.container)

    def test_process(self) -> None:
        first = ClassFactory.create(qname="first")
        second = ClassFactory.create(qname="second")
        third = ClassFactory.create(qname="third")

        first.attrs.append(AttrFactory.native(DataType.STRING))
        first.attrs.append(
            AttrFactory.create(
                types=[
                    AttrTypeFactory.create(qname="second", reference=second.ref),
                    AttrTypeFactory.create(qname="third", reference=third.ref),
                ],
                choices=[
                    AttrFactory.reference("second", reference=second.ref),
                    AttrFactory.reference("third", reference=third.ref),
                ],
            )
        )

        second.attrs = AttrFactory.list(2)
        third.attrs.append(AttrFactory.reference("first", reference=first.ref))
        self.container.extend([first, second, third])

        self.processor.process(first)

        first_flags = [tp.circular for tp in first.types()]
        self.assertEqual([False, False, True, False, True], first_flags)

        second_flags = [tp.circular for tp in second.types()]
        self.assertEqual([False, False], second_flags)

        # First has the flags this doesn't need it :)
        third_flags = [tp.circular for tp in third.types()]
        self.assertEqual([False], third_flags)

    def test_build_reference_types(self) -> None:
        target = ClassFactory.create()
        inner = ClassFactory.create()

        outer_attr = AttrFactory.create()
        inner_attr = AttrFactory.reference("foo", reference=target.ref)

        inner.attrs.append(inner_attr)
        target.inner.append(inner)
        target.attrs.append(outer_attr)

        self.container.add(target)

        self.processor.build_reference_types()

        expected = {
            target.ref: [inner_attr.types[0]],
            inner.ref: [inner_attr.types[0]],
        }

        self.assertEqual(expected, self.processor.reference_types)
