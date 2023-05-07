import sys
from typing import Iterator
from unittest import mock

from xsdata.codegen.mappers.dtd import DtdMapper
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.models.dtd import DtdAttributeDefault
from xsdata.models.dtd import DtdAttributeType
from xsdata.models.dtd import DtdContentOccur
from xsdata.models.dtd import DtdContentType
from xsdata.models.dtd import DtdElementType
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import DtdAttributeFactory
from xsdata.utils.testing import DtdContentFactory
from xsdata.utils.testing import DtdElementFactory
from xsdata.utils.testing import DtdFactory
from xsdata.utils.testing import FactoryTestCase


class DtdMapperTests(FactoryTestCase):
    def test_map(self):
        dtd = DtdFactory.root(2, location="tests.dtd")
        result = DtdMapper.map(dtd)

        self.assertIsInstance(result, Iterator)
        for cls in result:
            self.assertIsInstance(cls, Class)
            self.assertEqual(cls.location, dtd.location)

    @mock.patch.object(DtdMapper, "build_attributes")
    @mock.patch.object(DtdMapper, "build_elements")
    def test_build_class(self, mock_build_elements, mock_build_attributes):
        location = "tests.dtd"
        element = DtdElementFactory.create(
            name="root", prefix="ns", ns_map={"ns": "xsdata"}
        )
        actual = DtdMapper.build_class(element, "tests.dtd")
        expected = ClassFactory.create(
            qname="{xsdata}root",
            ns_map=element.ns_map,
            tag=Tag.ELEMENT,
            location=location,
            module=None,
        )

        self.assertEqual(expected, actual)

        mock_build_attributes.assert_called_once_with(actual, element)
        mock_build_elements.assert_called_once_with(actual, element)

    @mock.patch.object(DtdMapper, "build_attribute")
    def test_build_attributes(self, mock_build_attribute):
        attributes = DtdAttributeFactory.list(2)
        element = DtdElementFactory.create(attributes=attributes)
        target = ClassFactory.create()

        DtdMapper.build_attributes(target, element)

        mock_build_attribute.assert_has_calls(
            [
                mock.call(target, attributes[0]),
                mock.call(target, attributes[1]),
            ]
        )

    def test_build_attribute(self):
        target = ClassFactory.create()
        attribute = DtdAttributeFactory.create(
            name="lang", prefix="xml", default=DtdAttributeDefault.IMPLIED
        )
        DtdMapper.build_attribute(target, attribute)

        self.assertEqual(1, len(target.attrs))
        attr = target.attrs[0]

        self.assertEqual(0, attr.index)
        self.assertEqual(attribute.name, attr.name)
        self.assertEqual(Tag.ATTRIBUTE, attr.tag)
        self.assertEqual(Namespace.XML.uri, attr.namespace)
        self.assertEqual(1, len(attr.types))
        self.assertEqual(AttrTypeFactory.native(DataType.STRING), attr.types[0])
        self.assertEqual(1, attr.restrictions.max_occurs)
        self.assertEqual(0, attr.restrictions.min_occurs)

    def test_build_attribute_type_with_enumeration(self):
        target = ClassFactory.create()
        attribute = DtdAttributeFactory.create(
            type=DtdAttributeType.ENUMERATION, values=["a", "b", "c"]
        )
        actual = DtdMapper.build_attribute_type(target, attribute)

        self.assertTrue(actual.forward)
        self.assertEqual(attribute.name, actual.qname)

        self.assertEqual(1, len(target.inner))
        self.assertTrue(target.inner[0].is_enumeration)

        self.assertEqual(["a", "b", "c"], [x.name for x in target.inner[0].attrs])
        self.assertEqual(["a", "b", "c"], [x.default for x in target.inner[0].attrs])

        for attr in target.inner[0].attrs:
            self.assertEqual(Tag.ENUMERATION, attr.tag)
            self.assertTrue(attr.fixed)
            self.assertEqual([AttrTypeFactory.native(DataType.STRING)], attr.types)

    def test_build_attribute_restrictions_with_default_required(self):
        attr = AttrFactory.create()
        DtdMapper.build_attribute_restrictions(attr, DtdAttributeDefault.REQUIRED, "")
        self.assertEqual(1, attr.restrictions.max_occurs)
        self.assertEqual(1, attr.restrictions.min_occurs)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_build_attribute_restrictions_with_default_implied(self):
        attr = AttrFactory.create()
        DtdMapper.build_attribute_restrictions(attr, DtdAttributeDefault.IMPLIED, "")
        self.assertEqual(1, attr.restrictions.max_occurs)
        self.assertEqual(0, attr.restrictions.min_occurs)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_build_attribute_restrictions_with_default_fixed(self):
        attr = AttrFactory.create()
        DtdMapper.build_attribute_restrictions(attr, DtdAttributeDefault.FIXED, "abc")
        self.assertEqual(1, attr.restrictions.max_occurs)
        self.assertEqual(1, attr.restrictions.min_occurs)
        self.assertTrue(attr.fixed)
        self.assertEqual("abc", attr.default)

    def test_build_attribute_restrictions_with_default_none_and_no_value(self):
        attr = AttrFactory.create()
        DtdMapper.build_attribute_restrictions(attr, DtdAttributeDefault.NONE, None)
        self.assertEqual(1, attr.restrictions.max_occurs)
        self.assertEqual(0, attr.restrictions.min_occurs)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_build_attribute_restrictions_with_default_none_and_default_value(self):
        attr = AttrFactory.create()
        DtdMapper.build_attribute_restrictions(attr, DtdAttributeDefault.NONE, "abc")
        self.assertEqual(1, attr.restrictions.max_occurs)
        self.assertEqual(1, attr.restrictions.min_occurs)
        self.assertFalse(attr.fixed)
        self.assertEqual("abc", attr.default)

    def test_build_elements_with_mixed_element_type(self):
        target = ClassFactory.create(tag=Tag.ELEMENT)
        left = DtdContentFactory.create(
            type=DtdContentType.PCDATA, occur=DtdContentOccur.ONCE
        )
        right = DtdContentFactory.create(
            name="rad", type=DtdContentType.ELEMENT, occur=DtdContentOccur.ONCE
        )
        element = DtdElementFactory.create(
            type=DtdElementType.MIXED,
            content=DtdContentFactory.create(
                type=DtdContentType.OR, left=left, right=right
            ),
        )

        DtdMapper.build_elements(target, element)
        expected = [
            AttrFactory.create(
                tag=Tag.ELEMENT,
                name="rad",
                index=1,
                types=[AttrTypeFactory.create(qname="rad")],
            ),
        ]

        self.assertTrue(target.mixed)
        self.assertEqual(expected, target.attrs)
        self.assertEqual(Tag.COMPLEX_TYPE, target.tag)

        element.content.left = right
        element.content.right = left

        target.attrs.clear()
        target.mixed = False
        DtdMapper.build_elements(target, element)
        self.assertTrue(target.mixed)
        self.assertEqual(expected, target.attrs)
        self.assertEqual(Tag.COMPLEX_TYPE, target.tag)

    def test_build_elements_with_mixed_element_type_with_no_content(self):
        target = ClassFactory.create(tag=Tag.ELEMENT)
        element = DtdElementFactory.create(
            type=DtdElementType.MIXED,
            content=DtdContentFactory.create(
                type=DtdContentType.PCDATA,
            ),
        )

        DtdMapper.build_elements(target, element)
        expected = [
            AttrFactory.create(
                tag=Tag.EXTENSION,
                name="value",
                index=0,
                types=[AttrTypeFactory.native(DataType.STRING)],
            ),
        ]

        self.assertFalse(target.mixed)
        self.assertEqual(expected, target.attrs)
        self.assertEqual(Tag.COMPLEX_TYPE, target.tag)

    def test_build_elements_with_any_element_type(self):
        target = ClassFactory.create()
        element = DtdElementFactory.create(type=DtdElementType.ANY)

        DtdMapper.build_elements(target, element)
        self.assertEqual(0, len(target.attrs))
        self.assertEqual(1, len(target.extensions))

        self.assertEqual(str(DataType.ANY_TYPE), target.extensions[0].type.qname)
        self.assertTrue(target.extensions[0].type.native)

        self.assertFalse(target.mixed)

    def test_build_elements_with_undefined_element_type(self):
        target = ClassFactory.create()
        element = DtdElementFactory.create(type=DtdElementType.UNDEFINED)

        DtdMapper.build_elements(target, element)
        self.assertEqual(0, len(target.attrs))
        self.assertEqual(0, len(target.extensions))
        self.assertFalse(target.mixed)

    def test_build_elements_with_empty_element_type(self):
        target = ClassFactory.create()
        element = DtdElementFactory.create(type=DtdElementType.EMPTY)

        DtdMapper.build_elements(target, element)
        self.assertEqual(0, len(target.attrs))
        self.assertEqual(0, len(target.extensions))
        self.assertFalse(target.mixed)

    def test_build_elements_with_element_element_type(self):
        target = ClassFactory.create()
        element = DtdElementFactory.create(
            type=DtdElementType.ELEMENT, content=DtdContentFactory.create(name="child")
        )

        DtdMapper.build_elements(target, element)
        self.assertEqual(1, len(target.attrs))
        self.assertEqual(0, len(target.extensions))
        self.assertFalse(target.mixed)

    def test_build_content_with_type_element(self):
        content = DtdContentFactory.create(
            type=DtdContentType.ELEMENT, occur=DtdContentOccur.ONCE
        )
        target = ClassFactory.create()
        DtdMapper.build_content(target, content, nillable=True)
        self.assertEqual(1, len(target.attrs))
        self.assertEqual(content.name, target.attrs[0].name)
        self.assertTrue(target.attrs[0].restrictions.nillable)
        self.assertEqual(1, target.attrs[0].restrictions.max_occurs)
        self.assertEqual(1, target.attrs[0].restrictions.min_occurs)

    def test_build_content_type_seq(self):
        content = DtdContentFactory.create(
            type=DtdContentType.SEQ,
            left=DtdContentFactory.create(type=DtdContentType.ELEMENT),
            right=DtdContentFactory.create(type=DtdContentType.ELEMENT),
        )
        target = ClassFactory.create()
        DtdMapper.build_content(target, content, nillable=True)
        self.assertEqual(2, len(target.attrs))
        self.assertTrue(target.attrs[0].restrictions.nillable)
        self.assertTrue(target.attrs[1].restrictions.nillable)

    def test_build_content_type_or(self):
        content = DtdContentFactory.create(
            type=DtdContentType.OR,
            occur=DtdContentOccur.MULT,
            left=DtdContentFactory.create(type=DtdContentType.ELEMENT),
            right=DtdContentFactory.create(type=DtdContentType.ELEMENT),
        )
        target = ClassFactory.create()
        DtdMapper.build_content(target, content, nillable=True)
        self.assertEqual(2, len(target.attrs))
        for attr in target.attrs:
            self.assertEqual(id(content), attr.restrictions.choice)
            self.assertEqual(0, attr.restrictions.min_occurs)
            self.assertEqual(sys.maxsize, attr.restrictions.max_occurs)

    def test_build_content_type_or_nested(self):
        content = DtdContentFactory.create(
            type=DtdContentType.OR,
            left=DtdContentFactory.create(type=DtdContentType.ELEMENT),
            right=DtdContentFactory.create(type=DtdContentType.ELEMENT),
        )
        target = ClassFactory.create()
        DtdMapper.build_content(target, content, min_occurs=1, choice="abc")
        self.assertEqual(2, len(target.attrs))
        for attr in target.attrs:
            self.assertEqual("abc", attr.restrictions.choice)
            self.assertEqual(1, attr.restrictions.min_occurs)

    def test_build_content_type_pcdata(self):
        content = DtdContentFactory.create(
            type=DtdContentType.PCDATA,
        )
        target = ClassFactory.create()
        DtdMapper.build_content(target, content)

        expected = [
            AttrFactory.create(
                tag=Tag.EXTENSION,
                name="value",
                index=0,
                types=[AttrTypeFactory.native(DataType.STRING)],
            )
        ]
        self.assertEqual(expected, target.attrs)

    @mock.patch.object(DtdMapper, "build_content")
    def test_build_content_tree(self, mock_build_content):
        center = DtdContentFactory.create()
        target = ClassFactory.create()

        DtdMapper.build_content_tree(target, center, nillable=True)

        center.left = DtdContentFactory.create()
        center.right = DtdContentFactory.create()
        DtdMapper.build_content_tree(target, center, nillable=False)

        mock_build_content.assert_has_calls(
            [
                mock.call(target, center.left, nillable=False),
                mock.call(target, center.right, nillable=False),
            ]
        )

    def test_build_restrictions(self):
        result = DtdMapper.build_restrictions(DtdContentOccur.ONCE)
        self.assertEqual(1, result.min_occurs)
        self.assertEqual(1, result.max_occurs)

        result = DtdMapper.build_restrictions(DtdContentOccur.OPT)
        self.assertEqual(0, result.min_occurs)
        self.assertEqual(1, result.max_occurs)

        result = DtdMapper.build_restrictions(DtdContentOccur.MULT)
        self.assertEqual(0, result.min_occurs)
        self.assertEqual(sys.maxsize, result.max_occurs)

        result = DtdMapper.build_restrictions(DtdContentOccur.PLUS)
        self.assertEqual(1, result.min_occurs)
        self.assertEqual(sys.maxsize, result.max_occurs)

        result = DtdMapper.build_restrictions(DtdContentOccur.PLUS, nillable=True)
        self.assertEqual(1, result.min_occurs)
        self.assertEqual(sys.maxsize, result.max_occurs)
        self.assertTrue(result.nillable)

        result = DtdMapper.build_restrictions(DtdContentOccur.PLUS, min_occurs=0)
        self.assertEqual(0, result.min_occurs)

    def test_build_element(self):
        target = ClassFactory.create()
        restrictions = Restrictions()
        names = ["firs", "second", "third"]

        for name in names:
            DtdMapper.build_element(target, name, restrictions)

        self.assertEqual(len(names), len(target.attrs))

        for index, attr in enumerate(target.attrs):
            self.assertEqual(names[index], attr.name)
            self.assertEqual(index, attr.index)
            self.assertEqual(Tag.ELEMENT, attr.tag)
            self.assertEqual(restrictions, attr.restrictions)
            self.assertIsNot(restrictions, attr.restrictions)

            self.assertEqual(1, len(attr.types))
            self.assertFalse(attr.types[0].native)
            self.assertEqual(names[index], attr.types[0].qname)
