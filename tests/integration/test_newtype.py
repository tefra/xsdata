from dataclasses import dataclass, field, make_dataclass
from decimal import Decimal
from typing import NewType

import pytest

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.parsers import JsonParser, XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer

Speed = NewType("Speed", float)
Count = NewType("Count", int)
Label = NewType("Label", str)
NestedCount = NewType("NestedCount", Count)
Counts = NewType("Counts", list[Count])
Attributes = NewType("Attributes", dict[Label, Label])


@dataclass
class Car:
    speed: Speed = field(metadata={"type": "Attribute"})


@dataclass
class Child:
    id: int = field(metadata={"type": "Element"})


AliasedChild = NewType("AliasedChild", Child)


@pytest.mark.parametrize("parser", [XmlParser, JsonParser])
def test_newtype_attribute_uses_the_underlying_converter(parser) -> None:
    source = '<Car speed="100.5"/>' if parser is XmlParser else '{"speed": 100.5}'
    result = parser().from_string(source, Car)
    assert result == Car(Speed(100.5))
    assert type(result.speed) is float
    assert Car.__annotations__["speed"] is Speed


@pytest.mark.parametrize(
    "annotation,metadata,xml,json,expected",
    [
        (NestedCount, {"type": "Element"}, "<value>7</value>", '{"value": 7}', 7),
        (Count, {"type": "Text"}, "7", '{"value": 7}', 7),
        (Count | None, {"type": "Element"}, "", "{}", None),
        (
            Count | Decimal,
            {"type": "Element"},
            "<value>1.25</value>",
            '{"value": "1.25"}',
            Decimal("1.25"),
        ),
        (
            list[Label],
            {"type": "Element"},
            "<value>a</value><value>b</value>",
            '{"value": ["a", "b"]}',
            ["a", "b"],
        ),
        (
            Counts,
            {"type": "Element"},
            "<value>1</value><value>2</value>",
            '{"value": [1, 2]}',
            [1, 2],
        ),
        (
            Counts | None,
            {"type": "Element"},
            "<value>1</value><value>2</value>",
            '{"value": [1, 2]}',
            [1, 2],
        ),
        (
            Attributes,
            {"type": "Attributes"},
            'code="a" lang="en"',
            '{"value": {"code": "a", "lang": "en"}}',
            {"code": "a", "lang": "en"},
        ),
        (
            AliasedChild,
            {"type": "Element"},
            "<value><id>3</id></value>",
            '{"value": {"id": 3}}',
            Child(id=3),
        ),
        (
            list[Count],
            {"type": "Attribute", "tokens": True},
            'value="1 2"',
            '{"value": [1, 2]}',
            [1, 2],
        ),
        (
            list[list[Count]],
            {"type": "Element", "tokens": True},
            "<value>1 2</value><value>3</value>",
            '{"value": [[1, 2], [3]]}',
            [[1, 2], [3]],
        ),
    ],
)
@pytest.mark.parametrize("format", ["xml", "json"])
def test_newtype_fields_parse_and_serialize_like_their_supertypes(
    annotation, metadata, xml, json, expected, format
) -> None:
    model = make_dataclass(
        "Model", [("value", annotation, field(default=None, metadata=metadata))]
    )
    if format == "xml":
        source = (
            f"<Model {xml}/>"
            if metadata["type"] in ("Attribute", "Attributes")
            else f"<Model>{xml}</Model>"
        )
        parser, serializer = XmlParser(), XmlSerializer()
    else:
        source = json
        parser, serializer = JsonParser(), JsonSerializer()
    result = parser.from_string(source, model)
    assert result.value == expected
    assert parser.from_string(serializer.render(result), model) == result


@pytest.mark.parametrize("annotation", [set[Count], list[list[Count]]])
def test_newtype_does_not_make_unsupported_attribute_containers_valid(
    annotation,
) -> None:
    model = make_dataclass(
        "Model",
        [("value", annotation, field(default=None, metadata={"type": "Attribute"}))],
    )
    with pytest.raises(XmlContextError, match="does not support typing"):
        XmlParser().from_string('<Model value="1"/>', model)


@pytest.mark.parametrize("annotation,expected", [(int, 7), (str, "7"), (float, 7.0)])
def test_existing_scalar_annotations_keep_their_converters(
    annotation, expected
) -> None:
    model = make_dataclass(
        "Model", [("value", annotation, field(metadata={"type": "Attribute"}))]
    )
    result = XmlParser().from_string('<Model value="7"/>', model)
    assert result.value == expected
    assert type(result.value) is annotation
