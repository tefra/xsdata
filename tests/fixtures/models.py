from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import Union
from xml.etree.ElementTree import QName

from xsdata.utils.constants import return_true

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
    wildcard: List[object] = field(default_factory=list, metadata={"type": "Wildcard"})


@dataclass
class ChoiceType:
    choice: List[object] = field(
        metadata={
            "type": "Elements",
            "choices": (
                {"name": "a", "type": TypeA},
                {"name": "b", "type": TypeB},
                {"name": "int", "type": int},
                {"name": "int2", "type": int, "nillable": True},
                {"name": "float", "type": float},
                {"name": "qname", "type": QName},
                {
                    "name": "tokens",
                    "type": List[int],
                    "tokens": True,
                    "default_factory": return_true
                },
                {"name": "union", "type": Type["UnionType"], "namespace": "foo"},
                {"name": "p", "type": float, "fixed": True, "default": 1.1},
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
class UnionType:
    element: Union[TypeA, TypeB, TypeC, TypeD]


@dataclass
class BaseType:
    element: BaseA


@dataclass
class AttrsType:
    index: int = field(metadata={"type": "Attribute"})
    attrs: Dict[str, str] = field(metadata={"type": "Attributes", "namespace": "##any"})
    fixed: str = field(init=False, default="ignored", metadata={"type": "Attribute"})


@dataclass
class SequentialType:
    a0: Optional[str] = field(default=None, metadata=dict(type="Attribute"))
    a1: Dict[str, str] = field(default_factory=dict, metadata=dict(type="Attributes"))
    a2: List[str] = field(
        default_factory=list, metadata=dict(type="Attribute", tokens=True)
    )
    x0: Optional[int] = field(default=None)
    x1: List[int] = field(
        default_factory=list, metadata=dict(type="Element", sequence=1)
    )
    x2: List[int] = field(
        default_factory=list, metadata=dict(type="Element", sequence=1)
    )
    x3: List[int] = field(
        default_factory=list, metadata=dict(type="Element", sequence=2)
    )
    x4: Optional[int] = field(
        default=None, metadata=dict(type="Element", sequence=2)
    )


@dataclass
class Span:
    class Meta:
        name = "span"

    content: str


@dataclass
class Paragraph:
    class Meta:
        name = "p"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            choices=(
                dict(name="span", type=Span),
            ),
        )
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

    x1: int = field(metadata=dict(type="Element"))

@dataclass
class TypeNS1(TypeNS2):

    class Meta:
        namespace = "ns1"

    x2: int = field(metadata=dict(type="Element"))