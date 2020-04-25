from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Type

from lxml.etree import QName

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


@dataclass(frozen=True)
class XmlMeta:
    name: str
    clazz: Type
    qname: QName
    source_qname: QName
    nillable: bool
    vars: List[XmlVar] = field(default_factory=list)

    def find_var(
        self, qname: QName = QNames.ALL, condition: Optional[Callable] = None
    ) -> Optional[XmlVar]:
        for var in self.vars:
            if condition and not condition(var):
                continue

            if var.matches(qname):
                return var

        return None
