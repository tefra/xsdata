from unittest import TestCase

from tests import fixtures_dir
from xsdata.codegen.parsers import DefinitionsParser
from xsdata.models.wsdl import Definitions
from xsdata.models.wsdl import Import


class DefinitionsParserTests(TestCase):
    def setUp(self):
        self.parser = DefinitionsParser()
        super().setUp()

    def test_complete(self):
        path = fixtures_dir.joinpath("calculator/services.wsdl").resolve()
        parser = DefinitionsParser()
        definitions = parser.from_path(path, Definitions)

        self.assertIsInstance(definitions, Definitions)
        self.assertEqual(1, len(definitions.services))
        self.assertEqual(2, len(definitions.bindings))
        self.assertEqual(1, len(definitions.port_types))
        self.assertEqual(1, len(definitions.types.schemas))
        self.assertEqual(8, len(definitions.messages))

    def test_end_definitions(self):
        parser = DefinitionsParser()
        definitions = Definitions(
            imports=[Import(location="../foo.xsd"), Import(location="bar.xsd")]
        )

        parser.end_definitions(definitions)
        self.assertEqual("bar.xsd", definitions.imports[1].location)

        parser.location = "file://a/b/services/parent.wsdl"
        parser.end_definitions(definitions)
        self.assertEqual("file://a/b/foo.xsd", definitions.imports[0].location)
        self.assertEqual("file://a/b/services/bar.xsd", definitions.imports[1].location)

        # Update only Definitions instances
        parser.end_definitions("foo")
