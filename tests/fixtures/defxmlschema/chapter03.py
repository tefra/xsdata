from dataclasses import dataclass, field
from typing import List
from tests.fixtures.defxmlschema.chapter03ord import Order


@dataclass
class EnvelopeType:
    """
    :ivar order:
    """
    order: List[Order] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ord",
            "min_occurs": 1,
        }
    )


@dataclass
class Envelope(EnvelopeType):
    class Meta:
        name = "envelope"
