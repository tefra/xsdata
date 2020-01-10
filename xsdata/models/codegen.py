from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Type

from xsdata.models.elements import ComplexType, Element
from xsdata.models.enums import TagType


@dataclass
class Attr:
    name: str
    local_name: str = field(init=False)
    type: str
    local_type: str
    index: int
    type_aliases: Dict = field(default_factory=dict)
    namespace: Optional[str] = field(default=None)
    help: Optional[str] = field(default=None)
    forward_ref: bool = field(default=False)
    default: Optional[Any] = field(default=None)

    # Restrictions
    required: Optional[bool] = field(default=None)
    min_occurs: Optional[int] = field(default=None)
    max_occurs: Optional[int] = field(default=None)
    min_exclusive: Optional[float] = field(default=None)
    min_inclusive: Optional[float] = field(default=None)
    min_length: Optional[float] = field(default=None)
    max_exclusive: Optional[float] = field(default=None)
    max_inclusive: Optional[float] = field(default=None)
    max_length: Optional[float] = field(default=None)
    total_digits: Optional[int] = field(default=None)
    fraction_digits: Optional[int] = field(default=None)
    length: Optional[int] = field(default=None)
    white_space: Optional[str] = field(default=None)
    pattern: Optional[str] = field(default=None)

    def __post_init__(self):
        self.local_name = self.name

    @property
    def restrictions(self):
        result = {
            "required": self.required,
            "min_occurs": self.min_occurs,
            "max_occurs": self.max_occurs,
            "min_exclusive": self.min_exclusive,
            "max_exclusive": self.max_exclusive,
            "min_inclusive": self.min_inclusive,
            "max_inclusive": self.max_inclusive,
            "min_length": self.min_length,
            "max_length": self.max_length,
            "length": self.length,
            "fraction_digits": self.fraction_digits,
            "pattern": self.pattern,
            "total_digits": self.total_digits,
            "white_space": self.white_space,
        }
        return {k: v for k, v in result.items() if v is not None}

    @property
    def types(self):
        return filter(None, self.type.split(" "))

    @property
    def is_list(self):
        return self.max_occurs and self.max_occurs > 1

    @property
    def is_enumeration(self):
        return self.local_type == TagType.ENUMERATION.cname


@dataclass
class Extension:
    name: str
    index: int
    type: str

    @property
    def is_restriction(self):
        return self.type == TagType.RESTRICTION.cname


@dataclass
class Class:
    name: str
    type: Type
    is_abstract: bool
    namespace: Optional[str] = field(default=None)
    local_name: str = field(init=False)
    help: Optional[str] = field(default=None)
    extensions: List[Extension] = field(default_factory=list)
    attrs: List[Attr] = field(default_factory=list)
    inner: List["Class"] = field(default_factory=list)

    def __post_init__(self):
        self.local_name = self.name

    @property
    def is_enumeration(self):
        return self.attrs and self.attrs[0].is_enumeration

    @property
    def is_common(self):
        return self.type not in [Element, ComplexType]


@dataclass
class Package:
    name: str
    source: str
    alias: Optional[str] = field(default=None)
