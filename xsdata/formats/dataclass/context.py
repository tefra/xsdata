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
from typing import Set
from typing import Type
from typing import TypeVar

from xsdata.exceptions import XmlContextError
from xsdata.formats.bindings import T
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.models.enums import DataType
from xsdata.models.enums import NamespaceType
from xsdata.utils.constants import EMPTY_SEQUENCE
from xsdata.utils.constants import return_input
from xsdata.utils.namespaces import build_qname


@dataclass
class XmlContext:
    """
    The service provider for binding operations metadata.

    :param element_name_generator: Default element name generator
    :param attribute_name_generator: Default attribute name generator
    :ivar cache: Cache models metadata
    :ivar xsi_cache: Index models by xsi:type
    :ivar sys_modules: Number of imported modules
    """

    element_name_generator: Callable = field(default=return_input)
    attribute_name_generator: Callable = field(default=return_input)
    cache: Dict[Type, XmlMeta] = field(init=False, default_factory=dict)
    xsi_cache: Dict[str, List[Type]] = field(
        init=False, default_factory=lambda: defaultdict(list)
    )
    sys_modules: int = field(init=False, default_factory=int)

    def fetch(
        self,
        clazz: Type,
        parent_ns: Optional[str] = None,
        xsi_type: Optional[str] = None,
    ) -> XmlMeta:
        """
        Fetch the model metadata of the given dataclass type, namespace and xsi
        type.

        :param clazz: The requested dataclass type
        :param parent_ns: The inherited parent namespace
        :param xsi_type: if present it means that the given clazz is derived and the
            lookup procedure needs to check and match a dataclass model to the qualified
            name instead
        """
        meta = self.build(clazz, parent_ns)
        subclass = None
        if xsi_type and meta.source_qname != xsi_type:
            subclass = self.find_subclass(clazz, xsi_type)

        return self.build(subclass, parent_ns) if subclass else meta

    def build_xsi_cache(self):
        """Index all imported dataclasses by their xsi:type qualified name."""

        if len(sys.modules) == self.sys_modules:
            return

        self.xsi_cache.clear()

        for clazz in self.get_subclasses(object):
            if is_dataclass(clazz):
                meta = clazz.Meta if "Meta" in clazz.__dict__ else None
                local_name = getattr(meta, "name", None)
                element_name_generator = getattr(
                    meta, "element_name_generator", self.element_name_generator
                )
                local_name = local_name or element_name_generator(clazz.__name__)
                module = sys.modules[clazz.__module__]
                source_namespace = getattr(module, "__NAMESPACE__", None)
                source_qname = build_qname(source_namespace, local_name)
                self.xsi_cache[source_qname].append(clazz)

        self.sys_modules = len(sys.modules)

    def find_types(self, qname: str) -> List[Type[T]]:
        """
        Find all classes that match the given xsi:type qname.

        - Ignores native schema types, xs:string, xs:float, xs:int, ...
        - Rebuild cache if new modules were imported since last run

        :param qname: Qualified name
        """
        if not DataType.from_qname(qname):
            self.build_xsi_cache()
            if qname in self.xsi_cache:
                return self.xsi_cache[qname]

        return []

    def find_type(self, qname: str) -> Optional[Type[T]]:
        """
        Return the most recently imported class that matches the given xsi:type
        qname.

        :param qname: Qualified name
        """
        types: List[Type] = self.find_types(qname)
        return types[-1] if types else None

    def find_type_by_fields(self, field_names: Set) -> Optional[Type[T]]:
        """
        Find a dataclass from all the imported modules that matches the given
        list of field names.

        :param field_names: A unique list of field names
        """

        self.build_xsi_cache()
        for types in self.xsi_cache.values():
            for clazz in types:
                if field_names == {attr.name for attr in fields(clazz)}:
                    return clazz

        return None

    def find_subclass(self, clazz: Type, qname: str) -> Optional[Type]:
        """
        Compare all classes that match the given xsi:type qname and return the
        first one that is either a subclass or shares the same parent class as
        the original class.

        :param clazz: The search dataclass type
        :param qname: Qualified name
        """

        types: List[Type] = self.find_types(qname)
        for tp in types:
            for tp_mro in tp.__mro__:
                if tp_mro is not object and tp_mro in clazz.__mro__:
                    return tp

        return None

    def build(self, clazz: Type, parent_ns: Optional[str] = None) -> XmlMeta:
        """
        Fetch from cache or build the binding metadata for the given class and
        parent namespace.

        :param clazz: A dataclass type
        :param parent_ns: The inherited parent namespace
        """

        if clazz not in self.cache:

            # Ensure the given type is a dataclass.
            if not is_dataclass(clazz):
                raise XmlContextError(f"Object {clazz} is not a dataclass.")

            # Fetch the dataclass meta settings and make sure we don't inherit
            # the parent class meta.
            meta = clazz.Meta if "Meta" in clazz.__dict__ else None
            element_name_generator = getattr(
                meta, "element_name_generator", self.element_name_generator
            )
            attribute_name_generator = getattr(
                meta, "attribute_name_generator", self.attribute_name_generator
            )
            local_name = getattr(meta, "name", None)
            local_name = local_name or element_name_generator(clazz.__name__)
            nillable = getattr(meta, "nillable", False)
            namespace = getattr(meta, "namespace", parent_ns)
            module = sys.modules[clazz.__module__]
            source_namespace = getattr(module, "__NAMESPACE__", None)

            self.cache[clazz] = XmlMeta(
                clazz=clazz,
                qname=build_qname(namespace, local_name),
                source_qname=build_qname(source_namespace, local_name),
                nillable=nillable,
                vars=list(
                    self.get_type_hints(
                        clazz,
                        namespace,
                        element_name_generator,
                        attribute_name_generator,
                    )
                ),
            )
        return self.cache[clazz]

    def get_type_hints(
        self,
        clazz: Type,
        parent_ns: Optional[str],
        element_name_generator: Callable,
        attribute_name_generator: Callable,
    ) -> Iterator[XmlVar]:
        """
        Build the model fields binding metadata.

        :param clazz: The requested dataclass type
        :param parent_ns: The inherited parent namespace
        """
        type_hints = get_type_hints(clazz)
        default_xml_type = self.default_xml_type(clazz)

        for var in fields(clazz):
            tokens = var.metadata.get("tokens", False)
            xml_type = var.metadata.get("type")
            local_name = var.metadata.get("name")
            namespace = var.metadata.get("namespace")
            choices = var.metadata.get("choices", EMPTY_SEQUENCE)
            mixed = var.metadata.get("mixed", False)
            nillable = var.metadata.get("nillable", False)
            format_str = var.metadata.get("format", None)
            sequential = var.metadata.get("sequential", False)

            type_hint = type_hints[var.name]
            types = self.real_types(type_hint)
            any_type = object in types
            element_list = self.is_element_list(type_hint, tokens)
            is_class = any(is_dataclass(clazz) for clazz in types)
            xml_type = xml_type or (XmlType.ELEMENT if is_class else default_xml_type)

            if not local_name:
                if xml_type == XmlType.ATTRIBUTE:
                    local_name = attribute_name_generator(var.name)
                else:
                    local_name = element_name_generator(var.name)

            namespaces = self.resolve_namespaces(xml_type, namespace, parent_ns)
            default_namespace = self.default_namespace(namespaces)
            choice_vars = list(self.build_choices(clazz, var.name, parent_ns, choices))
            qname = build_qname(default_namespace, local_name)
            default_value = self.default_value(var)

            yield XmlVar(
                xml_type=xml_type,
                name=var.name,
                qname=qname,
                init=var.init,
                mixed=mixed,
                format=format_str,
                tokens=tokens,
                any_type=any_type,
                nillable=nillable,
                dataclass=is_class,
                sequential=sequential,
                list_element=element_list,
                default=default_value,
                types=types,
                choices=choice_vars,
                namespaces=namespaces,
            )

    def build_choices(
        self,
        clazz: Type,
        parent_name: str,
        parent_namespace: Optional[str],
        choices: List[Dict],
    ):
        existing_types = set()
        globalns = sys.modules[clazz.__module__].__dict__
        for choice in choices:
            xml_type = XmlType.WILDCARD if choice.get("wildcard") else XmlType.ELEMENT
            namespace = choice.get("namespace")
            tokens = choice.get("tokens", False)
            nillable = choice.get("nillable", False)
            format_str = choice.get("format", None)
            default_value = choice.get("default_factory", choice.get("default"))

            types = self.real_types(_eval_type(choice["type"], globalns, None))
            is_class = any(is_dataclass(clazz) for clazz in types)
            any_type = xml_type == XmlType.ELEMENT and object in types
            derived = any(True for tp in types if tp in existing_types) or any_type

            namespaces = self.resolve_namespaces(xml_type, namespace, parent_namespace)
            default_namespace = self.default_namespace(namespaces)
            qname = build_qname(default_namespace, choice.get("name", "any"))

            existing_types.update(types)

            yield XmlVar(
                xml_type=xml_type,
                name=parent_name,
                qname=qname,
                tokens=tokens,
                format=format_str,
                derived=derived,
                any_type=any_type,
                nillable=nillable,
                dataclass=is_class,
                default=default_value,
                types=types,
                namespaces=namespaces,
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


        :param xml_type: The xml type (Text|Element(s)|Attribute(s)|Wildcard)
        :param namespace: The field namespace
        :param parent_namespace: The parent namespace
        """
        if xml_type in (XmlType.ELEMENT, XmlType.WILDCARD) and namespace is None:
            namespace = parent_namespace

        if not namespace:
            return []

        result = set()
        for ns in namespace.split():
            if ns == NamespaceType.TARGET_NS:
                result.add(parent_namespace or NamespaceType.ANY_NS)
            elif ns == NamespaceType.LOCAL_NS:
                result.add("")
            elif ns == NamespaceType.OTHER_NS:
                result.add(f"!{parent_namespace or ''}")
            else:
                result.add(ns)
        return list(result)

    @classmethod
    def default_namespace(cls, namespaces: List[str]) -> Optional[str]:
        """
        Return the first valid namespace uri or None.

        :param namespaces: A list of namespace options which may
            include valid uri(s) or one of the ##any, ##other,
            ##targetNamespace, ##local
        """
        for namespace in namespaces:
            if namespace and not namespace.startswith("#"):
                return namespace

        return None

    @classmethod
    def default_value(cls, var: Field) -> Any:
        """Return the default value/factory for the given dataclass field."""

        if var.default_factory is not MISSING:  # type: ignore
            return var.default_factory  # type: ignore

        if var.default is not MISSING:
            return var.default

        return None

    @classmethod
    def real_types(cls, type_hint: Any) -> List:
        """
        Return a list of real types that can be used to bind or cast data.

        :param type_hint: A typing declaration
        """
        type_vars = []
        if type_hint is Dict:
            type_vars.append(type_hint)
        elif hasattr(type_hint, "__origin__"):
            while len(type_hint.__args__) == 1 and hasattr(
                type_hint.__args__[0], "__origin__"
            ):
                type_hint = type_hint.__args__[0]

            type_vars = [x for x in type_hint.__args__ if x is not None.__class__]
        else:
            type_vars.append(type_hint)

        types = []
        for type_var in type_vars:
            if isinstance(type_var, TypeVar):
                if type_var.__bound__:
                    types.append(type_var.__bound__)
                else:
                    types.extend(type_var.__constraints__)
            else:
                types.append(type_var)

        return converter.sort_types(types)

    @classmethod
    def is_derived(cls, obj: Any, clazz: Type) -> bool:
        """
        Return whether the given obj is derived from the given dataclass type.

        :param obj: A dataclass instance
        :param clazz: A dataclass type
        """

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
        """
        Return the default xml type for the fields of the given dataclass with
        an undefined type.

        :param clazz: A dataclass type
        """
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
        try:
            for subclass in clazz.__subclasses__():
                yield from cls.get_subclasses(subclass)
                yield subclass
        except TypeError:
            pass
