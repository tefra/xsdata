from dataclasses import dataclass
from dataclasses import field
from enum import IntEnum
from typing import Any
from typing import Dict
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
    types: List[Type]
    tag: Tag
    init: bool = True
    nillable: bool = False
    dataclass: bool = False
    sequential: bool = False
    default: Any = None
    wild_ns: List[str] = field(default_factory=list)

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


@dataclass(frozen=True)
class ClassMeta:
    name: str
    clazz: Type
    qname: QName
    nillable: bool
    vars: Dict[QName, ClassVar]

    @property
    def namespace(self):
        return self.qname.namespace

    @property
    def any_text(self) -> Optional[ClassVar]:
        return next((var for var in self.vars.values() if var.is_text), None)

    @property
    def any_attribute(self) -> Optional[ClassVar]:
        return next((var for var in self.vars.values() if var.is_any_attribute), None)

    @property
    def any_element(self) -> Optional[ClassVar]:
        return next((var for var in self.vars.values() if var.is_any_element), None)

    def get_var(self, qname: QName) -> Optional[ClassVar]:
        if qname in self.vars:
            return self.vars[qname]
        else:
            return self.get_wild_var(qname)

    def get_wild_var(self, qname: QName) -> Optional[ClassVar]:
        return next((var for var in self.get_wild_vars(qname)), None)

    def get_matching_wild_var(self, qname: QName, condition):
        return next((x for x in self.get_wild_vars(qname) if condition(x)), None)

    def get_wild_vars(self, qname: QName):
        for var in self.vars.values():
            if self.matches(var.wild_ns, qname):
                yield var

    @classmethod
    def matches(cls, namespaces: List[str], qname: QName) -> bool:
        return next(
            (True for namespace in namespaces if cls.match(namespace, qname)), False
        )

    @classmethod
    def match(cls, namespace: str, qname: QName):
        return (
            namespace
            and (
                namespace == qname.namespace
                or namespace == NamespaceType.ANY.value
                or namespace[0] == "!"
                and namespace[1:] != qname.namespace
            )
        ) or (not namespace and qname.namespace is None)
