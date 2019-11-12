from dataclasses import dataclass, field
from typing import List




@dataclass
class CompanyIdentificationType:
    pass


@dataclass
class ActionIdentificationType:
    """
    To provide details of action required or taken, the flights to which this action refers, and reasons for action taken.
    """

    action_request_code: str = field(
        default=None,
        metadata=dict(
            name="actionRequestCode",
            type="Element",
            help="Action request code",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    product_details: str = field(
        default=None,
        metadata=dict(
            name="productDetails",
            type="Element",
            help=None,
        )
    )


@dataclass
class AdditionalProductDetailsType:
    equipment_type: str = field(
        default=None,
        metadata=dict(
            name="equipmentType",
            type="Element",
            help="Type of aircraft",
            min_length=1.0,
            max_length=3.0
        )
    )
    operating_day: str = field(
        default=None,
        metadata=dict(
            name="operatingDay",
            type="Element",
            help="Day number of the week",
            min_length=1.0,
            max_length=7.0
        )
    )
    tech_stop_number: str = field(
        default=None,
        metadata=dict(
            name="techStopNumber",
            type="Element",
            help="Number of stops made in a journey if different from 0",
            pattern="-?[0-9]{1,2}"
        )
    )
    location_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="locationId",
            type="Element",
            help="Location places of the stops",
            min_occurs=0,
            max_occurs=3,
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class AdditionalProductDetailsTypeI:
    """
    To convey additional information concerning an airline flight.
    """

    leg_details: str = field(
        default=None,
        metadata=dict(
            name="legDetails",
            type="Element",
            help="Flight details",
        )
    )
    departure_station_info: str = field(
        default=None,
        metadata=dict(
            name="departureStationInfo",
            type="Element",
            help="Departure station",
        )
    )
    arrival_station_info: str = field(
        default=None,
        metadata=dict(
            name="arrivalStationInfo",
            type="Element",
            help=None,
        )
    )
    mileage_time_details: str = field(
        default=None,
        metadata=dict(
            name="mileageTimeDetails",
            type="Element",
            help="Ground Time Details when connection",
        )
    )


@dataclass
class AdditionalProductTypeI:
    """
    Additional details describing a specific means of transport.
    """

    equipment: str = field(
        default=None,
        metadata=dict(
            name="equipment",
            type="Element",
            help="Equipment type",
            min_length=1.0,
            max_length=3.0
        )
    )
    duration: str = field(
        default=None,
        metadata=dict(
            name="duration",
            type="Element",
            help="Elaps flying time of the leg",
            pattern="-?[0-9]{1,6}"
        )
    )
    complexing_flight_indicator: str = field(
        default=None,
        metadata=dict(
            name="complexingFlightIndicator",
            type="Element",
            help="COG indicator",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class AgentIdentificationType:
    arc_number: str = field(
        default=None,
        metadata=dict(
            name="arcNumber",
            type="Element",
            help="Contains ARC number",
            min_length=1.0,
            max_length=12.0
        )
    )
    ersp_number: str = field(
        default=None,
        metadata=dict(
            name="erspNumber",
            type="Element",
            help="ERSP number of the Office or Customer",
            min_length=1.0,
            max_length=12.0
        )
    )
    iata_number: str = field(
        default=None,
        metadata=dict(
            name="iataNumber",
            type="Element",
            help="IATA Number",
            min_length=1.0,
            max_length=12.0
        )
    )


@dataclass
class ArithmeticEvaluationType:
    code_operator: str = field(
        default=None,
        metadata=dict(
            name="codeOperator",
            type="Element",
            help="Boolean operator",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ArrivalLocalizationType:
    """
    To convey information of the requested arrival location
    """

    arrival_point_details: str = field(
        default=None,
        metadata=dict(
            name="arrivalPointDetails",
            type="Element",
            help="Details on the location of the arrival point",
        )
    )
    arrival_multi_city: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="arrivalMultiCity",
            type="Element",
            help="Arrival multi city option",
            min_occurs=0,
            max_occurs=20
        )
    )
    attribute_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            help="Attribute details",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class ArrivalLocationDetailsType:
    distance: str = field(
        default=None,
        metadata=dict(
            name="distance",
            type="Element",
            help="For Radius: This is the length of the requested radius around the location of destination.",
            pattern="-?[0-9]{1,3}"
        )
    )
    distance_unit: str = field(
        default=None,
        metadata=dict(
            name="distanceUnit",
            type="Element",
            help="Distance unit qualifier for radius",
            min_length=0.0,
            max_length=3.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            help="ATA/IATA airport/city code of arrival In case of SP request from a PNR, this field is empty.",
            min_length=3.0,
            max_length=5.0
        )
    )
    airport_city_qualifier: str = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            help="Request from no PNR A = consider the locationID specified as an airport (used only when ambiguous) C = consider the locationId as a city (used only when ambiguous) A and C are not used in case of a request from PNR Request from a PNR with Radius option: O = radius applies to the origin of the PNR segments D = radius applies to the destination of the PNR segments",
            min_length=1.0,
            max_length=1.0
        )
    )
    latitude: str = field(
        default=None,
        metadata=dict(
            name="latitude",
            type="Element",
            help="Latitude in degrees (decimal format) with hemisphere N=north S=south",
            min_length=6.0,
            max_length=6.0
        )
    )
    longitude: str = field(
        default=None,
        metadata=dict(
            name="longitude",
            type="Element",
            help="Longitude in degrees (decimal format) with hemisphere E=east, W=west",
            min_length=6.0,
            max_length=6.0
        )
    )


@dataclass
class ArrivalLocationDetailsType120834C:
    distance: str = field(
        default=None,
        metadata=dict(
            name="distance",
            type="Element",
            help="For Radius: This is the length of the requested radius around the location of origin.",
            pattern="-?[0-9]{1,3}"
        )
    )
    distance_unit: str = field(
        default=None,
        metadata=dict(
            name="distanceUnit",
            type="Element",
            help="Distance unit qualifier for radius",
            min_length=1.0,
            max_length=3.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            help="ATA/IATA airport/city code of arrival In case of SP request from a PNR, this field is empty.",
            min_length=3.0,
            max_length=5.0
        )
    )
    airport_city_qualifier: str = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            help="Request from no PNR A = consider the locationID specified as an airport (used only when ambiguous) C = consider the locationId as a city (used only when ambiguous) A and C are not used in case of a request from PNR Request from a PNR with Radius option: O = radius applies to the origin of the PNR segments D = radius applies to the destination of the PNR segments",
            min_length=1.0,
            max_length=1.0
        )
    )
    latitude: str = field(
        default=None,
        metadata=dict(
            name="latitude",
            type="Element",
            help="Latitude in degrees (decimal format) with hemisphere N=north S=south",
            min_length=6.0,
            max_length=6.0
        )
    )
    longitude: str = field(
        default=None,
        metadata=dict(
            name="longitude",
            type="Element",
            help="Longitude in degrees (decimal format) with hemisphere E=east, W=west",
            min_length=6.0,
            max_length=6.0
        )
    )


@dataclass
class AttributeDetailsType:
    requested_sgt: str = field(
        default=None,
        metadata=dict(
            name="requestedSgt",
            type="Element",
            help="Reference of the requested segment",
            min_length=1.0,
            max_length=3.0
        )
    )
    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="value",
            type="Element",
            help="List of airlines, cabins, time window, number of connections.",
            min_occurs=0,
            max_occurs=50,
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class AttributeInformationType:
    """
    To identify the type of attribute and the attribute
    """

    option: str = field(
        default=None,
        metadata=dict(
            name="option",
            type="Element",
            help="Code of options",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    option_information: str = field(
        default=None,
        metadata=dict(
            name="optionInformation",
            type="Element",
            help="Mandatory when alternate date option is used (ALT), must be set to plus (P) or minus (M) a number of days around the original PNR segment dates. E.g.: M1 (for minus 1 day) or P100 (for plus 100 days)",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class AttributeInformationType97181C:
    """
    To identify the type of attribute and the attribute
    """

    attribute_type: str = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
            help="Attribute type",
            required=True,
            min_length=1.0,
            max_length=25.0
        )
    )
    attribute_description: str = field(
        default=None,
        metadata=dict(
            name="attributeDescription",
            type="Element",
            help="Attribute description",
            min_length=1.0,
            max_length=256.0
        )
    )


@dataclass
class AttributeType:
    """
    Used to have tag value without code list for tag
    """

    selection_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="selectionDetails",
            type="Element",
            help="Option parameters",
            min_occurs=1,
            max_occurs=10
        )
    )


@dataclass
class AttributeType61377S:
    """
    Used to have tag value without code list for tag
    """

    attribute_qualifier: str = field(
        default=None,
        metadata=dict(
            name="attributeQualifier",
            type="Element",
            help="Criteria Set Type",
            min_length=1.0,
            max_length=3.0
        )
    )
    attribute_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            help="Criteria details",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class BooleanExpressionRuleType:
    """
    To perform boolean operations
    """

    boolean_expression: str = field(
        default=None,
        metadata=dict(
            name="booleanExpression",
            type="Element",
            help="Boolean expression associated to the decision rule.",
            required=True
        )
    )


@dataclass
class BucketDetailsType:
    code: str = field(
        default=None,
        metadata=dict(
            name="code",
            type="Element",
            help="Code",
            min_length=1.0,
            max_length=3.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            help="Option or distribution",
            min_length=1.0,
            max_length=3.0
        )
    )
    attribute: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="attribute",
            type="Element",
            help="Attribute",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class BucketInformationType:
    number: str = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            help="Number",
            min_length=1.0,
            max_length=3.0
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            help="Name",
            min_length=1.0,
            max_length=20.0
        )
    )
    completion: str = field(
        default=None,
        metadata=dict(
            name="completion",
            type="Element",
            help="Completion",
            pattern="[0-9A-Z]{1,3}"
        )
    )
    mode: str = field(
        default=None,
        metadata=dict(
            name="mode",
            type="Element",
            help="Mode",
            min_length=1.0,
            max_length=3.0
        )
    )
    value_ref: str = field(
        default=None,
        metadata=dict(
            name="valueRef",
            type="Element",
            help="Value reference",
            min_length=1.0,
            max_length=3.0
        )
    )
    weight: str = field(
        default=None,
        metadata=dict(
            name="weight",
            type="Element",
            help="Weight",
            pattern="-?[0-9]{1,4}"
        )
    )
    count: str = field(
        default=None,
        metadata=dict(
            name="count",
            type="Element",
            help="Number of solutions in the bucket",
            pattern="-?[0-9]{1,6}"
        )
    )
    attribute_count: str = field(
        default=None,
        metadata=dict(
            name="attributeCount",
            type="Element",
            help="Number of solutions per attribute",
            pattern="-?[0-9]{1,6}"
        )
    )


@dataclass
class CabinClassDesignationType:
    """
    Cabin class designation
    """

    cabin_designator: str = field(
        default=None,
        metadata=dict(
            name="cabinDesignator",
            type="Element",
            help="Cabin designator.",
            required=True,
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class CabinIdentificationType:
    cabin_qualifier: str = field(
        default=None,
        metadata=dict(
            name="cabinQualifier",
            type="Element",
            help="Cabin qualifier. For Star Pricer,MD stands for Mandatory Cabin qualifier. For other products no qualifier stands for Mandatory Cabin.",
            min_length=1.0,
            max_length=2.0
        )
    )
    cabin: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="cabin",
            type="Element",
            help="Cabin",
            min_occurs=1,
            max_occurs=3,
            min_length=0.0,
            max_length=1.0
        )
    )


@dataclass
class CabinIdentificationType233500C:
    cabin_qualifier: str = field(
        default=None,
        metadata=dict(
            name="cabinQualifier",
            type="Element",
            help="Cabin qualifier. For Star Pricer,MD stands for Mandatory Cabin qualifier. For other products no qualifier stands for Mandatory Cabin.",
            min_length=1.0,
            max_length=2.0
        )
    )
    cabin: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="cabin",
            type="Element",
            help="Cabin",
            min_occurs=0,
            max_occurs=5,
            min_length=0.0,
            max_length=1.0
        )
    )


@dataclass
class CabinProductDetailsType:
    rbd: str = field(
        default=None,
        metadata=dict(
            name="rbd",
            type="Element",
            help="Reservation booking designator - RBD",
            required=True,
            min_length=1.0,
            max_length=1.0
        )
    )
    booking_modifier: str = field(
        default=None,
        metadata=dict(
            name="bookingModifier",
            type="Element",
            help="Reservation Booking Modifier",
            pattern="[0-9A-Z]"
        )
    )
    cabin: str = field(
        default=None,
        metadata=dict(
            name="cabin",
            type="Element",
            help="Indicates the cabin related to the Booking code",
            min_length=1.0,
            max_length=1.0
        )
    )
    avl_status: str = field(
        default=None,
        metadata=dict(
            name="avlStatus",
            type="Element",
            help="Availibility status : posting level",
            pattern="[0-9A-Z]{1,3}"
        )
    )


