import json
from dataclasses import dataclass, is_dataclass
from io import BytesIO
from typing import Any, Dict, List, Optional, Type

from lxml.etree import Element, QName, iterparse

from xsdata.formats.dataclass.mixins import Field, ModelInspect
from xsdata.formats.mixins import AbstractParser
from xsdata.models.enums import EventType


@dataclass
class JsonParser(AbstractParser, ModelInspect):
    def parse(self, source: BytesIO, clazz: Type) -> Type:
        """Parse the JSON input stream and return the resulting object tree."""
        ctx = json.load(source)
        return self.parse_context(ctx, clazz)

    def parse_context(self, data: Dict, model: Type) -> Type:
        """
        Recursively build the given model from the input dict data.

        :raise TypeError: When parsing fails for any reason
        """
        params = {}

        if isinstance(data, list) and len(data) == 1:
            data = data[0]

        for field in self.fields(model):
            value = self.parse_value(data, field)

            if not value:
                params[field.name] = value
            elif is_dataclass(field.type):
                params[field.name] = (
                    [self.parse_context(val, field.type) for val in value]
                    if field.is_list
                    else self.parse_context(value, field.type)
                )
            else:
                params[field.name] = (
                    list(map(field.type, value))
                    if field.is_list
                    else field.type(value)
                )
        try:
            return model(**params)
        except Exception:
            raise TypeError("Parsing failed")

    @staticmethod
    def parse_value(data: Dict, field: Field):
        """Find the field value in the given dictionary or return the default
        field value."""
        if field.local_name in data:
            value = data[field.local_name]
            if field.is_list and type(value) is not list:
                value = [value]
        elif callable(field.default):
            value = field.default()
        else:
            value = field.default

        return value


@dataclass
class XmlParser(AbstractParser, ModelInspect):
    def parse(self, source: BytesIO, clazz: Type) -> Type:
        """Parse the XML input stream and return the resulting object tree."""
        ctx = iterparse(source=source, events=(EventType.START, EventType.END))
        return self.parse_context(ctx, clazz)

    def parse_context(self, context: iterparse, clazz: Type) -> Type:
        """Build the given model from the iterparse event data."""
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
