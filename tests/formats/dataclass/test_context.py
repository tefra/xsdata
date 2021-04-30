from dataclasses import fields
from dataclasses import make_dataclass
from dataclasses import replace
from unittest import mock
from unittest import TestCase

from tests.fixtures.books import BookForm
from tests.fixtures.books import BooksForm
from tests.fixtures.defxmlschema.chapter13 import ItemsType
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.models.enums import DataType


class XmlContextTests(TestCase):
    def setUp(self):
        self.ctx = XmlContext()
        super().setUp()

    @mock.patch.object(XmlContext, "find_subclass")
    @mock.patch.object(XmlContext, "build")
    def test_fetch(self, mock_build, mock_find_subclass):
        meta = XmlMeta(
            clazz=ItemsType,
            qname="ItemsType",
            source_qname="ItemsType",
            nillable=False,
        )
        mock_build.return_value = meta
        actual = self.ctx.fetch(ItemsType, "foo")
        self.assertEqual(meta, actual)
        self.assertEqual(0, mock_find_subclass.call_count)
        mock_build.assert_called_once_with(ItemsType, "foo")

    @mock.patch.object(XmlContext, "find_subclass")
    @mock.patch.object(XmlContext, "build")
    def test_fetch_with_xsi_type_and_subclass_not_found(
        self, mock_build, mock_find_subclass
    ):
        meta = XmlMeta(
            clazz=ItemsType,
            qname="ItemsType",
            source_qname="ItemsType",
            nillable=False,
        )

        mock_build.return_value = meta
        mock_find_subclass.return_value = None
        actual = self.ctx.fetch(ItemsType, xsi_type="foo")
        self.assertEqual(meta, actual)
        mock_find_subclass.assert_called_once_with(ItemsType, "foo")

    @mock.patch.object(XmlContext, "find_subclass")
    @mock.patch.object(XmlContext, "build")
    def test_fetch_with_xsi_type_and_subclass_found(
        self, mock_build, mock_find_subclass
    ):
        meta = XmlMeta(
            clazz=ItemsType,
            qname="ItemsType",
            source_qname="ItemsType",
            nillable=False,
        )
        xsi_meta = replace(meta, qname="XsiType")

        mock_build.side_effect = [meta, xsi_meta]
        mock_find_subclass.return_value = xsi_meta
        actual = self.ctx.fetch(ItemsType, xsi_type="foo")
        self.assertEqual(xsi_meta, actual)
        mock_find_subclass.assert_called_once_with(ItemsType, "foo")

    def test_find(self):
        self.assertIsNone(self.ctx.find_type(str(DataType.FLOAT)))
        self.assertEqual(BookForm, self.ctx.find_type("{urn:books}BookForm"))

        self.ctx.xsi_cache["{urn:books}BookForm"].append(BooksForm)
        self.assertEqual(BooksForm, self.ctx.find_type("{urn:books}BookForm"))

    def test_find_type_by_fields(self):
        field_names = {f.name for f in fields(BookForm)}
        self.assertEqual(BookForm, self.ctx.find_type_by_fields(field_names))

        field_names.pop()  # Test matching less fields
        self.assertEqual(BookForm, self.ctx.find_type_by_fields(field_names))

        field_names.update({"please", "dont", "exist"})  # Test matching with more
        self.assertIsNone(self.ctx.find_type_by_fields(field_names))

    def test_find_subclass(self):
        a = make_dataclass("A", fields=[])
        b = make_dataclass("B", fields=[], bases=(a,))
        c = make_dataclass("C", fields=[], bases=(a,))
        other = make_dataclass("Other", fields=[])

        self.assertEqual(b, self.ctx.find_subclass(a, "B"))
        self.assertEqual(b, self.ctx.find_subclass(c, "B"))
        self.assertEqual(a, self.ctx.find_subclass(b, "A"))
        self.assertEqual(a, self.ctx.find_subclass(c, "A"))
        self.assertIsNone(self.ctx.find_subclass(c, "Unknown"))
        self.assertIsNone(self.ctx.find_subclass(c, "Other"))

    def test_is_derived(self):
        a = make_dataclass("A", fields=[])
        b = make_dataclass("B", fields=[], bases=(a,))
        c = make_dataclass("C", fields=[], bases=(a,))
        d = make_dataclass("D", fields=[])

        self.assertTrue(self.ctx.is_derived(c(), b))
        self.assertTrue(self.ctx.is_derived(b(), c))
        self.assertTrue(self.ctx.is_derived(a(), b))
        self.assertTrue(self.ctx.is_derived(a(), c))
        self.assertTrue(self.ctx.is_derived(a(), a))
        self.assertFalse(self.ctx.is_derived(a(), d))
        self.assertFalse(self.ctx.is_derived(None, d))
