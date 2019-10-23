from dataclasses import dataclass
from typing import Optional


@dataclass
class Base:
    prefix: str
    nsmap: dict


@dataclass
class Documentation(Base):
    lang: str
    source: str
    text: str


@dataclass
class Element(Base):
    id: Optional[str]
    name: str
    ref: Optional[str]
    type: Optional[str]
    substitution_group: Optional[str]
    default_value: Optional[str]
    fixed_value: Optional[str]
    form: Optional[str]
    min_occurs: Optional[int]
    max_occurs: Optional[int]
    nillable: Optional[bool]
    abstract: Optional[bool]
    # block: Optional[List]
    # final: Optional[List]

    documentation: Documentation
