from dataclasses import dataclass
from typing import Any, Optional

from lxml.etree import ElementTree

from xsdata.formats.dataclass.serializers.mixins import EventGenerator
from xsdata.formats.dataclass.serializers.writers.lxml import LxmlTreeBuilder
from xsdata.utils import namespaces


@dataclass
class TreeSerializer(EventGenerator):
    """Lxml tree serializer for data classes.

    Args:
        config: The serializer config instance
        context: The models context instance
    """

    def render(self, obj: Any, ns_map: dict | None = None) -> ElementTree:
        """Serialize the input model instance to a lxml etree instance.

        Args:
            obj: The input model instance to serialize
            ns_map: A user defined namespace prefix-URI map

        Returns:
            The element tree instance.
        """
        builder = LxmlTreeBuilder(
            config=self.config,
            ns_map=namespaces.clean_prefixes(ns_map) if ns_map else {},
        )
        return builder.build(self.generate(obj))
