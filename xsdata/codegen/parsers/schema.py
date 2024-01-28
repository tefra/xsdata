import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Type, Union
from urllib.parse import urljoin

from xsdata.formats.bindings import T
from xsdata.formats.dataclass.parsers.bases import Parsed
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.xml import UserXmlParser
from xsdata.models import xsd
from xsdata.models.enums import FormType, Mode, Namespace
from xsdata.models.mixins import ElementBase

OPEN_CONTENT_ELEMENT = Union[xsd.ComplexType, xsd.Restriction, xsd.Extension]


@dataclass
class SchemaParser(UserXmlParser):
    """Xml schema definition parser.

    Apply implied rules, set indexes, resolve
    location paths...

    Args:
        location: The schema location uri
        target_namespace: The schema target namespace

    Attributes:
        index: The current element index
        indices: The child element indices
        element_form: The schema element form
        attribute_form: The schema attribute form
        default_attributes: The schema default attributes
        default_open_content: The schema default open content
    """

    location: Optional[str] = field(default=None)
    target_namespace: Optional[str] = field(default=None)
    index: int = field(default_factory=int, init=False)
    indices: List[int] = field(default_factory=list, init=False)
    element_form: Optional[str] = field(default=None, init=False)
    attribute_form: Optional[str] = field(default=None, init=False)
    default_attributes: Optional[str] = field(default=None, init=False)
    default_open_content: Optional[xsd.DefaultOpenContent] = field(
        default=None, init=False
    )

    def start(
        self,
        clazz: Optional[Type[T]],
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """Build and queue the XmlNode for the starting element.

        Override to set the current element index and append it in
        child element indices.

        Args:
            clazz: The target class type, auto locate if omitted
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
        """
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
        """Parse the last xml node and bind any intermediate objects.

        Override to set the xsd model index and ns map.

        Args:
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            text: The element text content
            tail: The element tail content

        Returns:
            Whether the binding process was successful.
        """
        item = queue[-1]
        super().end(queue, objects, qname, text, tail)

        obj = objects[-1][1]
        self.set_index(obj, self.indices.pop())
        self.set_namespace_map(obj, getattr(item, "ns_map", None))

        return obj

    def start_schema(self, attrs: Dict[str, str]):
        """Start schema element entrypoint.

        Store the element/attribute default forms and the
        default attributes, for later processing.

        Args:
            attrs: The element attributes

        """
        self.element_form = attrs.get("elementFormDefault")
        self.attribute_form = attrs.get("attributeFormDefault")
        self.default_attributes = attrs.get("defaultAttributes")

    def end_schema(self, obj: T):
        """End schema element entrypoint.

        Normalize various properties for the schema and it's children.

        Args:
            obj: The xsd schema instance.
        """
        if isinstance(obj, xsd.Schema):
            self.set_schema_forms(obj)
            self.set_schema_namespaces(obj)
            self.add_default_imports(obj)
            self.resolve_schemas_locations(obj)
            self.reset_element_occurs(obj)

    def end_attribute(self, obj: T):
        """End attribute element entrypoint.

        Assign the schema's default form in the attribute instance,
        if it doesn't define its own.

        Args:
            obj: The xsd attribute instance

        """
        if isinstance(obj, xsd.Attribute) and obj.form is None and self.attribute_form:
            obj.form = FormType(self.attribute_form)

    def end_complex_type(self, obj: T):
        """End complex type element entrypoint.

        Post parsing processor to apply default open content and attributes if
        applicable.

        Default open content doesn't apply if the current complex type
        has one of complex content, simple content or has its own open
        content.

        Args:
            obj: The xsd complex type instance
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
        """End default open content element entrypoint.

        If the open content element mode is suffix, adjust
        the index to trick later processors into putting attrs
        derived from this open content last in the generated classes.

        Store the obj for later processing.

        Args:
            obj: The xsd default open content instance
        .
        """
        if isinstance(obj, xsd.DefaultOpenContent):
            if obj.any and obj.mode == Mode.SUFFIX:
                obj.any.index = sys.maxsize

            self.default_open_content = obj

    def end_element(self, obj: T):
        """End element entrypoint.

        Assign the schema's default form in the element instance,
        if it doesn't define its own.

        Args:
            obj: The xsd element instance
        """
        if isinstance(obj, xsd.Element) and obj.form is None and self.element_form:
            obj.form = FormType(self.element_form)

    def end_extension(self, obj: T):
        """End extension element entrypoint.

        Assign the schema's default open content in the extension instance,
        if it doesn't define its own.

        Args:
            obj: The xsd extension instance
        """
        if isinstance(obj, xsd.Extension) and not obj.open_content:
            obj.open_content = self.default_open_content

    @classmethod
    def end_open_content(cls, obj: T):
        """End open content element entrypoint.

        If the open content element mode is suffix, adjust
        the index to trick later processors into putting attrs
        derived from this open content last in the generated classes.

        Args:
            obj: The xsd open content instance

        """
        if isinstance(obj, xsd.OpenContent) and obj.any and obj.mode == Mode.SUFFIX:
            obj.any.index = sys.maxsize

    def end_restriction(self, obj: T):
        """End restriction element entrypoint.

        Assign the schema's default open content in the restriction instance,
        if it doesn't define its own.

        Args:
            obj: The xsd restriction instance
        """
        if isinstance(obj, xsd.Restriction) and not obj.open_content:
            obj.open_content = self.default_open_content

    def set_schema_forms(self, obj: xsd.Schema):
        """Cascade schema forms to elements and attributes.

        Args:
            obj: The xsd schema instance
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
        """Set the schema target namespace.

        If the schema was imported and doesn't have a target namespace,
        it automatically inherits the parent schema target namespace.

        Args:
            obj: The xsd schema instance
        """
        obj.target_namespace = obj.target_namespace or self.target_namespace

    def resolve_schemas_locations(self, obj: xsd.Schema):
        """Resolve the location attributes of the schema.

        This method covers relative paths and implied schema
        locations to common namespaces like xsi, xlink.

        Schema elements with location attribute:
            - override
            - redefines
            - include
            - import

        Args:
            obj: The xsd schema instance
        """
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
        """Resolve the given location string.

        Use the parser location attribute as the base uri.

        Args:
            location: The location uri

        Returns:
            The resolved location or None if it was not resolved
        """
        return urljoin(self.location, location) if self.location and location else None

    def resolve_local_path(
        self,
        location: Optional[str],
        namespace: Optional[str],
    ) -> Optional[str]:
        """Resolve the given namespace to one of the local standard schemas.

        w3.org protects against fetching common schemas not from a browser,
        instead we use the local xsdata copies.

        Args:
            location: The schema location
            namespace: The schema namespace

        Returns:
            The local path or the absolute remote uri.
        """
        common_ns = Namespace.get_enum(namespace)
        local_path = common_ns.location if common_ns else None

        if local_path and (not location or location.find("w3.org/") > 0):
            return local_path

        return self.resolve_path(location)

    @classmethod
    def has_elements(cls, obj: ElementBase) -> bool:
        """Helper function to check if instance has children.

        Valid children: xs:element, xs:any, xs:group.

        Args:
            obj: The element base instance

        Returns:
            The bool result.

        """
        accepted_types = (xsd.Element, xsd.Any, xsd.Group)
        return any(
            isinstance(child, accepted_types) or cls.has_elements(child)
            for child in obj.children()
        )

    @classmethod
    def set_namespace_map(cls, obj: Any, ns_map: Optional[Dict]):
        """Add common namespaces like xml, xsi, xlink if they are missing.

        These prefixes are implied and we need to support them.

        Args:
            obj: A xsd model instance
            ns_map: The namespace prefix-URI map
        """
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
        """Helper method to set an object's index.

        Args:
            obj: A xsd model instance
            index: The index number
        """
        if hasattr(obj, "index"):
            obj.index = index

    @classmethod
    def add_default_imports(cls, obj: xsd.Schema):
        """Add missing imports to the standard schemas.

        We might need to generate the classes from these
        common schemas, so add these implied imports.

        Args:
            obj: The xsd schema instance
        """
        imp_namespaces = [imp.namespace for imp in obj.imports]
        xsi_ns = Namespace.XSI.uri
        if xsi_ns in obj.ns_map.values() and xsi_ns not in imp_namespaces:
            obj.imports.insert(0, xsd.Import(namespace=xsi_ns))

    @classmethod
    def reset_element_occurs(cls, obj: xsd.Schema):
        """Reset the root elements occurs restrictions.

        The root elements don't get those.

        Args:
            obj: The xsd schema instance
        """
        for element in obj.elements:
            element.min_occurs = None
            element.max_occurs = None
