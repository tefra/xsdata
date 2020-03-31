from lxml.etree import QName

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase


class ClassTests(FactoryTestCase):
    def test_dependencies(self):
        obj = ClassFactory.create(
            attrs=[
                AttrFactory.create(types=[AttrTypeFactory.xs_decimal()]),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(name="xs:annotated", forward_ref=True)
                    ]
                ),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(name="xs:openAttrs"),
                        AttrTypeFactory.create(name="xs:localAttribute"),
                    ]
                ),
            ],
            extensions=ExtensionFactory.list(
                1, type=AttrTypeFactory.create(name="xs:localElement")
            ),
            inner=[
                ClassFactory.create(
                    attrs=AttrFactory.list(2, types=AttrTypeFactory.list(1, name="foo"))
                )
            ],
        )

        expected = {
            QName("{http://www.w3.org/2001/XMLSchema}localAttribute"),
            QName("{http://www.w3.org/2001/XMLSchema}localElement"),
            QName("{http://www.w3.org/2001/XMLSchema}openAttrs"),
            QName("{xsdata}foo"),
        }
        self.assertEqual(expected, obj.dependencies())

    def test_source_qname(self):
        obj = ClassFactory.create()
        self.assertEqual(QName(obj.source_namespace, obj.name), obj.source_qname())

        self.assertEqual(QName("x", "x").text, obj.source_qname("x:x").text)
        self.assertNotIn("x", obj.nsmap)

        obj.nsmap["foo"] = "bar"
        self.assertEqual(QName("bar", "foo"), obj.source_qname("foo:foo"))

    def test_property_source_prefix(self):
        namespace = "http://xsdata.foo"
        obj = ClassFactory.create(nsmap={None: namespace}, source_namespace=namespace)

        self.assertIsNone(obj.source_prefix)

        obj.source_namespace = None
        self.assertIsNone(obj.source_prefix)

        obj.source_namespace = "tns"
        self.assertEqual("tns", obj.source_prefix)

        obj.nsmap["foo"] = namespace
        obj.source_namespace = namespace
        self.assertEqual("foo", obj.source_prefix)
