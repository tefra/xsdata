from dataclasses import dataclass
from dataclasses import make_dataclass
from dataclasses import replace
from unittest.case import TestCase

from tests.fixtures.books.books import BookForm
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlAttribute
from xsdata.formats.dataclass.models.elements import XmlAttributes
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlElements
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.elements import XmlWildcard


@dataclass
class Fixture:
    a: int


class XmlValTests(TestCase):
    def test_property_clazz(self):
        var = XmlVar(name="foo", qname="foo")
        self.assertIsNone(var.clazz)

        var = XmlVar(name="foo", qname="foo", dataclass=True, types=[Fixture])
        self.assertEqual(Fixture, var.clazz)

    def test_property_is_clazz_union(self):
        var = XmlVar(name="foo", qname="foo", dataclass=True, types=[Fixture])
        self.assertFalse(var.is_clazz_union)

        var.types.append(Fixture)
        self.assertTrue(var.is_clazz_union)

    def test_property_is_list(self):
        var = XmlVar(name="foo", qname="foo")
        self.assertFalse(var.is_list)

        var = XmlVar(name="foo", qname="foo", types=[int], list_element=True)
        self.assertTrue(var.is_list)

    def test_default_properties(self):
        var = XmlVar(name="foo", qname="foo")
        self.assertFalse(var.is_any_type)
        self.assertFalse(var.is_attribute)
        self.assertFalse(var.is_attributes)
        self.assertFalse(var.is_wildcard)
        self.assertFalse(var.is_element)
        self.assertFalse(var.is_elements)
        self.assertFalse(var.is_text)
        self.assertFalse(var.is_mixed_content)

    def test_matches(self):
        var = XmlVar(name="foo", qname="foo")
        self.assertTrue(var.matches("*"))
        self.assertTrue(var.matches(var.qname))
        self.assertFalse(var.matches("bar"))

    def test_find_choice(self):
        var = XmlVar(name="foo", qname="foo")
        self.assertIsNone(var.find_choice("foo"))

    def test_find_value_choice(self):
        var = XmlVar(name="foo", qname="foo")
        self.assertIsNone(var.find_value_choice(int))


class XmlElementTests(TestCase):
    def test_property_is_element(self):
        var = XmlElement(name="foo", qname="foo")

        self.assertIsInstance(var, XmlVar)
        self.assertTrue(var.is_element)

    def test_property_is_any_type(self):
        var = XmlElement(name="foo", qname="foo")
        self.assertFalse(var.is_any_type)

        var = XmlElement(name="foo", qname="foo", types=[int, object])
        self.assertFalse(var.is_any_type)

        var = XmlElement(name="foo", qname="foo", types=[object])
        self.assertTrue(var.is_any_type)


class XmlElementsTests(TestCase):
    def test_property_is_elements(self):
        var = XmlElements(name="foo", qname="foo")

        self.assertTrue(var.is_elements)

    def test_find_choice(self):
        choices = [XmlElement(name="a", qname="{a}a"), XmlElement(name="b", qname="b")]
        var = XmlElements(name="foo", qname="foo", choices=choices)

        self.assertFalse(var.matches("a"))
        self.assertIsNone(var.find_choice("a"))

        self.assertEqual(choices[0], var.find_choice("{a}a"))
        self.assertTrue(var.matches("{a}a"))

        self.assertEqual(choices[1], var.find_choice("b"))
        self.assertTrue(var.matches("b"))

    def test_find_value_choice(self):
        c = make_dataclass("C", fields=[])
        d = make_dataclass("D", fields=[], bases=(c,))

        var = XmlElements(
            name="compound",
            qname="compound",
            choices=[
                XmlElement(qname="a", name="a", types=[int]),
                XmlElement(qname="b", name="b", types=[int], tokens=True),
                XmlElement(qname="c", name="c", types=[c], dataclass=True),
            ],
        )

        self.assertIsNone(var.find_value_choice("foo"))
        self.assertEqual(var.choices[0], var.find_value_choice(1))
        self.assertEqual(var.choices[1], var.find_value_choice([1, 2]))
        self.assertEqual(var.choices[2], var.find_value_choice(d()))
        self.assertEqual(var.choices[2], var.find_value_choice(c()))


class XmlWildcardTests(TestCase):
    def test_property_is_mixed_content(self):
        var = XmlWildcard(name="foo", qname="foo")

        self.assertIsInstance(var, XmlVar)
        self.assertFalse(var.is_mixed_content)

        var = replace(var, mixed=True)
        self.assertTrue(var.is_mixed_content)

    def test_property_is_wildcard(self):
        var = XmlWildcard(name="foo", qname="foo")

        self.assertIsInstance(var, XmlVar)
        self.assertTrue(var.is_wildcard)

    def test_matches(self):
        var = XmlWildcard(name="foo", qname="foo")
        self.assertTrue(var.matches("*"))
        self.assertTrue(var.matches("a"))

        var = XmlWildcard(name="foo", qname="foo", namespaces=["tns"])
        self.assertFalse(var.matches("a"))
        self.assertTrue(var.matches("{tns}a"))

        var = XmlWildcard(name="foo", qname="foo", namespaces=["##any"])
        self.assertTrue(var.matches("a"))
        self.assertTrue(var.matches("{tns}a"))

        var = XmlWildcard(name="foo", qname="foo", namespaces=[""])
        self.assertTrue(var.matches("a"))
        self.assertFalse(var.matches("{tns}a"))

        var = XmlWildcard(name="foo", qname="foo", namespaces=["!tns"])
        self.assertTrue(var.matches("{foo}a"))
        self.assertFalse(var.matches("{tns}a"))


class XmlAttributeTests(TestCase):
    def test_property_is_attribute(self):
        var = XmlAttribute(name="foo", qname="foo")

        self.assertIsInstance(var, XmlVar)
        self.assertTrue(var.is_attribute)


class XmlAttributesTests(TestCase):
    def test_property_is_attributes(self):
        var = XmlAttributes(name="foo", qname="foo")

        self.assertIsInstance(var, XmlVar)
        self.assertTrue(var.is_attributes)


class XmlTextTests(TestCase):
    def test_property_is_text(self):
        var = XmlText(name="foo", qname="foo")

        self.assertIsInstance(var, XmlVar)
        self.assertTrue(var.is_text)


class XmlMetaTests(TestCase):
    def test_find_var(self):
        ctx = XmlContext()
        meta = ctx.build(BookForm)

        self.assertIsInstance(meta.find_var("author"), XmlElement)
        self.assertIsNone(meta.find_var("author", FindMode.ATTRIBUTE))
        self.assertIsNone(meta.find_var("nope"))

    def test_find_var_uses_cache(self):
        ctx = XmlContext()
        meta = ctx.build(BookForm)

        self.assertEqual("author", meta.find_var("author").name)
        self.assertEqual(1, len(meta.cache))
        key = tuple(meta.cache.keys())[0]

        meta.cache[key] = 1
        self.assertEqual("title", meta.find_var("author").name)