@dataclass
class CodedAttributeInformationType:
    """
    Attribute information
    """

    attribute_type: str = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
            help="Attribute type identification",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    attribute_description: str = field(
        default=None,
        metadata=dict(
            name="attributeDescription",
            type="Element",
            help="Attribute Description",
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class CodedAttributeInformationType120742C:
    """
    Convey coded key and corresponding value
    """

    name: str = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            help="Name.",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="value",
            type="Element",
            help="Value.",
            min_occurs=0,
            max_occurs=10,
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class CodedAttributeInformationType139508C:
    """
    Convey coded key and corresponding value
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            help="Attribute type",
            min_length=1.0,
            max_length=5.0
        )
    )
    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="value",
            type="Element",
            help="Value.",
            min_occurs=0,
            max_occurs=10,
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class CodedAttributeInformationType247828C:
    """
    Convey coded key and corresponding value
    """

    attribute_type: str = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
            help=None,
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    attribute_description: str = field(
        default=None,
        metadata=dict(
            name="attributeDescription",
            type="Element",
            help="Attribute description",
            min_length=1.0,
            max_length=10.0
        )
    )


@dataclass
class CodedAttributeInformationType254574C:
    """
    Convey coded key and corresponding value
    """

    attribute_type: str = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
            help="Attribute type",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    attribute_description: str = field(
        default=None,
        metadata=dict(
            name="attributeDescription",
            type="Element",
            help="Attribute description",
            min_length=1.0,
            max_length=50.0
        )
    )


@dataclass
class CodedAttributeInformationType275401C:
    """
    Convey coded key and corresponding value
    """

    fee_type: str = field(
        default=None,
        metadata=dict(
            name="feeType",
            type="Element",
            help="Type of fee/reduction",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    fee_id_number: str = field(
        default=None,
        metadata=dict(
            name="feeIdNumber",
            type="Element",
            help="Fee Id Number",
            required=True,
            min_length=1.0,
            max_length=50.0
        )
    )


@dataclass
class CodedAttributeType:
    """
    Used to have tag value without code list for tag
    """

    attribute_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            help="Attribute details",
            min_occurs=1,
            max_occurs=9
        )
    )


@dataclass
class CodedAttributeType197696S:
    """
    Used to have tag value without code list for tag
    """

    fee_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="feeId",
            type="Element",
            help="Fee/reduction Id",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class CodedAttributeType78500S:
    """
    Used to have tag value without code list for tag
    """

    attribute_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            help="Atrribute details.",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class CommercialAgreementsType:
    """
    To specify commercial agreements between two or more companies related to joint, shared, lease operations etc.
    """

    codeshare_details: str = field(
        default=None,
        metadata=dict(
            name="codeshareDetails",
            type="Element",
            help="Codeshare Details",
            required=True
        )
    )
    other_codeshare_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="otherCodeshareDetails",
            type="Element",
            help="Other codeshare details",
            min_occurs=0,
            max_occurs=8
        )
    )


@dataclass
class CommercialAgreementsType78540S:
    """
    To specify commercial agreements between two or more companies related to joint, shared, lease operations etc.
    """

    codeshare_details: str = field(
        default=None,
        metadata=dict(
            name="codeshareDetails",
            type="Element",
            help="Codeshare Details",
        )
    )
    other_codeshare_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="otherCodeshareDetails",
            type="Element",
            help="Other codeshare details",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class CompanyIdentificationType120719C:
    carrier_qualifier: str = field(
        default=None,
        metadata=dict(
            name="carrierQualifier",
            type="Element",
            help="Item description identification.",
            required=True,
            min_length=0.0,
            max_length=1.0
        )
    )
    carrier_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="carrierId",
            type="Element",
            help="carrier id",
            min_occurs=1,
            max_occurs=99,
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class CompanyIdentificationType195544C:
    marketing_carrier: str = field(
        default=None,
        metadata=dict(
            name="marketingCarrier",
            type="Element",
            help="Marketing carrier",
            required=True,
            min_length=2.0,
            max_length=3.0
        )
    )
    operating_carrier: str = field(
        default=None,
        metadata=dict(
            name="operatingCarrier",
            type="Element",
            help="Operating carrier",
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class CompanyIdentificationType275415C:
    carrier_qualifier: str = field(
        default=None,
        metadata=dict(
            name="carrierQualifier",
            type="Element",
            help="Item description identification.",
            required=True,
            min_length=0.0,
            max_length=1.0
        )
    )
    carrier_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="carrierId",
            type="Element",
            help="carrier id",
            min_occurs=1,
            max_occurs=999,
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class CompanyIdentificationTypeI:
    """
    Code or name to identify a company and any associated companies.
    """

    marketing_company: str = field(
        default=None,
        metadata=dict(
            name="marketingCompany",
            type="Element",
            help="Carrier code",
            required=True,
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class CompanyRoleIdentificationType:
    """
    To indicate commercial agreements related to the service being provided.
    """

    transport_stage_qualifier: str = field(
        default=None,
        metadata=dict(
            name="transportStageQualifier",
            type="Element",
            help="Codeshare qualifier",
            required=True,
            min_length=1.0,
            max_length=1.0
        )
    )
    airline_designator: str = field(
        default=None,
        metadata=dict(
            name="airlineDesignator",
            type="Element",
            help="company identification",
            min_length=2.0,
            max_length=3.0
        )
    )
    flight_number: str = field(
        default=None,
        metadata=dict(
            name="flightNumber",
            type="Element",
            help="flight number",
            pattern="-?[0-9]{1,4}"
        )
    )
    operational_suffix: str = field(
        default=None,
        metadata=dict(
            name="operationalSuffix",
            type="Element",
            help="suffix",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class CompanyRoleIdentificationType120761C:
    """
    To indicate commercial agreements related to the service being provided.
    """

    code_share_type: str = field(
        default=None,
        metadata=dict(
            name="codeShareType",
            type="Element",
            help="Type of code share agreement.",
            min_length=1.0,
            max_length=1.0
        )
    )
    airline_designator: str = field(
        default=None,
        metadata=dict(
            name="airlineDesignator",
            type="Element",
            help="company identification",
            min_length=2.0,
            max_length=3.0
        )
    )
    flight_number: str = field(
        default=None,
        metadata=dict(
            name="flightNumber",
            type="Element",
            help="flight number",
            pattern="-?[0-9]{1,4}"
        )
    )


@dataclass
class ConnectPointDetailsType:
    exclusion_identifier: str = field(
        default=None,
        metadata=dict(
            name="exclusionIdentifier",
            type="Element",
            help="Exclusion identification",
            required=True,
            min_length=0.0,
            max_length=1.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            help="Place or Location identification",
            required=True,
            min_length=3.0,
            max_length=5.0
        )
    )
    airport_city_qualifier: str = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            help="Airport/city qualifier",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class ConnectPointDetailsType195492C:
    inclusion_identifier: str = field(
        default=None,
        metadata=dict(
            name="inclusionIdentifier",
            type="Element",
            help="Inclusion identification",
            required=True,
            min_length=0.0,
            max_length=1.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            help="Place or Location identification",
            required=True,
            min_length=3.0,
            max_length=5.0
        )
    )
    airport_city_qualifier: str = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            help="Airport/city qualifier",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class ConnectionDetailsTypeI:
    """
    To specify the location, product supplier and time for a connection with the next means of transport.
    """

    location: str = field(
        default=None,
        metadata=dict(
            name="location",
            type="Element",
            help="Location",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ConnectionTypeI:
    """
    To specify connection city and airline designator.
    """

    connection_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="connectionDetails",
            type="Element",
            help="Connection details.",
            min_occurs=1,
            max_occurs=17
        )
    )


@dataclass
class ConsumerReferenceIdentificationTypeI:
    """
    Identification of consumer references by type, company, number and reference to a traveller.
    """

    reference_qualifier: str = field(
        default=None,
        metadata=dict(
            name="referenceQualifier",
            type="Element",
            help=None,
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    reference_number: str = field(
        default=None,
        metadata=dict(
            name="referenceNumber",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=35.0
        )
    )
    reference_party_name: str = field(
        default=None,
        metadata=dict(
            name="referencePartyName",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=35.0
        )
    )
    traveller_reference_nbr: str = field(
        default=None,
        metadata=dict(
            name="travellerReferenceNbr",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=10.0
        )
    )


@dataclass
class ConsumerReferenceInformationType:
    """
    To specify consumer reference information.
    """

    customer_references: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="customerReferences",
            type="Element",
            help="Customer references",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class ConversionRateDetailsType:
    conversion_type: str = field(
        default=None,
        metadata=dict(
            name="conversionType",
            type="Element",
            help="Conversion type",
            min_length=1.0,
            max_length=3.0
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            help="Currency",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ConversionRateType:
    """
    To specify conversion rate details
    """

    conversion_rate_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="conversionRateDetail",
            type="Element",
            help="Detail of conversion rate of First Monetary Unit",
            min_occurs=1,
            max_occurs=2
        )
    )


@dataclass
class CorporateFareIdentifiersType:
    fare_qualifier: str = field(
        default=None,
        metadata=dict(
            name="fareQualifier",
            type="Element",
            help="Indicates the type of corporate fares requested",
            min_length=1.0,
            max_length=3.0
        )
    )
    identify_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="identifyNumber",
            type="Element",
            help="Corporate contract number or name",
            min_occurs=0,
            max_occurs=20,
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class CorporateFareInformationType:
    """
    To specify corporate fare information
    """

    corporate_fare_identifiers: str = field(
        default=None,
        metadata=dict(
            name="corporateFareIdentifiers",
            type="Element",
            help="Corporate fare identifiers",
        )
    )


@dataclass
class CorporateIdentificationType:
    """
    To specify corporate number(s) or name(s)
    """

    corporate_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="corporateId",
            type="Element",
            help="Corporate identity",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class CorporateIdentityType:
    """
    Corporate fare types indicated in PTK are detailed
    """

    corporate_qualifier: str = field(
        default=None,
        metadata=dict(
            name="corporateQualifier",
            type="Element",
            help="Indicates if 1A corporate (RC) or Unifare corporate (RW) requested.",
            required=True,
            min_length=0.0,
            max_length=3.0
        )
    )
    identity: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="identity",
            type="Element",
            help="Corporate contract number or name",
            min_occurs=1,
            max_occurs=9,
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class CriteriaiDetaislType:
    """
    Criteria details : weights/parameters list
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=3.0
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=18.0
        )
    )
    attribute: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="attribute",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99,
            min_length=1.0,
            max_length=9.0
        )
    )


