from __future__ import annotations

from dataclasses import dataclass, field

from tests.fixtures.annotations.units import unit

__NAMESPACE__ = "http://domain.org/schema/model"


@dataclass(kw_only=True)
class Measurement:
    value: float = field(
        metadata={
            "required": True,
        }
    )
    unit: None | unit = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Weight(Measurement):
    class Meta:
        namespace = "http://domain.org/schema/model"
