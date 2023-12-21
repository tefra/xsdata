from __future__ import annotations
from dataclasses import dataclass, field
from tests.fixtures.annotations.units import unit

__NAMESPACE__ = "http://domain.org/schema/model"


@dataclass
class Measurement:
    value: float | None = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: unit | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Weight(Measurement):
    class Meta:
        namespace = "http://domain.org/schema/model"