@dataclass
class DataInformationType:
    """
    To identify specific data and a quantity related to the data.
    """

    indicator: str = field(
        default=None,
        metadata=dict(
            name="indicator",
            type="Element",
            help="Ancillary services options",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class DataTypeInformationType:
    """
    To identify the type of data to be sent and to qualify the data when required.
    """

    sub_type: str = field(
        default=None,
        metadata=dict(
            name="subType",
            type="Element",
            help="Carrier fee code",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    option: str = field(
        default=None,
        metadata=dict(
            name="option",
            type="Element",
            help="Status (automated, manually added, exempted). Default is automated",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class DateAndTimeDetailsType:
    """
    DATE AND TIME DETAILS
    """

    flexibility_qualifier: str = field(
        default=None,
        metadata=dict(
            name="flexibilityQualifier",
            type="Element",
            help="Trip Duration type(Plus,Minus,Combined)",
            min_length=1.0,
            max_length=3.0
        )
    )
    trip_interval: str = field(
        default=None,
        metadata=dict(
            name="tripInterval",
            type="Element",
            help="Number of days added or/and retrieved to the trip duration",
            pattern="-?[0-9]{1,6}"
        )
    )
    trip_duration: str = field(
        default=None,
        metadata=dict(
            name="tripDuration",
            type="Element",
            help="Period between date of departure and date of arrival",
            pattern="-?[0-9]{1,4}"
        )
    )


@dataclass
class DateAndTimeDetailsType120762C:
    date_qualifier: str = field(
        default=None,
        metadata=dict(
            name="dateQualifier",
            type="Element",
            help="Date time period qualifier",
            min_length=1.0,
            max_length=3.0
        )
    )
    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            help="First Date",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    first_time: str = field(
        default=None,
        metadata=dict(
            name="firstTime",
            type="Element",
            help="First Time",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    equipement_type: str = field(
        default=None,
        metadata=dict(
            name="equipementType",
            type="Element",
            help="Movement type.",
            min_length=1.0,
            max_length=3.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            help="Place/location identification.",
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class DateAndTimeDetailsType254619C:
    """
    DATE AND TIME DETAILS
    """

    range_qualifier: str = field(
        default=None,
        metadata=dict(
            name="rangeQualifier",
            type="Element",
            help="To identify type of range (Plus,Minus or combined)",
            min_length=1.0,
            max_length=3.0
        )
    )
    day_interval: str = field(
        default=None,
        metadata=dict(
            name="dayInterval",
            type="Element",
            help="Range of dates : Number of Days preceding or/and Following the request departure date",
            pattern="-?[0-9]{1,6}"
        )
    )
    time_atdestination: str = field(
        default=None,
        metadata=dict(
            name="timeAtdestination",
            type="Element",
            help="Time at destination (local)",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )


@dataclass
class DateAndTimeDetailsTypeI:
    """
    DATE AND TIME DETAILS
    """

    time_qualifier: str = field(
        default=None,
        metadata=dict(
            name="timeQualifier",
            type="Element",
            help="Toidentify type of time Arrival/Departure",
            min_length=1.0,
            max_length=3.0
        )
    )
    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            help="Date",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time: str = field(
        default=None,
        metadata=dict(
            name="time",
            type="Element",
            help="Time",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    time_window: str = field(
        default=None,
        metadata=dict(
            name="timeWindow",
            type="Element",
            help="Time window size in hours",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class DateAndTimeDetailsTypeI120740C:
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            help="Date time period qualifier",
            min_length=1.0,
            max_length=3.0
        )
    )
    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            help="First Date",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time: str = field(
        default=None,
        metadata=dict(
            name="time",
            type="Element",
            help="First Time",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    qualifier2: str = field(
        default=None,
        metadata=dict(
            name="qualifier2",
            type="Element",
            help=".",
            min_length=1.0,
            max_length=3.0
        )
    )
    reserved1: str = field(
        default=None,
        metadata=dict(
            name="reserved1",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=3.0
        )
    )
    reserved2: str = field(
        default=None,
        metadata=dict(
            name="reserved2",
            type="Element",
            help=None,
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class DateAndTimeInformationType:
    """
    not the standard only used in fare quote message
    """

    stop_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="stopDetails",
            type="Element",
            help="Details on date and time",
            min_occurs=1,
            max_occurs=2
        )
    )
    dummy_net: str = field(
        default=None,
        metadata=dict(
            name="Dummy.NET",
            type="Element",
            help=None,
        )
    )


@dataclass
class DateAndTimeInformationType181295S:
    """
    Target estimated or actual dates and times
    """

    first_date_time_detail: str = field(
        default=None,
        metadata=dict(
            name="firstDateTimeDetail",
            type="Element",
            help="Details on date and Time",
            required=True
        )
    )
    range_of_date: str = field(
        default=None,
        metadata=dict(
            name="rangeOfDate",
            type="Element",
            help="Details of the Requested Range of Dates",
        )
    )
    trip_details: str = field(
        default=None,
        metadata=dict(
            name="tripDetails",
            type="Element",
            help="Details of the trip duration",
        )
    )


@dataclass
class DateAndTimeInformationTypeI:
    """
    To convey information regarding estimated or actual dates and times of operational events
    """

    date_time_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="dateTimeDetails",
            type="Element",
            help="DATE AND TIME DETAILS.",
            min_occurs=0,
            max_occurs=2
        )
    )


@dataclass
class DateTimePeriodDetailsTypeI:
    """
    To indicate period of applicability.
    """

    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            help="Qualifier",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            help="Value",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class DepartureLocationType:
    """
    To convey information of requested departure
    """

    departure_point: str = field(
        default=None,
        metadata=dict(
            name="departurePoint",
            type="Element",
            help="Details on localization of the departure point",
        )
    )
    dep_multi_city: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="depMultiCity",
            type="Element",
            help="Departure multi city option",
            min_occurs=0,
            max_occurs=20
        )
    )
    first_pnr_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="firstPnrSegmentRef",
            type="Element",
            help="To specify a series or a range of PNR segments",
        )
    )
    attribute_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            help="Attribute details",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class FareDetailsType:
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            help="Qualifier",
            pattern="[0-9A-Z]{1,3}"
        )
    )
    rate: str = field(
        default=None,
        metadata=dict(
            name="rate",
            type="Element",
            help="Rate",
            pattern="-?[0-9]{1,8}"
        )
    )
    country: str = field(
        default=None,
        metadata=dict(
            name="country",
            type="Element",
            help="Country",
            min_length=1.0,
            max_length=3.0
        )
    )
    fare_category: str = field(
        default=None,
        metadata=dict(
            name="fareCategory",
            type="Element",
            help="Fare Category",
            pattern="[0-9A-Z]{1,3}"
        )
    )


@dataclass
class FareFamilyCriteriaType:
    """
    Fare family criteria
    """

    carrier_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="carrierId",
            type="Element",
            help="Fare publishing carrier.",
            min_occurs=0,
            max_occurs=20,
            min_length=1.0,
            max_length=3.0
        )
    )
    rdb: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="rdb",
            type="Element",
            help="Reservation booking designator.",
            min_occurs=0,
            max_occurs=20,
            min_length=1.0,
            max_length=2.0
        )
    )
    fare_family_info: str = field(
        default=None,
        metadata=dict(
            name="fareFamilyInfo",
            type="Element",
            help="Fare family info.",
        )
    )
    fare_product_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="fareProductDetail",
            type="Element",
            help="Fare product detail.",
            min_occurs=0,
            max_occurs=20
        )
    )
    corporate_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="corporateInfo",
            type="Element",
            help="Corporate information.",
            min_occurs=0,
            max_occurs=20
        )
    )
    cabin_product: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="cabinProduct",
            type="Element",
            help="Indicates flight cabin details.",
            min_occurs=0,
            max_occurs=6
        )
    )
    cabin_processing_identifier: str = field(
        default=None,
        metadata=dict(
            name="cabinProcessingIdentifier",
            type="Element",
            help="Cabin processing option.",
            min_length=1.0,
            max_length=3.0
        )
    )
    date_time_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="dateTimeDetails",
            type="Element",
            help="Product date or time.",
            min_occurs=0,
            max_occurs=20
        )
    )
    other_criteria: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="otherCriteria",
            type="Element",
            help="Other criteria.",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class FareFamilyDetailsType:
    """
    NEW FARE SEARCH
    """

    commercial_family: str = field(
        default=None,
        metadata=dict(
            name="commercialFamily",
            type="Element",
            help="Commercial fare Family Short name",
            required=True,
            min_length=1.0,
            max_length=10.0
        )
    )


