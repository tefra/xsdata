import sys
from collections import defaultdict
from dataclasses import dataclass
from dataclasses import Field
from dataclasses import field
from dataclasses import fields
from dataclasses import is_dataclass
from dataclasses import MISSING
from typing import _eval_type  # type: ignore
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
from xsdata.models.enums import DataType
from xsdata.models.enums import NamespaceType
from xsdata.utils.constants import EMPTY_SEQUENCE
from xsdata.utils.namespaces import build_qname


@dataclass
class XmlContext:
    """
    Generate and cache the necessary metadata to bind an xml document data to a
    dataclass model.

    :param element_name: Default callable to convert field names to element tags
    :param attribute_name: Default callable to convert field names to attribute tags
    :param cache: Cache models metadata
    :param xsi_cache: Index models by xsi:type
    """

    element_name: Callable = field(default=lambda x: x)
    attribute_name: Callable = field(default=lambda x: x)
    cache: Dict[Type, XmlMeta] = field(default_factory=dict)
    xsi_cache: Dict[str, List[Type]] = field(default_factory=lambda: defaultdict(list))
    sys_modules: int = field(default=0, init=False)

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
        subclass = None
        if xsi_type and meta.source_qname != xsi_type:
            subclass = self.find_subclass(clazz, xsi_type)

        return self.build(subclass, parent_ns) if subclass else meta

    def build_xsi_cache(self):
        """Index all imported dataclasses by their xsi:type qualified name."""
        self.xsi_cache.clear()

        for clazz in self.get_subclasses(object):
            if is_dataclass(clazz):
                meta = clazz.Meta if "Meta" in clazz.__dict__ else None
                name = getattr(meta, "name", None) or self.local_name(clazz.__name__)
                module = sys.modules[clazz.__module__]
                source_namespace = getattr(module, "__NAMESPACE__", None)
                source_qname = build_qname(source_namespace, name)
                self.xsi_cache[source_qname].append(clazz)

    def find_types(self, qname: str) -> Optional[List[Type]]:
        """
        Find all classes that match the given xsi:type qname.

        - Ignores native schema types, xs:string, xs:float, xs:int, ...
        - Rebuild cache if new modules were imported since last run
        """
        if DataType.from_qname(qname):
            return None

        if len(sys.modules) != self.sys_modules:
            self.build_xsi_cache()
            self.sys_modules = len(sys.modules)

        return self.xsi_cache[qname] if qname in self.xsi_cache else None

    def find_type(self, qname: str) -> Optional[Type]:
        """Return the most recently imported class that matches the given
        xsi:type qname."""
        types = self.find_types(qname)
        return types[-1] if types else None

    def find_subclass(self, clazz: Type, qname: str) -> Optional[Type]:
        """Compare all classes that match the given xsi:type qname and return
        the first one that is either a subclass or shares the same parent class
        as the original class."""

        types = self.find_types(qname)
        if types:
            for tp in types:
                for tp_mro in tp.__mro__:
                    if tp_mro is not object and tp_mro in clazz.__mro__:
                        return tp

        return None

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
            default_namespace = self.default_namespace(namespaces)
            qname = build_qname(default_namespace, local_name)

            choices = list(
                self.build_choices(
                    clazz,
                    var.name,
                    parent_ns,
                    var.metadata.get("choices", EMPTY_SEQUENCE),
                )
            )

            yield xml_clazz(
                name=var.name,
                qname=qname,
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
                choices=choices,
            )

    def build_choices(
        self,
        clazz: Type,
        parent_name: str,
        parent_namespace: Optional[str],
        choices: List[Dict],
    ):
        existing = set()
        globalns = sys.modules[clazz.__module__].__dict__
        for choice in choices:
            xml_type = XmlType.WILDCARD if choice.get("wildcard") else XmlType.ELEMENT
            namespace = choice.get("namespace")
            namespaces = self.resolve_namespaces(xml_type, namespace, parent_namespace)
            default_namespace = self.default_namespace(namespaces)

            types = self.real_types(_eval_type(choice["type"], globalns, None))
            derived = any(True for tp in types if tp in existing)
            is_class = any(is_dataclass(clazz) for clazz in types)
            xml_clazz = XmlType.to_xml_class(xml_type)
            qname = build_qname(default_namespace, choice.get("name", "any"))
            nillable = choice.get("nillable", False)

            if xml_type == XmlType.ELEMENT and len(types) == 1 and types[0] == object:
                derived = True

            yield xml_clazz(
                name=parent_name,
                qname=qname,
                namespaces=namespaces,
                nillable=nillable,
                dataclass=is_class,
                tokens=choice.get("tokens", False),
                derived=derived or nillable,
                types=types,
            )
            existing.update(types)

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
    def default_namespace(cls, namespaces: List[str]) -> Optional[str]:
        """Return the first valid namespace uri or None."""
        for namespace in namespaces:
            if namespace and not namespace.startswith("#"):
                return namespace

        return None

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

            types = [x for x in type_hint.__args__ if x is not None.__class__]
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

        return any(x is not object and isinstance(obj, x) for x in clazz.__bases__)

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

    @classmethod
    def get_subclasses(cls, clazz: Type):
        if clazz is not type:
            for subclass in clazz.__subclasses__():
                yield from cls.get_subclasses(subclass)
                yield subclass

    def local_name(self, name: str, xml_type: Optional[str] = None) -> str:
        if xml_type == "Attribute":
            return self.attribute_name(name)

        return self.element_name(name)
