from typing import Type

from xsdata.formats.dataclass.serializers.mixins import XmlWriter
from xsdata.formats.dataclass.serializers.writers.native import XmlEventWriter

try:
    from xsdata.formats.dataclass.serializers.writers.lxml import LxmlEventWriter

    def default_writer() -> Type[XmlWriter]:
        return LxmlEventWriter


except ImportError:  # pragma: no cover

    def default_writer() -> Type[XmlWriter]:
        return XmlEventWriter


__all__ = ["LxmlEventWriter", "XmlEventWriter", "default_writer"]
