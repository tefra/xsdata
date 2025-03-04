import datetime
from calendar import isleap
from collections.abc import Iterator
from typing import Any, Optional, Union


def parse_date_args(value: Any, fmt: str) -> Iterator[Optional[int]]:
    """Parse the fmt args from the value."""
    if not isinstance(value, str):
        raise ValueError("")

    parser = DateTimeParser(value.strip(), fmt)
    return parser.parse()


def calculate_timezone(offset: Optional[int]) -> Optional[datetime.timezone]:
    """Return a timezone instance by the given hours offset."""
    if offset is None:
        return None

    if offset == 0:
        return datetime.timezone.utc

    return datetime.timezone(datetime.timedelta(minutes=offset))


def calculate_offset(obj: Union[datetime.time, datetime.datetime]) -> Optional[int]:
    """Convert the datetime offset to signed minutes."""
    offset = obj.utcoffset()
    if offset is None:
        return None

    return int(offset.total_seconds() // 60)


def format_date(year: int, month: int, day: int) -> str:
    """Return a xml formatted signed date."""
    if year < 0:
        year = -year
        sign = "-"
    else:
        sign = ""

    return f"{sign}{year:04d}-{month:02d}-{day:02d}"


def format_time(hour: int, minute: int, second: int, fractional_second: int) -> str:
    """Return a xml formatted time."""
    if not fractional_second:
        return f"{hour:02d}:{minute:02d}:{second:02d}"

    microsecond, nano = divmod(fractional_second, 1000)
    if nano:
        return f"{hour:02d}:{minute:02d}:{second:02d}.{fractional_second:09d}"

    milli, micro = divmod(microsecond, 1000)
    if micro:
        return f"{hour:02d}:{minute:02d}:{second:02d}.{microsecond:06d}"

    return f"{hour:02d}:{minute:02d}:{second:02d}.{milli:03d}"


def format_offset(offset: Optional[int]) -> str:
    """Return a xml formatted time offset."""
    if offset is None:
        return ""

    if offset == 0:
        return "Z"

    if offset < 0:
        sign = "-"
        offset = -offset
    else:
        sign = "+"

    hh, mm = divmod(offset, 60)

    return f"{sign}{hh:02d}:{mm:02d}"


# Copied from calendar.monthlen for some reason it's not exported
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def monthlen(year: int, month: int) -> int:
    """Return the number of days for a specific month and year."""
    return mdays[month] + (month == 2 and isleap(year))


def validate_date(year: int, month: int, day: int) -> None:
    """Validate the given year, month day is a valid date."""
    if not 1 <= month <= 12:
        raise ValueError("Month must be in 1..12")

    max_days = monthlen(year, month)
    if not 1 <= day <= max_days:
        raise ValueError(f"Day must be in 1..{max_days}")


def validate_time(hour: int, minute: int, second: int, franctional_second: int) -> None:
    """Validate the time args are valid."""
    if not 0 <= hour <= 24:
        raise ValueError("Hour must be in 0..24")

    if hour == 24 and (minute != 0 or second != 0 or franctional_second != 0):
        raise ValueError("Day time exceeded")

    if not 0 <= minute <= 59:
        raise ValueError("Minute must be in 0..59")

    if not 0 <= second <= 59:
        raise ValueError("Second must be in 0..59")

    if not 0 <= franctional_second <= 999999999:
        raise ValueError("Fractional second must be in 0..999999999")


SIMPLE_TWO_DIGITS_FORMATS = ("d", "m", "H", "M")


class DateTimeParser:
    """XML Datetime parser.

    Args:
        value: The datetime string
        fmt: The target format string

    Attributes:
        vlen: The length of the datetime string
        flen: The length of the format string
        vidx: The current position of the datetime string
        fidx: The current position of the format string
    """

    def __init__(self, value: str, fmt: str):
        """Initialize a DateTimeParser instance."""
        self.format = fmt
        self.value = value
        self.vlen = len(value)
        self.flen = len(fmt)
        self.vidx = 0
        self.fidx = 0

    def parse(self) -> Iterator[Optional[int]]:
        """Yield the parsed datetime string arguments."""
        try:
            while self.fidx < self.flen:
                char = self.next_format_char()

                if char != "%":
                    self.skip(char)
                else:
                    var = self.next_format_char()
                    yield from self.parse_var(var)

            if self.vidx != self.vlen:
                raise ValueError

        except Exception:
            raise ValueError(
                f"String '{self.value}' does not match format '{self.format}'"
            )

    def next_format_char(self) -> str:
        """Return the next format character to evaluate."""
        char = self.format[self.fidx]
        self.fidx += 1
        return char

    def has_more(self) -> bool:
        """Return whether the value is not fully parsed yet."""
        return self.vidx < self.vlen

    def peek(self) -> str:
        """Return the current evaluated character of the datetime string."""
        return self.value[self.vidx]

    def skip(self, char: str) -> None:
        """Validate and skip over the given char."""
        if not self.has_more() or self.peek() != char:
            raise ValueError

        self.vidx += 1

    def parse_var(self, var: str) -> Iterator[Optional[int]]:
        """Parse the given var from the datetime string."""
        if var in SIMPLE_TWO_DIGITS_FORMATS:
            yield self.parse_digits(2)
        elif var == "Y":
            yield self.parse_year()
        elif var == "S":
            yield self.parse_digits(2)

            yield self.parse_fractional_second()
        elif var == "z":
            yield self.parse_offset()
        else:
            raise ValueError

    def parse_year(self) -> int:
        """Parse the year argument."""
        negative = False
        if self.peek() == "-":
            self.vidx += 1
            negative = True

        start = self.vidx
        year = self.parse_minimum_digits(4)
        end = self.vidx
        raw = self.value[start:end]

        leading_zeros = len(raw) - len(raw.lstrip("0"))
        if (
            (leading_zeros == 1 and year > 999)
            or (leading_zeros == 2 and year > 99)
            or (leading_zeros == 3 and year > 9)
            or (leading_zeros == 4 and year > 0)
            or (leading_zeros > 4)
        ):
            raise ValueError

        if negative:
            return -year

        return year

    def parse_fractional_second(self) -> int:
        """Parse the fractional second argument."""
        if self.has_more() and self.peek() == ".":
            self.vidx += 1
            return self.parse_fixed_digits(9)

        return 0

    def parse_digits(self, digits: int) -> int:
        """Parse the given number of digits."""
        start = self.vidx
        self.vidx += digits
        return int(self.value[start : self.vidx])

    def parse_minimum_digits(self, min_digits: int) -> int:
        """Parse until the next character is not a digit."""
        start = self.vidx
        self.vidx += min_digits

        while self.has_more() and self.peek().isdigit():
            self.vidx += 1

        return int(self.value[start : self.vidx])

    def parse_fixed_digits(self, max_digits: int) -> int:
        """Parse a fixed number of digits."""
        start = self.vidx
        just = max_digits
        while max_digits and self.has_more() and self.peek().isdigit():
            self.vidx += 1
            max_digits -= 1

        return int(self.value[start : self.vidx].ljust(just, "0"))

    def parse_offset(self) -> Optional[int]:
        """Parse the xml timezone offset as minutes."""
        if not self.has_more():
            return None

        ctrl = self.peek()
        if ctrl == "Z":
            self.vidx += 1
            return 0

        if ctrl in ("-", "+"):
            self.vidx += 1
            offset = self.parse_digits(2) * 60
            self.skip(":")
            offset += self.parse_digits(2)
            offset *= -1 if ctrl == "-" else 1
            return offset

        raise ValueError
