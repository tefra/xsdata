from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar
from unittest import TestCase

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.parsers.nodes.idref import (
    IdRefNode,
    _IdRefPlaceholder,
    get_obj_key,
)
from xsdata.utils.testing import XmlVarFactory

# ---------------------------------------------------------------------------
# Minimal dataclass fixtures
# ---------------------------------------------------------------------------


@dataclass
class _WithKey:
    """Object whose Meta defines a composite key."""

    class Meta:
        key: ClassVar[list[str]] = ["name", "code"]

    name: str = ""
    code: str = ""


@dataclass
class _WithEmptyKey:
    """Object whose Meta.key is explicitly empty — should return None."""

    class Meta:
        key: ClassVar[list[str]] = []

    name: str = ""


@dataclass
class _WithKeyMissingAttr:
    """Meta.key references a field that doesn't exist on the object."""

    class Meta:
        key: ClassVar[list[str]] = ["nonexistent_field"]

    name: str = ""


@dataclass
class _WithoutMeta:
    """No Meta class at all — get_obj_key should return None."""

    name: str = ""


# ---------------------------------------------------------------------------
# get_obj_key tests
# ---------------------------------------------------------------------------


class GetObjKeyTests(TestCase):
    def test_returns_composite_key(self) -> None:
        obj = _WithKey(name="albert", code="fictional")
        self.assertEqual("albert_fictional", get_obj_key(obj))

    def test_empty_key_list_returns_none(self) -> None:
        """Meta.key = [] → break from loop, returns None (covers line 24)."""
        obj = _WithEmptyKey(name="albert")
        self.assertIsNone(get_obj_key(obj))

    def test_missing_attribute_returns_none(self) -> None:
        """Key field absent on object → returns None (covers line 27)."""
        obj = _WithKeyMissingAttr(name="albert")
        self.assertIsNone(get_obj_key(obj))

    def test_no_meta_returns_none(self) -> None:
        """No Meta class at all → returns None from the final return."""
        obj = _WithoutMeta(name="albert")
        self.assertIsNone(get_obj_key(obj))

    def test_key_inherited_via_mro(self) -> None:
        """Key defined on a parent class is found by MRO walk."""

        @dataclass
        class Child(_WithKey):
            extra: str = ""

        obj = Child(name="peter", code="test", extra="x")
        self.assertEqual("peter_test", get_obj_key(obj))


# ---------------------------------------------------------------------------
# _IdRefPlaceholder tests
# ---------------------------------------------------------------------------


class IdRefPlaceholderTests(TestCase):
    def test_stores_key(self) -> None:
        ph = _IdRefPlaceholder("albert_fictional")
        self.assertEqual("albert_fictional", ph.key)

    def test_repr(self) -> None:
        """__repr__ returns a useful string (covers line 45)."""
        ph = _IdRefPlaceholder("albert_fictional")
        self.assertEqual("_IdRefPlaceholder('albert_fictional')", repr(ph))


# ---------------------------------------------------------------------------
# IdRefNode tests
# ---------------------------------------------------------------------------


class IdRefNodeTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.context = XmlContext()
        self.var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            name="ref",
            idref=True,
        )
        self.node = IdRefNode(var=self.var, context=self.context)

    def test_bind_backward_ref_returns_real_object(self) -> None:
        """Key already present in registry → real object emitted immediately."""
        obj = _WithKey(name="albert", code="fictional")
        self.context.idref_registry["albert_fictional"] = obj

        objects: list = []
        result = self.node.bind(self.var.qname, "albert_fictional", None, objects)

        self.assertTrue(result)
        self.assertEqual(1, len(objects))
        self.assertIs(obj, objects[0][1])

    def test_bind_forward_ref_emits_placeholder(self) -> None:
        """Key not in registry → placeholder emitted (forward reference)."""
        objects: list = []
        result = self.node.bind(self.var.qname, "albert_fictional", None, objects)

        self.assertTrue(result)
        self.assertEqual(1, len(objects))
        placeholder = objects[0][1]
        self.assertIsInstance(placeholder, _IdRefPlaceholder)
        self.assertEqual("albert_fictional", placeholder.key)

    def test_bind_empty_text_uses_empty_string_key(self) -> None:
        """text=None is normalised to '' as the lookup key."""
        objects: list = []
        result = self.node.bind(self.var.qname, None, None, objects)

        self.assertTrue(result)
        placeholder = objects[0][1]
        self.assertIsInstance(placeholder, _IdRefPlaceholder)
        self.assertEqual("", placeholder.key)

    def test_child_raises_xml_context_error(self) -> None:
        """IDREF nodes must not have children (covers line 86)."""
        with self.assertRaises(XmlContextError):
            self.node.child("anything", {}, {}, 0)
