from typing import Dict
from unittest import TestCase

from xsdata.models.enums import Namespace
from xsdata.utils.namespaces import generate_prefix
from xsdata.utils.namespaces import prefix_exists


class NamespacesTests(TestCase):
    def load_prefix(self):
        ns_map: Dict = {}
        self.assertEqual("ns0", generate_prefix("a", ns_map))
        self.assertEqual("ns0", generate_prefix("a", ns_map))
        self.assertEqual("ns0", generate_prefix("a", ns_map))
        self.assertEqual("xs", generate_prefix(Namespace.XS.uri, ns_map))
        self.assertEqual("soap-env", generate_prefix(Namespace.SOAP_ENV.uri, ns_map))

        expected = {
            "ns0": "a",
            "soap-env": "http://schemas.xmlsoap.org/soap/envelope/",
            "xs": "http://www.w3.org/2001/XMLSchema",
        }
        self.assertEqual(expected, ns_map)

    def test_generate_prefix(self):
        ns_map: Dict = {}
        self.assertEqual("ns0", generate_prefix("a", ns_map))
        self.assertEqual("xs", generate_prefix(Namespace.XS.uri, ns_map))
        self.assertEqual("soap-env", generate_prefix(Namespace.SOAP_ENV.uri, ns_map))
        self.assertEqual("ns3", generate_prefix("b", ns_map))

        expected = {
            "ns0": "a",
            "ns3": "b",
            "soap-env": "http://schemas.xmlsoap.org/soap/envelope/",
            "xs": "http://www.w3.org/2001/XMLSchema",
        }
        self.assertEqual(expected, ns_map)

    def prefix_exists(self):
        self.assertFalse(prefix_exists("a", {}))
        self.assertFalse(prefix_exists("a", {"foo": "a"}))
        self.assertFalse(prefix_exists("a", {None: "a"}))
