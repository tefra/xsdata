import copy
from dataclasses import dataclass
from dataclasses import make_dataclass
from typing import Iterator
from unittest import mock
from unittest.case import TestCase

from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.utils.testing import XmlMetaFactory
from xsdata.utils.testing import XmlVarFactory


@dataclass
class Fixture:
    a: int


class XmlValTests(TestCase):
    def test_property_local_name(self):
        var = XmlVarFactory.create(name="a", qname="{B}A")
        self.assertEqual("A", var.local_name)

    def test_property_clazz(self):
        var = XmlVarFactory.create(name="foo")
        self.assertIsNone(var.clazz)

        var = XmlVarFactory.create(name="foo", types=(Fixture,))
        self.assertEqual(Fixture, var.clazz)

    def test_get_xml_type(self):
        for xml_type in XmlType.all():
            var = XmlVarFactory.create(name="foo", xml_type=xml_type)
            self.assertEqual(xml_type, var.get_xml_type())

    def test_property_is_clazz_union(self):
        var = XmlVarFactory.create(name="foo", types=(Fixture,))
        self.assertFalse(var.is_clazz_union)

        var = XmlVarFactory.create(name="foo", types=(Fixture, int))
        self.assertTrue(var.is_clazz_union)

    def test_find_choice(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENTS,
            name="foo",
            qname="foo",
            elements={
                "{a}a": XmlVarFactory.create(
                    xml_type=XmlType.ELEMENT, name="a", qname="{a}a"
                ),
                "b": XmlVarFactory.create(
                    xml_type=XmlType.ELEMENT, name="b", qname="b"
                ),
            },
        )

        self.assertIsNone(var.find_choice("a"))
        self.assertEqual("a", var.find_choice("{a}a").name)
        self.assertEqual("b", var.find_choice("b").name)

        var.elements.clear()
        var.wildcards = [
            XmlVarFactory.create(
                xml_type=XmlType.WILDCARD,
                name="target",
                namespaces=("foo",),
            ),
            XmlVarFactory.create(
                xml_type=XmlType.WILDCARD,
                name="other",
                namespaces=("!foo",),
            ),
        ]

        self.assertEqual(var.wildcards[1], var.find_choice("{a}a"))
        self.assertEqual(var.wildcards[0], var.find_choice("{foo}a"))

    def test_find_value_choice(self):
        c = make_dataclass("C", fields=[])
        d = make_dataclass("D", fields=[], bases=(c,))

        elements = [
            XmlVarFactory.create(xml_type=XmlType.ELEMENT, name="a", types=(int,)),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT, name="b", types=(int,), tokens=True
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                name="c",
                types=(c,),
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                name="d",
                types=(float,),
                nillable=True,
            ),
        ]

        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENTS,
            name="compound",
            elements={x.qname: x for x in elements},
        )

        self.assertIsNone(var.find_value_choice("foo"))
        self.assertEqual(elements[0], var.find_value_choice(1))
        self.assertEqual(elements[1], var.find_value_choice([1, 2]))
        self.assertEqual(elements[2], var.find_value_choice(d()))
        self.assertEqual(elements[2], var.find_value_choice(c()))
        self.assertEqual(elements[3], var.find_value_choice(None))

    def test_match_namespace(self):
        var = XmlVarFactory.create(xml_type=XmlType.WILDCARD, name="foo")
        self.assertTrue(var.match_namespace("*"))
        self.assertTrue(var.match_namespace("a"))

        var = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, name="foo", namespaces=("tns",)
        )
        self.assertFalse(var.match_namespace("a"))
        self.assertTrue(var.match_namespace("{tns}a"))

        var = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, name="foo", namespaces=("##any",)
        )
        self.assertTrue(var.match_namespace("a"))
        self.assertTrue(var.match_namespace("{tns}a"))

        var = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, name="foo", namespaces=("",)
        )
        self.assertTrue(var.match_namespace("a"))
        self.assertFalse(var.match_namespace("{tns}a"))

        var = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, name="foo", namespaces=("!tns",)
        )
        self.assertTrue(var.match_namespace("{foo}a"))
        self.assertFalse(var.match_namespace("{tns}a"))

        var.namespace_matches["{tns}cached"] = True
        self.assertTrue(var.match_namespace("{tns}cached"))

    def test_eq(self):
        var = XmlVarFactory.create(name="foo", types=(int, float))
        clone = copy.deepcopy(var)
        self.assertEqual(var, clone)

        clone.default = 1
        self.assertNotEqual(var, clone)
        self.assertNotEqual(var, 1)
        self.assertNotEqual(1, var)

    def test_repr(self):
        var = XmlVarFactory.create(name="foo", types=(int, float))
        expected = (
            "XmlVar("
            "index=0, "
            "name=foo, "
            "qname=foo, "
            "types=(<class 'int'>, <class 'float'>), "
            "init=True, "
            "mixed=False, "
            "tokens=False, "
            "format=None, "
            "derived=False, "
            "any_type=False, "
            "nillable=False, "
            "sequential=False, "
            "list_element=False, "
            "default=None, "
            "xml_type=Element, "
            "namespaces=(), "
            "elements={}, "
            "wildcards=[])"
        )
        self.assertEqual(expected, repr(var))


