from tests.factories import AttrChoiceFactory
from tests.factories import FactoryTestCase
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.models.enums import Tag


class AttrChoiceTests(FactoryTestCase):
    def test_property_xml_type(self):
        for tag in Tag.names():
            choice = AttrChoiceFactory.create(tag=tag)

            if tag == Tag.ANY:
                self.assertEqual(XmlType.WILDCARD, choice.xml_type)
            else:
                self.assertIsNone(choice.xml_type)

    def test_property_is_tokens(self):
        choice = AttrChoiceFactory.create()
        self.assertFalse(choice.is_tokens)

        choice.restrictions.tokens = True
        self.assertTrue(choice.is_tokens)
