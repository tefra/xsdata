from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class Attr:
    name: str
    type: str
    metadata: dict = field(default_factory=dict)
    default: Optional[Any] = field(default=None)

    def __post_init__(self):
        if self.metadata.get("help") is None:
            del self.metadata["help"]

    @property
    def is_list(self):
        return "min_occurs" in self.metadata and "max_occurs" in self.metadata


@dataclass
class Class:
    name: str
    metadata: dict = field(default_factory=dict)
    help: Optional[str] = field(default=None)
    extends: Optional[str] = field(default=None)
    attrs: List[Attr] = field(default_factory=list)
