import sys
from collections import defaultdict
from dataclasses import Field
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
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type

from xsdata.exceptions import XmlContextError
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.typing import evaluate
from xsdata.models.enums import NamespaceType
from xsdata.utils.constants import EMPTY_SEQUENCE
from xsdata.utils.constants import return_input
from xsdata.utils.namespaces import build_qname


class XmlMetaBuilder:
    @classmethod
    def build(
        cls,
        clazz: Type,
        parent_ns: Optional[str],
        element_name_generator: Callable,
        attribute_name_generator: Callable,
    ) -> XmlMeta:
        """Build the binding metadata for a dataclass and its fields."""

        if not is_dataclass(clazz):
            raise XmlContextError(f"Type '{clazz}' is not a dataclass.")

        # Fetch the dataclass meta settings and make sure we don't inherit
        # the parent class meta.
        meta = clazz.Meta if "Meta" in clazz.__dict__ else None
        element_name_generator = getattr(
            meta, "element_name_generator", element_name_generator
        )
        attribute_name_generator = getattr(
            meta, "attribute_name_generator", attribute_name_generator
        )
        local_name = getattr(meta, "name", None)
        local_name = local_name or element_name_generator(clazz.__name__)
        nillable = getattr(meta, "nillable", False)
        namespace = getattr(meta, "namespace", parent_ns)
        module = sys.modules[clazz.__module__]
        source_namespace = getattr(module, "__NAMESPACE__", None)
        class_vars = cls.build_vars(
            clazz, namespace, element_name_generator, attribute_name_generator
        )

        attributes = {}
        elements: Dict[str, List[XmlVar]] = defaultdict(list)
        choices = []
        any_attributes = []
        wildcards = []
        text = None

        for var in class_vars:
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
            qname=build_qname(namespace, local_name),
            source_qname=build_qname(source_namespace, local_name),
            nillable=nillable,
            text=text,
            attributes=attributes,
            elements=elements,
            choices=choices,
            any_attributes=any_attributes,
            wildcards=wildcards,
        )

    @classmethod
    def build_vars(
        cls,
        clazz: Type,
        parent_ns: Optional[str],
        element_name_generator: Callable,
        attribute_name_generator: Callable,
    ):
        """Build the binding metadata for the given dataclass fields."""
        type_hints = get_type_hints(clazz)
        globalns = sys.modules[clazz.__module__].__dict__
        builder = XmlVarBuilder(
            default_xml_type=cls.default_xml_type(clazz),
            parent_ns=parent_ns,
            element_name_generator=element_name_generator,
            attribute_name_generator=attribute_name_generator,
        )

        for index, _field in enumerate(fields(clazz)):
            var = builder.build(
                index,
                _field.name,
                type_hints[_field.name],
                _field.metadata,
                _field.init,
                cls.default_field_value(_field),
                globalns,
            )
            if var is not None:
                yield var

    @classmethod
    def build_source_qname(cls, clazz: Type, element_name_generator: Callable) -> str:
        """Build the source qualified name of a model based on the module
        namespace."""
        meta = clazz.Meta if "Meta" in clazz.__dict__ else None
        local_name = getattr(meta, "name", None)
        element_name_generator = getattr(
            meta, "element_name_generator", element_name_generator
        )
        local_name = local_name or element_name_generator(clazz.__name__)
        module = sys.modules[clazz.__module__]
        source_namespace = getattr(module, "__NAMESPACE__", None)
        return build_qname(source_namespace, local_name)

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
    def default_field_value(cls, var: Field) -> Any:
        """Return the default value/factory for the given dataclass field."""

        if var.default_factory is not MISSING:  # type: ignore
            return var.default_factory  # type: ignore

        if var.default is not MISSING:
            return var.default

        return None


