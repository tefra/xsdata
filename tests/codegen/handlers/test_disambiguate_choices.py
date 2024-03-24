from dataclasses import replace

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import DisambiguateChoices
from xsdata.codegen.models import Restrictions, Status
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType, Tag
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    FactoryTestCase,
)


class DisambiguateChoicesTest(FactoryTestCase):
    maxDiff = None

    def setUp(self):
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.handler = DisambiguateChoices(self.container)

    def test_process_with_duplicate_wildcards(self):
        compound = AttrFactory.create(tag=Tag.CHOICE, types=[])
        target = ClassFactory.create()
        target.attrs.append(compound)
        compound.choices.append(AttrFactory.native(DataType.STRING))
        compound.choices.append(AttrFactory.any(namespace="foo"))
        compound.choices.append(
            AttrFactory.any(
                namespace="bar", restrictions=Restrictions(min_occurs=1, max_occurs=1)
            )
        )
        compound.choices.append(
            AttrFactory.any(
                namespace="bar", restrictions=Restrictions(max_occurs=3, min_occurs=0)
            )
        )
        self.container.add(target)
        self.handler.process(target)

        self.assertEqual(2, len(compound.choices))

        wildcard = compound.choices[-1]
        self.assertEqual("content", wildcard.name)
        self.assertEqual([AttrTypeFactory.native(DataType.ANY_TYPE)], wildcard.types)
        self.assertEqual("foo bar", wildcard.namespace)
        self.assertEqual(1, wildcard.restrictions.min_occurs)
        self.assertEqual(4, wildcard.restrictions.max_occurs)

    def test_process_with_duplicate_simple_types(self):
        compound = AttrFactory.create(tag=Tag.CHOICE)
        compound.types.clear()
        target = ClassFactory.create()
        target.attrs.append(compound)
        compound.choices.append(AttrFactory.native(DataType.STRING, name="a"))
        compound.choices.append(
            AttrFactory.native(DataType.STRING, name="b", namespace="xs")
        )
        self.container.add(target)

        self.handler.process(target)
        self.assertEqual(2, len(compound.choices))

        self.assertEqual("a", compound.choices[0].types[0].qname)
        self.assertEqual("{xs}b", compound.choices[1].types[0].qname)

        self.assertEqual(2, len(target.inner))
        self.assertEqual("a", target.inner[0].qname)
        self.assertEqual("{xs}b", target.inner[1].qname)

        self.assertEqual([], [x.qname for x in compound.types])

    def test_process_with_duplicate_any_types(self):
        compound = AttrFactory.create(tag=Tag.CHOICE, types=[])
        target = ClassFactory.create()
        target.attrs.append(compound)
        compound.choices.append(AttrFactory.native(DataType.ANY_TYPE, name="a"))
        compound.choices.append(
            AttrFactory.native(DataType.ANY_TYPE, name="b", namespace="xs")
        )
        self.container.add(target)

        self.handler.process(target)
        self.assertEqual(2, len(compound.choices))

        self.assertEqual("a", compound.choices[0].types[0].qname)
        self.assertEqual("{xs}b", compound.choices[1].types[0].qname)

        self.assertEqual(2, len(target.inner))
        self.assertEqual("a", target.inner[0].qname)
        self.assertEqual("{xs}b", target.inner[1].qname)

    def test_process_with_duplicate_complex_types(self):
        compound = AttrFactory.any()
        target = ClassFactory.create()
        target.attrs.append(compound)
        compound.choices.append(AttrFactory.reference(qname="myint"))
        compound.choices.append(AttrFactory.reference(qname="myint"))
        self.container.add(target)

        self.handler.process(target)
        self.assertEqual(2, len(compound.choices))

        self.assertEqual("attr_C", compound.choices[0].types[0].qname)
        self.assertEqual("attr_D", compound.choices[1].types[0].qname)

        self.assertEqual(2, len(target.inner))
        self.assertEqual("attr_C", target.inner[0].qname)
        self.assertEqual("attr_D", target.inner[1].qname)

        for inner in target.inner:
            self.assertEqual("myint", inner.extensions[0].type.qname)
            self.assertEqual("myint", inner.extensions[0].type.qname)

        self.assertEqual(DataType.ANY_TYPE, compound.types[0].datatype)

    def test_disambiguate_choice_with_unnest_true(self):
        target = ClassFactory.create()
        attr = AttrFactory.reference(qname="a")

        config = GeneratorConfig()
        config.output.unnest_classes = True
        container = ClassContainer(config=config)
        handler = DisambiguateChoices(container)

        container.add(target)
        handler.disambiguate_choice(target, attr)

        self.assertIsNotNone(container.find(attr.qname))

    def test_disambiguate_choice_with_circular_ref(self):
        target = ClassFactory.create()
        attr = AttrFactory.reference(qname="a")
        attr.types[0].circular = True

        self.container.add(target)
        self.handler.disambiguate_choice(target, attr)

        self.assertTrue(attr.types[0].circular)
        self.assertIsNotNone(self.container.find(attr.qname))

    def test_find_ambiguous_choices_ignore_wildcards(self):
        """Wildcards are merged."""

        attr = AttrFactory.create()
        attr.choices.append(AttrFactory.any())
        attr.choices.append(AttrFactory.any())
        attr.choices.append(
            AttrFactory.create(
                name="this", types=[AttrTypeFactory.native(DataType.ANY_TYPE)]
            )
        )

        result = self.handler.find_ambiguous_choices(attr)
        self.assertEqual(["this"], [x.name for x in result])

    def test_is_simple_type(self):
        attr = AttrFactory.native(DataType.STRING)
        self.assertTrue(self.handler.is_simple_type(attr))

        enumeration = ClassFactory.enumeration(2)
        self.container.add(enumeration)
        attr = AttrFactory.reference(qname=enumeration.qname)
        self.assertTrue(self.handler.is_simple_type(attr))

        complex = ClassFactory.create()
        self.container.add(complex)
        attr = AttrFactory.reference(qname=complex.qname)
        self.assertFalse(self.handler.is_simple_type(attr))

    def test_create_ref_class(self):
        source = ClassFactory.create(
            status=Status.RESOLVED,
            location="here.xsd",
            ns_map={"foo": "bar"},
        )
        attr = AttrFactory.create(
            namespace="test",
            restrictions=Restrictions(nillable=True),
        )

        result = self.handler.create_ref_class(source, attr, inner=True)

        self.assertTrue(result.local_type)
        self.assertEqual("{test}attr_B", result.qname)
        self.assertEqual(source.status, result.status)
        self.assertEqual(Tag.ELEMENT, result.tag)
        self.assertEqual(source.location, result.location)
        self.assertEqual(source.ns_map, result.ns_map)
        self.assertEqual(attr.restrictions.nillable, result.nillable)

    def test_create_ref_class_creates_unique_inner_names(self):
        source = ClassFactory.create(
            status=Status.RESOLVED,
            location="here.xsd",
            ns_map={"foo": "bar"},
        )
        attr = AttrFactory.create(name="a")
        source.inner.append(ClassFactory.create(qname="{xs}a"))
        result = self.handler.create_ref_class(source, attr, inner=True)

        self.assertEqual("a_1", result.name)

    def test_add_any_type_value(self):
        target = ClassFactory.elements(2)
        source = AttrFactory.any()
        self.handler.add_any_type_value(target, source)

        last = target.attrs[-1]
        self.assertEqual("content", last.name)
        self.assertEqual(Tag.ANY, last.tag)
        self.assertEqual(source.namespace, last.namespace)
        self.assertEqual([AttrTypeFactory.native(DataType.ANY_TYPE)], last.types)
        self.assertFalse(last.restrictions.is_optional)
        self.assertFalse(last.restrictions.is_list)

    def test_add_simply_type_value(self):
        target = ClassFactory.elements(2)
        source = AttrFactory.native(
            DataType.STRING,
            restrictions=Restrictions(
                max_length=2, nillable=True, path=[("s", 1, 1, 1)]
            ),
        )
        self.handler.add_simple_type_value(target, source)

        last = target.attrs[-1]
        self.assertEqual("value", last.name)
        self.assertEqual(Tag.EXTENSION, last.tag)
        self.assertIsNone(last.namespace)
        self.assertEqual(source.types, last.types)
        self.assertFalse(last.restrictions.is_optional)
        self.assertFalse(last.restrictions.is_list)
        self.assertEqual([], last.restrictions.path)
        self.assertFalse(last.restrictions.nillable)

    def test_add_extension(self):
        target = ClassFactory.create()
        source = AttrFactory.reference("{xs}type")
        source.types[0].forward = True
        source.types[0].circular = True
        self.handler.add_extension(target, source)

        last = target.extensions[-1]
        self.assertEqual(Tag.EXTENSION, last.tag)

        expected = replace(source.types[0], forward=False, circular=False)
        self.assertEqual(expected, last.type)
        self.assertEqual(Restrictions(), last.restrictions)
