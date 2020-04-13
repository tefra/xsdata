from dataclasses import dataclass
from dataclasses import field
from typing import Any
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
    def clazz(self):
        return self.types[0] if self.dataclass else None

    @property
    def is_any_type(self):
        return False

    @property
    def is_attribute(self):
        return False

    @property
    def is_attributes(self):
        return False

    @property
    def is_element(self):
        return False

    @property
    def is_list(self):
        return self.default is list

    @property
    def is_text(self):
        return False

    @property
    def is_tokens(self):
        return False

    @property
    def is_wildcard(self):
        return False

    def matches(self, qname: QName, condition=None):
        if condition and not condition(self):
            return False

        return qname in (self.qname, QNames.ALL)


@dataclass(frozen=True)
class XmlElement(XmlVar):
    @property
    def is_element(self):
        return True

    @property
    def is_any_type(self):
        """xs:element with type anyType."""
        return len(self.types) == 1 and self.types[0] is object


@dataclass(frozen=True)
class XmlWildcard(XmlVar):
    @property
    def is_wildcard(self):
        return True

    @property
    def is_any_type(self):
        return True

    def matches(self, qname: QName, condition=None):
        if condition and not condition(self):
            return False

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
    def is_attribute(self):
        return True


@dataclass(frozen=True)
class XmlAttributes(XmlVar):
    @property
    def is_attributes(self):
        return True


@dataclass(frozen=True)
class XmlText(XmlVar):
    @property
    def is_tokens(self):
        return self.is_list

    @property
    def is_text(self):
        return True


@dataclass(frozen=True)
class XmlMeta:
    name: str
    clazz: Type
    qname: QName
    nillable: bool
    vars: List[XmlVar] = field(default_factory=list)

    def find_var(self, qname: QName = QNames.ALL, condition=None) -> Optional[XmlVar]:
        for var in self.vars:
            if not var.is_wildcard and var.matches(qname, condition):
                return var

        for var in self.vars:
            if var.is_wildcard and var.matches(qname, condition):
                return var

        return None
