from unittest import TestCase

from tests.fixtures.typemapping.city import City
from tests.fixtures.typemapping.house import House
from tests.fixtures.typemapping.street import Street
from xsdata.formats.dataclass.serializers import (
    JsonSerializer,
    PycodeSerializer,
    XmlSerializer,
)
from xsdata.formats.dataclass.serializers.config import SerializerConfig


class TypeMappingTests(TestCase):
    def test_type_mapping(self) -> None:
        city1 = City(name="footown")
        street1 = Street(name="foostreet")
        house1 = House(number=23)
        city1.streets.append(street1)
        street1.houses.append(house1)

        type_mapping = {"City": City, "Street": Street, "House": House}
        serializer_config = SerializerConfig(globalns=type_mapping)

        json_serializer = JsonSerializer(config=serializer_config)
        xml_serializer = XmlSerializer(config=serializer_config)
        pycode_serializer = PycodeSerializer()

        for model in (city1, street1, house1):
            json_serializer.render(model)
            xml_serializer.render(model)
            pycode_serializer.render(model)
