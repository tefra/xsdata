import sys
from collections import defaultdict
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

from xsdata.exceptions import XmlContextError
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.models.enums import NamespaceType
from xsdata.utils.namespaces import build_qname


@dataclass
class XmlContext:
    """
    Generate and cache the necessary metadata to bind an xml document data to a
    dataclass model.

    :param element_name: Default callable to convert field names to element tags
    :param attribute_name: Default callable to convert field names to attribute tags
    :param cache: Local storage to store and reuse models' bind metadata.
    """

    element_name: Callable = field(default=lambda x: x)
    attribute_name: Callable = field(default=lambda x: x)
    cache: Dict[Type, XmlMeta] = field(default_factory=dict)

    def fetch(
        self,
        clazz: Type,
        parent_ns: Optional[str] = None,
        xsi_type: Optional[str] = None,
    ) -> XmlMeta:
        """
        Fetch the model metadata of the given dataclass type, namespace and xsi
        type.

        :param clazz: A dataclass model
        :param parent_ns: The parent dataclass namespace if present.
        :param xsi_type: if present it means that the given clazz is derived and the
            lookup procedure needs to check and match a dataclass model to the qualified
            name instead.
        """
        meta = self.build(clazz, parent_ns)

        subclass = self.find_subclass(clazz, xsi_type) if xsi_type else None
        if subclass:
            meta = self.build(subclass, parent_ns)

        return meta

    def find_subclass(self, clazz: Type, xsi_type: str) -> Optional[Type]:
        """
        Find a derived class of the given clazz that matches the given
        qualified xsi type.

        The derived class is either a subclass or shares the same parent
        class as the given class.
        """
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

    def match_class_source_qname(self, clazz: Type, xsi_type: str) -> bool:
        """Match a given source qualified name with the given xsi type."""
        if is_dataclass(clazz):
            meta = self.build(clazz)
            return meta.source_qname == xsi_type

        return False

    def build(self, clazz: Type, parent_ns: Optional[str] = None) -> XmlMeta:
        """Fetch from cache or build the metadata object for the given class
        and parent namespace."""

        if clazz not in self.cache:

            # Ensure the given type is a dataclass.
            if not is_dataclass(clazz):
                raise XmlContextError(f"Object {clazz} is not a dataclass.")

            # Fetch the dataclass meta settings and make sure we don't inherit
            # the parent class meta.
            meta = clazz.Meta if "Meta" in clazz.__dict__ else None
            name = getattr(meta, "name", None) or self.local_name(clazz.__name__)
            nillable = getattr(meta, "nillable", False)
            namespace = getattr(meta, "namespace", parent_ns)
            module = sys.modules[clazz.__module__]
            source_namespace = getattr(module, "__NAMESPACE__", None)

            self.cache[clazz] = XmlMeta(
                name=name,
                clazz=clazz,
                qname=build_qname(namespace, name),
                source_qname=build_qname(source_namespace, name),
                nillable=nillable,
                vars=list(self.get_type_hints(clazz, namespace)),
            )
        return self.cache[clazz]

    def get_type_hints(self, clazz: Type, parent_ns: Optional[str]) -> Iterator[XmlVar]:
        """Build the model class fields metadata."""
        type_hints = get_type_hints(clazz)
        default_xml_type = self.default_xml_type(clazz)

        for var in fields(clazz):
            type_hint = type_hints[var.name]
            types = self.real_types(type_hint)
            is_tokens = var.metadata.get("tokens", False)
            is_element_list = self.is_element_list(type_hint, is_tokens)
            is_class = any(is_dataclass(clazz) for clazz in types)
            xml_type = var.metadata.get("type")
            local_name = var.metadata.get("name")

            if not xml_type:
                xml_type = default_xml_type if not is_class else "Element"

            if not local_name:
                local_name = self.local_name(var.name, xml_type)

            xml_clazz = XmlType.to_xml_class(xml_type)
            namespace = var.metadata.get("namespace")
            namespaces = self.resolve_namespaces(xml_type, namespace, parent_ns)
            first_namespace = next((x for x in namespaces if x and x[0] != "#"), None)

            yield xml_clazz(
                name=var.name,
                qname=build_qname(first_namespace, local_name),
                namespaces=namespaces,
                init=var.init,
                mixed=var.metadata.get("mixed", False),
                nillable=var.metadata.get("nillable", False),
                dataclass=is_class,
                sequential=var.metadata.get("sequential", False),
                tokens=is_tokens,
                list_element=is_element_list,
                types=types,
                default=self.default_value(var),
            )

    @classmethod
    def resolve_namespaces(
        cls,
        xml_type: Optional[str],
        namespace: Optional[str],
        parent_namespace: Optional[str],
    ) -> List[str]:
        """
        Resolve the namespace(s) for the given xml type and the parent
        namespace.

        Only elements and wildcards are allowed to inherit the parent namespace if
        the given namespace is empty.

        In case of wildcard try to decode the ##any, ##other, ##local, ##target.
        """
        if xml_type in (XmlType.ELEMENT, XmlType.WILDCARD) and namespace is None:
            namespace = parent_namespace

        if not namespace:
            return []

        result = set()
        for ns in namespace.split():
            if ns == NamespaceType.TARGET:
                result.add(parent_namespace or NamespaceType.ANY)
            elif ns == NamespaceType.LOCAL:
                result.add("")
            elif ns == NamespaceType.OTHER:
                result.add(f"!{parent_namespace or ''}")
            else:
                result.add(ns)
        return list(result)

    @classmethod
    def default_value(cls, var: Field) -> Any:
        """Return the default value/factory for the given field."""

        if var.default_factory is not MISSING:  # type: ignore
            return var.default_factory  # type: ignore

        if var.default is not MISSING:
            return var.default

        return None

    @classmethod
    def real_types(cls, type_hint: Any) -> List:
        """Return a list of real types that can be used to bind or cast
        data."""
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

        return converter.sort_types(types)

    @classmethod
    def is_derived(cls, obj: Any, clazz: Type) -> bool:
        """Return whether the given obj is derived from the given dataclass
        type."""

        if obj is None:
            return False

        if isinstance(obj, clazz):
            return True

        return any(
            base is not object and isinstance(obj, base) for base in clazz.__bases__
        )

    @classmethod
    def is_element_list(cls, type_hint: Any, is_tokens: bool) -> bool:
        if getattr(type_hint, "__origin__", None) in (list, List):
            if not is_tokens:
                return True

            type_hint = type_hint.__args__[0]
            if getattr(type_hint, "__origin__", None) in (list, List):
                return True

        return False

    @classmethod
    def default_xml_type(cls, clazz: Type) -> str:
        """Return the default xml type for the fields of the given dataclass
        with an undefined type."""
        counters: Dict[str, int] = defaultdict(int)
        for var in fields(clazz):
            xml_type = var.metadata.get("type")
            counters[xml_type or "undefined"] += 1

        if counters[XmlType.TEXT] > 1:
            raise XmlContextError(
                f"Dataclass `{clazz.__name__}` includes more than one text node!"
            )

        if counters["undefined"] == 1 and counters[XmlType.TEXT] == 0:
            return XmlType.TEXT

        return XmlType.ELEMENT

    def local_name(self, name: str, xml_type: Optional[str] = None) -> str:
        if xml_type == "Attribute":
            return self.attribute_name(name)

        return self.element_name(name)
