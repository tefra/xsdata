from dataclasses import dataclass, field
from typing import List, Dict, Union, Optional
from xml.etree.ElementTree import QName


@dataclass
class TypeA:
    x: int


@dataclass
class TypeB:
    x: int
    y: str


@dataclass
class TypeC:
    x: int
    y: str
    z: float


@dataclass
class TypeD:
    x: int
    y: str
    z: Optional[bool]


@dataclass
class ExtendedType:
    a: Optional[TypeA] = field(default=None)
    any: Optional[object] = field(default=None)
    wildcard: Optional[object] = field(default=None, metadata={"type": "Wildcard"})


@dataclass
class ChoiceType:
    choice: List[object] = field(metadata={
        "type": "Elements",
        "choices": (
            {"name": "a", "type": TypeA},
            {"name": "b", "type": TypeB},
            {"name": "int", "type": int},
            {"name": "int2", "type": int, "nillable": True},
            {"name": "float", "type": float},
            {"name": "qname", "type": QName},
            {"name": "tokens", "type": List[int], "tokens": True},
        )
    })


@dataclass
class UnionType:
    element: Union[TypeA, TypeB, TypeC, TypeD]


@dataclass
class AttrsType:
    attrs: Dict[str, str] = field(metadata={"type": "Attributes"})
