import re
from collections import UserString
from typing import Dict
from typing import Tuple

xml_duration_re = re.compile(
    r"^([-]?)P"
    r"(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?"
    r"(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(.\d+)?)S)?)?$"
)


class Duration(UserString):
    def __init__(self, seq: object) -> None:
        super().__init__(seq)

        (
            self.years,
            self.months,
            self.days,
            self.hours,
            self.minutes,
            self.seconds,
            self.negative,
        ) = self._validate_units()

    def _validate_units(self) -> Tuple:

        if len(self.data) < 3:
            raise ValueError(f"Invalid isoformat string '{self.data}'")

        match = xml_duration_re.match(self.data)
        if not match:
            raise ValueError(f"Invalid isoformat string '{self.data}'")

        groups = match.groups()

        if "T" in self.data and groups[4] == groups[5] == groups[6] is None:
            raise ValueError(f"Invalid isoformat string '{self.data}'")

        years = int(groups[1]) if groups[1] else None
        months = int(groups[2]) if groups[2] else None
        days = int(groups[3]) if groups[3] else None
        hours = int(groups[4]) if groups[4] else None
        minutes = int(groups[5]) if groups[5] else None
        seconds = float(groups[6]) if groups[6] else None
        negative = groups[0] == "-"
        return (years, months, days, hours, minutes, seconds, negative)

    def asdict(self) -> Dict:
        return {
            "years": self.years,
            "months": self.months,
            "days": self.days,
            "hours": self.hours,
            "minutes": self.minutes,
            "seconds": self.seconds,
            "negative": self.negative,
        }

    def __repr__(self) -> str:
        return f'Duration("{self.data}")'