class XmlMetaTests(TestCase):
    def setUp(self) -> None:
        a = make_dataclass("a", [])
        self.meta = XmlMetaFactory.create(
            clazz=a,
            qname="a",
            choices=[],
            wildcards=[],
            attributes={},
            elements={},
            any_attributes=[],
        )

    def test_find_attribute(self):
        a = XmlVarFactory.create(xml_type=XmlType.ATTRIBUTE, name="a")
        b = XmlVarFactory.create(xml_type=XmlType.ATTRIBUTE, name="b")

        self.meta.attributes[a.qname] = a
        self.meta.attributes[b.qname] = b

        self.assertEqual(a, self.meta.find_attribute("a"))
        self.assertEqual(b, self.meta.find_attribute("b"))

    def test_find_elements(self):
        a_1 = XmlVarFactory.create(xml_type=XmlType.ATTRIBUTE, qname="a", name="a_1")
        a_2 = XmlVarFactory.create(xml_type=XmlType.ATTRIBUTE, qname="a", name="a_2")

        self.meta.elements[a_1.qname] = [a_1, a_2]

        self.assertEqual([a_1, a_2], self.meta.find_elements("a"))
        self.assertEqual([], self.meta.find_elements("b"))

    @mock.patch.object(XmlVar, "find_choice")
    def test_find_choice(self, mock_find_choice):
        a_1 = XmlVarFactory.create(xml_type=XmlType.ATTRIBUTE, qname="a", name="a_1")
        a_2 = XmlVarFactory.create(xml_type=XmlType.ATTRIBUTE, qname="a", name="a_2")

        mock_find_choice.side_effect = [None, None, None, a_1, a_2]
        choice_1 = XmlVarFactory.create(
            xml_type=XmlType.ATTRIBUTE, qname="compound_1", name="compound_1"
        )
        choice_2 = XmlVarFactory.create(
            xml_type=XmlType.ATTRIBUTE, qname="compound_2", name="compound_2"
        )
        self.meta.choices = [choice_1, choice_2]

        self.assertIsNone(self.meta.find_choice("a"))
        self.assertEqual(a_1, self.meta.find_choice("a"))
        self.assertEqual(a_2, self.meta.find_choice("a"))

        mock_find_choice.assert_has_calls([mock.call("a") for _ in range(5)])

    @mock.patch.object(XmlVar, "match_namespace")
    def test_find_any_attributes(self, mock_match_namespace):
        mock_match_namespace.side_effect = [False, False, False, True]

        attributes = [
            XmlVarFactory.create(xml_type=XmlType.ATTRIBUTES, qname="any", name="any"),
            XmlVarFactory.create(
                xml_type=XmlType.ATTRIBUTES, qname="other", name="any"
            ),
        ]
        self.meta.any_attributes = attributes

        self.assertIsNone(self.meta.find_any_attributes("a"))
        self.assertEqual(attributes[1], self.meta.find_any_attributes("a"))

        mock_match_namespace.assert_has_calls([mock.call("a") for _ in range(4)])

    @mock.patch.object(XmlVar, "match_namespace")
    def test_find_wildcard(self, mock_match_namespace):
        mock_match_namespace.side_effect = [False, False, False, True]

        wildcards = [
            XmlVarFactory.create(xml_type=XmlType.WILDCARD, qname="any", name="any"),
            XmlVarFactory.create(xml_type=XmlType.WILDCARD, qname="other", name="any"),
        ]
        self.meta.wildcards = wildcards

        self.assertIsNone(self.meta.find_wildcard("a"))
        self.assertEqual(wildcards[1], self.meta.find_wildcard("a"))

        mock_match_namespace.assert_has_calls([mock.call("a") for _ in range(4)])

    def test_find_children(self):
        element1 = XmlVarFactory.create(xml_type=XmlType.ELEMENT, name="a")
        element2 = XmlVarFactory.create(xml_type=XmlType.ELEMENT, qname="a", name="a1")

        option1 = XmlVarFactory.create(xml_type=XmlType.ELEMENT, qname="a", name="a3")
        option2 = XmlVarFactory.create(xml_type=XmlType.ELEMENT, name="b")

        choice = XmlVarFactory.create(
            xml_type=XmlType.ELEMENTS,
            qname="c1",
            name="c1",
            elements={
                "a": option1,
                "b": option2,
            },
        )
        wildcard = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, qname="any", name="any"
        )

        self.meta.elements["a"] = [element1, element2]
        self.meta.choices.append(choice)
        self.meta.wildcards.append(wildcard)

        result = self.meta.find_children("a")
        self.assertIsInstance(result, Iterator)
        self.assertEqual([element1, element2, option1, wildcard], list(result))

    def test_repr(self):
        expected = (
            "XmlMeta("
            "clazz=<class 'types.a'>, "
            "qname=a, "
            "source_qname=a, "
            "nillable=False, "
            "text=None, "
            "choices=[], "
            "elements={}, "
            "wildcards=[], "
            "attributes={}, "
            "any_attributes=[])"
        )
        self.assertEqual(expected, repr(self.meta))
