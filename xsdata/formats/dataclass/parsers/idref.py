from __future__ import annotations

from typing import Any

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.nodes.idref import _IdRefPlaceholder


def _get_key(obj: Any) -> str | None:
    """Walk the MRO to find and build the composite key string for *obj*.

    Returns ``None`` when no ``Meta.key`` is defined in the class hierarchy,
    when the key list is empty, or when any key attribute is absent from *obj*.
    Multiple key fields are joined with ``_``.
    """
    for cls in obj.__class__.__mro__:
        cls_meta = cls.__dict__.get("Meta")
        if cls_meta is not None and hasattr(cls_meta, "key"):
            key_fields: list[str] = list(cls_meta.key)
            if not key_fields:
                break
            _MISSING = object()
            parts = [getattr(obj, k, _MISSING) for k in key_fields]
            if any(v is _MISSING for v in parts):
                # Key field(s) not present on this object — not keyed
                return None
            return "_".join(str(v) for v in parts)
    return None


def resolve_idrefs(root: Any, context: XmlContext) -> None:
    """Replace all ``_IdRefPlaceholder`` instances in *root* after parsing.

    The parser stores a :class:`~xsdata.formats.dataclass.parsers.nodes.idref._IdRefPlaceholder`
    whenever it encounters a field with ``idref=True``.  An IDREF may appear in
    the XML *before* the object it refers to, so a two-pass algorithm is used:

    **Pass 1 – collect** — DFS-walk the object tree, skipping IDREF fields
    (which only hold placeholders at this point), and register every object
    that has a non-empty ``Meta.key`` in a ``{key_string: object}`` registry.

    **Pass 2 – replace** — second DFS-walk that substitutes every
    ``_IdRefPlaceholder`` found in IDREF fields with the real object looked up
    from the registry.

    Args:
        root: The fully-parsed top-level object.
        context: The ``XmlContext`` used during parsing (supplies metadata).
    """
    if not context.class_type.is_model(root):
        return

    registry: dict[str, Any] = {}

    # ------------------------------------------------------------------ #
    # Pass 1 – build {key → object} registry                              #
    # ------------------------------------------------------------------ #
    def collect(obj: Any) -> None:
        if not context.class_type.is_model(obj):
            return
        key = _get_key(obj)
        if key:
            registry[key] = obj
        meta = context.build(obj.__class__)
        for var in meta.get_element_vars():
            if var.is_idref:
                # IDREF fields only hold placeholders at this stage — skip
                continue
            value = getattr(obj, var.name, None)
            if value is None:
                continue
            if isinstance(value, list):
                for item in value:
                    collect(item)
            else:
                collect(value)

    collect(root)

    # ------------------------------------------------------------------ #
    # Pass 2 – replace placeholders with real objects                     #
    # ------------------------------------------------------------------ #
    def replace(obj: Any) -> None:
        if not context.class_type.is_model(obj):
            return
        meta = context.build(obj.__class__)
        for var in meta.get_element_vars():
            value = getattr(obj, var.name, None)
            if value is None:
                continue
            if var.is_idref:
                # Resolve placeholders in this IDREF field
                if isinstance(value, list):
                    setattr(
                        obj,
                        var.name,
                        [
                            registry.get(item.key, item)
                            if isinstance(item, _IdRefPlaceholder)
                            else item
                            for item in value
                        ],
                    )
                elif isinstance(value, _IdRefPlaceholder):
                    setattr(obj, var.name, registry.get(value.key, value))
            else:
                # Recurse into non-IDREF child fields
                if isinstance(value, list):
                    for item in value:
                        replace(item)
                else:
                    replace(value)

    replace(root)
