from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BaseType:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar d:
    :ivar e:
    :ivar f:
    :ivar g:
    :ivar x:
    """
    a: Optional[int] = field(
        default=None,
        metadata=dict(
            name="a",
            type="Attribute"
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            name="b",
            type="Attribute"
        )
    )
    c: str = field(
        default="c",
        metadata=dict(
            name="c",
            type="Attribute"
        )
    )
    d: Optional[str] = field(
        default=None,
        metadata=dict(
            name="d",
            type="Attribute"
        )
    )
    e: Optional[str] = field(
        default=None,
        metadata=dict(
            name="e",
            type="Attribute"
        )
    )
    f: Optional[str] = field(
        default=None,
        metadata=dict(
            name="f",
            type="Attribute"
        )
    )
    g: Optional[str] = field(
        default=None,
        metadata=dict(
            name="g",
            type="Attribute"
        )
    )
    x: Optional[str] = field(
        default=None,
        metadata=dict(
            name="x",
            type="Attribute"
        )
    )


@dataclass
class DerivedType(BaseType):
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar d:
    :ivar e:
    :ivar f:
    :ivar g:
    """
    a: Optional[int] = field(
        default=None,
        metadata=dict(
            name="a",
            type="Attribute"
        )
    )
    b: str = field(
        default="b",
        metadata=dict(
            name="b",
            type="Attribute"
        )
    )
    c: str = field(
        default="c2",
        metadata=dict(
            name="c",
            type="Attribute"
        )
    )
    d: Optional[str] = field(
        default=None,
        metadata=dict(
            name="d",
            type="Attribute"
        )
    )
    e: Optional[str] = field(
        default=None,
        metadata=dict(
            name="e",
            type="Attribute"
        )
    )
    f: Optional[str] = field(
        default=None,
        metadata=dict(
            name="f",
            type="Attribute",
            required=True
        )
    )
    g: Optional[str] = field(
        default=None,
        metadata=dict(
            name="g",
            type="Attribute"
        )
    )
