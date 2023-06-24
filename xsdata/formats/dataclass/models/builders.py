import sys
from collections import defaultdict
from enum import Enum
from typing import Any
from typing import Callable
from typing import Dict
from typing import get_type_hints
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NamedTuple
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type

from xsdata.exceptions import XmlContextError
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.compat import ClassType
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.typing import evaluate
from xsdata.models.enums import NamespaceType
from xsdata.utils.collections import first
from xsdata.utils.constants import EMPTY_SEQUENCE
from xsdata.utils.constants import return_input
from xsdata.utils.namespaces import build_qname


class ClassMeta(NamedTuple):
    element_name_generator: Callable
    attribute_name_generator: Callable
    qname: str
    local_name: str
    nillable: bool
    namespace: Optional[str]
    target_qname: Optional[str]


class XmlMetaBuilder:
    __slots__ = (
        "class_type",
        "element_name_generator",
        "attribute_name_generator",
        "globalns",
    )

    def __init__(
        self,
        class_type: ClassType,
        element_name_generator: Callable,
        attribute_name_generator: Callable,
        globalns: Optional[Dict[str, Callable]] = None,
    ):
        self.class_type = class_type
        self.element_name_generator = element_name_generator
        self.attribute_name_generator = attribute_name_generator
        self.globalns = globalns

    def build(self, clazz: Type, parent_namespace: Optional[str]) -> XmlMeta:
        """Build the binding metadata for a dataclass and its fields."""
        self.class_type.verify_model(clazz)

        meta = self.build_class_meta(clazz, parent_namespace)
        class_vars = self.build_vars(
            clazz,
            meta.namespace,
            meta.element_name_generator,
            meta.attribute_name_generator,
        )

        attributes = {}
        elements: Dict[str, List[XmlVar]] = defaultdict(list)
        choices = []
        any_attributes = []
        wildcards = []
        wrappers: Dict[str, List[XmlVar]] = defaultdict(list)
        text = None

        for var in class_vars:
            if var.wrapper is not None:
                wrappers[var.wrapper].append(var)
            if var.is_attribute:
                attributes[var.qname] = var
            elif var.is_element:
                elements[var.qname].append(var)
            elif var.is_elements:
                choices.append(var)
            elif var.is_attributes:
                any_attributes.append(var)
            elif var.is_wildcard:
                wildcards.append(var)
            else:  # var.is_text
                text = var

        return XmlMeta(
            clazz=clazz,
            qname=meta.qname,
            target_qname=meta.target_qname,
            nillable=meta.nillable,
            text=text,
            attributes=attributes,
            elements=elements,
            choices=choices,
            any_attributes=any_attributes,
            wildcards=wildcards,
            wrappers=wrappers,
        )

    def build_vars(
        self,
        clazz: Type,
        namespace: Optional[str],
        element_name_generator: Callable,
        attribute_name_generator: Callable,
    ):
        """Build the binding metadata for the given dataclass fields."""
        type_hints = get_type_hints(clazz, globalns=self.globalns)
        builder = XmlVarBuilder(
            class_type=self.class_type,
            default_xml_type=self.default_xml_type(clazz),
            element_name_generator=element_name_generator,
            attribute_name_generator=attribute_name_generator,
        )

        for field in self.class_type.get_fields(clazz):
            real_clazz = self.find_declared_class(clazz, field.name)
            globalns = sys.modules[real_clazz.__module__].__dict__
            parent_namespace = namespace
            if real_clazz is not clazz and "Meta" in real_clazz.__dict__:
                parent_namespace = getattr(real_clazz.Meta, "namespace", namespace)

            var = builder.build(
                field.name,
                type_hints[field.name],
                field.metadata,
                field.init,
                parent_namespace,
                self.class_type.default_value(field),
                globalns,
            )
            if var is not None:
                yield var

    def build_class_meta(
        self, clazz: Type, parent_namespace: Optional[str] = None
    ) -> ClassMeta:
        """
        Fetch the class meta options and merge defaults.

        Metaclass is not inheritable
        """
        meta = clazz.Meta if "Meta" in clazz.__dict__ else None
        element_name_generator = getattr(
            meta, "element_name_generator", self.element_name_generator
        )
        attribute_name_generator = getattr(
            meta, "attribute_name_generator", self.attribute_name_generator
        )
        global_type = getattr(meta, "global_type", True)
        local_name = getattr(meta, "name", None)
        local_name = local_name or element_name_generator(clazz.__name__)
        nillable = getattr(meta, "nillable", False)
        namespace = getattr(meta, "namespace", parent_namespace)
        qname = build_qname(namespace, local_name)

        if self.is_inner_class(clazz) or not global_type:
            target_qname = None
        else:
            module = sys.modules[clazz.__module__]
            target_namespace = self.target_namespace(module, meta)
            target_qname = build_qname(target_namespace, local_name)

        return ClassMeta(
            element_name_generator,
            attribute_name_generator,
            qname,
            local_name,
            nillable,
            namespace,
            target_qname,
        )

    @classmethod
    def find_declared_class(cls, clazz: Type, name: str) -> Type:
        for base in clazz.__mro__:
            ann = base.__dict__.get("__annotations__")
            if ann and name in ann:
                return base

        raise XmlContextError(f"Failed to detect the declared class for field {name}")

    @classmethod
    def is_inner_class(cls, clazz: Type) -> bool:
        """Return whether the given type is nested inside another type."""
        return "." in clazz.__qualname__

    @classmethod
    def target_namespace(cls, module: Any, meta: Any) -> Optional[str]:
        """The target namespace this class metadata was defined in."""
        namespace = getattr(meta, "target_namespace", None)
        if namespace is not None:
            return namespace

        namespace = getattr(module, "__NAMESPACE__", None)
        if namespace is not None:
            return namespace

        return getattr(meta, "namespace", None)

    def default_xml_type(self, clazz: Type) -> str:
        """Return the default xml type for the fields of the given dataclass
        with an undefined type."""
        counters: Dict[str, int] = defaultdict(int)
        for var in self.class_type.get_fields(clazz):
            xml_type = var.metadata.get("type")
            counters[xml_type or "undefined"] += 1

        if counters[XmlType.TEXT] > 1:
            raise XmlContextError(
                f"Dataclass `{clazz.__name__}` includes more than one text node!"
            )

        if counters["undefined"] == 1 and counters[XmlType.TEXT] == 0:
            return XmlType.TEXT

        return XmlType.ELEMENT