@dataclass
class FareFamilyType:
    """
    NEW FARE SEACH
    """

    commercial_family_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="commercialFamilyDetails",
            type="Element",
            help="Indicates Commercial Fare Family Short names",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class FareFamilyType80157S:
    """
    NEW FARE SEACH
    """

    ref_number: str = field(
        default=None,
        metadata=dict(
            name="refNumber",
            type="Element",
            help="Fare Family Reference Number",
            pattern="-?[0-9]{1,3}"
        )
    )
    fare_familyname: str = field(
        default=None,
        metadata=dict(
            name="fareFamilyname",
            type="Element",
            help="Fare Family Short Name",
            min_length=1.0,
            max_length=10.0
        )
    )
    hierarchy: str = field(
        default=None,
        metadata=dict(
            name="hierarchy",
            type="Element",
            help="HIERARCHICAL ORDER WITHIN FARE FAMILY",
            pattern="-?[0-9]{1,4}"
        )
    )
    commercial_family_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="commercialFamilyDetails",
            type="Element",
            help="Indicates Commercial Fare Family Short names",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class FareInformationType:
    value_qualifier: str = field(
        default=None,
        metadata=dict(
            name="valueQualifier",
            type="Element",
            help="Value Qualifier",
            pattern="[0-9A-Z]{1,3}"
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            help="Value",
            pattern="-?[0-9]{1,15}"
        )
    )
    fare_details: str = field(
        default=None,
        metadata=dict(
            name="fareDetails",
            type="Element",
            help="Fare Details",
        )
    )
    identity_number: str = field(
        default=None,
        metadata=dict(
            name="identityNumber",
            type="Element",
            help="Identity Number",
            min_length=1.0,
            max_length=35.0
        )
    )
    fare_type_grouping: str = field(
        default=None,
        metadata=dict(
            name="fareTypeGrouping",
            type="Element",
            help="Fare Type Grouping",
        )
    )
    rate_category: str = field(
        default=None,
        metadata=dict(
            name="rateCategory",
            type="Element",
            help="Rate Category",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class FareInformationTypeI:
    """
    To specify fare details.
    """

    value_qualifier: str = field(
        default=None,
        metadata=dict(
            name="valueQualifier",
            type="Element",
            help="PTC (Full Codeset List described in ATPCo Documentation B11109 Appendix A)",
            min_length=1.0,
            max_length=3.0
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            help="age",
            pattern="-?[0-9]{1,15}"
        )
    )


@dataclass
class FareMasterPricerTravelBoardSearch:
    """
    Master Pricer Travel Board Search Flex pricer Flex pricer.
    """

    number_of_unit: str = field(
        default=None,
        metadata=dict(
            name="numberOfUnit",
            type="Element",
            help="Number of seats , recommendations.",
        )
    )
    global_options: str = field(
        default=None,
        metadata=dict(
            name="globalOptions",
            type="Element",
            help="Global options",
        )
    )
    pax_reference: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="paxReference",
            type="Element",
            help="Traveler Details",
            min_occurs=0,
            max_occurs=6
        )
    )
    customer_ref: str = field(
        default=None,
        metadata=dict(
            name="customerRef",
            type="Element",
            help="Customer references",
        )
    )
    form_of_payment_by_passenger: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="formOfPaymentByPassenger",
            type="Element",
            help="Fee with different payment forms by passenger.",
            min_occurs=0,
            max_occurs=60
        )
    )
    solution_family: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="solutionFamily",
            type="Element",
            help="Solution Family",
            min_occurs=0,
            max_occurs=20
        )
    )
    passenger_info_grp: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="passengerInfoGrp",
            type="Element",
            help="Passenger info group (9 ADT + 9 IN)",
            min_occurs=0,
            max_occurs=9
        )
    )
    fare_families: List["FareMasterPricerTravelBoardSearch.str"] = field(
        default_factory=list,
        metadata=dict(
            name="fareFamilies",
            type="Element",
            help="Fare families.",
            min_occurs=0,
            max_occurs=20
        )
    )
    fare_options: "FareMasterPricerTravelBoardSearch.str" = field(
        default=None,
        metadata=dict(
            name="fareOptions",
            type="Element",
            help="Fare options",
        )
    )
    price_to_beat: str = field(
        default=None,
        metadata=dict(
            name="priceToBeat",
            type="Element",
            help="Indicates Price to beat",
        )
    )
    tax_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="taxInfo",
            type="Element",
            help="Tax Details",
            min_occurs=0,
            max_occurs=9
        )
    )
    travel_flight_info: str = field(
        default=None,
        metadata=dict(
            name="travelFlightInfo",
            type="Element",
            help="Details of a Flight : Direct, Non stop...",
        )
    )
    value_search: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="valueSearch",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    buckets: List["FareMasterPricerTravelBoardSearch.str"] = field(
        default_factory=list,
        metadata=dict(
            name="buckets",
            type="Element",
            help="Buckets",
            min_occurs=0,
            max_occurs=10
        )
    )
    itinerary: List["FareMasterPricerTravelBoardSearch.str"] = field(
        default_factory=list,
        metadata=dict(
            name="itinerary",
            type="Element",
            help="Itinerary",
            min_occurs=0,
            max_occurs=18
        )
    )
    ticket_change_info: "FareMasterPricerTravelBoardSearch.str" = field(
        default=None,
        metadata=dict(
            name="ticketChangeInfo",
            type="Element",
            help="Changed ticket information.",
        )
    )
    combination_fare_families: List["FareMasterPricerTravelBoardSearch.str"] = field(
        default_factory=list,
        metadata=dict(
            name="combinationFareFamilies",
            type="Element",
            help="Specify fare family combinations",
            min_occurs=0,
            max_occurs=2000
        )
    )
    fee_option: List["FareMasterPricerTravelBoardSearch.str"] = field(
        default_factory=list,
        metadata=dict(
            name="feeOption",
            type="Element",
            help="Fee option group.",
            min_occurs=0,
            max_occurs=9
        )
    )
    office_id_details: List["FareMasterPricerTravelBoardSearch.str"] = field(
        default_factory=list,
        metadata=dict(
            name="officeIdDetails",
            type="Element",
            help="List of Office Id Details",
            min_occurs=0,
            max_occurs=20
        )
    )

    @dataclass
    class FareFamilies:
        family_information: str = field(
            default=None,
            metadata=dict(
                name="familyInformation",
                type="Element",
                help="Segment used to target Commercial Fare Family.",
                required=True
            )
        )
        family_criteria: str = field(
            default=None,
            metadata=dict(
                name="familyCriteria",
                type="Element",
                help="Description of Fare Family Criteria.",
            )
        )
        fare_family_segment: List["FareMasterPricerTravelBoardSearch.FareFamilies.str"] = field(
            default_factory=list,
            metadata=dict(
                name="fareFamilySegment",
                type="Element",
                help="Fare family requested segment details.",
                min_occurs=0,
                max_occurs=6
            )
        )
        other_possible_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.str"] = field(
            default_factory=list,
            metadata=dict(
                name="otherPossibleCriteria",
                type="Element",
                help="Description of other possible fare family criteria.",
                min_occurs=0,
                max_occurs=20
            )
        )

        @dataclass
        class FareFamilySegment:
            reference_info: str = field(
                default=None,
                metadata=dict(
                    name="referenceInfo",
                    type="Element",
                    help="Requested segment reference",
                    required=True
                )
            )
            family_criteria: str = field(
                default=None,
                metadata=dict(
                    name="familyCriteria",
                    type="Element",
                    help="Description of fare family criteria.",
                )
            )

        @dataclass
        class OtherPossibleCriteria:
            logical_link: str = field(
                default=None,
                metadata=dict(
                    name="logicalLink",
                    type="Element",
                    help="Logical link with other criteria.",
                    required=True
                )
            )
            family_criteria: str = field(
                default=None,
                metadata=dict(
                    name="familyCriteria",
                    type="Element",
                    help="Description of fare family criteria.",
                )
            )
            fare_family_segment: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.str"] = field(
                default_factory=list,
                metadata=dict(
                    name="fareFamilySegment",
                    type="Element",
                    help="Fare family requested segment details.",
                    min_occurs=0,
                    max_occurs=6
                )
            )

            @dataclass
            class FareFamilySegment:
                reference_info: str = field(
                    default=None,
                    metadata=dict(
                        name="referenceInfo",
                        type="Element",
                        help="Requested segment reference",
                        required=True
                    )
                )
                family_criteria: str = field(
                    default=None,
                    metadata=dict(
                        name="familyCriteria",
                        type="Element",
                        help="Description of fare family criteria.",
                    )
                )

    @dataclass
    class FareOptions:
        pricing_tick_info: str = field(
            default=None,
            metadata=dict(
                name="pricingTickInfo",
                type="Element",
                help="Pricing and ticketing details.",
                required=True
            )
        )
        corporate: str = field(
            default=None,
            metadata=dict(
                name="corporate",
                type="Element",
                help="Corporate name/number used to target fares",
            )
        )
        ticketing_price_scheme: str = field(
            default=None,
            metadata=dict(
                name="ticketingPriceScheme",
                type="Element",
                help="Ticketing price scheme.",
            )
        )
        fee_id_description: str = field(
            default=None,
            metadata=dict(
                name="feeIdDescription",
                type="Element",
                help="PSR number",
            )
        )
        conversion_rate: str = field(
            default=None,
            metadata=dict(
                name="conversionRate",
                type="Element",
                help="Used to force the currency of pricing",
            )
        )
        form_of_payment: str = field(
            default=None,
            metadata=dict(
                name="formOfPayment",
                type="Element",
                help="Form of payment information.",
            )
        )
        frequent_traveller_info: str = field(
            default=None,
            metadata=dict(
                name="frequentTravellerInfo",
                type="Element",
                help="Frequent traveller information",
            )
        )
        monetary_cabin_info: str = field(
            default=None,
            metadata=dict(
                name="monetaryCabinInfo",
                type="Element",
                help="Monetary and cabin information.",
            )
        )

    @dataclass
    class Buckets:
        bucket_info: str = field(
            default=None,
            metadata=dict(
                name="bucketInfo",
                type="Element",
                help="Bucket information: name, priority, weight",
                required=True
            )
        )
        bucket_details: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="bucketDetails",
                type="Element",
                help="Bucket details",
                min_occurs=0,
                max_occurs=15
            )
        )

    @dataclass
    class Itinerary:
        requested_segment_ref: str = field(
            default=None,
            metadata=dict(
                name="requestedSegmentRef",
                type="Element",
                help="Indicates reference of the requested segment",
                required=True
            )
        )
        departure_localization: str = field(
            default=None,
            metadata=dict(
                name="departureLocalization",
                type="Element",
                help="Specification of the requested departure point",
            )
        )
        arrival_localization: str = field(
            default=None,
            metadata=dict(
                name="arrivalLocalization",
                type="Element",
                help="Specification of the requested arrival point",
            )
        )
        time_details: str = field(
            default=None,
            metadata=dict(
                name="timeDetails",
                type="Element",
                help="Details on requested date and time plus range of date trip duration",
            )
        )
        flight_info: str = field(
            default=None,
            metadata=dict(
                name="flightInfo",
                type="Element",
                help="Specify Flight options.",
            )
        )
        family_information: str = field(
            default=None,
            metadata=dict(
                name="familyInformation",
                type="Element",
                help="Segment used to target Commercial Fare Family at requested segment level",
            )
        )
        value_search: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="valueSearch",
                type="Element",
                help=None,
                min_occurs=0,
                max_occurs=99
            )
        )
        group_of_flights: List["FareMasterPricerTravelBoardSearch.Itinerary.str"] = field(
            default_factory=list,
            metadata=dict(
                name="groupOfFlights",
                type="Element",
                help="list of proposed segments per requested segment",
                min_occurs=0,
                max_occurs=6
            )
        )
        flight_info_pnr: List["FareMasterPricerTravelBoardSearch.Itinerary.str"] = field(
            default_factory=list,
            metadata=dict(
                name="flightInfoPNR",
                type="Element",
                help="Info concerning the flights booked in the PNR",
                min_occurs=0,
                max_occurs=4
            )
        )
        requested_segment_action: str = field(
            default=None,
            metadata=dict(
                name="requestedSegmentAction",
                type="Element",
                help="Action identification for the requested segment",
            )
        )
        attributes: str = field(
            default=None,
            metadata=dict(
                name="attributes",
                type="Element",
                help="Coded attributes",
            )
        )

        @dataclass
        class GroupOfFlights:
            prop_flight_gr_detail: str = field(
                default=None,
                metadata=dict(
                    name="propFlightGrDetail",
                    type="Element",
                    help="To indicate parameters for proposed flight group.",
                    required=True
                )
            )
            price_to_beat: str = field(
                default=None,
                metadata=dict(
                    name="priceToBeat",
                    type="Element",
                    help="Indicates Price to beat",
                )
            )
            flight_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.str"] = field(
                default_factory=list,
                metadata=dict(
                    name="flightDetails",
                    type="Element",
                    help="list of flight per proposed segment",
                    min_occurs=1,
                    max_occurs=4
                )
            )

            @dataclass
            class FlightDetails:
                flight_information: str = field(
                    default=None,
                    metadata=dict(
                        name="flightInformation",
                        type="Element",
                        help="Specification of details on the flight and posting availability",
                        required=True
                    )
                )
                avl_info: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="avlInfo",
                        type="Element",
                        help="returns booking class and availability context",
                        min_occurs=0,
                        max_occurs=6
                    )
                )
                technical_stop: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="technicalStop",
                        type="Element",
                        help="Details on Flight date, time and location of technical stop or change of gauge",
                        min_occurs=0,
                        max_occurs=5
                    )
                )
                commercial_agreement: str = field(
                    default=None,
                    metadata=dict(
                        name="commercialAgreement",
                        type="Element",
                        help="Code Share Agreement description for current flight.",
                    )
                )
                add_info: str = field(
                    default=None,
                    metadata=dict(
                        name="addInfo",
                        type="Element",
                        help="Additional Info about flight, such as Reference number, and several options",
                    )
                )
                terminal_equipment_details: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="terminalEquipmentDetails",
                        type="Element",
                        help="Terminal, Equipment and EFT Details. If a Total EFT of the Travel Solution is requested then we will have 2 occurrences of the terminalEquipmentDetails attached to the first leg flightInformation: the 1st occurence will give the EFT of the leg, the 2nd occurrence will give the total EFT of the Travel Solution.",
                        min_occurs=0,
                        max_occurs=2
                    )
                )
                reservation_info: str = field(
                    default=None,
                    metadata=dict(
                        name="reservationInfo",
                        type="Element",
                        help="PNR flight reservation info",
                    )
                )
                price_to_beat: str = field(
                    default=None,
                    metadata=dict(
                        name="priceToBeat",
                        type="Element",
                        help="Indicates Price to beat",
                    )
                )

        @dataclass
        class FlightInfoPnr:
            travel_response_details: str = field(
                default=None,
                metadata=dict(
                    name="travelResponseDetails",
                    type="Element",
                    help="Travel Response Details: - Board/Off aiports - Flight number - Part of the journey - Day difference between Board and off - Departure/Arrival dates - Departure/Arrival times",
                    required=True
                )
            )
            time_table_date: str = field(
                default=None,
                metadata=dict(
                    name="timeTableDate",
                    type="Element",
                    help="Time Table Effective/Discontinue dates and frequency of operating Travel Solution",
                )
            )
            terminal_equipment_details: List[str] = field(
                default_factory=list,
                metadata=dict(
                    name="terminalEquipmentDetails",
                    type="Element",
                    help="Terminal, Equipment and EFT Details. If a Total EFT of the Travel Solution is requested then we will have 2 occurrences of the terminalEquipmentDetails attached to the first leg travelResponseDetails: the 1st occurrence will give the EFT of the leg, the 2nd occurrence will give the total EFT of the Travel Solution.",
                    min_occurs=0,
                    max_occurs=2
                )
            )
            codeshare_data: str = field(
                default=None,
                metadata=dict(
                    name="codeshareData",
                    type="Element",
                    help="Codeshare data",
                )
            )
            disclosure: str = field(
                default=None,
                metadata=dict(
                    name="disclosure",
                    type="Element",
                    help="Disclosure message from an operating carrier.",
                )
            )
            stop_details: str = field(
                default=None,
                metadata=dict(
                    name="stopDetails",
                    type="Element",
                    help="Stops Details",
                )
            )
            traffic_restriction_data: str = field(
                default=None,
                metadata=dict(
                    name="trafficRestrictionData",
                    type="Element",
                    help="Traffic restriction information",
                )
            )
            reservation_info: str = field(
                default=None,
                metadata=dict(
                    name="reservationInfo",
                    type="Element",
                    help="PNR flight reservation info",
                )
            )
            incidental_stop_info: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.str"] = field(
                default_factory=list,
                metadata=dict(
                    name="incidentalStopInfo",
                    type="Element",
                    help="Incidental stop information.",
                    min_occurs=0,
                    max_occurs=8
                )
            )

            @dataclass
            class IncidentalStopInfo:
                date_time_info: str = field(
                    default=None,
                    metadata=dict(
                        name="dateTimeInfo",
                        type="Element",
                        help="Incidental stop date/time information",
                        required=True
                    )
                )

    @dataclass
    class TicketChangeInfo:
        ticket_number_details: str = field(
            default=None,
            metadata=dict(
                name="ticketNumberDetails",
                type="Element",
                help="Ticket nb details.",
                required=True
            )
        )
        ticket_requested_segments: List["FareMasterPricerTravelBoardSearch.TicketChangeInfo.str"] = field(
            default_factory=list,
            metadata=dict(
                name="ticketRequestedSegments",
                type="Element",
                help="Changed ticket requested segments.",
                min_occurs=0,
                max_occurs=6
            )
        )

        @dataclass
        class TicketRequestedSegments:
            action_identification: str = field(
                default=None,
                metadata=dict(
                    name="actionIdentification",
                    type="Element",
                    help="Action identification.",
                    required=True
                )
            )
            connect_point_details: str = field(
                default=None,
                metadata=dict(
                    name="connectPointDetails",
                    type="Element",
                    help="Connected cities in changed ticket requested segment.",
                )
            )

    @dataclass
    class CombinationFareFamilies:
        item_ffcnumber: str = field(
            default=None,
            metadata=dict(
                name="itemFFCNumber",
                type="Element",
                help="Specification of the item number",
                required=True
            )
        )
        nb_of_units: str = field(
            default=None,
            metadata=dict(
                name="nbOfUnits",
                type="Element",
                help="Number of units.",
            )
        )
        reference_info: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="referenceInfo",
                type="Element",
                help="Requested segment reference",
                min_occurs=0,
                max_occurs=6
            )
        )

    @dataclass
    class FeeOption:
        fee_type_info: str = field(
            default=None,
            metadata=dict(
                name="feeTypeInfo",
                type="Element",
                help="Nature of the fee (OB,OC,..)",
                required=True
            )
        )
        rate_tax: str = field(
            default=None,
            metadata=dict(
                name="rateTax",
                type="Element",
                help="Associated rate tax.",
            )
        )
        fee_details: List["FareMasterPricerTravelBoardSearch.FeeOption.str"] = field(
            default_factory=list,
            metadata=dict(
                name="feeDetails",
                type="Element",
                help="Details for each fee.",
                min_occurs=0,
                max_occurs=99
            )
        )

        @dataclass
        class FeeDetails:
            fee_info: str = field(
                default=None,
                metadata=dict(
                    name="feeInfo",
                    type="Element",
                    help="Fee information",
                    required=True
                )
            )
            associated_amounts: str = field(
                default=None,
                metadata=dict(
                    name="associatedAmounts",
                    type="Element",
                    help="Associated amounts : amounts to take into account to calculate fee.",
                )
            )
            fee_description_grp: "FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.str" = field(
                default=None,
                metadata=dict(
                    name="feeDescriptionGrp",
                    type="Element",
                    help="Fee description",
                )
            )

            @dataclass
            class FeeDescriptionGrp:
                item_number_info: str = field(
                    default=None,
                    metadata=dict(
                        name="itemNumberInfo",
                        type="Element",
                        help="Specification of the item number",
                        required=True
                    )
                )
                service_attributes_info: str = field(
                    default=None,
                    metadata=dict(
                        name="serviceAttributesInfo",
                        type="Element",
                        help="Attributes (SSR code EMD, RFIC, SSIM)",
                    )
                )
                service_description_info: str = field(
                    default=None,
                    metadata=dict(
                        name="serviceDescriptionInfo",
                        type="Element",
                        help="Other service information (service description, ...)",
                    )
                )

    @dataclass
    class OfficeIdDetails:
        office_id_information: str = field(
            default=None,
            metadata=dict(
                name="officeIdInformation",
                type="Element",
                help="Office Id Information",
                required=True
            )
        )
        nb_of_units: str = field(
            default=None,
            metadata=dict(
                name="nbOfUnits",
                type="Element",
                help="Number of units.",
            )
        )
        uid_option: str = field(
            default=None,
            metadata=dict(
                name="uidOption",
                type="Element",
                help="UID option",
            )
        )
        pricing_tick_info: str = field(
            default=None,
            metadata=dict(
                name="pricingTickInfo",
                type="Element",
                help="Pricing and ticketing details.",
            )
        )
        corporate_fare_info: str = field(
            default=None,
            metadata=dict(
                name="corporateFareInfo",
                type="Element",
                help="Corporate fare information",
            )
        )
        travel_flight_info: str = field(
            default=None,
            metadata=dict(
                name="travelFlightInfo",
                type="Element",
                help="Details of a Flight : Direct, Non stop...",
            )
        )
        airline_distribution_details: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.str"] = field(
            default_factory=list,
            metadata=dict(
                name="airlineDistributionDetails",
                type="Element",
                help="Details of airline distribution at requested segment level",
                min_occurs=0,
                max_occurs=6
            )
        )

        @dataclass
        class AirlineDistributionDetails:
            requested_segment_ref: str = field(
                default=None,
                metadata=dict(
                    name="requestedSegmentRef",
                    type="Element",
                    help="Indicates reference of the requested segment",
                    required=True
                )
            )
            flight_info: str = field(
                default=None,
                metadata=dict(
                    name="flightInfo",
                    type="Element",
                    help="Specify Flight options.",
                )
            )


