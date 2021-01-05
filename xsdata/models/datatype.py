import re
from collections import UserString
from typing import Any
from typing import Dict
from typing import Optional
from typing import Tuple

from xsdata.utils.dates import format_date
from xsdata.utils.dates import format_offset
from xsdata.utils.dates import format_time
from xsdata.utils.dates import parse_date_args

xml_duration_re = re.compile(
    r"^([-]?)P"
    r"(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?"
    r"(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(.\d+)?)S)?)?$"
)


class DateFormat:
    DATE = "%Y-%m-%d%z"
    TIME = "%H:%M:%S%z"
    DATE_TIME = "%Y-%m-%dT%H:%M:%S%z"
    G_DAY = "---%d%z"
    G_MONTH = "--%m%z"
    G_MONTH_DAY = "--%m-%d%z"
    G_YEAR = "%Y%z"
    G_YEAR_MONTH = "%Y-%m%z"


class XmlDate:
    __slots__ = "year", "month", "day", "offset"

    def __init__(self, year: int, month: int, day: int, offset: Optional[int] = None):
        self.year = year
        self.month = month
        self.day = day
        self.offset = offset

    @classmethod
    def parse(cls, string: str) -> "XmlDate":
        return XmlDate(*parse_date_args(string, DateFormat.DATE))

    def __str__(self) -> str:
        return format_date(self.year, self.month, self.day) + format_offset(self.offset)

    def __repr__(self) -> str:
        args = [self.year, self.month, self.day, self.offset]
        if args[-1] is None:
            del args[-1]

        return f"{self.__class__.__name__}({', '.join(map(str, args))})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, XmlDate):
            return (
                self.year == other.year
                and self.month == other.month
                and self.day == other.day
                and self.offset == other.offset
            )

        return NotImplemented


class XmlDateTime:
    __slots__ = (
        "year",
        "month",
        "day",
        "hour",
        "minute",
        "second",
        "microsecond",
        "offset",
    )

    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        microsecond: int = 0,
        offset: Optional[int] = None,
    ):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.offset = offset

    @classmethod
    def parse(cls, string: str) -> "XmlDateTime":
        return XmlDateTime(*parse_date_args(string, DateFormat.DATE_TIME))

    def __str__(self) -> str:
        return "{}T{}{}".format(
            format_date(self.year, self.month, self.day),
            format_time(self.hour, self.minute, self.second, self.microsecond),
            format_offset(self.offset),
        )

    def __repr__(self) -> str:
        args = [getattr(self, name) for name in self.__slots__]
        if args[-1] is None:
            del args[-1]

            if args[-1] == 0:
                del args[-1]

        return f"{self.__class__.__name__}({', '.join(map(str, args))})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, XmlDateTime):
            return (
                self.year == other.year
                and self.month == other.month
                and self.day == other.day
                and self.hour == other.hour
                and self.minute == other.minute
                and self.second == other.second
                and self.microsecond == other.microsecond
                and self.offset == other.offset
            )

        return NotImplemented


class XmlTime:
    __slots__ = "hour", "minute", "second", "microsecond", "offset"

    def __init__(
        self,
        hour: int,
        minute: int,
        second: int,
        microsecond: int,
        offset: Optional[int] = None,
    ):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.offset = offset

    @classmethod
    def parse(cls, string: str) -> "XmlTime":
        return XmlTime(*parse_date_args(string, DateFormat.TIME))

    def __str__(self) -> str:
        return "{}{}".format(
            format_time(self.hour, self.minute, self.second, self.microsecond),
            format_offset(self.offset),
        )

    def __repr__(self) -> str:
        args = [self.hour, self.minute, self.second, self.microsecond, self.offset]
        if args[-1] is None:
            del args[-1]

        return f"{self.__class__.__name__}({', '.join(map(str, args))})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, XmlTime):
            return (
                self.hour == other.hour
                and self.minute == other.minute
                and self.second == other.second
                and self.microsecond == other.microsecond
                and self.offset == other.offset
            )

        return NotImplemented


class XmlDuration(UserString):
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
        ) = self._parse_unit()

    def _parse_unit(self) -> Tuple:

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
        return f'{self.__class__.__name__}("{self.data}")'


mdays = [31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class XmlPeriod(UserString):
    def __init__(self, seq: object) -> None:
        super().__init__(seq)

        (
            self.year,
            self.month,
            self.day,
            self.offset,
        ) = self._parse_unit()

    def _parse_unit(self) -> Tuple:
        year = month = day = offset = None
        if self.data.startswith("---"):
            day, offset = parse_date_args(self.data, DateFormat.G_DAY)

        elif self.data.startswith("--"):
            if len(self.data) in (4, 5, 10):  # fixed lengths with/out timezone
                month, offset = parse_date_args(self.data, DateFormat.G_MONTH)
            else:
                month, day, offset = parse_date_args(self.data, DateFormat.G_MONTH_DAY)
        else:
            end = len(self.data)
            if self.data.find(":") > -1:  # offset
                end -= 6

            if self.data[:end].rfind("-") > 3:  # Minimum position for month sep
                year, month, offset = parse_date_args(
                    self.data, DateFormat.G_YEAR_MONTH
                )
            else:
                year, offset = parse_date_args(self.data, DateFormat.G_YEAR)

        self._check_units(month, day)

        return year, month, day, offset

    def _check_units(self, month: Optional[int], day: Optional[int]):
        if month is not None and not 1 <= month <= 12:
            raise ValueError(f"Invalid format '{self.data}'")

        if day is not None:
            max_days = mdays[month or 0]
            if not 1 <= day <= max_days:
                raise ValueError(f"Invalid format '{self.data}'")

    def asdict(self) -> Dict:
        return {
            "year": self.year,
            "month": self.month,
            "day": self.day,
            "offset": self.offset,
        }

    def __repr__(self) -> str:
        return f'XmlPeriod("{self.data}")'
