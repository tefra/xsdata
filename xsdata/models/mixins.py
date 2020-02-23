import sys
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from dataclasses import Field
from dataclasses import field
from dataclasses import fields
from dataclasses import is_dataclass
from typing import Any
from typing import Dict
from typing import Iterator
from typing import Optional
from typing import Type
from typing import TypeVar

from lxml import etree

from xsdata.models.enums import FormType
from xsdata.models.enums import Namespace
from xsdata.utils import text


class NamedField:
    @property
    def real_type(self) -> Optional[str]:
        raise NotImplementedError(
            "%s::real_type missing implementation", self.__class__.__name__
        )

    @property
    def real_name(self) -> str:
        name = getattr(self, "name", None) or getattr(self, "ref", None)
        if name:
            return name

        raise NotImplementedError("Element has no name: {}".format(self))

    @property
    def is_abstract(self) -> bool:
        return getattr(self, "abstract", False)

    @property
    def is_qualified(self):
        return getattr(self, "form", FormType.UNQUALIFIED) == FormType.QUALIFIED

    @property
    def prefix(self):
        prefix, _ = text.split(getattr(self, "ref", "") or "")
        return prefix


class RestrictedField(ABC):
    @abstractmethod
    def get_restrictions(self) -> Dict[str, Any]:
        return dict()


class OccurrencesMixin:
    min_occurs: Optional[int] = None
    max_occurs: Optional[int] = None

    def get_restrictions(self) -> Dict[str, Any]:
        if self.min_occurs is None or self.max_occurs is None:
            raise ValueError(
                f"Class `{self.__class__.__name__}` min or max occurs is empty"
            )

        if self.min_occurs == self.max_occurs == 1:
            return dict(required=True)
        if self.max_occurs >= self.min_occurs and self.max_occurs > 1:
            return dict(min_occurs=self.min_occurs, max_occurs=self.max_occurs)
        return dict()


T = TypeVar("T", bound="BaseModel")


class BaseModel:
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def create(cls: Type[T], **kwargs) -> T:
        if not kwargs.get("nsmap"):
            kwargs.update({"nsmap": {"xs": Namespace.SCHEMA.uri}})

        kwargs = {
            text.snake_case(etree.QName(key).localname): value
            for key, value in kwargs.items()
            if value is not None
        }

        data = {
            attr.name: cls.prepare_value(attr, kwargs)
            for attr in fields(cls)
            if attr.name in kwargs
        }

        return cls(**data)

    @classmethod
    def prepare_value(cls, attr: Field, kwargs: Dict) -> Any:
        name = attr.name
        value = kwargs[name]

        if is_dataclass(value):
            return value
        if isinstance(value, dict):
            return value
        if isinstance(value, list):
            return value

        clazz = attr.type
        if name == "max_occurs" and value == "unbounded":
            return sys.maxsize

        # Optional
        if hasattr(clazz, "__origin__"):
            clazz = clazz.__args__[0]

        try:
            if clazz is bool:
                return value == "true" or value is True
            if clazz is int:
                return int(value)
            if clazz is float:
                return float(value)
        except ValueError:
            return str(value)

        return clazz(value)


@dataclass
class ElementBase(BaseModel):
    index: int = field(default_factory=int)
    id: Optional[str] = None

    def children(self):
        for attribute in fields(self):
            value = getattr(self, attribute.name)
            if (
                isinstance(value, list)
                and len(value)
                and isinstance(value[0], ElementBase)
            ):
                for v in value:
                    yield v
            elif isinstance(value, ElementBase):
                yield value

    @property
    def is_attribute(self) -> bool:
        return False

    @property
    def default_value(self):
        return getattr(self, "default", None) or getattr(self, "fixed", None)

    @property
    def is_fixed(self):
        return getattr(self, "fixed", None) is not None

    @property
    def is_mixed(self):
        return False

    @property
    def extends(self) -> Optional[str]:
        return None

    @property
    def extensions(self) -> Iterator[str]:
        extends = self.extends or ""
        return filter(None, extends.split(" "))

    @property
    def class_name(self):
        return self.__class__.__name__

    @property
    def num(self):
        return sum(
            [
                len(getattr(self, attribute.name))
                for attribute in fields(self)
                if isinstance(getattr(self, attribute.name), list)
            ]
        )
