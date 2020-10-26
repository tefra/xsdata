from unittest import mock

from tests.factories import AttrChoiceFactory
from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.handlers import AttributeChoiceGroupHandler
from xsdata.codegen.models import Restrictions


class AttributeChoiceGroupHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = AttributeChoiceGroupHandler()

    @mock.patch.object(AttributeChoiceGroupHandler, "group_attrs")
    def test_process(self, mock_group_attrs):
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
        mock_group_attrs.assert_has_calls(
            [
                mock.call(target, target.attrs[0:2]),
                mock.call(target, target.attrs[2:4]),
            ]
        )

    def test_group_attrs(self):
        target = ClassFactory.create(attrs=AttrFactory.list(2))
        target.attrs[0].restrictions.min_occurs = 10
        target.attrs[0].restrictions.max_occurs = 15
        target.attrs[1].restrictions.min_occurs = 5
        target.attrs[1].restrictions.max_occurs = 20

        expected = AttrFactory.create(
            name="attr_B_Or_attr_C",
            local_name="attr_B_Or_attr_C",
            tag="Choice",
            index=0,
            types=[AttrTypeFactory.xs_any()],
            choices=[
                AttrChoiceFactory.create(
                    tag=target.attrs[0].tag,
                    name="attr_B",
                    types=target.attrs[0].types,
                ),
                AttrChoiceFactory.create(
                    tag=target.attrs[1].tag,
                    name="attr_C",
                    types=target.attrs[1].types,
                ),
            ],
        )
        expected_res = Restrictions(min_occurs=5, max_occurs=20)

        self.processor.group_attrs(target, list(target.attrs))
        self.assertEqual(1, len(target.attrs))
        self.assertEqual(expected, target.attrs[0])
        self.assertEqual(expected_res, target.attrs[0].restrictions)

    def test_group_attrs_limit_name(self):
        target = ClassFactory.create(attrs=AttrFactory.list(3))
        self.processor.group_attrs(target, list(target.attrs))

        self.assertEqual(1, len(target.attrs))
        self.assertEqual("attr_B_Or_attr_C_Or_attr_D", target.attrs[0].name)

        target = ClassFactory.create(attrs=AttrFactory.list(4))
        self.processor.group_attrs(target, list(target.attrs))
        self.assertEqual("choice", target.attrs[0].name)

    def test_convert_attr(self):
        attr = AttrFactory.create(
            name="a", local_name="aaa", namespace="xsdata", default="123"
        )
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

        actual = self.processor.convert_attr(attr)

        self.assertEqual(attr.local_name, actual.name)
        self.assertEqual(attr.namespace, actual.namespace)
        self.assertEqual(attr.default, actual.default)
        self.assertEqual(attr.tag, actual.tag)
        self.assertEqual(attr.types, actual.types)
        self.assertEqual(expected_res, actual.restrictions)
