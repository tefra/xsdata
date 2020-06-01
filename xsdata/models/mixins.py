from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from typing import Any
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import TypeVar

from xsdata.exceptions import SchemaValueError
from xsdata.models.enums import DataType
from xsdata.models.enums import FormType
from xsdata.models.enums import Namespace
from xsdata.utils import text

T = TypeVar("T", bound="ElementBase")


@dataclass
class ElementBase:
    """
    Base xsd schema model.

    :param index: Occurrence position inside the definition
    :param ns_map: Namespaces map to prefixes.
    """

    index: int = field(default_factory=int)
    ns_map: Dict = field(default_factory=dict)

    @property
    def class_name(self) -> str:
        """Return the schema element class name."""
        return self.__class__.__name__

    @property
    def default_type(self) -> DataType:
        """Return the default type if the given element has not specific
        type."""
        return DataType.STRING

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
    def extensions(self) -> Iterator[str]:
        """Return an iterator of all the base types."""
        yield from ()

    @property
    def has_children(self) -> bool:
        """Return whether or not this element has any children."""
        return any(True for _ in self.children())

    @property
    def has_form(self) -> bool:
        """Return whether or not this element has the form attribute."""
        return hasattr(self, "form")

    @property
    def is_abstract(self) -> bool:
        """Return whether or not this element is defined as abstract."""
        return getattr(self, "abstract", False)

    @property
    def is_attribute(self) -> bool:
        """Return whether or not this element is qualified to be a class
        attribute."""
        return False

    @property
    def is_fixed(self) -> bool:
        """Return whether or not this element has a fixed value."""
        return getattr(self, "fixed", None) is not None

    @property
    def is_mixed(self) -> bool:
        """Return whether or not this element accepts mixed content value."""
        return False

    @property
    def is_nillable(self) -> bool:
        """Return whether or not this element is accepts empty empty values."""
        return getattr(self, "nillable", False)

    @property
    def is_qualified(self) -> bool:
        """Return whether or not this element name needs to be referenced with
        the target namespace."""
        if self.has_form:
            if getattr(self, "form", FormType.UNQUALIFIED) == FormType.QUALIFIED:
                return True

            if self.is_ref:
                return True

        return False

    @property
    def is_ref(self) -> bool:
        """Return whether or not this element is a reference to another
        element."""
        return getattr(self, "ref", None) is not None

    @property
    def is_wildcard(self) -> bool:
        """Return whether or not this element is a wildcard
        element/attribute."""
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
    def raw_type(self) -> Optional[str]:
        """Return if present the type attribute value."""
        return getattr(self, "type", None)

    @property
    def real_name(self) -> str:
        """
        Return the real name for this element by looking by looking either to
        the name or ref attribute value.

        :raises: SchemaValueError if this property is accessed by any elements that
        don't have either name/ref properties present.
        """
        name = getattr(self, "name", None) or getattr(self, "ref", None)
        if name:
            return name

        raise SchemaValueError(f"Schema class `{self.class_name}` unknown real name.")

    @property
    def real_type(self) -> Optional[str]:
        """
        Return the real type for this element.

        :raises: SchemaValueError if this property is accessed by any element that
        doesn't have any type lookup algorithm.
        """
        raise SchemaValueError(f"Schema class `{self.class_name}` unknown real type.")

    @property
    def substitutions(self) -> List[str]:
        """Return the substitution groups of this element."""
        return []

    def get_restrictions(self) -> Dict[str, Any]:
        """Return the restrictions dictionary of this element."""
        return {}

    def schema_prefix(self) -> Optional[str]:
        """Return the target namespace prefix used in the schema definition if
        any."""
        return next(
            (
                prefix
                for prefix, namespace in self.ns_map.items()
                if namespace == Namespace.XS.uri
            ),
            None,
        )

    def children(self) -> Iterator["ElementBase"]:
        """Iterate over all the ElementBase childrent of this element."""
        for attribute in fields(self):
            value = getattr(self, attribute.name)
            if (
                isinstance(value, list)
                and len(value) > 0
                and isinstance(value[0], ElementBase)
            ):
                yield from value
            elif isinstance(value, ElementBase):
                yield value
