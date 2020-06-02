import json
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Type

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

        return super().default(obj)


@dataclass
class DictSerializer(AbstractSerializer):
    """
    Simple dictionary serializer with access to the dict factory.

    :param dict_factory: Override default dict factory to add further logic.
    """

    dict_factory: Callable = field(default=dict)

    def render(self, obj: object) -> Dict:
        """Convert the given object tree to dictionary with primitive
        values."""
        return asdict(obj, dict_factory=self.dict_factory)


@dataclass
class JsonSerializer(AbstractSerializer):
    """
    Simple json.dumps wrapper.

    :param dict_factory: Callable to generate dictionary.
    :param encoder: Value encoder.
    :param indent: output indentation.
    """

    dict_factory: Callable = field(default=dict)
    encoder: Type[json.JSONEncoder] = field(default=JsonEncoder)
    indent: Optional[int] = field(default=None)

    def render(self, obj: object) -> str:
        """Convert the given object tree to json string."""
        return json.dumps(
            asdict(obj, dict_factory=self.dict_factory),
            cls=self.encoder,
            indent=self.indent,
        )
