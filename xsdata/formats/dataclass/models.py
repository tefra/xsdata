from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional

from lxml.etree import register_namespace

from xsdata.models.enums import Namespace


@dataclass
class AnyElement:
    qname: Optional[str] = field(default=None)
    text: Optional[str] = field(default=None)
    tail: Optional[str] = field(default=None)
    children: List[object] = field(default_factory=list)
    attributes: Dict = field(
        default_factory=dict, metadata=dict(name="attributes", type="AnyAttribute")
    )


@dataclass
class AnyText:
    text: Optional[str]
    nsmap: Dict = field(default_factory=dict)
    attributes: Dict = field(
        default_factory=dict, metadata=dict(name="attributes", type="AnyAttribute")
    )


@dataclass
class Namespaces:
    items: Dict = field(default_factory=dict, init=False)
    auto_ns: int = field(default_factory=int, init=False)

    @property
    def prefixes(self):
        return list(filter(None, self.items.values()))

    @property
    def ns_map(self):
        return {v: k for k, v in self.items.items()}

    def add(self, uri: Optional[str], prefix: Optional[str] = None):
        if uri and uri not in self.items:
            namespace = Namespace.get_enum(uri)
            if namespace:
                prefix = namespace.prefix
            elif not prefix:
                prefix = f"ns{self.auto_ns}"
                self.auto_ns += 1
            self.items[uri] = prefix

    def add_all(self, ns_map: Dict):
        for prefix, uri in ns_map.items():
            self.add(uri, prefix)

    def clear(self):
        self.items.clear()

    def register(self):
        for uri, prefix in self.items.items():
            if prefix and not prefix.startswith("ns"):
                register_namespace(prefix, uri)