class XmlVarBuilder:

    __slots__ = (
        "default_xml_type",
        "parent_ns",
        "element_name_generator",
        "attribute_name_generator",
    )

    def __init__(
        self,
        default_xml_type: str,
        parent_ns: Optional[str] = None,
        element_name_generator: Callable = return_input,
        attribute_name_generator: Callable = return_input,
    ):
        self.default_xml_type = default_xml_type
        self.parent_ns = parent_ns
        self.element_name_generator = element_name_generator
        self.attribute_name_generator = attribute_name_generator

    def build(
        self,
        index: int,
        name: str,
        type_hint: Any,
        metadata: Mapping[str, Any],
        init: bool,
        default_value: Any,
        globalns: Any,
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
        nillable = metadata.get("nillable", False)
        format_str = metadata.get("format", None)
        sequential = metadata.get("sequential", False)

        origin, sub_origin, types = self.analyze_types(type_hint, globalns)

        if not self.is_valid(xml_type, origin, sub_origin, types, tokens, init):
            raise XmlContextError(
                f"Xml type '{xml_type}' does not support typing: {type_hint}"
            )

        local_name = self.build_local_name(xml_type, local_name, name)
        element_list = self.is_element_list(origin, sub_origin, tokens)
        any_type = self.is_any_type(types, xml_type)
        namespaces = self.resolve_namespaces(xml_type, namespace)
        default_namespace = self.default_namespace(namespaces)
        qname = build_qname(default_namespace, local_name)

        elements = {}
        wildcards = []
        for choice in self.build_choices(name, choices, globalns):
            if choice.is_element:
                elements[choice.qname] = choice
            else:  # choice.is_wildcard:
                wildcards.append(choice)

        return XmlVar(
            index=index + 1,
            name=name,
            qname=qname,
            init=init,
            mixed=mixed,
            format=format_str,
            tokens=tokens,
            any_type=any_type,
            nillable=nillable,
            sequential=sequential,
            list_element=element_list,
            default=default_value,
            types=types,
            elements=elements,
            wildcards=wildcards,
            namespaces=namespaces,
            xml_type=xml_type,
            derived=False,
        )

    def build_choices(
        self, name: str, choices: List[Dict], globalns: Any
    ) -> Iterator[XmlVar]:
        """Build the binding metadata for a compound dataclass field."""
        existing_types: Set[type] = set()

        for index, choice in enumerate(choices):
            default_value = choice.get("default_factory", choice.get("default"))

            metadata = choice.copy()
            metadata["name"] = choice.get("name", "any")
            type_hint = metadata["type"]

            if choice.get("wildcard"):
                metadata["type"] = XmlType.WILDCARD
            else:
                metadata["type"] = XmlType.ELEMENT

            var = self.build(
                index, name, type_hint, metadata, True, default_value, globalns
            )

            # It's impossible for choice elements to be ignorable, read above!
            assert var is not None

            var.list_element = True

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

    def resolve_namespaces(
        self,
        xml_type: Optional[str],
        namespace: Optional[str],
    ) -> Tuple[str, ...]:
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
            namespace = self.parent_ns

        if not namespace:
            return ()

        result = set()
        for ns in namespace.split():
            if ns == NamespaceType.TARGET_NS:
                result.add(self.parent_ns or NamespaceType.ANY_NS)
            elif ns == NamespaceType.LOCAL_NS:
                result.add("")
            elif ns == NamespaceType.OTHER_NS:
                result.add(f"!{self.parent_ns or ''}")
            else:
                result.add(ns)

        return tuple(result)

    @classmethod
    def default_namespace(cls, namespaces: Sequence[str]) -> Optional[str]:
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
    def is_element_list(cls, origin: Any, sub_origin: Any, is_tokens: bool) -> bool:
        """
        Return whether the field is a list element.

        If the field is derived from xs:NMTOKENS both origins have to be
        lists.
        """
        if origin is list:
            return not is_tokens or sub_origin is list

        return False

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

        The only case we support a sub origin is for fields derived from xs:NMTOKENS!


        :raises XmlContextError: if the typing is not supported for binding
        """
        try:
            types = evaluate(type_hint, globalns)
            origin = None
            sub_origin = None

            while types[0] in (list, dict):
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

    @classmethod
    def is_valid(
        cls,
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
        elif origin is dict or tokens and origin is not list:
            # Origin dict is only supported by Attributes
            # xs:NMTOKENS need origin list
            return False

        if object in types:
            # Any type, secondary types are not allowed
            return len(types) == 1

        return cls.is_typing_supported(types)

    @classmethod
    def is_typing_supported(cls, types: Sequence[Type]) -> bool:
        # Validate all types are registered in the converter.
        for tp in types:
            if (
                not is_dataclass(tp)
                and tp not in converter.registry
                and not issubclass(tp, Enum)
            ):
                return False

        return True
