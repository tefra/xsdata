import sys
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import Union
from urllib.parse import urljoin

from xsdata.formats.bindings import T
from xsdata.formats.dataclass.parsers.bases import Parsed
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.xml import UserXmlParser
from xsdata.models import xsd
from xsdata.models.enums import FormType
from xsdata.models.enums import Mode
from xsdata.models.enums import Namespace
from xsdata.models.mixins import ElementBase

OPEN_CONTENT_ELEMENT = Union[xsd.ComplexType, xsd.Restriction, xsd.Extension]


@dataclass
class SchemaParser(UserXmlParser):
    """
    A simple parser to convert an xsd schema to an easy to handle data
    structure based on dataclasses.

    The parser is as a dummy as possible, but it will try to normalize
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
        clazz: Optional[Type[T]],
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
        super().end(queue, objects, qname, text, tail)

        obj = objects[-1][1]
        self.set_index(obj, self.indices.pop())
        self.set_namespace_map(obj, getattr(item, "ns_map", None))

        return obj

    def start_schema(self, attrs: Dict):
        """Collect the schema's default form for attributes and elements for
        later usage."""

        self.element_form = attrs.get("elementFormDefault", None)
        self.attribute_form = attrs.get("attributeFormDefault", None)
        self.default_attributes = attrs.get("defaultAttributes", None)

    def end_schema(self, obj: T):
        """Normalize various properties for the schema and it's children."""
        if isinstance(obj, xsd.Schema):
            self.set_schema_forms(obj)
            self.set_schema_namespaces(obj)
            self.add_default_imports(obj)
            self.resolve_schemas_locations(obj)
            self.reset_element_occurs(obj)

    def end_attribute(self, obj: T):
        """Assign the schema's default form for attributes if the given
        attribute form is None."""
        if isinstance(obj, xsd.Attribute) and obj.form is None and self.attribute_form:
            obj.form = FormType(self.attribute_form)

    def end_complex_type(self, obj: T):
        """
        Post parsing processor to apply default open content and attributes if
        applicable.

        Default open content doesn't apply if the current complex type
        has one of complex content, simple content or has its own open
        content.
        """
        if not isinstance(obj, xsd.ComplexType):
            return

        if obj.default_attributes_apply and self.default_attributes:
            attribute_group = xsd.AttributeGroup(ref=self.default_attributes)
            obj.attribute_groups.insert(0, attribute_group)

        if (
            obj.simple_content
            or obj.complex_content
            or obj.open_content
            or not self.default_open_content
        ):
            return

        if self.default_open_content.applies_to_empty or self.has_elements(obj):
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

        if local_path and (not location or location.find("w3.org/") > 0):
            return local_path

        return self.resolve_path(location)

    @classmethod
    def has_elements(cls, obj: ElementBase) -> bool:
        accepted_types = (xsd.Element, xsd.Any, xsd.Group)
        return any(
            isinstance(child, accepted_types) or cls.has_elements(child)
            for child in obj.children()
        )

    @classmethod
    def set_namespace_map(cls, obj: Any, ns_map: Optional[Dict]):
        """Add common namespaces like xml, xsi, xlink if they are missing."""
        if hasattr(obj, "ns_map"):
            if ns_map:
                obj.ns_map.update(
                    {prefix: uri for prefix, uri in ns_map.items() if uri}
                )

            ns_list = obj.ns_map.values()
            obj.ns_map.update(
                {
                    ns.prefix: ns.uri
                    for ns in Namespace.common()
                    if ns.uri not in ns_list
                }
            )

    @classmethod
    def set_index(cls, obj: Any, index: int):
        if hasattr(obj, "index"):
            obj.index = index

    @classmethod
    def add_default_imports(cls, obj: xsd.Schema):
        """Add missing imports to the standard schemas if the namespace is
        declared and."""
        imp_namespaces = [imp.namespace for imp in obj.imports]
        xsi_ns = Namespace.XSI.uri
        if xsi_ns in obj.ns_map.values() and xsi_ns not in imp_namespaces:
            obj.imports.insert(0, xsd.Import(namespace=xsi_ns))

    @classmethod
    def reset_element_occurs(cls, obj: xsd.Schema):
        for element in obj.elements:
            element.min_occurs = None
            element.max_occurs = None
