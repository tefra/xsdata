import datetime
import re
from collections import UserString
from typing import Dict
from typing import NamedTuple
from typing import Optional

from xsdata.utils.collections import Immutable
from xsdata.utils.dates import calculate_timezone
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


class XmlDate(Immutable):
    """
    Immutable structure for xs:date values [-]CCYY-MM-DD[Z|(+|-)hh:mm]

    :param year: Any signed integer, eg (0, -535, 2020)
    :param month: Unsigned integer between 1-12
    :param day: Unsigned integer between 1-31
    :param offset: Timezone offset in minutes
    """

    __slots__ = ("year", "month", "day", "offset")

    def __init__(self, year: int, month: int, day: int, offset: Optional[int] = None):
        self.year = year
        self.month = month
        self.day = day
        self.offset = offset
        self._hashcode = -1  # Lock the object

    @classmethod
    def parse(cls, string: str) -> "XmlDate":
        """
        Initialize instance from string format ``%Y-%m-%dT%z``

        :raise ValueError: If format doesn't match input
        """
        return XmlDate(*parse_date_args(string, DateFormat.DATE))

    def date(self) -> datetime.date:
        """Return a :class:`datetime.date` instance."""
        return datetime.date(self.year, self.month, self.day)

    def datetime(self) -> datetime.datetime:
        tz_info = calculate_timezone(self.offset)
        return datetime.datetime(self.year, self.month, self.day, tzinfo=tz_info)

    def __str__(self) -> str:
        """
        XML ISO 8601 format.

        Examples:
            - 2001-10-26
            - 2001-10-26+02:00
            - 2001-10-26Z
        """
        return format_date(self.year, self.month, self.day) + format_offset(self.offset)

    def __repr__(self) -> str:
        args = [self.year, self.month, self.day, self.offset]
        if args[-1] is None:
            del args[-1]

        return f"{self.__class__.__name__}({', '.join(map(str, args))})"


class XmlDateTime(Immutable):
    """
    Immutable structure for xs:dateTime values [-]CCYY-MM-
    DDThh:mm:ss[Z|(+|-)hh:mm]

    :param year: Any signed integer, eg (0, -535, 2020)
    :param month: Unsigned integer between 1-12
    :param day: Unsigned integer between 1-31
    :param hour: Unsigned integer between 0-24
    :param minute: Unsigned integer between 0-59
    :param second: Unsigned integer between 0-59
    :param microsecond: Unsigned integer between 0-999999
    :param offset: Timezone offset in minutes
    """

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
        self._hashcode = -1  # Lock the object

    @classmethod
    def parse(cls, string: str) -> "XmlDateTime":
        """
        Initialize instance from string format ``%Y-%m-%dT%H:%M:%S%z``

        :raise ValueError: If format doesn't match input
        """
        return XmlDateTime(*parse_date_args(string, DateFormat.DATE_TIME))

    def datetime(self) -> datetime.datetime:
        """Return a :class:`datetime.datetime` instance."""
        return datetime.datetime(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
            self.microsecond,
            tzinfo=calculate_timezone(self.offset),
        )

    def __str__(self) -> str:
        """
        XML ISO 8601 format.

        Examples:
            - 2001-10-26T21:32:52
            - 2001-10-26T21:32:52+02:00
            - 2001-10-26T19:32:52Z
            - 2001-10-26T19:32:52.126789
            - 2001-10-26T21:32:52.126
            - -2001-10-26T21:32:52.126Z
        """
        return "{}T{}{}".format(
            format_date(self.year, self.month, self.day),
            format_time(self.hour, self.minute, self.second, self.microsecond),
            format_offset(self.offset),
        )

    def __repr__(self) -> str:
        args = list(self)
        if args[-1] is None:
            del args[-1]

            if args[-1] == 0:
                del args[-1]

        return f"{self.__class__.__name__}({', '.join(map(str, args))})"


class XmlTime(Immutable):
    """
    Immutable structure for xs:time values hh:mm:ss[Z|(+|-)hh:mm]

    :param hour: Unsigned integer between 0-24
    :param minute: Unsigned integer between 0-59
    :param second: Unsigned integer between 0-59
    :param microsecond: Unsigned integer between 0-999999
    :param offset: Timezone offset in minutes
    """

    __slots__ = ("hour", "minute", "second", "microsecond", "offset")

    def __init__(
        self,
        hour: int,
        minute: int,
        second: int,
        microsecond: int = 0,
        offset: Optional[int] = None,
    ):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.offset = offset
        self._hashcode = -1  # Lock the object

    @classmethod
    def parse(cls, string: str) -> "XmlTime":
        """
        Initialize instance from string format ``%H:%M:%S%z``

        :raise ValueError: If format doesn't match input
        """
        return XmlTime(*parse_date_args(string, DateFormat.TIME))

    def time(self) -> datetime.time:
        """Return a :class:`datetime.time` instance."""
        return datetime.time(
            self.hour,
            self.minute,
            self.second,
            self.microsecond,
            tzinfo=calculate_timezone(self.offset),
        )

    def __str__(self) -> str:
        """
        XML ISO 8601 format.

        Examples:
            - 21:32:52
            - 21:32:52+02:00,
            - 19:32:52Z
            - 21:32:52.126789
            - 21:32:52.126Z
        """
        return "{}{}".format(
            format_time(self.hour, self.minute, self.second, self.microsecond),
            format_offset(self.offset),
        )

    def __repr__(self) -> str:
        args = list(self)
        if args[-1] is None:
            del args[-1]

        return f"{self.__class__.__name__}({', '.join(map(str, args))})"


