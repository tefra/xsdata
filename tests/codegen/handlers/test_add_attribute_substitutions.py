from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AddAttributeSubstitutions
from xsdata.codegen.models import AttrType
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import Tag
from xsdata.utils.namespaces import build_qname
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    FactoryTestCase,
)


class AddAttributeSubstitutionsTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()

        container = ClassContainer(config=GeneratorConfig())
        self.processor = AddAttributeSubstitutions(container=container)

    @mock.patch.object(AddAttributeSubstitutions, "process_attribute")
    @mock.patch.object(AddAttributeSubstitutions, "create_substitutions")
    def test_process(self, mock_create_substitutions, mock_process_attribute) -> None:
        def init_substitutions() -> None:
            self.processor.substitutions = {}

        mock_create_substitutions.side_effect = init_substitutions

        target = ClassFactory.create(
            attrs=[AttrFactory.enumeration(), AttrFactory.any(), AttrFactory.element()]
        )

        self.processor.process(target)
        self.processor.process(ClassFactory.create())
        mock_process_attribute.assert_called_once_with(target, target.attrs[2])
        mock_create_substitutions.assert_called_once()

    @mock.patch("xsdata.utils.collections.find")
    def test_process_attribute(self, mock_find) -> None:
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(types=[AttrTypeFactory.create("foo")]),
                AttrFactory.create(types=[AttrTypeFactory.create("bar")]),
            ]
        )
        mock_find.side_effect = [-1, 2]

        first_attr = target.attrs[0]
        second_attr = target.attrs[1]
        first_attr.restrictions.min_occurs = 1
        first_attr.restrictions.max_occurs = 2
        second_attr.restrictions.min_occurs = 1

        attr_qname = first_attr.types[0].qname
        reference_attrs = AttrFactory.list(2)
        reference_attrs[0].restrictions.min_occurs = 1
        reference_attrs[1].restrictions.min_occurs = 1

        self.processor.create_substitutions()
        self.processor.substitutions[attr_qname] = reference_attrs
        self.processor.process_attribute(target, first_attr)

        self.assertEqual(4, len(target.attrs))

        # Guard against multiple runs in case of xs:groups
        self.processor.process_attribute(target, first_attr)
        self.assertEqual(4, len(target.attrs))

        self.assertEqual(reference_attrs[0], target.attrs[0])
        self.assertIsNot(reference_attrs[0], target.attrs[0])
        self.assertEqual(reference_attrs[1], target.attrs[3])
        self.assertIsNot(reference_attrs[1], target.attrs[3])
        self.assertEqual(2, target.attrs[0].restrictions.max_occurs)
        self.assertEqual(2, target.attrs[3].restrictions.max_occurs)

        self.assertEqual(0, target.attrs[0].restrictions.min_occurs)
        self.assertEqual(0, target.attrs[1].restrictions.min_occurs)
        self.assertEqual(1, target.attrs[2].restrictions.min_occurs)
        self.assertEqual(0, target.attrs[3].restrictions.min_occurs)

        self.assertEqual("foo", target.attrs[0].substitution)
        self.assertEqual("foo", target.attrs[1].substitution)
        self.assertEqual(None, target.attrs[2].substitution)
        self.assertEqual("foo", target.attrs[3].substitution)

        self.processor.process_attribute(target, second_attr)
        self.assertEqual(4, len(target.attrs))

    @mock.patch.object(AddAttributeSubstitutions, "create_substitution")
    def test_create_substitutions(self, mock_create_substitution) -> None:
        ns = "xsdata"
        classes = [
            ClassFactory.create(
                substitutions=[build_qname(ns, "foo"), build_qname(ns, "bar")],
                abstract=True,
            ),
            ClassFactory.create(substitutions=[build_qname(ns, "foo")], abstract=True),
        ]

        reference_attrs = AttrFactory.list(3)
        mock_create_substitution.side_effect = reference_attrs

        self.processor.container.extend(classes)
        self.processor.create_substitutions()

        expected = {
            build_qname(ns, "foo"): [reference_attrs[0], reference_attrs[2]],
            build_qname(ns, "bar"): [reference_attrs[1]],
        }
        self.assertEqual(expected, self.processor.substitutions)

        mock_create_substitution.assert_has_calls(
            [mock.call(classes[0]), mock.call(classes[0]), mock.call(classes[1])]
        )

    def test_create_substitution(self) -> None:
        item = ClassFactory.elements(1, qname=build_qname("foo", "bar"))
        actual = self.processor.create_substitution(item)

        expected = AttrFactory.create(
            name=item.name,
            default=None,
            types=[AttrType(qname=build_qname("foo", "bar"))],
            tag=Tag.ELEMENT,
        )

        self.assertEqual(expected, actual)

    def test_prepare_substituted(self) -> None:
        attr = AttrFactory.create()
        attr.restrictions.min_occurs = 1
        attr.restrictions.path.append(("s", 0, 1, 1))

        self.processor.prepare_substituted(attr)

        self.assertEqual(0, attr.restrictions.min_occurs)
        self.assertEqual(id(attr), attr.restrictions.choice)
        self.assertEqual(2, len(attr.restrictions.path))
        self.assertEqual(("c", id(attr), 1, 1), attr.restrictions.path[-1])

        attr.restrictions.choice = 1
        self.processor.prepare_substituted(attr)
        self.assertEqual(("c", id(attr), 1, 1), attr.restrictions.path[-1])
