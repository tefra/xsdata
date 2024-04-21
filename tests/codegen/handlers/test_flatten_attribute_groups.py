from xsdata.codegen.container import ClassContainer
from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.handlers import FlattenAttributeGroups
from xsdata.codegen.models import Status
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory, ClassFactory, FactoryTestCase


class FlattenAttributeGroupsTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer(config=GeneratorConfig())
        self.processor = FlattenAttributeGroups(container=container)

    def test_process(self):
        group = ClassFactory.create(qname="group", tag=Tag.GROUP)
        group.attrs = [
            AttrFactory.reference(name="one", qname="inner_one", forward=True),
            AttrFactory.reference(name="two", qname="inner_two", forward=True),
        ]
        inner_one = ClassFactory.create(
            qname="inner_one",
            attrs=[
                AttrFactory.reference(qname="group", tag=Tag.GROUP),
            ],
        )
        inner_two = inner_one.clone(qname="inner_two")
        inner_one.parent = group
        inner_two.parent = group
        group.inner.extend([inner_one, inner_two])
        target = ClassFactory.create(
            attrs=[
                AttrFactory.reference(qname="group", tag=Tag.GROUP),
            ]
        )
        self.processor.container.extend([group, target])
        self.processor.container.process()

        self.assertEqual(["one", "two"], [x.name for x in target.attrs])
        self.assertEqual(["inner_one", "inner_two"], [x.name for x in target.inner])

        for inner in target.inner:
            self.assertEqual(["one", "two"], [x.name for x in inner.attrs])
            self.assertEqual(0, len(inner.inner))

    def test_process_attribute_with_self_reference(self):
        group_attr = AttrFactory.attribute_group(name="bar")
        target = ClassFactory.create(qname="bar", tag=Tag.ATTRIBUTE_GROUP)
        target.attrs.append(group_attr)

        target.status = Status.FLATTENING
        self.processor.container.add(target)

        self.processor.process_attribute(target, group_attr)
        self.assertFalse(group_attr in target.attrs)

    def test_process_attribute_with_unknown_source(self):
        group_attr = AttrFactory.attribute_group(name="bar")
        target = ClassFactory.create()
        target.attrs.append(group_attr)

        with self.assertRaises(CodegenError):
            self.processor.process_attribute(target, group_attr)
