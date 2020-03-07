from typing import Iterator
from unittest import TestCase

from xsdata.models.elements import Import
from xsdata.models.elements import Include
from xsdata.models.elements import Override
from xsdata.models.elements import Redefine
from xsdata.models.elements import Schema


class SchemaTests(TestCase):
    def test_sub_schemas(self):
        imports = [
            Import.create(schema_location="../foo.xsd"),
            Import.create(schema_location="../bar.xsd"),
        ]
        includes = [
            Include.create(schema_location="common.xsd"),
            Include.create(schema_location="uncommon.xsd"),
        ]
        redefines = [
            Redefine.create(schema_location="a.xsd"),
            Redefine.create(schema_location="b.xsd"),
        ]
        overrides = [
            Override.create(schema_location="a.xsd"),
            Override.create(schema_location="b.xsd"),
        ]
        schema = Schema.create(
            imports=imports, includes=includes, redefines=redefines, overrides=overrides
        )

        actual = schema.included()
        expected = imports + includes + redefines + overrides
        self.assertIsInstance(actual, Iterator)
        self.assertEqual(expected, list(actual))
