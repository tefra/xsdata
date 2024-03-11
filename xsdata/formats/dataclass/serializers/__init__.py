from xsdata.formats.dataclass.serializers.code import PycodeSerializer
from xsdata.formats.dataclass.serializers.dict import DictEncoder, DictFactory
from xsdata.formats.dataclass.serializers.json import JsonSerializer
from xsdata.formats.dataclass.serializers.tree.native import XmlTreeSerializer
from xsdata.formats.dataclass.serializers.xml import XmlSerializer

__all__ = [
    "DictEncoder",
    "DictFactory",
    "JsonSerializer",
    "XmlSerializer",
    "PycodeSerializer",
]

try:
    from xsdata.formats.dataclass.serializers.tree.lxml import LxmlTreeSerializer

    __all__.append("LxmlTreeSerializer")
except ImportError:  # pragma: no cover
    pass  # pragma: no cover
