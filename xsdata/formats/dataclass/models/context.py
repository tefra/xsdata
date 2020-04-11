from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import List
from typing import Optional
from typing import Type

from lxml.etree import QName

from xsdata.models.enums import NamespaceType


@dataclass(frozen=True)
class ClassVar:
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
    def is_attribute(self):
        return False

    @property
    def is_attributes(self):
        return False

    @property
    def is_wildcard(self):
        return False

    @property
    def is_element(self):
        return False

    @property
    def is_list(self):
        return self.default is list

    @property
    def is_tokens(self):
        return self.is_text and self.is_list

    @property
    def is_text(self):
        return False

    @property
    def namespace(self):
        return self.qname.namespace

    def matches(self, qname: QName, condition=None):
        if condition and not condition(self):
            return False
        else:
            return qname == self.qname


@dataclass(frozen=True)
class XmlElement(ClassVar):
    @property
    def is_element(self):
        return True


@dataclass(frozen=True)
class XmlWildcard(ClassVar):
    @property
    def is_wildcard(self):
        return True

    def matches(self, qname: QName, condition=None):
        if condition and not condition(self):
            return False

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
class XmlAttribute(ClassVar):
    @property
    def is_attribute(self):
        return True


@dataclass(frozen=True)
class XmlAttributes(ClassVar):
    @property
    def is_attributes(self):
        return True


@dataclass(frozen=True)
class XmlText(ClassVar):
    @property
    def is_text(self):
        return True


@dataclass(frozen=True)
class ClassMeta:
    name: str
    clazz: Type
    qname: QName
    nillable: bool
    vars: List[ClassVar] = field(default_factory=list)

    @property
    def namespace(self):
        return self.qname.namespace

    @property
    def any_text(self) -> Optional[ClassVar]:
        return next((var for var in self.vars if var.is_text), None)

    @property
    def any_attribute(self) -> Optional[ClassVar]:
        return next((var for var in self.vars if var.is_attributes), None)

    @property
    def any_element(self) -> Optional[ClassVar]:
        return next((var for var in self.vars if var.is_wildcard), None)

    def find_var(self, qname: QName, condition=None) -> Optional[ClassVar]:
        for var in self.vars:
            if not var.is_wildcard and var.matches(qname, condition):
                return var

        for var in self.vars:
            if var.is_wildcard and var.matches(qname, condition):
                return var

        return None
