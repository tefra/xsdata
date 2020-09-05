import copy
import json
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from dataclasses import is_dataclass
from decimal import Decimal
from enum import Enum
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Type
from xml.etree.ElementTree import QName

from xsdata.formats.bindings import AbstractSerializer


def filter_none(x: Tuple) -> Dict:
    return {k: v for k, v in x if v is not None}


class DictFactory:
    """Dictionary factory types."""

    FILTER_NONE = filter_none


class JsonEncoder(json.JSONEncoder):
    """Custom Json encoder to support additional python build-in types."""

    def default(self, obj: Any) -> Any:
        """Override parent method to handle enumerations and decimals."""

        if isinstance(obj, Enum):
            return obj.value

        if isinstance(obj, Decimal):
            return str(obj)

        if isinstance(obj, QName):
            return str(obj)

        return super().default(obj)


def asdict(obj: Any, dict_factory: Callable = dict) -> Any:
    """Clone dataclasses implementation to support pickling lxml.etree.QName
    objects."""
    if is_dataclass(obj):
        return dict_factory(
            [(f.name, asdict(getattr(obj, f.name), dict_factory)) for f in fields(obj)]
        )

    if isinstance(obj, (list, tuple)):
        return type(obj)(asdict(v, dict_factory) for v in obj)

    if isinstance(obj, dict):
        return type(obj)(
            (asdict(k, dict_factory), asdict(v, dict_factory)) for k, v in obj.items()
        )

    if isinstance(obj, QName):
        return obj.text  # QNames are readonly anyway!

    return copy.deepcopy(obj)


@dataclass
class JsonSerializer(AbstractSerializer):
    """
    Simple json.dumps wrapper.

    :param indent: output indentation.
    :param encoder: Value encoder.
    :param dict_factory: Override default dict factory to add further logic.
    """

    indent: Optional[int] = field(default=None)
    encoder: Type[json.JSONEncoder] = field(default=JsonEncoder)
    dict_factory: Callable = field(default=dict)

    def render(self, obj: object) -> str:
        """Convert the given object tree to json string."""
        return json.dumps(
            asdict(obj, dict_factory=self.dict_factory),
            cls=self.encoder,
            indent=self.indent,
        )
