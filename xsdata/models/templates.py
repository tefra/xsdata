from dataclasses import dataclass, fields
from typing import Any, Dict, List, Optional


@dataclass
class Property:
    def as_dict(self):
        def convert(value):
            if isinstance(value, Dict):
                return {k: v for k, v in value.items() if v is not None}
            elif isinstance(value, list):
                return [v.as_dict() for v in value]
            return value

        return {
            field.name: convert(getattr(self, field.name, None))
            for field in fields(self)
            if getattr(self, field.name, None)
        }


@dataclass
class FieldProperty(Property):
    name: str
    type: str
    metadata: dict
    default: Optional[Any] = None


@dataclass
class ClassProperty(Property):
    name: str
    metadata: dict
    fields: List[FieldProperty]
    help: Optional[str] = None
    extends: Optional[str] = None
