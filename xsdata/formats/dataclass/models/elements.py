from dataclasses import dataclass
from dataclasses import field
from enum import auto
from enum import IntEnum
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from lxml.etree import QName

from xsdata.models.enums import FormType
from xsdata.models.enums import NamespaceType
from xsdata.models.enums import QNames


@dataclass(frozen=True)
class XmlVar:
    """
    Dataclass field bind metadata.

    :param name: field name,
    :param qname: qualified local name,
    :param init:  field is present in the constructor arguments.
    :param nillable: allow to render empty nillable elements,
    :param dataclass: field type is a dataclass or a primitive type.
    :param sequential: switch to sequential rendering with other sequential siblings,
    :param default: default value or factory
    :param types: field bind or cast types.
    :param namespaces: a list of the all the possible namespaces.
    """

    name: str
    qname: QName
    init: bool = True
    nillable: bool = False
    dataclass: bool = False
    sequential: bool = False
    default: Any = None
    types: List[Type] = field(default_factory=list)
    namespaces: List[str] = field(default_factory=list)

    @property
    def clazz(self) -> Optional[Type]:
        """Return the first type if field is bound to a dataclass."""
        return self.types[0] if self.dataclass else None

    @property
    def is_any_type(self) -> bool:
        """Return whether or not the field type is xs:anyType."""
        return False

    @property
    def is_attribute(self) -> bool:
        """Return whether or not the field is derived from xs:attribute."""
        return False

    @property
    def is_attributes(self) -> bool:
        """Return whether or not the field is derived from xs:anyAttributes."""
        return False

    @property
    def is_element(self) -> bool:
        """Return whether or not the field is derived from xs:element."""
        return False

    @property
    def is_list(self) -> bool:
        """Return whether or not the field is a list of elements."""
        return self.default is list

    @property
    def is_text(self) -> bool:
        """Return whether or not the field is a text element."""
        return False

    @property
    def is_tokens(self) -> bool:
        """Return whether or not the field is a list of tokens."""
        return False

    @property
    def is_wildcard(self) -> bool:
        """Return whether or not the field is a text element."""
        return False

    def matches(self, qname: QName) -> bool:
        """
        Match the field qualified local name to the given qname.

        Return True automatically if the local name is a wildcard.
        """
        return qname in (self.qname, QNames.ALL)


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
    def is_wildcard(self) -> bool:
        return True

    @property
    def is_any_type(self) -> bool:
        return True

    def matches(self, qname: QName) -> bool:
        """Match the given qname to the wildcard allowed namespaces."""

        if qname == QNames.ALL:
            return True

        if not self.namespaces and qname.namespace is None:
            return True

        for namespace in self.namespaces:
            if not namespace and qname.namespace is None:
                return True
            if namespace == qname.namespace:
                return True
            if namespace == NamespaceType.ANY.value:
                return True
            if namespace and namespace[0] == "!" and namespace[1:] != qname.namespace:
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
    def is_tokens(self) -> bool:
        return self.is_list

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
    FindMode.NOT_WILDCARD: lambda x: not x.is_wildcard,
    FindMode.LIST: lambda x: x.is_list,
    FindMode.NOT_LIST: lambda x: not x.is_list,
}


@dataclass(frozen=True)
class XmlMeta:
    """
    Dataclass model bind metadata.

    :param name: local name
    :param clazz: dataclass type
    :param qname: local name qualified with target namespace.
    :param source_qname: local name qualified with source namespace.
    :param nillable: allow render as empty element.
    :param vars: list of field metadata
    :param cache: field lookup cache
    """

    name: str
    clazz: Type
    qname: QName
    source_qname: QName
    nillable: bool
    vars: List[XmlVar] = field(default_factory=list)
    cache: Dict = field(default_factory=dict)

    @property
    def element_form(self) -> FormType:
        """Return element form: qualified/unqualified."""
        return (
            FormType.UNQUALIFIED
            if not self.qname.namespace
            or any(var.is_element and not var.namespaces for var in self.vars)
            else FormType.QUALIFIED
        )

    def find_var(
        self, qname: QName = QNames.ALL, mode: FindMode = FindMode.ALL
    ) -> Optional[XmlVar]:
        """
        Find a field by it's qualified name and the specified type.

        The lookup process is cached.
        """
        key = (
            hash(qname),
            hash(mode),
        )
        if key not in self.cache:
            self.cache[key] = self._find_var(qname, mode)

        return self.cache[key]

    def _find_var(
        self, qname: QName = QNames.ALL, mode: FindMode = FindMode.ALL,
    ) -> Optional[XmlVar]:

        find_func = find_lambdas[mode]

        return next(
            (var for var in self.vars if find_func(var) and var.matches(qname)), None,
        )
