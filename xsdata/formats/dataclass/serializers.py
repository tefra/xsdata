import json
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Type

from lxml.etree import Element
from lxml.etree import QName
from lxml.etree import SubElement
from lxml.etree import tostring

from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.mixins import AbstractSerializer


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
    :param dict_factory: Callable to generate dictionary
    :param encoder: Value encoder
    :param indent: Pretty print indent
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
    :param xml_declaration: Add xml declaration
    :param encoding: Result text encoding
    :param pretty_print: Enable pretty output
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

    def render_tree(self, obj: object) -> Element:
        """
        Convert a dataclass instance to a nested Element structure.

        If the instance class is generated from the xsdata cli the root
        element's name will be auto assigned otherwise it will default
        to the class name.

        :raise TypeError: If the instance is not a dataclass
        """
        if not self.is_dataclass(obj):
            raise TypeError(f"Object {obj} is not a dataclass.")

        meta = self.class_meta(obj.__class__)
        qname = self.render_tag(meta.name, meta.namespace)
        namespaces = self.namespaces(obj.__class__)
        nsmap = {f"ns{index}": ns for index, ns in enumerate(sorted(namespaces))}
        return self.render_node(obj, Element(qname, nsmap=nsmap))

    def render_node(self, obj, parent, nillable=False) -> Element:
        """Recursively traverse the given dataclass instance fields and build
        the lxml Element structure."""
        if not self.is_dataclass(obj):
            parent.text = self.render_value(obj)
            return parent

        for f in self.fields(obj.__class__):
            value = getattr(obj, f.name)

            if not value:
                continue
            elif f.is_attribute:
                if f.namespace is None:
                    qname = f.local_name
                else:
                    qname = self.render_tag(f.local_name, f.namespace)

                parent.set(qname, self.render_value(value))
            elif f.is_text:
                parent.text = self.render_value(value)
            else:
                value = value if isinstance(value, list) else [value]

                if f.namespace == "":
                    qname = f.local_name
                elif f.namespace:
                    qname = self.render_tag(f.local_name, f.namespace)
                elif parent.prefix:
                    qname = self.render_tag(f.local_name, parent.nsmap[parent.prefix])
                else:
                    qname = f.local_name

                for val in value:
                    sub_element = SubElement(parent, qname)
                    self.render_node(val, sub_element)

                    if (
                        f.is_nillable
                        and sub_element.text is None
                        and len(sub_element) == 0
                    ):
                        sub_element.set(
                            "{http://www.w3.org/2001/XMLSchema-instance}nil", "true"
                        )

        return parent

    @staticmethod
    def render_tag(name, namespace=None) -> QName:
        return QName(namespace, name)

    @staticmethod
    def render_value(value) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, Enum):
            return str(value.value)

        return str(value)
