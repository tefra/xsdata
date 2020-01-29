import io
import pathlib
import re
from dataclasses import dataclass, field
from typing import List, Optional

from lxml import etree

from xsdata.models import elements
from xsdata.models.elements import (
    All,
    Attribute,
    Choice,
    Element,
    Schema,
    Sequence,
)
from xsdata.models.enums import DataType, EventType, FormType, TagType
from xsdata.models.mixins import BaseModel, ElementBase
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
    target_namespace: Optional[str] = field(default=None)

    @classmethod
    def create(cls, source: object, target_namespace=None) -> Schema:
        """A shortcut class method to initialize the parser, parse the given
        source and return the generated Schema instance."""

        ctx = etree.iterparse(source, events=(EventType.START, EventType.END))
        return cls(context=ctx, target_namespace=target_namespace).parse()

    @classmethod
    def from_file(cls, path: pathlib.Path, target_namespace=None) -> Schema:
        """A shortcut class method for file path sources."""

        if isinstance(path, str):
            path = pathlib.Path(path).resolve()

        schema = cls.create(str(path), target_namespace=target_namespace)
        schema.location = path
        return schema

    @classmethod
    def from_bytes(cls, source: bytes, target_namespace=None) -> Schema:
        """A shortcut class method for bytes source."""

        return cls.create(
            io.BytesIO(source), target_namespace=target_namespace
        )

    @classmethod
    def from_string(cls, source: str, target_namespace=None) -> Schema:
        """A shortcut class method for string source."""
        return cls.from_bytes(
            source.encode(), target_namespace=target_namespace
        )

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
        mixed = None
        for event, elem in self.context:
            tag = methods.get(elem.tag)
            if tag is None:
                mixed = elem
                continue

            if event == EventType.START:
                if mixed is not None:
                    raise NotImplementedError(f"Unsupported tag `{elem.tag}`")

                builder = getattr(elements, tag.cname)
                element = builder.from_element(elem, index=index)
                self.elements.append(element)
                index += 1
            elif event == EventType.END:
                element = self.elements.pop()
                self.set_text(element, elem, mixed)
                if mixed is not None:
                    mixed = None
                if not elem.attrib and elem.text is None:
                    continue
                if self.elements:
                    self.assign_to_parent(element, elem.prefix)

            method_name = f"{event}_{tag.value}"
            if hasattr(self, method_name):
                getattr(self, method_name)(element, elem)

        return element

    @classmethod
    def set_text(
        cls,
        obj: ElementBase,
        element: etree.Element,
        mixed: Optional[etree.Element],
    ):
        """Set text attributes to elements that support well formed xml."""

        if not hasattr(obj, "text"):  # It's ok not to have text attribute
            if mixed is None:  # It's not ok if the mixed arguments is not None
                return
            raise NotImplementedError(f"Unsupported tag `{mixed.tag}`")

        xml = etree.tostring(
            element, method="c14n", pretty_print=True
        ).decode()
        start_root = xml.find(">")
        end_root = xml.rfind("<")

        clean_text = re.sub(
            r"\s+", " ", xml[start_root + 1 : end_root]
        ).strip()
        setattr(obj, "text", clean_text)

    def start_schema(self, obj: Schema, element: etree.Element):
        """Collect the schema's default form for attributes and elements for
        later usage."""

        if isinstance(obj, Schema):
            self.element_form = obj.element_form_default
            self.attribute_form = obj.attribute_form_default

            obj.nsmap = element.nsmap
            if obj.target_namespace is None:
                if self.target_namespace is not None:
                    obj.target_namespace = self.target_namespace

    @classmethod
    def end_schema(cls, obj: Schema, *args):
        """Root elements and attributes are always qualified."""
        if isinstance(obj, Schema):
            for element in obj.elements:
                element.form = FormType.QUALIFIED
            for attribute in obj.attributes:
                attribute.form = FormType.QUALIFIED

    def start_element(self, obj: Element, *args):
        """Assign the schema's default form for elements if the given element
        form is None."""

        if isinstance(obj, Element) and obj.form is None:
            obj.form = self.element_form

    def start_attribute(self, obj: Attribute, *args):
        """Assign the schema's default form for attributes if the given
        attribute form is None."""

        if isinstance(obj, Attribute) and obj.form is None:
            obj.form = self.attribute_form

    @classmethod
    def end_choice(cls, obj: Choice, *args):
        """Elements inside a choice are by definition optional, reset their min
        occurs counter."""

        if isinstance(obj, Choice):
            for child in obj.elements:
                child.min_occurs = 0
                if child.max_occurs is None:
                    child.max_occurs = obj.max_occurs

    @classmethod
    def end_all(cls, obj: All, *args):
        """Elements inside an all element can by definition appear at most
        once, reset their max occur counter."""

        if isinstance(obj, All):
            for child in obj.elements:
                child.max_occurs = 1
                if child.min_occurs is None:
                    child.min_occurs = obj.min_occurs

    @classmethod
    def end_sequence(cls, obj: Sequence, *args):
        """Elements inside a sequence inherit min|max occur counter if it is
        not set."""
        if isinstance(obj, Sequence):
            for child in obj.elements:
                if child.min_occurs is None:
                    child.min_occurs = obj.min_occurs
                if child.max_occurs is None:
                    child.max_occurs = obj.max_occurs

    def assign_to_parent(self, element, prefix):
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
                id = f"{prefix}:{DataType.ID.code}"
                if getattr(element, "type", "") == id:
                    for sibling in siblings:
                        if getattr(sibling, "type", "") == id:
                            raise ValueError(f"Duplicated ID: `{element}`")

                return siblings.append(element)

        raise ValueError(
            "Class {} missing attribute `{}`".format(
                type(parent).__name__, name
            )
        )
