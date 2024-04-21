from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://domain.org/schema/model/units"


class unit(str, Enum):
    M = "m"
    KG = "kg"
    PERCENT_SIGN = "%"
    NA = "NA"
