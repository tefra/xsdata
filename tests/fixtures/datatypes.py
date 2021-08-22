from collections import namedtuple
from typing import Any

from xsdata.exceptions import ConverterError
from xsdata.formats.converter import Converter
from xsdata.formats.converter import converter

Telephone = namedtuple('Telephone', ['country_code', 'area_code', 'number'])


class PhoneConverter(Converter):

    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        parts = value.split("-")
        if len(parts) == 3:
            return Telephone(*map(int, parts))

        raise ConverterError()

    def serialize(self, value: Telephone, **kwargs: Any) -> str:
        return "-".join(map(str, value))


converter.register_converter(Telephone, PhoneConverter())
