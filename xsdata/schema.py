from typing import Dict, List

from lxml import etree

from xsdata.builders import Documentation, Element
from xsdata.enums import Event, Tag


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
        if "block" in element.attrib:
            raise NotImplementedError("Unsupported element attribute `block`")
        if "final" in element.attrib:
            raise NotImplementedError("Unsupported element attribute `final`")

        el = Element.from_element(element)
        el.documentation = self.documentations.pop(self.element_index, None)
        self.push_element(Element.from_element(element))

    def end_documentation(self, element):
        doc = Documentation.from_element(element)
        doc.text = element.text
        self.documentations[self.element_index] = doc

    def push_element(self, element: Element):
        self.elements[self.element_parent].append(element)


if __name__ == "__main__":
    import sys

    schema = SchemaReader(sys.argv[1])
    result = schema.parse()
