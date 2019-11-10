from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator, List, Optional, Tuple

from xsdata.models.elements import Schema


@dataclass
class Attr:
    name: str
    type: str
    help: Optional[str]
    local_type: str
    local_name: str = field(init=False)
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
    extends: Optional[str] = field(default=None)
    attrs: List[Attr] = field(default_factory=list)
    inner: List["Class"] = field(default_factory=list)


class Renderer(ABC):
    @abstractmethod
    def render(
        self, schema: Schema, classes: List[Class], target: Path
    ) -> Iterator[Tuple[Path, str]]:
        pass
