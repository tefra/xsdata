from dataclasses import dataclass, field
from enum import Enum
from io import StringIO
from typing import (
    Any,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
)
from xml.etree.ElementTree import QName

from xsdata.exceptions import SerializerError
from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta, XmlVar
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.mixins import (
    EventGenerator,
    EventIterator,
    XmlWriter,
    XmlWriterEvent,
)
from xsdata.formats.dataclass.serializers.writers import default_writer
from xsdata.models.enums import DataType, QNames
from xsdata.utils import collections, namespaces
from xsdata.utils.constants import EMPTY_MAP


@dataclass
class XmlSerializer(EventGenerator, AbstractSerializer):
    """Xml serializer for data classes.

    Args:
        config: The serializer config instance
        context: The models context instance
        writer: The xml writer class
    """

    writer: Type[XmlWriter] = field(default=default_writer())

    def render(self, obj: Any, ns_map: Optional[Dict] = None) -> str:
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

    def write(self, out: TextIO, obj: Any, ns_map: Optional[Dict] = None):
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
