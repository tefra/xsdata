from __future__ import annotations

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.mixins import XmlNode


class _IdRefPlaceholder:
    """Placeholder for an unresolved IDREF during parsing.

    Attributes:
        key: The raw key string from the element text (e.g. ``"albert"``).
    """

    __slots__ = ("key",)

    def __init__(self, key: str) -> None:
        self.key = key

    def __repr__(self) -> str:
        return f"_IdRefPlaceholder({self.key!r})"


class IdRefNode(XmlNode):
    """XmlNode for element fields that carry ``idref=True`` metadata.

    Reads element text as a key string and emits an ``_IdRefPlaceholder``
    into the objects list.  Resolved by ``resolve_idrefs`` after parsing.

    Args:
        var: The xml var whose ``is_idref`` flag is ``True``.
    """

    __slots__ = ("var",)

    def __init__(self, var: XmlVar) -> None:
        self.var = var

    def bind(
        self,
        qname: str,
        text: str | None,
        tail: str | None,
        objects: list,
    ) -> bool:
        """Emit a placeholder for the key text and return True."""
        objects.append((qname, _IdRefPlaceholder(text or "")))
        return True

    def child(self, qname: str, attrs: dict, ns_map: dict, position: int) -> XmlNode:
        """Raise an error — IDREF elements must not have child elements."""
        raise XmlContextError("IdRef node doesn't support child nodes!")

