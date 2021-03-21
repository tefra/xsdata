import datetime
from calendar import isleap
from typing import Any
from typing import Generator
from typing import Optional
from typing import Union


def parse_date_args(value: Any, fmt: str) -> Generator:
    if not isinstance(value, str):
        raise ValueError("")

    parser = DateTimeParser(value.strip(), fmt)
    return parser.parse()


def calculate_timezone(offset: Optional[int]) -> Optional[datetime.timezone]:
    if offset is None:
        return None

    if offset == 0:
        return datetime.timezone.utc

    return datetime.timezone(datetime.timedelta(minutes=offset))


def calculate_offset(obj: Union[datetime.time, datetime.datetime]) -> Optional[int]:
    offset = obj.utcoffset()
    if offset is None:
        return None

    return int(offset.total_seconds() // 60)


# year, month, day, hour, minute, seconds, microseconds, offset (minutes)
_DURATIONS = 31556926.0, 2629743, 86400, 3600, 60, 1, 0.000001, -60


def calculate_duration(*args: int) -> float:
    year = args[0]
    if year < 0:
        negative = True
        year = -year
    else:
        negative = False

    total = year * _DURATIONS[0]
    total += sum(args[i] * _DURATIONS[i] for i in range(1, 8) if args[i])
    return -total if negative else total


def format_date(year: int, month: int, day: int) -> str:
    if year < 0:
        year = -year
        sign = "-"
    else:
        sign = ""

    return f"{sign}{year:04d}-{month:02d}-{day:02d}"


def format_time(hour: int, minute: int, second: int, microsecond: int) -> str:
    if not microsecond:
        return f"{hour:02d}:{minute:02d}:{second:02d}"

    milli, micro = divmod(microsecond, 1000)
    if micro:
        return f"{hour:02d}:{minute:02d}:{second:02d}.{microsecond:06d}"

    return f"{hour:02d}:{minute:02d}:{second:02d}.{milli:03d}"


def format_offset(offset: Optional[int]) -> str:
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
    return mdays[month] + (month == 2 and isleap(year))


def validate_date(year: int, month: int, day: int):
    if not 1 <= month <= 12:
        raise ValueError("Month must be in 1..12")

    max_days = monthlen(year, month)
    if not 1 <= day <= max_days:
        raise ValueError(f"Day must be in 1..{max_days}")


def validate_time(hour: int, minute: int, second: int, microsecond: int):

    if not 0 <= hour <= 24:
        raise ValueError("Hour must be in 0..24")

    if hour == 24 and (minute != 0 or second != 0 or microsecond != 0):
        raise ValueError("Day time exceeded")

    if not 0 <= minute <= 59:
        raise ValueError("Minute must be in 0..59")

    if not 0 <= second <= 59:
        raise ValueError("Second must be in 0..59")

    if not 0 <= microsecond <= 999999:
        raise ValueError("Microsecond must be in 0..999999")


class DateTimeParser:
    def __init__(self, value: str, fmt: str):
        self.format = fmt
        self.value = value
        self.vlen = len(value)
        self.flen = len(fmt)
        self.vidx = 0
        self.fidx = 0

    def parse(self):
        try:
            while self.fidx < self.flen:
                char = self.next_format_char()

                if char != "%":
                    self.skip(char)
                else:
                    var = self.next_format_char()
                    yield from self.parse_var(var)

            if self.vidx != self.vlen:
                raise ValueError()

        except Exception:
            raise ValueError(
                f"String '{self.value}' does not match format '{self.format}'"
            )

    def next_format_char(self) -> str:
        char = self.format[self.fidx]
        self.fidx += 1
        return char

    def has_more(self) -> bool:
        return self.vidx < self.vlen

    def peek(self) -> str:
        return self.value[self.vidx]

    def skip(self, char: str):
        if not self.has_more() or self.peek() != char:
            raise ValueError()

        self.vidx += 1

    def parse_var(self, var: str):
        if var == "d":
            yield self.parse_digits(2)
        elif var == "m":
            yield self.parse_digits(2)
        elif var == "Y":
            yield self.parse_year()
        elif var == "H":
            yield self.parse_digits(2)
        elif var == "M":
            yield self.parse_digits(2)
        elif var == "S":
            yield self.parse_digits(2)

            yield self.parse_microsecond()
        elif var == "z":
            yield self.parse_offset()
        else:
            raise ValueError()

    def parse_year(self) -> int:
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
            raise ValueError()

        if negative:
            return -year

        return year

    def parse_microsecond(self) -> int:
        if self.has_more() and self.peek() == ".":
            self.vidx += 1
            return self.parse_fixed_digits(6)
        else:
            return 0

    def parse_digits(self, digits: int) -> int:
        start = self.vidx
        self.vidx += digits
        return int(self.value[start : self.vidx])

    def parse_minimum_digits(self, min_digits: int) -> int:
        start = self.vidx
        self.vidx += min_digits

        while self.has_more() and self.peek().isdigit():
            self.vidx += 1

        return int(self.value[start : self.vidx])

    def parse_fixed_digits(self, max_digits: int) -> int:
        start = self.vidx
        just = max_digits
        while max_digits and self.has_more() and self.peek().isdigit():
            self.vidx += 1
            max_digits -= 1

        return int(self.value[start : self.vidx].ljust(just, "0"))

    def parse_offset(self) -> Optional[int]:

        if not self.has_more():
            return None

        ctrl = self.peek()
        if ctrl == "Z":
            self.vidx += 1
            return 0

        if ctrl == "-" or ctrl == "+":
            self.vidx += 1
            offset = self.parse_digits(2) * 60
            self.skip(":")
            offset += self.parse_digits(2)
            offset *= -1 if ctrl == "-" else 1
            return offset

        raise ValueError()
