import sys

from lxml.etree import QName

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.models.enums import Namespace
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import SimpleType


class ClassTests(FactoryTestCase):
    def test_dependencies(self):
        obj = ClassFactory.create(
            attrs=[
                AttrFactory.create(types=[AttrTypeFactory.xs_decimal()]),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(
                            qname=QName(Namespace.XS.uri, "annotated"), forward=True
                        )
                    ]
                ),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(
                            qname=QName(Namespace.XS.uri, "openAttrs")
                        ),
                        AttrTypeFactory.create(
                            qname=QName(Namespace.XS.uri, "localAttribute")
                        ),
                    ]
                ),
            ],
            extensions=[
                ExtensionFactory.create(
                    type=AttrTypeFactory.create(qname=QName(Namespace.XS.uri, "foobar"))
                ),
                ExtensionFactory.create(
                    type=AttrTypeFactory.create(qname=QName(Namespace.XS.uri, "foobar"))
                ),
            ],
            inner=[
                ClassFactory.create(
                    attrs=AttrFactory.list(
                        2, types=AttrTypeFactory.list(1, qname="foo")
                    )
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
