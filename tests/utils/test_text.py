from unittest import TestCase

from xsdata.utils.text import camel_case
from xsdata.utils.text import capitalize
from xsdata.utils.text import mixed_case
from xsdata.utils.text import pascal_case
from xsdata.utils.text import snake_case
from xsdata.utils.text import split_words


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
        self.assertEqual("tmessage_db", snake_case("TMessageDB"))

    def test_pascal_case(self):
        self.assertEqual("UserName", pascal_case("userName"))
        self.assertEqual("UserName", pascal_case("User.Name"))
        self.assertEqual("UserName", pascal_case("UserName"))
        self.assertEqual("UserName", pascal_case("USER_NAME"))
        self.assertEqual("UserName", pascal_case("user_name"))
        self.assertEqual("TmessageDb", pascal_case("TMessageDB"))
        self.assertEqual("P00P", pascal_case("p00p"))

    def test_camel_case(self):
        self.assertEqual("userName", camel_case("userName"))
        self.assertEqual("userName", camel_case("User.Name"))
        self.assertEqual("userName", camel_case("UserName"))
        self.assertEqual("userName", camel_case("USER_NAME"))
        self.assertEqual("userName", camel_case("user_name"))
        self.assertEqual("tmessageDb", camel_case("TMessageDB"))
        self.assertEqual("p00P", camel_case("p00p"))

    def test_mixed_case(self):
        self.assertEqual("UserName", mixed_case("userName"))
        self.assertEqual("Username", mixed_case("user_name"))
        self.assertEqual("TMessageDB", mixed_case("TMessageDB"))
        self.assertEqual("P00p", mixed_case("p00p"))

    def test_capitalize(self):
        self.assertEqual("UserName", capitalize("userName"))
        self.assertEqual(".userName", capitalize(".userName"))

    def test_split_words(self):
        self.assertEqual(["user", "Name"], split_words("userName"))
        self.assertEqual(["User", "Name"], split_words("User.Name"))
        self.assertEqual(["User", "Name"], split_words("UserName"))
        self.assertEqual(["USER", "NAME"], split_words("USER_NAME"))
        self.assertEqual(["user", "name"], split_words("user_name"))
        self.assertEqual(["user", "name"], split_words("user__name"))
        self.assertEqual(["common", "v48", "0"], split_words("common_v48_0"))
        self.assertEqual(["user"], split_words("user"))
        self.assertEqual(["user"], split_words("_user"))
        self.assertEqual(["user"], split_words("__user"))
        self.assertEqual(["TMessage", "DB"], split_words("TMessageDB"))
        self.assertEqual(["GLOBAL", "REF"], split_words("GLOBAL-REF"))
