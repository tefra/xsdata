from dataclasses import MISSING, dataclass, field, fields, is_dataclass
from typing import Any, Dict, Iterator, get_type_hints

from xsdata.models.enums import TagType


@dataclass(frozen=True)
class Field:
    name: str
    local_name: str
    type: Any
    is_list: bool = False
    is_attribute: bool = False
    default: Any = None


@dataclass
class ModelInspect:
    cache: Dict = field(init=False, default_factory=dict)

    def fields(self, model: object) -> Iterator[Field]:
        if not self.is_dataclass(model):
            raise TypeError(f"Object {model} is not a dataclass")

        type_hints = self.get_type_hints(model)
        for f in fields(model):

            tp = type_hints[f.name]
            is_list = False

            if hasattr(tp, "__origin__"):
                is_list = tp.__origin__ is list
                tp = tp.__args__[0]

            default_value = None
            if f.default_factory is not MISSING:  # type: ignore
                default_value = f.default_factory  # type: ignore
            elif f.default is not MISSING:
                default_value = f.default

            yield Field(
                name=f.name,
                local_name=f.metadata["name"],
                is_list=is_list,
                is_attribute=f.metadata["type"] == TagType.ATTRIBUTE.cname,
                type=tp,
                default=default_value,
            )

    def get_type_hints(self, model):
        if model not in self.cache:
            self.cache[model] = get_type_hints(model)
        return self.cache[model]

    @staticmethod
    def is_dataclass(obj: object):
        return is_dataclass(obj)
