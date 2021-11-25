from typing import Dict
from unittest import TestCase

from xsdata.models.enums import Namespace
from xsdata.utils.namespaces import build_qname
from xsdata.utils.namespaces import clean_prefixes
from xsdata.utils.namespaces import clean_uri
from xsdata.utils.namespaces import generate_prefix
from xsdata.utils.namespaces import is_default
from xsdata.utils.namespaces import is_ncname
from xsdata.utils.namespaces import is_uri
from xsdata.utils.namespaces import load_prefix
from xsdata.utils.namespaces import prefix_exists
from xsdata.utils.namespaces import split_qname
from xsdata.utils.namespaces import to_package_name


class NamespacesTests(TestCase):
    def test_load_prefix(self):
        ns_map: Dict = {}
        self.assertEqual("ns0", load_prefix("a", ns_map))
        self.assertEqual("ns0", load_prefix("a", ns_map))
        self.assertEqual("ns0", load_prefix("a", ns_map))
        self.assertEqual("xs", load_prefix(Namespace.XS.uri, ns_map))
        self.assertEqual("soapenv", load_prefix(Namespace.SOAP_ENV.uri, ns_map))

        expected = {
            "ns0": "a",
            "soapenv": "http://schemas.xmlsoap.org/soap/envelope/",
            "xs": "http://www.w3.org/2001/XMLSchema",
        }
        self.assertEqual(expected, ns_map)

    def test_generate_prefix(self):
        ns_map: Dict = {}
        self.assertEqual("ns0", generate_prefix("a", ns_map))
        self.assertEqual("xs", generate_prefix(Namespace.XS.uri, ns_map))
        self.assertEqual("soapenv", generate_prefix(Namespace.SOAP_ENV.uri, ns_map))
        self.assertEqual("ns3", generate_prefix("b", ns_map))

        expected = {
            "ns0": "a",
            "ns3": "b",
            "soapenv": "http://schemas.xmlsoap.org/soap/envelope/",
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

    def test_is_ncname(self):
        self.assertFalse(is_ncname(""))
        self.assertFalse(is_ncname(":abc123"))
        self.assertFalse(is_ncname("9abc123"))
        self.assertFalse(is_ncname("abc:123"))
        self.assertTrue(is_ncname("a_1.2-b3"))

    def test_is_uri(self):
        self.assertFalse(is_uri("|"))
        self.assertFalse(is_uri(""))
        self.assertTrue(is_uri("a"))
        self.assertTrue(is_uri("urn:books"))
        self.assertTrue(is_uri(Namespace.XS.uri))

    def test_is_default(self):
        self.assertFalse(is_default("foo", {}))
        self.assertFalse(is_default("foo", {"a": "foo"}))
        self.assertTrue(is_default("foo", {"": "foo"}))
        self.assertTrue(is_default("foo", {None: "foo"}))
        self.assertTrue(is_default("foo", {"a": "foo", None: "foo"}))

    def test_to_package_name(self):
        cases = {
            "http://www.w3.org/XML/1998/namespace": "org.w3.XML.1998.namespace",
            "http://www.w3.org/XML/2008/06/xlink.xsd": "org.w3.XML.2008.06.xlink",
            "http://xsdtesting": "xsdtesting",
            "http://xsdtesting:8080": "xsdtesting",
            "http://xsdtesting:8080#target": "xsdtesting",
            "myNS.tempuri.org": "org.tempuri.myNS",
            "ElemDecl/disallowedSubst": "ElemDecl.disallowedSubst",
            "http://xstest-tns/schema11": "xstest-tns.schema11",
            "http://uri.etsi.org/#": "org.etsi.uri",
            "urn:xmlns:25hoursaday-com:address": "com.25hoursaday.address",
            "urn:my.test:SchemaB": "my.test.SchemaB",
            "http://": "",
            "": "",
            " ": "",
            None: "",
        }

        for uri, package in cases.items():
            self.assertEqual(package, to_package_name(uri))
