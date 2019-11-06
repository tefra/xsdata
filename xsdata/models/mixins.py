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
        name = getattr(self, "name")
        if name:
            return name

        name = getattr(self, "ref")
        if name:
            return strip_prefix(name)

        raise NotImplementedError("Element has no name: {}".format(self))


class SignatureField(TypedField, NamedField, ABC):
    pass


class RestrictedField(ABC):
    @abstractmethod
    def get_restrictions(self) -> Dict[str, Any]:
        pass


class OccurrencesMixin(RestrictedField):
    def get_restrictions(self) -> Dict[str, Any]:
        return dict(
            min_occurs=getattr(self, "min_occurs"),
            max_occurs=getattr(self, "min_occurs"),
        )


class ExtendsMixin(ABC):
    @property
    @abstractmethod
    def extends(self) -> Optional[str]:
        pass


class ExtendsNone(ExtendsMixin):
    @property
    def extends(self) -> Optional[str]:
        pass
