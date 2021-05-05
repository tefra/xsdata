from dataclasses import dataclass
from dataclasses import make_dataclass
from unittest import mock
from unittest.case import TestCase

from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar


@dataclass
class Fixture:
    a: int


class XmlValTests(TestCase):
    def test_property_lname(self):
        var = XmlVar(name="a", qname="{B}A")
        self.assertEqual("A", var.lname)

    def test_property_clazz(self):
        var = XmlVar(name="foo", qname="foo")
        self.assertIsNone(var.clazz)

        var = XmlVar(name="foo", qname="foo", dataclass=True, types=(Fixture,))
        self.assertEqual(Fixture, var.clazz)

    def test_property_is_clazz_union(self):
        var = XmlVar(name="foo", qname="foo", dataclass=True, types=(Fixture,))
        self.assertFalse(var.is_clazz_union)

        var.types = var.types + (int,)
        self.assertTrue(var.is_clazz_union)

    def test_property_is_list(self):
        var = XmlVar(name="foo", qname="foo")
        self.assertFalse(var.list_element)

        var = XmlVar(name="foo", qname="foo", types=(int,), list_element=True)
        self.assertTrue(var.list_element)

    def test_find_choice(self):
        var = XmlVar(
            is_elements=True,
            name="foo",
            qname="foo",
            elements={
                "{a}a": XmlVar(is_element=True, name="a", qname="{a}a"),
                "b": XmlVar(is_element=True, name="b", qname="b"),
            },
        )

        self.assertIsNone(var.find_choice("a"))
        self.assertEqual("a", var.find_choice("{a}a").name)
        self.assertEqual("b", var.find_choice("b").name)

        var.elements.clear()
        var.wildcards = [
            XmlVar(
                is_wildcard=True, name="target", qname="target", namespaces=("foo",)
            ),
            XmlVar(is_wildcard=True, name="other", qname="other", namespaces=("!foo",)),
        ]

        self.assertEqual(var.wildcards[1], var.find_choice("{a}a"))
        self.assertEqual(var.wildcards[0], var.find_choice("{foo}a"))

    def test_find_value_choice(self):
        c = make_dataclass("C", fields=[])
        d = make_dataclass("D", fields=[], bases=(c,))

        elements = [
            XmlVar(is_element=True, qname="a", name="a", types=(int,)),
            XmlVar(is_element=True, qname="b", name="b", types=(int,), tokens=True),
            XmlVar(is_element=True, qname="c", name="c", types=(c,), dataclass=True),
            XmlVar(is_element=True, qname="d", name="d", types=(float,), nillable=True),
        ]

        var = XmlVar(
            is_elements=True,
            name="compound",
            qname="compound",
            elements={x.qname: x for x in elements},
        )

        self.assertIsNone(var.find_value_choice("foo"))
        self.assertEqual(elements[0], var.find_value_choice(1))
        self.assertEqual(elements[1], var.find_value_choice([1, 2]))
        self.assertEqual(elements[2], var.find_value_choice(d()))
        self.assertEqual(elements[2], var.find_value_choice(c()))
        self.assertEqual(elements[3], var.find_value_choice(None))

    def test_match_namespace(self):
        var = XmlVar(is_wildcard=True, name="foo", qname="foo")
        self.assertTrue(var.match_namespace("*"))
        self.assertTrue(var.match_namespace("a"))

        var = XmlVar(is_wildcard=True, name="foo", qname="foo", namespaces=("tns",))
        self.assertFalse(var.match_namespace("a"))
        self.assertTrue(var.match_namespace("{tns}a"))

        var = XmlVar(is_wildcard=True, name="foo", qname="foo", namespaces=("##any",))
        self.assertTrue(var.match_namespace("a"))
        self.assertTrue(var.match_namespace("{tns}a"))

        var = XmlVar(is_wildcard=True, name="foo", qname="foo", namespaces=("",))
        self.assertTrue(var.match_namespace("a"))
        self.assertFalse(var.match_namespace("{tns}a"))

        var = XmlVar(is_wildcard=True, name="foo", qname="foo", namespaces=("!tns",))
        self.assertTrue(var.match_namespace("{foo}a"))
        self.assertFalse(var.match_namespace("{tns}a"))

        var.namespace_matches["{tns}cached"] = True
        self.assertTrue(var.match_namespace("{tns}cached"))


class XmlMetaTests(TestCase):
    def setUp(self) -> None:
        a = make_dataclass("a", [])
        self.meta = XmlMeta(clazz=a, qname="a", source_qname="a", nillable=False)

    def test_find_attribute(self):
        a = XmlVar(is_attribute=True, qname="a", name="a")
        b = XmlVar(is_attribute=True, qname="b", name="b")

        self.meta.attributes[a.qname] = a
        self.meta.attributes[b.qname] = b

        self.assertEqual(a, self.meta.find_attribute("a"))
        self.assertEqual(b, self.meta.find_attribute("b"))

    def test_find_elements(self):
        a_1 = XmlVar(is_attribute=True, qname="a", name="a_1")
        a_2 = XmlVar(is_attribute=True, qname="a", name="a_2")

        self.meta.elements[a_1.qname] = [a_1, a_2]

        self.assertEqual([a_1, a_2], self.meta.find_elements("a"))
        self.assertEqual([], self.meta.find_elements("b"))

    @mock.patch.object(XmlVar, "find_choice")
    def test_find_choice(self, mock_find_choice):
        a_1 = XmlVar(is_attribute=True, qname="a", name="a_1")
        a_2 = XmlVar(is_attribute=True, qname="a", name="a_2")

        mock_find_choice.side_effect = [None, None, None, a_1, a_2]
        choice_1 = XmlVar(is_attribute=True, qname="compound_1", name="compound_1")
        choice_2 = XmlVar(is_attribute=True, qname="compound_2", name="compound_2")
        self.meta.choices = [choice_1, choice_2]

        self.assertIsNone(self.meta.find_choice("a"))
        self.assertEqual(a_1, self.meta.find_choice("a"))
        self.assertEqual(a_2, self.meta.find_choice("a"))

        mock_find_choice.assert_has_calls([mock.call("a") for _ in range(5)])

    @mock.patch.object(XmlVar, "match_namespace")
    def test_find_any_attributes(self, mock_match_namespace):
        mock_match_namespace.side_effect = [False, False, False, True]

        attributes = [
            XmlVar(is_attributes=True, qname="any", name="any"),
            XmlVar(is_attributes=True, qname="other", name="any"),
        ]
        self.meta.any_attributes = attributes

        self.assertIsNone(self.meta.find_any_attributes("a"))
        self.assertEqual(attributes[1], self.meta.find_any_attributes("a"))

        mock_match_namespace.assert_has_calls([mock.call("a") for _ in range(4)])

    @mock.patch.object(XmlVar, "match_namespace")
    def test_find_wildcard(self, mock_match_namespace):
        mock_match_namespace.side_effect = [False, False, False, True]

        wildcards = [
            XmlVar(is_wildcard=True, qname="any", name="any"),
            XmlVar(is_wildcard=True, qname="other", name="any"),
        ]
        self.meta.wildcards = wildcards

        self.assertIsNone(self.meta.find_wildcard("a"))
        self.assertEqual(wildcards[1], self.meta.find_wildcard("a"))

        mock_match_namespace.assert_has_calls([mock.call("a") for _ in range(4)])
