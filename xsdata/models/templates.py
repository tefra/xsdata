from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class Attr:
    name: str
    type: str
    metadata: dict = field(default_factory=dict)
    default: Optional[Any] = field(default=None)


@dataclass
class Class:
    name: str
    metadata: dict = field(default_factory=dict)
    help: Optional[str] = field(default=None)
    extends: Optional[str] = field(default=None)
    attrs: List[Attr] = field(default_factory=list)
