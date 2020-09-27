from unittest import TestCase

from xsdata.utils.text import camel_case
from xsdata.utils.text import capitalize
from xsdata.utils.text import mixed_case
from xsdata.utils.text import pascal_case
from xsdata.utils.text import snake_case
from xsdata.utils.text import split_words


class TextTests(TestCase):
    def test_snake_case(self):
        self.assertEqual("p00p", snake_case("p00p"))
        self.assertEqual("advtype", snake_case("ADVType"))
        self.assertEqual("agent_id", snake_case("AgentID"))
        self.assertEqual("override_pcc", snake_case("OverridePCC"))
        self.assertEqual("enxp_explicit", snake_case("ENXP_explicit"))
        self.assertEqual("tmessage_db", snake_case("TMessageDB"))

    def test_pascal_case(self):
        self.assertEqual("P00P", pascal_case("p00p"))
        self.assertEqual("Advtype", pascal_case("ADVType"))
        self.assertEqual("AgentId", pascal_case("AgentID"))
        self.assertEqual("OverridePcc", pascal_case("OverridePCC"))
        self.assertEqual("EnxpExplicit", pascal_case("ENXP_explicit"))
        self.assertEqual("TmessageDb", pascal_case("TMessageDB"))

    def test_camel_case(self):
        self.assertEqual("p00P", camel_case("p00p"))
        self.assertEqual("advtype", camel_case("ADVType"))
        self.assertEqual("agentId", camel_case("AgentID"))
        self.assertEqual("overridePcc", camel_case("OverridePCC"))
        self.assertEqual("enxpExplicit", camel_case("ENXP_explicit"))
        self.assertEqual("tmessageDb", camel_case("TMessageDB"))

    def test_mixed_case(self):
        self.assertEqual("P00p", mixed_case("p00p"))
        self.assertEqual("ADVType", mixed_case("ADVType"))
        self.assertEqual("AgentID", mixed_case("AgentID"))
        self.assertEqual("OverridePCC", mixed_case("OverridePCC"))
        self.assertEqual("ENXPexplicit", mixed_case("ENXP_explicit"))
        self.assertEqual("TMessageDB", mixed_case("TMessageDB"))

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
