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

from xsdata.exceptions import SerializerError
from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.converters import to_xml
from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.dataclass.models import AnyElement
from xsdata.formats.dataclass.models import AnyText
from xsdata.formats.dataclass.models import Namespaces
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
            parent.text = to_xml(obj)
            return parent

        meta = self.class_meta(obj.__class__, QName(parent).namespace)
        for var in meta.vars.values():
            value = getattr(obj, var.name)
            if value is not None:
                if not var.is_any_element:
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

    def set_children(
        self, parent: Element, value: Any, var: ClassVar, namespaces: Namespaces
    ):
        value = value if isinstance(value, list) else [value]
        for val in value:
            sub_element = SubElement(parent, var.qname)
            self.render_node(val, sub_element, namespaces)
            self.set_nil_attribute(var, sub_element, namespaces)

    @classmethod
    def set_attribute(cls, parent: Element, value: Any, var: ClassVar):
        parent.set(var.qname, to_xml(value))

    @classmethod
    def set_attributes(cls, parent: Element, values: Any):
        for key, value in values.items():
            parent.set(key, value)

    @classmethod
    def set_text(cls, parent: Element, value: Any):
        parent.text = to_xml(value)

    @classmethod
    def set_any_children(cls, parent: Element, value: Any, namespaces: Namespaces):
        value = value if isinstance(value, list) else [value]
        for val in value:
            if isinstance(val, str):
                if parent.text:
                    parent.tail = val
                else:
                    parent.text = val
            elif isinstance(val, AnyText):
                parent.text = val.text
                namespaces.add_all(val.nsmap)
                cls.set_attributes(parent, val.attributes)
            elif isinstance(val, AnyElement):
                qname = QName(val.qname)
                namespaces.add(qname.namespace)

                sub_element = SubElement(parent, qname)
                sub_element.text = val.text
                sub_element.tail = val.tail

                cls.set_attributes(sub_element, val.attributes)
                for child in val.children:
                    cls.set_any_children(sub_element, child, namespaces)

    @staticmethod
    def set_nil_attribute(var: ClassVar, element: Element, namespaces: Namespaces):
        if var.is_nillable and element.text is None and len(element) == 0:
            namespaces.add(Namespace.XSI.uri, Namespace.XSI.prefix)
            qname = QName(Namespace.XSI.uri, "nil")
            element.set(qname, "true")
