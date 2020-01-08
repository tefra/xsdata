from pathlib import Path

from tests.factories import AttrFactory, ClassFactory, FactoryTestCase
from xsdata.formats.plantuml.generator import PlantUmlGenerator
from xsdata.models.elements import Schema


class PlantUmlGeneratorTests(FactoryTestCase):
    def test_render(self):
        schema = Schema.create(location=Path("foo.xsd"))
        package = "some.Foo.Some.ThugLife"
        classes = [
            ClassFactory.create(attrs=AttrFactory.list(2)),
            ClassFactory.create(attrs=AttrFactory.list(3)),
        ]

        iterator = PlantUmlGenerator().render(schema, classes, package)

        actual = [(file, output) for file, output in iterator]
        self.assertEqual(1, len(actual))
        self.assertEqual(2, len(actual[0]))
        self.assertIsInstance(actual[0][0], Path)
        self.assertTrue(actual[0][0].is_absolute())
        self.assertEqual(
            "some/Foo/Some/ThugLife/foo.pu",
            str(actual[0][0].relative_to(Path.cwd())),
        )

        output = """@startuml

class class_B {
    +attr_B : xs:string
    +attr_C : xs:string
}
class class_C {
    +attr_D : xs:string
    +attr_E : xs:string
    +attr_F : xs:string
}

@enduml"""
        self.assertEqual(output, actual[0][1])
