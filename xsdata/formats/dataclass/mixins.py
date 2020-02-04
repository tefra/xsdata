from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from dataclasses import is_dataclass
from dataclasses import MISSING
from enum import Enum
from typing import Any
from typing import Callable
from typing import Dict
from typing import get_type_hints
from typing import Iterator
from typing import List
from typing import Optional
from typing import Set
from typing import Type

from lxml.etree import QName

from xsdata.models.enums import TagType


class NodeType(Enum):
    TEXT = 1
    ATTRIBUTE = 2
    ELEMENT = 3
    ROOT = 4


@dataclass(frozen=True)
class Field:
    name: str
    local_name: str
    type: Any
    node_type: NodeType
    is_nillable: bool = False
    is_list: bool = False
    is_dataclass: bool = False
    default: Any = None
    namespace: Optional[str] = None

    @property
    def is_attribute(self):
        return self.node_type == NodeType.ATTRIBUTE

    @property
    def is_text(self):
        return self.node_type == NodeType.TEXT

    @property
    def is_element(self):
        return self.node_type == NodeType.ELEMENT


@dataclass(frozen=True)
class Meta:
    name: str
    mixed: bool
    namespace: Optional[str]


@dataclass
class QueueItem:

    index: int = field(default_factory=int)
    child_index: int = field(default_factory=int)
    qname: Optional[QName] = None
    clazz: Optional[Type] = None
    meta: Optional[Meta] = None
    fields: Dict = field(default_factory=dict)


@dataclass
class ModelInspect:
    name: Callable = field(default=lambda x: x)
    fields_cache: Dict = field(init=False, default_factory=dict)
    class_cache: Dict = field(init=False, default_factory=dict)
    ns_cache: Dict = field(init=False, default_factory=dict)

    def fields(self, clazz: Type) -> List[Field]:
        if clazz not in self.fields_cache:
            if not self.is_dataclass(clazz):
                raise TypeError(f"Object {clazz} is not a dataclass")

            self.fields_cache[clazz] = list(self.get_type_hints(clazz))

        return self.fields_cache[clazz]

    def namespaces(self, clazz: Type) -> List[str]:
        if clazz not in self.ns_cache:
            if not self.is_dataclass(clazz):
                raise TypeError(f"Object {clazz} is not a dataclass")

            self.ns_cache[clazz] = list(self.get_unique_namespaces(clazz))

        return self.ns_cache[clazz]

    def get_unique_namespaces(self, clazz) -> Set[str]:
        namespaces = set()
        if self.is_dataclass(clazz):
            meta = self.class_meta(clazz)
            if meta.namespace:
                namespaces.add(meta.namespace)

            for f in self.fields(clazz):
                if f.namespace:
                    namespaces.add(f.namespace)
                if f.is_dataclass:
                    namespaces.update(self.namespaces(f.type))

        return namespaces

    def get_type_hints(self, clazz) -> Iterator[Field]:
        type_hints = get_type_hints(clazz)

        for arg in fields(clazz):
            tp = type_hints[arg.name]
            is_list = False

            if hasattr(tp, "__origin__"):
                is_list = tp.__origin__ is list
                tp = tp.__args__[0]

            default_value = None
            if arg.default_factory is not MISSING:  # type: ignore
                default_value = arg.default_factory  # type: ignore
            elif arg.default is not MISSING:
                default_value = arg.default

            namespace = arg.metadata.get("namespace")
            if namespace is None:
                namespace = self.class_meta(tp).namespace

            yield Field(
                name=arg.name,
                local_name=arg.metadata.get("name") or self.name(arg.name),
                node_type=self.node_type(arg.metadata.get("type")),
                is_list=is_list,
                is_nillable=arg.metadata.get("nillable") is True,
                is_dataclass=self.is_dataclass(tp),
                type=tp,
                default=default_value,
                namespace=namespace,
            )

    @staticmethod
    def node_type(type_str: Optional[str]):
        if type_str == TagType.ATTRIBUTE:
            return NodeType.ATTRIBUTE
        if type_str == TagType.ELEMENT:
            return NodeType.ELEMENT

        return NodeType.TEXT

    def class_meta(self, clazz: Type) -> Meta:
        if clazz not in self.class_cache:
            meta = getattr(clazz, "Meta", None)
            self.class_cache[clazz] = Meta(
                name=getattr(meta, "name", self.name(clazz.__name__)),
                mixed=getattr(meta, "mixed", False),
                namespace=getattr(meta, "namespace", None),
            )
        return self.class_cache[clazz]

    @staticmethod
    def is_dataclass(obj: object):
        return is_dataclass(obj)
