import json
from dataclasses import dataclass, field
from io import StringIO
from typing import Any, Callable, Dict, TextIO, Tuple

from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.dataclass.serializers import DictEncoder


def filter_none(x: Tuple) -> Dict:
    """Convert a key-value pairs to dict, ignoring None values.

    Args:
        x: Key-value pairs

    Returns:
        The filtered dictionary.
    """
    return {k: v for k, v in x if v is not None}


class DictFactory:
    """Dictionary factory types."""

    FILTER_NONE = filter_none


@dataclass
class JsonSerializer(DictEncoder, AbstractSerializer):
    """Json serializer for data classes.

    Args:
        config: The serializer config instance
        context: The models context instance
        dict_factory: Dictionary factory
        dump_factory: Json dump factory e.g. json.dump
    """

    dump_factory: Callable = field(default=json.dump)

    def render(self, obj: Any) -> str:
        """Serialize the input model instance to json string.

        Args:
            obj: The input model instance

        Returns:
            The serialized json string output.
        """
        output = StringIO()
        self.write(output, obj)
        return output.getvalue()

    def write(self, out: TextIO, obj: Any):
        """Serialize the given object to the output text stream.

        Args:
            out: The output text stream
            obj: The input model instance to serialize
        """
        self.dump_factory(self.encode(obj), out, indent=self.config.indent)
