from unittest import TestCase

from xsdata.utils.text import capitalize
from xsdata.utils.text import clean_uri
from xsdata.utils.text import pascal_case
from xsdata.utils.text import qname
from xsdata.utils.text import snake_case
from xsdata.utils.text import split_qname


class TextTests(TestCase):
    def test_snake_case(self):
        self.assertEqual("user_name", snake_case("userName"))
        self.assertEqual("user_name", snake_case("User.Name"))
        self.assertEqual("user_name", snake_case("UserName"))
        self.assertEqual("user_name", snake_case("USER_NAME"))
        self.assertEqual("user_name", snake_case("user_name"))
        self.assertEqual("common_v48_0", snake_case("common_v48_0"))
        self.assertEqual("user", snake_case("user"))
        self.assertEqual("user", snake_case("User"))
        self.assertEqual("user", snake_case("USER"))
        self.assertEqual("user", snake_case("_user"))
        self.assertEqual("user", snake_case("_User"))
        self.assertEqual("user", snake_case("__user"))
        self.assertEqual("user_name", snake_case("user__name"))

    def test_pascal_case(self):
        self.assertEqual("UserName", pascal_case("userName"))
        self.assertEqual("UserName", pascal_case("User.Name"))
        self.assertEqual("UserName", pascal_case("UserName"))
        self.assertEqual("UserName", pascal_case("USER_NAME"))
        self.assertEqual("UserName", pascal_case("user_name"))

    def test_capitalize(self):
        self.assertEqual("UserName", capitalize("userName"))
        self.assertEqual(".userName", capitalize(".userName"))

    def test_clean_uri(self):
        self.assertEqual("any", clean_uri("##any"))
        self.assertEqual("a", clean_uri("urn:a"))
        self.assertEqual("a_com/b", clean_uri("http://a.com/b.xsd"))
        self.assertEqual("a_com/b", clean_uri("http://www.a.com/b.xsd"))
        self.assertEqual("a_com/b", clean_uri("https://a.com/b.wsdl"))
        self.assertEqual("a_com/b", clean_uri("https://www.a.com/b.xsd"))

    def test_qname(self):
        self.assertEqual("{a}b", qname("a", "b"))
        self.assertEqual("b", qname("", "b"))
        self.assertEqual("b", qname(None, "b"))

        self.assertEqual("b", qname("b", ""))
        self.assertEqual("b", qname("b"))
        self.assertEqual("b", qname("b", None))

        with self.assertRaises(ValueError):
            qname(None, None)

    def test_split_qname(self):
        self.assertEqual(("a", "b"), split_qname("{a}b"))
        self.assertEqual((None, "b"), split_qname("b"))

        with self.assertRaises(IndexError):
            split_qname("")
