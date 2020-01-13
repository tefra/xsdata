import io
import pathlib
from dataclasses import dataclass, field
from typing import List, Optional

from lxml import etree

from xsdata.models import elements
from xsdata.models.elements import Attribute, Choice, Element, Schema
from xsdata.models.enums import EventType, FormType, TagType, XSDType
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
    elements: List[BaseModel] = field(default_factory=list)
    element_form: Optional[FormType] = field(init=False, default=None)
    attribute_form: Optional[FormType] = field(init=False, default=None)

    @classmethod
    def create(cls, source: object) -> Schema:
        """A shortcut class method to initialize the parser, parse the given
        source and return the generated Schema instance."""

        ctx = etree.iterparse(source, events=(EventType.START, EventType.END))
        return cls(context=ctx).parse()

    @classmethod
    def from_file(cls, path: pathlib.Path) -> Schema:
        """A shortcut class method for file path sources."""

        if isinstance(path, str):
            path = pathlib.Path(path).resolve()

        schema = cls.create(str(path))
        schema.location = path
        return schema

    @classmethod
    def from_bytes(cls, source: bytes) -> Schema:
        """A shortcut class method for bytes source."""

        return cls.create(io.BytesIO(source))

    @classmethod
    def from_string(cls, source: str) -> Schema:
        """A shortcut class method for string source."""
        return cls.from_bytes(source=source.encode())

    def parse(self) -> Schema:
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
        for event, elem in self.context:
            tag = methods.get(elem.tag)
            if tag is None:
                raise NotImplementedError(
                    "Unsupported tag `{}`".format(elem.tag)
                )

            if event == EventType.START:
                builder = getattr(elements, tag.cname)
                element = builder.from_element(elem, index=index)
                self.elements.append(element)
                index += 1
            elif event == EventType.END:
                element = self.elements.pop()
                if len(elem.attrib) == 0 and elem.text is None:
                    continue
                if len(self.elements) > 0:
                    self.assign_to_parent(element)

            method_name = f"{event}_{tag.value}"
            if hasattr(self, method_name):
                getattr(self, method_name)(element, elem)

        return element

    def start_schema(self, schema: Schema, *args):
        """Collect the schema's default form for attributes and elements for
        later usage."""

        if isinstance(schema, Schema):
            self.element_form = schema.element_form_default
            self.attribute_form = schema.attribute_form_default

    def start_element(self, element: Element, *args):
        """Assign the schema's default form for elements if the given element
        form is None."""

        if isinstance(element, Element) and element.form is None:
            element.form = self.element_form

    def start_attribute(self, attribute: Attribute, *args):
        """Assign the schema's default form for attributes if the given
        attribute form is None."""

        if isinstance(attribute, Attribute) and attribute.form is None:
            attribute.form = self.attribute_form

    def end_choice(self, choice: Choice, *args):
        """Elements inside a choice are by definition optional, reset their min
        occurs counter."""

        if isinstance(choice, Choice):
            for child in choice.elements:
                child.min_occurs = 0

    def assign_to_parent(self, element):
        """
        Assign an element to its parent either in a list of same type objects
        or directly as an attribute.

        :raise ValueError when we can't assign or append the element to the
            correct place. This practically will mean that we encountered a
            new not implemented element.
        """

        name = snake_case(type(element).__name__)
        parent = self.elements[-1]

        if hasattr(parent, name):
            return setattr(parent, name, element)
        else:
            plural_name = "{}s".format(name)
            if hasattr(parent, plural_name):
                siblings = getattr(parent, plural_name)
                if getattr(element, "type", "") == XSDType.ID.code:
                    for sibling in siblings:
                        if getattr(sibling, "type", "") == XSDType.ID.code:
                            raise ValueError(f"Duplicated ID: `{element}`")

                return siblings.append(element)

        raise ValueError(
            "Class {} missing attribute `{}`".format(
                type(parent).__name__, name
            )
        )
