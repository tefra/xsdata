from typing import Dict
from unittest import TestCase

from xsdata.models.enums import Namespace
from xsdata.utils.namespaces import build_qname
from xsdata.utils.namespaces import clean_prefixes
from xsdata.utils.namespaces import clean_uri
from xsdata.utils.namespaces import generate_prefix
from xsdata.utils.namespaces import load_prefix
from xsdata.utils.namespaces import prefix_exists
from xsdata.utils.namespaces import split_qname


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

    def test_clean_uri(self):
        self.assertEqual("any", clean_uri("##any"))
        self.assertEqual("a", clean_uri("urn:a"))
        self.assertEqual("a_com/b", clean_uri("http://a.com/b.xsd"))
        self.assertEqual("a_com/b", clean_uri("http://www.a.com/b.xsd"))
        self.assertEqual("a_com/b", clean_uri("https://a.com/b.wsdl"))
        self.assertEqual("a_com/b", clean_uri("https://www.a.com/b.xsd"))

    def test_build_qname(self):
        self.assertEqual("{a}b", build_qname("a", "b"))
        self.assertEqual("b", build_qname("", "b"))
        self.assertEqual("b", build_qname(None, "b"))

        self.assertEqual("b", build_qname("b", ""))
        self.assertEqual("b", build_qname("b"))
        self.assertEqual("b", build_qname("b", None))

        with self.assertRaises(ValueError):
            build_qname(None, None)

    def test_split_qname(self):
        self.assertEqual(("a", "b"), split_qname("{a}b"))
        self.assertEqual((None, "b"), split_qname("b"))
        self.assertEqual((None, "{"), split_qname("{"))
        self.assertEqual((None, "{foobar"), split_qname("{foobar"))

        with self.assertRaises(IndexError):
            split_qname("")
