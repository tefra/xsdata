from typing import Type

from xsdata.formats.dataclass.parsers.handlers.native import XmlEventHandler
from xsdata.formats.dataclass.parsers.handlers.native import XmlSaxHandler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler

try:
    from xsdata.formats.dataclass.parsers.handlers.lxml import LxmlEventHandler
    from xsdata.formats.dataclass.parsers.handlers.lxml import LxmlSaxHandler

    def default_handler() -> Type[XmlHandler]:
        return LxmlEventHandler


except ImportError:  # pragma: no cover

    def default_handler() -> Type[XmlHandler]:
        return XmlEventHandler


__all__ = [
    "LxmlEventHandler",
    "LxmlSaxHandler",
    "XmlEventHandler",
    "XmlSaxHandler",
    "default_handler",
]
