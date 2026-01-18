from dataclasses import dataclass, field
from io import StringIO, TextIOBase
from typing import (
    Any,
    Optional,
)

from xsdata.formats.dataclass.serializers.mixins import (
    EventGenerator,
    XmlWriter,
)
from xsdata.formats.dataclass.serializers.writers import DEFAULT_XML_WRITER
from xsdata.utils import namespaces


@dataclass
class XmlSerializer(EventGenerator):
    """Xml serializer for data classes.

    Args:
        config: The serializer config instance
        context: The models context instance
        writer: The xml writer class
    """

    writer: type[XmlWriter] = field(default=DEFAULT_XML_WRITER)

    def render(self, obj: Any, ns_map: dict | None = None) -> str:
        """Serialize the input model instance to xml string.

        Args:
            obj: The input model instance to serialize
            ns_map: A user defined namespace prefix-URI map

        Returns:
            The serialized xml string output.
        """
        output = StringIO()
        self.write(output, obj, ns_map)
        return output.getvalue()

    def write(self, out: TextIOBase, obj: Any, ns_map: dict | None = None) -> None:
        """Serialize the given object to the output text stream.

        Args:
            out: The output text stream
            obj: The input model instance to serialize
            ns_map: A user defined namespace prefix-URI map
        """
        events = self.generate(obj)
        handler = self.writer(
            config=self.config,
            output=out,
            ns_map=namespaces.clean_prefixes(ns_map) if ns_map else {},
        )
        handler.write(events)
