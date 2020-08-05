import os
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional

from xsdata.exceptions import SchemaValueError
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.models.enums import DataType
from xsdata.models.enums import FormType
from xsdata.models.enums import Namespace
from xsdata.models.enums import NamespaceType
from xsdata.utils import collections
from xsdata.utils import text

Condition = Optional[Callable]


@dataclass
class ElementBase:
    """
    Base xsd schema model.

    :param index: Occurrence position inside the definition
    :param ns_map: Namespaces map to prefixes.
    """

    index: int = field(default_factory=int, init=False)
    ns_map: Dict = field(default_factory=dict, init=False)

    @property
    def class_name(self) -> str:
        """Return the schema element class name."""
        return self.__class__.__name__

    @property
    def default_type(self) -> str:
        """Return the default type if the given element has not specific
        type."""
        return self.data_type_ref(DataType.STRING)

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

        :raises SchemaValueError: when instance has no name/ref attribute.
        """
        name = getattr(self, "name", None) or getattr(self, "ref", None)
        if name:
            return text.suffix(name)

        raise SchemaValueError(f"Schema class `{self.class_name}` unknown real name.")

    @property
    def real_type(self) -> str:
        """
        Return the real type for this element.

        :raises SchemaValueError: when attribute instance is missing implementation.
        """
        raise SchemaValueError(f"Schema class `{self.class_name}` unknown real type.")

    @property
    def substitutions(self) -> List[str]:
        """Return the substitution groups of this element."""
        return []

    def data_type_ref(self, data_type: DataType) -> str:
        """Return the given data type code with the xml schema namespace prefix
        if any."""
        prefix = collections.map_key(self.ns_map, Namespace.XS.uri)
        return f"{prefix}:{data_type.code}" if prefix else data_type.code

    def get_restrictions(self) -> Dict[str, Any]:
        """Return the restrictions dictionary of this element."""
        return {}

    def children(self, condition: Condition = None) -> Iterator["ElementBase"]:
        """Iterate over all the ElementBase children of this element that match
        the given condition if any."""
        for f in fields(self):
            value = getattr(self, f.name)
            if (
                isinstance(value, list)
                and len(value) > 0
                and isinstance(value[0], ElementBase)
            ):
                yield from (val for val in value if not condition or condition(val))
            elif isinstance(value, ElementBase):
                if not condition or condition(value):
                    yield value


class ModuleMixin:
    @property
    def module(self) -> str:
        """Return a valid module name based on the instance location uri."""
        location = getattr(self, "location", None)
        if not location:
            raise SchemaValueError(f"{self.__class__.__name__} empty location.")

        module = location.split("/")[-1]
        name, extension = os.path.splitext(module)
        return name if extension in (".xsd", ".wsdl") else module


def attribute(default: Any = None, init: bool = True, **kwargs: Any) -> Any:
    """Shortcut method for attribute fields."""
    kwargs.update(type=XmlType.ATTRIBUTE)
    return field(init=init, default=default, metadata=kwargs)


def element(init: bool = True, **kwargs: Any) -> Any:
    """Shortcut method for element fields."""
    kwargs.update(type=XmlType.ELEMENT)
    return field(init=init, default=None, metadata=kwargs)


def array_element(init: bool = True, **kwargs: Any) -> Any:
    """Shortcut method for list element fields."""
    kwargs.update(type=XmlType.ELEMENT)
    return field(init=init, default_factory=list, metadata=kwargs)


def array_any_element(init: bool = True, **kwargs: Any) -> Any:
    """Shortcut method for list wildcard fields."""
    kwargs.update(type=XmlType.WILDCARD, namespace=NamespaceType.ANY)
    return field(init=init, default_factory=list, metadata=kwargs)
