from unittest import mock

from xsdata.codegen.handlers import AttributeCompoundChoiceHandler
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeCompoundChoiceHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = AttributeCompoundChoiceHandler()

    @mock.patch.object(AttributeCompoundChoiceHandler, "group_fields")
    def test_process(self, mock_group_fields):
        target = ClassFactory.elements(8)
        # First group repeating
        target.attrs[0].restrictions.choice = "1"
        target.attrs[1].restrictions.choice = "1"
        target.attrs[1].restrictions.max_occurs = 2
        # Second group repeating
        target.attrs[2].restrictions.choice = "2"
        target.attrs[3].restrictions.choice = "2"
        target.attrs[3].restrictions.max_occurs = 2
        # Third group optional
        target.attrs[4].restrictions.choice = "3"
        target.attrs[5].restrictions.choice = "3"

        self.processor.process(target)
        mock_group_fields.assert_has_calls(
            [
                mock.call(target, target.attrs[0:2]),
                mock.call(target, target.attrs[2:4]),
            ]
        )

    def test_group_fields(self):
        target = ClassFactory.create(attrs=AttrFactory.list(2))
        target.attrs[0].restrictions.choice = "1"
        target.attrs[1].restrictions.choice = "1"
        target.attrs[0].restrictions.min_occurs = 10
        target.attrs[0].restrictions.max_occurs = 15
        target.attrs[1].restrictions.min_occurs = 5
        target.attrs[1].restrictions.max_occurs = 20

        expected = AttrFactory.create(
            name="attr_B_Or_attr_C",
            tag="Choice",
            index=0,
            types=[AttrTypeFactory.native(DataType.ANY_TYPE)],
            choices=[
                AttrFactory.create(
                    tag=target.attrs[0].tag,
                    name="attr_B",
                    types=target.attrs[0].types,
                ),
                AttrFactory.create(
                    tag=target.attrs[1].tag,
                    name="attr_C",
                    types=target.attrs[1].types,
                ),
            ],
        )
        expected_res = Restrictions(min_occurs=5, max_occurs=20)

        self.processor.group_fields(target, list(target.attrs))
        self.assertEqual(1, len(target.attrs))
        self.assertEqual(expected, target.attrs[0])
        self.assertEqual(expected_res, target.attrs[0].restrictions)

    def test_group_fields_with_effective_choices_sums_occurs(self):
        target = ClassFactory.create(attrs=AttrFactory.list(2))
        target.attrs[0].restrictions.choice = "effective_1"
        target.attrs[1].restrictions.choice = "effective_1"
        target.attrs[0].restrictions.min_occurs = 1
        target.attrs[0].restrictions.max_occurs = 2
        target.attrs[1].restrictions.min_occurs = 3
        target.attrs[1].restrictions.max_occurs = 4

        expected_res = Restrictions(min_occurs=4, max_occurs=6)

        self.processor.group_fields(target, list(target.attrs))
        self.assertEqual(1, len(target.attrs))
        self.assertEqual(expected_res, target.attrs[0].restrictions)

    def test_group_fields_limit_name(self):
        target = ClassFactory.create(attrs=AttrFactory.list(3))
        for attr in target.attrs:
            attr.restrictions.choice = "1"

        self.processor.group_fields(target, list(target.attrs))

        self.assertEqual(1, len(target.attrs))
        self.assertEqual("attr_B_Or_attr_C_Or_attr_D", target.attrs[0].name)

        target = ClassFactory.create(attrs=AttrFactory.list(4))
        for attr in target.attrs:
            attr.restrictions.choice = "1"

        self.processor.group_fields(target, list(target.attrs))
        self.assertEqual("choice", target.attrs[0].name)

        target = ClassFactory.create()
        attr = AttrFactory.element(restrictions=Restrictions(choice="1"))
        target.attrs.append(attr)
        target.attrs.append(attr.clone())
        self.processor.group_fields(target, list(target.attrs))
        self.assertEqual("choice", target.attrs[0].name)

    def test_build_attr_choice(self):
        attr = AttrFactory.create(
            name="a", namespace="xsdata", default="123", help="help", fixed=True
        )
        attr.local_name = "aaa"
        attr.restrictions = Restrictions(
            required=True,
            prohibited=None,
            min_occurs=1,
            max_occurs=1,
            min_exclusive="1.1",
            min_inclusive="1",
            min_length=1,
            max_exclusive="1",
            max_inclusive="1.1",
            max_length=10,
            total_digits=333,
            fraction_digits=2,
            length=5,
            white_space="collapse",
            pattern=r"[A-Z]",
            explicit_timezone="+1",
            nillable=True,
            choice="abc",
            sequential=True,
        )
        expected_res = attr.restrictions.clone()
        expected_res.min_occurs = None
        expected_res.max_occurs = None
        expected_res.sequential = None

        actual = self.processor.build_attr_choice(attr)

        self.assertEqual(attr.local_name, actual.name)
        self.assertEqual(attr.namespace, actual.namespace)
        self.assertEqual(attr.default, actual.default)
        self.assertEqual(attr.tag, actual.tag)
        self.assertEqual(attr.types, actual.types)
        self.assertEqual(expected_res, actual.restrictions)
        self.assertEqual(attr.help, actual.help)
        self.assertFalse(actual.fixed)
