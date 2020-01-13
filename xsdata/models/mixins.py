import re
import sys
from abc import ABC, abstractmethod
from dataclasses import MISSING, Field, dataclass, fields
from typing import Any, Dict, Iterator, Optional, Type, TypeVar

from lxml import etree

from xsdata.models.enums import FormType, Namespace
from xsdata.utils import text


class TypedField(ABC):
    @property
    @abstractmethod
    def real_type(self) -> Optional[str]:
        pass


class NamedField:
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
    def namespace(self):
        form: FormType = getattr(self, "form", FormType.UNQUALIFIED)
        if form == FormType.UNQUALIFIED:
            return None

        lookup = getattr(self, "ref", None) or getattr(self, "name")

        prefix, _ = text.split(lookup or "")
        return self.nsmap.get(prefix)


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


T = TypeVar("T", bound="BaseModel")


class BaseModel:
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def from_element(cls: Type[T], el: etree.Element, index: int) -> T:
        attrs = {
            text.snake_case(etree.QName(key).localname): value
            for key, value in el.attrib.items()
        }
        data = {
            attr.name: cls.xsd_value(attr, attrs)
            if attr.name in attrs
            else cls.default_value(attr)
            for attr in fields(cls)
            if attr.init
        }

        if "nsmap" in data:
            data["nsmap"] = el.nsmap
        if "prefix" in data:
            data["prefix"] = el.prefix
        if "text" in data and el.text:
            data["text"] = re.sub(r"\s+", " ", el.text).strip()
        data["index"] = index

        return cls(**data)

    @classmethod
    def default_value(cls: Type[T], field: Field) -> Any:
        factory = getattr(field, "default_factory")
        if getattr(field, "default_factory") is not MISSING:
            return factory()  # mypy: ignore
        return None if field.default is MISSING else field.default

    @classmethod
    def xsd_value(cls, field: Field, kwargs: Dict) -> Any:
        name = field.name
        value = kwargs[name]
        clazz = field.type

        if name == "max_occurs" and value == "unbounded":
            return sys.maxsize

        # Optional
        if hasattr(clazz, "__origin__"):
            clazz = clazz.__args__[0]

        if clazz == bool:
            return value == "true"

        try:
            if clazz == int:
                return int(value)
            if clazz == float:
                return float(value)
        except ValueError:
            return str(value)

        return clazz(value)

    @classmethod
    def create(cls: Type[T], **kwargs) -> T:
        if not kwargs.get("prefix") and not kwargs.get("nsmap"):
            kwargs.update({"prefix": "xs", "nsmap": {"xs": Namespace.SCHEMA}})

        data = {
            attr.name: kwargs[attr.name]
            if attr.name in kwargs
            else cls.default_value(attr)
            for attr in fields(cls)
            if attr.init
        }

        return cls(**data)


@dataclass
class ElementBase(BaseModel):
    id: Optional[str]
    prefix: str
    nsmap: dict
    index: int

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
    def extends(self) -> Optional[str]:
        return None

    @property
    def extensions(self) -> Iterator[str]:
        extends = self.extends or ""
        return filter(None, extends.split(" "))

    @property
    def num(self):
        return sum(
            [
                len(getattr(self, attribute.name))
                for attribute in fields(self)
                if isinstance(getattr(self, attribute.name), list)
            ]
        )
