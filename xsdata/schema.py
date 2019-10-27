from typing import List

from lxml import etree

from xsdata.models import elements
from xsdata.models.elements import BaseModel
from xsdata.models.enums import Event, Tag
from xsdata.utils.text import capitalize, snake_case


class SchemaReader:
    def __init__(self, path: str):
        self.path = path
        self.documentations: dict = {}
        self.methods = {tag.qname: tag for tag in Tag}
        self.element_index = 0
        self.element_parent = Tag.SCHEMA
        self.elements: List[BaseModel] = []

    def parse(self) -> BaseModel:
        context = etree.iterparse(self.path, events=(Event.START, Event.END))
        for event, elem in context:
            tag = self.methods.get(elem.tag)
            if tag is None:
                raise NotImplementedError(
                    "Unsupported tag `{}`".format(elem.tag)
                )

            method = getattr(self, "{}_{}".format(event, tag.value), None)
            if method:
                method(elem)
            elif event == Event.START:
                builder = getattr(elements, capitalize(tag.value))
                self.elements.append(builder.from_element(elem))
            elif event == Event.END:
                element = self.elements.pop()
                if len(self.elements) > 0:
                    self.assign_to_parent(element)

        return element

    def assign_to_parent(self, element):
        name = snake_case(type(element).__name__)
        parent = self.elements[-1]

        if hasattr(parent, name):
            return setattr(parent, name, element)
        else:
            plural_name = "{}s".format(name)
            if hasattr(parent, plural_name):
                children = getattr(parent, plural_name)
                if type(children) == list:
                    return children.append(element)

        raise ValueError(
            "Class {} missing attribute `{}`".format(
                type(parent).__name__, name
            )
        )
