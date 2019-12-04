from dataclasses import dataclass, field
from enum import Enum

from lxml.etree import Element, QName, SubElement, cleanup_namespaces, tostring

from xsdata.formats.inspect import ModelInspect


@dataclass
class XmlSerializer(ModelInspect):
    ns_list: list = field(init=False, default_factory=list)

    def render(
        self,
        obj: object,
        xml_declaration=True,
        encoding="UTF-8",
        pretty_print=False,
        **kwargs,
    ) -> bytes:

        tree = self.render_tree(obj)
        return tostring(
            tree,
            xml_declaration=xml_declaration,
            encoding=encoding,
            pretty_print=pretty_print,
            **kwargs,
        )

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

        meta = self.type_meta(obj.__class__)
        qname = self.render_tag(meta.name, meta.namespace)
        root = self.render_node(obj, Element(qname))

        cleanup_namespaces(
            root,
            top_nsmap={
                None if index == 0 else f"ns{index}": namespace
                for index, namespace in enumerate(self.ns_list)
            },
        )

        return root

    def render_node(self, obj, parent) -> Element:
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
                parent.set(f.local_name, self.render_value(value))
            else:
                value = value if type(value) is list else [value]
                if f.namespace:
                    qname = self.render_tag(f.local_name, f.namespace)
                elif parent.prefix:
                    qname = self.render_tag(
                        f.local_name, parent.nsmap[parent.prefix]
                    )
                else:
                    qname = f.local_name

                for val in value:
                    sub_element = SubElement(parent, qname)
                    self.render_node(val, sub_element)

        return parent

    def render_tag(self, name, namespace=None) -> QName:
        if namespace and namespace not in self.ns_list:
            self.ns_list.append(namespace)
        return QName(namespace, name)

    @staticmethod
    def render_value(value) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, Enum):
            return str(value.value)

        return str(value)
