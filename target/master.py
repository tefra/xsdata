from dataclasses import dataclass, field


@dataclass
class CompanyIdentificationType:

    pass


@dataclass
class AlphaNumericStringLength0To1:
    """Format limitations: an..1"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 0.0,
            "max_length": 1.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength0To18:
    """Format limitations: an..18"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 0.0,
            "max_length": 18.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength0To3:
    """Format limitations: an..3"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 0.0,
            "max_length": 3.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To1:
    """Format limitations: an1"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 1.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To10:
    """Format limitations: an..10"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 10.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To12:
    """Format limitations: an..12"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 12.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To18:
    """Format limitations: an..18"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 18.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To2:
    """Format limitations: an..2"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 2.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To20:
    """Format limitations: an..20"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 20.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To25:
    """Format limitations: an..25"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 25.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To250:
    """Format limitations: an..250"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 250.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To256:
    """Format limitations: an..256"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 256.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To28:
    """Format limitations: an..28"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 28.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To3:
    """Format limitations: an..3"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 3.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To30:
    """Format limitations: an..30"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 30.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To35:
    """Format limitations: an..35"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 35.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To4:
    """Format limitations: an..4"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 4.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To5:
    """Format limitations: an..5"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 5.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To50:
    """Format limitations: an..50"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 50.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To6:
    """Format limitations: an..6"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 6.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To7:
    """Format limitations: an..7"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 7.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To70:
    """Format limitations: an..70"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 70.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To8:
    """Format limitations: an..8"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 8.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength1To9:
    """Format limitations: an..9"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 9.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength2To3:
    """Format limitations: an2..3"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 2.0,
            "max_length": 3.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength3To5:
    """Format limitations: an3..5"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 3.0,
            "max_length": 5.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaNumericStringLength6To6:
    """Format limitations: an6"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 6.0,
            "max_length": 6.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaStringLength0To1:
    """Format limitations: a..1"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 0.0,
            "max_length": 1.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaStringLength1To1:
    """Format limitations: a1"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 1.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaStringLength1To2:
    """Format limitations: a..2"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 2.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaStringLength1To3:
    """Format limitations: a..3"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 1.0,
            "max_length": 3.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaStringLength3To3:
    """Format limitations: a3"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 3.0,
            "max_length": 3.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AlphaStringLength3To5:
    """Format limitations: a3..5"""

    value: str = field(
        default=None,
        metadata={
            "min_length": 3.0,
            "max_length": 5.0,
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AmaEdicodesetTypeLength1:
    """Used for codes in the AMADEUS code tables. Code Length is one alphanumeric character."""

    value: str = field(
        default=None,
        metadata={
            "pattern": "[0-9A-Z]",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AmaEdicodesetTypeLength1to3:
    """Used for codes in the AMADEUS code tables. Code Length is three alphanumeric characters."""

    value: str = field(
        default=None,
        metadata={
            "pattern": "[0-9A-Z]{1,3}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class DateDdmmyy:
    """Date format: DDMMYY"""

    value: str = field(
        default=None,
        metadata={
            "pattern": "(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class DateYyyymmdd:
    """Date format: YYYYMMDD"""

    value: str = field(
        default=None,
        metadata={
            "pattern": "[0-9]{4}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericDecimalLength1To12:
    """Format limitations: n..12"""

    value: float = field(
        default=None,
        metadata={"name": "value", "type": "Restriction", "help": None},
    )


@dataclass
class NumericDecimalLength1To18:
    """Format limitations: n..18"""

    value: float = field(
        default=None,
        metadata={"name": "value", "type": "Restriction", "help": None},
    )


@dataclass
class NumericIntegerLength0To3:
    """Format limitations: n..3"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{0,3}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength0To35:
    """Format limitations: n..35"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{0,35}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength1To1:
    """Format limitations: n1"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{1,1}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength1To15:
    """Format limitations: n..15"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{1,15}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength1To18:
    """Format limitations: n..18"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{1,18}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength1To2:
    """Format limitations: n..2"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{1,2}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength1To3:
    """Format limitations: n..3"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{1,3}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength1To4:
    """Format limitations: n..4"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{1,4}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength1To6:
    """Format limitations: n..6"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{1,6}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength1To8:
    """Format limitations: n..8"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{1,8}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength1To9:
    """Format limitations: n..9"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{1,9}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class NumericIntegerLength4To4:
    """Format limitations: n4"""

    value: int = field(
        default=None,
        metadata={
            "pattern": "-?[0-9]{4,4}",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class Time24Hhmm:
    """Time format: 24H. All digits are mandatory . Example: from 0000 to 2359"""

    value: str = field(
        default=None,
        metadata={
            "pattern": "([0-1][0-9]|2[0-3])[0-5][0-9]",
            "name": "value",
            "type": "Restriction",
            "help": None,
        },
    )


@dataclass
class AdditionalProductDetailsType:

    equipment_type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "equipmentType",
            "type": "Element",
            "help": "Type of aircraft",
        },
    )
    operating_day: AlphaNumericStringLength1To7 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "operatingDay",
            "type": "Element",
            "help": "Day number of the week",
        },
    )
    tech_stop_number: NumericIntegerLength1To2 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "techStopNumber",
            "type": "Element",
            "help": "Number of stops made in a journey if different from 0",
        },
    )
    location_id: AlphaStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "locationId",
            "type": "Element",
            "help": "Location places of the stops",
        },
    )


@dataclass
class AdditionalProductTypeI:
    """Additional details describing a specific means of transport."""

    equipment: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "equipment",
            "type": "Element",
            "help": "Equipment type",
        },
    )
    duration: NumericIntegerLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "duration",
            "type": "Element",
            "help": "Elaps flying time of the leg",
        },
    )
    complexing_flight_indicator: AlphaNumericStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "complexingFlightIndicator",
            "type": "Element",
            "help": "COG indicator",
        },
    )


@dataclass
class AgentIdentificationType:

    arc_number: AlphaNumericStringLength1To12 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "arcNumber",
            "type": "Element",
            "help": "Contains ARC number",
        },
    )
    ersp_number: AlphaNumericStringLength1To12 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "erspNumber",
            "type": "Element",
            "help": "ERSP number of the Office or Customer",
        },
    )
    iata_number: AlphaNumericStringLength1To12 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "iataNumber",
            "type": "Element",
            "help": "IATA Number",
        },
    )


@dataclass
class ArithmeticEvaluationType:

    code_operator: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "codeOperator",
            "type": "Element",
            "help": "Boolean operator",
        },
    )


@dataclass
class ArrivalLocationDetailsType:

    distance: NumericIntegerLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "distance",
            "type": "Element",
            "help": "For Radius: This is the length of the requested radius around the location of destination.",
        },
    )
    distance_unit: AlphaNumericStringLength0To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "distanceUnit",
            "type": "Element",
            "help": "Distance unit qualifier for radius",
        },
    )
    location_id: AlphaStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "locationId",
            "type": "Element",
            "help": "ATA/IATA airport/city code of arrival In case of SP request from a PNR, this field is empty.",
        },
    )
    airport_city_qualifier: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "airportCityQualifier",
            "type": "Element",
            "help": "Request from no PNR A = consider the locationID specified as an airport (used only when ambiguous) C = consider the locationId as a city (used only when ambiguous) A and C are not used in case of a request from PNR Request from a PNR with Radius option: O = radius applies to the origin of the PNR segments D = radius applies to the destination of the PNR segments",
        },
    )
    latitude: AlphaNumericStringLength6To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "latitude",
            "type": "Element",
            "help": "Latitude in degrees (decimal format) with hemisphere N=north S=south",
        },
    )
    longitude: AlphaNumericStringLength6To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "longitude",
            "type": "Element",
            "help": "Longitude in degrees (decimal format) with hemisphere E=east, W=west",
        },
    )


@dataclass
class ArrivalLocationDetailsType120834C:

    distance: NumericIntegerLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "distance",
            "type": "Element",
            "help": "For Radius: This is the length of the requested radius around the location of origin.",
        },
    )
    distance_unit: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "distanceUnit",
            "type": "Element",
            "help": "Distance unit qualifier for radius",
        },
    )
    location_id: AlphaStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "locationId",
            "type": "Element",
            "help": "ATA/IATA airport/city code of arrival In case of SP request from a PNR, this field is empty.",
        },
    )
    airport_city_qualifier: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "airportCityQualifier",
            "type": "Element",
            "help": "Request from no PNR A = consider the locationID specified as an airport (used only when ambiguous) C = consider the locationId as a city (used only when ambiguous) A and C are not used in case of a request from PNR Request from a PNR with Radius option: O = radius applies to the origin of the PNR segments D = radius applies to the destination of the PNR segments",
        },
    )
    latitude: AlphaNumericStringLength6To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "latitude",
            "type": "Element",
            "help": "Latitude in degrees (decimal format) with hemisphere N=north S=south",
        },
    )
    longitude: AlphaNumericStringLength6To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "longitude",
            "type": "Element",
            "help": "Longitude in degrees (decimal format) with hemisphere E=east, W=west",
        },
    )


@dataclass
class AttributeDetailsType:

    requested_sgt: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "requestedSgt",
            "type": "Element",
            "help": "Reference of the requested segment",
        },
    )
    value: AlphaNumericStringLength1To20 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 50,
            "name": "value",
            "type": "Element",
            "help": "List of airlines, cabins, time window, number of connections.",
        },
    )


@dataclass
class AttributeInformationType:
    """To identify the type of attribute and the attribute"""

    option: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "option",
            "type": "Element",
            "help": "Code of options",
        },
    )
    option_information: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "optionInformation",
            "type": "Element",
            "help": "Mandatory when alternate date option is used (ALT), must be set to plus (P) or minus (M) a number of days around the original PNR segment dates. E.g.: M1 (for minus 1 day) or P100 (for plus 100 days)",
        },
    )


@dataclass
class AttributeInformationType97181C:
    """To identify the type of attribute and the attribute"""

    attribute_type: AlphaNumericStringLength1To25 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "attributeType",
            "type": "Element",
            "help": "Attribute type",
        },
    )
    attribute_description: AlphaNumericStringLength1To256 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "attributeDescription",
            "type": "Element",
            "help": "Attribute description",
        },
    )


@dataclass
class BucketInformationType:

    number: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "number",
            "type": "Element",
            "help": "Number",
        },
    )
    name: AlphaNumericStringLength1To20 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "name",
            "type": "Element",
            "help": "Name",
        },
    )
    completion: AmaEdicodesetTypeLength1to3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "completion",
            "type": "Element",
            "help": "Completion",
        },
    )
    mode: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "mode",
            "type": "Element",
            "help": "Mode",
        },
    )
    value_ref: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "valueRef",
            "type": "Element",
            "help": "Value reference",
        },
    )
    weight: NumericIntegerLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "weight",
            "type": "Element",
            "help": "Weight",
        },
    )
    count: NumericIntegerLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "count",
            "type": "Element",
            "help": "Number of solutions in the bucket",
        },
    )
    attribute_count: NumericIntegerLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "attributeCount",
            "type": "Element",
            "help": "Number of solutions per attribute",
        },
    )


@dataclass
class CabinClassDesignationType:
    """Cabin class designation"""

    cabin_designator: AlphaNumericStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "cabinDesignator",
            "type": "Element",
            "help": "Cabin designator.",
        },
    )


@dataclass
class CabinIdentificationType:

    cabin_qualifier: AlphaNumericStringLength1To2 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "cabinQualifier",
            "type": "Element",
            "help": "Cabin qualifier. For Star Pricer,MD stands for Mandatory Cabin qualifier. For other products no qualifier stands for Mandatory Cabin.",
        },
    )
    cabin: AlphaStringLength0To1 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 3,
            "name": "cabin",
            "type": "Element",
            "help": "Cabin",
        },
    )


@dataclass
class CabinIdentificationType233500C:

    cabin_qualifier: AlphaNumericStringLength1To2 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "cabinQualifier",
            "type": "Element",
            "help": "Cabin qualifier. For Star Pricer,MD stands for Mandatory Cabin qualifier. For other products no qualifier stands for Mandatory Cabin.",
        },
    )
    cabin: AlphaStringLength0To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "cabin",
            "type": "Element",
            "help": "Cabin",
        },
    )


@dataclass
class CabinProductDetailsType:

    rbd: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "rbd",
            "type": "Element",
            "help": "Reservation booking designator - RBD",
        },
    )
    booking_modifier: AmaEdicodesetTypeLength1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "bookingModifier",
            "type": "Element",
            "help": "Reservation Booking Modifier",
        },
    )
    cabin: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "cabin",
            "type": "Element",
            "help": "Indicates the cabin related to the Booking code",
        },
    )
    avl_status: AmaEdicodesetTypeLength1to3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "avlStatus",
            "type": "Element",
            "help": "Availibility status : posting level",
        },
    )


@dataclass
class CodedAttributeInformationType:
    """Attribute information"""

    attribute_type: AlphaNumericStringLength1To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "attributeType",
            "type": "Element",
            "help": "Attribute type identification",
        },
    )
    attribute_description: AlphaNumericStringLength1To20 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "attributeDescription",
            "type": "Element",
            "help": "Attribute Description",
        },
    )


@dataclass
class CodedAttributeInformationType120742C:
    """Convey coded key and corresponding value"""

    name: AlphaNumericStringLength1To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "name",
            "type": "Element",
            "help": "Name.",
        },
    )
    value: AlphaNumericStringLength1To20 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 10,
            "name": "value",
            "type": "Element",
            "help": "Value.",
        },
    )


@dataclass
class CodedAttributeInformationType139508C:
    """Convey coded key and corresponding value"""

    type: AlphaNumericStringLength1To5 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "type",
            "type": "Element",
            "help": "Attribute type",
        },
    )
    value: AlphaNumericStringLength1To20 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 10,
            "name": "value",
            "type": "Element",
            "help": "Value.",
        },
    )


@dataclass
class CodedAttributeInformationType247828C:
    """Convey coded key and corresponding value"""

    attribute_type: AlphaNumericStringLength1To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "attributeType",
            "type": "Element",
            "help": None,
        },
    )
    attribute_description: AlphaNumericStringLength1To10 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "attributeDescription",
            "type": "Element",
            "help": "Attribute description",
        },
    )


@dataclass
class CodedAttributeInformationType254574C:
    """Convey coded key and corresponding value"""

    attribute_type: AlphaNumericStringLength1To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "attributeType",
            "type": "Element",
            "help": "Attribute type",
        },
    )
    attribute_description: AlphaNumericStringLength1To50 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "attributeDescription",
            "type": "Element",
            "help": "Attribute description",
        },
    )


@dataclass
class CodedAttributeInformationType275401C:
    """Convey coded key and corresponding value"""

    fee_type: AlphaNumericStringLength1To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "feeType",
            "type": "Element",
            "help": "Type of fee/reduction",
        },
    )
    fee_id_number: AlphaNumericStringLength1To50 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "feeIdNumber",
            "type": "Element",
            "help": "Fee Id Number",
        },
    )


@dataclass
class CompanyIdentificationType120719C:

    carrier_qualifier: AlphaNumericStringLength0To1 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "carrierQualifier",
            "type": "Element",
            "help": "Item description identification.",
        },
    )
    carrier_id: AlphaNumericStringLength2To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 99,
            "name": "carrierId",
            "type": "Element",
            "help": "carrier id",
        },
    )


@dataclass
class CompanyIdentificationType195544C:

    marketing_carrier: AlphaNumericStringLength2To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "marketingCarrier",
            "type": "Element",
            "help": "Marketing carrier",
        },
    )
    operating_carrier: AlphaNumericStringLength2To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "operatingCarrier",
            "type": "Element",
            "help": "Operating carrier",
        },
    )


@dataclass
class CompanyIdentificationType275415C:

    carrier_qualifier: AlphaNumericStringLength0To1 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "carrierQualifier",
            "type": "Element",
            "help": "Item description identification.",
        },
    )
    carrier_id: AlphaNumericStringLength2To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "carrierId",
            "type": "Element",
            "help": "carrier id",
        },
    )


@dataclass
class CompanyIdentificationTypeI:
    """Code or name to identify a company and any associated companies."""

    marketing_company: AlphaNumericStringLength2To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "marketingCompany",
            "type": "Element",
            "help": "Carrier code",
        },
    )


@dataclass
class CompanyRoleIdentificationType:
    """To indicate commercial agreements related to the service being provided."""

    transport_stage_qualifier: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "transportStageQualifier",
            "type": "Element",
            "help": "Codeshare qualifier",
        },
    )
    airline_designator: AlphaNumericStringLength2To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "airlineDesignator",
            "type": "Element",
            "help": "company identification",
        },
    )
    flight_number: NumericIntegerLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightNumber",
            "type": "Element",
            "help": "flight number",
        },
    )
    operational_suffix: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "operationalSuffix",
            "type": "Element",
            "help": "suffix",
        },
    )


@dataclass
class CompanyRoleIdentificationType120761C:
    """To indicate commercial agreements related to the service being provided."""

    code_share_type: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "codeShareType",
            "type": "Element",
            "help": "Type of code share agreement.",
        },
    )
    airline_designator: AlphaNumericStringLength2To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "airlineDesignator",
            "type": "Element",
            "help": "company identification",
        },
    )
    flight_number: NumericIntegerLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightNumber",
            "type": "Element",
            "help": "flight number",
        },
    )


@dataclass
class ConnectPointDetailsType:

    exclusion_identifier: AlphaStringLength0To1 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "exclusionIdentifier",
            "type": "Element",
            "help": "Exclusion identification",
        },
    )
    location_id: AlphaStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "locationId",
            "type": "Element",
            "help": "Place or Location identification",
        },
    )
    airport_city_qualifier: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "airportCityQualifier",
            "type": "Element",
            "help": "Airport/city qualifier",
        },
    )


@dataclass
class ConnectPointDetailsType195492C:

    inclusion_identifier: AlphaNumericStringLength0To1 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "inclusionIdentifier",
            "type": "Element",
            "help": "Inclusion identification",
        },
    )
    location_id: AlphaStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "locationId",
            "type": "Element",
            "help": "Place or Location identification",
        },
    )
    airport_city_qualifier: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "airportCityQualifier",
            "type": "Element",
            "help": "Airport/city qualifier",
        },
    )


@dataclass
class ConnectionDetailsTypeI:
    """To specify the location, product supplier and time for a connection with the next means of transport."""

    location: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "location",
            "type": "Element",
            "help": "Location",
        },
    )


@dataclass
class ConsumerReferenceIdentificationTypeI:
    """Identification of consumer references by type, company, number and reference to a traveller."""

    reference_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "referenceQualifier",
            "type": "Element",
            "help": None,
        },
    )
    reference_number: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "referenceNumber",
            "type": "Element",
            "help": None,
        },
    )
    reference_party_name: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "referencePartyName",
            "type": "Element",
            "help": None,
        },
    )
    traveller_reference_nbr: AlphaNumericStringLength1To10 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "travellerReferenceNbr",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class ConversionRateDetailsType:

    conversion_type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "conversionType",
            "type": "Element",
            "help": "Conversion type",
        },
    )
    currency: AlphaStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "currency",
            "type": "Element",
            "help": "Currency",
        },
    )


@dataclass
class CorporateFareIdentifiersType:

    fare_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "fareQualifier",
            "type": "Element",
            "help": "Indicates the type of corporate fares requested",
        },
    )
    identify_number: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "identifyNumber",
            "type": "Element",
            "help": "Corporate contract number or name",
        },
    )


@dataclass
class CorporateIdentityType:
    """Corporate fare types indicated in PTK are detailed"""

    corporate_qualifier: AlphaNumericStringLength0To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "corporateQualifier",
            "type": "Element",
            "help": "Indicates if 1A corporate (RC) or Unifare corporate (RW) requested.",
        },
    )
    identity: AlphaNumericStringLength1To20 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 9,
            "name": "identity",
            "type": "Element",
            "help": "Corporate contract number or name",
        },
    )


@dataclass
class CriteriaiDetaislType:
    """Criteria details : weights/parameters list"""

    type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "type",
            "type": "Element",
            "help": None,
        },
    )
    value: AlphaNumericStringLength1To18 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "value",
            "type": "Element",
            "help": None,
        },
    )
    attribute: AlphaNumericStringLength1To9 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "attribute",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class DataInformationType:
    """To identify specific data and a quantity related to the data."""

    indicator: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "indicator",
            "type": "Element",
            "help": "Ancillary services options",
        },
    )


@dataclass
class DataTypeInformationType:
    """To identify the type of data to be sent and to qualify the data when required."""

    sub_type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "subType",
            "type": "Element",
            "help": "Carrier fee code",
        },
    )
    option: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "option",
            "type": "Element",
            "help": "Status (automated, manually added, exempted). Default is automated",
        },
    )


@dataclass
class DateAndTimeDetailsType:
    """DATE AND TIME DETAILS"""

    flexibility_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flexibilityQualifier",
            "type": "Element",
            "help": "Trip Duration type(Plus,Minus,Combined)",
        },
    )
    trip_interval: NumericIntegerLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "tripInterval",
            "type": "Element",
            "help": "Number of days added or/and retrieved to the trip duration",
        },
    )
    trip_duration: NumericIntegerLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "tripDuration",
            "type": "Element",
            "help": "Period between date of departure and date of arrival",
        },
    )


@dataclass
class DateAndTimeDetailsType120762C:

    date_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "dateQualifier",
            "type": "Element",
            "help": "Date time period qualifier",
        },
    )
    date: DateDdmmyy = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "date",
            "type": "Element",
            "help": "First Date",
        },
    )
    first_time: Time24Hhmm = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "firstTime",
            "type": "Element",
            "help": "First Time",
        },
    )
    equipement_type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "equipementType",
            "type": "Element",
            "help": "Movement type.",
        },
    )
    location_id: AlphaNumericStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "locationId",
            "type": "Element",
            "help": "Place/location identification.",
        },
    )


@dataclass
class DateAndTimeDetailsType254619C:
    """DATE AND TIME DETAILS"""

    range_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "rangeQualifier",
            "type": "Element",
            "help": "To identify type of range (Plus,Minus or combined)",
        },
    )
    day_interval: NumericIntegerLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "dayInterval",
            "type": "Element",
            "help": "Range of dates : Number of Days preceding or/and Following the request departure date",
        },
    )
    time_atdestination: Time24Hhmm = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "timeAtdestination",
            "type": "Element",
            "help": "Time at destination (local)",
        },
    )


@dataclass
class DateAndTimeDetailsTypeI:
    """DATE AND TIME DETAILS"""

    time_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "timeQualifier",
            "type": "Element",
            "help": "Toidentify type of time Arrival/Departure",
        },
    )
    date: DateDdmmyy = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "date",
            "type": "Element",
            "help": "Date",
        },
    )
    time: Time24Hhmm = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "time",
            "type": "Element",
            "help": "Time",
        },
    )
    time_window: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "timeWindow",
            "type": "Element",
            "help": "Time window size in hours",
        },
    )


@dataclass
class DateAndTimeDetailsTypeI120740C:

    qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "qualifier",
            "type": "Element",
            "help": "Date time period qualifier",
        },
    )
    date: DateDdmmyy = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "date",
            "type": "Element",
            "help": "First Date",
        },
    )
    time: Time24Hhmm = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "time",
            "type": "Element",
            "help": "First Time",
        },
    )
    qualifier2: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "qualifier2",
            "type": "Element",
            "help": ".",
        },
    )
    reserved1: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "reserved1",
            "type": "Element",
            "help": None,
        },
    )
    reserved2: AlphaNumericStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "reserved2",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class DateTimePeriodDetailsTypeI:
    """To indicate period of applicability."""

    qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "qualifier",
            "type": "Element",
            "help": "Qualifier",
        },
    )
    value: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "value",
            "type": "Element",
            "help": "Value",
        },
    )


@dataclass
class FareDetailsType:

    qualifier: AmaEdicodesetTypeLength1to3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "qualifier",
            "type": "Element",
            "help": "Qualifier",
        },
    )
    rate: NumericIntegerLength1To8 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "rate",
            "type": "Element",
            "help": "Rate",
        },
    )
    country: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "country",
            "type": "Element",
            "help": "Country",
        },
    )
    fare_category: AmaEdicodesetTypeLength1to3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "fareCategory",
            "type": "Element",
            "help": "Fare Category",
        },
    )


@dataclass
class FareFamilyDetailsType:
    """NEW FARE SEARCH"""

    commercial_family: AlphaNumericStringLength1To10 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "commercialFamily",
            "type": "Element",
            "help": "Commercial fare Family Short name",
        },
    )


@dataclass
class FareInformationTypeI:
    """To specify fare details."""

    value_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "valueQualifier",
            "type": "Element",
            "help": "PTC (Full Codeset List described in ATPCo Documentation B11109 Appendix A)",
        },
    )
    value: NumericIntegerLength1To15 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "value",
            "type": "Element",
            "help": "age",
        },
    )


@dataclass
class FareProductDetailsType:

    fare_basis: AlphaNumericStringLength0To18 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "fareBasis",
            "type": "Element",
            "help": "Fare basis code",
        },
    )
    fare_type: AlphaNumericStringLength0To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "fareType",
            "type": "Element",
            "help": "Type of fare",
        },
    )


@dataclass
class FareQualifierInformationType:
    """To specify multiple qualifier for fare selections."""

    fare_family_qual: AlphaNumericStringLength0To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 9,
            "name": "fareFamilyQual",
            "type": "Element",
            "help": "Fare family combinability.",
        },
    )


@dataclass
class FareTypeGroupingInformationType:

    pricing_group: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "pricingGroup",
            "type": "Element",
            "help": "Pricing Group",
        },
    )


@dataclass
class FormOfPaymentDetailsTypeI:
    """To specify the form of payment type, amounts, approval codes, and other related information."""

    type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "type",
            "type": "Element",
            "help": "Form of payment identification",
        },
    )
    charged_amount: NumericDecimalLength1To12 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "chargedAmount",
            "type": "Element",
            "help": "amount to be charged on this form",
        },
    )
    credit_card_number: AlphaNumericStringLength1To20 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "creditCardNumber",
            "type": "Element",
            "help": "Reference number",
        },
    )


@dataclass
class FreeTextDetailsType:

    text_subject_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "textSubjectQualifier",
            "type": "Element",
            "help": "Qualifier of the free text. Always literal in our usage.",
        },
    )
    information_type: AlphaNumericStringLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "informationType",
            "type": "Element",
            "help": "Type of the free text. Always 7 for our usage.",
        },
    )
    source: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "source",
            "type": "Element",
            "help": "Source of the information.",
        },
    )
    encoding: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "encoding",
            "type": "Element",
            "help": "Encoding method used.",
        },
    )


@dataclass
class FrequencyType:
    """Give the days of the week involved for a period"""

    qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "qualifier",
            "type": "Element",
            "help": "Indicate if the sequence number represents days of the week or days of the month.",
        },
    )
    value: NumericIntegerLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 7,
            "name": "value",
            "type": "Element",
            "help": "Used to represent days of the week. 1 is monday and 7 is sunday.",
        },
    )


@dataclass
class FrequentTravellerIdentificationType:

    carrier: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "carrier",
            "type": "Element",
            "help": "Carrier where the FQTV is registered.",
        },
    )
    number: AlphaNumericStringLength1To28 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "number",
            "type": "Element",
            "help": None,
        },
    )
    customer_reference: AlphaNumericStringLength1To10 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "customerReference",
            "type": "Element",
            "help": "Specifies which traveller in the TIF segment the frequent traveller number applies (same as 9944 in TIF).",
        },
    )
    status: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "status",
            "type": "Element",
            "help": "status code: 'OK' if the frequent flyer card has been validated",
        },
    )
    tier_level: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "tierLevel",
            "type": "Element",
            "help": "To specify a Tier linked to the FQTV",
        },
    )
    priority_code: AlphaNumericStringLength1To12 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "priorityCode",
            "type": "Element",
            "help": "For example : priority code",
        },
    )
    tier_description: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "tierDescription",
            "type": "Element",
            "help": "For example : Level description",
        },
    )
    company_code: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "companyCode",
            "type": "Element",
            "help": "For example : Company code of alliance",
        },
    )
    customer_value: NumericIntegerLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "customerValue",
            "type": "Element",
            "help": None,
        },
    )
    type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "type",
            "type": "Element",
            "help": "To specify the product/account number qualifier. (e.g. 2=Corporate Frequent Flyer).",
        },
    )


@dataclass
class FrequentTravellerIdentificationType249074C:
    """Identification of the frequent traveller number by company code with the capability to reference a specific traveller."""

    carrier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "carrier",
            "type": "Element",
            "help": "carrier",
        },
    )
    number: AlphaNumericStringLength1To25 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "number",
            "type": "Element",
            "help": "Frequent traveller number",
        },
    )
    customer_reference: AlphaNumericStringLength1To10 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "customerReference",
            "type": "Element",
            "help": "Customer reference",
        },
    )
    tier_level: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "tierLevel",
            "type": "Element",
            "help": "Tier level",
        },
    )
    priority_code: AlphaNumericStringLength1To12 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "priorityCode",
            "type": "Element",
            "help": "Priority code",
        },
    )
    tier_description: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "tierDescription",
            "type": "Element",
            "help": "Tier description",
        },
    )
    type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "type",
            "type": "Element",
            "help": "To specify the product/account number qualifier. (e.g. 2=Corporate Frequent Flyer).",
        },
    )


@dataclass
class ItemNumberIdentificationType:
    """Goods identification for a specified source"""

    number: AlphaNumericStringLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "number",
            "type": "Element",
            "help": "Fare family combination number",
        },
    )
    type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "type",
            "type": "Element",
            "help": "Type",
        },
    )
    qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "qualifier",
            "type": "Element",
            "help": "Qualifier",
        },
    )
    responsible_agency: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "responsibleAgency",
            "type": "Element",
            "help": "Responsible agency",
        },
    )


@dataclass
class ItineraryDetailsType:
    """Forces arrival or departure to/from the same city or airport option"""

    airport_city_qualifier: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "airportCityQualifier",
            "type": "Element",
            "help": "Airport/City Qualifier: the passenger wants to depart/arrive from/to the same airport or city in the specified requested segment",
        },
    )
    segment_number: NumericIntegerLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "segmentNumber",
            "type": "Element",
            "help": "Requested segment number",
        },
    )


@dataclass
class LocationDetailsTypeI:

    location_id: AlphaStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "locationId",
            "type": "Element",
            "help": "Place or Location identification",
        },
    )
    country: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "country",
            "type": "Element",
            "help": "Country, coded",
        },
    )


@dataclass
class LocationIdentificationDetailsType:

    location_id: AlphaStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "locationId",
            "type": "Element",
            "help": "3 characters ATA/IATA airport/city code",
        },
    )
    airport_city_qualifier: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "airportCityQualifier",
            "type": "Element",
            "help": "Airport/city qualifier: the requested point is an airport when ambiguity exists (e.g. HOU)",
        },
    )
    terminal: AlphaNumericStringLength1To5 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "terminal",
            "type": "Element",
            "help": "Terminal information",
        },
    )


@dataclass
class LocationTypeI:
    """To identify a location by code or name."""

    true_location_id: AlphaStringLength3To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "trueLocationId",
            "type": "Element",
            "help": "Departure or Arrival IATA airport code",
        },
    )


@dataclass
class MileageTimeDetailsTypeI:
    """Information about the distance/duration of a trip."""

    elapsed_ground_time: NumericIntegerLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "elapsedGroundTime",
            "type": "Element",
            "help": "Ground Time in minutes at Board point (connection with incoming flight)",
        },
    )


@dataclass
class MonetaryAndCabinInformationDetailsType:

    amount_type: AlphaNumericStringLength0To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "amountType",
            "type": "Element",
            "help": "Amount qualifier.",
        },
    )
    amount: NumericDecimalLength1To18 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "amount",
            "type": "Element",
            "help": "Amount",
        },
    )
    currency: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "currency",
            "type": "Element",
            "help": "ISO currency code",
        },
    )
    location_id: AlphaStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "locationId",
            "type": "Element",
            "help": "Airport/city code",
        },
    )
    cabin_class_designator: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "cabinClassDesignator",
            "type": "Element",
            "help": "Cabin class designator",
        },
    )


@dataclass
class MonetaryInformationDetailsTypeI:

    qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "qualifier",
            "type": "Element",
            "help": "Monetary amount type qualifier, coded",
        },
    )
    amount: NumericIntegerLength1To18 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "amount",
            "type": "Element",
            "help": "Allowance or charge number",
        },
    )
    currency: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "currency",
            "type": "Element",
            "help": "Currency, coded",
        },
    )


@dataclass
class MonetaryInformationDetailsTypeI194597C:

    qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "qualifier",
            "type": "Element",
            "help": "Monetary amount type qualifier, coded",
        },
    )
    amount: NumericIntegerLength1To18 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "amount",
            "type": "Element",
            "help": "Allowance or charge number",
        },
    )
    currency: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "currency",
            "type": "Element",
            "help": "Currency, coded",
        },
    )
    location_id: AlphaStringLength3To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "locationId",
            "type": "Element",
            "help": "Place or Location identification",
        },
    )


@dataclass
class MonetaryInformationDetailsTypeI65140C:
    """To specify the type of monetary amount, the amount, and the currency code."""

    type_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "typeQualifier",
            "type": "Element",
            "help": "Qualifier",
        },
    )
    amount: AlphaNumericStringLength1To12 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "amount",
            "type": "Element",
            "help": "Amount",
        },
    )
    currency: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "currency",
            "type": "Element",
            "help": "Currency",
        },
    )


@dataclass
class MonetaryInformationDetailsTypeI65141C:
    """To specify the type of monetary amount, the amount, and the currency code."""

    type_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "typeQualifier",
            "type": "Element",
            "help": "Qualifier",
        },
    )
    amount: AlphaNumericStringLength1To12 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "amount",
            "type": "Element",
            "help": "Amount",
        },
    )
    currency: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "currency",
            "type": "Element",
            "help": "Currency",
        },
    )
    location: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "location",
            "type": "Element",
            "help": "Location",
        },
    )


@dataclass
class MultiCityOptionType:
    """List of requested arrival points"""

    location_id: AlphaStringLength3To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "locationId",
            "type": "Element",
            "help": "ATA/IATA airport/city code of arrival multi city option enable to define until 20 airports/cities",
        },
    )
    airport_city_qualifier: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "airportCityQualifier",
            "type": "Element",
            "help": "Requested arrival point is an airport or a city (default is city and used only when ambiguity)",
        },
    )


@dataclass
class MultipleIdentificationNumbersTypeI:
    """To specify more than one identification number."""

    corporate_number_identifier: AlphaNumericStringLength1To12 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "corporateNumberIdentifier",
            "type": "Element",
            "help": "Corporate number or ALL.",
        },
    )
    corporate_name: AlphaNumericStringLength1To20 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "corporateName",
            "type": "Element",
            "help": "Corporate name.",
        },
    )


@dataclass
class NumberOfUnitDetailsType:

    number_of_units: NumericIntegerLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "numberOfUnits",
            "type": "Element",
            "help": "Number of Units",
        },
    )
    type_of_unit: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "typeOfUnit",
            "type": "Element",
            "help": "Number of unit qualifier",
        },
    )


@dataclass
class NumberOfUnitDetailsType270113C:

    number_of_units: NumericIntegerLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "numberOfUnits",
            "type": "Element",
            "help": "Number of Units",
        },
    )
    type_of_unit: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "typeOfUnit",
            "type": "Element",
            "help": "Number of unit qualifier",
        },
    )


@dataclass
class NumberOfUnitDetailsTypeI:

    number_of_units: NumericIntegerLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "numberOfUnits",
            "type": "Element",
            "help": "Number of Units",
        },
    )
    type_of_unit: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "typeOfUnit",
            "type": "Element",
            "help": "Number of unit qualifier",
        },
    )


@dataclass
class OriginatorIdentificationDetailsTypeI:
    """To identify a user"""

    office_name: NumericIntegerLength1To9 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "officeName",
            "type": "Element",
            "help": "Office Name.",
        },
    )
    agent_signin: AlphaNumericStringLength1To9 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "agentSignin",
            "type": "Element",
            "help": "Agent Sign In .",
        },
    )
    confidential_office: AlphaNumericStringLength1To9 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "confidentialOffice",
            "type": "Element",
            "help": "Confidential Office Name.",
        },
    )
    other_office: AlphaNumericStringLength1To9 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "otherOffice",
            "type": "Element",
            "help": "Other Office Name",
        },
    )


@dataclass
class PnrsegmentReferenceType:
    """Reference to PNR segment"""

    pnr_segment_tattoo: NumericIntegerLength0To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "pnrSegmentTattoo",
            "type": "Element",
            "help": "For a request from PNR: this is the reference number of a PNR air segment. In case a range of PNR segments is specified (eg. segments 2-5), then it is the 1st of the range, the last being in ARR.",
        },
    )
    pnr_segment_qualifier: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "pnrSegmentQualifier",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class PricingTicketingInformationType:
    """To specify indicators related to pricing and ticketing."""

    price_type: AlphaNumericStringLength0To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 50,
            "name": "priceType",
            "type": "Element",
            "help": "Price type qualifier",
        },
    )


@dataclass
class ProductDateTimeType:
    """Product date or time"""

    date: DateDdmmyy = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "date",
            "type": "Element",
            "help": ".",
        },
    )
    time: Time24Hhmm = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "time",
            "type": "Element",
            "help": ".",
        },
    )


@dataclass
class ProductDateTimeType195546C:

    date_of_departure: DateDdmmyy = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "dateOfDeparture",
            "type": "Element",
            "help": "Departure date",
        },
    )
    time_of_departure: Time24Hhmm = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "timeOfDeparture",
            "type": "Element",
            "help": "Departure time",
        },
    )
    date_of_arrival: DateDdmmyy = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "dateOfArrival",
            "type": "Element",
            "help": "Arrival date",
        },
    )
    time_of_arrival: Time24Hhmm = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "timeOfArrival",
            "type": "Element",
            "help": "Arrival time",
        },
    )
    date_variation: NumericIntegerLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "dateVariation",
            "type": "Element",
            "help": "Arrival date compared to departure date, only if different from 0",
        },
    )


@dataclass
class ProductDateTimeTypeI:
    """To specify the dates and times associated with a product."""

    departure_date: DateYyyymmdd = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "departureDate",
            "type": "Element",
            "help": "Departure date in YYYYMMDD format",
        },
    )
    departure_time: Time24Hhmm = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "departureTime",
            "type": "Element",
            "help": "Departure time",
        },
    )
    arrival_date: DateYyyymmdd = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "arrivalDate",
            "type": "Element",
            "help": "Arrival date",
        },
    )
    arrival_time: Time24Hhmm = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "arrivalTime",
            "type": "Element",
            "help": "Arrival time",
        },
    )
    date_variation: NumericIntegerLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "dateVariation",
            "type": "Element",
            "help": "Day difference between Departure date of the leg and date of reference (Departure or Arrival date specified in the SDI)",
        },
    )


@dataclass
class ProductDateTimeTypeI194583C:
    """To specify the dates and times associated with a product."""

    date: DateDdmmyy = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "date",
            "type": "Element",
            "help": "Ticketing Purchase Date",
        },
    )
    other_date: DateDdmmyy = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "otherDate",
            "type": "Element",
            "help": "Ticketing purchase date",
        },
    )


@dataclass
class ProductDateTimeTypeI194598C:

    date: DateDdmmyy = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "date",
            "type": "Element",
            "help": "First date",
        },
    )
    rtc_date: DateDdmmyy = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "rtcDate",
            "type": "Element",
            "help": "Half round trip combination.",
        },
    )


@dataclass
class ProductFacilitiesType:
    """Level of access"""

    last_seat_available: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "lastSeatAvailable",
            "type": "Element",
            "help": "Yes-No indicator whether Last Seat Available",
        },
    )
    level_of_access: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "levelOfAccess",
            "type": "Element",
            "help": "Level of access",
        },
    )
    electronic_ticketing: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "electronicTicketing",
            "type": "Element",
            "help": "Yes-No indicator whether electronic ticketing",
        },
    )
    operational_suffix: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "operationalSuffix",
            "type": "Element",
            "help": "Product identification suffix",
        },
    )
    product_detail_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "productDetailQualifier",
            "type": "Element",
            "help": "Define whether a flight has been polled or not",
        },
    )
    flight_characteristic: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "flightCharacteristic",
            "type": "Element",
            "help": "Add some flight restrictions (See code set list)",
        },
    )


@dataclass
class ProductIdentificationDetailsTypeI:
    """Code, number or name to identify a specific product or service."""

    flight_number: NumericIntegerLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "flightNumber",
            "type": "Element",
            "help": "Flight number",
        },
    )
    operational_suffix: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "operationalSuffix",
            "type": "Element",
            "help": "Flight suffix",
        },
    )


@dataclass
class ProductIdentificationDetailsTypeI50878C:
    """Code, number or name to identify a specific product or service."""

    flight_number: AlphaNumericStringLength1To5 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "flightNumber",
            "type": "Element",
            "help": None,
        },
    )
    booking_class: AlphaNumericStringLength1To2 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "bookingClass",
            "type": "Element",
            "help": None,
        },
    )
    operational_suffix: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "operationalSuffix",
            "type": "Element",
            "help": None,
        },
    )
    modifier: AlphaNumericStringLength1To7 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "modifier",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class ProductLocationDetailsTypeI:
    """To indicate a location and the type of location."""

    station: AlphaStringLength3To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "station",
            "type": "Element",
            "help": "airport",
        },
    )


@dataclass
class ProductTypeDetailsType:
    """Product type details"""

    sequence_number: AlphaNumericStringLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "sequenceNumber",
            "type": "Element",
            "help": ".",
        },
    )
    availability_context: AlphaNumericStringLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "availabilityContext",
            "type": "Element",
            "help": "PNR availability context",
        },
    )


@dataclass
class ProductTypeDetailsType120801C:

    flight_type: AlphaNumericStringLength1To2 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "flightType",
            "type": "Element",
            "help": "Type of flight",
        },
    )


@dataclass
class ProductTypeDetailsType205137C:
    """To specify additional characteristics of a product or service."""

    avl: AlphaNumericStringLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 9,
            "name": "avl",
            "type": "Element",
            "help": "indicates whether the flight is domestic or international",
        },
    )


@dataclass
class ProductTypeDetailsTypeI:
    """To specify additional characteristics of a product or service."""

    flight_indicator: AlphaStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 5,
            "name": "flightIndicator",
            "type": "Element",
            "help": "Part of the journey (C,E,S), Codeshare service (A), Technical stop at off point in a Direct (TSD), Technical stop at off point in a COG (TSC), E-Ticket candidate (ET), Prohibited Countries (RPC, WPC)",
        },
    )


@dataclass
class ProposedSegmentDetailsType:

    ref: AlphaNumericStringLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "ref",
            "type": "Element",
            "help": "Flight proposal reference",
        },
    )
    unit_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "unitQualifier",
            "type": "Element",
            "help": "Elapse Flying Time",
        },
    )


@dataclass
class ReferencingDetailsType:
    """Referencing details"""

    ref_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "refQualifier",
            "type": "Element",
            "help": "Segment reference qualifier",
        },
    )
    ref_number: NumericIntegerLength0To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "refNumber",
            "type": "Element",
            "help": "Flight or flight group reference",
        },
    )


@dataclass
class SegmentRepetitionControlDetailsTypeI:
    """Information about the number of selection segments to be processed."""

    quantity: NumericIntegerLength1To15 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "quantity",
            "type": "Element",
            "help": "traveller number",
        },
    )


@dataclass
class SelectionDetailsInformationType:
    """To specify a selected option and associated information."""

    type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "type",
            "type": "Element",
            "help": "Carrier fee type",
        },
    )
    option_information: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "optionInformation",
            "type": "Element",
            "help": "Carrier fee status",
        },
    )


@dataclass
class SelectionDetailsInformationTypeI:
    """To specify a selected option and associated information."""

    option: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "option",
            "type": "Element",
            "help": None,
        },
    )
    option_information: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "optionInformation",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class SpecialRequirementsDataDetailsType:
    """Special requirements data details"""

    seat_characteristics: AlphaNumericStringLength1To2 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "seatCharacteristics",
            "type": "Element",
            "help": "SSR seat characteristic",
        },
    )


@dataclass
class SpecialRequirementsTypeDetailsType:

    service_classification: AlphaNumericStringLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "serviceClassification",
            "type": "Element",
            "help": "To specify the Service Classification of the Service Requirement.",
        },
    )
    service_status: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "serviceStatus",
            "type": "Element",
            "help": "Status",
        },
    )
    service_number_of_instances: NumericIntegerLength1To15 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "serviceNumberOfInstances",
            "type": "Element",
            "help": "To specify the number of items involved",
        },
    )
    service_marketing_carrier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "serviceMarketingCarrier",
            "type": "Element",
            "help": "To specify to which marketing carrier the service applies",
        },
    )
    service_group: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "serviceGroup",
            "type": "Element",
            "help": "Specify the Service group",
        },
    )
    service_sub_group: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "serviceSubGroup",
            "type": "Element",
            "help": "Specify the Service Sub-Group",
        },
    )
    service_free_text: AlphaNumericStringLength1To70 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "serviceFreeText",
            "type": "Element",
            "help": "Free Text attached to the Service.",
        },
    )


@dataclass
class StationInformationTypeI:
    """To specify departure/arrival information concerning a means of transport."""

    terminal: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "terminal",
            "type": "Element",
            "help": "Departure terminal",
        },
    )


@dataclass
class StructuredDateTimeType:
    """Store date and time in a structured way"""

    year: NumericIntegerLength4To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "year",
            "type": "Element",
            "help": "Year number. The format is a little long for short term usage but it can be reduced by implementation if required.",
        },
    )
    month: NumericIntegerLength1To2 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "month",
            "type": "Element",
            "help": "Month number in the year ( begins to 1 )",
        },
    )
    day: NumericIntegerLength1To2 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "day",
            "type": "Element",
            "help": "Day number in the month ( begins to 1 )",
        },
    )


@dataclass
class TaxDetailsTypeI:

    rate: AlphaNumericStringLength1To18 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "rate",
            "type": "Element",
            "help": "Duty/tax/fee rate",
        },
    )
    country: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "country",
            "type": "Element",
            "help": "Country, coded",
        },
    )
    currency: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "currency",
            "type": "Element",
            "help": "Currency, coded",
        },
    )
    type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "type",
            "type": "Element",
            "help": "Duty/Tax fee type, coded",
        },
    )
    amount_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "amountQualifier",
            "type": "Element",
            "help": "Amount type qualifier, coded",
        },
    )


@dataclass
class TicketNumberDetailsTypeI:
    """To specify a ticket number, type of ticket, and related information."""

    number: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "number",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class TicketingPriceSchemeType:
    """Price Scheme Information"""

    reference_number: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "referenceNumber",
            "type": "Element",
            "help": "PSR (Price Scheme Reference): unique reference of the price scheme as a 8 digit number.",
        },
    )
    name: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "name",
            "type": "Element",
            "help": "Price Scheme Name",
        },
    )
    status: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "status",
            "type": "Element",
            "help": "Price Scheme Status. Is the price scheme valid for service fee calculation ?",
        },
    )
    description: AlphaNumericStringLength1To250 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "description",
            "type": "Element",
            "help": "free flow description of the price scheme",
        },
    )


@dataclass
class TrafficRestrictionDetailsTypeI:
    """Coded or free text details which restrict a means of transport."""

    code: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "code",
            "type": "Element",
            "help": "Traffic Restriction code",
        },
    )


@dataclass
class TravellerDetailsType:

    ref: NumericIntegerLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "ref",
            "type": "Element",
            "help": "Direct reference of passenger assigned by requesting system.",
        },
    )
    infant_indicator: NumericIntegerLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "infantIndicator",
            "type": "Element",
            "help": "Traveller is an infant",
        },
    )


@dataclass
class UniqueIdDescriptionType:

    passenger_fee_ref_qualif: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "passengerFeeRefQualif",
            "type": "Element",
            "help": "Reference qualifier.",
        },
    )


@dataclass
class ActionIdentificationType:
    """To provide details of action required or taken, the flights to which this action refers, and reasons for action taken."""

    action_request_code: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "actionRequestCode",
            "type": "Element",
            "help": "Action request code",
        },
    )
    product_details: ProductIdentificationDetailsTypeI50878C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "productDetails",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class AdditionalProductDetailsTypeI:
    """To convey additional information concerning an airline flight."""

    leg_details: AdditionalProductTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "legDetails",
            "type": "Element",
            "help": "Flight details",
        },
    )
    departure_station_info: StationInformationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "departureStationInfo",
            "type": "Element",
            "help": "Departure station",
        },
    )
    arrival_station_info: StationInformationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "arrivalStationInfo",
            "type": "Element",
            "help": None,
        },
    )
    mileage_time_details: MileageTimeDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "mileageTimeDetails",
            "type": "Element",
            "help": "Ground Time Details when connection",
        },
    )


@dataclass
class ArrivalLocalizationType:
    """To convey information of the requested arrival location"""

    arrival_point_details: ArrivalLocationDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "arrivalPointDetails",
            "type": "Element",
            "help": "Details on the location of the arrival point",
        },
    )
    arrival_multi_city: MultiCityOptionType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "arrivalMultiCity",
            "type": "Element",
            "help": "Arrival multi city option",
        },
    )
    attribute_details: CodedAttributeInformationType139508C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "attributeDetails",
            "type": "Element",
            "help": "Attribute details",
        },
    )


@dataclass
class AttributeType:
    """Used to have tag value without code list for tag"""

    selection_details: AttributeInformationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 10,
            "name": "selectionDetails",
            "type": "Element",
            "help": "Option parameters",
        },
    )


@dataclass
class AttributeType61377S:
    """Used to have tag value without code list for tag"""

    attribute_qualifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "attributeQualifier",
            "type": "Element",
            "help": "Criteria Set Type",
        },
    )
    attribute_details: AttributeInformationType97181C = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 99,
            "name": "attributeDetails",
            "type": "Element",
            "help": "Criteria details",
        },
    )


@dataclass
class BooleanExpressionRuleType:
    """To perform boolean operations"""

    boolean_expression: ArithmeticEvaluationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "booleanExpression",
            "type": "Element",
            "help": "Boolean expression associated to the decision rule.",
        },
    )


@dataclass
class BucketDetailsType:

    code: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "code",
            "type": "Element",
            "help": "Code",
        },
    )
    type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "type",
            "type": "Element",
            "help": "Option or distribution",
        },
    )
    attribute: AttributeDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 10,
            "name": "attribute",
            "type": "Element",
            "help": "Attribute",
        },
    )


@dataclass
class CodedAttributeType:
    """Used to have tag value without code list for tag"""

    attribute_details: CodedAttributeInformationType254574C = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 9,
            "name": "attributeDetails",
            "type": "Element",
            "help": "Attribute details",
        },
    )


@dataclass
class CodedAttributeType197696S:
    """Used to have tag value without code list for tag"""

    fee_id: CodedAttributeInformationType275401C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "feeId",
            "type": "Element",
            "help": "Fee/reduction Id",
        },
    )


@dataclass
class CodedAttributeType78500S:
    """Used to have tag value without code list for tag"""

    attribute_details: CodedAttributeInformationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 20,
            "name": "attributeDetails",
            "type": "Element",
            "help": "Atrribute details.",
        },
    )


@dataclass
class CommercialAgreementsType:
    """To specify commercial agreements between two or more companies related to joint, shared, lease operations etc."""

    codeshare_details: CompanyRoleIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "codeshareDetails",
            "type": "Element",
            "help": "Codeshare Details",
        },
    )
    other_codeshare_details: CompanyRoleIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 8,
            "name": "otherCodeshareDetails",
            "type": "Element",
            "help": "Other codeshare details",
        },
    )


@dataclass
class CommercialAgreementsType78540S:
    """To specify commercial agreements between two or more companies related to joint, shared, lease operations etc."""

    codeshare_details: CompanyRoleIdentificationType120761C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "codeshareDetails",
            "type": "Element",
            "help": "Codeshare Details",
        },
    )
    other_codeshare_details: CompanyRoleIdentificationType120761C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "otherCodeshareDetails",
            "type": "Element",
            "help": "Other codeshare details",
        },
    )


@dataclass
class ConnectionTypeI:
    """To specify connection city and airline designator."""

    connection_details: ConnectionDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 17,
            "name": "connectionDetails",
            "type": "Element",
            "help": "Connection details.",
        },
    )


@dataclass
class ConsumerReferenceInformationType:
    """To specify consumer reference information."""

    customer_references: ConsumerReferenceIdentificationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 20,
            "name": "customerReferences",
            "type": "Element",
            "help": "Customer references",
        },
    )


@dataclass
class ConversionRateType:
    """To specify conversion rate details"""

    conversion_rate_detail: ConversionRateDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 2,
            "name": "conversionRateDetail",
            "type": "Element",
            "help": "Detail of conversion rate of First Monetary Unit",
        },
    )


@dataclass
class CorporateFareInformationType:
    """To specify corporate fare information"""

    corporate_fare_identifiers: CorporateFareIdentifiersType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "corporateFareIdentifiers",
            "type": "Element",
            "help": "Corporate fare identifiers",
        },
    )


@dataclass
class CorporateIdentificationType:
    """To specify corporate number(s) or name(s)"""

    corporate_id: CorporateIdentityType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "corporateId",
            "type": "Element",
            "help": "Corporate identity",
        },
    )


@dataclass
class DateAndTimeInformationType:
    """not the standard only used in fare quote message"""

    stop_details: DateAndTimeDetailsType120762C = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 2,
            "name": "stopDetails",
            "type": "Element",
            "help": "Details on date and time",
        },
    )


@dataclass
class DateAndTimeInformationType181295S:
    """Target estimated or actual dates and times"""

    first_date_time_detail: DateAndTimeDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "firstDateTimeDetail",
            "type": "Element",
            "help": "Details on date and Time",
        },
    )
    range_of_date: DateAndTimeDetailsType254619C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "rangeOfDate",
            "type": "Element",
            "help": "Details of the Requested Range of Dates",
        },
    )
    trip_details: DateAndTimeDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "tripDetails",
            "type": "Element",
            "help": "Details of the trip duration",
        },
    )


@dataclass
class DateAndTimeInformationTypeI:
    """To convey information regarding estimated or actual dates and times of operational events"""

    date_time_details: DateAndTimeDetailsTypeI120740C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "dateTimeDetails",
            "type": "Element",
            "help": "DATE AND TIME DETAILS.",
        },
    )


@dataclass
class DepartureLocationType:
    """To convey information of requested departure"""

    departure_point: ArrivalLocationDetailsType120834C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "departurePoint",
            "type": "Element",
            "help": "Details on localization of the departure point",
        },
    )
    dep_multi_city: MultiCityOptionType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "depMultiCity",
            "type": "Element",
            "help": "Departure multi city option",
        },
    )
    first_pnr_segment_ref: PnrsegmentReferenceType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "firstPnrSegmentRef",
            "type": "Element",
            "help": "To specify a series or a range of PNR segments",
        },
    )
    attribute_details: CodedAttributeInformationType139508C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "attributeDetails",
            "type": "Element",
            "help": "Attribute details",
        },
    )


@dataclass
class FareFamilyCriteriaType:
    """Fare family criteria"""

    carrier_id: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "carrierId",
            "type": "Element",
            "help": "Fare publishing carrier.",
        },
    )
    rdb: AlphaStringLength1To2 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "rdb",
            "type": "Element",
            "help": "Reservation booking designator.",
        },
    )
    fare_family_info: FareQualifierInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "fareFamilyInfo",
            "type": "Element",
            "help": "Fare family info.",
        },
    )
    fare_product_detail: FareProductDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "fareProductDetail",
            "type": "Element",
            "help": "Fare product detail.",
        },
    )
    corporate_info: MultipleIdentificationNumbersTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "corporateInfo",
            "type": "Element",
            "help": "Corporate information.",
        },
    )
    cabin_product: CabinClassDesignationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 6,
            "name": "cabinProduct",
            "type": "Element",
            "help": "Indicates flight cabin details.",
        },
    )
    cabin_processing_identifier: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "cabinProcessingIdentifier",
            "type": "Element",
            "help": "Cabin processing option.",
        },
    )
    date_time_details: ProductDateTimeTypeI194583C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "dateTimeDetails",
            "type": "Element",
            "help": "Product date or time.",
        },
    )
    other_criteria: CodedAttributeInformationType120742C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "otherCriteria",
            "type": "Element",
            "help": "Other criteria.",
        },
    )


@dataclass
class FareFamilyType:
    """NEW FARE SEACH"""

    commercial_family_details: FareFamilyDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "commercialFamilyDetails",
            "type": "Element",
            "help": "Indicates Commercial Fare Family Short names",
        },
    )


@dataclass
class FareFamilyType80157S:
    """NEW FARE SEACH"""

    ref_number: NumericIntegerLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "refNumber",
            "type": "Element",
            "help": "Fare Family Reference Number",
        },
    )
    fare_familyname: AlphaNumericStringLength1To10 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "fareFamilyname",
            "type": "Element",
            "help": "Fare Family Short Name",
        },
    )
    hierarchy: NumericIntegerLength1To4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "hierarchy",
            "type": "Element",
            "help": "HIERARCHICAL ORDER WITHIN FARE FAMILY",
        },
    )
    commercial_family_details: FareFamilyDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "commercialFamilyDetails",
            "type": "Element",
            "help": "Indicates Commercial Fare Family Short names",
        },
    )


@dataclass
class FareInformationType:

    value_qualifier: AmaEdicodesetTypeLength1to3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "valueQualifier",
            "type": "Element",
            "help": "Value Qualifier",
        },
    )
    value: NumericIntegerLength1To15 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "value",
            "type": "Element",
            "help": "Value",
        },
    )
    fare_details: FareDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "fareDetails",
            "type": "Element",
            "help": "Fare Details",
        },
    )
    identity_number: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "identityNumber",
            "type": "Element",
            "help": "Identity Number",
        },
    )
    fare_type_grouping: FareTypeGroupingInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "fareTypeGrouping",
            "type": "Element",
            "help": "Fare Type Grouping",
        },
    )
    rate_category: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "rateCategory",
            "type": "Element",
            "help": "Rate Category",
        },
    )


@dataclass
class FlightProductInformationType:
    """To specify flight product information details"""

    cabin_product: CabinProductDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 26,
            "name": "cabinProduct",
            "type": "Element",
            "help": "Indicates flight cabin details",
        },
    )
    context_details: ProductTypeDetailsType205137C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "contextDetails",
            "type": "Element",
            "help": "To specify additional characteristics.",
        },
    )


@dataclass
class FormOfPaymentTypeI:
    """To convey details describing the form of payment."""

    form_of_payment_details: FormOfPaymentDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "formOfPaymentDetails",
            "type": "Element",
            "help": "FORM OF PAYMENT DETAILS",
        },
    )


@dataclass
class FreeTextInformationType:
    """This segment is used to convey the free text"""

    free_text_details: FreeTextDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "freeTextDetails",
            "type": "Element",
            "help": "Details for the free text message",
        },
    )
    free_text: AlphaNumericStringLength1To70 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "freeText",
            "type": "Element",
            "help": "Free text corresponding to the DEI 127 data.",
        },
    )


@dataclass
class FrequentTravellerIdentificationCodeType:
    """To specify frequent traveler information"""

    frequent_traveller_details: FrequentTravellerIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 99,
            "name": "frequentTravellerDetails",
            "type": "Element",
            "help": "Frequent Traveller Info",
        },
    )


@dataclass
class FrequentTravellerIdentificationCodeType177150S:
    """To specify frequent traveler information."""

    frequent_traveller_details: FrequentTravellerIdentificationType249074C = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 99,
            "name": "frequentTravellerDetails",
            "type": "Element",
            "help": "Frequent traveller details",
        },
    )


@dataclass
class HeaderInformationTypeI:
    """To specify header information applicable to the entire message."""

    status: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "status",
            "type": "Element",
            "help": "Status",
        },
    )
    date_time_period_details: DateTimePeriodDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "dateTimePeriodDetails",
            "type": "Element",
            "help": "Date and Time info",
        },
    )
    reference_number: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "referenceNumber",
            "type": "Element",
            "help": "Reference number",
        },
    )
    product_identification: AlphaNumericStringLength1To35 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "productIdentification",
            "type": "Element",
            "help": "Contains product identification such as UIC code...",
        },
    )


@dataclass
class ItemNumberType:
    """To specify an item number"""

    item_number_id: ItemNumberIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "itemNumberId",
            "type": "Element",
            "help": "Indicates the fare family combination number",
        },
    )


@dataclass
class ItemNumberType80866S:
    """To specify an item number"""

    item_number_details: ItemNumberIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "itemNumberDetails",
            "type": "Element",
            "help": "Item number details",
        },
    )


@dataclass
class ItemReferencesAndVersionsType:
    """Exchange and link unique identifiers"""

    passenger_fee_ref_type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "passengerFeeRefType",
            "type": "Element",
            "help": "Reference Qualifier.",
        },
    )
    passenger_fee_ref_number: NumericIntegerLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "passengerFeeRefNumber",
            "type": "Element",
            "help": "Reference number.",
        },
    )
    other_characteristics: UniqueIdDescriptionType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "otherCharacteristics",
            "type": "Element",
            "help": "Unique id description.",
        },
    )


@dataclass
class MonetaryAndCabinInformationType:

    money_and_cabin_info: MonetaryAndCabinInformationDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "moneyAndCabinInfo",
            "type": "Element",
            "help": "Monetary and cabin information.",
        },
    )


@dataclass
class MonetaryInformationType:
    """To specify monetary information details"""

    money_info: MonetaryInformationDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "moneyInfo",
            "type": "Element",
            "help": "MONEY INFORMATION",
        },
    )
    additional_money_info: MonetaryInformationDetailsTypeI194597C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 19,
            "name": "additionalMoneyInfo",
            "type": "Element",
            "help": "MONEY INFORMATION",
        },
    )


@dataclass
class MonetaryInformationType80162S:
    """To convey monetary amounts, rates and percentages."""

    monetary_details: MonetaryInformationDetailsTypeI65140C = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 20,
            "name": "monetaryDetails",
            "type": "Element",
            "help": "Monetary info",
        },
    )


@dataclass
class MonetaryInformationTypeI:
    """To convey monetary amounts, rates and percentages."""

    monetary_details: MonetaryInformationDetailsTypeI65141C = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 20,
            "name": "monetaryDetails",
            "type": "Element",
            "help": "Monetary info",
        },
    )


@dataclass
class NumberOfUnitsType:
    """To specify the number of Units required"""

    unit_number_detail: NumberOfUnitDetailsType270113C = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 20,
            "name": "unitNumberDetail",
            "type": "Element",
            "help": "NUMBER OF UNIT DETAILS",
        },
    )


@dataclass
class NumberOfUnitsType80154S:
    """To specify the number of Units required"""

    unit_number_detail: NumberOfUnitDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 20,
            "name": "unitNumberDetail",
            "type": "Element",
            "help": "NUMBER OF UNIT DETAILS",
        },
    )


@dataclass
class OriginAndDestinationRequestType:
    """To convey information regarding Requested Segments"""

    seg_ref: NumericIntegerLength1To2 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "segRef",
            "type": "Element",
            "help": "Requested segment number",
        },
    )
    location_forcing: ItineraryDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "locationForcing",
            "type": "Element",
            "help": "Forces arrival or departure, from/to the same airport/city",
        },
    )


@dataclass
class PassengerItineraryInformationType:
    """Contains PNR travel (Reservation Booking code, Booking status). Only present in case with-PNR."""

    booking: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "booking",
            "type": "Element",
            "help": ".",
        },
    )
    identifier: AlphaNumericStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "identifier",
            "type": "Element",
            "help": ".",
        },
    )
    status: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "status",
            "type": "Element",
            "help": ".",
        },
    )
    item_number: NumericIntegerLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "itemNumber",
            "type": "Element",
            "help": ".",
        },
    )
    date_time_details: ProductDateTimeType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "dateTimeDetails",
            "type": "Element",
            "help": ".",
        },
    )
    designator: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "designator",
            "type": "Element",
            "help": ".",
        },
    )
    movement_type: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "movementType",
            "type": "Element",
            "help": ".",
        },
    )
    product_type_details: ProductTypeDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "productTypeDetails",
            "type": "Element",
            "help": ".",
        },
    )


@dataclass
class PricingTicketingDetailsType:
    """To specify pricing/ticketing details"""

    pricing_ticketing: PricingTicketingInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "pricingTicketing",
            "type": "Element",
            "help": "Pricing ticketing Details.",
        },
    )
    ticketing_date: ProductDateTimeTypeI194598C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "ticketingDate",
            "type": "Element",
            "help": "PRODUCT DATE OR TIME",
        },
    )
    company_id: CompanyIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "companyId",
            "type": "Element",
            "help": "COMPANY IDENTIFICATION",
        },
    )
    selling_point: LocationDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "sellingPoint",
            "type": "Element",
            "help": "LOCATION DETAILS",
        },
    )
    ticketing_point: LocationDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "ticketingPoint",
            "type": "Element",
            "help": "LOCATION DETAILS",
        },
    )
    journey_origin_point: LocationDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "journeyOriginPoint",
            "type": "Element",
            "help": "Used to Target Transborder Fares",
        },
    )
    corporate_id: AgentIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "corporateId",
            "type": "Element",
            "help": "Contains the ARC,IATA and ERSP numbers",
        },
    )


@dataclass
class ProposedSegmentType:
    """To specify the parameters used for product quality"""

    flight_proposal: ProposedSegmentDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 9,
            "name": "flightProposal",
            "type": "Element",
            "help": "Parameters for proposed flight group",
        },
    )
    flight_characteristic: AlphaNumericStringLength0To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightCharacteristic",
            "type": "Element",
            "help": "Flight characteristics.",
        },
    )
    maj_cabin: AlphaStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "majCabin",
            "type": "Element",
            "help": "Majority cabin",
        },
    )


@dataclass
class ReferenceInfoType:
    """To provide specific reference identification for a traveller."""

    referencing_detail: ReferencingDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "referencingDetail",
            "type": "Element",
            "help": "Referencing details",
        },
    )


@dataclass
class RoutingInformationTypeI:
    """To provide routing information."""

    routing_details: ProductLocationDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "routingDetails",
            "type": "Element",
            "help": "Stops details",
        },
    )


@dataclass
class SegmentRepetitionControlTypeI:
    """To indicate the number of segment group repetitions."""

    segment_control_details: SegmentRepetitionControlDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "segmentControlDetails",
            "type": "Element",
            "help": "Segment control details",
        },
    )


@dataclass
class SelectionDetailsType:
    """To specify the details for making a selection."""

    carrier_fee_details: SelectionDetailsInformationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "carrierFeeDetails",
            "type": "Element",
            "help": "Carrier fees options",
        },
    )
    other_selection_details: SelectionDetailsInformationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 98,
            "name": "otherSelectionDetails",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class SpecialRequirementsDetailsType:
    """To specify special requests or service s information relating to a traveller"""

    service_requirements_info: SpecialRequirementsTypeDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "serviceRequirementsInfo",
            "type": "Element",
            "help": "To specify the Service Requirement of the customer",
        },
    )
    seat_details: SpecialRequirementsDataDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "seatDetails",
            "type": "Element",
            "help": "Seat details",
        },
    )


@dataclass
class SpecificDataInformationType:
    """To specify miscellaneous data by first identifying the type of data to be sent and then the actual data."""

    data_type_information: DataTypeInformationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "dataTypeInformation",
            "type": "Element",
            "help": "Carrier fee description",
        },
    )
    data_information: DataInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "dataInformation",
            "type": "Element",
            "help": "Data information",
        },
    )


@dataclass
class StructuredPeriodInformationType:
    """This segment is designed to convey period in a structured way."""

    begin_date_time: StructuredDateTimeType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "beginDateTime",
            "type": "Element",
            "help": "Effective date of period of operation",
        },
    )
    end_date_time: StructuredDateTimeType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "endDateTime",
            "type": "Element",
            "help": "Discontinue date of period of operation",
        },
    )
    frequency: FrequencyType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "frequency",
            "type": "Element",
            "help": "It is used with a period to give a restriction for days impacted. It permits for example to indicate on which days, a flight operates.",
        },
    )


@dataclass
class TaxType:
    """To specify details realting to tax(es)"""

    withhold_tax_surcharge: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "withholdTaxSurcharge",
            "type": "Element",
            "help": "Duty tax fee category, coded",
        },
    )
    tax_detail: TaxDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "taxDetail",
            "type": "Element",
            "help": "TAX DETAILS",
        },
    )


@dataclass
class TicketNumberTypeI:
    """To convey information related to a specific ticket."""

    document_details: TicketNumberDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 99,
            "name": "documentDetails",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class TrafficRestrictionTypeI:
    """To convey certain restrictions that apply to a means of transport on all or part of a journey"""

    traffic_restriction_details: TrafficRestrictionDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "trafficRestrictionDetails",
            "type": "Element",
            "help": "Traffic Restriction Details",
        },
    )


@dataclass
class TravelFlightInformationType:
    """Information about flight options"""

    cabin_id: CabinIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "cabinId",
            "type": "Element",
            "help": "Cabin identification",
        },
    )
    company_identity: CompanyIdentificationType120719C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "companyIdentity",
            "type": "Element",
            "help": "Company Identification",
        },
    )
    flight_detail: ProductTypeDetailsType120801C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightDetail",
            "type": "Element",
            "help": "Type of flight details",
        },
    )
    inclusion_detail: ConnectPointDetailsType195492C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "inclusionDetail",
            "type": "Element",
            "help": "Details of included connecting points",
        },
    )
    exclusion_detail: ConnectPointDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "exclusionDetail",
            "type": "Element",
            "help": "Further connection details",
        },
    )
    unit_number_detail: NumberOfUnitDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "unitNumberDetail",
            "type": "Element",
            "help": "Nb of connections for each requested segment of the journey.",
        },
    )


@dataclass
class TravelFlightInformationType165053S:
    """Information about flight options"""

    cabin_id: CabinIdentificationType233500C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "cabinId",
            "type": "Element",
            "help": "Cabin identification",
        },
    )
    company_identity: CompanyIdentificationType120719C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "companyIdentity",
            "type": "Element",
            "help": "Company Identification",
        },
    )
    flight_detail: ProductTypeDetailsType120801C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightDetail",
            "type": "Element",
            "help": "Type of flight details",
        },
    )
    inclusion_detail: ConnectPointDetailsType195492C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "inclusionDetail",
            "type": "Element",
            "help": "Details of included connect point",
        },
    )
    exclusion_detail: ConnectPointDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "exclusionDetail",
            "type": "Element",
            "help": "Further connection details",
        },
    )
    unit_number_detail: NumberOfUnitDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "unitNumberDetail",
            "type": "Element",
            "help": "Nb of connections allowed at requested segment level.",
        },
    )


@dataclass
class TravelFlightInformationType197722S:
    """Information about flight options"""

    cabin_id: CabinIdentificationType233500C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "cabinId",
            "type": "Element",
            "help": "Cabin identification",
        },
    )
    company_identity: CompanyIdentificationType275415C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "companyIdentity",
            "type": "Element",
            "help": "Company Identification",
        },
    )
    flight_detail: ProductTypeDetailsType120801C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightDetail",
            "type": "Element",
            "help": "Type of flight details",
        },
    )
    inclusion_detail: ConnectPointDetailsType195492C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "inclusionDetail",
            "type": "Element",
            "help": "Details of included connect point",
        },
    )
    exclusion_detail: ConnectPointDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "exclusionDetail",
            "type": "Element",
            "help": "Further connection details",
        },
    )
    unit_number_detail: NumberOfUnitDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "unitNumberDetail",
            "type": "Element",
            "help": "Added departed flights flag",
        },
    )


@dataclass
class TravelProductInformationTypeI:
    """To specify details related to a product."""

    flight_date: ProductDateTimeTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightDate",
            "type": "Element",
            "help": "Flight Date",
        },
    )
    board_point_details: LocationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "boardPointDetails",
            "type": "Element",
            "help": "Board point",
        },
    )
    offpoint_details: LocationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "offpointDetails",
            "type": "Element",
            "help": "Off point",
        },
    )
    company_details: CompanyIdentificationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "companyDetails",
            "type": "Element",
            "help": None,
        },
    )
    flight_identification: ProductIdentificationDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightIdentification",
            "type": "Element",
            "help": "Flight identification",
        },
    )
    flight_type_details: ProductTypeDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightTypeDetails",
            "type": "Element",
            "help": "Identify flight part of the journey",
        },
    )


@dataclass
class TravelProductType:
    """Contains flight travel (date, time, flight number,...) and posting avaibility information"""

    product_date_time: ProductDateTimeType195546C = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "productDateTime",
            "type": "Element",
            "help": "Date and time of departure and arrival",
        },
    )
    location: LocationIdentificationDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 2,
            "name": "location",
            "type": "Element",
            "help": "Location of departure and arrival",
        },
    )
    company_id: CompanyIdentificationType195544C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "companyId",
            "type": "Element",
            "help": "Company identification",
        },
    )
    flight_ortrain_number: AlphaNumericStringLength1To8 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightOrtrainNumber",
            "type": "Element",
            "help": "Flight number or trainNumber",
        },
    )
    product_detail: AdditionalProductDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "productDetail",
            "type": "Element",
            "help": "Product details",
        },
    )
    add_product_detail: ProductFacilitiesType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "addProductDetail",
            "type": "Element",
            "help": "Additional product details",
        },
    )
    attribute_details: CodedAttributeInformationType247828C = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "attributeDetails",
            "type": "Element",
            "help": "Attribute details",
        },
    )


@dataclass
class TravellerReferenceInformationType:
    """To specify traveller/personal details"""

    ptc: AlphaNumericStringLength1To6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "ptc",
            "type": "Element",
            "help": "Requested passenger type",
        },
    )
    traveller: TravellerDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 9,
            "name": "traveller",
            "type": "Element",
            "help": "Traveller details",
        },
    )


@dataclass
class UserIdentificationType:
    """User Identification"""

    office_identification: OriginatorIdentificationDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "officeIdentification",
            "type": "Element",
            "help": "Originator Identification Details",
        },
    )
    office_type: AlphaNumericStringLength1To1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "officeType",
            "type": "Element",
            "help": "Used to specify which kind of info is given in DE 9900.",
        },
    )
    office_code: AlphaNumericStringLength1To30 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "officeCode",
            "type": "Element",
            "help": "The code given to an agent by the originating reservation system.",
        },
    )


@dataclass
class ValueSearchCriteriaType:
    """To specify Criteria with list of parameters"""

    criteria_name: AlphaNumericStringLength1To50 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "criteriaName",
            "type": "Element",
            "help": None,
        },
    )
    criteria_code: AlphaNumericStringLength1To3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "criteriaCode",
            "type": "Element",
            "help": None,
        },
    )
    value: AlphaNumericStringLength1To18 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "value",
            "type": "Element",
            "help": None,
        },
    )
    criteria_details: CriteriaiDetaislType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 10,
            "name": "criteriaDetails",
            "type": "Element",
            "help": None,
        },
    )


@dataclass
class AirlineDistributionDetailsType16:
    """Inner ComplexType name auto generated"""

    requested_segment_ref: OriginAndDestinationRequestType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "requestedSegmentRef",
            "type": "Element",
            "help": "Indicates reference of the requested segment",
        },
    )
    flight_info: TravelFlightInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightInfo",
            "type": "Element",
            "help": "Specify Flight options.",
        },
    )


@dataclass
class BucketsType4:
    """Inner ComplexType name auto generated"""

    bucket_info: BucketInformationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "bucketInfo",
            "type": "Element",
            "help": "Bucket information: name, priority, weight",
        },
    )
    bucket_details: BucketDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 15,
            "name": "bucketDetails",
            "type": "Element",
            "help": "Bucket details",
        },
    )


@dataclass
class CombinationFareFamiliesType7:
    """Inner ComplexType name auto generated"""

    item_ffcnumber: ItemNumberType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "itemFFCNumber",
            "type": "Element",
            "help": "Specification of the item number",
        },
    )
    nb_of_units: NumberOfUnitsType80154S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "nbOfUnits",
            "type": "Element",
            "help": "Number of units.",
        },
    )
    reference_info: ReferenceInfoType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 6,
            "name": "referenceInfo",
            "type": "Element",
            "help": "Requested segment reference",
        },
    )


@dataclass
class FareFamilySegmentType10:
    """Inner ComplexType name auto generated"""

    reference_info: ReferenceInfoType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "referenceInfo",
            "type": "Element",
            "help": "Requested segment reference",
        },
    )
    family_criteria: FareFamilyCriteriaType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "familyCriteria",
            "type": "Element",
            "help": "Description of fare family criteria.",
        },
    )


@dataclass
class FareFamilySegmentType17:
    """Inner ComplexType name auto generated"""

    reference_info: ReferenceInfoType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "referenceInfo",
            "type": "Element",
            "help": "Requested segment reference",
        },
    )
    family_criteria: FareFamilyCriteriaType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "familyCriteria",
            "type": "Element",
            "help": "Description of fare family criteria.",
        },
    )


@dataclass
class FareOptionsType3:
    """Inner ComplexType name auto generated"""

    pricing_tick_info: PricingTicketingDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "pricingTickInfo",
            "type": "Element",
            "help": "Pricing and ticketing details.",
        },
    )
    corporate: CorporateIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "corporate",
            "type": "Element",
            "help": "Corporate name/number used to target fares",
        },
    )
    ticketing_price_scheme: TicketingPriceSchemeType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "ticketingPriceScheme",
            "type": "Element",
            "help": "Ticketing price scheme.",
        },
    )
    fee_id_description: CodedAttributeType197696S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "feeIdDescription",
            "type": "Element",
            "help": "PSR number",
        },
    )
    conversion_rate: ConversionRateType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "conversionRate",
            "type": "Element",
            "help": "Used to force the currency of pricing",
        },
    )
    form_of_payment: FormOfPaymentTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "formOfPayment",
            "type": "Element",
            "help": "Form of payment information.",
        },
    )
    frequent_traveller_info: FrequentTravellerIdentificationCodeType177150S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "frequentTravellerInfo",
            "type": "Element",
            "help": "Frequent traveller information",
        },
    )
    monetary_cabin_info: MonetaryAndCabinInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "monetaryCabinInfo",
            "type": "Element",
            "help": "Monetary and cabin information.",
        },
    )


@dataclass
class FeeDescriptionGrpType20:
    """Inner ComplexType name auto generated"""

    item_number_info: ItemNumberType80866S = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "itemNumberInfo",
            "type": "Element",
            "help": "Specification of the item number",
        },
    )
    service_attributes_info: AttributeType61377S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "serviceAttributesInfo",
            "type": "Element",
            "help": "Attributes (SSR code EMD, RFIC, SSIM)",
        },
    )
    service_description_info: SpecialRequirementsDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "serviceDescriptionInfo",
            "type": "Element",
            "help": "Other service information (service description, ...)",
        },
    )


@dataclass
class FlightDetailsType18:
    """Inner ComplexType name auto generated"""

    flight_information: TravelProductType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "flightInformation",
            "type": "Element",
            "help": "Specification of details on the flight and posting availability",
        },
    )
    avl_info: FlightProductInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 6,
            "name": "avlInfo",
            "type": "Element",
            "help": "returns booking class and availability context",
        },
    )
    technical_stop: DateAndTimeInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "technicalStop",
            "type": "Element",
            "help": "Details on Flight date, time and location of technical stop or change of gauge",
        },
    )
    commercial_agreement: CommercialAgreementsType78540S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "commercialAgreement",
            "type": "Element",
            "help": "Code Share Agreement description for current flight.",
        },
    )
    add_info: HeaderInformationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "addInfo",
            "type": "Element",
            "help": "Additional Info about flight, such as Reference number, and several options",
        },
    )
    terminal_equipment_details: AdditionalProductDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "terminalEquipmentDetails",
            "type": "Element",
            "help": "Terminal, Equipment and EFT Details. If a Total EFT of the Travel Solution is requested then we will have 2 occurrences of the terminalEquipmentDetails attached to the first leg flightInformation: the 1st occurence will give the EFT of the leg, the 2nd occurrence will give the total EFT of the Travel Solution.",
        },
    )
    reservation_info: PassengerItineraryInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "reservationInfo",
            "type": "Element",
            "help": "PNR flight reservation info",
        },
    )
    price_to_beat: MonetaryInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "priceToBeat",
            "type": "Element",
            "help": "Indicates Price to beat",
        },
    )


@dataclass
class FoprepresentationType:

    form_of_payment_details: FormOfPaymentTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "formOfPaymentDetails",
            "type": "Element",
            "help": "Form of payment information.",
        },
    )
    passenger_fee_reference: ItemReferencesAndVersionsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "passengerFeeReference",
            "type": "Element",
            "help": "Fee/Reduction Passenger reference.",
        },
    )


@dataclass
class IncidentalStopInfoType19:
    """Inner ComplexType name auto generated"""

    date_time_info: DateAndTimeInformationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "dateTimeInfo",
            "type": "Element",
            "help": "Incidental stop date/time information",
        },
    )


@dataclass
class PsgDetailsInfoType1:
    """Inner ComplexType name auto generated"""

    discount_ptc: FareInformationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "discountPtc",
            "type": "Element",
            "help": "PTC/Discount Code age",
        },
    )
    flequent_flyer_details: FrequentTravellerIdentificationCodeType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flequentFlyerDetails",
            "type": "Element",
            "help": "Tier level information",
        },
    )


@dataclass
class TicketRequestedSegmentsType14:
    """Inner ComplexType name auto generated"""

    action_identification: ActionIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "actionIdentification",
            "type": "Element",
            "help": "Action identification.",
        },
    )
    connect_point_details: ConnectionTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "connectPointDetails",
            "type": "Element",
            "help": "Connected cities in changed ticket requested segment.",
        },
    )


@dataclass
class FeeDetailsType15:
    """Inner ComplexType name auto generated"""

    fee_info: SpecificDataInformationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "feeInfo",
            "type": "Element",
            "help": "Fee information",
        },
    )
    associated_amounts: MonetaryInformationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "associatedAmounts",
            "type": "Element",
            "help": "Associated amounts : amounts to take into account to calculate fee.",
        },
    )
    fee_description_grp: FeeDescriptionGrpType20 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "feeDescriptionGrp",
            "type": "Element",
            "help": "Fee description",
        },
    )


@dataclass
class FlightInfoPnrType13:
    """Inner ComplexType name auto generated"""

    travel_response_details: TravelProductInformationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "travelResponseDetails",
            "type": "Element",
            "help": "Travel Response Details: - Board/Off aiports - Flight number - Part of the journey - Day difference between Board and off - Departure/Arrival dates - Departure/Arrival times",
        },
    )
    time_table_date: StructuredPeriodInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "timeTableDate",
            "type": "Element",
            "help": "Time Table Effective/Discontinue dates and frequency of operating Travel Solution",
        },
    )
    terminal_equipment_details: AdditionalProductDetailsTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "terminalEquipmentDetails",
            "type": "Element",
            "help": "Terminal, Equipment and EFT Details. If a Total EFT of the Travel Solution is requested then we will have 2 occurrences of the terminalEquipmentDetails attached to the first leg travelResponseDetails: the 1st occurrence will give the EFT of the leg, the 2nd occurrence will give the total EFT of the Travel Solution.",
        },
    )
    codeshare_data: CommercialAgreementsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "codeshareData",
            "type": "Element",
            "help": "Codeshare data",
        },
    )
    disclosure: FreeTextInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "disclosure",
            "type": "Element",
            "help": "Disclosure message from an operating carrier.",
        },
    )
    stop_details: RoutingInformationTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "stopDetails",
            "type": "Element",
            "help": "Stops Details",
        },
    )
    traffic_restriction_data: TrafficRestrictionTypeI = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "trafficRestrictionData",
            "type": "Element",
            "help": "Traffic restriction information",
        },
    )
    reservation_info: PassengerItineraryInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "reservationInfo",
            "type": "Element",
            "help": "PNR flight reservation info",
        },
    )
    incidental_stop_info: IncidentalStopInfoType19 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 8,
            "name": "incidentalStopInfo",
            "type": "Element",
            "help": "Incidental stop information.",
        },
    )


@dataclass
class GroupOfFlightsType12:
    """Inner ComplexType name auto generated"""

    prop_flight_gr_detail: ProposedSegmentType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "propFlightGrDetail",
            "type": "Element",
            "help": "To indicate parameters for proposed flight group.",
        },
    )
    price_to_beat: MonetaryInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "priceToBeat",
            "type": "Element",
            "help": "Indicates Price to beat",
        },
    )
    flight_details: FlightDetailsType18 = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 4,
            "name": "flightDetails",
            "type": "Element",
            "help": "list of flight per proposed segment",
        },
    )


@dataclass
class GroupPassengerDetailsType:
    """Contain passenger information"""

    passenger_reference: SegmentRepetitionControlTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "passengerReference",
            "type": "Element",
            "help": "Trigger",
        },
    )
    psg_details_info: PsgDetailsInfoType1 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "psgDetailsInfo",
            "type": "Element",
            "help": "pricing option at passenger level",
        },
    )


@dataclass
class OfficeIdDetailsType9:
    """Inner ComplexType name auto generated"""

    office_id_information: UserIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "officeIdInformation",
            "type": "Element",
            "help": "Office Id Information",
        },
    )
    nb_of_units: NumberOfUnitsType80154S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "nbOfUnits",
            "type": "Element",
            "help": "Number of units.",
        },
    )
    uid_option: CodedAttributeType78500S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "uidOption",
            "type": "Element",
            "help": "UID option",
        },
    )
    pricing_tick_info: PricingTicketingDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "pricingTickInfo",
            "type": "Element",
            "help": "Pricing and ticketing details.",
        },
    )
    corporate_fare_info: CorporateFareInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "corporateFareInfo",
            "type": "Element",
            "help": "Corporate fare information",
        },
    )
    travel_flight_info: TravelFlightInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "travelFlightInfo",
            "type": "Element",
            "help": "Details of a Flight : Direct, Non stop...",
        },
    )
    airline_distribution_details: AirlineDistributionDetailsType16 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 6,
            "name": "airlineDistributionDetails",
            "type": "Element",
            "help": "Details of airline distribution at requested segment level",
        },
    )


@dataclass
class OtherPossibleCriteriaType11:
    """Inner ComplexType name auto generated"""

    logical_link: BooleanExpressionRuleType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "logicalLink",
            "type": "Element",
            "help": "Logical link with other criteria.",
        },
    )
    family_criteria: FareFamilyCriteriaType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "familyCriteria",
            "type": "Element",
            "help": "Description of fare family criteria.",
        },
    )
    fare_family_segment: FareFamilySegmentType17 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 6,
            "name": "fareFamilySegment",
            "type": "Element",
            "help": "Fare family requested segment details.",
        },
    )


@dataclass
class TicketChangeInfoType6:
    """Inner ComplexType name auto generated"""

    ticket_number_details: TicketNumberTypeI = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "ticketNumberDetails",
            "type": "Element",
            "help": "Ticket nb details.",
        },
    )
    ticket_requested_segments: TicketRequestedSegmentsType14 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 6,
            "name": "ticketRequestedSegments",
            "type": "Element",
            "help": "Changed ticket requested segments.",
        },
    )


@dataclass
class FareFamiliesType2:
    """Inner ComplexType name auto generated"""

    family_information: FareFamilyType80157S = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "familyInformation",
            "type": "Element",
            "help": "Segment used to target Commercial Fare Family.",
        },
    )
    family_criteria: FareFamilyCriteriaType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "familyCriteria",
            "type": "Element",
            "help": "Description of Fare Family Criteria.",
        },
    )
    fare_family_segment: FareFamilySegmentType10 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 6,
            "name": "fareFamilySegment",
            "type": "Element",
            "help": "Fare family requested segment details.",
        },
    )
    other_possible_criteria: OtherPossibleCriteriaType11 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "otherPossibleCriteria",
            "type": "Element",
            "help": "Description of other possible fare family criteria.",
        },
    )


@dataclass
class FeeOptionType8:
    """Inner ComplexType name auto generated"""

    fee_type_info: SelectionDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "feeTypeInfo",
            "type": "Element",
            "help": "Nature of the fee (OB,OC,..)",
        },
    )
    rate_tax: MonetaryInformationType80162S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "rateTax",
            "type": "Element",
            "help": "Associated rate tax.",
        },
    )
    fee_details: FeeDetailsType15 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "feeDetails",
            "type": "Element",
            "help": "Details for each fee.",
        },
    )


@dataclass
class ItineraryType5:
    """Inner ComplexType name auto generated"""

    requested_segment_ref: OriginAndDestinationRequestType = field(
        default=None,
        metadata={
            "min_occurs": 1,
            "max_occurs": 1,
            "name": "requestedSegmentRef",
            "type": "Element",
            "help": "Indicates reference of the requested segment",
        },
    )
    departure_localization: DepartureLocationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "departureLocalization",
            "type": "Element",
            "help": "Specification of the requested departure point",
        },
    )
    arrival_localization: ArrivalLocalizationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "arrivalLocalization",
            "type": "Element",
            "help": "Specification of the requested arrival point",
        },
    )
    time_details: DateAndTimeInformationType181295S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "timeDetails",
            "type": "Element",
            "help": "Details on requested date and time plus range of date trip duration",
        },
    )
    flight_info: TravelFlightInformationType165053S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "flightInfo",
            "type": "Element",
            "help": "Specify Flight options.",
        },
    )
    family_information: FareFamilyType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "familyInformation",
            "type": "Element",
            "help": "Segment used to target Commercial Fare Family at requested segment level",
        },
    )
    value_search: ValueSearchCriteriaType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "valueSearch",
            "type": "Element",
            "help": None,
        },
    )
    group_of_flights: GroupOfFlightsType12 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 6,
            "name": "groupOfFlights",
            "type": "Element",
            "help": "list of proposed segments per requested segment",
        },
    )
    flight_info_pnr: FlightInfoPnrType13 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 4,
            "name": "flightInfoPNR",
            "type": "Element",
            "help": "Info concerning the flights booked in the PNR",
        },
    )
    requested_segment_action: ActionIdentificationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "requestedSegmentAction",
            "type": "Element",
            "help": "Action identification for the requested segment",
        },
    )
    attributes: CodedAttributeType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "attributes",
            "type": "Element",
            "help": "Coded attributes",
        },
    )


@dataclass
class FareMasterPricerTravelBoardSearch:
    """Master Pricer Travel Board Search Flex pricer Flex pricer."""

    number_of_unit: NumberOfUnitsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "numberOfUnit",
            "type": "Element",
            "help": "Number of seats , recommendations.",
        },
    )
    global_options: AttributeType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "globalOptions",
            "type": "Element",
            "help": "Global options",
        },
    )
    pax_reference: TravellerReferenceInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 6,
            "name": "paxReference",
            "type": "Element",
            "help": "Traveler Details",
        },
    )
    customer_ref: ConsumerReferenceInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "customerRef",
            "type": "Element",
            "help": "Customer references",
        },
    )
    form_of_payment_by_passenger: FoprepresentationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 60,
            "name": "formOfPaymentByPassenger",
            "type": "Element",
            "help": "Fee with different payment forms by passenger.",
        },
    )
    solution_family: FareInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "solutionFamily",
            "type": "Element",
            "help": "Solution Family",
        },
    )
    passenger_info_grp: GroupPassengerDetailsType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "passengerInfoGrp",
            "type": "Element",
            "help": "Passenger info group (9 ADT + 9 IN)",
        },
    )
    fare_families: FareFamiliesType2 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "fareFamilies",
            "type": "Element",
            "help": "Fare families.",
        },
    )
    fare_options: FareOptionsType3 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "fareOptions",
            "type": "Element",
            "help": "Fare options",
        },
    )
    price_to_beat: MonetaryInformationType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "priceToBeat",
            "type": "Element",
            "help": "Indicates Price to beat",
        },
    )
    tax_info: TaxType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "taxInfo",
            "type": "Element",
            "help": "Tax Details",
        },
    )
    travel_flight_info: TravelFlightInformationType197722S = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "travelFlightInfo",
            "type": "Element",
            "help": "Details of a Flight : Direct, Non stop...",
        },
    )
    value_search: ValueSearchCriteriaType = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "valueSearch",
            "type": "Element",
            "help": None,
        },
    )
    buckets: BucketsType4 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 10,
            "name": "buckets",
            "type": "Element",
            "help": "Buckets",
        },
    )
    itinerary: ItineraryType5 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 18,
            "name": "itinerary",
            "type": "Element",
            "help": "Itinerary",
        },
    )
    ticket_change_info: TicketChangeInfoType6 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 1,
            "name": "ticketChangeInfo",
            "type": "Element",
            "help": "Changed ticket information.",
        },
    )
    combination_fare_families: CombinationFareFamiliesType7 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2000,
            "name": "combinationFareFamilies",
            "type": "Element",
            "help": "Specify fare family combinations",
        },
    )
    fee_option: FeeOptionType8 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "feeOption",
            "type": "Element",
            "help": "Fee option group.",
        },
    )
    office_id_details: OfficeIdDetailsType9 = field(
        default=None,
        metadata={
            "min_occurs": 0,
            "max_occurs": 20,
            "name": "officeIdDetails",
            "type": "Element",
            "help": "List of Office Id Details",
        },
    )
