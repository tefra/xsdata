from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class FieldProperty:
    name: str
    type: str
    metadata: dict
    default: Optional[Any] = field(default=None)


@dataclass
class ClassProperty:
    name: str
    metadata: dict
    help: Optional[str] = field(default=None)
    extends: Optional[str] = field(default=None)
    fields: List[FieldProperty] = field(default_factory=list)
