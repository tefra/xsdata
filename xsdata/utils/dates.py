from datetime import timedelta
from datetime import timezone
from typing import Optional


class DateTimeParser:
    def __init__(self, value: str, fmt: str):
        self.format = fmt
        self.value = value
        self.vlen = len(value)
        self.flen = len(fmt)
        self.vidx = 0
        self.fidx = 0

        self.year: Optional[int] = None
        self.month: Optional[int] = None
        self.day: Optional[int] = None
        self.hour: Optional[int] = None
        self.minute: Optional[int] = None
        self.second: Optional[int] = None
        self.microsecond: Optional[int] = None
        self.tz_info: Optional[timezone] = None

    def parse(self):
        try:
            while self.fidx < self.flen:
                char = self.next_format_char()

                if char != "%":
                    self.skip(char)
                else:
                    var = self.next_format_char()
                    self.parse_var(var)

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
        if var == "D":
            self.day = self.parse_digits(2)
        elif var == "M":
            self.month = self.parse_digits(2)
        elif var == "Y":
            negative = False
            if self.peek() == "-":
                self.vidx += 1
                negative = True

            self.year = self.parse_minimum_digits(4)
            if negative:
                self.year = -self.year
        elif var == "h":
            self.hour = self.parse_digits(2)
        elif var == "m":
            self.minute = self.parse_digits(2)
        elif var == "s":
            self.second = self.parse_digits(2)
            if self.has_more() and self.peek() == ".":
                self.vidx += 1
                self.microsecond = self.parse_fixed_digits(6)
        elif var == "z":
            self.tz_info = self.parse_timezone()
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

    def parse_timezone(self) -> Optional[timezone]:

        if not self.has_more():
            return None

        ctrl = self.peek()
        if ctrl == "Z":
            self.vidx += 1
            return timezone.utc

        if ctrl == "-" or ctrl == "+":
            self.vidx += 1
            offset = self.parse_digits(2) * 60
            self.skip(":")
            offset += self.parse_digits(2)
            offset *= -1 if ctrl == "-" else 1
            return timezone(timedelta(minutes=offset))

        raise ValueError()
