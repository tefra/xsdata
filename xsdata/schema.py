from dataclasses import asdict
from pprint import pprint
from typing import List

import stringcase
from lxml import etree

from xsdata import builders
from xsdata.builders import Builder
from xsdata.enums import Event, Tag


class SchemaReader:
    def __init__(self, path: str):
        self.path = path
        self.documentations: dict = {}
        self.methods = {tag.qname: tag for tag in Tag}
        self.element_index = 0
        self.element_parent = Tag.SCHEMA
        self.elements: List[Builder] = []

    def parse(self):
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
                builder = getattr(builders, stringcase.capitalcase(tag.value))
                self.elements.append(builder.from_element(elem))
            elif event == Event.END:
                element = self.elements.pop()
                if len(self.elements) == 0:
                    return element
                self.assign_to_parent(element)

        return self.elements

    def assign_to_parent(self, element):
        name = stringcase.snakecase(type(element).__name__)
        parent = self.elements[-1]

        if hasattr(parent, name):
            setattr(parent, name, element)
        else:
            plural_name = "{}s".format(name)
            if hasattr(parent, plural_name):
                children = getattr(parent, plural_name)
                if type(children) == list:
                    children.append(element)
                else:
                    raise ValueError(
                        "Property `{}::{}` is not a list".format(
                            type(parent).__name__, plural_name
                        )
                    )


if __name__ == "__main__":
    import sys

    schema = SchemaReader(sys.argv[1])
    result = schema.parse()
    pprint(asdict(result))
