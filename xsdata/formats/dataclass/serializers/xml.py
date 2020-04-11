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
from xsdata.formats.dataclass.context import ModelContext
from xsdata.formats.dataclass.models.context import ClassMeta
from xsdata.formats.dataclass.models.context import ClassVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames


@dataclass
class XmlSerializer(AbstractSerializer, ModelContext):
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
            self.set_text(parent, obj, namespaces)
            return parent

        meta = self.class_meta(obj.__class__, QName(parent).namespace)
        for var, value in self.next_value(meta, obj):
            if value is not None:
                if not var.is_wildcard and not var.is_attributes:
                    namespaces.add(var.namespace)

                if var.is_attribute:
                    self.set_attribute(parent, var.qname, value, namespaces)
                elif var.is_attributes:
                    self.set_attributes(parent, value, namespaces)
                elif var.is_text:
                    self.set_text(parent, value, namespaces)
                else:
                    self.render_sub_nodes(parent, value, var, namespaces)

        self.set_nil_attribute(parent, meta.nillable, namespaces)
        return parent

    def render_sub_nodes(
        self, parent, values: Any, var: ClassVar, namespaces: Namespaces
    ):
        if not isinstance(values, list):
            values = [values]

        for value in values:
            if value is None:
                continue
            elif isinstance(value, AnyElement):
                if value.qname:
                    sub_element = SubElement(parent, value.qname)
                else:
                    sub_element = parent

                namespaces.add_all(value.ns_map)
                self.set_text(sub_element, value.text, namespaces)
                self.set_tail(sub_element, value.tail, namespaces)
                self.set_attributes(sub_element, value.attributes, namespaces)
                for child in value.children:
                    self.render_sub_nodes(sub_element, child, var, namespaces)
                    self.set_nil_attribute(parent, var.nillable, namespaces)
            elif var.is_element or is_dataclass(value):
                qname = value.qname if hasattr(value, "qname") else var.qname
                sub_element = SubElement(parent, qname)
                self.render_node(value, sub_element, namespaces)
                self.set_nil_attribute(sub_element, var.nillable, namespaces)
            elif not parent.text or var.is_text:
                self.set_text(parent, value, namespaces)
            else:
                self.set_tail(parent, value, namespaces)

    @classmethod
    def set_attribute(
        cls, parent: Element, key: Any, value: Any, namespaces: Namespaces
    ):
        if key != QNames.XSI_NIL or (not parent.text and len(parent) == 0):
            value = to_xml(value, namespaces)
            if value:
                parent.set(key, to_xml(value, namespaces))

    @classmethod
    def set_attributes(cls, parent: Element, values: Any, namespaces: Namespaces):
        for key, value in values.items():
            cls.set_attribute(parent, key, value, namespaces)

    @classmethod
    def set_text(cls, parent: Element, value: Any, namespaces: Namespaces):
        value = to_xml(value, namespaces)
        if isinstance(value, str) and len(value) == 0:
            value = None
        parent.text = value

    @classmethod
    def set_tail(cls, parent: Element, value: Any, namespaces: Namespaces):
        parent.tail = to_xml(value, namespaces)

    @classmethod
    def set_nil_attribute(
        cls, element: Element, nillable: bool, namespaces: Namespaces
    ):
        if nillable and element.text is None and len(element) == 0:
            namespaces.add(Namespace.XSI.uri, Namespace.XSI.prefix)
            element.set(QNames.XSI_NIL, "true")

    @classmethod
    def next_value(cls, meta: ClassMeta, obj: Any):

        index = 0
        attrs = meta.vars
        stop = len(attrs)
        while index < stop:
            var = attrs[index]
            if not var.sequential:
                yield var, getattr(obj, var.name)
                index += 1
                continue

            end = next(
                (i for i in range(index + 1, stop) if not attrs[i].sequential), stop
            )
            sequence = attrs[index:end]
            index = end
            j = 0

            rolling = True
            while rolling:
                rolling = False
                for var in sequence:
                    values = getattr(obj, var.name)
                    if j < len(values):
                        rolling = True
                        yield var, values[j]
                j += 1
