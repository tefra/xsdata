import json
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Type

from xsdata.formats.bindings import AbstractSerializer


def filter_none(x: Tuple):
    return dict((k, v) for k, v in x if v is not None)


class DictFactory:
    FILTER_NONE = filter_none


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        if isinstance(obj, Decimal):
            return str(obj)

        return super(JsonEncoder, self).default(obj)


@dataclass
class DictSerializer(AbstractSerializer):
    dict_factory: Callable = field(default=dict)

    def render(self, obj: object) -> Dict:
        """Convert the given object tree to dictionary with primitive
        values."""
        return asdict(obj, dict_factory=self.dict_factory)


@dataclass
class JsonSerializer(AbstractSerializer):
    """
    :ivar dict_factory: Callable to generate dictionary
    :ivar encoder: Value encoder
    :ivar indent: Pretty print indent
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
