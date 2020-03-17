from collections import defaultdict
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
    items: Dict = field(default_factory=lambda: defaultdict(set), init=False)
    auto_ns: int = field(default_factory=int, init=False)

    @property
    def prefixes(self):
        return list(filter(None, self.ns_map.keys()))

    @property
    def ns_map(self):
        return {
            prefix: uri for uri, prefixes in self.items.items() for prefix in prefixes
        }

    def add(self, uri: Optional[str], prefix: Optional[str] = None):
        if not uri or uri in self.items and not prefix:
            return

        namespace = Namespace.get_enum(uri)
        prefix = namespace.prefix if namespace else prefix
        if not prefix:
            prefix = f"ns{self.auto_ns}"
            self.auto_ns += 1

        self.items[uri].add(prefix)

    def add_all(self, ns_map: Dict):
        for prefix, uri in ns_map.items():
            self.add(uri, prefix)

    def clear(self):
        self.items.clear()

    def register(self):
        for prefix, uri in self.ns_map.items():
            if prefix and not prefix.startswith("ns"):
                register_namespace(prefix, uri)
