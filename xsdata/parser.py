import pathlib
import sys
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Callable
from typing import Optional
from typing import Type
from typing import TypeVar

from lxml import etree

from xsdata.formats.dataclass.parsers import QueueItem
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.models import elements as xsd
from xsdata.models.enums import FormType
from xsdata.utils import text

T = TypeVar("T")


@dataclass
class SchemaParser(XmlParser):
    name: Callable = field(default=text.camel_case)
    """
    A simple parser to convert an xsd schema to an easy to handle data
    structure based on dataclasses.

    The parser is a dummy as possible but it will try to normalize
    certain things like apply parent properties to children.
    """

    element_form: Optional[FormType] = field(init=False, default=None)
    attribute_form: Optional[FormType] = field(init=False, default=None)
    target_namespace: Optional[str] = field(default=None)

    def from_xsd_string(self, source: str) -> xsd.Schema:
        return super().from_string(source, xsd.Schema)

    def from_xsd_path(self, path: pathlib.Path) -> xsd.Schema:
        schema = super().from_path(path, xsd.Schema)
        schema.location = path
        return schema

    def end_node(self, element: etree.Element) -> Optional[Type]:
        """Override parent method to skip empty elements and to set the object
        index."""
        if not element.attrib and element.text is None:
            self.queue.pop()
            return None

        item = self.queue[-1]
        obj = super(SchemaParser, self).end_node(element)

        # Make sure queue item is not part of mixed content
        if obj is None or item is None:
            return None

        obj.index = item.index
        return obj

    def start_schema(self, element: etree.Element, item: QueueItem):
        """Collect the schema's default form for attributes and elements for
        later usage."""

        self.element_form = element.attrib.get("elementFormDefault", None)
        self.attribute_form = element.attrib.get("attributeFormDefault", None)

    def end_schema(self, obj: T, element: etree.Element):
        """Collect the schema's default form for attributes and elements for
        later usage."""
        if isinstance(obj, xsd.Schema):
            if self.element_form:
                obj.element_form_default = FormType(self.element_form)
            if self.attribute_form:
                obj.attribute_form_default = FormType(self.attribute_form)

            obj.nsmap = element.nsmap
            if obj.target_namespace is None and self.target_namespace is not None:
                obj.target_namespace = self.target_namespace

            for child_element in obj.elements:
                child_element.form = FormType.QUALIFIED

            for child_attribute in obj.attributes:
                child_attribute.form = FormType.QUALIFIED

    def end_element(self, obj: T, element: etree.Element):
        """Assign the schema's default form for elements if the given element
        form is None."""
        if isinstance(obj, xsd.Element) and obj.form is None and self.element_form:
            obj.form = FormType(self.element_form)

    def end_attribute(self, obj: T, element: etree.Element):
        """Assign the schema's default form for attributes if the given
        attribute form is None."""
        if isinstance(obj, xsd.Attribute) and obj.form is None and self.attribute_form:
            obj.form = FormType(self.attribute_form)

    @staticmethod
    def end_choice(obj: T, element: etree.Element):
        """Elements inside a choice are by definition optional, reset their min
        occurs counter."""
        if isinstance(obj, xsd.Choice):
            for child in obj.elements:
                child.min_occurs = 0
                if child.max_occurs is None:
                    child.max_occurs = obj.max_occurs

    @staticmethod
    def end_all(obj: T, element: etree.Element):
        """Elements inside an all element can by definition appear at most
        once, reset their max occur counter."""

        if isinstance(obj, xsd.All):
            for child in obj.elements:
                child.max_occurs = 1
                if child.min_occurs is None:
                    child.min_occurs = obj.min_occurs

    @staticmethod
    def end_sequence(obj: T, element: etree.Element):
        """Elements inside a sequence inherit min|max occur counter if it is
        not set."""
        if isinstance(obj, xsd.Sequence):
            for child in obj.elements:
                if child.min_occurs is None:
                    child.min_occurs = obj.min_occurs
                if child.max_occurs is None:
                    child.max_occurs = obj.max_occurs

    @classmethod
    def parse_value(cls, tp: Type, value: Any) -> Any:
        if tp is int and value == "unbounded":
            return sys.maxsize
        try:
            return super().parse_value(tp, value)
        except ValueError:
            return str(value)
