import sys
from unittest import mock

from xsdata.codegen.mappers.element import ElementMapper
from xsdata.codegen.models import Restrictions
from xsdata.codegen.utils import ClassUtils
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.enums import DataType
from xsdata.models.enums import QNames
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class ElementMapperTests(FactoryTestCase):
    @mock.patch.object(ClassUtils, "flatten")
    @mock.patch.object(ElementMapper, "build_class")
    def test_map(self, mock_build_class, mock_flatten):
        element = AnyElement(qname="{xsdata}root")
        root_class = ClassFactory.create()
        flat_classes = ClassFactory.list(5)
        iter_flat_classes = iter(flat_classes)

        mock_build_class.return_value = root_class
        mock_flatten.return_value = iter_flat_classes

        actual = ElementMapper.map(element, "tests")

        self.assertEqual(flat_classes, actual)
        mock_build_class.assert_called_once_with(element, "xsdata")
        mock_flatten.assert_called_once_with(root_class, "tests/root")

    def test_build_class_simple_type(self):
        element = AnyElement(
            qname="{xsdata}root",
            attributes={"{foo}bar": "1", "{bar}foo": "2.0"},
            text="true",
        )

        actual = ElementMapper.build_class(element, "target")
        expected = ClassFactory.create(
            tag=Tag.ELEMENT,
            qname="{xsdata}root",
            namespace="xsdata",
            location="",
            module=None,
            ns_map={},
            attrs=[
                AttrFactory.native(
                    DataType.INT,
                    tag=Tag.ATTRIBUTE,
                    name="bar",
                    namespace="foo",
                    index=0,
                ),
                AttrFactory.native(
                    DataType.FLOAT,
                    tag=Tag.ATTRIBUTE,
                    name="foo",
                    namespace="bar",
                    index=1,
                ),
                AttrFactory.native(
                    DataType.BOOLEAN,
                    tag=Tag.SIMPLE_TYPE,
                    name="value",
                    namespace=None,
                    index=2,
                ),
            ],
        )
        self.assertEqual(expected, actual)
        for attr in actual.attrs:
            self.assertEqual(1, attr.restrictions.min_occurs)
            self.assertEqual(1, attr.restrictions.max_occurs)

    def test_build_class_complex_type(self):
        element = AnyElement(
            qname="{xsdata}root",
            children=[
                AnyElement(qname="{xsdata}child", text="primitive"),
                AnyElement(
                    qname="{inner}child", attributes={"{foo}bar": "1", "{bar}foo": "2"}
                ),
            ],
        )

        actual = ElementMapper.build_class(element, "target")
        expected = ClassFactory.create(
            tag=Tag.ELEMENT,
            qname="{xsdata}root",
            namespace="xsdata",
            location="",
            module=None,
            ns_map={},
            attrs=[
                AttrFactory.native(
                    DataType.STRING,
                    tag=Tag.ELEMENT,
                    name="child",
                    namespace="xsdata",
                    index=0,
                ),
                AttrFactory.element(
                    name="child",
                    namespace="inner",
                    types=[AttrTypeFactory.create(qname="{target}child", forward=True)],
                    index=1,
                ),
            ],
        )
        self.assertEqual(1, len(actual.inner))

        actual.inner.clear()
        self.assertEqual(expected, actual)

    def test_build_class_with_sequences(self):
        element = AnyElement(
            qname="root",
            children=[
                AnyElement(qname="a"),
                AnyElement(qname="b"),
                AnyElement(qname="a"),
                AnyElement(qname="b"),
                AnyElement(qname="c"),
                AnyElement(qname="d"),
                AnyElement(qname="e"),
                AnyElement(qname="d"),
            ],
        )

        actual = ElementMapper.build_class(element, "target")
        expected = ClassFactory.create(
            tag=Tag.ELEMENT,
            qname="root",
            namespace="",
            location="",
            module=None,
            ns_map={},
            attrs=[
                AttrFactory.native(
                    DataType.ANY_SIMPLE_TYPE,
                    tag=Tag.ELEMENT,
                    name="a",
                    namespace="",
                    index=0,
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=sys.maxsize,
                        path=[("s", 1, 1, sys.maxsize)],
                    ),
                ),
                AttrFactory.native(
                    DataType.ANY_SIMPLE_TYPE,
                    tag=Tag.ELEMENT,
                    name="b",
                    namespace="",
                    index=1,
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=sys.maxsize,
                        path=[("s", 1, 1, sys.maxsize)],
                    ),
                ),
                AttrFactory.native(
                    DataType.ANY_SIMPLE_TYPE,
                    tag=Tag.ELEMENT,
                    name="c",
                    namespace="",
                    index=2,
                    restrictions=Restrictions(min_occurs=1, max_occurs=1),
                ),
                AttrFactory.native(
                    DataType.ANY_SIMPLE_TYPE,
                    tag=Tag.ELEMENT,
                    name="d",
                    namespace="",
                    index=3,
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=sys.maxsize,
                        path=[("s", 2, 1, sys.maxsize)],
                    ),
                ),
                AttrFactory.native(
                    DataType.ANY_SIMPLE_TYPE,
                    tag=Tag.ELEMENT,
                    name="e",
                    namespace="",
                    index=4,
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=sys.maxsize,
                        path=[("s", 2, 1, sys.maxsize)],
                    ),
                ),
            ],
        )
        self.assertEqual(expected, actual)

    def test_build_class_mixed_content(self):
        element = AnyElement(
            qname="{xsdata}root",
            children=[
                AnyElement(qname="{xsdata}child", text="primitive"),
                AnyElement(qname="something", text="foo", tail="bar"),
            ],
        )

        actual = ElementMapper.build_class(element, None)
        expected = ClassFactory.create(
            tag=Tag.ELEMENT,
            qname="{xsdata}root",
            namespace="xsdata",
            location="",
            module=None,
            mixed=True,
            ns_map={},
            attrs=[
                AttrFactory.native(
                    DataType.STRING,
                    name="child",
                    namespace="xsdata",
                    index=0,
                    restrictions=Restrictions(min_occurs=0, max_occurs=1),
                ),
                AttrFactory.native(
                    DataType.STRING,
                    namespace="",
                    name="something",
                    index=1,
                    restrictions=Restrictions(min_occurs=0, max_occurs=1),
                ),
            ],
        )
        self.assertEqual(expected, actual)

        element = AnyElement(
            qname="{xsdata}root",
            text="foo",
            children=[
                AnyElement(qname="{xsdata}child", text="primitive"),
            ],
        )
        actual = ElementMapper.build_class(element, None)
        self.assertTrue(actual.mixed)

    def test_build_class_nillable(self):
        element = AnyElement(qname="{xsdata}root", attributes={QNames.XSI_NIL: "1"})
        target = ElementMapper.build_class(element, None)
        self.assertTrue(target.nillable)

        element.attributes[QNames.XSI_NIL] = " true "
        target = ElementMapper.build_class(element, None)
        self.assertTrue(target.nillable)

    def test_build_class_ignore_invalid(self):
        element = AnyElement(
            qname="{xsdata}root",
            children=[
                AnyElement(text="primitive"),
                "",
            ],
        )
        actual = ElementMapper.build_class(element, None)
        self.assertEqual(0, len(actual.attrs))

    def test_build_attribute_type(self):
        actual = ElementMapper.build_attribute_type(QNames.XSI_TYPE, "")
        self.assertEqual(str(DataType.QNAME), actual.qname)
        self.assertTrue(actual.native)

        actual = ElementMapper.build_attribute_type("name", "foo")
        self.assertEqual(str(DataType.STRING), actual.qname)
        self.assertTrue(actual.native)

        actual = ElementMapper.build_attribute_type("name", "")
        self.assertEqual(str(DataType.ANY_SIMPLE_TYPE), actual.qname)
        self.assertTrue(actual.native)

        actual = ElementMapper.build_attribute_type("name", None)
        self.assertEqual(str(DataType.ANY_SIMPLE_TYPE), actual.qname)
        self.assertTrue(actual.native)

        actual = ElementMapper.build_attribute_type("name", 1)
        self.assertEqual(str(DataType.SHORT), actual.qname)
        self.assertTrue(actual.native)

        actual = ElementMapper.build_attribute_type("name", "1.9")
        self.assertEqual(str(DataType.FLOAT), actual.qname)
        self.assertTrue(actual.native)

    def test_add_attribute(self):
        target = ClassFactory.elements(2)
        attr = target.attrs[0].clone()
        attr.index += 1

        ElementMapper.add_attribute(target, attr)

        self.assertEqual(2, len(target.attrs))
        self.assertEqual(sys.maxsize, target.attrs[0].restrictions.max_occurs)
        self.assertEqual(1, len(target.attrs[0].types))

        attr = target.attrs[1].clone()
        ElementMapper.add_attribute(target, attr)

        attr = AttrFactory.create()
        ElementMapper.add_attribute(target, attr)
        self.assertEqual(3, len(target.attrs))

    def test_select_namespace(self):
        self.assertEqual("a", ElementMapper.select_namespace("a", "a", Tag.ELEMENT))
        self.assertEqual("b", ElementMapper.select_namespace("b", "a", Tag.ELEMENT))
        self.assertEqual("", ElementMapper.select_namespace(None, "a", Tag.ELEMENT))

        self.assertEqual("a", ElementMapper.select_namespace("a", "a", Tag.ATTRIBUTE))
        self.assertEqual("b", ElementMapper.select_namespace("b", "a", Tag.ATTRIBUTE))
        self.assertIsNone(ElementMapper.select_namespace(None, "a", Tag.ATTRIBUTE))

    def test_sequential_groups(self):
        a = AnyElement(qname="a")
        b = AnyElement(qname="b")
        c = AnyElement(qname="c")
        d = AnyElement(qname="d")
        e = AnyElement(qname="e")

        p = AnyElement(children=[a, b, c, d])
        actual = ElementMapper.sequential_groups(p)
        self.assertEqual([], actual)

        p = AnyElement(children=[a, b, a])
        actual = ElementMapper.sequential_groups(p)
        self.assertEqual([[0, 1, 2]], actual)

        p = AnyElement(children=[a, b, a, c])
        actual = ElementMapper.sequential_groups(p)
        self.assertEqual([[0, 1, 2]], actual)

        p = AnyElement(children=[a, b, a, c, d, e, d])
        actual = ElementMapper.sequential_groups(p)
        self.assertEqual([[0, 1, 2], [4, 5, 6]], actual)
