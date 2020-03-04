from dataclasses import dataclass
from dataclasses import field
from dataclasses import is_dataclass
from typing import Any
from typing import Optional
from typing import Set

from lxml.etree import cleanup_namespaces
from lxml.etree import Element
from lxml.etree import QName
from lxml.etree import SubElement
from lxml.etree import tostring

from xsdata.exceptions import SerializerError
from xsdata.formats.converters import to_xml
from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.dataclass.models import AnyElement
from xsdata.formats.mixins import AbstractSerializer
from xsdata.models.enums import Namespace


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
            parent.text = to_xml(obj)
            return parent

        meta = self.class_meta(obj.__class__, QName(parent).namespace)
        for var in meta.vars.values():
            value = getattr(obj, var.name)
            if value is not None:
                if var.namespace:
                    namespaces.add(var.namespace)

                if var.is_attribute:
                    self.set_attribute(parent, value, var)
                elif var.is_any_attribute:
                    self.set_attributes(parent, value)
                elif var.is_any_element:
                    self.set_any_children(parent, value, namespaces)
                elif var.is_text:
                    if is_dataclass(value):
                        raise SerializerError("Text nodes can't be dataclasses!")
                    self.set_text(parent, value)
                else:
                    self.set_children(parent, value, var, namespaces)
            elif var.is_text:
                self.set_nil_attribute(var, parent, namespaces)

        return parent

    def set_attribute(self, parent: Element, value: Any, var: ClassVar):
        parent.set(var.qname, to_xml(value))

    def set_attributes(self, parent: Element, value: Any):
        for qname, value in value.items():
            parent.set(qname, to_xml(value))

    def set_text(self, parent: Element, value: Any):
        parent.text = to_xml(value)

    def set_children(
        self, parent: Element, value: Any, var: ClassVar, namespaces: Set[str]
    ):
        value = value if isinstance(value, list) else [value]
        for val in value:
            sub_element = SubElement(parent, var.qname)
            self.render_node(val, sub_element, namespaces)
            self.set_nil_attribute(var, sub_element, namespaces)

    @classmethod
    def set_any_children(cls, parent: Element, value: Any, namespaces: Set[str]):
        value = value if isinstance(value, list) else [value]
        for val in value:

            if isinstance(val, str):
                if parent.text:
                    parent.tail = val
                else:
                    parent.text = val
            elif isinstance(val, AnyElement):
                qname = QName(val.qname)
                namespace = qname.namespace
                if namespace:
                    namespaces.add(namespace)

                sub_element = SubElement(parent, qname)
                sub_element.text = val.text
                sub_element.tail = val.tail

                for child in val.children:
                    cls.set_any_children(sub_element, child, namespaces)

    @staticmethod
    def set_nil_attribute(var: ClassVar, element: Element, namespaces: Set[str]):
        if var.is_nillable and element.text is None and len(element) == 0:
            namespaces.add(Namespace.XSI.uri)
            qname = QName(Namespace.XSI.uri, "nil")
            element.set(qname, "true")
