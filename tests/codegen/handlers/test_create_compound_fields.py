from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import CreateCompoundFields
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class CreateCompoundFieldsTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.config = GeneratorConfig()
        self.config.output.compound_fields.enabled = True
        self.container = ClassContainer(config=self.config)
        self.processor = CreateCompoundFields(container=self.container)

    @mock.patch.object(CreateCompoundFields, "group_fields")
    def test_process(self, mock_group_fields):
        target = ClassFactory.elements(8)
        # First group repeating
        target.attrs[0].restrictions.choice = "1"
        target.attrs[1].restrictions.choice = "1"
        target.attrs[1].restrictions.max_occurs = 1
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
        target = ClassFactory.create(attrs=AttrFactory.list(4))
        target.attrs[0].restrictions.choice = "1"
        target.attrs[1].restrictions.choice = "1"
        target.attrs[0].restrictions.min_occurs = 10
        target.attrs[0].restrictions.max_occurs = 15
        target.attrs[1].restrictions.min_occurs = 5
        target.attrs[1].restrictions.max_occurs = 20
        target.attrs[2].restrictions.min_occurs = 2
        target.attrs[2].restrictions.max_occurs = 4
        target.attrs[3].restrictions.min_occurs = 1
        target.attrs[3].restrictions.max_occurs = 3
        target.attrs[2].restrictions.group = 1
        target.attrs[3].restrictions.group = 1

        expected = AttrFactory.create(
            name="choice",
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
                AttrFactory.create(
                    tag=target.attrs[2].tag,
                    name="attr_D",
                    types=target.attrs[2].types,
                ),
                AttrFactory.create(
                    tag=target.attrs[3].tag,
                    name="attr_E",
                    types=target.attrs[3].types,
                ),
            ],
        )
        expected_res = Restrictions(min_occurs=3, max_occurs=20)

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

    def test_choose_name(self):
        target = ClassFactory.create()

        actual = self.processor.choose_name(target, ["a", "b", "c"])
        self.assertEqual("a_Or_b_Or_c", actual)

        actual = self.processor.choose_name(target, ["a", "b", "c", "d"])
        self.assertEqual("choice", actual)

        target.attrs.append(AttrFactory.create(name="choice"))
        actual = self.processor.choose_name(target, ["a", "b", "c", "d"])
        self.assertEqual("choice_1", actual)

        actual = self.processor.choose_name(target, ["a", "b", "c", "d"])
        self.assertEqual("choice_1", actual)

        self.processor.config.default_name = "ThisOrThat"
        actual = self.processor.choose_name(target, ["a", "b", "c", "d"])
        self.assertEqual("ThisOrThat", actual)

        self.processor.config.force_default_name = True
        actual = self.processor.choose_name(target, ["a", "b", "c"])
        self.assertEqual("ThisOrThat", actual)

    def test_build_reserved_names(self):
        base = ClassFactory.create(
            attrs=[
                AttrFactory.create("standalone"),
                AttrFactory.create(
                    name="first",
                    tag=Tag.CHOICE,
                    choices=[
                        AttrFactory.create(name="a"),
                        AttrFactory.create(name="b"),
                        AttrFactory.create(name="c"),
                    ],
                ),
                AttrFactory.create(
                    name="second",
                    tag=Tag.CHOICE,
                    choices=[
                        AttrFactory.create(name="b"),
                        AttrFactory.create(name="c"),
                    ],
                ),
            ]
        )

        target = ClassFactory.create()
        target.extensions.append(ExtensionFactory.reference(qname=base.qname))
        self.processor.container.extend([base, target])

        actual = self.processor.build_reserved_names(target, names=["b", "c"])
        expected = {"standalone", "first"}

        self.assertEqual(expected, actual)

    def test_build_attr_choice(self):
        attr = AttrFactory.create(
            name="a", namespace="xsdata", default="123", help="help", fixed=True
        )
        attr.local_name = "aaa"
        attr.restrictions = Restrictions(
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
            sequence=1,
        )
        expected_res = attr.restrictions.clone()
        expected_res.min_occurs = None
        expected_res.max_occurs = None
        expected_res.sequence = None

        actual = self.processor.build_attr_choice(attr)

        self.assertEqual(attr.local_name, actual.name)
        self.assertEqual(attr.namespace, actual.namespace)
        self.assertEqual(attr.default, actual.default)
        self.assertEqual(attr.tag, actual.tag)
        self.assertEqual(attr.types, actual.types)
        self.assertEqual(expected_res, actual.restrictions)
        self.assertEqual(attr.help, actual.help)
        self.assertFalse(actual.fixed)

    def test_attr_group_key(self):
        attr = AttrFactory.create()
        self.assertEqual(id(attr), self.processor.attr_group_key(attr))

        attr.restrictions.sequence = 1
        self.assertEqual(1, self.processor.attr_group_key(attr))

        attr.restrictions.group = 2
        self.assertEqual(2, self.processor.attr_group_key(attr))

    def test_reset_sequence(self):
        def len_sequence(target: Class):
            return len([attr for attr in target.attrs if attr.restrictions.sequence])

        restrictions = Restrictions(max_occurs=2, sequence=1)
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(restrictions=restrictions.clone()),
                AttrFactory.create(restrictions=restrictions.clone()),
            ]
        )

        attrs_clone = [attr.clone() for attr in target.attrs]

        self.processor.config.enabled = False
        self.processor.reset_sequence(target, 0)
        self.assertEqual(2, len_sequence(target))

        target.attrs[0].restrictions.sequence = None
        self.processor.reset_sequence(target, 0)
        self.assertEqual(1, len_sequence(target))

        self.processor.reset_sequence(target, 1)
        self.assertEqual(0, len_sequence(target))

        target.attrs = attrs_clone
        target.attrs[1].restrictions.sequence = None
        self.processor.reset_sequence(target, 0)
        self.assertEqual(0, len_sequence(target))

        target.attrs[0].restrictions.sequence = 1
        target.attrs[0].restrictions.max_occurs = 0
        target.attrs[1].restrictions.sequence = 1
        self.processor.reset_sequence(target, 0)
        self.assertEqual(1, len_sequence(target))