@dataclass
class FareProductDetailsType:
    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="fareBasis",
            type="Element",
            help="Fare basis code",
            min_length=0.0,
            max_length=18.0
        )
    )
    fare_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="fareType",
            type="Element",
            help="Type of fare",
            min_occurs=0,
            max_occurs=3,
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class FareQualifierInformationType:
    """
    To specify multiple qualifier for fare selections.
    """

    fare_family_qual: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="fareFamilyQual",
            type="Element",
            help="Fare family combinability.",
            min_occurs=1,
            max_occurs=9,
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class FareTypeGroupingInformationType:
    pricing_group: str = field(
        default=None,
        metadata=dict(
            name="pricingGroup",
            type="Element",
            help="Pricing Group",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class FlightProductInformationType:
    """
    To specify flight product information details
    """

    cabin_product: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="cabinProduct",
            type="Element",
            help="Indicates flight cabin details",
            min_occurs=0,
            max_occurs=26
        )
    )
    context_details: str = field(
        default=None,
        metadata=dict(
            name="contextDetails",
            type="Element",
            help="To specify additional characteristics.",
        )
    )


@dataclass
class FoprepresentationType:
    form_of_payment_details: str = field(
        default=None,
        metadata=dict(
            name="formOfPaymentDetails",
            type="Element",
            help="Form of payment information.",
            required=True
        )
    )
    passenger_fee_reference: str = field(
        default=None,
        metadata=dict(
            name="passengerFeeReference",
            type="Element",
            help="Fee/Reduction Passenger reference.",
        )
    )


