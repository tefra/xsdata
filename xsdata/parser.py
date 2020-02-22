import pathlib
import sys
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union

from lxml import etree

from xsdata.formats.dataclass.parsers import QueueItem
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.models import elements as xsd
from xsdata.models.enums import FormType
from xsdata.models.mixins import OccurrencesMixin
from xsdata.utils import text

T = TypeVar("T")


@dataclass
class SchemaParser(XmlParser):
    name_generator: Callable = field(default=text.camel_case)
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

    def end_node(self, element: etree.Element) -> Optional[T]:
        """Override parent method to skip empty elements and to set the object
        index."""
        if not element.attrib and element.text is None and len(element) == 0:
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
        if not isinstance(obj, xsd.Choice):
            return

        for child in obj.children():
            if isinstance(child, OccurrencesMixin):
                child.min_occurs = 0
                if child.max_occurs is None:
                    child.max_occurs = obj.max_occurs

    @classmethod
    def end_all(cls, obj: T, element: etree.Element):
        """Elements inside an all element can by definition appear at most
        once, reset their max occur counter."""

        if not isinstance(obj, xsd.All):
            return

        for child in obj.children():
            if isinstance(child, OccurrencesMixin):
                cls.inherit_occurs(obj, child, force=True)

    @classmethod
    def end_sequence(cls, obj: T, element: etree.Element):
        """Elements inside a sequence inherit min|max occur counter if it is
        not set."""
        if not isinstance(obj, xsd.Sequence):
            return

        for child in obj.children():
            if isinstance(child, OccurrencesMixin):
                cls.inherit_occurs(obj, child)

    @classmethod
    def inherit_occurs(
        cls,
        parent: Union[xsd.Sequence, xsd.All],
        child: OccurrencesMixin,
        force: bool = False,
    ):
        if child.min_occurs is None or force:
            child.min_occurs = parent.min_occurs
        if child.max_occurs is None or force:
            child.max_occurs = parent.max_occurs

    @classmethod
    def parse_value(cls, types: List[Type], value: Any) -> Any:
        if int in types and value == "unbounded":
            return sys.maxsize
        try:
            return super().parse_value(types, value)
        except ValueError:
            return str(value)
