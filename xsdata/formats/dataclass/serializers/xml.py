from dataclasses import dataclass
from dataclasses import field
from dataclasses import is_dataclass
from typing import Any
from typing import List
from typing import Optional

from lxml.etree import cleanup_namespaces
from lxml.etree import Element
from lxml.etree import QName
from lxml.etree import SubElement
from lxml.etree import tostring

from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.dataclass.context import ModelContext
from xsdata.formats.dataclass.models.context import ClassMeta
from xsdata.formats.dataclass.models.context import ClassVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.formats.dataclass.serializers.utils import SerializeUtils


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
            SerializeUtils.set_text(parent, obj, namespaces)
            return parent

        meta = self.class_meta(obj.__class__, QName(parent).namespace)
        for var, value in self.next_value(meta, obj):
            if value is None:
                continue
            elif var.is_attribute:
                SerializeUtils.set_attribute(parent, var.qname, value, namespaces)
            elif var.is_attributes:
                SerializeUtils.set_attributes(parent, value, namespaces)
            elif var.is_text:
                namespaces.add(var.namespace)
                SerializeUtils.set_text(parent, value, namespaces)
            elif isinstance(value, list):
                self.render_sub_nodes(parent, value, var, namespaces)
            else:
                self.render_sub_node(parent, value, var, namespaces)

        SerializeUtils.set_nil_attribute(parent, meta.nillable, namespaces)
        return parent

    def render_sub_nodes(
        self, parent: Element, values: List, var: ClassVar, namespaces: Namespaces
    ):
        for value in values:
            self.render_sub_node(parent, value, var, namespaces)

    def render_sub_node(
        self, parent: Element, value: Any, var: ClassVar, namespaces: Namespaces
    ):
        if isinstance(value, AnyElement):
            self.render_wildcard_node(parent, value, var, namespaces)
        elif var.is_element or is_dataclass(value):
            self.render_element_node(parent, value, var, namespaces)
        elif not parent.text:
            SerializeUtils.set_text(parent, value, namespaces)
        else:
            SerializeUtils.set_tail(parent, value, namespaces)

    def render_element_node(
        self, parent: Element, value: Any, var: ClassVar, namespaces: Namespaces
    ):
        qname = value.qname if hasattr(value, "qname") else var.qname

        if isinstance(qname, QName):
            namespaces.add(qname.namespace)

        sub_element = SubElement(parent, qname)
        self.render_node(value, sub_element, namespaces)
        SerializeUtils.set_nil_attribute(sub_element, var.nillable, namespaces)

    def render_wildcard_node(
        self, parent: Element, value: Any, var: ClassVar, namespaces: Namespaces
    ):
        if value.qname:
            sub_element = SubElement(parent, value.qname)
        else:
            sub_element = parent

        namespaces.add_all(value.ns_map)
        SerializeUtils.set_text(sub_element, value.text, namespaces)
        SerializeUtils.set_tail(sub_element, value.tail, namespaces)
        SerializeUtils.set_attributes(sub_element, value.attributes, namespaces)
        for child in value.children:
            self.render_sub_node(sub_element, child, var, namespaces)

        SerializeUtils.set_nil_attribute(sub_element, var.nillable, namespaces)

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
