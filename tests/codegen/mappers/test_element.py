import sys
from typing import Generator
from unittest import mock

from xsdata.codegen.mappers.element import ElementMapper
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.enums import DataType
from xsdata.models.enums import QNames
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class ElementMapperTests(FactoryTestCase):
    @mock.patch.object(ElementMapper, "flatten")
    @mock.patch.object(ElementMapper, "build_class")
    def test_map(self, mock_build_class, mock_flatten):
        element = AnyElement(qname="{xsdata}root")
        root_class = ClassFactory.create()
        flat_classes = ClassFactory.list(5)
        iter_flat_classes = iter(flat_classes)

        mock_build_class.return_value = root_class
        mock_flatten.return_value = iter_flat_classes

        actual = ElementMapper.map(element)

        self.assertEqual(flat_classes, actual)
        mock_build_class.assert_called_once_with(element, "xsdata")
        mock_flatten.assert_called_once_with(root_class, "root")

    def test_flatten(self):
        target = ClassFactory.create(
            qname="{xsdata}root", attrs=AttrFactory.list(3), inner=ClassFactory.list(2)
        )

        for attr in target.attrs:
            attr.types.extend([x.clone() for x in attr.types])
            for tp in attr.types:
                tp.forward = True

        result = ElementMapper.flatten(target, "xsdata")
        actual = list(result)

        self.assertIsInstance(result, Generator)
        self.assertEqual(3, len(actual))

        for obj in actual:
            self.assertEqual("xsdata", obj.module)

        for attr in target.attrs:
            self.assertEqual(1, len(attr.types))
            self.assertFalse(attr.types[0].forward)

    @mock.patch.object(ElementMapper, "merge_attributes")
    def test_reduce(self, mock_merge_attributes):
        first = ClassFactory.elements(2)
        second = first.clone()
        second.attrs.append(AttrFactory.create())
        third = second.clone()
        third.attrs.append(AttrFactory.create())
        fourth = ClassFactory.create()

        actual = ElementMapper.reduce([first, second, third, fourth])

        self.assertEqual([third, fourth], list(actual))
        mock_merge_attributes.assert_has_calls(
            [
                mock.call(third, first),
                mock.call(third, second),
            ]
        )

    def test_build_class_simple_type(self):
        element = AnyElement(
            qname="{xsdata}root",
            attributes={"{foo}bar": "1", "{bar}foo": "2.0"},
            text="true",
        )

        actual = ElementMapper.build_class(element, "target")
        expected = ClassFactory.create(
            tag=Tag.ELEMENT,
            qname="{target}root",
            namespace="xsdata",
            module="",
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
            qname="{target}root",
            namespace="xsdata",
            module="",
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
            qname="root",
            namespace="xsdata",
            module="",
            mixed=True,
            ns_map={},
            attrs=[
                AttrFactory.native(
                    DataType.STRING, name="child", namespace="xsdata", index=0
                ),
                AttrFactory.native(DataType.STRING, name="something", index=1),
            ],
        )
        self.assertEqual(expected, actual)

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

        class A:
            pass

        actual = ElementMapper.build_attribute_type("name", A())
        self.assertEqual(str(DataType.ANY_SIMPLE_TYPE), actual.qname)
        self.assertTrue(actual.native)

    def test_add_attribute(self):
        target = ClassFactory.elements(2)
        attr = target.attrs[0].clone()
        attr.index += 1

        ElementMapper.add_attribute(target, attr)

        self.assertEqual(2, len(target.attrs))
        self.assertEqual(sys.maxsize, target.attrs[0].restrictions.max_occurs)
        self.assertEqual(2, len(target.attrs[0].types))
        self.assertFalse(target.attrs[0].restrictions.sequential)

        attr = target.attrs[1].clone()
        attr.restrictions.sequential = True
        ElementMapper.add_attribute(target, attr)
        self.assertTrue(target.attrs[1].restrictions.sequential)

        attr = AttrFactory.create()
        ElementMapper.add_attribute(target, attr)
        self.assertEqual(3, len(target.attrs))

    def test_merge_attributes(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(name="a", index=10),
                AttrFactory.element(name="b", index=1),
                AttrFactory.element(name="c", index=2),
                AttrFactory.attribute(name="id", index=0),
            ]
        )

        source = target.clone()

        target.attrs[0].restrictions.min_occurs = 2
        target.attrs[0].restrictions.max_occurs = 3

        source.attrs[1].restrictions.min_occurs = 3
        source.attrs[1].restrictions.max_occurs = 4
        source.attrs[3].restrictions.min_occurs = 3
        source.attrs[3].restrictions.max_occurs = 4
        source.attrs.append(AttrFactory.enumeration(name="d", index=4))

        ElementMapper.merge_attributes(target, source)

        names = ["id", "b", "c", "d", "a"]
        min_occurs = [0, 0, 0, None, 0]
        max_occurs = [4, 4, 1, None, 3]

        self.assertEqual(names, [x.name for x in target.attrs])
        self.assertEqual(min_occurs, [x.restrictions.min_occurs for x in target.attrs])
        self.assertEqual(max_occurs, [x.restrictions.max_occurs for x in target.attrs])

    def test_select_namespace(self):
        self.assertEqual("a", ElementMapper.select_namespace("a", "a", Tag.ELEMENT))
        self.assertEqual("b", ElementMapper.select_namespace("b", "a", Tag.ELEMENT))
        self.assertEqual("", ElementMapper.select_namespace(None, "a", Tag.ELEMENT))

        self.assertEqual("a", ElementMapper.select_namespace("a", "a", Tag.ATTRIBUTE))
        self.assertEqual("b", ElementMapper.select_namespace("b", "a", Tag.ATTRIBUTE))
        self.assertIsNone(ElementMapper.select_namespace(None, "a", Tag.ATTRIBUTE))

    def test_sequential_names(self):
        a = AnyElement(qname="a")
        b = AnyElement(qname="b")

        actual = ElementMapper.sequential_names([a, b])
        self.assertEqual(0, len(actual))

        actual = ElementMapper.sequential_names([a, b, a])
        self.assertEqual({"a", "b"}, actual)

        c = AnyElement(qname="c")
        actual = ElementMapper.sequential_names([a, b, a, c])
        self.assertEqual({"a", "b"}, actual)

        d = AnyElement(qname="d")
        e = AnyElement(qname="e")

        actual = ElementMapper.sequential_names([a, b, a, c, d, e, d])
        self.assertEqual({"a", "b", "d", "e"}, actual)
