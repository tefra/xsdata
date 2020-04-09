from dataclasses import dataclass
from enum import IntEnum
from typing import Any
from typing import List
from typing import Optional
from typing import Type

from lxml.etree import QName

from xsdata.models.enums import NamespaceType
from xsdata.models.enums import TagType


class Tag(IntEnum):
    TEXT = 1
    ATTRIBUTE = 2
    ANY_ATTRIBUTE = 3
    ELEMENT = 4
    ANY_ELEMENT = 5
    ROOT = 6
    MISC = 7

    @classmethod
    def from_metadata_type(cls, meta_type: Optional[str]) -> "Tag":
        return __tag_type_map__.get(meta_type, cls.TEXT)


__tag_type_map__ = {
    TagType.ATTRIBUTE: Tag.ATTRIBUTE,
    TagType.ANY_ATTRIBUTE: Tag.ANY_ATTRIBUTE,
    TagType.ELEMENT: Tag.ELEMENT,
    TagType.ANY: Tag.ANY_ELEMENT,
    None: Tag.MISC,
}


@dataclass(frozen=True)
class ClassVar:
    name: str
    qname: QName
    namespaces: List[str]
    types: List[Type]
    tag: Tag
    init: bool = True
    nillable: bool = False
    dataclass: bool = False
    sequential: bool = False
    default: Any = None

    @property
    def clazz(self):
        return self.types[0] if self.dataclass else None

    @property
    def is_attribute(self):
        return self.tag == Tag.ATTRIBUTE

    @property
    def is_any_attribute(self):
        return self.tag == Tag.ANY_ATTRIBUTE

    @property
    def is_any_element(self):
        return self.tag == Tag.ANY_ELEMENT

    @property
    def is_element(self):
        return self.tag == Tag.ELEMENT

    @property
    def is_list(self):
        return self.default is list

    @property
    def is_text(self):
        return self.tag == Tag.TEXT

    @property
    def namespace(self):
        return self.qname.namespace

    def matches(self, qname: QName, condition=None):
        if condition and not condition(self):
            return False

        if not self.is_any_element and qname.localname != self.qname.localname:
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
class ClassMeta:
    name: str
    clazz: Type
    qname: QName
    nillable: bool
    vars: List[ClassVar]

    @property
    def namespace(self):
        return self.qname.namespace

    @property
    def any_text(self) -> Optional[ClassVar]:
        return next((var for var in self.vars if var.is_text), None)

    @property
    def any_attribute(self) -> Optional[ClassVar]:
        return next((var for var in self.vars if var.is_any_attribute), None)

    @property
    def any_element(self) -> Optional[ClassVar]:
        return next((var for var in self.vars if var.is_any_element), None)

    def find_var(self, qname: QName, condition=None):
        for var in self.vars:
            if not var.is_any_element and var.matches(qname, condition):
                return var

        for var in self.vars:
            if var.is_any_element and var.matches(qname, condition):
                return var
