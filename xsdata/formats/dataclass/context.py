from dataclasses import dataclass
from dataclasses import Field
from dataclasses import field
from dataclasses import fields
from dataclasses import is_dataclass
from dataclasses import MISSING
from typing import Any
from typing import Callable
from typing import Dict
from typing import get_type_hints
from typing import Iterator
from typing import List
from typing import Optional
from typing import Type

from lxml.etree import QName

from xsdata.exceptions import ModelInspectionError
from xsdata.formats.converters import sort_types
from xsdata.formats.dataclass.models.context import ClassMeta
from xsdata.formats.dataclass.models.context import ClassVar
from xsdata.formats.dataclass.models.context import Tag
from xsdata.models.enums import NamespaceType


@dataclass
class ModelContext:
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
            nillable = getattr(meta, "nillable", False)
            namespace = getattr(meta, "namespace", parent_ns)

            self.cache[clazz] = ClassMeta(
                name=name,
                clazz=clazz,
                qname=QName(namespace, name),
                nillable=nillable,
                vars=list(self.get_type_hints(clazz, namespace)),
            )
        return self.cache[clazz]

    def get_type_hints(self, clazz, parent_ns: Optional[str]) -> Iterator[ClassVar]:
        type_hints = get_type_hints(clazz)

        for var in fields(clazz):
            type_hint = type_hints[var.name]
            types = self.real_types(type_hint)

            tag = Tag.from_metadata_type(var.metadata.get("type"))
            namespace = var.metadata.get("namespace")
            namespaces = self.resolve_namespaces(tag, namespace, parent_ns)
            local_name = var.metadata.get("name") or self.name_generator(var.name)
            is_class = next((False for clazz in types if not is_dataclass(clazz)), True)

            first_namespace = (
                namespaces[0]
                if len(namespaces) > 0 and namespaces[0] and namespaces[0][0] != "#"
                else None
            )

            yield ClassVar(
                name=var.name,
                qname=QName(first_namespace, local_name),
                namespaces=namespaces,
                tag=tag,
                init=var.init,
                nillable=var.metadata.get("nillable", False),
                dataclass=is_class,
                sequential=var.metadata.get("sequential", False),
                types=types,
                default=self.default_value(var),
            )

    @staticmethod
    def resolve_namespaces(tag: Tag, namespace, parent_namespace):

        if tag in (Tag.ELEMENT, Tag.ANY_ELEMENT) and namespace is None:
            namespace = parent_namespace

        if not namespace:
            return []

        result = set()
        for ns in namespace.split(" "):
            ns = ns.strip()
            if not ns:
                continue

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
    def real_types(type_hint) -> List:
        types = []
        if type_hint is Dict:
            types.append(type_hint)
        elif hasattr(type_hint, "__origin__"):
            while len(type_hint.__args__) == 1 and hasattr(
                type_hint.__args__[0], "__origin__"
            ):
                type_hint = type_hint.__args__[0]

            types = [
                x for x in type_hint.__args__ if x is not None.__class__  # type: ignore
            ]
        else:
            types.append(type_hint)

        return sort_types(types)
