import sys

from xsdata.codegen.models import SIMPLE_TYPES
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.utils.namespaces import build_qname
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class ClassTests(FactoryTestCase):
    def test_dependencies(self):
        obj = ClassFactory.create(
            attrs=[
                AttrFactory.create(types=[AttrTypeFactory.native(DataType.DECIMAL)]),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(
                            qname=build_qname(Namespace.XS.uri, "annotated"),
                            forward=True,
                        )
                    ],
                    choices=[
                        AttrFactory.create(
                            name="x",
                            types=[
                                AttrTypeFactory.create(qname="choiceAttr"),
                                AttrTypeFactory.native(DataType.STRING),
                            ],
                        ),
                        AttrFactory.create(
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
                ExtensionFactory.reference(build_qname(Namespace.XS.uri, "foobar")),
                ExtensionFactory.reference(build_qname(Namespace.XS.uri, "foobar")),
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
        obj = ClassFactory.create(tag=Tag.ELEMENT)
        self.assertTrue(obj.is_complex)

        obj = ClassFactory.create(tag=Tag.COMPLEX_TYPE)
        self.assertTrue(obj.is_complex)

        obj = ClassFactory.create(tag=Tag.SIMPLE_TYPE)
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

        obj.extensions.append(ExtensionFactory.create())
        self.assertFalse(obj.is_simple_type)

    def test_property_should_generate(self):
        obj = ClassFactory.create(tag=Tag.ELEMENT)
        self.assertTrue(obj.should_generate)

        obj = ClassFactory.create(tag=Tag.COMPLEX_TYPE)
        self.assertTrue(obj.should_generate)

        obj.attrs.append(AttrFactory.create(tag=Tag.EXTENSION))
        self.assertFalse(obj.should_generate)

        obj = ClassFactory.create(tag=Tag.BINDING_OPERATION)
        self.assertTrue(obj.should_generate)

        obj = ClassFactory.create(tag=Tag.BINDING_MESSAGE)
        self.assertTrue(obj.should_generate)

        obj = ClassFactory.enumeration(2)
        self.assertTrue(obj.should_generate)

        obj = ClassFactory.create(tag=Tag.SIMPLE_TYPE)
        self.assertFalse(obj.should_generate)
