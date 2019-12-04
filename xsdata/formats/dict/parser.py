import json
from dataclasses import dataclass, is_dataclass
from typing import Dict, Type

from xsdata.formats.inspect import Field, ModelInspect


@dataclass
class DictParser(ModelInspect):
    def from_json(self, json_str: str, model: Type) -> Type:
        return self.parse(json.loads(json_str), model)

    def parse(self, data: Dict, model: Type) -> Type:
        params = {}

        if type(data) is list and len(data) == 1:
            data = data[0]

        for field in self.fields(model):
            value = self.parse_value(data, field)

            if not value:
                params[field.name] = value
            elif is_dataclass(field.type):
                params[field.name] = (
                    [self.parse(val, field.type) for val in value]
                    if field.is_list
                    else self.parse(value, field.type)
                )
            else:
                params[field.name] = (
                    list(map(field.type, value))
                    if field.is_list
                    else field.type(value)
                )
        try:
            return model(**params)
        except Exception as e:
            raise TypeError("Serialization failed")

    @staticmethod
    def parse_value(data: Dict, field: Field):
        if field.local_name in data:
            value = data[field.local_name]
            if field.is_list and type(value) is not list:
                value = [value]
        elif callable(field.default):
            value = field.default()
        else:
            value = field.default

        return value
