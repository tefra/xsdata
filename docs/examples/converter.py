from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from xsdata.formats.converter import Converter, converter
from xsdata.formats.dataclass.parsers import XmlParser


@dataclass
class Root:
    updated_at: datetime = field(metadata={"type": "Attribute"})


class DatetimeConverter(Converter):
    def from_string(self, value: str, **kwargs: Any) -> datetime:
        return datetime.fromisoformat(value)

    def to_string(self, value: datetime, **kwargs: Any) -> str:
        return value.isoformat(sep=" ")


converter.register_converter(datetime, DatetimeConverter())
root = XmlParser().from_string('<root updated_at="2011-11-04T00:05:23">', Root)

assert root == Root(updated_at=datetime(2011, 11, 4, 0, 5, 23))
