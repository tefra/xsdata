from dataclasses import dataclass
from unittest.case import TestCase

from lxml.etree import QName

from tests.fixtures import BookForm
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlAttribute
from xsdata.formats.dataclass.models.elements import XmlAttributes
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.elements import XmlWildcard
from xsdata.models.enums import QNames


@dataclass
class Fixture:
    a: int


class XmlValTests(TestCase):
    def test_property_clazz(self):
        var = XmlVar(name="foo", qname=QName("foo"))
        self.assertIsNone(var.clazz)

        var = XmlVar(name="foo", qname=QName("foo"), dataclass=True, types=[Fixture])
        self.assertEqual(Fixture, var.clazz)

    def test_property_is_list(self):
        var = XmlVar(name="foo", qname=QName("foo"))
        self.assertFalse(var.is_list)

        var = XmlVar(name="foo", qname=QName("foo"), types=[int], default=list)
        self.assertTrue(var.is_list)

    def test_default_properties(self):
        var = XmlVar(name="foo", qname=QName("foo"))
        self.assertFalse(var.is_any_type)
        self.assertFalse(var.is_attribute)
        self.assertFalse(var.is_attributes)
        self.assertFalse(var.is_wildcard)
        self.assertFalse(var.is_element)
        self.assertFalse(var.is_text)
        self.assertFalse(var.is_tokens)

    def test_matches(self):
        var = XmlVar(name="foo", qname=QName("foo"))
        self.assertTrue(var.matches(QNames.ALL))
        self.assertTrue(var.matches(var.qname))
        self.assertFalse(var.matches(QName("bar")))


class XmlElementTests(TestCase):
    def test_property_is_element(self):
        var = XmlElement(name="foo", qname=QName("foo"))

        self.assertIsInstance(var, XmlVar)
        self.assertTrue(var.is_element)

    def test_property_is_any_type(self):
        var = XmlElement(name="foo", qname=QName("foo"))
        self.assertFalse(var.is_any_type)

        var = XmlElement(name="foo", qname=QName("foo"), types=[int, object])
        self.assertFalse(var.is_any_type)

        var = XmlElement(name="foo", qname=QName("foo"), types=[object])
        self.assertTrue(var.is_any_type)


class XmlWildcardTests(TestCase):
    def test_property_is_wildcard(self):
        var = XmlWildcard(name="foo", qname=QName("foo"))

        self.assertIsInstance(var, XmlVar)
        self.assertTrue(var.is_wildcard)

    def test_property_is_any_type(self):
        var = XmlWildcard(name="foo", qname=QName("foo"))
        self.assertTrue(var.is_any_type)

    def test_matches(self):
        var = XmlWildcard(name="foo", qname=QName("foo"))
        self.assertTrue(var.matches(QNames.ALL))
        self.assertTrue(var.matches(QName("a")))

        var = XmlWildcard(name="foo", qname=QName("foo"), namespaces=["tns"])
        self.assertFalse(var.matches(QName("a")))
        self.assertTrue(var.matches(QName("tns", "a")))

        var = XmlWildcard(name="foo", qname=QName("foo"), namespaces=["##any"])
        self.assertTrue(var.matches(QName("a")))
        self.assertTrue(var.matches(QName("tns", "a")))

        var = XmlWildcard(name="foo", qname=QName("foo"), namespaces=[""])
        self.assertTrue(var.matches(QName("a")))
        self.assertFalse(var.matches(QName("tns", "a")))

        var = XmlWildcard(name="foo", qname=QName("foo"), namespaces=["!tns"])
        self.assertTrue(var.matches(QName("foo", "a")))
        self.assertFalse(var.matches(QName("tns", "a")))


class XmlAttributeTests(TestCase):
    def test_property_is_attribute(self):
        var = XmlAttribute(name="foo", qname=QName("foo"))

        self.assertIsInstance(var, XmlVar)
        self.assertTrue(var.is_attribute)


class XmlAttributesTests(TestCase):
    def test_property_is_attributes(self):
        var = XmlAttributes(name="foo", qname=QName("foo"))

        self.assertIsInstance(var, XmlVar)
        self.assertTrue(var.is_attributes)


class XmlTextTests(TestCase):
    def test_property_is_text(self):
        var = XmlText(name="foo", qname=QName("foo"))

        self.assertIsInstance(var, XmlVar)
        self.assertTrue(var.is_text)

    def test_property_is_tokens(self):
        var = XmlText(name="foo", qname=QName("foo"))
        self.assertFalse(var.is_tokens)

        var = XmlText(name="foo", qname=QName("foo"), default=list)
        self.assertTrue(var.is_tokens)


class XmlMeta(TestCase):
    def test_find_var(self):
        ctx = XmlContext()
        meta = ctx.build(BookForm)
        author = QName("author")

        self.assertIsInstance(meta.find_var(author), XmlElement)
        self.assertIsNone(meta.find_var(author, lambda x: not x.is_element))
        self.assertIsNone(meta.find_var(QName("nope")))
