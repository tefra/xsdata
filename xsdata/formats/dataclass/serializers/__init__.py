from contextlib import suppress

from xsdata.formats.dataclass.serializers.code import PycodeSerializer
from xsdata.formats.dataclass.serializers.dict import DictEncoder, DictFactory
from xsdata.formats.dataclass.serializers.json import JsonSerializer
from xsdata.formats.dataclass.serializers.xml import XmlSerializer

__all__ = [
    "DictEncoder",
    "DictFactory",
    "JsonSerializer",
    "PycodeSerializer",
    "XmlSerializer",
]

with suppress(ImportError):
    from xsdata.formats.dataclass.serializers.tree import TreeSerializer  # noqa: F401

    __all__.append("TreeSerializer")
