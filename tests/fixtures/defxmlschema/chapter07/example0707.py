from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ParaType:
    """
    :ivar value:
    :ivar language:
    """
    value: Optional[str] = field(
        default=None,
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class ChapterType:
    """
    :ivar p:
    :ivar language:
    """
    p: List[ParaType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Chapter(ChapterType):
    class Meta:
        name = "chapter"
