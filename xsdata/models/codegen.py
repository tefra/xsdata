from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from dataclasses import replace
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from lxml.etree import QName

from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.enums import DataType
from xsdata.models.enums import TagType
from xsdata.utils import text


def qname(name: str, nsmap, default_namespace: Optional[str] = None) -> str:
    prefix, suffix = text.split(name)
    namespace = default_namespace

    if prefix:
        name = suffix
        namespace = nsmap.get(prefix)

    return QName(namespace, name)


@dataclass
class Restrictions:
    required: Optional[bool] = field(default=None)
    prohibited: Optional[bool] = field(default=None)
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
    explicit_timezone: Optional[str] = field(default=None)
    nillable: Optional[bool] = field(default=None)

    @property
    def is_list(self):
        return self.max_occurs and self.max_occurs > 1

    def __post_init__(self):
        self.correct_required()

    def update(self, source: "Restrictions"):
        for restriction in fields(self):
            value = getattr(source, restriction.name)
            if value is not None:
                setattr(self, restriction.name, value)

        self.correct_required()

    def correct_required(self):
        if self.min_occurs == 0 and self.max_occurs <= 1:
            self.required = None
            self.min_occurs = None
            self.max_occurs = None
        if self.min_occurs == 1 and self.max_occurs == 1:
            self.required = True
            self.min_occurs = None
            self.max_occurs = None
        elif self.max_occurs and self.max_occurs > 1:
            self.min_occurs = 0 if self.min_occurs is None else self.min_occurs
            self.required = None

    def asdict(self) -> Dict:
        return {k: v for k, v in asdict(self).items() if v is not None}

    def clone(self):
        return replace(self)


@dataclass
class AttrType:
    name: str
    index: int = field(default_factory=int)
    alias: Optional[str] = field(default=None)
    native: bool = field(default=False)
    forward_ref: bool = field(default=False)
    self_ref: bool = field(default=False)

    @property
    def native_name(self) -> Optional[str]:
        data_type = DataType.get_enum(self.name) if self.native else None
        return data_type.local_name if data_type else None

    @property
    def native_code(self) -> Optional[str]:
        data_type = DataType.get_enum(self.name) if self.native else None
        return data_type.code if data_type else None

    @property
    def native_type(self):
        data_type = DataType.get_enum(self.name) if self.native else None
        return data_type.local if data_type else None

    def clone(self):
        return replace(self)


@dataclass
class Attr:
    name: str
    local_name: str = field(init=False)
    local_type: str
    index: int = field(compare=False)
    default: Any = field(default=None)
    wildcard: bool = field(default=False)
    fixed: bool = field(default=False)
    types: List[AttrType] = field(default_factory=list)
    display_type: Optional[str] = field(default=None)
    namespace: Optional[str] = field(default=None)
    help: Optional[str] = field(default=None)
    restrictions: Restrictions = field(default_factory=Restrictions, compare=False)

    def __post_init__(self):
        self.local_name = self.name

    @property
    def is_list(self):
        return self.restrictions.is_list

    @property
    def is_map(self) -> bool:
        return (
            len(self.types) == 1
            and self.types[0].native
            and isinstance(self.types[0].native_type, tuple)
        )

    @property
    def is_factory(self):
        return self.is_list or self.is_map

    @property
    def is_enumeration(self) -> bool:
        return self.local_type == TagType.ENUMERATION

    @property
    def is_attribute(self) -> bool:
        return self.local_type == TagType.ATTRIBUTE

    def clone(self, **kwargs):
        return replace(
            self,
            types=[type.clone() for type in self.types],
            restrictions=self.restrictions.clone(),
            **kwargs,
        )


@dataclass
class Extension:
    type: AttrType
    restrictions: Restrictions

    def clone(self):
        return replace(
            self, type=self.type.clone(), restrictions=self.restrictions.clone()
        )


@dataclass
class Class:
    name: str
    type: Type
    module: str
    package: str
    mixed: bool
    abstract: bool
    nillable: bool
    namespace: Optional[str] = field(default=None)
    local_name: str = field(init=False)
    help: Optional[str] = field(default=None)
    extensions: List[Extension] = field(default_factory=list)
    attrs: List[Attr] = field(default_factory=list)
    inner: List["Class"] = field(default_factory=list)
    nsmap: Dict = field(default_factory=dict)
    source_namespace: Optional[str] = field(default=None)

    def __post_init__(self):
        self.local_name = self.name

    @property
    def key(self) -> str:
        return f"{self.source_namespace}::{self.type.__name__}::{self.name}"

    @property
    def is_enumeration(self) -> bool:
        return len(self.attrs) > 0 and self.attrs[0].is_enumeration

    @property
    def is_common(self):
        return self.type not in [Element, ComplexType]

    @property
    def is_nillable(self) -> bool:
        return self.nillable or next(
            (True for ext in self.extensions if ext.restrictions.nillable), False
        )

    @property
    def target_module(self):
        return f"{self.package}.{self.module}"

    @property
    def is_element(self):
        return self.type is Element

    def clone(self):
        inners = [inner.clone() for inner in self.inner]
        extensions = [extension.clone() for extension in self.extensions]
        attrs = [attr.clone() for attr in self.attrs]
        return replace(self, inner=inners, extensions=extensions, attrs=attrs)

    def source_qname(self, name: Optional[str] = None) -> QName:
        return qname(name or self.name, self.nsmap, self.source_namespace)


@dataclass
class Package:
    name: str
    source: str
    alias: Optional[str] = field(default=None)
