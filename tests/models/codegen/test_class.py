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
