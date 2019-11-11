import pathlib
from dataclasses import dataclass, field
from typing import List

from lxml import etree

from xsdata.models import elements
from xsdata.models.elements import BaseModel, Schema
from xsdata.models.enums import Event, Tag
from xsdata.utils.text import capitalize, snake_case


@dataclass
class SchemaParser:
    path: pathlib.Path
    elements: List[BaseModel] = field(default_factory=list)
    methods: dict = field(init=False)

    def __post_init__(self):
        self.methods = {tag.qname: tag for tag in Tag}
        if isinstance(self.path, str):
            self.path = pathlib.Path(self.path).resolve()

    def parse(self) -> Schema:
        context = etree.iterparse(
            str(self.path), events=(Event.START, Event.END)
        )
        for event, elem in context:
            tag = self.methods.get(elem.tag)
            if tag is None:
                raise NotImplementedError(
                    "Unsupported tag `{}`".format(elem.tag)
                )

            if event == Event.START:
                builder = getattr(elements, capitalize(tag.value))
                element = builder.from_element(elem)
                self.elements.append(element)
            elif event == Event.END:
                element = self.elements.pop()
                if len(elem.attrib) == 0 and elem.text is None:
                    continue
                if len(self.elements) > 0:
                    self.assign_to_parent(element)

            method = getattr(self, "{}_{}".format(event, tag.value), None)
            if method:
                method(element, elem)

        return element

    def end_schema(self, element, *args):
        assert isinstance(element, Schema)
        element.location = self.path

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
