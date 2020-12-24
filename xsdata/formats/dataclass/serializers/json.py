import json
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Type

from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.converter import converter


def filter_none(x: Tuple) -> Dict:
    return {k: v for k, v in x if v is not None}


class DictFactory:
    """Dictionary factory types."""

    FILTER_NONE = filter_none


class JsonEncoder(json.JSONEncoder):
    """Custom Json encoder to support additional python build-in types."""

    def default(self, obj: Any) -> Any:
        """Override parent method to plug the builtin converters."""
        return converter.encode(obj)


@dataclass
class JsonSerializer(AbstractSerializer):
    """
    Json serializer for dataclasses.

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
