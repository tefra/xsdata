from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class TypedField(ABC):
    @property
    @abstractmethod
    def real_type(self) -> Optional[str]:
        pass


class ExtendsMixin(ABC):
    @property
    @abstractmethod
    def extensions(self) -> List[str]:
        pass


class NamedField:
    @property
    def real_name(self) -> str:
        name = getattr(self, "name", None) or getattr(self, "ref", None)
        if name:
            return name

        raise NotImplementedError("Element has no name: {}".format(self))


class RestrictedField(ABC):
    @abstractmethod
    def get_restrictions(self) -> Dict[str, Any]:
        pass


class OccurrencesMixin:
    def get_restrictions(self) -> Dict[str, Any]:
        min_occurs = getattr(self, "min_occurs", 1)
        max_occurs = getattr(self, "max_occurs", 1)
        if min_occurs == max_occurs == 1:
            return dict(required=True)
        if max_occurs > min_occurs and max_occurs > 1:
            return dict(min_occurs=min_occurs, max_occurs=max_occurs)
        return dict()