class XmlVarBuilder:
    __slots__ = (
        "index",
        "class_type",
        "default_xml_type",
        "element_name_generator",
        "attribute_name_generator",
    )

    def __init__(
        self,
        class_type: ClassType,
        default_xml_type: str,
        element_name_generator: Callable = return_input,
        attribute_name_generator: Callable = return_input,
    ):
        self.index = 0
        self.class_type = class_type
        self.default_xml_type = default_xml_type
        self.element_name_generator = element_name_generator
        self.attribute_name_generator = attribute_name_generator

    def build(
        self,
        name: str,
        type_hint: Any,
        metadata: Mapping[str, Any],
        init: bool,
        parent_namespace: Optional[str],
        default_value: Any,
        globalns: Any,
        factory: Optional[Callable] = None,
    ) -> Optional[XmlVar]:
        """Build the binding metadata for a dataclass field."""
        xml_type = metadata.get("type", self.default_xml_type)
        if xml_type == XmlType.IGNORE:
            return None

        tokens = metadata.get("tokens", False)
        local_name = metadata.get("name")
        namespace = metadata.get("namespace")
        choices = metadata.get("choices", EMPTY_SEQUENCE)
        mixed = metadata.get("mixed", False)
        required = metadata.get("required", False)
        nillable = metadata.get("nillable", False)
        format_str = metadata.get("format", None)
        sequence = metadata.get("sequence", None)
        wrapper = metadata.get("wrapper", None)

        origin, sub_origin, types = self.analyze_types(type_hint, globalns)

        if not self.is_valid(xml_type, origin, sub_origin, types, tokens, init):
            raise XmlContextError(
                f"Xml type '{xml_type}' does not support typing: {type_hint}"
            )

        if wrapper is not None:
            if not isinstance(origin, type) or not issubclass(
                origin, (list, set, tuple)
            ):
                raise XmlContextError(
                    f"a wrapper requires a collection type on attribute {name}"
                )

        local_name = self.build_local_name(xml_type, local_name, name)

        if tokens and sub_origin is None:
            sub_origin = origin
            origin = None

        if origin is None:
            origin = factory

        any_type = self.is_any_type(types, xml_type)
        clazz = first(tp for tp in types if self.class_type.is_model(tp))
        namespaces = self.resolve_namespaces(xml_type, namespace, parent_namespace)
        default_namespace = self.default_namespace(namespaces)
        qname = build_qname(default_namespace, local_name)
        if wrapper is not None:
            wrapper = build_qname(default_namespace, wrapper)

        elements = {}
        wildcards = []
        self.index += 1
        cur_index = self.index
        for choice in self.build_choices(
            name, choices, origin, globalns, parent_namespace
        ):
            if choice.is_element:
                elements[choice.qname] = choice
            else:  # choice.is_wildcard:
                wildcards.append(choice)

        return XmlVar(
            index=cur_index,
            name=name,
            qname=qname,
            init=init,
            mixed=mixed,
            format=format_str,
            clazz=clazz,
            any_type=any_type,
            required=required,
            nillable=nillable,
            sequence=sequence,
            factory=origin,
            tokens_factory=sub_origin,
            default=default_value,
            types=types,
            elements=elements,
            wildcards=wildcards,
            namespaces=namespaces,
            xml_type=xml_type,
            derived=False,
            wrapper=wrapper,
        )

    def build_choices(
        self,
        name: str,
        choices: List[Dict],
        factory: Callable,
        globalns: Any,
        parent_namespace: Optional[str],
    ) -> Iterator[XmlVar]:
        """Build the binding metadata for a compound dataclass field."""
        existing_types: Set[type] = set()

        for choice in choices:
            default_value = self.class_type.default_choice_value(choice)

            metadata = choice.copy()
            metadata["name"] = choice.get("name", "any")
            type_hint = metadata["type"]

            if choice.get("wildcard"):
                metadata["type"] = XmlType.WILDCARD
            else:
                metadata["type"] = XmlType.ELEMENT

            var = self.build(
                name,
                type_hint,
                metadata,
                True,
                parent_namespace,
                default_value,
                globalns,
                factory,
            )

            # It's impossible for choice elements to be ignorable, read above!
            assert var is not None

            if var.any_type or any(True for tp in var.types if tp in existing_types):
                var.derived = True

            existing_types.update(var.types)

            yield var

    def build_local_name(
        self, xml_type: str, local_name: Optional[str], name: str
    ) -> str:
        """Build a local name based on the field name and xml type if it's not
        set."""
        if not local_name:
            if xml_type == XmlType.ATTRIBUTE:
                return self.attribute_name_generator(name)

            return self.element_name_generator(name)

        return local_name

    @classmethod
    def resolve_namespaces(
        cls,
        xml_type: Optional[str],
        namespace: Optional[str],
        parent_namespace: Optional[str],
    ) -> Tuple[str, ...]:
        """
        Resolve the namespace(s) for the given xml type and the parent
        namespace.

        Only elements and wildcards are allowed to inherit the parent
        namespace if the given namespace is empty.

        In case of wildcard try to decode the ##any, ##other, ##local,
        ##target.

        :param xml_type: The xml type
            (Text|Element(s)|Attribute(s)|Wildcard)
        :param namespace: The field namespace
        :param parent_namespace: The parent namespace
        """
        if xml_type in (XmlType.ELEMENT, XmlType.WILDCARD) and namespace is None:
            namespace = parent_namespace

        if not namespace:
            return ()

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

        return tuple(result)

    @classmethod
    def default_namespace(cls, namespaces: Sequence[str]) -> Optional[str]:
        """
        Return the first valid namespace uri or None.

        :param namespaces: A list of namespace options which may include
            valid uri(s) or one of the ##any, ##other,
            ##targetNamespace, ##local
        """
        for namespace in namespaces:
            if namespace and not namespace.startswith("#"):
                return namespace

        return None

    @classmethod
    def is_any_type(cls, types: Sequence[Type], xml_type: str) -> bool:
        """Return whether the given xml type supports derived values."""
        if xml_type in (XmlType.ELEMENT, XmlType.ELEMENTS):
            return object in types

        return False

    @classmethod
    def analyze_types(
        cls, type_hint: Any, globalns: Any
    ) -> Tuple[Any, Any, Tuple[Type, ...]]:
        """
        Analyze a type hint and return the origin, sub origin and the type
        args.

        The only case we support a sub origin is for fields derived from
        xs:NMTOKENS!

        :raises XmlContextError: if the typing is not supported for
            binding
        """
        try:
            types = evaluate(type_hint, globalns)
            origin = None
            sub_origin = None

            while types[0] in (tuple, list, dict):
                if origin is None:
                    origin = types[0]
                elif sub_origin is None:
                    sub_origin = types[0]
                else:
                    raise TypeError()

                types = types[1:]

            return origin, sub_origin, tuple(converter.sort_types(types))
        except Exception:
            raise XmlContextError(f"Unsupported typing: {type_hint}")

    def is_valid(
        self,
        xml_type: str,
        origin: Any,
        sub_origin: Any,
        types: Sequence[Type],
        tokens: bool,
        init: bool,
    ) -> bool:
        """Validate the given xml type against common unsupported cases."""

        if not init:
            # Ignore init==false vars
            return True

        if xml_type == XmlType.ATTRIBUTES:
            # Attributes need origin dict, no sub origin and tokens
            if origin is not dict or sub_origin or tokens:
                return False
        elif origin is dict or tokens and origin not in (list, tuple):
            # Origin dict is only supported by Attributes
            # xs:NMTOKENS need origin list
            return False

        if object in types:
            # Any type, secondary types are not allowed
            return len(types) == 1

        return self.is_typing_supported(types)

    def is_typing_supported(self, types: Sequence[Type]) -> bool:
        # Validate all types are registered in the converter.
        for tp in types:
            if (
                not self.class_type.is_model(tp)
                and tp not in converter.registry
                and not issubclass(tp, Enum)
            ):
                return False

        return True
