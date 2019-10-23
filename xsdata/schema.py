from typing import Dict, List

from lxml import etree

from xsdata.builders import Documentation, Element
from xsdata.enums import Event, Tag


def stripns(text: str):
    try:
        namespace, text = text.split("}", 1)
        return text
    except ValueError:
        return text


class SchemaReader:
    def __init__(self, path: str):
        self.path = path
        self.documentations: dict = {}
        self.methods = {tag.qname: tag for tag in Tag}
        self.element_index = 0
        self.element_parent = Tag.SCHEMA
        self.elements: Dict[Tag, List] = {
            tag.value: [] for tag in Tag.element_parents()
        }

    def parse(self):

        context = etree.iterparse(self.path, events=(Event.START, Event.END))
        for event, elem in context:
            tag = self.methods.get(elem.tag)
            if tag is None:
                raise NotImplementedError(
                    "Unsupported tag `{}`".format(elem.tag)
                )

            method = getattr(self, "{}_{}".format(event, tag.value), None)

            if event == Event.START and tag in Tag.element_parents():
                self.start_element_parent(tag)

            if method:
                method(elem)
            else:
                print("Skipping event: {} {}".format(event, elem.tag))

    def start_element_parent(self, tag: Tag):
        self.elements[tag] = []
        self.element_parent = tag

    def start_element(self, element):
        self.element_index += 1

    def end_element(self, element):
        attrs = self.clean_element_attrs(element)

        if "block" in attrs:
            raise NotImplementedError("Unsupported element attribute `block`")
        if "final" in attrs:
            raise NotImplementedError("Unsupported element attribute `final`")

        self.push_element(
            Element(
                id=attrs.get("id"),
                name=attrs.get("name"),
                ref=attrs.get("ref"),
                type=attrs.get("type"),
                substitution_group=attrs.get("substitutionGroup"),
                default_value=attrs.get("default"),
                fixed_value=attrs.get("fixed"),
                form=attrs.get("form"),
                min_occurs=int(attrs.get("minOccurs", 1)),
                max_occurs=int(attrs.get("maxOccurs", 0)),
                nillable=attrs.get("nillable", False) == "true",
                abstract=attrs.get("abstract", False) == "true",
                nsmap=element.nsmap,
                prefix=element.prefix,
                documentation=self.documentations.pop(
                    self.element_index, None
                ),
            )
        )

    def end_documentation(self, element):
        attrs = self.clean_element_attrs(element)
        self.documentations[self.element_index] = Documentation(
            lang=attrs.get("lang"),
            source=attrs.get("source"),
            text=element.text,
            nsmap=element.nsmap,
            prefix=element.prefix,
        )

    def push_element(self, element: Element):
        self.elements[self.element_parent].append(element)

    def clean_element_attrs(self, element):
        return {stripns(key): value for key, value in element.attrib.items()}


if __name__ == "__main__":
    import sys

    schema = SchemaReader(sys.argv[1])
    result = schema.parse()
