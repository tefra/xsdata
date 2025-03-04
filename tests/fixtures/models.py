from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Optional, Union
from xml.etree.ElementTree import QName

__NAMESPACE__ = "xsdata"


@dataclass
class TypeA:
    x: int


@dataclass
class TypeB:
    x: int
    y: str
    skip: Optional[str] = field(default=None, metadata={"type": "Ignore"})


@dataclass
class TypeC:
    x: int
    y: str
    z: float
    fixed: str = field(init=False, default="ignored")
    restricted: Any = field(init=False, metadata={"type": "Ignore"})


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
class BaseA:
    x: str


@dataclass
class BaseB(BaseA):
    y: str


@dataclass
class BaseC(BaseB):
    z: str


@dataclass
class NillableType:
    class Meta:
        nillable = True

    value: Optional[str] = field(default="abc")


@dataclass
class FixedType:
    value: str = field(init=False, default="abc")


@dataclass
class ExtendedType:
    a: Optional[TypeA] = field(default=None)
    any: Optional[object] = field(default=None)
    wildcard: Optional[object] = field(default=None, metadata={"type": "Wildcard"})


@dataclass
class ExtendedListType:
    wildcard: list[object] = field(default_factory=list, metadata={"type": "Wildcard"})


@dataclass
class ChoiceType:
    choice: list[object] = field(
        metadata={
            "type": "Elements",
            "choices": (
                {"name": "a", "type": TypeA},
                {"name": "b", "type": TypeB},
                {"name": "int", "type": int},
                {"name": "float", "type": float},
                {"name": "qname", "type": QName},
                {"name": "union", "type": type["UnionType"], "namespace": "foo"},
                {"name": "tokens", "type": list[Decimal], "tokens": True, "default_factory": list},
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )

@dataclass
class OptionalChoiceType:
    a_or_b: Optional[object] = field(
        metadata={
            "type": "Elements",
            "choices": (
                {"name": "a", "type": TypeA},
                {"name": "b", "type": TypeB},
            ),
        }
    )


@dataclass
class AmbiguousChoiceType:
    choice: int = field(
        metadata={
            "type": "Elements",
            "choices": (
                {"name": "a", "type": int},
                {"name": "b", "type": int},
            ),
        }
    )


@dataclass
class UnionType:
    element: Union[TypeA, TypeB, TypeC, TypeD]


@dataclass
class BaseType:
    element: BaseA


@dataclass
class AttrsType:
    index: int = field(metadata={"type": "Attribute"})
    attrs: dict[str, str] = field(metadata={"type": "Attributes", "namespace": "##any"})
    fixed: str = field(init=False, default="ignored", metadata={"type": "Attribute"})


@dataclass
class SequentialType:
    a0: Optional[str] = field(default=None, metadata={"type": "Attribute"})
    a1: dict[str, str] = field(default_factory=dict, metadata={"type": "Attributes"})
    a2: list[str] = field(
        default_factory=list, metadata={"type": "Attribute", "tokens": True}
    )
    x0: Optional[int] = field(default=None)
    x1: list[int] = field(
        default_factory=list, metadata={"type": "Element", "sequence": 1}
    )
    x2: list[int] = field(
        default_factory=list, metadata={"type": "Element", "sequence": 1}
    )
    x3: list[int] = field(
        default_factory=list, metadata={"type": "Element", "sequence": 2}
    )
    x4: Optional[int] = field(
        default=None, metadata={"type": "Element", "sequence": 2}
    )
    x5: Optional[str] = field(default=None, metadata={"type": "Element", "nillable": True})
    x6: Optional[str] = field(default=None, metadata={"type": "Element", "nillable": True, "required": True})


@dataclass
class Span:
    class Meta:
        name = "span"

    content: str


@dataclass
class Paragraph:
    class Meta:
        name = "p"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {"name": "span", "type": Span},
            ),
        }
    )


@dataclass
class Parent:
    class Meta:
        global_type = False

    @dataclass
    class Inner:
        pass


@dataclass
class TypeNS2:

    class Meta:
        namespace = "ns2"

    x1: int = field(metadata={"type": "Element"})

@dataclass
class TypeNS1(TypeNS2):

    class Meta:
        namespace = "ns1"

    x2: int = field(metadata={"type": "Element"})