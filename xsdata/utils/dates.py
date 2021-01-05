from typing import Any
from typing import Generator
from typing import Optional


def parse_date_args(value: Any, fmt: str) -> Generator:
    if not isinstance(value, str):
        raise ValueError("")

    parser = DateTimeParser(value, fmt)
    return parser.parse()


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

    hh, mm = divmod(offset, 3600)
    mm, ss = divmod(mm, 60)

    return f"{sign}{hh:02d}:{mm:02d}"


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
            negative = False
            if self.peek() == "-":
                self.vidx += 1
                negative = True

            year = self.parse_minimum_digits(4)
            if negative:
                yield -year
            else:
                yield year

        elif var == "H":
            yield self.parse_digits(2)
        elif var == "M":
            yield self.parse_digits(2)
        elif var == "S":
            yield self.parse_digits(2)
            if self.has_more() and self.peek() == ".":
                self.vidx += 1
                yield self.parse_fixed_digits(6)
            else:
                yield 0
        elif var == "z":
            yield self.parse_offset()
        else:
            raise ValueError()

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
            return offset * 60

        raise ValueError()
