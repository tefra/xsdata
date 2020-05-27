import sys

from lxml.etree import QName

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import SimpleType


class ClassTests(FactoryTestCase):
    def test_dependencies(self):
        obj = ClassFactory.create(
            attrs=[
                AttrFactory.create(types=[AttrTypeFactory.xs_decimal()]),
                AttrFactory.create(
                    types=[AttrTypeFactory.create(name="xs:annotated", forward=True)]
                ),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(name="xs:openAttrs"),
                        AttrTypeFactory.create(name="xs:localAttribute"),
                    ]
                ),
            ],
            extensions=[
                ExtensionFactory.create(type=AttrTypeFactory.create(name="xs:foobar")),
                ExtensionFactory.create(type=AttrTypeFactory.create(name="xs:foobar")),
            ],
            inner=[
                ClassFactory.create(
                    attrs=AttrFactory.list(2, types=AttrTypeFactory.list(1, name="foo"))
                )
            ],
        )

        expected = [
            QName("{http://www.w3.org/2001/XMLSchema}openAttrs"),
            QName("{http://www.w3.org/2001/XMLSchema}localAttribute"),
            QName("{http://www.w3.org/2001/XMLSchema}foobar"),
            QName("{xsdata}foo"),
        ]
        self.assertEqual(expected, list(obj.dependencies()))

    def test_source_qname(self):
        obj = ClassFactory.create()
        self.assertEqual(QName(obj.source_namespace, obj.name), obj.source_qname())

        self.assertEqual(QName("x", "x").text, obj.source_qname("x:x").text)
        self.assertNotIn("x", obj.ns_map)

        obj.ns_map["foo"] = "bar"
        self.assertEqual(QName("bar", "foo"), obj.source_qname("foo:foo"))

    def test_property_has_suffix_attr(self):
        obj = ClassFactory.create()

        self.assertFalse(obj.has_suffix_attr)

        obj.attrs.append(AttrFactory.create())
        obj.attrs.append(AttrFactory.create())
        self.assertFalse(obj.has_suffix_attr)

        obj.attrs[1].index = sys.maxsize
        self.assertTrue(obj.has_suffix_attr)

    def test_property_has_wild_attr(self):
        obj = ClassFactory.create()
        self.assertFalse(obj.has_wild_attr)

        obj.attrs.append(AttrFactory.create())
        obj.attrs.append(AttrFactory.create())
        self.assertFalse(obj.has_wild_attr)

        obj.attrs.append(AttrFactory.any())
        self.assertTrue(obj.has_wild_attr)

    def test_property_source_prefix(self):
        namespace = "http://xsdata.foo"
        obj = ClassFactory.create(ns_map={None: namespace}, source_namespace=namespace)

        self.assertIsNone(obj.source_prefix)

        obj.source_namespace = None
        self.assertIsNone(obj.source_prefix)

        obj.source_namespace = "tns"
        self.assertEqual("tns", obj.source_prefix)

        obj.ns_map["foo"] = namespace
        obj.source_namespace = namespace
        self.assertEqual("foo", obj.source_prefix)

    def test_property_is_complex(self):
        obj = ClassFactory.create(type=SimpleType)
        self.assertFalse(obj.is_complex)

        obj = ClassFactory.create(type=Element)
        self.assertTrue(obj.is_complex)

        obj = ClassFactory.create(type=ComplexType)
        self.assertTrue(obj.is_complex)

    def test_property_is_enumeration(self):
        obj = ClassFactory.enumeration(2)
        self.assertTrue(obj.is_enumeration)

        obj.attrs.append(AttrFactory.element())
        self.assertFalse(obj.is_enumeration)

        obj.attrs.clear()
        self.assertFalse(obj.is_enumeration)
