from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional

from lxml.etree import register_namespace

from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.models.enums import Namespace
from xsdata.utils import collections


@dataclass
class AnyElement:
    """
    Generic ElementNode dataclass to bind xml document data to wildcard fields.

    :param qname: The namespace qualified name.
    :param text: Element text content.
    :param tail: Element tail content.
    :param ns_map: The prefix-URI Namespace mapping
    :param children: A list of child elements.
    :param attributes: The element key-value attribute mapping.
    """

    qname: Optional[str] = field(default=None)
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
    """
    Namespaces container used during parsing or generating xml documents.

    :param data: Namespace to prefixes map
    :param auto_ns: Current auto increment prefix id
    :param _ns_map: Prefix to namespace cache auto generated if the data change.
    """

    data: Dict = field(default_factory=lambda: defaultdict(set), init=False)
    auto_ns: int = field(default_factory=int, init=False)
    _ns_map: Optional[Dict] = field(init=False, default=None)

    @property
    def prefixes(self) -> List[str]:
        """Return the list of prefixes."""
        return list(filter(None, self.ns_map.keys()))

    @property
    def ns_map(self) -> Dict:
        """Return the prefix to namespace map."""
        if self._ns_map is None:
            self._ns_map = {
                (prefix or None): uri
                for uri, prefixes in sorted(self.data.items())
                for prefix in sorted(prefixes)
            }
        return self._ns_map

    def prefix(self, namespace: str) -> Optional[str]:
        """Return the prefix for the given namespace."""
        return collections.map_key(self.ns_map, namespace)

    def add(self, uri: Optional[str], prefix: Optional[str] = None):
        """
        Add the given uri and optional prefix to the data storage.

        If the prefix is missing and the uri exists in the storage skip the process.

        If the namespace is one of the common use the predefined prefix to
        follow the lxml convention.

        If the prefix is none assign the next auto increment prefix ns0,ns1,ns2 ...
        """
        if not uri or uri in self.data and prefix is None:
            return

        namespace = Namespace.get_enum(uri)
        prefix = namespace.prefix.replace("_", "-") if namespace else prefix
        if prefix is None:
            prefix = f"ns{self.auto_ns}"

        self.auto_ns += 1
        self._ns_map = None
        self.data[uri].add(prefix)

    def add_all(self, ns_map: Dict):
        """
        Shortcut method to all multiple namespaces/prefixes.

        If prefix is none set the prefix to an empty string as it's the
        convention for the default namespace.
        """
        for prefix, uri in ns_map.items():
            self.add(uri, prefix or "")

    def clear(self):
        """Clear the data storage and ns map cache."""
        self._ns_map = None
        self.data.clear()

    def register(self):
        """Register the current namespaces map to lxml global registry."""
        for prefix, uri in self.ns_map.items():
            if prefix and not prefix.startswith("ns"):
                register_namespace(prefix, uri)

    def unregister(self):
        """Remove from lxml global registry the current namespaces map."""
        for prefix, uri in self.ns_map.items():
            if prefix and not prefix.startswith("ns") and not Namespace.get_enum(uri):
                register_namespace(prefix, "")
