from __future__ import annotations

from typing import Any

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.mixins import XmlNode


def get_obj_key(obj: Any) -> str | None:
    """Walk the MRO to build a composite key string for *obj*.

    Returns ``None`` when no ``Meta.key`` is defined, the list is empty,
    or any named attribute is absent from the object.  Multiple key fields
    are joined with ``_``.
    """
    _MISSING = object()
    for cls in obj.__class__.__mro__:
        cls_meta = cls.__dict__.get("Meta")
        if cls_meta is not None and hasattr(cls_meta, "key"):
            key_fields: list[str] = list(cls_meta.key)
            if not key_fields:
                break
            parts = [getattr(obj, k, _MISSING) for k in key_fields]
            if any(v is _MISSING for v in parts):
                return None
            return "_".join(str(v) for v in parts)
    return None


class _IdRefPlaceholder:
    """Placeholder for an unresolved forward IDREF during parsing.

    Attributes:
        key: The raw key string from the element text (e.g. ``"albert_fictional"``).
    """

    __slots__ = ("key",)

    def __init__(self, key: str) -> None:
        self.key = key

    def __repr__(self) -> str:
        return f"_IdRefPlaceholder({self.key!r})"


class IdRefNode(XmlNode):
    """XmlNode for element fields that carry ``idref=True`` metadata.

    If the referenced object is already in the context's IDREF registry the
    real object is emitted immediately (backward reference, zero overhead).
    Otherwise a :class:`_IdRefPlaceholder` is emitted and resolved by
    :meth:`~xsdata.formats.dataclass.parsers.nodes.element.ElementNode.bind`
    as soon as the target object is created (forward reference).

    Args:
        var: The xml var whose ``is_idref`` flag is ``True``.
        context: The shared xml context that holds the per-parse registry.
    """

    __slots__ = ("context", "var")

    def __init__(self, var: XmlVar, context: XmlContext) -> None:
        self.var = var
        self.context = context

    def bind(
        self,
        qname: str,
        text: str | None,
        tail: str | None,
        objects: list,
    ) -> bool:
        """Emit the real object or a placeholder, depending on registry state."""
        key = text or ""
        resolved = self.context.idref_registry.get(key)
        if resolved is not None:
            objects.append((qname, resolved))
        else:
            objects.append((qname, _IdRefPlaceholder(key)))
        return True

    def child(self, qname: str, attrs: dict, ns_map: dict, position: int) -> XmlNode:
        """Raise an error — IDREF elements must not have child elements."""
        raise XmlContextError("IdRef node doesn't support child nodes!")
