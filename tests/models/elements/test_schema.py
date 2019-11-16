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

        expected = ["../foo.xsd", "../bar.xsd", "common.xsd", "uncommon.xsd"]
        self.assertEqual(expected, schema.sub_schemas())
