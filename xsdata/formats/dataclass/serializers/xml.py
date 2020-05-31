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

from xsdata.exceptions import SerializerError
from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.formats.dataclass.serializers.utils import SerializeUtils
from xsdata.models.enums import FormType
from xsdata.models.enums import QNames

DEFAULT_NS_PREFIX = ""


@dataclass
class XmlSerializer(AbstractSerializer):
    """
    :param xml_declaration: Add xml declaration
    :param encoding: Result text encoding
    :param pretty_print: Enable pretty output
    :param context: XmlContext instance
    """

    xml_declaration: bool = field(default=True)
    encoding: str = field(default="UTF-8")
    pretty_print: bool = field(default=False)
    context: XmlContext = field(default_factory=XmlContext)

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
        meta = self.context.build(obj.__class__)
        namespaces = namespaces or Namespaces()
        namespaces.register()
        prefix = DEFAULT_NS_PREFIX if meta.element_form == FormType.QUALIFIED else None
        namespaces.add(meta.qname.namespace, prefix=prefix)

        root = Element(meta.qname, nsmap=namespaces.ns_map)
        self.render_node(root, obj, namespaces)
        cleanup_namespaces(
            root, top_nsmap=namespaces.ns_map, keep_ns_prefixes=namespaces.prefixes
        )
        return root

    def render_node(self, parent: Element, obj: Any, namespaces: Namespaces):
        """Recursively traverse the given object and build the xml tree."""
        if is_dataclass(obj):
            self.render_complex_node(parent, obj, namespaces)
        else:
            SerializeUtils.set_text(parent, obj, namespaces)

    def render_complex_node(self, parent: Element, obj: Any, namespaces: Namespaces):
        meta = self.context.build(obj.__class__, QName(parent).namespace)
        for var, value in self.next_value(meta, obj):
            if value is None:
                continue
            elif var.is_attribute:
                SerializeUtils.set_attribute(parent, var.qname, value, namespaces)
            elif var.is_attributes:
                SerializeUtils.set_attributes(parent, value, namespaces)
            elif var.is_text:
                namespaces.add(var.qname.namespace)
                SerializeUtils.set_text(parent, value, namespaces)
            elif isinstance(value, list):
                self.render_sub_nodes(parent, value, var, namespaces)
            else:
                self.render_sub_node(parent, value, var, namespaces)

        SerializeUtils.set_nil_attribute(parent, meta.nillable, namespaces)

    def render_sub_nodes(
        self, parent: Element, values: List, var: XmlVar, namespaces: Namespaces
    ):
        for value in values:
            self.render_sub_node(parent, value, var, namespaces)

    def render_sub_node(
        self, parent: Element, value: Any, var: XmlVar, namespaces: Namespaces
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
        self, parent: Element, value: Any, var: XmlVar, namespaces: Namespaces
    ):
        if hasattr(value, "qname"):
            qname = value.qname
        elif var.is_wildcard:
            meta = self.context.fetch(value.__class__, QName(parent).namespace)
            qname = meta.qname
        else:
            qname = var.qname

        namespaces.add(qname.namespace)
        sub_element = SubElement(parent, qname)
        self.render_node(sub_element, value, namespaces)
        self.set_xsi_type(sub_element, value, var, namespaces)
        SerializeUtils.set_nil_attribute(sub_element, var.nillable, namespaces)

    def render_wildcard_node(
        self, parent: Element, value: Any, var: XmlVar, namespaces: Namespaces
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

    def set_xsi_type(
        self, parent: Element, value: Any, var: XmlVar, namespaces: Namespaces
    ):
        if not var.clazz or value.__class__ is var.clazz:
            return

        if self.context.is_derived(value, var.clazz):
            meta = self.context.fetch(value.__class__, QName(parent.tag).namespace)
            SerializeUtils.set_attribute(
                parent, QNames.XSI_TYPE, meta.source_qname, namespaces
            )
        else:
            raise SerializerError(
                f"{value.__class__.__name__} is not derived from {var.clazz.__name__}"
            )

    @classmethod
    def next_value(cls, meta: XmlMeta, obj: Any):

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
