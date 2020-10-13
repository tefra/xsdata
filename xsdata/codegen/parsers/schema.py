import sys
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from urllib.parse import urljoin

from xsdata.formats.bindings import T
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.nodes import Parsed
from xsdata.formats.dataclass.parsers.xml import XmlParser
from xsdata.models import xsd
from xsdata.models.enums import FormType
from xsdata.models.enums import Mode
from xsdata.models.enums import Namespace


@dataclass
class SchemaParser(XmlParser):
    """
    A simple parser to convert an xsd schema to an easy to handle data
    structure based on dataclasses.

    The parser is a dummy as possible but it will try to normalize
    certain things like apply parent properties to children.

    :param location:
    :param element_form:
    :param attribute_form:
    :param target_namespace:
    :param default_attributes:
    :param default_open_content:
    """

    index: int = field(default_factory=int)
    indices: List[int] = field(default_factory=list)
    location: Optional[str] = field(default=None)
    element_form: Optional[FormType] = field(init=False, default=None)
    attribute_form: Optional[FormType] = field(init=False, default=None)
    target_namespace: Optional[str] = field(default=None)
    default_attributes: Optional[str] = field(default=None)
    default_open_content: Optional[xsd.DefaultOpenContent] = field(default=None)

    def start(
        self,
        clazz: Type,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        self.index += 1
        self.indices.append(self.index)
        super().start(clazz, queue, objects, qname, attrs, ns_map)

    def end(
        self,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        text: Optional[str],
        tail: Optional[str],
    ) -> Any:
        """Override parent method to set element index and namespaces map."""
        item = queue[-1]
        obj: Any = super().end(queue, objects, qname, text, tail)

        self.set_index(obj, self.indices.pop())
        self.set_namespace_map(obj, getattr(item, "ns_map", None))

        return obj

    def start_schema(self, attrs: Dict):
        """Collect the schema's default form for attributes and elements for
        later usage."""

        self.element_form = attrs.get("elementFormDefault", None)
        self.attribute_form = attrs.get("attributeFormDefault", None)
        self.default_attributes = attrs.get("defaultAttributes", None)

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

    def set_schema_namespaces(self, obj: xsd.Schema):
        """Set the given schema's target namespace and add the default
        namespaces if the are missing xsi, xlink, xml, xs."""
        obj.target_namespace = obj.target_namespace or self.target_namespace

    @staticmethod
    def set_namespace_map(obj: Any, ns_map: Optional[Dict]):
        """Add common namespaces like xml, xsi, xlink if they are missing."""
        if hasattr(obj, "ns_map"):

            if ns_map:
                obj.ns_map.update(
                    {prefix: uri for prefix, uri in ns_map.items() if uri}
                )

            ns_list = obj.ns_map.values()
            ns_common = (Namespace.XS, Namespace.XSI, Namespace.XML, Namespace.XLINK)
            obj.ns_map.update(
                {ns.prefix: ns.uri for ns in ns_common if ns.uri not in ns_list}
            )

    @staticmethod
    def set_index(obj: Any, index: int):
        if hasattr(obj, "index"):
            obj.index = index

    @staticmethod
    def add_default_imports(obj: xsd.Schema):
        """Add missing imports to the standard schemas if the namespace is
        declared and."""
        imp_namespaces = [imp.namespace for imp in obj.imports]
        xsi_ns = Namespace.XSI.uri
        if xsi_ns in obj.ns_map.values() and xsi_ns not in imp_namespaces:
            obj.imports.insert(0, xsd.Import(namespace=xsi_ns))

    def resolve_schemas_locations(self, obj: xsd.Schema):
        """Resolve the locations of the schema overrides, redefines, includes
        and imports relatively to the schema location."""
        if not self.location:
            return

        obj.location = self.location
        for over in obj.overrides:
            over.location = self.resolve_path(over.schema_location)

        for red in obj.redefines:
            red.location = self.resolve_path(red.schema_location)

        for inc in obj.includes:
            inc.location = self.resolve_path(inc.schema_location)

        for imp in obj.imports:
            imp.location = self.resolve_local_path(imp.schema_location, imp.namespace)

    def resolve_path(self, location: Optional[str]) -> Optional[str]:
        """Resolve the given location string relatively the schema location
        path."""

        return urljoin(self.location, location) if self.location and location else None

    def resolve_local_path(
        self, location: Optional[str], namespace: Optional[str]
    ) -> Optional[str]:
        """Resolve the given namespace to one of the local standard schemas or
        fallback to the external file path."""

        common_ns = Namespace.get_enum(namespace)
        local_path = common_ns.location if common_ns else None
        return local_path if local_path else self.resolve_path(location)

    def end_attribute(self, obj: T):
        """Assign the schema's default form for attributes if the given
        attribute form is None."""
        if isinstance(obj, xsd.Attribute) and obj.form is None and self.attribute_form:
            obj.form = FormType(self.attribute_form)

    def end_complex_type(self, obj: T):
        """Prepend an attribute group reference when default attributes
        apply."""
        if not isinstance(obj, xsd.ComplexType):
            return

        if obj.default_attributes_apply and self.default_attributes:
            attribute_group = xsd.AttributeGroup(ref=self.default_attributes)
            obj.attribute_groups.insert(0, attribute_group)

        if not obj.open_content:
            obj.open_content = self.default_open_content

    def end_default_open_content(self, obj: T):
        """Set the instance default open content to be used later as a property
        for all extensions and restrictions."""
        if isinstance(obj, xsd.DefaultOpenContent):
            if obj.any and obj.mode == Mode.SUFFIX:
                obj.any.index = sys.maxsize

            self.default_open_content = obj

    def end_element(self, obj: T):
        """Assign the schema's default form for elements if the given element
        form is None."""
        if isinstance(obj, xsd.Element) and obj.form is None and self.element_form:
            obj.form = FormType(self.element_form)

    def end_extension(self, obj: T):
        """Set the open content if any to the given extension."""
        if isinstance(obj, xsd.Extension) and not obj.open_content:
            obj.open_content = self.default_open_content

    @classmethod
    def end_open_content(cls, obj: T):
        """Adjust the index to trick later processors into putting attributes
        derived from this open content last in classes."""
        if isinstance(obj, xsd.OpenContent) and obj.any and obj.mode == Mode.SUFFIX:
            obj.any.index = sys.maxsize

    def end_restriction(self, obj: T):
        """Set the open content if any to the given restriction."""
        if isinstance(obj, xsd.Restriction) and not obj.open_content:
            obj.open_content = self.default_open_content

    def end_schema(self, obj: T):
        """Normalize various properties for the schema and it's children."""
        if isinstance(obj, xsd.Schema):
            self.set_schema_forms(obj)
            self.set_schema_namespaces(obj)
            self.add_default_imports(obj)
            self.resolve_schemas_locations(obj)
