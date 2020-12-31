import re
from collections import UserString
from typing import Dict
from typing import Tuple

from xsdata.utils.dates import DateTimeParser

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
            raise ValueError(f"Invalid format '{self.data}'")

        match = xml_duration_re.match(self.data)
        if not match:
            raise ValueError(f"Invalid format '{self.data}'")

        groups = match.groups()

        if "T" in self.data and groups[4] == groups[5] == groups[6] is None:
            raise ValueError(f"Invalid format '{self.data}'")

        years = int(groups[1]) if groups[1] else None
        months = int(groups[2]) if groups[2] else None
        days = int(groups[3]) if groups[3] else None
        hours = int(groups[4]) if groups[4] else None
        minutes = int(groups[5]) if groups[5] else None
        seconds = float(groups[6]) if groups[6] else None
        negative = groups[0] == "-"

        return years, months, days, hours, minutes, seconds, negative

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


FORMAT_G_DAY = "---%D%z"
FORMAT_G_MONTH = "--%M%z"
FORMAT_G_MONTH_DAY = "--%M-%D%z"
FORMAT_G_YEAR = "%Y%z"
FORMAT_G_YEAR_MONTH = "%Y-%M%z"

mdays = [31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Period(UserString):
    def __init__(self, seq: object) -> None:
        super().__init__(seq)

        (
            self.year,
            self.month,
            self.day,
            self.timezone,
        ) = self._validate_units()

    def _validate_units(self) -> Tuple:
        fmt = self._get_format()
        parser = DateTimeParser(self.data, fmt)
        parser.parse()

        if parser.month is not None and not 1 <= parser.month <= 12:
            raise ValueError(f"Invalid format '{self.data}'")

        if parser.day is not None:
            max_days = mdays[parser.month or 0]
            if not 1 <= parser.day <= max_days:
                raise ValueError(f"Invalid format '{self.data}'")

        return parser.year, parser.month, parser.day, parser.tz_info

    def _get_format(self) -> str:
        if self.data.startswith("---"):
            return FORMAT_G_DAY

        if self.data.startswith("--"):
            if len(self.data) in (4, 5, 10):  # fixed lengths with/out timezone
                return FORMAT_G_MONTH

            return FORMAT_G_MONTH_DAY  # fixed lengths 7, 8, 13

        end = len(self.data)
        if self.data.find(":") > -1:  # offset timezone ignore it
            end -= 6

        if self.data[:end].rfind("-") > 3:  # Minimum position for month sep
            return FORMAT_G_YEAR_MONTH

        return FORMAT_G_YEAR

    def asdict(self) -> Dict:
        return {
            "year": self.year,
            "month": self.month,
            "day": self.day,
            "timezone": self.timezone,
        }

    def __repr__(self) -> str:
        return f'Period("{self.data}")'
