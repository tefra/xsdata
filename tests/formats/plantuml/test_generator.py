from pathlib import Path

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.formats.plantuml.generator import PlantUmlGenerator


class PlantUmlGeneratorTests(FactoryTestCase):
    def test_render(self):
        classes = [
            ClassFactory.elements(2),
            ClassFactory.elements(3),
        ]

        iterator = PlantUmlGenerator().render(classes)

        actual = [out for out in iterator]
        self.assertEqual(1, len(actual))
        self.assertEqual(3, len(actual[0]))
        self.assertIsInstance(actual[0][0], Path)
        self.assertTrue(actual[0][0].is_absolute())
        self.assertEqual("foo.tests", actual[0][1])
        self.assertEqual("foo/tests.pu", str(actual[0][0].relative_to(Path.cwd())))

        output = """@startuml

class class_B {
    +attr_B : string
    +attr_C : string
}
class class_C {
    +attr_D : string
    +attr_E : string
    +attr_F : string
}

@enduml"""
        self.assertEqual(output, actual[0][2])
