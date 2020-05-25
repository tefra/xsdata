from dataclasses import dataclass
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Bl,
    Ce,
    Ii,
    Ts,
)

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class BirthTime(Ts):
    class Meta:
        name = "birthTime"
        namespace = "urn:hl7-org:sdtc"


@dataclass
class DeceasedInd(Bl):
    class Meta:
        name = "deceasedInd"
        namespace = "urn:hl7-org:sdtc"


@dataclass
class DeceasedTime(Ts):
    class Meta:
        name = "deceasedTime"
        namespace = "urn:hl7-org:sdtc"


@dataclass
class DischargeDispositionCode(Ce):
    class Meta:
        name = "dischargeDispositionCode"
        namespace = "urn:hl7-org:sdtc"


@dataclass
class Id(Ii):
    class Meta:
        name = "id"
        namespace = "urn:hl7-org:sdtc"
