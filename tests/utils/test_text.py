import string
from unittest import TestCase

from xsdata.utils.text import alnum
from xsdata.utils.text import camel_case
from xsdata.utils.text import capitalize
from xsdata.utils.text import classify
from xsdata.utils.text import kebab_case
from xsdata.utils.text import mixed_case
from xsdata.utils.text import mixed_pascal_case
from xsdata.utils.text import mixed_snake_case
from xsdata.utils.text import original_case
from xsdata.utils.text import pascal_case
from xsdata.utils.text import screaming_snake_case
from xsdata.utils.text import snake_case
from xsdata.utils.text import split_words
from xsdata.utils.text import StringType


class TextTests(TestCase):
    def test_original_case(self):
        self.assertEqual("p00p", original_case("p00p", foobar=True))
        self.assertEqual("p00p", original_case("p00p"))
        self.assertEqual("USERName", original_case("USERName"))
        self.assertEqual("UserNAME", original_case("UserNAME"))
        self.assertEqual("USER_name", original_case("USER_name"))
        self.assertEqual("USER-NAME", original_case("USER-NAME"))
        self.assertEqual("User_Name", original_case("User_Name"))
        self.assertEqual("user_name", original_case("user_name"))
        self.assertEqual("SUserNAME", original_case("SUserNAME"))

    def test_snake_case(self):
        self.assertEqual("p00p", snake_case("p00p", foobar=True))
        self.assertEqual("p00p", snake_case("p00p"))
        self.assertEqual("username", snake_case("USERName"))
        self.assertEqual("user_name", snake_case("UserNAME"))
        self.assertEqual("user_name", snake_case("USER_name"))
        self.assertEqual("user_name", snake_case("USER-NAME"))
        self.assertEqual("user_name", snake_case("User_Name"))
        self.assertEqual("user_name", snake_case("user_name"))
        self.assertEqual("suser_name", snake_case("SUserNAME"))

    def test_screaming_snake_case(self):
        self.assertEqual("P00P", screaming_snake_case("p00p", foobar=True))
        self.assertEqual("P00P", screaming_snake_case("p00p"))
        self.assertEqual("USERNAME", screaming_snake_case("USERName"))
        self.assertEqual("USER_NAME", screaming_snake_case("UserNAME"))
        self.assertEqual("USER_NAME", screaming_snake_case("USER_name"))
        self.assertEqual("USER_NAME", screaming_snake_case("USER-NAME"))
        self.assertEqual("USER_NAME", screaming_snake_case("User_Name"))
        self.assertEqual("USER_NAME", screaming_snake_case("user_name"))
        self.assertEqual("SUSER_NAME", screaming_snake_case("SUserNAME"))

    def test_pascal_case(self):
        self.assertEqual("P00P", pascal_case("p00p", foobar=True))
        self.assertEqual("P00P", pascal_case("p00p"))
        self.assertEqual("Username", pascal_case("USERName"))
        self.assertEqual("UserName", pascal_case("UserNAME"))
        self.assertEqual("UserName", pascal_case("USER_name"))
        self.assertEqual("UserName", pascal_case("USER-NAME"))
        self.assertEqual("UserName", pascal_case("User_Name"))
        self.assertEqual("UserName", pascal_case("user_name"))
        self.assertEqual("SuserName", pascal_case("SUserNAME"))

    def test_camel_case(self):
        self.assertEqual("p00P", camel_case("p00p", foobar=True))
        self.assertEqual("p00P", camel_case("p00p"))
        self.assertEqual("username", camel_case("USERName"))
        self.assertEqual("userName", camel_case("UserNAME"))
        self.assertEqual("userName", camel_case("USER_name"))
        self.assertEqual("userName", camel_case("USER-NAME"))
        self.assertEqual("userName", camel_case("User_Name"))
        self.assertEqual("userName", camel_case("user_name"))
        self.assertEqual("suserName", camel_case("SUserNAME"))

    def test_mixed_case(self):
        self.assertEqual("p00p", mixed_case("p00p", foobar=True))
        self.assertEqual("p00p", mixed_case("p00p"))
        self.assertEqual("USERName", mixed_case("USERName"))
        self.assertEqual("UserNAME", mixed_case("UserNAME"))
        self.assertEqual("USERname", mixed_case("USER_name"))
        self.assertEqual("USERNAME", mixed_case("USER-NAME"))
        self.assertEqual("UserName", mixed_case("User_Name"))
        self.assertEqual("username", mixed_case("user_name"))
        self.assertEqual("SUserNAME", mixed_case("SUserNAME"))

    def test_mixed_pascal_case(self):
        self.assertEqual("P00p", mixed_pascal_case("p00p", foobar=True))
        self.assertEqual("P00p", mixed_pascal_case("p00p"))
        self.assertEqual("USERName", mixed_pascal_case("USERName"))
        self.assertEqual("UserNAME", mixed_pascal_case("UserNAME"))
        self.assertEqual("USERname", mixed_pascal_case("USER_name"))
        self.assertEqual("USERNAME", mixed_pascal_case("USER-NAME"))
        self.assertEqual("UserName", mixed_pascal_case("User_Name"))
        self.assertEqual("Username", mixed_pascal_case("user_name"))
        self.assertEqual("SUserNAME", mixed_pascal_case("SUserNAME"))

    def test_mixed_snake_case(self):
        self.assertEqual("p00p", mixed_snake_case("p00p", foobar=True))
        self.assertEqual("p00p", mixed_snake_case("p00p"))
        self.assertEqual("USERName", mixed_snake_case("USERName"))
        self.assertEqual("User_NAME", mixed_snake_case("UserNAME"))
        self.assertEqual("USER_name", mixed_snake_case("USER_name"))
        self.assertEqual("USER_NAME", mixed_snake_case("USER-NAME"))
        self.assertEqual("User_Name", mixed_snake_case("User_Name"))
        self.assertEqual("user_name", mixed_snake_case("user_name"))
        self.assertEqual("SUser_NAME", mixed_snake_case("SUserNAME"))

    def test_kebab_case(self):
        self.assertEqual("p00p", kebab_case("p00p", foobar=True))
        self.assertEqual("p00p", kebab_case("p00p"))
        self.assertEqual("USERName", kebab_case("USERName"))
        self.assertEqual("User-NAME", kebab_case("UserNAME"))
        self.assertEqual("USER-name", kebab_case("USER_name"))
        self.assertEqual("USER-NAME", kebab_case("USER-NAME"))
        self.assertEqual("User-Name", kebab_case("User_Name"))
        self.assertEqual("user-name", kebab_case("user_name"))
        self.assertEqual("SUser-NAME", kebab_case("SUserNAME"))

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
        self.assertEqual(["book"], split_words("βιβλιο-book"))

    def test_alnum(self):
        self.assertEqual("foo1", alnum("foo 1"))
        self.assertEqual("foo1", alnum(" foo_1 "))
        self.assertEqual("foo1", alnum("\tfoo*1"))
        self.assertEqual("foo1", alnum(" foo*1"))
        self.assertEqual("1", alnum(" βιβλίο*1"))

    def test_classify(self):
        for ltr in string.ascii_uppercase:
            self.assertEqual(StringType.UPPER, classify(ltr))

        for ltr in string.ascii_lowercase:
            self.assertEqual(StringType.LOWER, classify(ltr))

        for ltr in string.digits:
            self.assertEqual(StringType.NUMERIC, classify(ltr))

        for ltr in "~!@#$%^&*()_+β":
            self.assertEqual(StringType.OTHER, classify(ltr))
