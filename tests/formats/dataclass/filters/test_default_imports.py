from unittest import TestCase

from xsdata.formats.dataclass.filters import default_imports


class DefaultImportsTests(TestCase):
    def test_default_imports_with_decimal(self):
        output = " Decimal "

        expected = "from decimal import Decimal"
        self.assertIn(expected, default_imports(output))

    def test_default_imports_with_enum(self):
        output = " (Enum) "

        expected = "from enum import Enum"
        self.assertIn(expected, default_imports(output))

    def test_default_imports_with_dataclasses(self):
        output = " @dataclass "

        expected = "from dataclasses import dataclass"
        self.assertIn(expected, default_imports(output))

        output = " field( "
        expected = "from dataclasses import field"
        self.assertIn(expected, default_imports(output))

        output = " field( @dataclass "
        expected = "from dataclasses import dataclass, field"
        self.assertIn(expected, default_imports(output))

    def test_default_imports_with_qname(self):
        output = " QName "

        expected = "from lxml.etree import QName"
        self.assertIn(expected, default_imports(output))

    def test_default_imports_with_typing(self):
        output = " Dict[ "

        expected = "from typing import Dict"
        self.assertIn(expected, default_imports(output))

        output = " List[ "

        expected = "from typing import List"
        self.assertIn(expected, default_imports(output))

        output = " Optional[ "

        expected = "from typing import Optional"
        self.assertIn(expected, default_imports(output))

        output = " Union[ "

        expected = "from typing import Union"
        self.assertIn(expected, default_imports(output))

        output = " Optional[Union[Dict[ "

        expected = "from typing import Dict, Optional, Union"
        self.assertIn(expected, default_imports(output))

    def test_default_imports_combo(self):
        output = """@dataclass
class Foo:
    field: Optional[str] = field(default=None)"""

        expected = """from dataclasses import dataclass, field
from typing import Optional"""
        self.assertEqual(expected, default_imports(output))
