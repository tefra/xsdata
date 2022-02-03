from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://domain.org/schema/model/units"


class unit(Enum):
    M = "m"
    KG = "kg"
    VALUE = "%"
    NA = "NA"
