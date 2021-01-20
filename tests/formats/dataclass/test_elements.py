from dataclasses import dataclass
from dataclasses import make_dataclass
from dataclasses import replace
from unittest.case import TestCase

from tests.fixtures.books.books import BookForm
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.elements import XmlVar


@dataclass
class Fixture:
    a: int


class XmlValTests(TestCase):
    def test_init_with_xml_type(self):
        var = XmlVar(name="a", qname="a", xml_type=XmlType.TEXT)
        self.assertFalse(var.element)
        self.assertFalse(var.elements)
        self.assertFalse(var.attribute)
        self.assertFalse(var.attributes)
        self.assertTrue(var.text)
        self.assertFalse(var.wildcard)

        var = XmlVar(name="a", qname="a", xml_type=XmlType.ELEMENT)
        self.assertTrue(var.element)
        self.assertFalse(var.elements)
        self.assertFalse(var.attribute)
        self.assertFalse(var.attributes)
        self.assertFalse(var.text)
        self.assertFalse(var.wildcard)

        var = XmlVar(name="a", qname="a", xml_type=XmlType.ELEMENTS)
        self.assertFalse(var.element)
        self.assertTrue(var.elements)
        self.assertFalse(var.attribute)
        self.assertFalse(var.attributes)
        self.assertFalse(var.text)
        self.assertFalse(var.wildcard)

        var = XmlVar(name="a", qname="a", xml_type=XmlType.ATTRIBUTE)
        self.assertFalse(var.element)
        self.assertFalse(var.elements)
        self.assertTrue(var.attribute)
        self.assertFalse(var.attributes)
        self.assertFalse(var.text)
        self.assertFalse(var.wildcard)

        var = XmlVar(name="a", qname="a", xml_type=XmlType.ATTRIBUTES)
        self.assertFalse(var.element)
        self.assertFalse(var.elements)
        self.assertFalse(var.attribute)
        self.assertTrue(var.attributes)
        self.assertFalse(var.text)
        self.assertFalse(var.wildcard)

        var = XmlVar(name="a", qname="a", xml_type=XmlType.WILDCARD)
        self.assertFalse(var.element)
        self.assertFalse(var.elements)
        self.assertFalse(var.attribute)
        self.assertFalse(var.attributes)
        self.assertFalse(var.text)
        self.assertTrue(var.wildcard)

        var = XmlVar(name="a", qname="a")
        self.assertFalse(var.element)
        self.assertFalse(var.elements)
        self.assertFalse(var.attribute)
        self.assertFalse(var.attributes)
        self.assertFalse(var.text)
        self.assertFalse(var.wildcard)

        with self.assertRaises(XmlContextError) as cm:
            XmlVar(name="a", qname="a", xml_type="xsdata")

        self.assertEqual("Unknown xml type `xsdata`", str(cm.exception))

    def test_property_lname(self):
        var = XmlVar(name="a", qname="{B}A")
        self.assertEqual("A", var.lname)

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
        self.assertFalse(var.list_element)

        var = XmlVar(name="foo", qname="foo", types=[int], list_element=True)
        self.assertTrue(var.list_element)

    def test_matches(self):
        var = XmlVar(name="foo", qname="foo")
        self.assertTrue(var.matches("*"))
        self.assertTrue(var.matches(var.qname))
        self.assertFalse(var.matches("bar"))

    def test_find_choice(self):
        choices = [
            XmlVar(element=True, name="a", qname="{a}a"),
            XmlVar(element=True, name="b", qname="b"),
        ]
        var = XmlVar(elements=True, name="foo", qname="foo", choices=choices)

        self.assertFalse(var.matches("a"))
        self.assertIsNone(var.find_choice("a"))

        self.assertEqual(choices[0], var.find_choice("{a}a"))
        self.assertTrue(var.matches("{a}a"))

        self.assertEqual(choices[1], var.find_choice("b"))
        self.assertTrue(var.matches("b"))

    def test_find_value_choice(self):
        c = make_dataclass("C", fields=[])
        d = make_dataclass("D", fields=[], bases=(c,))

        var = XmlVar(
            elements=True,
            name="compound",
            qname="compound",
            choices=[
                XmlVar(element=True, qname="a", name="a", types=[int]),
                XmlVar(element=True, qname="b", name="b", types=[int], tokens=True),
                XmlVar(element=True, qname="c", name="c", types=[c], dataclass=True),
                XmlVar(element=True, qname="d", name="d", types=[float], nillable=True),
            ],
        )

        self.assertIsNone(var.find_value_choice("foo"))
        self.assertEqual(var.choices[0], var.find_value_choice(1))
        self.assertEqual(var.choices[1], var.find_value_choice([1, 2]))
        self.assertEqual(var.choices[2], var.find_value_choice(d()))
        self.assertEqual(var.choices[2], var.find_value_choice(c()))
        self.assertEqual(var.choices[3], var.find_value_choice(None))

    def test_matches_widlcard(self):
        var = XmlVar(wildcard=True, name="foo", qname="foo")
        self.assertTrue(var.matches("*"))
        self.assertTrue(var.matches("a"))

        var = XmlVar(wildcard=True, name="foo", qname="foo", namespaces=["tns"])
        self.assertFalse(var.matches("a"))
        self.assertTrue(var.matches("{tns}a"))

        var = XmlVar(wildcard=True, name="foo", qname="foo", namespaces=["##any"])
        self.assertTrue(var.matches("a"))
        self.assertTrue(var.matches("{tns}a"))

        var = XmlVar(wildcard=True, name="foo", qname="foo", namespaces=[""])
        self.assertTrue(var.matches("a"))
        self.assertFalse(var.matches("{tns}a"))

        var = XmlVar(wildcard=True, name="foo", qname="foo", namespaces=["!tns"])
        self.assertTrue(var.matches("{foo}a"))
        self.assertFalse(var.matches("{tns}a"))


class XmlMetaTests(TestCase):
    def test_find_var(self):
        ctx = XmlContext()
        meta = ctx.build(BookForm)

        self.assertTrue(meta.find_var("author").element)
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
