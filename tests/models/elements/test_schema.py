from typing import Iterator
from unittest import TestCase

from xsdata.models.elements import Import
from xsdata.models.elements import Include
from xsdata.models.elements import Redefine
from xsdata.models.elements import Schema
from xsdata.models.enums import Namespace


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
            redefines=[
                Redefine.create(schema_location="a.xsd"),
                Redefine.create(schema_location="b.xsd"),
            ],
        )

        actual = schema.sub_schemas()
        expected = schema.imports + schema.includes + schema.redefines
        self.assertIsInstance(actual, Iterator)
        self.assertEqual(expected, list(actual))

    def test_sub_schemas_include_instance_import_if_missing(self):
        schema = Schema.create(nsmap={"foo": Namespace.XSI.value})

        actual = list(schema.sub_schemas())
        self.assertEqual(1, len(actual))
        self.assertEqual(Import.create(namespace=Namespace.XSI.value), actual[0])

        instance_import = Import.create(
            namespace=Namespace.XSI.value, schema_location="somewhere.xsd"
        )
        schema.imports.append(instance_import)
        actual = list(schema.sub_schemas())
        self.assertEqual(1, len(actual))
        self.assertEqual(instance_import, actual[0])
