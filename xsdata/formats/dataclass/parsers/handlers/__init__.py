from typing import Type

from xsdata.formats.dataclass.parsers.handlers.native import XmlEventHandler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler

try:
    from xsdata.formats.dataclass.parsers.handlers.lxml import LxmlEventHandler

    def default_handler() -> Type[XmlHandler]:
        return LxmlEventHandler

except ImportError:  # pragma: no cover

    def default_handler() -> Type[XmlHandler]:
        return XmlEventHandler


__all__ = [
    "LxmlEventHandler",
    "XmlEventHandler",
    "default_handler",
]
