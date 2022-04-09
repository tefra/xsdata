from xsdata.codegen.handlers import RenameDuplicateAttributes
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class RenameDuplicateAttributesTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = RenameDuplicateAttributes()

    def test_process(self):
        attrs = [
            AttrFactory.create(name="a", tag=Tag.ELEMENT),
            AttrFactory.create(name="a", tag=Tag.ATTRIBUTE),
            AttrFactory.create(name="b", tag=Tag.ATTRIBUTE),
            AttrFactory.create(name="c", tag=Tag.ATTRIBUTE),
            AttrFactory.create(name="c", tag=Tag.ELEMENT),
            AttrFactory.create(name="d", tag=Tag.ELEMENT),
            AttrFactory.create(name="d", tag=Tag.ELEMENT),
            AttrFactory.create(name="e", tag=Tag.ELEMENT, namespace="b"),
            AttrFactory.create(name="e", tag=Tag.ELEMENT),
            AttrFactory.create(name="f", tag=Tag.ELEMENT),
            AttrFactory.create(name="f", tag=Tag.ELEMENT, namespace="a"),
            AttrFactory.create(name="gA", tag=Tag.ENUMERATION),
            AttrFactory.create(name="g[A]", tag=Tag.ENUMERATION),
            AttrFactory.create(name="g_a", tag=Tag.ENUMERATION),
            AttrFactory.create(name="g_a_1", tag=Tag.ENUMERATION),
        ]
        target = ClassFactory.create(attrs=attrs)

        self.processor.process(target)
        expected = [
            "a",
            "a_Attribute",
            "b",
            "c_Attribute",
            "c",
            "d_Element",
            "d",
            "b_e",
            "e",
            "f",
            "a_f",
            "gA",
            "g[A]_2",
            "g_a_3",
            "g_a_1",
        ]
        self.assertEqual(expected, [x.name for x in attrs])
