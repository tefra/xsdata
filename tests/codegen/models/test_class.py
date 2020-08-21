import sys

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.models import wsdl
from xsdata.models import xsd
from xsdata.models.enums import Namespace
from xsdata.utils import text


class ClassTests(FactoryTestCase):
    def test_dependencies(self):
        obj = ClassFactory.create(
            attrs=[
                AttrFactory.create(types=[AttrTypeFactory.xs_decimal()]),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(
                            qname=text.qname(Namespace.XS.uri, "annotated"),
                            forward=True,
                        )
                    ]
                ),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(
                            qname=text.qname(Namespace.XS.uri, "openAttrs")
                        ),
                        AttrTypeFactory.create(
                            qname=text.qname(Namespace.XS.uri, "localAttribute")
                        ),
                    ]
                ),
            ],
            extensions=[
                ExtensionFactory.create(
                    type=AttrTypeFactory.create(
                        qname=text.qname(Namespace.XS.uri, "foobar")
                    )
                ),
                ExtensionFactory.create(
                    type=AttrTypeFactory.create(
                        qname=text.qname(Namespace.XS.uri, "foobar")
                    )
                ),
            ],
            inner=[
                ClassFactory.create(
                    attrs=AttrFactory.list(
                        2, types=AttrTypeFactory.list(1, qname="{xsdata}foo")
                    )
                )
            ],
        )

        expected = [
            text.qname("{http://www.w3.org/2001/XMLSchema}openAttrs"),
            text.qname("{http://www.w3.org/2001/XMLSchema}localAttribute"),
            text.qname("{http://www.w3.org/2001/XMLSchema}foobar"),
            text.qname("{xsdata}foo"),
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

    def test_property_is_complex(self):
        obj = ClassFactory.create(type=xsd.Element)
        self.assertTrue(obj.is_complex)

        obj = ClassFactory.create(type=xsd.ComplexType)
        self.assertTrue(obj.is_complex)

        obj = ClassFactory.create(type=xsd.SimpleType)
        self.assertFalse(obj.is_complex)

    def test_property_is_enumeration(self):
        obj = ClassFactory.enumeration(2)
        self.assertTrue(obj.is_enumeration)

        obj.attrs.append(AttrFactory.element())
        self.assertFalse(obj.is_enumeration)

        obj.attrs.clear()
        self.assertFalse(obj.is_enumeration)

    def test_property_should_generate(self):
        obj = ClassFactory.create(type=xsd.Element)
        self.assertTrue(obj.should_generate)

        obj = ClassFactory.create(type=xsd.ComplexType)
        self.assertTrue(obj.should_generate)

        obj = ClassFactory.create(type=wsdl.BindingOperation)
        self.assertTrue(obj.should_generate)

        obj = ClassFactory.create(type=wsdl.BindingMessage)
        self.assertTrue(obj.should_generate)

        obj = ClassFactory.enumeration(2)
        self.assertTrue(obj.should_generate)

        obj = ClassFactory.create(type=xsd.SimpleType)
        self.assertFalse(obj.should_generate)

        obj = ClassFactory.create(type=wsdl.BindingMessage, strict_type=True)
        self.assertFalse(obj.should_generate)
