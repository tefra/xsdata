import sys
from unittest import mock

from xsdata.codegen.mappers import DictMapper
from xsdata.codegen.models import Restrictions
from xsdata.codegen.utils import ClassUtils
from xsdata.models.enums import DataType, Tag
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    FactoryTestCase,
)


class DictMapperTests(FactoryTestCase):
    @mock.patch.object(ClassUtils, "flatten")
    @mock.patch.object(DictMapper, "build_class")
    def test_map(self, mock_build_class, mock_flatten) -> None:
        data = {"value": 1}
        root_class = ClassFactory.create()
        flat_classes = ClassFactory.list(5)
        iter_flat_classes = iter(flat_classes)

        mock_build_class.return_value = root_class
        mock_flatten.return_value = iter_flat_classes

        actual = DictMapper.map(data, "root", "tests")

        self.assertEqual(flat_classes, actual)
        mock_build_class.assert_called_once_with(data, "root")
        mock_flatten.assert_called_once_with(root_class, "tests/root")

    def test_build_class(self) -> None:
        data = {"a": 1, "b": True}
        actual = DictMapper.build_class(data, "root")
        expected = ClassFactory.create(
            tag=Tag.ELEMENT,
            qname="root",
            location="",
            module=None,
            ns_map={},
            attrs=[
                AttrFactory.native(
                    DataType.SHORT,
                    tag=Tag.ELEMENT,
                    name="a",
                    index=0,
                ),
                AttrFactory.native(
                    DataType.BOOLEAN,
                    tag=Tag.ELEMENT,
                    name="b",
                    index=1,
                ),
            ],
        )
        self.assertEqual(expected, actual)

    def test_build_class_attribute_from_list(self) -> None:
        target = ClassFactory.create()
        data = [1, True, 1.1]

        DictMapper.build_class_attribute(target, "a", data)

        expected = AttrFactory.create(
            name="a",
            tag=Tag.ELEMENT,
            types=[
                AttrTypeFactory.native(DataType.SHORT, tag=Tag.ELEMENT),
                AttrTypeFactory.native(DataType.BOOLEAN, tag=Tag.ELEMENT),
                AttrTypeFactory.native(DataType.FLOAT, tag=Tag.ELEMENT),
            ],
        )
        restrictions = Restrictions(min_occurs=1, max_occurs=sys.maxsize)
        self.assertEqual(expected, target.attrs[0])
        self.assertEqual(restrictions, target.attrs[0].restrictions)

    def test_build_class_attribute_from_empty_list(self) -> None:
        target = ClassFactory.create()
        data = []

        DictMapper.build_class_attribute(target, "a", data)

        expected = AttrFactory.create(
            name="a",
            tag=Tag.ELEMENT,
            types=[
                AttrTypeFactory.native(DataType.ANY_SIMPLE_TYPE, tag=Tag.ELEMENT),
            ],
        )
        restrictions = Restrictions(min_occurs=0, max_occurs=sys.maxsize)
        self.assertEqual(expected, target.attrs[0])
        self.assertEqual(restrictions, target.attrs[0].restrictions)

    def test_build_class_attribute_from_dict(self) -> None:
        target = ClassFactory.create()
        data = {"sub1": 1, "sub2": "value", "sub3": None}
        DictMapper.build_class_attribute(target, "a", data)

        expected = AttrFactory.create(
            name="a",
            tag=Tag.ELEMENT,
            types=[AttrTypeFactory.create(qname="a", forward=True)],
        )

        expected_inner = ClassFactory.create(
            qname="a",
            tag=Tag.ELEMENT,
            location="",
            module=None,
            ns_map={},
            attrs=[
                AttrFactory.native(DataType.SHORT, name="sub1"),
                AttrFactory.native(DataType.STRING, name="sub2"),
                AttrFactory.native(DataType.STRING, name="sub3"),
            ],
        )

        self.assertEqual(expected, target.attrs[0])
        self.assertEqual(expected_inner, target.inner[0])
        self.assertEqual(1, len(target.inner))

        self.assertFalse(target.inner[0].attrs[0].restrictions.is_optional)
        self.assertFalse(target.inner[0].attrs[1].restrictions.is_optional)
        self.assertTrue(target.inner[0].attrs[2].restrictions.is_optional)
