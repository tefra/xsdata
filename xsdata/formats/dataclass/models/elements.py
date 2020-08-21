from dataclasses import dataclass
from dataclasses import field
from enum import auto
from enum import IntEnum
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.models.enums import FormType
from xsdata.models.enums import NamespaceType
from xsdata.utils import text


@dataclass(frozen=True)
class XmlVar:
    """
    Dataclass field bind metadata.

    :param name: Field name.
    :param qname: Namespace qualified local name.
    :param init:  Field is present in the constructor parameters.
    :param mixed:  Field supports mixed content.
    :param tokens: Use a list to map simple values.
    :param nillable: Allow empty content elements rendering.
    :param dataclass: Specify whether the field type is a dataclass.
    :param sequential: Switch to sequential rendering with other sequential siblings
    :param list_element: Specify whether the field represents a list of elements
    :param default: Field default value or factory
    :param types: Field simple types.
    :param namespaces: Field list of the all the possible namespaces.
    """

    name: str
    qname: str
    init: bool = True
    mixed: bool = False
    tokens: bool = False
    nillable: bool = False
    dataclass: bool = False
    sequential: bool = False
    list_element: bool = False
    default: Any = None
    types: List[Type] = field(default_factory=list)
    namespaces: List[str] = field(default_factory=list)

    @property
    def clazz(self) -> Optional[Type]:
        """Return the first type if field is bound to a dataclass."""
        return self.types[0] if self.dataclass else None

    @property
    def is_any_type(self) -> bool:
        """Return whether the field type is xs:anyType."""
        return False

    @property
    def is_attribute(self) -> bool:
        """Return whether the field is derived from xs:attribute."""
        return False

    @property
    def is_attributes(self) -> bool:
        """Return whether the field is derived from xs:anyAttributes."""
        return False

    @property
    def is_element(self) -> bool:
        """Return whether the field is derived from xs:element."""
        return False

    @property
    def is_list(self) -> bool:
        """Return whether the field is a list of elements."""
        return self.list_element

    @property
    def is_mixed_content(self) -> bool:
        """Return whether the field is a mixed content list of of elements."""
        return False

    @property
    def is_clazz_union(self) -> bool:
        return self.dataclass and len(self.types) > 1

    @property
    def is_text(self) -> bool:
        """Return whether the field is a text element."""
        return False

    @property
    def is_wildcard(self) -> bool:
        """Return whether the field is a text element."""
        return False

    @property
    def local_name(self) -> str:
        """The element local name."""
        return text.split_qname(self.qname)[1]

    @property
    def namespace(self) -> Optional[str]:
        """The element namespace."""
        return text.split_qname(self.qname)[0]

    def matches(self, qname: str) -> bool:
        """
        Match the field qualified local name to the given qname.

        Return True automatically if the local name is a wildcard.
        """
        return qname in (self.qname, "*")


@dataclass(frozen=True)
class XmlElement(XmlVar):
    """Dataclass field bind metadata for xml elements."""

    @property
    def is_element(self) -> bool:
        return True

    @property
    def is_any_type(self) -> bool:
        return len(self.types) == 1 and self.types[0] is object


@dataclass(frozen=True)
class XmlWildcard(XmlVar):
    """Dataclass field bind metadata for xml wildcard elements."""

    @property
    def is_mixed_content(self) -> bool:
        return self.mixed

    @property
    def is_wildcard(self) -> bool:
        return True

    @property
    def is_any_type(self) -> bool:
        return True

    def matches(self, qname: str) -> bool:
        """Match the given qname to the wildcard allowed namespaces."""

        if qname == "*":
            return True

        namespace, tag = text.split_qname(qname)
        if not self.namespaces and namespace is None:
            return True

        return any(self.match_namespace(ns, namespace) for ns in self.namespaces)

    @staticmethod
    def match_namespace(source: Optional[str], cmp: Optional[str]) -> bool:
        if not source and cmp is None:
            return True
        if source == cmp:
            return True
        if source == NamespaceType.ANY:
            return True
        if source and source[0] == "!" and source[1:] != cmp:
            return True

        return False


@dataclass(frozen=True)
class XmlAttribute(XmlVar):
    """Dataclass field bind metadata for xml attributes."""

    @property
    def is_attribute(self) -> bool:
        return True


@dataclass(frozen=True)
class XmlAttributes(XmlVar):
    """Dataclass field bind metadata for xml wildcard attributes."""

    @property
    def is_attributes(self) -> bool:
        return True


@dataclass(frozen=True)
class XmlText(XmlVar):
    """Dataclass field bind metadata for xml text content."""

    @property
    def is_text(self) -> bool:
        return True


class FindMode(IntEnum):
    """Find switches to be used to find a specific var."""

    ALL = auto()
    ATTRIBUTE = auto()
    ATTRIBUTES = auto()
    ELEMENT = auto()
    TEXT = auto()
    WILDCARD = auto()
    MIXED_CONTENT = ()
    NOT_WILDCARD = auto()
    LIST = auto()
    NOT_LIST = auto()


find_lambdas = {
    FindMode.ALL: lambda x: True,
    FindMode.ATTRIBUTE: lambda x: x.is_attribute,
    FindMode.ATTRIBUTES: lambda x: x.is_attributes,
    FindMode.ELEMENT: lambda x: x.is_element,
    FindMode.TEXT: lambda x: x.is_text,
    FindMode.WILDCARD: lambda x: x.is_wildcard,
    FindMode.MIXED_CONTENT: lambda x: x.is_mixed_content,
    FindMode.NOT_WILDCARD: lambda x: not x.is_wildcard,
    FindMode.LIST: lambda x: x.is_list,
    FindMode.NOT_LIST: lambda x: not x.is_list,
}


@dataclass(frozen=True)
class XmlMeta:
    """
    Dataclass model bind metadata.

    :param name: The local name
    :param clazz: The dataclass type
    :param qname: The namespace qualified name.
    :param source_qname: The source namespace qualified name.
    :param nillable: Specifies whether an explicit empty value can be assigned.
    :param vars: The list of field metadata
    """

    name: str
    clazz: Type
    qname: str
    source_qname: str
    nillable: bool
    vars: List[XmlVar] = field(default_factory=list)
    cache: Dict = field(default_factory=dict, init=False)

    @property
    def element_form(self) -> FormType:
        """Return element form: qualified/unqualified."""
        return (
            FormType.UNQUALIFIED
            if not self.qname.startswith("{")
            or any(var.is_element and not var.namespaces for var in self.vars)
            else FormType.QUALIFIED
        )

    @property
    def namespace(self) -> Optional[str]:
        return text.split_qname(self.qname)[0]

    def find_var(
        self, qname: str = "*", mode: FindMode = FindMode.ALL
    ) -> Optional[XmlVar]:
        """Find and cache a field by it's qualified name and the specified
        mode."""
        key = (qname, mode.value)
        if key not in self.cache:
            self.cache[key] = self._find_var(qname, mode)

        index = self.cache[key]
        return None if index < 0 else self.vars[index]

    def _find_var(self, qname: str, mode: FindMode) -> int:
        find_func = find_lambdas[mode]

        return next(
            (
                index
                for index, var in enumerate(self.vars)
                if find_func(var) and var.matches(qname)
            ),
            -1,
        )
