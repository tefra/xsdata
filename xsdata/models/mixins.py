from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from xsdata.models.enums import XSDType
from xsdata.utils.text import pascal_case, safe_snake, strip_prefix


class TypedField(ABC):
    @property
    def display_type(self) -> Optional[str]:
        raw_type = self.raw_type
        if raw_type is None:
            return None

        xsd_type = XSDType.find(raw_type)
        if xsd_type is not None:
            return xsd_type.py_name

        return pascal_case(strip_prefix(raw_type))

    @property
    @abstractmethod
    def raw_type(self) -> Optional[str]:
        pass


class NamedField:
    @property
    def pascal_name(self) -> str:
        return pascal_case(self.raw_name)

    @property
    def snake_name(self) -> str:
        return safe_snake(self.raw_name)

    @property
    def raw_name(self) -> str:
        name = getattr(self, "name", None)
        if name:
            return name

        name = getattr(self, "ref", None)
        if name:
            return strip_prefix(name)

        raise NotImplementedError("Element has no name: {}".format(self))


class SignatureField(TypedField, NamedField, ABC):
    pass


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
        elif min_occurs == 0 and max_occurs == 1:
            return dict()

        return dict(min_occurs=min_occurs, max_occurs=max_occurs,)


class ExtendsMixin(ABC):
    @property
    @abstractmethod
    def extends(self) -> Optional[str]:
        pass