class TimeInterval(NamedTuple):
    negative: bool
    years: Optional[int]
    months: Optional[int]
    days: Optional[int]
    hours: Optional[int]
    minutes: Optional[int]
    seconds: Optional[float]


class XmlDuration(UserString):
    """
    Immutable string representation for xs:duration values.

    Format PnYnMnDTnHnMnS:
        - **P**: literal value that starts the expression
        - **nY**: the number of years followed by a literal Y
        - **nM**: the number of months followed by a literal M
        - **nD**: the number of days followed by a literal D
        - **T**: literal value that separates date and time parts
        - **nH**: the number of hours followed by a literal H
        - **nM**: the number of minutes followed by a literal M
        - **nS**: the number of seconds followed by a literal S

    :param value: String representation of a xs:duration, eg **P2Y6M5DT12H**
    """

    def __init__(self, value: str) -> None:
        super().__init__(value)
        self._interval = self._parse_interval(value)

    @property
    def years(self) -> Optional[int]:
        """Number of years in the interval."""
        return self._interval.years

    @property
    def months(self) -> Optional[int]:
        """Number of months in the interval."""
        return self._interval.months

    @property
    def days(self) -> Optional[int]:
        """Number of days in the interval."""
        return self._interval.days

    @property
    def hours(self) -> Optional[int]:
        """Number of hours in the interval."""
        return self._interval.hours

    @property
    def minutes(self) -> Optional[int]:
        """Number of minutes in the interval."""
        return self._interval.minutes

    @property
    def seconds(self) -> Optional[float]:
        """Number of seconds in the interval."""
        return self._interval.seconds

    @property
    def negative(self) -> bool:
        """Negative flag of the interval."""
        return self._interval.negative

    @classmethod
    def _parse_interval(cls, value: str) -> TimeInterval:
        if not isinstance(value, str):
            raise ValueError("Value must be string")

        if len(value) < 3:
            raise ValueError(f"Invalid format '{value}'")

        match = xml_duration_re.match(value)
        if not match:
            raise ValueError(f"Invalid format '{value}'")

        groups = match.groups()
        res = TimeInterval(
            negative=groups[0] == "-",
            years=int(groups[1]) if groups[1] else None,
            months=int(groups[2]) if groups[2] else None,
            days=int(groups[3]) if groups[3] else None,
            hours=int(groups[4]) if groups[4] else None,
            minutes=int(groups[5]) if groups[5] else None,
            seconds=float(groups[6]) if groups[6] else None,
        )

        if "T" in value and res.hours == res.minutes == res.seconds is None:
            raise ValueError(f"Invalid format '{value}'")
        return res

    def asdict(self) -> Dict:
        return self._interval._asdict()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.data}")'


mdays = [31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class TimePeriod(NamedTuple):
    year: Optional[int]
    month: Optional[int]
    day: Optional[int]
    offset: Optional[int]


class XmlPeriod(UserString):
    """
    Immutable string representation for xs:g[Year[Month[Day]]] types.

    On initialization the period format will be analyzed and parsed
    into date units.

    Formats:
        - xs:gDay: **---%d%z**
        - xs:gMonth: **--%m%z**
        - xs:gYear: **%Y%z**
        - xs:gMonthDay: **--%m-%d%z**
        - xs:gYearMonth: **%Y-%m%z**

    :param value: String representation of a xs:period, eg **--11-01Z**
    """

    def __init__(self, value: str) -> None:
        super().__init__(value)
        self._period = self._parse_period(value)

    @property
    def year(self) -> Optional[int]:
        """Period year."""
        return self._period.year

    @property
    def month(self) -> Optional[int]:
        """Period month."""
        return self._period.month

    @property
    def day(self) -> Optional[int]:
        """Period day."""
        return self._period.day

    @property
    def offset(self) -> Optional[int]:
        """Period timezone offset in minutes."""
        return self._period.offset

    @classmethod
    def _parse_period(cls, value: str) -> TimePeriod:
        year = month = day = offset = None
        if value.startswith("---"):
            day, offset = parse_date_args(value, DateFormat.G_DAY)

        elif value.startswith("--"):
            if len(value) in (4, 5, 10):  # fixed lengths with/out timezone
                month, offset = parse_date_args(value, DateFormat.G_MONTH)
            else:
                month, day, offset = parse_date_args(value, DateFormat.G_MONTH_DAY)
        else:
            end = len(value)
            if value.find(":") > -1:  # offset
                end -= 6

            if value[:end].rfind("-") > 3:  # Minimum position for month sep
                year, month, offset = parse_date_args(value, DateFormat.G_YEAR_MONTH)
            else:
                year, offset = parse_date_args(value, DateFormat.G_YEAR)

        if not cls._is_valid(month, day):
            raise ValueError(f"Invalid format '{value}'")

        return TimePeriod(year=year, month=month, day=day, offset=offset)

    @classmethod
    def _is_valid(cls, month: Optional[int], day: Optional[int]) -> bool:
        if month is not None and not 1 <= month <= 12:
            return False

        if day is not None:
            max_days = mdays[month or 0]
            if not 1 <= day <= max_days:
                return False

        return True

    def asdict(self) -> Dict:
        """Return date units as dict."""
        return self._period._asdict()

    def __repr__(self) -> str:
        return f'XmlPeriod("{self.data}")'
