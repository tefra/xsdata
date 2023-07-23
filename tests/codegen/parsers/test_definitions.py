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
        parser = DefinitionsParser(location="here.wsdl")
        definitions = parser.from_path(path, Definitions)

        self.assertIsInstance(definitions, Definitions)
        self.assertEqual(1, len(definitions.services))
        self.assertEqual(2, len(definitions.bindings))
        self.assertEqual(1, len(definitions.port_types))
        self.assertEqual(1, len(definitions.types.schemas))
        self.assertEqual(8, len(definitions.messages))
        self.assertEqual(parser.location, definitions.bindings[0].location)

    def test_end_import(self):
        parser = DefinitionsParser(location="foo/bar.wsdl")
        imp = Import(location="../hello/foo.wsdl")

        parser.end_import(imp)
        self.assertEqual("hello/foo.wsdl", imp.location)

        parser.location = None
        parser.end_import(imp)
        self.assertEqual("hello/foo.wsdl", imp.location)
