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
class TypeDuplicate:
    x: int
    x1: str = field(metadata={"name": "x"})


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


@dataclass
class SequentialType:
    a0: Optional[str] = field(default=None, metadata=dict(type="Attribute"))
    a1: Dict[str, str] = field(default_factory=dict, metadata=dict(type="Attributes"))
    a2: List[str] = field(
        default_factory=list, metadata=dict(type="Attribute", tokens=True)
    )
    x0: Optional[int] = field(default=None)
    x1: List[int] = field(
        default_factory=list, metadata=dict(type="Element", sequential=True)
    )
    x2: List[int] = field(
        default_factory=list, metadata=dict(type="Element", sequential=True)
    )
    x3: List[int] = field(
        default_factory=list, metadata=dict(type="Element", sequential=True)
    )


@dataclass
class MixedType:
    x: int
    y: str
    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807,
        ),
    )
