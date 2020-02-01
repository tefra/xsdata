import io
import pathlib
import re
from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Optional

from lxml import etree

from xsdata.models import elements as xsd
from xsdata.models.enums import EventType
from xsdata.models.enums import FormType
from xsdata.models.enums import TagType
from xsdata.models.mixins import BaseModel
from xsdata.utils.text import snake_case


@dataclass
class SchemaParser:
    """
    A simple parser to convert an xsd schema to an easy to handle data
    structure based on dataclasses.

    The parser is a dummy as possible but it will try to normalize
    certain things like apply parent properties to children.
    """

    context: etree.iterparse
    mixed_content: Optional[etree.Element] = field(default=None)
    elements: List[BaseModel] = field(default_factory=list)
    element_form: Optional[FormType] = field(init=False, default=None)
    attribute_form: Optional[FormType] = field(init=False, default=None)
    target_namespace: Optional[str] = field(default=None)

    @classmethod
    def create(cls, source: object, target_namespace=None) -> xsd.Schema:
        """A shortcut class method to initialize the parser, parse the given
        source and return the generated Schema instance."""

        ctx = etree.iterparse(source, events=(EventType.START, EventType.END))
        return cls(context=ctx, target_namespace=target_namespace).parse()

    @classmethod
    def from_file(cls, path: pathlib.Path, target_namespace=None) -> xsd.Schema:
        """A shortcut class method for file path sources."""

        if isinstance(path, str):
            path = pathlib.Path(path).resolve()

        schema = cls.create(str(path), target_namespace=target_namespace)
        schema.location = path
        return schema

    @classmethod
    def from_bytes(cls, source: bytes, target_namespace=None) -> xsd.Schema:
        """A shortcut class method for bytes source."""

        return cls.create(io.BytesIO(source), target_namespace=target_namespace)

    @classmethod
    def from_string(cls, source: str, target_namespace=None) -> xsd.Schema:
        """A shortcut class method for string source."""
        return cls.from_bytes(source.encode(), target_namespace=target_namespace)

    def parse(self) -> xsd.Schema:
        """
        Main parse procedure which depends heavily on binding data classes that
        have all the necessary attributes to match all the possible xsd
        elements and attributes.

        Elements are initialized on the start event of the parser and assigned
        to the parent element on the end event. The procedure all includes
        start/end hooks for each element type.

        Elements with no attributes and text are ignored.
        """

        methods = TagType.qnames()
        index = 0
        queue = []

        for event, elem in self.context:
            tag = methods.get(elem.tag)

            if tag is None:
                self.mixed_content = elem
                continue
            elif event == EventType.START:
                model = getattr(xsd, tag.cname)
                queue.append((model, index, len(self.elements)))
                index += 1
            elif event == EventType.END:
                model, obj_index, chd_index = queue.pop()
                if not elem.attrib and elem.text is None and model is not xsd.Schema:
                    continue

                obj = model.create(index=obj_index, **elem.attrib)
                while len(self.elements) > chd_index:
                    self.assign_to_parent(obj, self.elements.pop(chd_index))

                self.elements.append(obj)

            method_name = f"{event}_{tag.value}"
            if hasattr(self, method_name):
                getattr(self, method_name)(elem)

        if self.mixed_content is not None:
            raise NotImplementedError(f"Unsupported tag `{self.mixed_content.tag}`")

        obj = self.elements.pop()
        if not isinstance(obj, xsd.Schema):
            raise ValueError("Schema parser failed for an unknown reason.")

        return obj

    def end_documentation(self, element: etree.Element):
        obj = self.elements[-1]
        if isinstance(obj, xsd.Documentation):
            obj.text = self.get_mixed_text(element)
            self.mixed_content = None

    def end_appinfo(self, element: etree.Element):
        obj = self.elements[-1]
        if isinstance(obj, xsd.Appinfo):
            obj.text = self.get_mixed_text(element)
            self.mixed_content = None

    @classmethod
    def get_mixed_text(cls, element: etree.Element):
        """Set text attributes to elements that support well formed xml."""

        xml = etree.tostring(element, method="c14n", pretty_print=True).decode()
        start_root = xml.find(">")
        end_root = xml.rfind("<")

        return re.sub(r"\s+", " ", xml[start_root + 1 : end_root]).strip()

    def start_schema(self, element: etree.Element):
        """Collect the schema's default form for attributes and elements for
        later usage."""

        self.element_form = element.attrib.get("elementFormDefault", None)
        self.attribute_form = element.attrib.get("attributeFormDefault", None)

    def end_schema(self, element: etree.Element):
        """Collect the schema's default form for attributes and elements for
        later usage."""
        obj = self.elements[-1]
        if isinstance(obj, xsd.Schema):
            if self.element_form:
                obj.element_form_default = FormType(self.element_form)
            if self.attribute_form:
                obj.attribute_form_default = FormType(self.attribute_form)

            obj.nsmap = element.nsmap
            if obj.target_namespace is None and self.target_namespace is not None:
                obj.target_namespace = self.target_namespace

            for element in obj.elements:
                element.form = FormType.QUALIFIED
            for attribute in obj.attributes:
                attribute.form = FormType.QUALIFIED

    def end_element(self, element: etree.Element):
        """Assign the schema's default form for elements if the given element
        form is None."""
        obj = self.elements[-1]
        if isinstance(obj, xsd.Element) and obj.form is None and self.element_form:
            obj.form = FormType(self.element_form)

    def end_attribute(self, element: etree.Element):
        """Assign the schema's default form for attributes if the given
        attribute form is None."""
        obj = self.elements[-1]
        if isinstance(obj, xsd.Attribute) and obj.form is None and self.attribute_form:
            obj.form = FormType(self.attribute_form)

    def end_choice(self, element: etree.Element):
        """Elements inside a choice are by definition optional, reset their min
        occurs counter."""
        obj = self.elements[-1]
        if isinstance(obj, xsd.Choice):
            for child in obj.elements:
                child.min_occurs = 0
                if child.max_occurs is None:
                    child.max_occurs = obj.max_occurs

    def end_all(self, element: etree.Element):
        """Elements inside an all element can by definition appear at most
        once, reset their max occur counter."""

        obj = self.elements[-1]
        if isinstance(obj, xsd.All):
            for child in obj.elements:
                child.max_occurs = 1
                if child.min_occurs is None:
                    child.min_occurs = obj.min_occurs

    def end_sequence(self, element: etree.Element):
        """Elements inside a sequence inherit min|max occur counter if it is
        not set."""
        obj = self.elements[-1]
        if isinstance(obj, xsd.Sequence):
            for child in obj.elements:
                if child.min_occurs is None:
                    child.min_occurs = obj.min_occurs
                if child.max_occurs is None:
                    child.max_occurs = obj.max_occurs

    @classmethod
    def assign_to_parent(cls, parent: BaseModel, child: BaseModel):
        """
        Assign an element to its parent either in a list of same type objects
        or directly as an attribute.

        :raise ValueError: when we can't assign or append the element to the
            correct place. This practically will mean that we encountered a
            new not implemented element.
        """

        name = snake_case(child.__class__.__name__)
        if hasattr(parent, name):
            setattr(parent, name, child)
            return
        else:
            plural_name = f"{name}s"
            if hasattr(parent, plural_name):
                siblings = getattr(parent, plural_name)
                return siblings.append(child)

        raise ValueError(
            f"Class {parent.__class__.__name__} missing attribute `{name}`"
        )
