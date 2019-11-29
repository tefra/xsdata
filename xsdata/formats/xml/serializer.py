from dataclasses import dataclass, is_dataclass
from enum import Enum

from lxml import etree
from lxml.etree import Element, SubElement

from xsdata.formats.inspect import ModelInspect


@dataclass
class XmlSerializer(ModelInspect):
    def render(
        self,
        obj: object,
        xml_declaration=True,
        encoding="UTF-8",
        pretty_print=False,
        **kwargs,
    ) -> bytes:

        tree = self.render_tree(obj)
        return etree.tostring(
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

        name = getattr(obj, "ROOT_NAME", obj.__class__.__name__)
        root = Element(name)
        return self.render_node(obj, root)

    def render_node(self, obj, parent) -> Element:
        """Recursively traverse the given dataclass instance fields and build
        the lxml Element structure."""
        if not is_dataclass(obj):
            parent.text = self.render_value(obj)
            return parent

        for field in self.fields(obj.__class__):
            value = getattr(obj, field.name)
            if not value:
                continue

            if field.is_attribute:
                parent.set(field.local_name, self.render_value(value))
            elif field.is_list and len(value):
                for val in value:
                    sub_element = SubElement(parent, field.local_name)
                    self.render_node(val, sub_element)
            elif value:
                sub_element = SubElement(parent, field.local_name)
                self.render_node(value, sub_element)

        return parent

    @staticmethod
    def render_value(value):
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, Enum):
            return str(value.value)

        return str(value)
