import io
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Type

from lxml import etree

from xsdata.formats.inspect import ModelInspect
from xsdata.models.enums import EventType


@dataclass
class XmlParser(ModelInspect):
    def parse(self, source: str, clazz: Type) -> Type:
        context = etree.iterparse(
            source=io.BytesIO(source.encode()),
            events=(EventType.START, EventType.END),
        )

        types = []
        objects = []
        meta = self.class_meta(clazz)
        namespace = meta.namespace

        _, root = next(context)
        types.append(self.mapped_fields(clazz, namespace))
        objects.append(self.start_element(clazz, root))

        for event, element in context:
            if event == EventType.START:
                clazz = self.walk_types(types, namespace, element)
                obj = (
                    self.start_element(clazz, element)
                    if self.is_dataclass(clazz)
                    else self.parse_value(clazz, element.text)
                )
                objects.append(obj)

            elif event == EventType.END:
                obj = self.end_element(objects, types, element.tag)
                element.clear()

        return obj

    def walk_types(
        self,
        types: List[Dict],
        namespace: Optional[str],
        element: etree.Element,
    ) -> Type:
        field = types[-1][element.tag]
        if field.is_dataclass:
            types.append(self.mapped_fields(field.type, namespace))
        return field.type

    def start_element(self, clazz: Type, element: etree.Element) -> Type:
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
        self, objects: List[Type], types: List[Dict], tag: etree.QName
    ) -> Type:
        obj = objects.pop()
        if self.is_dataclass(obj):
            types.pop()

        if len(objects):
            field = types[-1][tag]
            parent = objects[-1]
            if field.is_list:
                getattr(parent, field.name).append(obj)
            else:
                setattr(parent, field.name, obj)

        return obj

    def mapped_fields(self, clazz: Type, namespace: Optional[str]) -> Dict:
        return {
            etree.QName(f.namespace or namespace, f.local_name).text: f
            for f in self.fields(clazz)
        }

    @staticmethod
    def parse_value(tp: Type, value: Any) -> Any:
        if tp is bool:
            return value == "true"
        else:
            return tp(value)
