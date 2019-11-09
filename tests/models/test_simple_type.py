import pytest

from tests.testcases import ModelTestCase
from xsdata.models.elements import (
    AnnotationBase,
    BaseModel,
    Enumeration,
    Restriction,
    Schema,
    SimpleType,
)
from xsdata.parser import SchemaParser


class SimpleTypeTests(ModelTestCase):
    result: BaseModel

    @classmethod
    def setUpClass(cls) -> None:
        xsd = cls.fixture_path("simple_types")
        reader = SchemaParser(xsd)
        cls.result = reader.parse()

    def setUp(self) -> None:
        self.assertIsInstance(self.result, Schema)

    def test_with_restriction(self):
        actual: SimpleType = self.result.simple_types[0]

        expected = SimpleType.build(
            name="DeviceType",
            restriction=Restriction.build(
                base="xs:string",
                enumerations=[
                    Enumeration.build(value="mobile"),
                    Enumeration.build(value="tablet"),
                    Enumeration.build(value="desktop"),
                ],
            ),
        )
        self.assertEqual(expected, actual)
        self.assertIsInstance(actual, AnnotationBase)

    @pytest.mark.skip(reason="Missing sample")
    def test_with_list(self):
        pass

    @pytest.mark.skip(reason="Missing sample")
    def test_with_union(self):
        pass
