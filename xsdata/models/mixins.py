from abc import ABC, abstractmethod
from typing import Optional

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
    def pascal_name(self) -> Optional[str]:
        raw_name = self.raw_name
        return pascal_case(raw_name) if raw_name else None

    @property
    def snake_name(self) -> Optional[str]:
        raw_name = self.raw_name
        if raw_name is None:
            return raw_name

        return safe_snake(raw_name)

    @property
    def raw_name(self) -> Optional[str]:
        name = getattr(self, "name")
        if name:
            return name

        name = getattr(self, "ref")
        if name:
            return strip_prefix(name)

        return None


class SignatureField(TypedField, NamedField, ABC):
    pass
