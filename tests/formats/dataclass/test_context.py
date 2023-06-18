import copy
from dataclasses import make_dataclass
from pathlib import Path
from unittest import mock

from tests.fixtures.artists import Artist
from tests.fixtures.artists import BeginArea
from tests.fixtures.books import BookForm
from tests.fixtures.books import BooksForm
from tests.fixtures.models import BaseType
from tests.fixtures.models import ChoiceType
from tests.fixtures.models import UnionType
from xsdata.formats.dataclass.context import XmlContext
from xsdata.models.enums import DataType
from xsdata.utils.testing import FactoryTestCase
from xsdata.utils.testing import XmlMetaFactory


class XmlContextTests(FactoryTestCase):
    def setUp(self):
        self.ctx = XmlContext()
        self.ctx.reset()
        super().setUp()

    @mock.patch.object(XmlContext, "find_subclass")
    @mock.patch.object(XmlContext, "build")
    def test_fetch(self, mock_build, mock_find_subclass):
        meta = XmlMetaFactory.create(clazz=Artist, qname="Artist")
        mock_build.return_value = meta
        actual = self.ctx.fetch(Artist, "foo")
        self.assertEqual(meta, actual)
        self.assertEqual(0, mock_find_subclass.call_count)
        mock_build.assert_called_once_with(Artist, "foo")

    @mock.patch.object(XmlContext, "find_subclass")
    @mock.patch.object(XmlContext, "build")
    def test_fetch_with_xsi_type_and_subclass_not_found(
        self, mock_build, mock_find_subclass
    ):
        meta = XmlMetaFactory.create(
            clazz=Artist,
            qname="Artist",
            target_qname="Artist",
            nillable=False,
        )

        mock_build.return_value = meta
        mock_find_subclass.return_value = None
        actual = self.ctx.fetch(Artist, xsi_type="foo")
        self.assertEqual(meta, actual)
        mock_find_subclass.assert_called_once_with(Artist, "foo")

    @mock.patch.object(XmlContext, "find_subclass")
    @mock.patch.object(XmlContext, "build")
    def test_fetch_with_xsi_type_and_subclass_found(
        self, mock_build, mock_find_subclass
    ):
        meta = XmlMetaFactory.create(clazz=Artist)
        xsi_meta = copy.deepcopy(meta)
        xsi_meta.qname = "XsiType"

        mock_build.side_effect = [meta, xsi_meta]
        mock_find_subclass.return_value = xsi_meta
        actual = self.ctx.fetch(Artist, xsi_type="foo")
        self.assertEqual(xsi_meta, actual)
        mock_find_subclass.assert_called_once_with(Artist, "foo")

    def test_find(self):
        self.assertIsNone(self.ctx.find_type(str(DataType.FLOAT)))
        self.assertEqual(BookForm, self.ctx.find_type("{urn:books}BookForm"))

        self.ctx.xsi_cache["{urn:books}BookForm"].append(BooksForm)
        self.assertEqual(BooksForm, self.ctx.find_type("{urn:books}BookForm"))

    def test_find_type_by_fields(self):
        field_names = {"id", "name", "sort-name"}
        self.assertEqual(BeginArea, self.ctx.find_type_by_fields(field_names))

        field_names.update({"please", "dont", "exist"})  # Test matching with more
        self.assertIsNone(self.ctx.find_type_by_fields(field_names))

    def test_local_names_match_remove_clazz_from_cache_on_error(self):
        undefined = make_dataclass("UndefinedType", [("content", "Literal['yes']")])
        unsupported = make_dataclass("UndefinedType", [("content", Path)])
        uncached = make_dataclass("Uncached", [("content", Path)])

        builder = self.ctx.get_builder()
        for clazz in (undefined, unsupported):
            meta = builder.build_class_meta(clazz)
            self.ctx.xsi_cache[meta.target_qname].append(clazz)

        self.assertFalse(self.ctx.local_names_match({"content"}, undefined))
        self.assertFalse(self.ctx.local_names_match({"content"}, unsupported))
        self.assertFalse(self.ctx.local_names_match({"content"}, uncached))

        total = [x for types in self.ctx.cache.values() for x in types]
        self.assertEqual(0, len(total))

    def test_find_subclass(self):
        a = make_dataclass("A", fields=[])
        b = make_dataclass("B", fields=[], bases=(a,))
        c = make_dataclass("C", fields=[], bases=(a,))
        other = make_dataclass("Other", fields=[])  # Included in the locals

        self.assertEqual(b, self.ctx.find_subclass(a, "B"))
        self.assertEqual(b, self.ctx.find_subclass(c, "B"))
        self.assertIsNone(self.ctx.find_subclass(b, "A"))
        self.assertIsNone(self.ctx.find_subclass(c, "A"))
        self.assertIsNone(self.ctx.find_subclass(c, "Unknown"))
        self.assertIsNone(self.ctx.find_subclass(c, "Other"))

    def is_binding_model(self):
        self.assertTrue(self.ctx.is_binding_model(ChoiceType))

        self.ctx.models_package = "xsdata.models"
        self.assertFalse(self.ctx.is_binding_model(ChoiceType))

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

    def test_build_recursive(self):
        self.ctx.build_recursive(ChoiceType)
        self.assertEqual(6, len(self.ctx.cache))

        self.ctx.build_recursive(BaseType)
        self.assertEqual(8, len(self.ctx.cache))

        self.ctx.build_recursive(UnionType)
        self.assertEqual(8, len(self.ctx.cache))
