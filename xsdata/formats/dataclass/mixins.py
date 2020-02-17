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
        return next((var for var in self.vars.values() if var.is_text), None)

    @property
    def any_attribute(self) -> Optional[ClassVar]:
        return next((var for var in self.vars.values() if var.is_any_attribute), None)

    @property
    def any_element(self) -> Optional[ClassVar]:
        return next((var for var in self.vars.values() if var.is_any_element), None)


@dataclass
class ModelInspect:
    name_generator: Callable = field(default=lambda x: x)
    cache: Dict[Type, ClassMeta] = field(default_factory=dict)

    def class_meta(self, clazz: Type, parent_ns: Optional[str] = None) -> ClassMeta:
        if clazz not in self.cache:
            if not is_dataclass(clazz):
                raise TypeError(f"Object {clazz} is not a dataclass.")

            meta = getattr(clazz, "Meta", None)
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
            namespace = self.real_namespace(var, tag, parent_ns)
            local_name = var.metadata.get("name") or self.name_generator(var.name)
            is_class = next((False for clazz in types if not is_dataclass(clazz)), True)

            yield ClassVar(
                name=var.name,
                qname=QName(namespace or None, local_name),
                tag=tag,
                init=var.init,
                is_list=is_list,
                is_nillable=var.metadata.get("nillable") is True,
                is_dataclass=is_class,
                types=types,
                default=self.default_value(var),
            )

    @staticmethod
    def real_namespace(var: Field, tag: Tag, parent_ns: Optional[str]) -> Optional[str]:
        namespace = var.metadata.get("namespace")
        if tag == Tag.ELEMENT:
            return namespace if namespace is not None else parent_ns
        else:
            return namespace

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

        return is_list, types
