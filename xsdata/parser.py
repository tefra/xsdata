import pathlib
import sys
from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar

from lxml import etree

from xsdata.formats.dataclass.parsers.xml import QueueItem
from xsdata.formats.dataclass.parsers.xml import XmlParser
from xsdata.models import elements as xsd
from xsdata.models.enums import FormType
from xsdata.models.enums import Namespace
from xsdata.models.mixins import OccurrencesMixin
from xsdata.utils import text

T = TypeVar("T")


class Force(Enum):
    NO = 0
    MIN_ONLY = 1
    MAX_ONLY = 2
    BOTH = 3


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
    default_attributes: Optional[str] = field(default=None)

    def from_xsd_string(self, source: str) -> xsd.Schema:
        return super().from_string(source, xsd.Schema)

    def from_xsd_path(self, path: pathlib.Path) -> xsd.Schema:
        schema = super().from_path(path, xsd.Schema)
        schema.location = path
        return schema

    def dequeue_node(self, element: etree.Element) -> Optional[T]:
        """Override parent method to skip empty elements and to set the object
        index."""
        if not element.attrib and element.text is None and len(element) == 0:
            self.queue.pop()
            return None

        item = self.queue[-1]
        obj = super(SchemaParser, self).dequeue_node(element)

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
        self.default_attributes = element.attrib.get("defaultAttributes", None)

    def end_schema(self, obj: T, element: etree.Element):
        """Set schema namespaces and default form for elements and
        attributes."""
        if isinstance(obj, xsd.Schema):
            self.set_schema_forms(obj)
            self.set_schema_namespaces(obj, element)

    def set_schema_forms(self, obj: xsd.Schema):
        """
        Set the default form type for elements and attributes.

        Global elements and attributes are by default qualified.
        """
        if self.element_form:
            obj.element_form_default = FormType(self.element_form)
        if self.attribute_form:
            obj.attribute_form_default = FormType(self.attribute_form)

        for child_element in obj.elements:
            child_element.form = FormType.QUALIFIED

        for child_attribute in obj.attributes:
            child_attribute.form = FormType.QUALIFIED

    def set_schema_namespaces(self, obj: xsd.Schema, element: etree.Element):
        """Set the given schema's target namespace and add the default
        namespaces if the are missing xsi, xlink, xml, xs."""
        obj.target_namespace = obj.target_namespace or self.target_namespace

        obj.nsmap = element.nsmap
        namespaces = obj.nsmap.values()

        for namespace in Namespace:
            if namespace.uri not in namespaces:
                obj.nsmap[namespace.prefix] = namespace.uri

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

    def end_complex_type(self, obj: T, element: etree.Element):
        """Prepend an attribute group reference when default attributes
        apply."""
        if (
            isinstance(obj, xsd.ComplexType)
            and obj.default_attributes_apply
            and self.default_attributes
        ):
            attribute_group = xsd.AttributeGroup.create(ref=self.default_attributes)
            obj.attribute_groups.insert(0, attribute_group)

    @classmethod
    def end_choice(cls, obj: T, element: etree.Element):
        """Elements inside a choice are by definition optional, reset their min
        occurs counter."""
        if isinstance(obj, xsd.Choice):
            cls.cascade_occurs(obj, 0, obj.max_occurs, force=Force.MIN_ONLY)

    @classmethod
    def end_default_open_content(cls, obj: T, element: etree.Element):
        if isinstance(obj, xsd.DefaultOpenContent):
            cls.cascade_occurs(obj, min_occurs=1, max_occurs=1)

    @classmethod
    def end_open_content(cls, obj: T, element: etree.Element):
        if isinstance(obj, xsd.OpenContent):
            cls.cascade_occurs(obj, 1, 1)

    @classmethod
    def end_all(cls, obj: T, element: etree.Element):
        """Elements inside an all element can by definition appear at most
        once, reset their max occur counter."""
        if isinstance(obj, xsd.All):
            cls.cascade_occurs(obj, obj.min_occurs, obj.max_occurs)

    @classmethod
    def end_sequence(cls, obj: T, element: etree.Element):
        """Elements inside a sequence inherit min|max occur counter if it is
        not set."""
        if isinstance(obj, xsd.Sequence):
            cls.cascade_occurs(obj, obj.min_occurs, obj.max_occurs)

    @classmethod
    def cascade_occurs(
        cls,
        parent: xsd.ElementBase,
        min_occurs: Optional[int] = None,
        max_occurs: Optional[int] = None,
        force: Force = Force.NO,
    ):

        force_min = force in (Force.BOTH, Force.MIN_ONLY)
        force_max = force in (Force.BOTH, Force.MAX_ONLY)

        for child in parent.children():
            if isinstance(child, OccurrencesMixin):
                if child.min_occurs == 1 or force_min:
                    child.min_occurs = min_occurs
                if child.max_occurs == 1 or force_max:
                    child.max_occurs = max_occurs

    @classmethod
    def parse_value(cls, types: List[Type], value: Any, default: Any = None) -> Any:
        if int in types and value == "unbounded":
            return sys.maxsize
        try:
            return super().parse_value(types, value, default)
        except ValueError:
            return str(value)
