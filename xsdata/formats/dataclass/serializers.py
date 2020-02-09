import json
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from dataclasses import is_dataclass
from enum import Enum
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type

from lxml.etree import cleanup_namespaces
from lxml.etree import Element
from lxml.etree import QName
from lxml.etree import SubElement
from lxml.etree import tostring

from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.mixins import AbstractSerializer
from xsdata.models.enums import Namespace


def filter_none(x: Tuple):
    return dict((k, v) for k, v in x if v is not None)


class DictFactory:
    FILTER_NONE = filter_none


class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value

        return super(EnumEncoder, self).default(obj)


@dataclass
class DictSerializer(AbstractSerializer):
    dict_factory: Callable = field(default=dict)

    def render(self, obj: object) -> Dict:
        """Convert the given object tree to dictionary with primitive
        values."""
        return asdict(obj, dict_factory=self.dict_factory)


@dataclass
class JsonSerializer(AbstractSerializer):
    """
    :ivar dict_factory: Callable to generate dictionary
    :ivar encoder: Value encoder
    :ivar indent: Pretty print indent
    """

    dict_factory: Callable = field(default=dict)
    encoder: Type[json.JSONEncoder] = field(default=EnumEncoder)
    indent: Optional[int] = field(default=None)

    def render(self, obj: object) -> str:
        """Convert the given object tree to json string."""
        return json.dumps(
            asdict(obj, dict_factory=self.dict_factory),
            cls=self.encoder,
            indent=self.indent,
        )


@dataclass
class XmlSerializer(AbstractSerializer, ModelInspect):
    """
    :ivar xml_declaration: Add xml declaration
    :ivar encoding: Result text encoding
    :ivar pretty_print: Enable pretty output
    """

    xml_declaration: bool = field(default=True)
    encoding: str = field(default="UTF-8")
    pretty_print: bool = field(default=False)

    def render(self, obj: object) -> str:
        """Convert the given object tree to xml string."""
        tree = self.render_tree(obj)
        return tostring(
            tree,
            xml_declaration=self.xml_declaration,
            encoding=self.encoding,
            pretty_print=self.pretty_print,
        ).decode()

    def render_tree(self, obj: object, namespace: Optional[str] = None) -> Element:
        """
        Convert a dataclass instance to a nested Element structure.

        If the instance class is generated from the xsdata cli the root
        element's name will be auto assigned otherwise it will default
        to the class name.

        :raise TypeError: If the instance is not a dataclass
        """
        meta = self.class_meta(obj.__class__, namespace)

        namespaces = set()
        if meta.namespace:
            namespaces.add(meta.namespace)

        root = self.render_node(obj, Element(meta.qname), namespaces)
        nsmap = {f"ns{index}": ns for index, ns in enumerate(sorted(namespaces))}
        cleanup_namespaces(root, top_nsmap=nsmap)
        return root

    def render_node(self, obj, parent, namespaces) -> Element:
        """Recursively traverse the given dataclass instance fields and build
        the lxml Element structure."""
        if not is_dataclass(obj):
            parent.text = self.render_value(obj)
            return parent

        meta = self.class_meta(obj.__class__, QName(parent).namespace)
        for var in meta.vars.values():
            value = getattr(obj, var.name)

            if value and var.namespace:
                namespaces.add(var.namespace)

            if not value:
                continue
            elif var.is_attribute:
                parent.set(var.qname, self.render_value(value))
            elif var.is_any_attribute:
                for qname, value in value.items():
                    parent.set(qname, value)
            elif var.is_text:
                parent.text = self.render_value(value)
            else:
                value = value if isinstance(value, list) else [value]
                for val in value:
                    sub_element = SubElement(parent, var.qname)
                    self.render_node(val, sub_element, namespaces)
                    self.set_nil_attribute(var, sub_element, namespaces)

        return parent

    @staticmethod
    def set_nil_attribute(var: ClassVar, element: Element, namespaces: Set[str]):
        if var.is_nillable and element.text is None and len(element) == 0:
            namespaces.add(Namespace.INSTANCE)
            qname = QName(Namespace.INSTANCE, "nil")
            element.set(qname, "true")

    @staticmethod
    def render_value(value) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, Enum):
            return str(value.value)

        return str(value)
