from typing import Dict
from unittest import TestCase

from xsdata.models.enums import Namespace
from xsdata.utils.namespaces import clean_prefixes
from xsdata.utils.namespaces import generate_prefix
from xsdata.utils.namespaces import load_prefix
from xsdata.utils.namespaces import prefix_exists


class NamespacesTests(TestCase):
    def test_load_prefix(self):
        ns_map: Dict = {}
        self.assertEqual("ns0", load_prefix("a", ns_map))
        self.assertEqual("ns0", load_prefix("a", ns_map))
        self.assertEqual("ns0", load_prefix("a", ns_map))
        self.assertEqual("xs", load_prefix(Namespace.XS.uri, ns_map))
        self.assertEqual("soap-env", load_prefix(Namespace.SOAP_ENV.uri, ns_map))

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

    def test_prefix_exists(self):
        self.assertFalse(prefix_exists("a", {}))
        self.assertTrue(prefix_exists("a", {"foo": "a"}))
        self.assertTrue(prefix_exists("a", {None: "a"}))

    def test_clean_prefixes(self):
        ns_map = {"": "a", None: "b", "foo": ""}
        self.assertEqual({None: "a"}, clean_prefixes(ns_map))

        ns_map = {None: "b", "": "a"}
        self.assertEqual({None: "b"}, clean_prefixes(ns_map))

        ns_map = {None: "b", "bb": "b", "c": 1}
        self.assertEqual({"bb": "b", "c": 1}, clean_prefixes(ns_map))

        ns_map = {"bb": "b", None: "b", "c": 1}
        self.assertEqual({"bb": "b", "c": 1}, clean_prefixes(ns_map))
