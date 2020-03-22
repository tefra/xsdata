from dataclasses import dataclass
from dataclasses import field
from dataclasses import is_dataclass
from typing import Any
from typing import Optional

from lxml.etree import cleanup_namespaces
from lxml.etree import Element
from lxml.etree import QName
from lxml.etree import SubElement
from lxml.etree import tostring

from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.converters import to_xml
from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.dataclass.models import AnyElement
from xsdata.formats.dataclass.models import AnyText
from xsdata.formats.dataclass.models import Namespaces
from xsdata.models.enums import Namespace

XSI_NIL_QNAME = QName(Namespace.XSI.uri, "nil")


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

    def render(self, obj: Any, namespaces: Optional[Namespaces] = None) -> str:
        """
        Convert the given object tree to xml string.

        Optionally provide a namespaces instance with a predefined list
        of namespace uris and prefixes.
        """
        tree = self.render_tree(obj, namespaces)
        return tostring(
            tree,
            xml_declaration=self.xml_declaration,
            encoding=self.encoding,
            pretty_print=self.pretty_print,
        ).decode()

    def render_tree(self, obj: Any, namespaces: Optional[Namespaces] = None) -> Element:
        """
        Convert a dataclass instance to a nested Element structure.

        Optionally provide a namespaces instance with a predefined list
        of namespace uris and prefixes.
        """
        meta = self.class_meta(obj.__class__)
        namespaces = namespaces or Namespaces()
        namespaces.register()
        namespaces.add(meta.namespace)

        root = self.render_node(obj, Element(meta.qname), namespaces)
        cleanup_namespaces(
            root, top_nsmap=namespaces.ns_map, keep_ns_prefixes=namespaces.prefixes
        )
        return root

    def render_node(self, obj, parent, namespaces: Namespaces) -> Element:
        """Recursively traverse the given dataclass instance fields and build
        the lxml Element structure."""
        if not is_dataclass(obj):
            self.set_text(parent, obj)
            return parent

        meta = self.class_meta(obj.__class__, QName(parent).namespace)
        for var in meta.vars.values():
            value = getattr(obj, var.name)
            if value is not None:
                if not var.is_any_element and not var.is_any_attribute:
                    namespaces.add(var.namespace)

                if var.is_attribute:
                    self.set_attribute(parent, var.qname, value)
                elif var.is_any_attribute:
                    self.set_attributes(parent, value)
                elif var.is_text:
                    self.set_text(parent, value)
                else:
                    self.render_sub_nodes(parent, value, var, namespaces)
            else:
                self.set_nil_attribute(parent, var, namespaces)

        self.unset_nil_attribute(parent)
        return parent

    def render_sub_nodes(
        self, parent, values: Any, var: ClassVar, namespaces: Namespaces
    ):
        if not isinstance(values, list):
            values = [values]

        is_wildcard = var.is_any_element

        for value in values:
            if value is None:
                continue
            elif not is_wildcard:
                sub_element = SubElement(parent, var.qname)
                self.render_node(value, sub_element, namespaces)
                self.set_nil_attribute(sub_element, var, namespaces)
            elif isinstance(value, str):
                if parent.text:
                    self.set_tail(parent, value)
                else:
                    self.set_text(parent, value)
            elif isinstance(value, AnyText):
                namespaces.add_all(value.nsmap)
                self.set_text(parent, value.text)
                self.set_attributes(parent, value.attributes)
            elif isinstance(value, AnyElement):
                qname = QName(value.qname)
                namespaces.add(qname.namespace)

                sub_element = SubElement(parent, qname)
                self.set_text(sub_element, value.text)
                self.set_tail(sub_element, value.tail)
                self.set_attributes(sub_element, value.attributes)
                for child in value.children:
                    self.render_sub_nodes(sub_element, child, var, namespaces)
            else:
                sub_element = SubElement(parent, value.qname)
                self.render_node(value, sub_element, namespaces)

        self.set_nil_attribute(parent, var, namespaces)

    @classmethod
    def set_attribute(cls, parent: Element, key: Any, value: Any):
        parent.set(to_xml(key), to_xml(value))

    @classmethod
    def set_attributes(cls, parent: Element, values: Any):
        for key, value in values.items():
            cls.set_attribute(parent, key, value)

    @classmethod
    def set_text(cls, parent: Element, value: Any):
        parent.text = to_xml(value)

    @classmethod
    def set_tail(cls, parent: Element, value: Any):
        parent.tail = to_xml(value)

    @staticmethod
    def set_nil_attribute(element: Element, var: ClassVar, namespaces: Namespaces):
        if var.is_nillable and element.text is None and len(element) == 0:
            namespaces.add(Namespace.XSI.uri, Namespace.XSI.prefix)
            element.set(XSI_NIL_QNAME, "true")

    @staticmethod
    def unset_nil_attribute(element: Element):
        if len(element) > 0 or element.text:
            element.attrib.pop(XSI_NIL_QNAME, None)
