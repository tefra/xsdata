from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, List, Optional


class TemplateVar(ABC):
    @abstractmethod
    def as_dict(self):
        pass


@dataclass
class FieldItem(TemplateVar):
    name: str
    type: str
    metadata: dict
    default: Optional[Any] = None

    def as_dict(self):
        data = dict(
            name=self.name,
            type=self.type,
            metadata={k: v for k, v in self.metadata.items() if v is not None},
        )

        if self.default is not None:
            data["default"] = self.default
        return data


@dataclass
class ClassItem:
    name: str
    metadata: dict
    fields: List[FieldItem]
    help: Optional[str] = None
    extends: Optional[str] = None

    def as_dict(self):
        data = dict(
            name=self.name,
            fields=self.fields,
            metadata={k: v for k, v in self.metadata.items() if v is not None},
        )
        if self.help:
            data["help"] = self.help
        if self.extends:
            data["extends"] = self.extends
        return data
