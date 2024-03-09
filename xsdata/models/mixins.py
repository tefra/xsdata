from dataclasses import dataclass, field, fields
from typing import Any, Callable, Dict, Iterator, List, Optional

from xsdata.codegen.exceptions import CodegenError
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.models.enums import DataType, FormType, Namespace, NamespaceType
from xsdata.utils import text
from xsdata.utils.constants import return_true


@dataclass
class ElementBase:
    """Base xsd schema model representation.

    Attributes:
        index: The element position in the schema
        ns_map: The element namespace prefix-URI map
    """

    index: int = field(
        default_factory=int,
        init=False,
        metadata={"type": "Ignore"},
    )
    ns_map: Dict[str, str] = field(
        default_factory=dict,
        init=False,
        metadata={"type": "Ignore"},
    )

    @property
    def class_name(self) -> str:
        """Return the schema element class name."""
        return self.__class__.__name__

    @property
    def default_type(self) -> str:
        """The element's inferred default type qname."""
        return DataType.STRING.prefixed(self.xs_prefix)

    @property
    def default_value(self) -> Any:
        """Return the default or the fixed attribute value."""
        default = getattr(self, "default", None)
        if default is None and hasattr(self, "fixed"):
            default = getattr(self, "fixed", None)

        return default

    @property
    def display_help(self) -> Optional[str]:
        """Return the display help for this element."""
        return None

    @property
    def bases(self) -> Iterator[str]:
        """Return an iterator of all the base types."""
        yield from ()

    @property
    def has_children(self) -> bool:
        """Return whether this element has any children."""
        return next(self.children(), None) is not None

    @property
    def has_form(self) -> bool:
        """Return whether this element has the form attribute."""
        return hasattr(self, "form")

    @property
    def is_abstract(self) -> bool:
        """Return whether this element is defined as abstract."""
        return getattr(self, "abstract", False)

    @property
    def is_property(self) -> bool:
        """Return whether this element is qualified to be a class property."""
        return False

    @property
    def is_fixed(self) -> bool:
        """Return whether this element has a fixed value."""
        return getattr(self, "fixed", None) is not None

    @property
    def is_mixed(self) -> bool:
        """Return whether this element accepts mixed content value."""
        return False

    @property
    def is_nillable(self) -> bool:
        """Return whether this element accepts nillable content."""
        return getattr(self, "nillable", False)

    @property
    def is_qualified(self) -> bool:
        """Return whether this element must be referenced with the target namespace."""
        if self.has_form:
            if getattr(self, "form", FormType.UNQUALIFIED) == FormType.QUALIFIED:
                return True

            if self.is_ref:
                return True

        return False

    @property
    def is_ref(self) -> bool:
        """Return whether this element is a reference to another element."""
        return getattr(self, "ref", None) is not None

    @property
    def is_wildcard(self) -> bool:
        """Return whether this element is a wildcard element/attribute."""
        return False

    @property
    def prefix(self) -> Optional[str]:
        """Return the namespace prefix for this element's type."""
        ref = getattr(self, "ref", None)
        return None if ref is None else text.prefix(ref)

    @property
    def raw_namespace(self) -> Optional[str]:
        """Return if present the target namespace attribute value."""
        return getattr(self, "target_namespace", None)

    @property
    def real_name(self) -> str:
        """Return the real name for this element."""
        name = getattr(self, "name", None) or getattr(self, "ref", None)
        if name:
            return text.suffix(name)

        raise CodegenError(
            "Schema type can't be used as a class/field", type=self.class_name
        )

    @property
    def attr_types(self) -> Iterator[str]:
        """Return the attr types for this element."""
        yield from ()

    @property
    def substitutions(self) -> List[str]:
        """Return the substitution groups of this element."""
        return []

    @property
    def xs_prefix(self) -> Optional[str]:
        """Return the xml schema URI prefix."""
        for prefix, uri in self.ns_map.items():
            if uri == Namespace.XS.uri:
                return prefix

        return None

    def get_restrictions(self) -> Dict[str, Any]:
        """Return the restrictions dictionary of this element."""
        return {}

    def children(self, condition: Callable = return_true) -> Iterator["ElementBase"]:
        """Yield the children recursively that match the given condition."""
        for f in fields(self):
            value = getattr(self, f.name)
            if isinstance(value, list) and value and isinstance(value[0], ElementBase):
                yield from (val for val in value if condition(val))
            elif isinstance(value, ElementBase) and condition(value):
                yield value


def text_node(**kwargs: Any) -> Any:
    """Shortcut method for text node fields."""
    metadata = extract_metadata(kwargs, type=XmlType.TEXT)
    add_default_value(kwargs, optional=False)

    return field(metadata=metadata, **kwargs)


def attribute(optional: bool = True, **kwargs: Any) -> Any:
    """Shortcut method for attribute fields."""
    metadata = extract_metadata(kwargs, type=XmlType.ATTRIBUTE)
    add_default_value(kwargs, optional=optional)

    return field(metadata=metadata, **kwargs)


def element(optional: bool = True, **kwargs: Any) -> Any:
    """Shortcut method for element fields."""
    metadata = extract_metadata(kwargs, type=XmlType.ELEMENT)
    add_default_value(kwargs, optional=optional)

    return field(metadata=metadata, **kwargs)


def add_default_value(params: Dict, optional: bool):
    """Add the default value if it's missing and the optional flag is true."""
    if optional and not ("default" in params or "default_factory" in params):
        params["default"] = None


def array_element(**kwargs: Any) -> Any:
    """Shortcut method for list element fields."""
    metadata = extract_metadata(kwargs, type=XmlType.ELEMENT)
    return field(metadata=metadata, default_factory=list, **kwargs)


def array_any_element(**kwargs: Any) -> Any:
    """Shortcut method for list wildcard fields."""
    metadata = extract_metadata(
        kwargs, type=XmlType.WILDCARD, namespace=NamespaceType.ANY_NS
    )
    return field(metadata=metadata, default_factory=list, **kwargs)


def extract_metadata(params: Dict, **kwargs: Any) -> Dict:
    """Remove dataclasses standard field properties and merge any additional."""
    metadata = {
        key: params.pop(key) for key in list(params.keys()) if key not in FIELD_PARAMS
    }
    metadata.update(kwargs)
    return metadata


FIELD_PARAMS = (
    "default",
    "default_factory",
    "init",
    "repr",
    "hash",
    "compare",
)
