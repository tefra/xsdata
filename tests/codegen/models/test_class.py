import sys

from tests.factories import AttrChoiceFactory
from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.models import AttrChoice
from xsdata.codegen.models import SIMPLE_TYPES
from xsdata.models import wsdl
from xsdata.models import xsd
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.utils.namespaces import build_qname


class ClassTests(FactoryTestCase):
    def test_dependencies(self):
        obj = ClassFactory.create(
            attrs=[
                AttrFactory.create(types=[AttrTypeFactory.xs_decimal()]),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(
                            qname=build_qname(Namespace.XS.uri, "annotated"),
                            forward=True,
                        )
                    ],
                    choices=[
                        AttrChoiceFactory.create(
                            name="x",
                            types=[
                                AttrTypeFactory.create(qname="choiceAttr"),
                                AttrTypeFactory.xs_string(),
                            ],
                        ),
                        AttrChoiceFactory.create(
                            name="x",
                            types=[
                                AttrTypeFactory.create(qname="choiceAttrTwo"),
                                AttrTypeFactory.create(qname="choiceAttrEnum"),
                            ],
                        ),
                    ],
                ),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(
                            qname=build_qname(Namespace.XS.uri, "openAttrs")
                        ),
                        AttrTypeFactory.create(
                            qname=build_qname(Namespace.XS.uri, "localAttribute")
                        ),
                    ]
                ),
            ],
            extensions=[
                ExtensionFactory.create(
                    type=AttrTypeFactory.create(
                        qname=build_qname(Namespace.XS.uri, "foobar")
                    )
                ),
                ExtensionFactory.create(
                    type=AttrTypeFactory.create(
                        qname=build_qname(Namespace.XS.uri, "foobar")
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
            "choiceAttr",
            "choiceAttrTwo",
            "choiceAttrEnum",
            "{http://www.w3.org/2001/XMLSchema}openAttrs",
            "{http://www.w3.org/2001/XMLSchema}localAttribute",
            "{http://www.w3.org/2001/XMLSchema}foobar",
            "{xsdata}foo",
        ]
        self.assertCountEqual(expected, list(obj.dependencies()))

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

    def test_is_simple_type(self):
        obj = ClassFactory.elements(2)

        self.assertFalse(obj.is_simple_type)

        obj.attrs.pop()
        self.assertFalse(obj.is_simple_type)

        for tag in SIMPLE_TYPES:
            obj.attrs[0].tag = tag
            self.assertTrue(obj.is_simple_type)

    def test_property_should_generate(self):
        obj = ClassFactory.create(type=xsd.Element)
        self.assertTrue(obj.should_generate)

        obj = ClassFactory.create(type=xsd.ComplexType)
        self.assertTrue(obj.should_generate)

        obj.attrs.append(AttrFactory.create(tag=Tag.EXTENSION))
        self.assertFalse(obj.should_generate)

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
