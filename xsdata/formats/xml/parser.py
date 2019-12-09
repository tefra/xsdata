import io
import pathlib
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Type

from lxml.etree import Element, QName, iterparse

from xsdata.formats.inspect import Field, ModelInspect
from xsdata.models.enums import EventType


@dataclass
class XmlParser(ModelInspect):
    def from_path(self, path: pathlib.Path, clazz: Type) -> Type:
        """A shortcut class method for file path source."""
        if isinstance(path, str):
            path = pathlib.Path(path).resolve()

        return self.parse(str(path), clazz)

    def from_string(self, source: str, clazz: Type) -> Type:
        """A shortcut class method for str source."""
        return self.from_bytes(source.encode(), clazz)

    def from_bytes(self, source: bytes, clazz: Type) -> Type:
        """A shortcut class method for bytes source."""
        return self.parse(io.BytesIO(source), clazz)

    def parse(self, source: object, clazz: Type) -> Type:
        """Create an iterparse instance with only start/end events and pass the
        ball the the context parser."""
        ctx = iterparse(source=source, events=(EventType.START, EventType.END))
        return self.parse_context(ctx, clazz)

    def parse_context(self, context: iterparse, clazz: Type) -> Type:
        """Run the iterator and build the objects tree according to the given
        class."""
        _, root = next(context)
        namespace = self.class_meta(clazz).namespace
        queue = [self.class_ns_fields(clazz, namespace)]
        objects = [self.build_object(clazz, root)]

        for event, element in context:
            if event == EventType.START:
                field = self.find_field(queue, namespace, element)
                obj = self.build_object_from_field(field, element)
                objects.append(obj)
            elif event == EventType.END:
                obj = self.end_element(objects, queue, element)
                element.clear()

        return obj

    def find_field(
        self, queue: List[Dict], namespace: Optional[str], element: Element,
    ) -> Field:
        """
        Find the current field from the fields queue.

        If the next field is also a dataclass append its fields map to
        the queue for the next event
        """
        field = queue[-1][element.tag]
        if field.is_dataclass:
            class_fields = self.class_ns_fields(field.type, namespace)
            queue.append(class_fields)

        return field

    def build_object_from_field(self, field: Field, element: Element) -> Type:
        """Bind the current element to a dataclass or simply parse its text
        value."""
        if not field.is_dataclass:
            return self.parse_value(field.type, element.text)

        return self.build_object(field.type, element)

    def build_object(self, clazz: Type, element: Element) -> Type:
        """Create a new class instance by the current element attributes and
        text."""
        params = {}
        for f in self.fields(clazz):
            if f.name == "value" and element.text:
                params[f.name] = self.parse_value(f.type, element.text)
            elif f.local_name in element.attrib:
                params[f.name] = self.parse_value(
                    f.type, element.attrib[f.local_name]
                )

        return clazz(**params)

    def end_element(
        self, objects: List[Type], queue: List[Dict], element: Element
    ) -> Type:
        """
        Finalize and return the last item of the objects list.

        Steps:
           * Pop the last item of the objects
           * If the object is a dataclass pop the fields queue which should be
             the current object's fields map
           * If the object is not the last in the list assign or append it
             to the correct parent field
        """
        obj = objects.pop()
        if self.is_dataclass(obj):
            queue.pop()

        if len(objects):
            field = queue[-1][element.tag]
            if field.is_list:
                getattr(objects[-1], field.name).append(obj)
            else:
                setattr(objects[-1], field.name, obj)

        return obj

    def class_ns_fields(
        self, clazz: Type, namespace: Optional[str]
    ) -> Dict[str, Field]:
        """Returns the given class fields indexed by their namespace qualified
        names for easier match."""
        return {
            QName(f.namespace or namespace, f.local_name).text: f
            for f in self.fields(clazz)
        }

    @staticmethod
    def parse_value(tp: Type, value: Any) -> Any:
        """Convert xml string values to python primite types."""
        return value == "true" if tp is bool else tp(value)
