import sys
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

from xsdata.exceptions import XmlContextError
from xsdata.formats.converters import sort_types
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.models.enums import NamespaceType


@dataclass
class XmlContext:
    name_generator: Callable = field(default=lambda x: x)
    cache: Dict[Type, XmlMeta] = field(default_factory=dict)

    def fetch(
        self,
        clazz: Type,
        parent_ns: Optional[str] = None,
        xsi_type: Optional[QName] = None,
    ) -> XmlMeta:
        meta = self.build(clazz, parent_ns)

        subclass = self.find_subclass(clazz, xsi_type) if xsi_type else None
        if subclass:
            meta = self.build(subclass, parent_ns)

        return meta

    def find_subclass(self, clazz: Type, xsi_type: QName) -> Optional[Type]:
        for subclass in clazz.__subclasses__():
            if self.match_class_source_qname(subclass, xsi_type):
                return subclass

        for base in clazz.__bases__:
            if not is_dataclass(base):
                continue

            if self.match_class_source_qname(base, xsi_type):
                return base

            sibling = self.find_subclass(base, xsi_type)
            if sibling:
                return sibling

        return None

    def match_class_source_qname(self, clazz: Type, xsi_type: QName) -> bool:
        if is_dataclass(clazz):
            meta = self.build(clazz)
            return meta.source_qname == xsi_type

        return False

    def build(self, clazz: Type, parent_ns: Optional[str] = None) -> XmlMeta:
        if clazz not in self.cache:
            if not is_dataclass(clazz):
                raise XmlContextError(f"Object {clazz} is not a dataclass.")

            meta = getattr(clazz, "Meta", None)
            if meta and meta.__qualname__ != f"{clazz.__name__}.Meta":
                meta = None

            name = getattr(meta, "name", self.name_generator(clazz.__name__))
            nillable = getattr(meta, "nillable", False)
            namespace = getattr(meta, "namespace", parent_ns)
            module = sys.modules[clazz.__module__]
            source_namespace = getattr(module, "__NAMESPACE__", None)

            self.cache[clazz] = XmlMeta(
                name=name,
                clazz=clazz,
                qname=QName(namespace, name),
                source_qname=QName(source_namespace, name),
                nillable=nillable,
                vars=list(self.get_type_hints(clazz, namespace)),
            )
        return self.cache[clazz]

    def get_type_hints(self, clazz: Type, parent_ns: Optional[str]) -> Iterator[XmlVar]:
        type_hints = get_type_hints(clazz)

        for var in fields(clazz):
            type_hint = type_hints[var.name]
            types = self.real_types(type_hint)
            xml_type = var.metadata.get("type")
            xml_clazz = XmlType.to_xml_class(xml_type)
            namespace = var.metadata.get("namespace")
            namespaces = self.resolve_namespaces(xml_type, namespace, parent_ns)
            local_name = var.metadata.get("name") or self.name_generator(var.name)
            is_class = any(is_dataclass(clazz) for clazz in types)
            first_namespace = (
                namespaces[0]
                if len(namespaces) > 0 and namespaces[0] and namespaces[0][0] != "#"
                else None
            )

            yield xml_clazz(
                name=var.name,
                qname=QName(first_namespace, local_name),
                namespaces=namespaces,
                init=var.init,
                nillable=var.metadata.get("nillable", False),
                dataclass=is_class,
                sequential=var.metadata.get("sequential", False),
                types=types,
                default=self.default_value(var),
            )

    @staticmethod
    def resolve_namespaces(
        xml_type: Optional[str],
        namespace: Optional[str],
        parent_namespace: Optional[str],
    ) -> List[str]:

        if xml_type in (XmlType.ELEMENT, XmlType.WILDCARD) and namespace is None:
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

        if var.default is not MISSING:
            return var.default

        return None

    @staticmethod
    def real_types(type_hint: Any) -> List:
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

    @classmethod
    def is_derived(cls, obj: Any, clazz: Type) -> bool:
        if isinstance(obj, clazz):
            return True

        return any(
            base is not object and isinstance(obj, base) for base in clazz.__bases__
        )
