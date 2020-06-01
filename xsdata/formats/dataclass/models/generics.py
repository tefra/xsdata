from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional

from lxml.etree import QName
from lxml.etree import register_namespace

from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.models.enums import Namespace


@dataclass
class AnyElement:
    qname: Optional[QName] = field(default=None)
    text: Optional[str] = field(default=None)
    tail: Optional[str] = field(default=None)
    ns_map: Dict = field(default_factory=dict)
    children: List[object] = field(
        default_factory=list, metadata={"type": XmlType.WILDCARD}
    )
    attributes: Dict = field(
        default_factory=dict, metadata={"type": XmlType.ATTRIBUTES}
    )


@dataclass
class Namespaces:
    data: Dict = field(default_factory=lambda: defaultdict(set), init=False)
    auto_ns: int = field(default_factory=int, init=False)
    dirty: bool = field(default=False, init=True)
    _ns_map: Optional[Dict] = field(init=False, default=None)

    @property
    def prefixes(self) -> List[str]:
        return list(filter(None, self.ns_map.keys()))

    @property
    def ns_map(self) -> Dict:
        if self._ns_map is None:
            self._ns_map = {
                (prefix or None): uri
                for uri, prefixes in sorted(self.data.items())
                for prefix in sorted(prefixes)
            }
        return self._ns_map

    def prefix(self, namespace: str) -> Optional[str]:
        return next(
            (prefix for prefix, uri in self.ns_map.items() if uri == namespace), None
        )

    def add(self, uri: Optional[str], prefix: Optional[str] = None):
        if not uri or uri in self.data and prefix is None:
            return

        namespace = Namespace.get_enum(uri)
        prefix = namespace.prefix if namespace else prefix
        if prefix is None:
            prefix = f"ns{self.auto_ns}"

        self.auto_ns += 1
        self._ns_map = None
        self.data[uri].add(prefix)

    def add_all(self, ns_map: Dict):
        for prefix, uri in ns_map.items():
            self.add(uri, prefix or "")

    def clear(self):
        self._ns_map = None
        self.data.clear()

    def register(self):
        for prefix, uri in self.ns_map.items():
            if prefix and not prefix.startswith("ns"):
                register_namespace(prefix, uri)

    def unregister(self):
        for prefix, uri in self.ns_map.items():
            if prefix and not prefix.startswith("ns") and not Namespace.get_enum(uri):
                register_namespace(prefix, "")
