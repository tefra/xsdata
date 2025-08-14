try:
    from lxml import etree
    from lxml.etree import _Element as Element
    etree_type = "lxml"
except ImportError:  # pragma: no cover
    from xml.etree import ElementTree as etree
    from xml.etree.ElementTree import Element
    etree_type = "native"

__all__ = [
    "etree",
    "etree_type",
    "Element"
]
