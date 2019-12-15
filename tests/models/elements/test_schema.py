from typing import Iterator
from unittest import TestCase

from xsdata.models.elements import Import, Include, Schema


class SchemaTests(TestCase):
    def test_sub_schemas(self):
        schema = Schema.create(
            imports=[
                Import.create(schema_location="../foo.xsd"),
                Import.create(schema_location="../bar.xsd"),
            ],
            includes=[
                Include.create(schema_location="common.xsd"),
                Include.create(schema_location="uncommon.xsd"),
            ],
        )

        actual = schema.sub_schemas()
        self.assertIsInstance(actual, Iterator)
        self.assertEqual(schema.imports + schema.includes, list(actual))
