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
from typing import List
from typing import Mapping
from typing import Optional
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
        # Ensure the given type is a dataclass.
        if not is_dataclass(clazz):
            raise XmlContextError(f"Object {clazz} is not a dataclass.")

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

        return XmlMeta(
            clazz=clazz,
            qname=build_qname(namespace, local_name),
            source_qname=build_qname(source_namespace, local_name),
            nillable=nillable,
            vars=list(class_vars),
        )

    @classmethod
    def build_vars(
        cls,
        clazz: Type,
        parent_ns: Optional[str],
        element_name_generator: Callable,
        attribute_name_generator: Callable,
    ):

        type_hints = get_type_hints(clazz)
        globalns = sys.modules[clazz.__module__].__dict__
        builder = XmlVarBuilder(
            default_xml_type=cls.default_xml_type(clazz),
            parent_ns=parent_ns,
            element_name_generator=element_name_generator,
            attribute_name_generator=attribute_name_generator,
        )

        for var in fields(clazz):
            yield builder.build(
                var.name,
                type_hints[var.name],
                var.metadata,
                var.init,
                cls.default_field_value(var),
                globalns,
            )

    @classmethod
    def build_source_qname(cls, clazz: Type, element_name_generator: Callable) -> str:
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
    def default_field_value(cls, var: Field) -> Any:
        """Return the default value/factory for the given dataclass field."""

        if var.default_factory is not MISSING:  # type: ignore
            return var.default_factory  # type: ignore

        if var.default is not MISSING:
            return var.default

        return None


@dataclass
class XmlVarBuilder:
    default_xml_type: str
    parent_ns: Optional[str] = None
    element_name_generator: Callable = field(default=return_input)
    attribute_name_generator: Callable = field(default=return_input)

    def build(
        self,
        name: str,
        type_hint: Any,
        metadata: Mapping[str, Any],
        init: bool,
        default_value: Any,
        globalns: Any,
    ) -> XmlVar:
        tokens = metadata.get("tokens", False)
        xml_type = metadata.get("type")
        local_name = metadata.get("name")
        namespace = metadata.get("namespace")
        choices = metadata.get("choices", EMPTY_SEQUENCE)
        mixed = metadata.get("mixed", False)
        nillable = metadata.get("nillable", False)
        format_str = metadata.get("format", None)
        sequential = metadata.get("sequential", False)

        origin, factory, types = self.analyze_types(evaluate(type_hint, globalns))
        is_class = self.is_class(types)
        xml_type = self.build_xml_type(xml_type, is_class)
        local_name = self.build_local_name(xml_type, local_name, name)
        element_list = self.is_element_list(origin, factory, tokens)
        any_type = self.is_any_type(types, xml_type)
        namespaces = self.resolve_namespaces(xml_type, namespace)
        default_namespace = self.default_namespace(namespaces)
        choice_vars = self.build_choices(name, choices, globalns)
        qname = build_qname(default_namespace, local_name)

        (
            element,
            elements,
            attribute,
            attributes,
            wildcard,
            text,
        ) = self.get_xml_attributes(xml_type)

        return XmlVar(
            name=name,
            qname=qname,
            init=init,
            mixed=mixed,
            format=format_str,
            tokens=tokens,
            any_type=any_type,
            nillable=nillable,
            dataclass=is_class,
            sequential=sequential,
            list_element=element_list,
            default=default_value,
            types=list(types),
            choices=choice_vars,
            namespaces=namespaces,
            element=element,
            elements=elements,
            attribute=attribute,
            attributes=attributes,
            wildcard=wildcard,
            text=text,
        )

    def build_choices(
        self, name: str, choices: List[Dict], globalns: Any
    ) -> List[XmlVar]:
        existing_types = set()

        result = []
        for choice in choices:
            default_value = choice.get("default_factory", choice.get("default"))

            metadata = choice.copy()
            metadata["name"] = choice.get("name", "any")
            type_hint = metadata["type"]

            if choice.get("wildcard"):
                metadata["type"] = XmlType.WILDCARD
            else:
                metadata["type"] = XmlType.ELEMENT

            var = self.build(name, type_hint, metadata, True, default_value, globalns)
            var.list_element = False

            if var.any_type or any(True for tp in var.types if tp in existing_types):
                var.derived = True

            existing_types.update(var.types)
            result.append(var)

        return result

    @classmethod
    def analyze_types(cls, types: Tuple[Type, ...]) -> Tuple[Any, Any, List[Type]]:
        origin = None
        factory = None

        while types[0] in (list, dict):

            if origin is None:
                origin = types[0]
            elif factory is None:
                factory = types[0]
            else:
                raise XmlContextError("Unsupported typing")

            types = types[1:]

        return origin, factory, converter.sort_types(list(types))

    def build_local_name(
        self, xml_type: str, local_name: Optional[str], name: str
    ) -> str:
        if not local_name:
            if xml_type == XmlType.ATTRIBUTE:
                return self.attribute_name_generator(name)

            return self.element_name_generator(name)

        return local_name

    def build_xml_type(self, xml_type: Optional[str], is_class: bool) -> str:
        if not xml_type:
            xml_type = XmlType.ELEMENT if is_class else self.default_xml_type

        return xml_type

    @classmethod
    def is_class(cls, types: List[Type]) -> bool:
        return any(is_dataclass(clazz) for clazz in types)

    def resolve_namespaces(
        self,
        xml_type: Optional[str],
        namespace: Optional[str],
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
            namespace = self.parent_ns

        if not namespace:
            return []

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
    def is_element_list(cls, origin: Any, factory: Any, is_tokens: bool) -> bool:
        if origin is list:
            return not is_tokens or factory is list

        return False

    @classmethod
    def is_any_type(cls, types: List[Type], xml_type: str) -> bool:
        if xml_type in (XmlType.ELEMENT, XmlType.ELEMENTS):
            return object in types

        return False

    @classmethod
    def get_xml_attributes(cls, xml_type: str) -> Tuple[bool, ...]:
        element = elements = attribute = attributes = wildcard = text = False

        if xml_type == XmlType.ELEMENT:
            element = True
        elif xml_type == XmlType.ELEMENTS:
            elements = True
        elif xml_type == XmlType.ATTRIBUTE:
            attribute = True
        elif xml_type == XmlType.ATTRIBUTES:
            attributes = True
        elif xml_type == XmlType.WILDCARD:
            wildcard = True
        else:
            text = True

        return element, elements, attribute, attributes, wildcard, text