@dataclass
class FormOfPaymentDetailsTypeI:
    """
    To specify the form of payment type, amounts, approval codes, and other related information.
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            help="Form of payment identification",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    charged_amount: str = field(
        default=None,
        metadata=dict(
            name="chargedAmount",
            type="Element",
            help="amount to be charged on this form",
        )
    )
    credit_card_number: str = field(
        default=None,
        metadata=dict(
            name="creditCardNumber",
            type="Element",
            help="Reference number",
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class FormOfPaymentTypeI:
    """
    To convey details describing the form of payment.
    """

    form_of_payment_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="formOfPaymentDetails",
            type="Element",
            help="FORM OF PAYMENT DETAILS",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class FreeTextDetailsType:
    text_subject_qualifier: str = field(
        default=None,
        metadata=dict(
            name="textSubjectQualifier",
            type="Element",
            help="Qualifier of the free text. Always literal in our usage.",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    information_type: str = field(
        default=None,
        metadata=dict(
            name="informationType",
            type="Element",
            help="Type of the free text. Always 7 for our usage.",
            min_length=1.0,
            max_length=4.0
        )
    )
    source: str = field(
        default=None,
        metadata=dict(
            name="source",
            type="Element",
            help="Source of the information.",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    encoding: str = field(
        default=None,
        metadata=dict(
            name="encoding",
            type="Element",
            help="Encoding method used.",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class FreeTextInformationType:
    """
    This segment is used to convey the free text
    """

    free_text_details: str = field(
        default=None,
        metadata=dict(
            name="freeTextDetails",
            type="Element",
            help="Details for the free text message",
            required=True
        )
    )
    free_text: str = field(
        default=None,
        metadata=dict(
            name="freeText",
            type="Element",
            help="Free text corresponding to the DEI 127 data.",
            required=True,
            min_length=1.0,
            max_length=70.0
        )
    )


@dataclass
class FrequencyType:
    """
    Give the days of the week involved for a period
    """

    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            help="Indicate if the sequence number represents days of the week or days of the month.",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="value",
            type="Element",
            help="Used to represent days of the week. 1 is monday and 7 is sunday.",
            min_occurs=0,
            max_occurs=7,
            pattern="-?[0-9]{1,1}"
        )
    )


@dataclass
class FrequentTravellerIdentificationCodeType:
    """
    To specify frequent traveler information
    """

    frequent_traveller_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="frequentTravellerDetails",
            type="Element",
            help="Frequent Traveller Info",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class FrequentTravellerIdentificationCodeType177150S:
    """
    To specify frequent traveler information.
    """

    frequent_traveller_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="frequentTravellerDetails",
            type="Element",
            help="Frequent traveller details",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class FrequentTravellerIdentificationType:
    carrier: str = field(
        default=None,
        metadata=dict(
            name="carrier",
            type="Element",
            help="Carrier where the FQTV is registered.",
            min_length=1.0,
            max_length=35.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=28.0
        )
    )
    customer_reference: str = field(
        default=None,
        metadata=dict(
            name="customerReference",
            type="Element",
            help="Specifies which traveller in the TIF segment the frequent traveller number applies (same as 9944 in TIF).",
            min_length=1.0,
            max_length=10.0
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="status",
            type="Element",
            help="status code: 'OK' if the frequent flyer card has been validated",
            min_length=1.0,
            max_length=3.0
        )
    )
    tier_level: str = field(
        default=None,
        metadata=dict(
            name="tierLevel",
            type="Element",
            help="To specify a Tier linked to the FQTV",
            min_length=1.0,
            max_length=35.0
        )
    )
    priority_code: str = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            help="For example : priority code",
            min_length=1.0,
            max_length=12.0
        )
    )
    tier_description: str = field(
        default=None,
        metadata=dict(
            name="tierDescription",
            type="Element",
            help="For example : Level description",
            min_length=1.0,
            max_length=35.0
        )
    )
    company_code: str = field(
        default=None,
        metadata=dict(
            name="companyCode",
            type="Element",
            help="For example : Company code of alliance",
            min_length=1.0,
            max_length=35.0
        )
    )
    customer_value: str = field(
        default=None,
        metadata=dict(
            name="customerValue",
            type="Element",
            help=None,
            pattern="-?[0-9]{1,4}"
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            help="To specify the product/account number qualifier. (e.g. 2=Corporate Frequent Flyer).",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class FrequentTravellerIdentificationType249074C:
    """
    Identification of the frequent traveller number by company code with the capability to reference a specific traveller.
    """

    carrier: str = field(
        default=None,
        metadata=dict(
            name="carrier",
            type="Element",
            help="carrier",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            help="Frequent traveller number",
            min_length=1.0,
            max_length=25.0
        )
    )
    customer_reference: str = field(
        default=None,
        metadata=dict(
            name="customerReference",
            type="Element",
            help="Customer reference",
            min_length=1.0,
            max_length=10.0
        )
    )
    tier_level: str = field(
        default=None,
        metadata=dict(
            name="tierLevel",
            type="Element",
            help="Tier level",
            min_length=1.0,
            max_length=35.0
        )
    )
    priority_code: str = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            help="Priority code",
            min_length=1.0,
            max_length=12.0
        )
    )
    tier_description: str = field(
        default=None,
        metadata=dict(
            name="tierDescription",
            type="Element",
            help="Tier description",
            min_length=1.0,
            max_length=35.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            help="To specify the product/account number qualifier. (e.g. 2=Corporate Frequent Flyer).",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class GroupPassengerDetailsType:
    """
    Contain passenger information
    """

    passenger_reference: str = field(
        default=None,
        metadata=dict(
            name="passengerReference",
            type="Element",
            help="Trigger",
            required=True
        )
    )
    psg_details_info: List["GroupPassengerDetailsType.str"] = field(
        default_factory=list,
        metadata=dict(
            name="psgDetailsInfo",
            type="Element",
            help="pricing option at passenger level",
            min_occurs=0,
            max_occurs=2
        )
    )

    @dataclass
    class PsgDetailsInfo:
        discount_ptc: str = field(
            default=None,
            metadata=dict(
                name="discountPtc",
                type="Element",
                help="PTC/Discount Code age",
                required=True
            )
        )
        flequent_flyer_details: str = field(
            default=None,
            metadata=dict(
                name="flequentFlyerDetails",
                type="Element",
                help="Tier level information",
            )
        )


@dataclass
class HeaderInformationTypeI:
    """
    To specify header information applicable to the entire message.
    """

    status: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="status",
            type="Element",
            help="Status",
            min_occurs=0,
            max_occurs=2,
            min_length=1.0,
            max_length=3.0
        )
    )
    date_time_period_details: str = field(
        default=None,
        metadata=dict(
            name="dateTimePeriodDetails",
            type="Element",
            help="Date and Time info",
        )
    )
    reference_number: str = field(
        default=None,
        metadata=dict(
            name="referenceNumber",
            type="Element",
            help="Reference number",
            min_length=1.0,
            max_length=35.0
        )
    )
    product_identification: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="productIdentification",
            type="Element",
            help="Contains product identification such as UIC code...",
            min_occurs=0,
            max_occurs=2,
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class ItemNumberIdentificationType:
    """
    Goods identification for a specified source
    """

    number: str = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            help="Fare family combination number",
            min_length=1.0,
            max_length=4.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            help="Type",
            min_length=1.0,
            max_length=3.0
        )
    )
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            help="Qualifier",
            min_length=1.0,
            max_length=3.0
        )
    )
    responsible_agency: str = field(
        default=None,
        metadata=dict(
            name="responsibleAgency",
            type="Element",
            help="Responsible agency",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ItemNumberType:
    """
    To specify an item number
    """

    item_number_id: str = field(
        default=None,
        metadata=dict(
            name="itemNumberId",
            type="Element",
            help="Indicates the fare family combination number",
            required=True
        )
    )


@dataclass
class ItemNumberType80866S:
    """
    To specify an item number
    """

    item_number_details: str = field(
        default=None,
        metadata=dict(
            name="itemNumberDetails",
            type="Element",
            help="Item number details",
            required=True
        )
    )


@dataclass
class ItemReferencesAndVersionsType:
    """
    Exchange and link unique identifiers
    """

    passenger_fee_ref_type: str = field(
        default=None,
        metadata=dict(
            name="passengerFeeRefType",
            type="Element",
            help="Reference Qualifier.",
            min_length=1.0,
            max_length=3.0
        )
    )
    passenger_fee_ref_number: str = field(
        default=None,
        metadata=dict(
            name="passengerFeeRefNumber",
            type="Element",
            help="Reference number.",
            pattern="-?[0-9]{1,3}"
        )
    )
    other_characteristics: str = field(
        default=None,
        metadata=dict(
            name="otherCharacteristics",
            type="Element",
            help="Unique id description.",
        )
    )


@dataclass
class ItineraryDetailsType:
    """
    Forces arrival or departure to/from the same city or airport option
    """

    airport_city_qualifier: str = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            help="Airport/City Qualifier: the passenger wants to depart/arrive from/to the same airport or city in the specified requested segment",
            required=True,
            min_length=1.0,
            max_length=1.0
        )
    )
    segment_number: str = field(
        default=None,
        metadata=dict(
            name="segmentNumber",
            type="Element",
            help="Requested segment number",
            required=True,
            pattern="-?[0-9]{1,3}"
        )
    )


@dataclass
class LocationDetailsTypeI:
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            help="Place or Location identification",
            required=True,
            min_length=3.0,
            max_length=5.0
        )
    )
    country: str = field(
        default=None,
        metadata=dict(
            name="country",
            type="Element",
            help="Country, coded",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class LocationIdentificationDetailsType:
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            help="3 characters ATA/IATA airport/city code",
            required=True,
            min_length=3.0,
            max_length=5.0
        )
    )
    airport_city_qualifier: str = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            help="Airport/city qualifier: the requested point is an airport when ambiguity exists (e.g. HOU)",
            min_length=1.0,
            max_length=1.0
        )
    )
    terminal: str = field(
        default=None,
        metadata=dict(
            name="terminal",
            type="Element",
            help="Terminal information",
            min_length=1.0,
            max_length=5.0
        )
    )


@dataclass
class LocationTypeI:
    """
    To identify a location by code or name.
    """

    true_location_id: str = field(
        default=None,
        metadata=dict(
            name="trueLocationId",
            type="Element",
            help="Departure or Arrival IATA airport code",
            required=True,
            min_length=3.0,
            max_length=3.0
        )
    )


@dataclass
class MileageTimeDetailsTypeI:
    """
    Information about the distance/duration of a trip.
    """

    elapsed_ground_time: str = field(
        default=None,
        metadata=dict(
            name="elapsedGroundTime",
            type="Element",
            help="Ground Time in minutes at Board point (connection with incoming flight)",
            pattern="-?[0-9]{1,4}"
        )
    )


@dataclass
class MonetaryAndCabinInformationDetailsType:
    amount_type: str = field(
        default=None,
        metadata=dict(
            name="amountType",
            type="Element",
            help="Amount qualifier.",
            min_length=0.0,
            max_length=3.0
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            help="Amount",
            required=True
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            help="ISO currency code",
            min_length=1.0,
            max_length=3.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            help="Airport/city code",
            min_length=3.0,
            max_length=5.0
        )
    )
    cabin_class_designator: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="cabinClassDesignator",
            type="Element",
            help="Cabin class designator",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class MonetaryAndCabinInformationType:
    money_and_cabin_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="moneyAndCabinInfo",
            type="Element",
            help="Monetary and cabin information.",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class MonetaryInformationDetailsTypeI:
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            help="Monetary amount type qualifier, coded",
            min_length=1.0,
            max_length=3.0
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            help="Allowance or charge number",
            required=True,
            pattern="-?[0-9]{1,18}"
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            help="Currency, coded",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class MonetaryInformationDetailsTypeI194597C:
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            help="Monetary amount type qualifier, coded",
            min_length=1.0,
            max_length=3.0
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            help="Allowance or charge number",
            required=True,
            pattern="-?[0-9]{1,18}"
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            help="Currency, coded",
            min_length=1.0,
            max_length=3.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            help="Place or Location identification",
            min_length=3.0,
            max_length=3.0
        )
    )


@dataclass
class MonetaryInformationDetailsTypeI65140C:
    """
    To specify the type of monetary amount, the amount, and the currency code.
    """

    type_qualifier: str = field(
        default=None,
        metadata=dict(
            name="typeQualifier",
            type="Element",
            help="Qualifier",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            help="Amount",
            min_length=1.0,
            max_length=12.0
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            help="Currency",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class MonetaryInformationDetailsTypeI65141C:
    """
    To specify the type of monetary amount, the amount, and the currency code.
    """

    type_qualifier: str = field(
        default=None,
        metadata=dict(
            name="typeQualifier",
            type="Element",
            help="Qualifier",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            help="Amount",
            min_length=1.0,
            max_length=12.0
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            help="Currency",
            min_length=1.0,
            max_length=3.0
        )
    )
    location: str = field(
        default=None,
        metadata=dict(
            name="location",
            type="Element",
            help="Location",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class MonetaryInformationType:
    """
    To specify monetary information details
    """

    money_info: str = field(
        default=None,
        metadata=dict(
            name="moneyInfo",
            type="Element",
            help="MONEY INFORMATION",
            required=True
        )
    )
    additional_money_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="additionalMoneyInfo",
            type="Element",
            help="MONEY INFORMATION",
            min_occurs=0,
            max_occurs=19
        )
    )


@dataclass
class MonetaryInformationType80162S:
    """
    To convey monetary amounts, rates and percentages.
    """

    monetary_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="monetaryDetails",
            type="Element",
            help="Monetary info",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class MonetaryInformationTypeI:
    """
    To convey monetary amounts, rates and percentages.
    """

    monetary_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="monetaryDetails",
            type="Element",
            help="Monetary info",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class MultiCityOptionType:
    """
    List of requested arrival points
    """

    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            help="ATA/IATA airport/city code of arrival multi city option enable to define until 20 airports/cities",
            required=True,
            min_length=3.0,
            max_length=5.0
        )
    )
    airport_city_qualifier: str = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            help="Requested arrival point is an airport or a city (default is city and used only when ambiguity)",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class MultipleIdentificationNumbersTypeI:
    """
    To specify more than one identification number.
    """

    corporate_number_identifier: str = field(
        default=None,
        metadata=dict(
            name="corporateNumberIdentifier",
            type="Element",
            help="Corporate number or ALL.",
            min_length=1.0,
            max_length=12.0
        )
    )
    corporate_name: str = field(
        default=None,
        metadata=dict(
            name="corporateName",
            type="Element",
            help="Corporate name.",
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class NumberOfUnitDetailsType:
    number_of_units: str = field(
        default=None,
        metadata=dict(
            name="numberOfUnits",
            type="Element",
            help="Number of Units",
            pattern="-?[0-9]{1,4}"
        )
    )
    type_of_unit: str = field(
        default=None,
        metadata=dict(
            name="typeOfUnit",
            type="Element",
            help="Number of unit qualifier",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class NumberOfUnitDetailsType270113C:
    number_of_units: str = field(
        default=None,
        metadata=dict(
            name="numberOfUnits",
            type="Element",
            help="Number of Units",
            required=True,
            pattern="-?[0-9]{1,6}"
        )
    )
    type_of_unit: str = field(
        default=None,
        metadata=dict(
            name="typeOfUnit",
            type="Element",
            help="Number of unit qualifier",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class NumberOfUnitDetailsTypeI:
    number_of_units: str = field(
        default=None,
        metadata=dict(
            name="numberOfUnits",
            type="Element",
            help="Number of Units",
            required=True,
            pattern="-?[0-9]{1,3}"
        )
    )
    type_of_unit: str = field(
        default=None,
        metadata=dict(
            name="typeOfUnit",
            type="Element",
            help="Number of unit qualifier",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class NumberOfUnitsType:
    """
    To specify the number of Units required
    """

    unit_number_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="unitNumberDetail",
            type="Element",
            help="NUMBER OF UNIT DETAILS",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class NumberOfUnitsType80154S:
    """
    To specify the number of Units required
    """

    unit_number_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="unitNumberDetail",
            type="Element",
            help="NUMBER OF UNIT DETAILS",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class OriginAndDestinationRequestType:
    """
    To convey information regarding Requested Segments
    """

    seg_ref: str = field(
        default=None,
        metadata=dict(
            name="segRef",
            type="Element",
            help="Requested segment number",
            required=True,
            pattern="-?[0-9]{1,2}"
        )
    )
    location_forcing: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="locationForcing",
            type="Element",
            help="Forces arrival or departure, from/to the same airport/city",
            min_occurs=0,
            max_occurs=2
        )
    )


@dataclass
class OriginatorIdentificationDetailsTypeI:
    """
    To identify a user
    """

    office_name: str = field(
        default=None,
        metadata=dict(
            name="officeName",
            type="Element",
            help="Office Name.",
            pattern="-?[0-9]{1,9}"
        )
    )
    agent_signin: str = field(
        default=None,
        metadata=dict(
            name="agentSignin",
            type="Element",
            help="Agent Sign In .",
            min_length=1.0,
            max_length=9.0
        )
    )
    confidential_office: str = field(
        default=None,
        metadata=dict(
            name="confidentialOffice",
            type="Element",
            help="Confidential Office Name.",
            min_length=1.0,
            max_length=9.0
        )
    )
    other_office: str = field(
        default=None,
        metadata=dict(
            name="otherOffice",
            type="Element",
            help="Other Office Name",
            min_length=1.0,
            max_length=9.0
        )
    )


@dataclass
class PassengerItineraryInformationType:
    """
    Contains PNR travel (Reservation Booking code, Booking status). Only present in case with-PNR.
    """

    booking: str = field(
        default=None,
        metadata=dict(
            name="booking",
            type="Element",
            help=".",
            min_length=1.0,
            max_length=1.0
        )
    )
    identifier: str = field(
        default=None,
        metadata=dict(
            name="identifier",
            type="Element",
            help=".",
            min_length=1.0,
            max_length=1.0
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="status",
            type="Element",
            help=".",
            min_length=1.0,
            max_length=3.0
        )
    )
    item_number: str = field(
        default=None,
        metadata=dict(
            name="itemNumber",
            type="Element",
            help=".",
            pattern="-?[0-9]{1,3}"
        )
    )
    date_time_details: str = field(
        default=None,
        metadata=dict(
            name="dateTimeDetails",
            type="Element",
            help=".",
        )
    )
    designator: str = field(
        default=None,
        metadata=dict(
            name="designator",
            type="Element",
            help=".",
            min_length=1.0,
            max_length=1.0
        )
    )
    movement_type: str = field(
        default=None,
        metadata=dict(
            name="movementType",
            type="Element",
            help=".",
            min_length=1.0,
            max_length=3.0
        )
    )
    product_type_details: str = field(
        default=None,
        metadata=dict(
            name="productTypeDetails",
            type="Element",
            help=".",
        )
    )


@dataclass
class PnrsegmentReferenceType:
    """
    Reference to PNR segment
    """

    pnr_segment_tattoo: str = field(
        default=None,
        metadata=dict(
            name="pnrSegmentTattoo",
            type="Element",
            help="For a request from PNR: this is the reference number of a PNR air segment. In case a range of PNR segments is specified (eg. segments 2-5), then it is the 1st of the range, the last being in ARR.",
            pattern="-?[0-9]{0,35}"
        )
    )
    pnr_segment_qualifier: str = field(
        default=None,
        metadata=dict(
            name="pnrSegmentQualifier",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class PricingTicketingDetailsType:
    """
    To specify pricing/ticketing details
    """

    pricing_ticketing: str = field(
        default=None,
        metadata=dict(
            name="pricingTicketing",
            type="Element",
            help="Pricing ticketing Details.",
        )
    )
    ticketing_date: str = field(
        default=None,
        metadata=dict(
            name="ticketingDate",
            type="Element",
            help="PRODUCT DATE OR TIME",
        )
    )
    company_id: str = field(
        default=None,
        metadata=dict(
            name="companyId",
            type="Element",
            help="COMPANY IDENTIFICATION",
        )
    )
    selling_point: str = field(
        default=None,
        metadata=dict(
            name="sellingPoint",
            type="Element",
            help="LOCATION DETAILS",
        )
    )
    ticketing_point: str = field(
        default=None,
        metadata=dict(
            name="ticketingPoint",
            type="Element",
            help="LOCATION DETAILS",
        )
    )
    journey_origin_point: str = field(
        default=None,
        metadata=dict(
            name="journeyOriginPoint",
            type="Element",
            help="Used to Target Transborder Fares",
        )
    )
    corporate_id: str = field(
        default=None,
        metadata=dict(
            name="corporateId",
            type="Element",
            help="Contains the ARC,IATA and ERSP numbers",
        )
    )


@dataclass
class PricingTicketingInformationType:
    """
    To specify indicators related to pricing and ticketing.
    """

    price_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="priceType",
            type="Element",
            help="Price type qualifier",
            min_occurs=1,
            max_occurs=50,
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class ProductDateTimeType:
    """
    Product date or time
    """

    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            help=".",
            required=True,
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time: str = field(
        default=None,
        metadata=dict(
            name="time",
            type="Element",
            help=".",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )


@dataclass
class ProductDateTimeType195546C:
    date_of_departure: str = field(
        default=None,
        metadata=dict(
            name="dateOfDeparture",
            type="Element",
            help="Departure date",
            required=True,
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time_of_departure: str = field(
        default=None,
        metadata=dict(
            name="timeOfDeparture",
            type="Element",
            help="Departure time",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    date_of_arrival: str = field(
        default=None,
        metadata=dict(
            name="dateOfArrival",
            type="Element",
            help="Arrival date",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time_of_arrival: str = field(
        default=None,
        metadata=dict(
            name="timeOfArrival",
            type="Element",
            help="Arrival time",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    date_variation: str = field(
        default=None,
        metadata=dict(
            name="dateVariation",
            type="Element",
            help="Arrival date compared to departure date, only if different from 0",
            pattern="-?[0-9]{1,1}"
        )
    )


@dataclass
class ProductDateTimeTypeI:
    """
    To specify the dates and times associated with a product.
    """

    departure_date: str = field(
        default=None,
        metadata=dict(
            name="departureDate",
            type="Element",
            help="Departure date in YYYYMMDD format",
            pattern="[0-9]{4}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])"
        )
    )
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="departureTime",
            type="Element",
            help="Departure time",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    arrival_date: str = field(
        default=None,
        metadata=dict(
            name="arrivalDate",
            type="Element",
            help="Arrival date",
            pattern="[0-9]{4}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])"
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="arrivalTime",
            type="Element",
            help="Arrival time",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    date_variation: str = field(
        default=None,
        metadata=dict(
            name="dateVariation",
            type="Element",
            help="Day difference between Departure date of the leg and date of reference (Departure or Arrival date specified in the SDI)",
            pattern="-?[0-9]{1,1}"
        )
    )


@dataclass
class ProductDateTimeTypeI194583C:
    """
    To specify the dates and times associated with a product.
    """

    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            help="Ticketing Purchase Date",
            required=True,
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    other_date: str = field(
        default=None,
        metadata=dict(
            name="otherDate",
            type="Element",
            help="Ticketing purchase date",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )


@dataclass
class ProductDateTimeTypeI194598C:
    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            help="First date",
            required=True,
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    rtc_date: str = field(
        default=None,
        metadata=dict(
            name="rtcDate",
            type="Element",
            help="Half round trip combination.",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )


@dataclass
class ProductFacilitiesType:
    """
    Level of access
    """

    last_seat_available: str = field(
        default=None,
        metadata=dict(
            name="lastSeatAvailable",
            type="Element",
            help="Yes-No indicator whether Last Seat Available",
            min_length=1.0,
            max_length=1.0
        )
    )
    level_of_access: str = field(
        default=None,
        metadata=dict(
            name="levelOfAccess",
            type="Element",
            help="Level of access",
            min_length=1.0,
            max_length=3.0
        )
    )
    electronic_ticketing: str = field(
        default=None,
        metadata=dict(
            name="electronicTicketing",
            type="Element",
            help="Yes-No indicator whether electronic ticketing",
            min_length=1.0,
            max_length=1.0
        )
    )
    operational_suffix: str = field(
        default=None,
        metadata=dict(
            name="operationalSuffix",
            type="Element",
            help="Product identification suffix",
            min_length=1.0,
            max_length=1.0
        )
    )
    product_detail_qualifier: str = field(
        default=None,
        metadata=dict(
            name="productDetailQualifier",
            type="Element",
            help="Define whether a flight has been polled or not",
            min_length=1.0,
            max_length=3.0
        )
    )
    flight_characteristic: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="flightCharacteristic",
            type="Element",
            help="Add some flight restrictions (See code set list)",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ProductIdentificationDetailsTypeI:
    """
    Code, number or name to identify a specific product or service.
    """

    flight_number: str = field(
        default=None,
        metadata=dict(
            name="flightNumber",
            type="Element",
            help="Flight number",
            required=True,
            pattern="-?[0-9]{1,4}"
        )
    )
    operational_suffix: str = field(
        default=None,
        metadata=dict(
            name="operationalSuffix",
            type="Element",
            help="Flight suffix",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class ProductIdentificationDetailsTypeI50878C:
    """
    Code, number or name to identify a specific product or service.
    """

    flight_number: str = field(
        default=None,
        metadata=dict(
            name="flightNumber",
            type="Element",
            help=None,
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    booking_class: str = field(
        default=None,
        metadata=dict(
            name="bookingClass",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=2.0
        )
    )
    operational_suffix: str = field(
        default=None,
        metadata=dict(
            name="operationalSuffix",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=3.0
        )
    )
    modifier: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="modifier",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=3,
            min_length=1.0,
            max_length=7.0
        )
    )


@dataclass
class ProductLocationDetailsTypeI:
    """
    To indicate a location and the type of location.
    """

    station: str = field(
        default=None,
        metadata=dict(
            name="station",
            type="Element",
            help="airport",
            min_length=3.0,
            max_length=3.0
        )
    )


@dataclass
class ProductTypeDetailsType:
    """
    Product type details
    """

    sequence_number: str = field(
        default=None,
        metadata=dict(
            name="sequenceNumber",
            type="Element",
            help=".",
            min_length=1.0,
            max_length=6.0
        )
    )
    availability_context: str = field(
        default=None,
        metadata=dict(
            name="availabilityContext",
            type="Element",
            help="PNR availability context",
            min_length=1.0,
            max_length=6.0
        )
    )


@dataclass
class ProductTypeDetailsType120801C:
    flight_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="flightType",
            type="Element",
            help="Type of flight",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=2.0
        )
    )


@dataclass
class ProductTypeDetailsType205137C:
    """
    To specify additional characteristics of a product or service.
    """

    avl: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="avl",
            type="Element",
            help="indicates whether the flight is domestic or international",
            min_occurs=1,
            max_occurs=9,
            min_length=1.0,
            max_length=6.0
        )
    )


@dataclass
class ProductTypeDetailsTypeI:
    """
    To specify additional characteristics of a product or service.
    """

    flight_indicator: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="flightIndicator",
            type="Element",
            help="Part of the journey (C,E,S), Codeshare service (A), Technical stop at off point in a Direct (TSD), Technical stop at off point in a COG (TSC), E-Ticket candidate (ET), Prohibited Countries (RPC, WPC)",
            min_occurs=1,
            max_occurs=5,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ProposedSegmentDetailsType:
    ref: str = field(
        default=None,
        metadata=dict(
            name="ref",
            type="Element",
            help="Flight proposal reference",
            min_length=1.0,
            max_length=6.0
        )
    )
    unit_qualifier: str = field(
        default=None,
        metadata=dict(
            name="unitQualifier",
            type="Element",
            help="Elapse Flying Time",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ProposedSegmentType:
    """
    To specify the parameters used for product quality
    """

    flight_proposal: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="flightProposal",
            type="Element",
            help="Parameters for proposed flight group",
            min_occurs=1,
            max_occurs=9
        )
    )
    flight_characteristic: str = field(
        default=None,
        metadata=dict(
            name="flightCharacteristic",
            type="Element",
            help="Flight characteristics.",
            min_length=0.0,
            max_length=3.0
        )
    )
    maj_cabin: str = field(
        default=None,
        metadata=dict(
            name="majCabin",
            type="Element",
            help="Majority cabin",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class ReferenceInfoType:
    """
    To provide specific reference identification for a traveller.
    """

    referencing_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="referencingDetail",
            type="Element",
            help="Referencing details",
            min_occurs=0,
            max_occurs=9
        )
    )
    dummy_net: str = field(
        default=None,
        metadata=dict(
            name="Dummy.NET",
            type="Element",
            help=None,
        )
    )


@dataclass
class ReferencingDetailsType:
    """
    Referencing details
    """

    ref_qualifier: str = field(
        default=None,
        metadata=dict(
            name="refQualifier",
            type="Element",
            help="Segment reference qualifier",
            min_length=1.0,
            max_length=3.0
        )
    )
    ref_number: str = field(
        default=None,
        metadata=dict(
            name="refNumber",
            type="Element",
            help="Flight or flight group reference",
            required=True,
            pattern="-?[0-9]{0,3}"
        )
    )


@dataclass
class RoutingInformationTypeI:
    """
    To provide routing information.
    """

    routing_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="routingDetails",
            type="Element",
            help="Stops details",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class SegmentRepetitionControlDetailsTypeI:
    """
    Information about the number of selection segments to be processed.
    """

    quantity: str = field(
        default=None,
        metadata=dict(
            name="quantity",
            type="Element",
            help="traveller number",
            pattern="-?[0-9]{1,15}"
        )
    )


@dataclass
class SegmentRepetitionControlTypeI:
    """
    To indicate the number of segment group repetitions.
    """

    segment_control_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="segmentControlDetails",
            type="Element",
            help="Segment control details",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class SelectionDetailsInformationType:
    """
    To specify a selected option and associated information.
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            help="Carrier fee type",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    option_information: str = field(
        default=None,
        metadata=dict(
            name="optionInformation",
            type="Element",
            help="Carrier fee status",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class SelectionDetailsInformationTypeI:
    """
    To specify a selected option and associated information.
    """

    option: str = field(
        default=None,
        metadata=dict(
            name="option",
            type="Element",
            help=None,
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    option_information: str = field(
        default=None,
        metadata=dict(
            name="optionInformation",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class SelectionDetailsType:
    """
    To specify the details for making a selection.
    """

    carrier_fee_details: str = field(
        default=None,
        metadata=dict(
            name="carrierFeeDetails",
            type="Element",
            help="Carrier fees options",
            required=True
        )
    )
    other_selection_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="otherSelectionDetails",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=98
        )
    )


@dataclass
class SpecialRequirementsDataDetailsType:
    """
    Special requirements data details
    """

    seat_characteristics: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="seatCharacteristics",
            type="Element",
            help="SSR seat characteristic",
            min_occurs=0,
            max_occurs=5,
            min_length=1.0,
            max_length=2.0
        )
    )
    dummy_net: str = field(
        default=None,
        metadata=dict(
            name="Dummy.NET",
            type="Element",
            help=None,
        )
    )


@dataclass
class SpecialRequirementsDetailsType:
    """
    To specify special requests or service s information relating to a traveller
    """

    service_requirements_info: str = field(
        default=None,
        metadata=dict(
            name="serviceRequirementsInfo",
            type="Element",
            help="To specify the Service Requirement of the customer",
            required=True
        )
    )
    seat_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="seatDetails",
            type="Element",
            help="Seat details",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class SpecialRequirementsTypeDetailsType:
    service_classification: str = field(
        default=None,
        metadata=dict(
            name="serviceClassification",
            type="Element",
            help="To specify the Service Classification of the Service Requirement.",
            required=True,
            min_length=1.0,
            max_length=4.0
        )
    )
    service_status: str = field(
        default=None,
        metadata=dict(
            name="serviceStatus",
            type="Element",
            help="Status",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_number_of_instances: str = field(
        default=None,
        metadata=dict(
            name="serviceNumberOfInstances",
            type="Element",
            help="To specify the number of items involved",
            pattern="-?[0-9]{1,15}"
        )
    )
    service_marketing_carrier: str = field(
        default=None,
        metadata=dict(
            name="serviceMarketingCarrier",
            type="Element",
            help="To specify to which marketing carrier the service applies",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_group: str = field(
        default=None,
        metadata=dict(
            name="serviceGroup",
            type="Element",
            help="Specify the Service group",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_sub_group: str = field(
        default=None,
        metadata=dict(
            name="serviceSubGroup",
            type="Element",
            help="Specify the Service Sub-Group",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_free_text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="serviceFreeText",
            type="Element",
            help="Free Text attached to the Service.",
            min_occurs=0,
            max_occurs=99,
            min_length=1.0,
            max_length=70.0
        )
    )


@dataclass
class SpecificDataInformationType:
    """
    To specify miscellaneous data by first identifying the type of data to be sent and then the actual data.
    """

    data_type_information: str = field(
        default=None,
        metadata=dict(
            name="dataTypeInformation",
            type="Element",
            help="Carrier fee description",
            required=True
        )
    )
    data_information: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="dataInformation",
            type="Element",
            help="Data information",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class StationInformationTypeI:
    """
    To specify departure/arrival information concerning a means of transport.
    """

    terminal: str = field(
        default=None,
        metadata=dict(
            name="terminal",
            type="Element",
            help="Departure terminal",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class StructuredDateTimeType:
    """
    Store date and time in a structured way
    """

    year: str = field(
        default=None,
        metadata=dict(
            name="year",
            type="Element",
            help="Year number. The format is a little long for short term usage but it can be reduced by implementation if required.",
            pattern="-?[0-9]{4,4}"
        )
    )
    month: str = field(
        default=None,
        metadata=dict(
            name="month",
            type="Element",
            help="Month number in the year ( begins to 1 )",
            pattern="-?[0-9]{1,2}"
        )
    )
    day: str = field(
        default=None,
        metadata=dict(
            name="day",
            type="Element",
            help="Day number in the month ( begins to 1 )",
            pattern="-?[0-9]{1,2}"
        )
    )


@dataclass
class StructuredPeriodInformationType:
    """
    This segment is designed to convey period in a structured way.
    """

    begin_date_time: str = field(
        default=None,
        metadata=dict(
            name="beginDateTime",
            type="Element",
            help="Effective date of period of operation",
        )
    )
    end_date_time: str = field(
        default=None,
        metadata=dict(
            name="endDateTime",
            type="Element",
            help="Discontinue date of period of operation",
        )
    )
    frequency: str = field(
        default=None,
        metadata=dict(
            name="frequency",
            type="Element",
            help="It is used with a period to give a restriction for days impacted. It permits for example to indicate on which days, a flight operates.",
        )
    )


@dataclass
class TaxDetailsTypeI:
    rate: str = field(
        default=None,
        metadata=dict(
            name="rate",
            type="Element",
            help="Duty/tax/fee rate",
            min_length=1.0,
            max_length=18.0
        )
    )
    country: str = field(
        default=None,
        metadata=dict(
            name="country",
            type="Element",
            help="Country, coded",
            min_length=1.0,
            max_length=3.0
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            help="Currency, coded",
            min_length=1.0,
            max_length=3.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            help="Duty/Tax fee type, coded",
            min_length=1.0,
            max_length=3.0
        )
    )
    amount_qualifier: str = field(
        default=None,
        metadata=dict(
            name="amountQualifier",
            type="Element",
            help="Amount type qualifier, coded",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class TaxType:
    """
    To specify details realting to tax(es)
    """

    withhold_tax_surcharge: str = field(
        default=None,
        metadata=dict(
            name="withholdTaxSurcharge",
            type="Element",
            help="Duty tax fee category, coded",
            min_length=1.0,
            max_length=3.0
        )
    )
    tax_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="taxDetail",
            type="Element",
            help="TAX DETAILS",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class TicketNumberDetailsTypeI:
    """
    To specify a ticket number, type of ticket, and related information.
    """

    number: str = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class TicketNumberTypeI:
    """
    To convey information related to a specific ticket.
    """

    document_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="documentDetails",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class TicketingPriceSchemeType:
    """
    Price Scheme Information
    """

    reference_number: str = field(
        default=None,
        metadata=dict(
            name="referenceNumber",
            type="Element",
            help="PSR (Price Scheme Reference): unique reference of the price scheme as a 8 digit number.",
            required=True,
            min_length=1.0,
            max_length=35.0
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            help="Price Scheme Name",
            min_length=1.0,
            max_length=35.0
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="status",
            type="Element",
            help="Price Scheme Status. Is the price scheme valid for service fee calculation ?",
            min_length=1.0,
            max_length=3.0
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            help="free flow description of the price scheme",
            min_length=1.0,
            max_length=250.0
        )
    )


@dataclass
class TrafficRestrictionDetailsTypeI:
    """
    Coded or free text details which restrict a means of transport.
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="code",
            type="Element",
            help="Traffic Restriction code",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class TrafficRestrictionTypeI:
    """
    To convey certain restrictions that apply to a means of transport on all or part of a journey
    """

    traffic_restriction_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="trafficRestrictionDetails",
            type="Element",
            help="Traffic Restriction Details",
            min_occurs=0,
            max_occurs=5
        )
    )


@dataclass
class TravelFlightInformationType:
    """
    Information about flight options
    """

    cabin_id: str = field(
        default=None,
        metadata=dict(
            name="cabinId",
            type="Element",
            help="Cabin identification",
        )
    )
    company_identity: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="companyIdentity",
            type="Element",
            help="Company Identification",
            min_occurs=0,
            max_occurs=20
        )
    )
    flight_detail: str = field(
        default=None,
        metadata=dict(
            name="flightDetail",
            type="Element",
            help="Type of flight details",
        )
    )
    inclusion_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="inclusionDetail",
            type="Element",
            help="Details of included connecting points",
            min_occurs=0,
            max_occurs=20
        )
    )
    exclusion_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="exclusionDetail",
            type="Element",
            help="Further connection details",
            min_occurs=0,
            max_occurs=2
        )
    )
    unit_number_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="unitNumberDetail",
            type="Element",
            help="Nb of connections for each requested segment of the journey.",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class TravelFlightInformationType165053S:
    """
    Information about flight options
    """

    cabin_id: str = field(
        default=None,
        metadata=dict(
            name="cabinId",
            type="Element",
            help="Cabin identification",
        )
    )
    company_identity: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="companyIdentity",
            type="Element",
            help="Company Identification",
            min_occurs=0,
            max_occurs=20
        )
    )
    flight_detail: str = field(
        default=None,
        metadata=dict(
            name="flightDetail",
            type="Element",
            help="Type of flight details",
        )
    )
    inclusion_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="inclusionDetail",
            type="Element",
            help="Details of included connect point",
            min_occurs=0,
            max_occurs=20
        )
    )
    exclusion_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="exclusionDetail",
            type="Element",
            help="Further connection details",
            min_occurs=0,
            max_occurs=20
        )
    )
    unit_number_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="unitNumberDetail",
            type="Element",
            help="Nb of connections allowed at requested segment level.",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class TravelFlightInformationType197722S:
    """
    Information about flight options
    """

    cabin_id: str = field(
        default=None,
        metadata=dict(
            name="cabinId",
            type="Element",
            help="Cabin identification",
        )
    )
    company_identity: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="companyIdentity",
            type="Element",
            help="Company Identification",
            min_occurs=0,
            max_occurs=20
        )
    )
    flight_detail: str = field(
        default=None,
        metadata=dict(
            name="flightDetail",
            type="Element",
            help="Type of flight details",
        )
    )
    inclusion_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="inclusionDetail",
            type="Element",
            help="Details of included connect point",
            min_occurs=0,
            max_occurs=20
        )
    )
    exclusion_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="exclusionDetail",
            type="Element",
            help="Further connection details",
            min_occurs=0,
            max_occurs=20
        )
    )
    unit_number_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="unitNumberDetail",
            type="Element",
            help="Added departed flights flag",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class TravelProductInformationTypeI:
    """
    To specify details related to a product.
    """

    flight_date: str = field(
        default=None,
        metadata=dict(
            name="flightDate",
            type="Element",
            help="Flight Date",
        )
    )
    board_point_details: str = field(
        default=None,
        metadata=dict(
            name="boardPointDetails",
            type="Element",
            help="Board point",
            required=True
        )
    )
    offpoint_details: str = field(
        default=None,
        metadata=dict(
            name="offpointDetails",
            type="Element",
            help="Off point",
            required=True
        )
    )
    company_details: str = field(
        default=None,
        metadata=dict(
            name="companyDetails",
            type="Element",
            help=None,
            required=True
        )
    )
    flight_identification: str = field(
        default=None,
        metadata=dict(
            name="flightIdentification",
            type="Element",
            help="Flight identification",
        )
    )
    flight_type_details: str = field(
        default=None,
        metadata=dict(
            name="flightTypeDetails",
            type="Element",
            help="Identify flight part of the journey",
        )
    )


@dataclass
class TravelProductType:
    """
    Contains flight travel (date, time, flight number,...) and posting avaibility information
    """

    product_date_time: str = field(
        default=None,
        metadata=dict(
            name="productDateTime",
            type="Element",
            help="Date and time of departure and arrival",
            required=True
        )
    )
    location: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="location",
            type="Element",
            help="Location of departure and arrival",
            min_occurs=1,
            max_occurs=2
        )
    )
    company_id: str = field(
        default=None,
        metadata=dict(
            name="companyId",
            type="Element",
            help="Company identification",
        )
    )
    flight_ortrain_number: str = field(
        default=None,
        metadata=dict(
            name="flightOrtrainNumber",
            type="Element",
            help="Flight number or trainNumber",
            min_length=1.0,
            max_length=8.0
        )
    )
    product_detail: str = field(
        default=None,
        metadata=dict(
            name="productDetail",
            type="Element",
            help="Product details",
        )
    )
    add_product_detail: str = field(
        default=None,
        metadata=dict(
            name="addProductDetail",
            type="Element",
            help="Additional product details",
        )
    )
    attribute_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            help="Attribute details",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class TravellerDetailsType:
    ref: str = field(
        default=None,
        metadata=dict(
            name="ref",
            type="Element",
            help="Direct reference of passenger assigned by requesting system.",
            required=True,
            pattern="-?[0-9]{1,3}"
        )
    )
    infant_indicator: str = field(
        default=None,
        metadata=dict(
            name="infantIndicator",
            type="Element",
            help="Traveller is an infant",
            pattern="-?[0-9]{1,1}"
        )
    )


@dataclass
class TravellerReferenceInformationType:
    """
    To specify traveller/personal details
    """

    ptc: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ptc",
            type="Element",
            help="Requested passenger type",
            min_occurs=0,
            max_occurs=3,
            min_length=1.0,
            max_length=6.0
        )
    )
    traveller: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="traveller",
            type="Element",
            help="Traveller details",
            min_occurs=1,
            max_occurs=9
        )
    )


@dataclass
class UniqueIdDescriptionType:
    passenger_fee_ref_qualif: str = field(
        default=None,
        metadata=dict(
            name="passengerFeeRefQualif",
            type="Element",
            help="Reference qualifier.",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class UserIdentificationType:
    """
    User Identification
    """

    office_identification: str = field(
        default=None,
        metadata=dict(
            name="officeIdentification",
            type="Element",
            help="Originator Identification Details",
        )
    )
    office_type: str = field(
        default=None,
        metadata=dict(
            name="officeType",
            type="Element",
            help="Used to specify which kind of info is given in DE 9900.",
            min_length=1.0,
            max_length=1.0
        )
    )
    office_code: str = field(
        default=None,
        metadata=dict(
            name="officeCode",
            type="Element",
            help="The code given to an agent by the originating reservation system.",
            min_length=1.0,
            max_length=30.0
        )
    )


@dataclass
class ValueSearchCriteriaType:
    """
    To specify Criteria with list of parameters
    """

    criteria_name: str = field(
        default=None,
        metadata=dict(
            name="criteriaName",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=50.0
        )
    )
    criteria_code: str = field(
        default=None,
        metadata=dict(
            name="criteriaCode",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=3.0
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            help=None,
            min_length=1.0,
            max_length=18.0
        )
    )
    criteria_details: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="criteriaDetails",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=10
        )
    )