import json
from dataclasses import dataclass
from io import BytesIO
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from lxml.etree import Element
from lxml.etree import iterparse
from lxml.etree import QName

from xsdata.formats.dataclass.mixins import Field
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.dataclass.mixins import QueueItem
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
            elif field.is_dataclass:
                params[field.name] = (
                    [self.parse_context(val, field.type) for val in value]
                    if field.is_list
                    else self.parse_context(value, field.type)
                )
            else:
                params[field.name] = (
                    list(map(field.type, value)) if field.is_list else field.type(value)
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
            if field.is_list and not isinstance(value, list):
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

        meta = self.class_meta(clazz)
        queue = []
        stack: List[Tuple[QName, Any]] = []
        _, root = next(context)
        qname = QName(meta.namespace, meta.name)

        fields = self.class_ns_fields(clazz, meta.namespace)
        item = QueueItem(qname=qname, clazz=clazz, fields=fields)
        queue.append(item)

        for event, element in context:
            qname = element.tag
            item = queue[-1]

            if event == EventType.START:
                field = item.fields[qname]
                fields = self.class_ns_fields(field.type, meta.namespace)
                queue.append(
                    QueueItem(
                        qname=qname, clazz=field.type, fields=fields, index=len(stack)
                    )
                )
            elif event == EventType.END:
                item = queue.pop()
                stack.append(self.build_object(item, element, stack))
                element.clear()

        if len(queue) > 0 or len(stack) != 1:
            raise AssertionError("Parsing failed with residual metadata")

        _, obj = stack.pop()

        return obj

    def build_object(
        self, item: QueueItem, element: Element, stack: List[Tuple[QName, Any]]
    ) -> Tuple[QName, Any]:
        """
        Objectify current element by the item clazz type.

        If the clazz is a dataclass build the objects tree and parse attributes from
        the element. Otherwise parse the elements text value

        :returns Tuple: The qualified object name and the object
        """
        if self.is_dataclass(item.clazz):
            children = self.fetch_class_children(item, stack)
            attributes = self.parse_element_attributes(item, element)
            obj = item.clazz(**children, **attributes)
        else:
            obj = self.parse_value(item.clazz, element.text)

        return item.qname, obj

    @staticmethod
    def fetch_class_children(
        item: QueueItem, stack: List[Tuple[QName, Any]]
    ) -> Dict[str, Any]:
        """
        Return a dictionary of qualified object names and objects for the given
        queue item.

        The object can be a primitive, another dataclass, or a list of
        either primitive values and dataclasses.
        """
        params: Dict[str, Any] = dict()
        while len(stack) > item.index:
            qname, value = stack.pop(item.index)
            field = item.fields[qname]
            if field.is_list:
                if field.name not in params:
                    params[field.name] = [value]
                else:
                    params[field.name].append(value)
            else:
                params[field.name] = value
        return params

    def parse_element_attributes(
        self, item: QueueItem, element: Element
    ) -> Dict[str, Any]:
        """Parse the given element's attributes and text value if any and
        return a dictionary of field names and values."""
        params: Dict[str, Any] = dict()
        for qname, field in item.fields.items():
            if qname in element.attrib:
                params[field.name] = self.parse_value(field.type, element.attrib[qname])
            elif field.is_text and element.text:
                params[field.name] = self.parse_value(field.type, element.text)

        return params

    def class_ns_fields(
        self, clazz: Type, namespace: Optional[str]
    ) -> Dict[str, Field]:
        """Returns the given class fields indexed by their namespace qualified
        names for easier match."""

        res: Dict = dict()
        if not self.is_dataclass(clazz):
            return res

        for field in self.fields(clazz):
            if field.is_element and field.namespace == "":
                res[field.local_name] = field
            if field.is_attribute and field.namespace is None:
                res[field.local_name] = field
            else:
                qname = QName(field.namespace or namespace, field.local_name)
                res[qname.text] = field
        return res

    @classmethod
    def parse_value(cls, tp: Type, value: Any) -> Any:
        """Convert xml string values to python primite types."""

        if hasattr(tp, "__origin__"):
            for tp_arg in tp.__args__:
                try:
                    return cls.parse_value(tp_arg, value)
                except ValueError:
                    pass
            return value

        return value == "true" if tp is bool else tp(value)
