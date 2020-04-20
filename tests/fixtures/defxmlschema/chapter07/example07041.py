from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/prod"


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
            type="Attribute",
            namespace="http://datypic.com/prod"
        )
    )
    unqual: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    qual: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://datypic.com/prod"
        )
    )
    unspec: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Size(SizeType):
    class Meta:
        name = "size"
        namespace = "http://datypic.com/prod"
