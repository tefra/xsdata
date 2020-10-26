from tests.factories import AttrChoiceFactory
from tests.factories import FactoryTestCase
from xsdata.models.enums import Tag


class AttrChoiceTests(FactoryTestCase):
    def test_property_is_wildcard(self):
        for tag in Tag.names():
            choice = AttrChoiceFactory.create(tag=tag)

            if tag == Tag.ANY:
                self.assertTrue(choice.is_wildcard)
            else:
                self.assertFalse(choice.is_wildcard)

    def test_property_is_tokens(self):
        choice = AttrChoiceFactory.create()
        self.assertFalse(choice.is_tokens)

        choice.restrictions.tokens = True
        self.assertTrue(choice.is_tokens)
