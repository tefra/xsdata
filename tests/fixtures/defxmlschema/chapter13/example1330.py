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
            type="Attribute"
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    c: str = field(
        default="c",
        metadata=dict(
            type="Attribute"
        )
    )
    d: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    e: str = field(
        init=False,
        default="e",
        metadata=dict(
            type="Attribute"
        )
    )
    f: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    g: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    x: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class DerivedType:
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
            type="Attribute"
        )
    )
    b: str = field(
        default="b",
        metadata=dict(
            type="Attribute"
        )
    )
    c: str = field(
        default="c2",
        metadata=dict(
            type="Attribute"
        )
    )
    d: str = field(
        init=False,
        default="d",
        metadata=dict(
            type="Attribute"
        )
    )
    e: str = field(
        init=False,
        default="e",
        metadata=dict(
            type="Attribute"
        )
    )
    f: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    g: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    x: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
