import pytest

from tests.utils import ModelTestCase
from xsdata.models.elements import (
    AnnotationBase,
    BaseModel,
    Enumeration,
    Restriction,
    Schema,
    SimpleType,
)
from xsdata.schema import SchemaReader


class SimpleTypeTests(ModelTestCase):
    result: BaseModel

    @classmethod
    def setUpClass(cls) -> None:
        xsd = cls.fixture_path("simple_types")
        reader = SchemaReader(xsd)
        cls.result = reader.parse()

    def setUp(self) -> None:
        self.assertIsInstance(self.result, Schema)

    def test_with_restriction(self):
        actual: SimpleType = self.result.simple_types[0]

        expected = SimpleType.from_partial(
            name="DeviceType",
            restriction=Restriction.from_partial(
                base="xs:string",
                enumerations=[
                    Enumeration.from_partial(value="mobile"),
                    Enumeration.from_partial(value="tablet"),
                    Enumeration.from_partial(value="desktop"),
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
