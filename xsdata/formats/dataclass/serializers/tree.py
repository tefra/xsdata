from dataclasses import dataclass
from typing import Any, Dict, Optional

from xsdata.formats.dataclass.serializers.mixins import EventGenerator
from xsdata.formats.dataclass.serializers.writers.lxml import LxmlTreeBuilder
from xsdata.utils import namespaces


@dataclass
class TreeSerializer(EventGenerator):
    def render(self, obj: Any, ns_map: Optional[Dict] = None):
        builder = LxmlTreeBuilder(
            config=self.config,
            ns_map=namespaces.clean_prefixes(ns_map) if ns_map else {},
        )
        return builder.build(self.generate(obj))
