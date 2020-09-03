from dataclasses import dataclass
from dataclasses import field
from decimal import Decimal
from typing import List

from xsdata.formats.dataclass.parsers import XmlParser


@dataclass
class Currency:
    id: int = field(metadata=dict(type="Attribute", name="ID"))
    name: str = field(metadata=dict(type="Attribute", name="Name"))
    num_code: int = field(metadata=dict(name="NumCode"))
    iso_code: str = field(metadata=dict(name="CharCode"))
    nominal: int = field(metadata=dict(name="Nominal"))
    value: Decimal = field(metadata=dict(name="Value"))


@dataclass
class Currencies:
    class Meta:
        name = "ValCurs"

    date: str = field(metadata=dict(type="Attribute", name="Date"))
    name: str = field(metadata=dict(type="Attribute"))
    values: List[Currency] = field(default_factory=list, metadata=dict(name="Valute"))


xml = """
<ValCurs Date="19.04.2020" name="Official exchange rate">
    <Valute ID="47">
        <NumCode>978</NumCode>
        <CharCode>EUR</CharCode>
        <Nominal>1</Nominal>
        <Name>Euro</Name>
        <Value>19.2743</Value>
    </Valute>
    <Valute ID="44">
        <NumCode>840</NumCode>
        <CharCode>USD</CharCode>
        <Nominal>1</Nominal>
        <Name>US Dollar</Name>
        <Value>17.7177</Value>
    </Valute>
</ValCurs>
"""

result = XmlParser().from_string(xml, Currencies)
assert result == Currencies(
    date="19.04.2020",
    name="Official exchange rate",
    values=[
        Currency(
            id=47,
            name="Euro",
            num_code=978,
            iso_code="EUR",
            nominal=1,
            value=Decimal("19.2743"),
        ),
        Currency(
            id=44,
            name="US Dollar",
            num_code=840,
            iso_code="USD",
            nominal=1,
            value=Decimal("17.7177"),
        ),
    ],
)
