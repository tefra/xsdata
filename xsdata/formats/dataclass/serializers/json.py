import json
from dataclasses import dataclass
from dataclasses import field
from dataclasses import is_dataclass
from enum import Enum
from json import JSONEncoder
from typing import Any
from typing import Optional
from typing import Type

from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlVar


@dataclass
class JsonSerializer(AbstractSerializer):
    """
    Json serializer for dataclasses.

    :param context: Model context provider
    :param encoder: JSONEncoder type
    :param indent: Output indentation
    """

    context: XmlContext = field(default_factory=XmlContext)
    encoder: Optional[Type[JSONEncoder]] = field(default=None)
    indent: Optional[int] = field(default=None)

    def render(self, obj: object) -> str:
        """Convert the given object tree to json string."""
        return json.dumps(self.convert(obj), cls=self.encoder, indent=self.indent)

    def convert(self, obj: Any, var: Optional[XmlVar] = None) -> Any:
        if var is None or is_dataclass(obj):
            metadata = self.context.build(obj.__class__)
            return {
                var.name: self.convert(getattr(obj, var.name), var)
                for var in metadata.vars
            }

        if isinstance(obj, (list, tuple)):
            return [self.convert(v, var) for v in obj]

        if isinstance(obj, (dict, int, float, str, bool)):
            return obj

        if isinstance(obj, Enum):
            return self.convert(obj.value, var)

        return converter.serialize(obj, format=var.format)
