from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class Attr:
    name: str
    local_name: str = field(init=False)
    type: str
    local_type: str
    namespace: Optional[str] = field(default=None)
    help: Optional[str] = field(default=None)
    forward_ref: bool = field(default=False)
    restrictions: dict = field(default_factory=dict)
    default: Optional[Any] = field(default=None)

    def __post_init__(self):
        self.local_name = self.name

    @property
    def is_list(self):
        return int(self.restrictions.get("max_occurs", 1)) > 1


@dataclass
class Class:
    name: str
    help: Optional[str] = field(default=None)
    extensions: List[str] = field(default_factory=list)
    attrs: List[Attr] = field(default_factory=list)
    inner: List["Class"] = field(default_factory=list)


@dataclass
class Object:
    name: str
    alias: Optional[str] = field(default=None)


@dataclass
class Package:
    name: str
    objects: List[Object] = field(default_factory=list)
