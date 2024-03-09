import sys

from xsdata.codegen.exceptions import CodegenError
from xsdata.models.enums import DataType, Namespace, Tag
from xsdata.utils.namespaces import build_qname
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    ExtensionFactory,
    FactoryTestCase,
)


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
                        ),
                        AttrTypeFactory.create(
                            qname="circular",
                            circular=True,
                        ),
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
                        2,
                        types=[
                            AttrTypeFactory.create(qname="{xsdata}foo"),
                            AttrTypeFactory.create(
                                qname="{xsdata}circular", circular=True
                            ),
                        ],
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
        self.assertIn("circular", list(obj.dependencies(allow_circular=True)))
        self.assertIn("{xsdata}circular", list(obj.dependencies(allow_circular=True)))

    def test_property_has_suffix_attr(self):
        obj = ClassFactory.create()

        self.assertFalse(obj.has_suffix_attr)

        obj.attrs.append(AttrFactory.create())
        obj.attrs.append(AttrFactory.create())
        self.assertFalse(obj.has_suffix_attr)

        obj.attrs[1].index = sys.maxsize
        self.assertTrue(obj.has_suffix_attr)

    def test_property_is_element(self):
        obj = ClassFactory.create(tag=Tag.ELEMENT)
        self.assertTrue(obj.is_element)

        obj = ClassFactory.create(tag=Tag.SIMPLE_TYPE)
        self.assertFalse(obj.is_element)

    def test_property_is_enumeration(self):
        obj = ClassFactory.enumeration(2)
        self.assertTrue(obj.is_enumeration)

        obj.attrs.append(AttrFactory.element())
        self.assertFalse(obj.is_enumeration)

        obj.attrs.clear()
        self.assertFalse(obj.is_enumeration)

    def test_property_is_restricted(self):
        obj = ClassFactory.create()
        ext = ExtensionFactory.create(tag=Tag.EXTENSION)
        obj.extensions.append(ext)

        self.assertFalse(obj.is_restricted)

        ext.tag = Tag.RESTRICTION
        self.assertTrue(obj.is_restricted)

    def test_property_is_group(self):
        self.assertTrue(ClassFactory.create(tag=Tag.GROUP).is_group)
        self.assertTrue(ClassFactory.create(tag=Tag.ATTRIBUTE_GROUP).is_group)
        self.assertFalse(ClassFactory.create(tag=Tag.ELEMENT).is_group)

    def test_property_ref(self):
        obj = ClassFactory.create()
        self.assertEqual(id(obj), obj.ref)

    def test_property_references(self):
        ext_1 = ExtensionFactory.create(AttrTypeFactory.create(reference=1))
        ext_2 = ExtensionFactory.create(AttrTypeFactory.create(reference=2))

        obj = ClassFactory.elements(3)
        obj.extensions.append(ext_1)
        obj.extensions.append(ext_2)

        obj.attrs[0].types[0].reference = 3
        obj.attrs[1].choices.append(AttrFactory.create())
        obj.attrs[1].choices[0].types[0].reference = 4
        obj.attrs[2].types[0].reference = 5

        obj.inner.append(ClassFactory.elements(2))
        obj.inner[0].attrs[1].types[0].reference = 6

        self.assertEqual(list(range(1, 7)), list(obj.references))

    def test_property_target_module(self):
        obj = ClassFactory.create(module=None, package=None)
        with self.assertRaises(CodegenError):
            obj.target_module

        obj.module = "bar"
        self.assertEqual("bar", obj.target_module)

        obj.package = "foo"
        self.assertEqual("foo.bar", obj.target_module)

    def test_property_is_mixed(self):
        obj = ClassFactory.create()
        self.assertFalse(obj.is_mixed)

        obj.attrs.append(AttrFactory.any(mixed=True))
        self.assertTrue(obj.is_mixed)

        obj = ClassFactory.create(mixed=True)
        self.assertTrue(obj.is_mixed)

    def test_has_forward_ref(self):
        forward_type = AttrTypeFactory.create("foo", forward=True)
        circular_type = AttrTypeFactory.create("foo", circular=True)

        obj = ClassFactory.elements(1)
        self.assertFalse(obj.has_forward_ref())

        obj.attrs[0].types.append(forward_type)
        self.assertTrue(obj.has_forward_ref())

        obj.attrs[0].types.pop()
        obj.attrs[0].choices.append(AttrFactory.create())
        obj.attrs[0].choices.append(AttrFactory.create(types=[circular_type]))
        self.assertTrue(obj.has_forward_ref())

        obj.attrs.clear()
        self.assertFalse(obj.has_forward_ref())

        inner = ClassFactory.elements(1)
        inner.attrs[0].types.append(circular_type)
        obj.inner.append(inner)
        self.assertTrue(obj.has_forward_ref())
