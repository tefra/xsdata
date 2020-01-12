from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SizeType:
    """
    :ivar global_value:
    :ivar unqual:
    :ivar qual:
    :ivar unspec:
    """
    global_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="global",
            type="Attribute"
        )
    )
    unqual: Optional[str] = field(
        default=None,
        metadata=dict(
            name="unqual",
            type="Attribute"
        )
    )
    qual: Optional[str] = field(
        default=None,
        metadata=dict(
            name="qual",
            type="Attribute",
            namespace="http://datypic.com/prod"
        )
    )
    unspec: Optional[str] = field(
        default=None,
        metadata=dict(
            name="unspec",
            type="Attribute"
        )
    )


@dataclass
class Size(SizeType):
    class Meta:
        name = "size"
