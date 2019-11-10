from unittest import TestCase

from xsdata.models.elements import Schema, Import, Include


class SchemaTests(TestCase):
    def test_sub_schemas(self):
        schema = Schema.build(
            imports=[
                Import.build(schema_location="../foo.xsd"),
                Import.build(schema_location="../bar.xsd"),
            ],
            includes=[
                Include.build(schema_location="common.xsd"),
                Include.build(schema_location="uncommon.xsd"),
            ]
        )

        expected = [
            "../foo.xsd",
            "../bar.xsd",
            "common.xsd",
            "uncommon.xsd"
        ]
        self.assertEqual(expected, schema.sub_schemas())
