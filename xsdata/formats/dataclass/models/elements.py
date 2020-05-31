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
        return self.types[0] if self.dataclass else None

    @property
    def is_any_type(self) -> bool:
        return False

    @property
    def is_attribute(self) -> bool:
        return False

    @property
    def is_attributes(self) -> bool:
        return False

    @property
    def is_element(self) -> bool:
        return False

    @property
    def is_list(self) -> bool:
        return self.default is list

    @property
    def is_text(self) -> bool:
        return False

    @property
    def is_tokens(self) -> bool:
        return False

    @property
    def is_wildcard(self) -> bool:
        return False

    def matches(self, qname: QName) -> bool:
        return qname in (self.qname, QNames.ALL)


@dataclass(frozen=True)
class XmlElement(XmlVar):
    @property
    def is_element(self) -> bool:
        return True

    @property
    def is_any_type(self) -> bool:
        """xs:element with type anyType."""
        return len(self.types) == 1 and self.types[0] is object


@dataclass(frozen=True)
class XmlWildcard(XmlVar):
    @property
    def is_wildcard(self) -> bool:
        return True

    @property
    def is_any_type(self) -> bool:
        return True

    def matches(self, qname: QName) -> bool:
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
    @property
    def is_attribute(self) -> bool:
        return True


@dataclass(frozen=True)
class XmlAttributes(XmlVar):
    @property
    def is_attributes(self) -> bool:
        return True


@dataclass(frozen=True)
class XmlText(XmlVar):
    @property
    def is_tokens(self) -> bool:
        return self.is_list

    @property
    def is_text(self) -> bool:
        return True


class FindMode(IntEnum):
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
    name: str
    clazz: Type
    qname: QName
    source_qname: QName
    nillable: bool
    vars: List[XmlVar] = field(default_factory=list)
    cache: Dict = field(default_factory=dict)

    @property
    def element_form(self) -> FormType:
        return (
            FormType.UNQUALIFIED
            if not self.qname.namespace
            or any(var.is_element and not var.namespaces for var in self.vars)
            else FormType.QUALIFIED
        )

    def find_var(
        self, qname: QName = QNames.ALL, mode: FindMode = FindMode.ALL
    ) -> Optional[XmlVar]:

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
