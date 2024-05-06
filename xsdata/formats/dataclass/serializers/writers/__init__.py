from typing import Type

from xsdata.formats.dataclass.serializers.mixins import XmlWriter
from xsdata.formats.dataclass.serializers.writers.native import (
    XmlEventWriter,
)

try:
    from xsdata.formats.dataclass.serializers.writers.lxml import LxmlEventWriter

    DEFAULT_XML_WRITER: Type[XmlWriter] = LxmlEventWriter
except ImportError:  # pragma: no cover
    DEFAULT_XML_WRITER = XmlEventWriter


__all__ = [
    "LxmlEventWriter",
    "XmlEventWriter",
    "DEFAULT_XML_WRITER",
]
