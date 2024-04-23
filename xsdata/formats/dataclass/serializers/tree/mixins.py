import abc
from dataclasses import dataclass
from typing import Any, Dict, Optional, Protocol

from xsdata.exceptions import XmlHandlerError
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.serializers.mixins import EventGenerator, XmlWriterEvent
from xsdata.formats.types import T
from xsdata.models.enums import EventType


class TreeBuilder(Protocol):
    def start(self, tag: str, attrs: Dict[str, Any]): ...  # pragma: no cover

    def end(self, tag: str): ...  # pragma: no cover

    def data(self, data: str): ...  # pragma: no cover


@dataclass
class TreeSerializer(EventGenerator):
    @abc.abstractmethod
    def render(self, obj: T) -> Any:
        """Serialize the input model instance to element tree.

        Args:
            obj: The input model instance to serialize

        Returns:
            The generated element tree instance.
        """

    def build(self, obj: T, builder: TreeBuilder):
        """Feed the builder with events from input model instance.

        Args:
            obj: The input model instance to serialize
            builder: The tree builder instance
        """
        pending_tag = None
        pending_attrs: Dict[str, Any] = {}
        for event, *element in self.generate(obj):
            if pending_tag is not None:
                builder.start(pending_tag, pending_attrs)
                pending_tag = None
                pending_attrs = {}

            if event == XmlWriterEvent.START:
                pending_tag = element[0]
                pending_attrs = {}
            elif event == XmlWriterEvent.ATTR:
                key, value = element
                pending_attrs[key] = value
            elif event == EventType.END:
                builder.end(*element)
            elif event == XmlWriterEvent.DATA:
                data = self.encode_data(element[0])
                builder.data(data)
            else:
                raise XmlHandlerError(f"Unhandled event: `{event}`.")

    @classmethod
    def encode_data(cls, data: Any) -> str:
        """Encode data for xml rendering.

        Args:
            data: The content to encode/serialize

        Returns:
            The xml encoded data
        """
        if data is None or isinstance(data, list) and not data:
            return ""

        if isinstance(data, str):
            return data

        return converter.serialize(data)
