from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class Attr:
    name: str
    type: str
    help: Optional[str]
    local_name: str
    local_type: str
    forward_ref: bool = field(default=False)
    restrictions: dict = field(default_factory=dict)
    default: Optional[Any] = field(default=None)

    @property
    def is_list(self):
        return (
            "min_occurs" in self.restrictions
            and "max_occurs" in self.restrictions
        )


@dataclass
class Class:
    name: str
    help: Optional[str] = field(default=None)
    extends: Optional[str] = field(default=None)
    attrs: List[Attr] = field(default_factory=list)
    inner: List["Class"] = field(default_factory=list)
