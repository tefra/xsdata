from dataclasses import dataclass
from dataclasses import Field
from dataclasses import field
from dataclasses import fields
from dataclasses import is_dataclass
from dataclasses import MISSING
from enum import IntEnum
from typing import Any
from typing import Callable
from typing import Dict
from typing import get_type_hints
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from lxml.etree import QName

from xsdata.exceptions import ModelInspectionError
from xsdata.formats.converters import sort_types
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
    is_nillable: bool = False
    is_list: bool = False
    is_dataclass: bool = False
    default: Any = None
    wild_ns: List[str] = field(default_factory=list)

    @property
    def clazz(self):
        return self.types[0] if self.is_dataclass else None

    @property
    def is_attribute(self):
        return self.tag == Tag.ATTRIBUTE

    @property
    def is_any_attribute(self):
        return self.tag == Tag.ANY_ATTRIBUTE

    @property
    def is_element(self):
        return self.tag == Tag.ELEMENT

    @property
    def is_any_element(self):
        return self.tag == Tag.ANY_ELEMENT

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
    mixed: bool
    vars: Dict[QName, ClassVar]

    @property
    def namespace(self):
        return self.qname.namespace

    @property
    def any_text(self) -> Optional[ClassVar]:
        return next((var for qname, var in self.vars.items() if var.is_text), None)

    @property
    def any_attribute(self) -> Optional[ClassVar]:
        return next(
            (var for qname, var in self.vars.items() if var.is_any_attribute), None
        )

    @property
    def any_element(self) -> Optional[ClassVar]:
        return next(
            (var for qname, var in self.vars.items() if var.is_any_element), None
        )

    def get_var(self, qname: QName) -> Optional[ClassVar]:
        if qname in self.vars:
            return self.vars[qname]

        return next(
            (
                var
                for _, var in self.vars.items()
                for wild_ns in var.wild_ns
                if self.match(wild_ns, qname)
            ),
            None,
        )

    @staticmethod
    def match(namespace: str, qname: QName):
        return (
            namespace
            and (
                namespace == qname.namespace
                or namespace == NamespaceType.ANY.value
                or namespace[0] == "!"
                and namespace[1:] != qname.namespace
            )
        ) or (not namespace and qname.namespace is None)


@dataclass
class ModelInspect:
    name_generator: Callable = field(default=lambda x: x)
    cache: Dict[Type, ClassMeta] = field(default_factory=dict)

    def class_meta(self, clazz: Type, parent_ns: Optional[str] = None) -> ClassMeta:
        if clazz not in self.cache:
            if not is_dataclass(clazz):
                raise ModelInspectionError(f"Object {clazz} is not a dataclass.")

            meta = getattr(clazz, "Meta", None)
            if meta and meta.__qualname__ != f"{clazz.__name__}.Meta":
                meta = None

            name = getattr(meta, "name", self.name_generator(clazz.__name__))
            mixed = getattr(meta, "mixed", False)
            namespace = getattr(meta, "namespace", parent_ns)

            self.cache[clazz] = ClassMeta(
                name=name,
                clazz=clazz,
                qname=QName(namespace, name),
                mixed=mixed,
                vars={arg.qname: arg for arg in self.get_type_hints(clazz, namespace)},
            )
        return self.cache[clazz]

    def get_type_hints(self, clazz, parent_ns: Optional[str]) -> Iterator[ClassVar]:
        type_hints = get_type_hints(clazz)

        for var in fields(clazz):
            type_hint = type_hints[var.name]
            is_list, types = self.real_types(type_hint)

            tag = Tag.from_metadata_type(var.metadata.get("type"))
            namespace = var.metadata.get("namespace")
            real_namespace = self.resolve_namespace(namespace, tag, parent_ns)
            wild_namespaces = self.wild_namespaces(namespace, tag, parent_ns)

            local_name = var.metadata.get("name") or self.name_generator(var.name)
            is_class = next((False for clazz in types if not is_dataclass(clazz)), True)

            yield ClassVar(
                name=var.name,
                qname=QName(real_namespace, local_name),
                wild_ns=wild_namespaces,
                tag=tag,
                init=var.init,
                is_list=is_list,
                is_nillable=var.metadata.get("nillable") is True,
                is_dataclass=is_class,
                types=types,
                default=self.default_value(var),
            )

    @staticmethod
    def resolve_namespace(
        namespace: Optional[str], tag: Tag, parent_namespace: Optional[str]
    ) -> Optional[str]:
        if tag == Tag.ANY_ELEMENT:
            namespace = None
        elif tag == Tag.ELEMENT and namespace is None:
            namespace = parent_namespace

        return namespace or None

    @staticmethod
    def wild_namespaces(
        namespace: Optional[str], tag: Tag, parent_namespace: Optional[str]
    ) -> List[str]:
        if tag != Tag.ANY_ELEMENT:
            return []

        result = set()
        for ns in (namespace or "##any").split(" "):
            ns = ns.strip()
            if ns:
                ns_type = NamespaceType.get_enum(ns)
                if ns_type == NamespaceType.TARGET:
                    result.add(parent_namespace or NamespaceType.ANY.value)
                elif ns_type == NamespaceType.LOCAL:
                    result.add("")
                elif ns_type == NamespaceType.OTHER:
                    result.add(f"!{parent_namespace or ''}")
                else:
                    result.add(ns)
        return list(result)

    @staticmethod
    def default_value(var: Field) -> Any:
        if var.default_factory is not MISSING:  # type: ignore
            return var.default_factory  # type: ignore
        elif var.default is not MISSING:
            return var.default
        else:
            return None

    @staticmethod
    def real_types(type_hint) -> Tuple:
        is_list = False
        types = []
        if type_hint is Dict:
            types.append(type_hint)
        elif hasattr(type_hint, "__origin__"):
            is_list = type_hint.__origin__ is list

            while len(type_hint.__args__) == 1 and hasattr(
                type_hint.__args__[0], "__origin__"
            ):
                type_hint = type_hint.__args__[0]

            types = [
                x for x in type_hint.__args__ if x is not None.__class__  # type: ignore
            ]
        else:
            types.append(type_hint)

        return is_list, sort_types(types)
