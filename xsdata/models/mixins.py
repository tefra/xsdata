from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from typing import Any
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar

from lxml import etree

from xsdata.exceptions import SchemaValueError
from xsdata.models.enums import DataType
from xsdata.models.enums import FormType
from xsdata.models.enums import Namespace
from xsdata.utils import text

T = TypeVar("T", bound="BaseModel")


class BaseModel:
    def __init__(self, *args: Any, **kwargs: Any):
        pass

    @classmethod
    def create(cls: Type[T], **kwargs: Any) -> T:
        if not kwargs.get("ns_map"):
            kwargs.update({"ns_map": {"xs": Namespace.XS.uri}})

        kwargs = {
            text.snake_case(etree.QName(key).localname): value
            for key, value in kwargs.items()
            if value is not None
        }

        data = {
            attr.name: kwargs[attr.name] for attr in fields(cls) if attr.name in kwargs
        }

        return cls(**data)


@dataclass
class ElementBase(BaseModel):
    index: int = field(default_factory=int)
    ns_map: Dict = field(default_factory=dict)

    @property
    def class_name(self) -> str:
        return self.__class__.__name__

    @property
    def default_type(self) -> DataType:
        return DataType.STRING

    @property
    def default_value(self) -> Any:
        default = getattr(self, "default", None)
        if default is None and hasattr(self, "fixed"):
            default = getattr(self, "fixed", None)

        return default

    @property
    def display_help(self) -> Optional[str]:
        return None

    @property
    def extends(self) -> Optional[str]:
        return None

    @property
    def extensions(self) -> Iterator[str]:
        extends = self.extends or ""
        return filter(None, extends.split(" "))

    @property
    def has_children(self) -> bool:
        return next((True for child in self.children()), False)

    @property
    def has_form(self) -> bool:
        return hasattr(self, "form")

    @property
    def is_abstract(self) -> bool:
        return getattr(self, "abstract", False)

    @property
    def is_attribute(self) -> bool:
        return False

    @property
    def is_fixed(self) -> bool:
        return getattr(self, "fixed", None) is not None

    @property
    def is_mixed(self) -> bool:
        return False

    @property
    def is_nillable(self) -> bool:
        return getattr(self, "nillable", False)

    @property
    def is_qualified(self) -> bool:
        if self.has_form:
            if getattr(self, "form", FormType.UNQUALIFIED) == FormType.QUALIFIED:
                return True

            if self.is_ref:
                return True

        return False

    @property
    def is_ref(self) -> bool:
        return getattr(self, "ref", None) is not None

    @property
    def is_wildcard(self) -> bool:
        return False

    @property
    def prefix(self) -> Optional[str]:
        ref = getattr(self, "ref", None)
        return None if ref is None else text.prefix(ref)

    @property
    def raw_namespace(self) -> Optional[str]:
        return getattr(self, "target_namespace", None)

    @property
    def raw_type(self) -> Optional[str]:
        return getattr(self, "type", None)

    @property
    def real_name(self) -> str:
        name = getattr(self, "name", None) or getattr(self, "ref", None)
        if name:
            return name

        raise SchemaValueError(f"Schema class `{self.class_name}` unknown real name.")

    @property
    def real_type(self) -> Optional[str]:
        raise SchemaValueError(f"Schema class `{self.class_name}` unknown real type.")

    @property
    def substitutions(self) -> List[str]:
        return []

    def get_restrictions(self) -> Dict[str, Any]:
        return {}

    def schema_prefix(self) -> Optional[str]:
        return next(
            (
                prefix
                for prefix, namespace in self.ns_map.items()
                if namespace == Namespace.XS.uri
            ),
            None,
        )

    def children(self) -> Iterator["ElementBase"]:
        for attribute in fields(self):
            value = getattr(self, attribute.name)
            if (
                isinstance(value, list)
                and len(value) > 0
                and isinstance(value[0], ElementBase)
            ):
                yield from value
            elif isinstance(value, ElementBase):
                yield value
