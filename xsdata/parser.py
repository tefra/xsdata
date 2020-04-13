import sys
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Optional
from typing import TypeVar

from lxml import etree

from xsdata.formats.dataclass.parsers.nodes import XmlNode
from xsdata.formats.dataclass.parsers.xml import XmlParser
from xsdata.models import elements as xsd
from xsdata.models.enums import FormType
from xsdata.models.enums import Mode
from xsdata.models.enums import Namespace
from xsdata.models.mixins import ElementBase

T = TypeVar("T")


@dataclass
class SchemaParser(XmlParser):
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
    default_open_content: Optional[xsd.DefaultOpenContent] = field(default=None)
    schema_location: Optional[Path] = field(default=None)

    def from_xsd_string(self, source: str) -> xsd.Schema:
        return super().from_string(source, xsd.Schema)

    def from_xsd_path(self, path: Path) -> xsd.Schema:
        self.schema_location = path
        return super().from_path(path, xsd.Schema)

    def dequeue_node(self, element: etree.Element) -> Optional[T]:
        """Override parent method to skip empty elements and to set the object
        index."""
        item = self.queue[-1]
        obj = super(SchemaParser, self).dequeue_node(element)

        if obj:
            obj.index = item.index
            self.set_namespace_map(element, obj)

        return obj

    def start_schema(self, element: etree.Element, item: XmlNode):
        """Collect the schema's default form for attributes and elements for
        later usage."""

        self.element_form = element.attrib.get("elementFormDefault", None)
        self.attribute_form = element.attrib.get("attributeFormDefault", None)
        self.default_attributes = element.attrib.get("defaultAttributes", None)

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

        self.set_namespace_map(element, obj)

    @staticmethod
    def set_namespace_map(element: etree.Element, obj: ElementBase):
        obj.ns_map = element.nsmap
        namespaces = obj.ns_map.values()
        for namespace in Namespace:
            if namespace.uri not in namespaces:
                obj.ns_map[namespace.prefix] = namespace.uri

    @staticmethod
    def add_default_imports(obj: xsd.Schema):
        """Add missing imports to the standard schemas if the namespace is
        declared and."""
        imp_namespaces = [imp.namespace for imp in obj.imports]
        xsi_ns = Namespace.XSI.value
        if xsi_ns in obj.ns_map.values() and xsi_ns not in imp_namespaces:
            obj.imports.insert(0, xsd.Import.create(namespace=xsi_ns))

    def resolve_schemas_locations(self, obj: xsd.Schema):
        """Resolve the locations of the schema overrides, redefines, includes
        and imports relatively to the schema location."""
        if not self.schema_location:
            return

        obj.location = self.schema_location
        for over in obj.overrides:
            over.location = self.resolve_path(over.schema_location)

        for red in obj.redefines:
            red.location = self.resolve_path(red.schema_location)

        for inc in obj.includes:
            inc.location = self.resolve_path(inc.schema_location)

        for imp in obj.imports:
            imp.location = self.resolve_local_path(imp.schema_location, imp.namespace)

    def resolve_path(self, location: Optional[str]) -> Optional[Path]:
        """Resolve the given location string relatively the schema location
        path."""
        path = None
        if self.schema_location and location:
            path = self.schema_location.parent.joinpath(location).resolve()
        return path if path and path.exists() else None

    def resolve_local_path(self, location, namespace):
        """Resolve the given namespace to one of the local standard schemas or
        fallback to the external file path."""
        if not location or location.startswith("http"):
            ns = Namespace.get_enum(namespace)
            return ns.location if ns else None

        return self.resolve_path(location)

    def end_attribute(self, obj: T, element: etree.Element):
        """Assign the schema's default form for attributes if the given
        attribute form is None."""
        if isinstance(obj, xsd.Attribute) and obj.form is None and self.attribute_form:
            obj.form = FormType(self.attribute_form)

    def end_complex_type(self, obj: T, element: etree.Element):
        """Prepend an attribute group reference when default attributes
        apply."""
        if not isinstance(obj, xsd.ComplexType):
            return

        if obj.default_attributes_apply and self.default_attributes:
            attribute_group = xsd.AttributeGroup.create(ref=self.default_attributes)
            obj.attribute_groups.insert(0, attribute_group)

        if not obj.open_content:
            obj.open_content = self.default_open_content

    def end_default_open_content(self, obj: T, element: etree.Element):
        if isinstance(obj, xsd.DefaultOpenContent):
            if obj.any and obj.mode == Mode.SUFFIX:
                obj.any.index = sys.maxsize

            self.default_open_content = obj

    def end_element(self, obj: T, element: etree.Element):
        """Assign the schema's default form for elements if the given element
        form is None."""
        if isinstance(obj, xsd.Element) and obj.form is None and self.element_form:
            obj.form = FormType(self.element_form)

    def end_extension(self, obj: T, element: etree.Element):
        if isinstance(obj, xsd.Extension) and not obj.open_content:
            obj.open_content = self.default_open_content

    @classmethod
    def end_open_content(cls, obj: T, element: etree.Element):
        if isinstance(obj, xsd.OpenContent):
            if obj.any and obj.mode == Mode.SUFFIX:
                obj.any.index = sys.maxsize

    def end_restriction(self, obj: T, element: etree.Element):
        if isinstance(obj, xsd.Restriction) and not obj.open_content:
            obj.open_content = self.default_open_content

    def end_schema(self, obj: T, element: etree.Element):
        """Normalize various properties for the schema and it's children."""
        if isinstance(obj, xsd.Schema):
            self.set_schema_forms(obj)
            self.set_schema_namespaces(obj, element)
            self.add_default_imports(obj)
            self.resolve_schemas_locations(obj)
