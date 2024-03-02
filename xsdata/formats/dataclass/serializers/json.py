import json
from dataclasses import dataclass, field
from io import StringIO
from typing import Any, Callable, TextIO

from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.dataclass.serializers import DictEncoder


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
