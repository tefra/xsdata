from dataclasses import dataclass, field
from typing import List




@dataclass
class CompanyIdentificationType:
    
    pass


@dataclass
class AdditionalProductDetailsType:
    """
    :ivar equipment_type: Type of aircraft
    :ivar operating_day: Day number of the week
    :ivar tech_stop_number: Number of stops made in a journey if different from 0
    :ivar location_id: Location places of the stops
    """
    equipment_type: str = field(
        default=None,
        metadata=dict(
            name="equipmentType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    operating_day: str = field(
        default=None,
        metadata=dict(
            name="operatingDay",
            type="Element",
            min_length=1.0,
            max_length=7.0
        )
    )
    tech_stop_number: int = field(
        default=None,
        metadata=dict(
            name="techStopNumber",
            type="Element",
            pattern="-?[0-9]{1,2}"
        )
    )
    location_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="locationId",
            type="Element",
            min_occurs=0,
            max_occurs=3,
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class AdditionalProductTypeI:
    """Additional details describing a specific means of transport.

    :ivar equipment: Equipment type
    :ivar duration: Elaps flying time of the leg
    :ivar complexing_flight_indicator: COG indicator
    """
    equipment: str = field(
        default=None,
        metadata=dict(
            name="equipment",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    duration: int = field(
        default=None,
        metadata=dict(
            name="duration",
            type="Element",
            pattern="-?[0-9]{1,6}"
        )
    )
    complexing_flight_indicator: str = field(
        default=None,
        metadata=dict(
            name="complexingFlightIndicator",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class AgentIdentificationType:
    """
    :ivar arc_number: Contains ARC number
    :ivar ersp_number: ERSP number of the Office or Customer
    :ivar iata_number: IATA Number
    """
    arc_number: str = field(
        default=None,
        metadata=dict(
            name="arcNumber",
            type="Element",
            min_length=1.0,
            max_length=12.0
        )
    )
    ersp_number: str = field(
        default=None,
        metadata=dict(
            name="erspNumber",
            type="Element",
            min_length=1.0,
            max_length=12.0
        )
    )
    iata_number: str = field(
        default=None,
        metadata=dict(
            name="iataNumber",
            type="Element",
            min_length=1.0,
            max_length=12.0
        )
    )


@dataclass
class ArithmeticEvaluationType:
    """
    :ivar code_operator: Boolean operator
    """
    code_operator: str = field(
        default=None,
        metadata=dict(
            name="codeOperator",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ArrivalLocationDetailsType:
    """
    :ivar distance: For Radius: This is the length of the requested radius around the location of destination.
    :ivar distance_unit: Distance unit qualifier for radius
    :ivar location_id: ATA/IATA airport/city code of arrival In case of SP request from a PNR, this field is empty.
    :ivar airport_city_qualifier: Request from no PNR A = consider the locationID specified as an airport (used only when ambiguous) C = consider the locationId as a city (used only when ambiguous) A and C are not used in case of a request from PNR Request from a PNR with Radius option: O = radius applies to the origin of the PNR segments D = radius applies to the destination of the PNR segments
    :ivar latitude: Latitude in degrees (decimal format) with hemisphere N=north S=south
    :ivar longitude: Longitude in degrees (decimal format) with hemisphere E=east, W=west
    """
    distance: int = field(
        default=None,
        metadata=dict(
            name="distance",
            type="Element",
            pattern="-?[0-9]{1,3}"
        )
    )
    distance_unit: str = field(
        default=None,
        metadata=dict(
            name="distanceUnit",
            type="Element",
            min_length=0.0,
            max_length=3.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            min_length=3.0,
            max_length=5.0
        )
    )
    airport_city_qualifier: str = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    latitude: str = field(
        default=None,
        metadata=dict(
            name="latitude",
            type="Element",
            min_length=6.0,
            max_length=6.0
        )
    )
    longitude: str = field(
        default=None,
        metadata=dict(
            name="longitude",
            type="Element",
            min_length=6.0,
            max_length=6.0
        )
    )


@dataclass
class ArrivalLocationDetailsType120834C:
    """
    :ivar distance: For Radius: This is the length of the requested radius around the location of origin.
    :ivar distance_unit: Distance unit qualifier for radius
    :ivar location_id: ATA/IATA airport/city code of arrival In case of SP request from a PNR, this field is empty.
    :ivar airport_city_qualifier: Request from no PNR A = consider the locationID specified as an airport (used only when ambiguous) C = consider the locationId as a city (used only when ambiguous) A and C are not used in case of a request from PNR Request from a PNR with Radius option: O = radius applies to the origin of the PNR segments D = radius applies to the destination of the PNR segments
    :ivar latitude: Latitude in degrees (decimal format) with hemisphere N=north S=south
    :ivar longitude: Longitude in degrees (decimal format) with hemisphere E=east, W=west
    """
    distance: int = field(
        default=None,
        metadata=dict(
            name="distance",
            type="Element",
            pattern="-?[0-9]{1,3}"
        )
    )
    distance_unit: str = field(
        default=None,
        metadata=dict(
            name="distanceUnit",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            min_length=3.0,
            max_length=5.0
        )
    )
    airport_city_qualifier: str = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    latitude: str = field(
        default=None,
        metadata=dict(
            name="latitude",
            type="Element",
            min_length=6.0,
            max_length=6.0
        )
    )
    longitude: str = field(
        default=None,
        metadata=dict(
            name="longitude",
            type="Element",
            min_length=6.0,
            max_length=6.0
        )
    )


@dataclass
class AttributeDetailsType:
    """
    :ivar requested_sgt: Reference of the requested segment
    :ivar value: List of airlines, cabins, time window, number of connections.
    """
    requested_sgt: str = field(
        default=None,
        metadata=dict(
            name="requestedSgt",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="value",
            type="Element",
            min_occurs=0,
            max_occurs=50,
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class AttributeInformationType:
    """To identify the type of attribute and the attribute.

    :ivar option: Code of options
    :ivar option_information: Mandatory when alternate date option is used (ALT), must be set to plus (P) or minus (M) a number of days around the original PNR segment dates. E.g.: M1 (for minus 1 day) or P100 (for plus 100 days)
    """
    option: str = field(
        default=None,
        metadata=dict(
            name="option",
            type="Element",
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
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class AttributeInformationType97181C:
    """To identify the type of attribute and the attribute.

    :ivar attribute_type: Attribute type
    :ivar attribute_description: Attribute description
    """
    attribute_type: str = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
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
            min_length=1.0,
            max_length=256.0
        )
    )


@dataclass
class BucketInformationType:
    """
    :ivar number: Number
    :ivar name: Name
    :ivar completion: Completion
    :ivar mode: Mode
    :ivar value_ref: Value reference
    :ivar weight: Weight
    :ivar count: Number of solutions in the bucket
    :ivar attribute_count: Number of solutions per attribute
    """
    number: str = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            min_length=1.0,
            max_length=20.0
        )
    )
    completion: str = field(
        default=None,
        metadata=dict(
            name="completion",
            type="Element",
            pattern="[0-9A-Z]{1,3}"
        )
    )
    mode: str = field(
        default=None,
        metadata=dict(
            name="mode",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    value_ref: str = field(
        default=None,
        metadata=dict(
            name="valueRef",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    weight: int = field(
        default=None,
        metadata=dict(
            name="weight",
            type="Element",
            pattern="-?[0-9]{1,4}"
        )
    )
    count: int = field(
        default=None,
        metadata=dict(
            name="count",
            type="Element",
            pattern="-?[0-9]{1,6}"
        )
    )
    attribute_count: int = field(
        default=None,
        metadata=dict(
            name="attributeCount",
            type="Element",
            pattern="-?[0-9]{1,6}"
        )
    )


@dataclass
class CabinClassDesignationType:
    """Cabin class designation.

    :ivar cabin_designator: Cabin designator.
    """
    cabin_designator: str = field(
        default=None,
        metadata=dict(
            name="cabinDesignator",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class CabinIdentificationType:
    """
    :ivar cabin_qualifier: Cabin qualifier. For Star Pricer,MD stands for Mandatory Cabin qualifier. For other products no qualifier stands for Mandatory Cabin.
    :ivar cabin: Cabin
    """
    cabin_qualifier: str = field(
        default=None,
        metadata=dict(
            name="cabinQualifier",
            type="Element",
            min_length=1.0,
            max_length=2.0
        )
    )
    cabin: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="cabin",
            type="Element",
            min_occurs=1,
            max_occurs=3,
            min_length=0.0,
            max_length=1.0
        )
    )


@dataclass
class CabinIdentificationType233500C:
    """
    :ivar cabin_qualifier: Cabin qualifier. For Star Pricer,MD stands for Mandatory Cabin qualifier. For other products no qualifier stands for Mandatory Cabin.
    :ivar cabin: Cabin
    """
    cabin_qualifier: str = field(
        default=None,
        metadata=dict(
            name="cabinQualifier",
            type="Element",
            min_length=1.0,
            max_length=2.0
        )
    )
    cabin: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="cabin",
            type="Element",
            min_occurs=0,
            max_occurs=5,
            min_length=0.0,
            max_length=1.0
        )
    )


@dataclass
class CabinProductDetailsType:
    """
    :ivar rbd: Reservation booking designator - RBD
    :ivar booking_modifier: Reservation Booking Modifier
    :ivar cabin: Indicates the cabin related to the Booking code
    :ivar avl_status: Availibility status : posting level
    """
    rbd: str = field(
        default=None,
        metadata=dict(
            name="rbd",
            type="Element",
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
            pattern="[0-9A-Z]"
        )
    )
    cabin: str = field(
        default=None,
        metadata=dict(
            name="cabin",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    avl_status: str = field(
        default=None,
        metadata=dict(
            name="avlStatus",
            type="Element",
            pattern="[0-9A-Z]{1,3}"
        )
    )


@dataclass
class CodedAttributeInformationType:
    """Attribute information.

    :ivar attribute_type: Attribute type identification
    :ivar attribute_description: Attribute Description
    """
    attribute_type: str = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
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
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class CodedAttributeInformationType120742C:
    """Convey coded key and corresponding value.

    :ivar name: Name.
    :ivar value: Value.
    """
    name: str = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
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
            min_occurs=0,
            max_occurs=10,
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class CodedAttributeInformationType139508C:
    """Convey coded key and corresponding value.

    :ivar type: Attribute type
    :ivar value: Value.
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=5.0
        )
    )
    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="value",
            type="Element",
            min_occurs=0,
            max_occurs=10,
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class CodedAttributeInformationType247828C:
    """Convey coded key and corresponding value.

    :ivar attribute_type:
    :ivar attribute_description: Attribute description
    """
    attribute_type: str = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
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
            min_length=1.0,
            max_length=10.0
        )
    )


@dataclass
class CodedAttributeInformationType254574C:
    """Convey coded key and corresponding value.

    :ivar attribute_type: Attribute type
    :ivar attribute_description: Attribute description
    """
    attribute_type: str = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
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
            min_length=1.0,
            max_length=50.0
        )
    )


@dataclass
class CodedAttributeInformationType275401C:
    """Convey coded key and corresponding value.

    :ivar fee_type: Type of fee/reduction
    :ivar fee_id_number: Fee Id Number
    """
    fee_type: str = field(
        default=None,
        metadata=dict(
            name="feeType",
            type="Element",
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
            required=True,
            min_length=1.0,
            max_length=50.0
        )
    )


@dataclass
class CompanyIdentificationType120719C:
    """
    :ivar carrier_qualifier: Item description identification.
    :ivar carrier_id: carrier id
    """
    carrier_qualifier: str = field(
        default=None,
        metadata=dict(
            name="carrierQualifier",
            type="Element",
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
            min_occurs=1,
            max_occurs=99,
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class CompanyIdentificationType195544C:
    """
    :ivar marketing_carrier: Marketing carrier
    :ivar operating_carrier: Operating carrier
    """
    marketing_carrier: str = field(
        default=None,
        metadata=dict(
            name="marketingCarrier",
            type="Element",
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
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class CompanyIdentificationType275415C:
    """
    :ivar carrier_qualifier: Item description identification.
    :ivar carrier_id: carrier id
    """
    carrier_qualifier: str = field(
        default=None,
        metadata=dict(
            name="carrierQualifier",
            type="Element",
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
            min_occurs=1,
            max_occurs=999,
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class CompanyIdentificationTypeI:
    """Code or name to identify a company and any associated companies.

    :ivar marketing_company: Carrier code
    """
    marketing_company: str = field(
        default=None,
        metadata=dict(
            name="marketingCompany",
            type="Element",
            required=True,
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class CompanyRoleIdentificationType:
    """To indicate commercial agreements related to the service being provided.

    :ivar transport_stage_qualifier: Codeshare qualifier
    :ivar airline_designator: company identification
    :ivar flight_number: flight number
    :ivar operational_suffix: suffix
    """
    transport_stage_qualifier: str = field(
        default=None,
        metadata=dict(
            name="transportStageQualifier",
            type="Element",
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
            min_length=2.0,
            max_length=3.0
        )
    )
    flight_number: int = field(
        default=None,
        metadata=dict(
            name="flightNumber",
            type="Element",
            pattern="-?[0-9]{1,4}"
        )
    )
    operational_suffix: str = field(
        default=None,
        metadata=dict(
            name="operationalSuffix",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class CompanyRoleIdentificationType120761C:
    """To indicate commercial agreements related to the service being provided.

    :ivar code_share_type: Type of code share agreement.
    :ivar airline_designator: company identification
    :ivar flight_number: flight number
    """
    code_share_type: str = field(
        default=None,
        metadata=dict(
            name="codeShareType",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    airline_designator: str = field(
        default=None,
        metadata=dict(
            name="airlineDesignator",
            type="Element",
            min_length=2.0,
            max_length=3.0
        )
    )
    flight_number: int = field(
        default=None,
        metadata=dict(
            name="flightNumber",
            type="Element",
            pattern="-?[0-9]{1,4}"
        )
    )


@dataclass
class ConnectPointDetailsType:
    """
    :ivar exclusion_identifier: Exclusion identification
    :ivar location_id: Place or Location identification
    :ivar airport_city_qualifier: Airport/city qualifier
    """
    exclusion_identifier: str = field(
        default=None,
        metadata=dict(
            name="exclusionIdentifier",
            type="Element",
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
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class ConnectPointDetailsType195492C:
    """
    :ivar inclusion_identifier: Inclusion identification
    :ivar location_id: Place or Location identification
    :ivar airport_city_qualifier: Airport/city qualifier
    """
    inclusion_identifier: str = field(
        default=None,
        metadata=dict(
            name="inclusionIdentifier",
            type="Element",
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
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class ConnectionDetailsTypeI:
    """To specify the location, product supplier and time for a connection with the
    next means of transport.

    :ivar location: Location
    """
    location: str = field(
        default=None,
        metadata=dict(
            name="location",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ConsumerReferenceIdentificationTypeI:
    """Identification of consumer references by type, company, number and reference
    to a traveller.

    :ivar reference_qualifier:
    :ivar reference_number:
    :ivar reference_party_name:
    :ivar traveller_reference_nbr:
    """
    reference_qualifier: str = field(
        default=None,
        metadata=dict(
            name="referenceQualifier",
            type="Element",
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
            min_length=1.0,
            max_length=35.0
        )
    )
    reference_party_name: str = field(
        default=None,
        metadata=dict(
            name="referencePartyName",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    traveller_reference_nbr: str = field(
        default=None,
        metadata=dict(
            name="travellerReferenceNbr",
            type="Element",
            min_length=1.0,
            max_length=10.0
        )
    )


@dataclass
class ConversionRateDetailsType:
    """
    :ivar conversion_type: Conversion type
    :ivar currency: Currency
    """
    conversion_type: str = field(
        default=None,
        metadata=dict(
            name="conversionType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class CorporateFareIdentifiersType:
    """
    :ivar fare_qualifier: Indicates the type of corporate fares requested
    :ivar identify_number: Corporate contract number or name
    """
    fare_qualifier: str = field(
        default=None,
        metadata=dict(
            name="fareQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    identify_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="identifyNumber",
            type="Element",
            min_occurs=0,
            max_occurs=20,
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class CorporateIdentityType:
    """Corporate fare types indicated in PTK are detailed.

    :ivar corporate_qualifier: Indicates if 1A corporate (RC) or Unifare corporate (RW) requested.
    :ivar identity: Corporate contract number or name
    """
    corporate_qualifier: str = field(
        default=None,
        metadata=dict(
            name="corporateQualifier",
            type="Element",
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
    :ivar type:
    :ivar value:
    :ivar attribute:
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            min_length=1.0,
            max_length=18.0
        )
    )
    attribute: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="attribute",
            type="Element",
            min_occurs=0,
            max_occurs=99,
            min_length=1.0,
            max_length=9.0
        )
    )


@dataclass
class DataInformationType:
    """To identify specific data and a quantity related to the data.

    :ivar indicator: Ancillary services options
    """
    indicator: str = field(
        default=None,
        metadata=dict(
            name="indicator",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class DataTypeInformationType:
    """To identify the type of data to be sent and to qualify the data when
    required.

    :ivar sub_type: Carrier fee code
    :ivar option: Status (automated, manually added, exempted). Default is automated
    """
    sub_type: str = field(
        default=None,
        metadata=dict(
            name="subType",
            type="Element",
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
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class DateAndTimeDetailsType:
    """DATE AND TIME DETAILS.

    :ivar flexibility_qualifier: Trip Duration type(Plus,Minus,Combined)
    :ivar trip_interval: Number of days added or/and retrieved to the trip duration
    :ivar trip_duration: Period between date of departure and date of arrival
    """
    flexibility_qualifier: str = field(
        default=None,
        metadata=dict(
            name="flexibilityQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    trip_interval: int = field(
        default=None,
        metadata=dict(
            name="tripInterval",
            type="Element",
            pattern="-?[0-9]{1,6}"
        )
    )
    trip_duration: int = field(
        default=None,
        metadata=dict(
            name="tripDuration",
            type="Element",
            pattern="-?[0-9]{1,4}"
        )
    )


@dataclass
class DateAndTimeDetailsType120762C:
    """
    :ivar date_qualifier: Date time period qualifier
    :ivar date: First Date
    :ivar first_time: First Time
    :ivar equipement_type: Movement type.
    :ivar location_id: Place/location identification.
    """
    date_qualifier: str = field(
        default=None,
        metadata=dict(
            name="dateQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    first_time: str = field(
        default=None,
        metadata=dict(
            name="firstTime",
            type="Element",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    equipement_type: str = field(
        default=None,
        metadata=dict(
            name="equipementType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class DateAndTimeDetailsType254619C:
    """DATE AND TIME DETAILS.

    :ivar range_qualifier: To identify type of range (Plus,Minus or combined)
    :ivar day_interval: Range of dates : Number of Days preceding or/and Following the request departure date
    :ivar time_atdestination: Time at destination (local)
    """
    range_qualifier: str = field(
        default=None,
        metadata=dict(
            name="rangeQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    day_interval: int = field(
        default=None,
        metadata=dict(
            name="dayInterval",
            type="Element",
            pattern="-?[0-9]{1,6}"
        )
    )
    time_atdestination: str = field(
        default=None,
        metadata=dict(
            name="timeAtdestination",
            type="Element",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )


@dataclass
class DateAndTimeDetailsTypeI:
    """DATE AND TIME DETAILS.

    :ivar time_qualifier: Toidentify type of time Arrival/Departure
    :ivar date: Date
    :ivar time: Time
    :ivar time_window: Time window size in hours
    """
    time_qualifier: str = field(
        default=None,
        metadata=dict(
            name="timeQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time: str = field(
        default=None,
        metadata=dict(
            name="time",
            type="Element",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    time_window: str = field(
        default=None,
        metadata=dict(
            name="timeWindow",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class DateAndTimeDetailsTypeI120740C:
    """
    :ivar qualifier: Date time period qualifier
    :ivar date: First Date
    :ivar time: First Time
    :ivar qualifier2: .
    :ivar reserved1:
    :ivar reserved2:
    """
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time: str = field(
        default=None,
        metadata=dict(
            name="time",
            type="Element",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    qualifier2: str = field(
        default=None,
        metadata=dict(
            name="qualifier2",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    reserved1: str = field(
        default=None,
        metadata=dict(
            name="reserved1",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    reserved2: str = field(
        default=None,
        metadata=dict(
            name="reserved2",
            type="Element",
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class DateTimePeriodDetailsTypeI:
    """To indicate period of applicability.

    :ivar qualifier: Qualifier
    :ivar value: Value
    """
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
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
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class FareDetailsType:
    """
    :ivar qualifier: Qualifier
    :ivar rate: Rate
    :ivar country: Country
    :ivar fare_category: Fare Category
    """
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            pattern="[0-9A-Z]{1,3}"
        )
    )
    rate: int = field(
        default=None,
        metadata=dict(
            name="rate",
            type="Element",
            pattern="-?[0-9]{1,8}"
        )
    )
    country: str = field(
        default=None,
        metadata=dict(
            name="country",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    fare_category: str = field(
        default=None,
        metadata=dict(
            name="fareCategory",
            type="Element",
            pattern="[0-9A-Z]{1,3}"
        )
    )


@dataclass
class FareFamilyDetailsType:
    """NEW FARE SEARCH.

    :ivar commercial_family: Commercial fare Family Short name
    """
    commercial_family: str = field(
        default=None,
        metadata=dict(
            name="commercialFamily",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=10.0
        )
    )


@dataclass
class FareInformationTypeI:
    """To specify fare details.

    :ivar value_qualifier: PTC (Full Codeset List described in ATPCo Documentation B11109 Appendix A)
    :ivar value: age
    """
    value_qualifier: str = field(
        default=None,
        metadata=dict(
            name="valueQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    value: int = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            pattern="-?[0-9]{1,15}"
        )
    )


@dataclass
class FareProductDetailsType:
    """
    :ivar fare_basis: Fare basis code
    :ivar fare_type: Type of fare
    """
    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="fareBasis",
            type="Element",
            min_length=0.0,
            max_length=18.0
        )
    )
    fare_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="fareType",
            type="Element",
            min_occurs=0,
            max_occurs=3,
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class FareQualifierInformationType:
    """To specify multiple qualifier for fare selections.

    :ivar fare_family_qual: Fare family combinability.
    """
    fare_family_qual: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="fareFamilyQual",
            type="Element",
            min_occurs=1,
            max_occurs=9,
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class FareTypeGroupingInformationType:
    """
    :ivar pricing_group: Pricing Group
    """
    pricing_group: str = field(
        default=None,
        metadata=dict(
            name="pricingGroup",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class FormOfPaymentDetailsTypeI:
    """To specify the form of payment type, amounts, approval codes, and other
    related information.

    :ivar type: Form of payment identification
    :ivar charged_amount: amount to be charged on this form
    :ivar credit_card_number: Reference number
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    charged_amount: float = field(
        default=None,
        metadata=dict(
            name="chargedAmount",
            type="Element"
        )
    )
    credit_card_number: str = field(
        default=None,
        metadata=dict(
            name="creditCardNumber",
            type="Element",
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class FreeTextDetailsType:
    """
    :ivar text_subject_qualifier: Qualifier of the free text. Always literal in our usage.
    :ivar information_type: Type of the free text. Always 7 for our usage.
    :ivar source: Source of the information.
    :ivar encoding: Encoding method used.
    """
    text_subject_qualifier: str = field(
        default=None,
        metadata=dict(
            name="textSubjectQualifier",
            type="Element",
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
            min_length=1.0,
            max_length=4.0
        )
    )
    source: str = field(
        default=None,
        metadata=dict(
            name="source",
            type="Element",
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
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class FrequencyType:
    """Give the days of the week involved for a period.

    :ivar qualifier: Indicate if the sequence number represents days of the week or days of the month.
    :ivar value: Used to represent days of the week. 1 is monday and 7 is sunday.
    """
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="value",
            type="Element",
            min_occurs=0,
            max_occurs=7,
            pattern="-?[0-9]{1,1}"
        )
    )


@dataclass
class FrequentTravellerIdentificationType:
    """
    :ivar carrier: Carrier where the FQTV is registered.
    :ivar number:
    :ivar customer_reference: Specifies which traveller in the TIF segment the frequent traveller number applies (same as 9944 in TIF).
    :ivar status: status code: 'OK' if the frequent flyer card has been validated
    :ivar tier_level: To specify a Tier linked to the FQTV
    :ivar priority_code: For example : priority code
    :ivar tier_description: For example : Level description
    :ivar company_code: For example : Company code of alliance
    :ivar customer_value:
    :ivar type: To specify the product/account number qualifier. (e.g. 2=Corporate Frequent Flyer).
    """
    carrier: str = field(
        default=None,
        metadata=dict(
            name="carrier",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            min_length=1.0,
            max_length=28.0
        )
    )
    customer_reference: str = field(
        default=None,
        metadata=dict(
            name="customerReference",
            type="Element",
            min_length=1.0,
            max_length=10.0
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="status",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    tier_level: str = field(
        default=None,
        metadata=dict(
            name="tierLevel",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    priority_code: str = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            min_length=1.0,
            max_length=12.0
        )
    )
    tier_description: str = field(
        default=None,
        metadata=dict(
            name="tierDescription",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    company_code: str = field(
        default=None,
        metadata=dict(
            name="companyCode",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    customer_value: int = field(
        default=None,
        metadata=dict(
            name="customerValue",
            type="Element",
            pattern="-?[0-9]{1,4}"
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class FrequentTravellerIdentificationType249074C:
    """Identification of the frequent traveller number by company code with the
    capability to reference a specific traveller.

    :ivar carrier: carrier
    :ivar number: Frequent traveller number
    :ivar customer_reference: Customer reference
    :ivar tier_level: Tier level
    :ivar priority_code: Priority code
    :ivar tier_description: Tier description
    :ivar type: To specify the product/account number qualifier. (e.g. 2=Corporate Frequent Flyer).
    """
    carrier: str = field(
        default=None,
        metadata=dict(
            name="carrier",
            type="Element",
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
            min_length=1.0,
            max_length=25.0
        )
    )
    customer_reference: str = field(
        default=None,
        metadata=dict(
            name="customerReference",
            type="Element",
            min_length=1.0,
            max_length=10.0
        )
    )
    tier_level: str = field(
        default=None,
        metadata=dict(
            name="tierLevel",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    priority_code: str = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            min_length=1.0,
            max_length=12.0
        )
    )
    tier_description: str = field(
        default=None,
        metadata=dict(
            name="tierDescription",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ItemNumberIdentificationType:
    """Goods identification for a specified source.

    :ivar number: Fare family combination number
    :ivar type: Type
    :ivar qualifier: Qualifier
    :ivar responsible_agency: Responsible agency
    """
    number: str = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            min_length=1.0,
            max_length=4.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    responsible_agency: str = field(
        default=None,
        metadata=dict(
            name="responsibleAgency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ItineraryDetailsType:
    """Forces arrival or departure to/from the same city or airport option.

    :ivar airport_city_qualifier: Airport/City Qualifier: the passenger wants to depart/arrive from/to the same airport or city in the specified requested segment
    :ivar segment_number: Requested segment number
    """
    airport_city_qualifier: str = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=1.0
        )
    )
    segment_number: int = field(
        default=None,
        metadata=dict(
            name="segmentNumber",
            type="Element",
            required=True,
            pattern="-?[0-9]{1,3}"
        )
    )


@dataclass
class LocationDetailsTypeI:
    """
    :ivar location_id: Place or Location identification
    :ivar country: Country, coded
    """
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
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
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class LocationIdentificationDetailsType:
    """
    :ivar location_id: 3 characters ATA/IATA airport/city code
    :ivar airport_city_qualifier: Airport/city qualifier: the requested point is an airport when ambiguity exists (e.g. HOU)
    :ivar terminal: Terminal information
    """
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
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
            min_length=1.0,
            max_length=1.0
        )
    )
    terminal: str = field(
        default=None,
        metadata=dict(
            name="terminal",
            type="Element",
            min_length=1.0,
            max_length=5.0
        )
    )


@dataclass
class LocationTypeI:
    """To identify a location by code or name.

    :ivar true_location_id: Departure or Arrival IATA airport code
    """
    true_location_id: str = field(
        default=None,
        metadata=dict(
            name="trueLocationId",
            type="Element",
            required=True,
            min_length=3.0,
            max_length=3.0
        )
    )


@dataclass
class MileageTimeDetailsTypeI:
    """Information about the distance/duration of a trip.

    :ivar elapsed_ground_time: Ground Time in minutes at Board point (connection with incoming flight)
    """
    elapsed_ground_time: int = field(
        default=None,
        metadata=dict(
            name="elapsedGroundTime",
            type="Element",
            pattern="-?[0-9]{1,4}"
        )
    )


@dataclass
class MonetaryAndCabinInformationDetailsType:
    """
    :ivar amount_type: Amount qualifier.
    :ivar amount: Amount
    :ivar currency: ISO currency code
    :ivar location_id: Airport/city code
    :ivar cabin_class_designator: Cabin class designator
    """
    amount_type: str = field(
        default=None,
        metadata=dict(
            name="amountType",
            type="Element",
            min_length=0.0,
            max_length=3.0
        )
    )
    amount: float = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            required=True
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            min_length=3.0,
            max_length=5.0
        )
    )
    cabin_class_designator: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="cabinClassDesignator",
            type="Element",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class MonetaryInformationDetailsTypeI:
    """
    :ivar qualifier: Monetary amount type qualifier, coded
    :ivar amount: Allowance or charge number
    :ivar currency: Currency, coded
    """
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    amount: int = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            required=True,
            pattern="-?[0-9]{1,18}"
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class MonetaryInformationDetailsTypeI194597C:
    """
    :ivar qualifier: Monetary amount type qualifier, coded
    :ivar amount: Allowance or charge number
    :ivar currency: Currency, coded
    :ivar location_id: Place or Location identification
    """
    qualifier: str = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    amount: int = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            required=True,
            pattern="-?[0-9]{1,18}"
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            min_length=3.0,
            max_length=3.0
        )
    )


@dataclass
class MonetaryInformationDetailsTypeI65140C:
    """To specify the type of monetary amount, the amount, and the currency code.

    :ivar type_qualifier: Qualifier
    :ivar amount: Amount
    :ivar currency: Currency
    """
    type_qualifier: str = field(
        default=None,
        metadata=dict(
            name="typeQualifier",
            type="Element",
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
            min_length=1.0,
            max_length=12.0
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class MonetaryInformationDetailsTypeI65141C:
    """To specify the type of monetary amount, the amount, and the currency code.

    :ivar type_qualifier: Qualifier
    :ivar amount: Amount
    :ivar currency: Currency
    :ivar location: Location
    """
    type_qualifier: str = field(
        default=None,
        metadata=dict(
            name="typeQualifier",
            type="Element",
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
            min_length=1.0,
            max_length=12.0
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    location: str = field(
        default=None,
        metadata=dict(
            name="location",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class MultiCityOptionType:
    """List of requested arrival points.

    :ivar location_id: ATA/IATA airport/city code of arrival multi city option enable to define until 20 airports/cities
    :ivar airport_city_qualifier: Requested arrival point is an airport or a city (default is city and used only when ambiguity)
    """
    location_id: str = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
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
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class MultipleIdentificationNumbersTypeI:
    """To specify more than one identification number.

    :ivar corporate_number_identifier: Corporate number or ALL.
    :ivar corporate_name: Corporate name.
    """
    corporate_number_identifier: str = field(
        default=None,
        metadata=dict(
            name="corporateNumberIdentifier",
            type="Element",
            min_length=1.0,
            max_length=12.0
        )
    )
    corporate_name: str = field(
        default=None,
        metadata=dict(
            name="corporateName",
            type="Element",
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class NumberOfUnitDetailsType:
    """
    :ivar number_of_units: Number of Units
    :ivar type_of_unit: Number of unit qualifier
    """
    number_of_units: int = field(
        default=None,
        metadata=dict(
            name="numberOfUnits",
            type="Element",
            pattern="-?[0-9]{1,4}"
        )
    )
    type_of_unit: str = field(
        default=None,
        metadata=dict(
            name="typeOfUnit",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class NumberOfUnitDetailsType270113C:
    """
    :ivar number_of_units: Number of Units
    :ivar type_of_unit: Number of unit qualifier
    """
    number_of_units: int = field(
        default=None,
        metadata=dict(
            name="numberOfUnits",
            type="Element",
            required=True,
            pattern="-?[0-9]{1,6}"
        )
    )
    type_of_unit: str = field(
        default=None,
        metadata=dict(
            name="typeOfUnit",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class NumberOfUnitDetailsTypeI:
    """
    :ivar number_of_units: Number of Units
    :ivar type_of_unit: Number of unit qualifier
    """
    number_of_units: int = field(
        default=None,
        metadata=dict(
            name="numberOfUnits",
            type="Element",
            required=True,
            pattern="-?[0-9]{1,3}"
        )
    )
    type_of_unit: str = field(
        default=None,
        metadata=dict(
            name="typeOfUnit",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class OriginatorIdentificationDetailsTypeI:
    """To identify a user.

    :ivar office_name: Office Name.
    :ivar agent_signin: Agent Sign In .
    :ivar confidential_office: Confidential Office Name.
    :ivar other_office: Other Office Name
    """
    office_name: int = field(
        default=None,
        metadata=dict(
            name="officeName",
            type="Element",
            pattern="-?[0-9]{1,9}"
        )
    )
    agent_signin: str = field(
        default=None,
        metadata=dict(
            name="agentSignin",
            type="Element",
            min_length=1.0,
            max_length=9.0
        )
    )
    confidential_office: str = field(
        default=None,
        metadata=dict(
            name="confidentialOffice",
            type="Element",
            min_length=1.0,
            max_length=9.0
        )
    )
    other_office: str = field(
        default=None,
        metadata=dict(
            name="otherOffice",
            type="Element",
            min_length=1.0,
            max_length=9.0
        )
    )


@dataclass
class PnrsegmentReferenceType:
    """Reference to PNR segment.

    :ivar pnr_segment_tattoo: For a request from PNR: this is the reference number of a PNR air segment. In case a range of PNR segments is specified (eg. segments 2-5), then it is the 1st of the range, the last being in ARR.
    :ivar pnr_segment_qualifier:
    """
    pnr_segment_tattoo: int = field(
        default=None,
        metadata=dict(
            name="pnrSegmentTattoo",
            type="Element",
            pattern="-?[0-9]{0,35}"
        )
    )
    pnr_segment_qualifier: str = field(
        default=None,
        metadata=dict(
            name="pnrSegmentQualifier",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class PricingTicketingInformationType:
    """To specify indicators related to pricing and ticketing.

    :ivar price_type: Price type qualifier
    """
    price_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="priceType",
            type="Element",
            min_occurs=1,
            max_occurs=50,
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class ProductDateTimeType:
    """Product date or time.

    :ivar date: .
    :ivar time: .
    """
    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            required=True,
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time: str = field(
        default=None,
        metadata=dict(
            name="time",
            type="Element",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )


@dataclass
class ProductDateTimeType195546C:
    """
    :ivar date_of_departure: Departure date
    :ivar time_of_departure: Departure time
    :ivar date_of_arrival: Arrival date
    :ivar time_of_arrival: Arrival time
    :ivar date_variation: Arrival date compared to departure date, only if different from 0
    """
    date_of_departure: str = field(
        default=None,
        metadata=dict(
            name="dateOfDeparture",
            type="Element",
            required=True,
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time_of_departure: str = field(
        default=None,
        metadata=dict(
            name="timeOfDeparture",
            type="Element",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    date_of_arrival: str = field(
        default=None,
        metadata=dict(
            name="dateOfArrival",
            type="Element",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time_of_arrival: str = field(
        default=None,
        metadata=dict(
            name="timeOfArrival",
            type="Element",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    date_variation: int = field(
        default=None,
        metadata=dict(
            name="dateVariation",
            type="Element",
            pattern="-?[0-9]{1,1}"
        )
    )


@dataclass
class ProductDateTimeTypeI:
    """To specify the dates and times associated with a product.

    :ivar departure_date: Departure date in YYYYMMDD format
    :ivar departure_time: Departure time
    :ivar arrival_date: Arrival date
    :ivar arrival_time: Arrival time
    :ivar date_variation: Day difference between Departure date of the leg and date of reference (Departure or Arrival date specified in the SDI)
    """
    departure_date: str = field(
        default=None,
        metadata=dict(
            name="departureDate",
            type="Element",
            pattern="[0-9]{4}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])"
        )
    )
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="departureTime",
            type="Element",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    arrival_date: str = field(
        default=None,
        metadata=dict(
            name="arrivalDate",
            type="Element",
            pattern="[0-9]{4}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])"
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="arrivalTime",
            type="Element",
            pattern="([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    date_variation: int = field(
        default=None,
        metadata=dict(
            name="dateVariation",
            type="Element",
            pattern="-?[0-9]{1,1}"
        )
    )


@dataclass
class ProductDateTimeTypeI194583C:
    """To specify the dates and times associated with a product.

    :ivar date: Ticketing Purchase Date
    :ivar other_date: Ticketing purchase date
    """
    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            required=True,
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    other_date: str = field(
        default=None,
        metadata=dict(
            name="otherDate",
            type="Element",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )


@dataclass
class ProductDateTimeTypeI194598C:
    """
    :ivar date: First date
    :ivar rtc_date: Half round trip combination.
    """
    date: str = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            required=True,
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    rtc_date: str = field(
        default=None,
        metadata=dict(
            name="rtcDate",
            type="Element",
            pattern="(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )


@dataclass
class ProductFacilitiesType:
    """Level of access.

    :ivar last_seat_available: Yes-No indicator whether Last Seat Available
    :ivar level_of_access: Level of access
    :ivar electronic_ticketing: Yes-No indicator whether electronic ticketing
    :ivar operational_suffix: Product identification suffix
    :ivar product_detail_qualifier: Define whether a flight has been polled or not
    :ivar flight_characteristic: Add some flight restrictions (See code set list)
    """
    last_seat_available: str = field(
        default=None,
        metadata=dict(
            name="lastSeatAvailable",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    level_of_access: str = field(
        default=None,
        metadata=dict(
            name="levelOfAccess",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    electronic_ticketing: str = field(
        default=None,
        metadata=dict(
            name="electronicTicketing",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    operational_suffix: str = field(
        default=None,
        metadata=dict(
            name="operationalSuffix",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    product_detail_qualifier: str = field(
        default=None,
        metadata=dict(
            name="productDetailQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    flight_characteristic: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="flightCharacteristic",
            type="Element",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ProductIdentificationDetailsTypeI:
    """Code, number or name to identify a specific product or service.

    :ivar flight_number: Flight number
    :ivar operational_suffix: Flight suffix
    """
    flight_number: int = field(
        default=None,
        metadata=dict(
            name="flightNumber",
            type="Element",
            required=True,
            pattern="-?[0-9]{1,4}"
        )
    )
    operational_suffix: str = field(
        default=None,
        metadata=dict(
            name="operationalSuffix",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class ProductIdentificationDetailsTypeI50878C:
    """Code, number or name to identify a specific product or service.

    :ivar flight_number:
    :ivar booking_class:
    :ivar operational_suffix:
    :ivar modifier:
    """
    flight_number: str = field(
        default=None,
        metadata=dict(
            name="flightNumber",
            type="Element",
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
            min_length=1.0,
            max_length=2.0
        )
    )
    operational_suffix: str = field(
        default=None,
        metadata=dict(
            name="operationalSuffix",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    modifier: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="modifier",
            type="Element",
            min_occurs=0,
            max_occurs=3,
            min_length=1.0,
            max_length=7.0
        )
    )


@dataclass
class ProductLocationDetailsTypeI:
    """To indicate a location and the type of location.

    :ivar station: airport
    """
    station: str = field(
        default=None,
        metadata=dict(
            name="station",
            type="Element",
            min_length=3.0,
            max_length=3.0
        )
    )


@dataclass
class ProductTypeDetailsType:
    """Product type details.

    :ivar sequence_number: .
    :ivar availability_context: PNR availability context
    """
    sequence_number: str = field(
        default=None,
        metadata=dict(
            name="sequenceNumber",
            type="Element",
            min_length=1.0,
            max_length=6.0
        )
    )
    availability_context: str = field(
        default=None,
        metadata=dict(
            name="availabilityContext",
            type="Element",
            min_length=1.0,
            max_length=6.0
        )
    )


@dataclass
class ProductTypeDetailsType120801C:
    """
    :ivar flight_type: Type of flight
    """
    flight_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="flightType",
            type="Element",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=2.0
        )
    )


@dataclass
class ProductTypeDetailsType205137C:
    """To specify additional characteristics of a product or service.

    :ivar avl: indicates whether the flight is domestic or international
    """
    avl: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="avl",
            type="Element",
            min_occurs=1,
            max_occurs=9,
            min_length=1.0,
            max_length=6.0
        )
    )


@dataclass
class ProductTypeDetailsTypeI:
    """To specify additional characteristics of a product or service.

    :ivar flight_indicator: Part of the journey (C,E,S), Codeshare service (A), Technical stop at off point in a Direct (TSD), Technical stop at off point in a COG (TSC), E-Ticket candidate (ET), Prohibited Countries (RPC, WPC)
    """
    flight_indicator: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="flightIndicator",
            type="Element",
            min_occurs=1,
            max_occurs=5,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ProposedSegmentDetailsType:
    """
    :ivar ref: Flight proposal reference
    :ivar unit_qualifier: Elapse Flying Time
    """
    ref: str = field(
        default=None,
        metadata=dict(
            name="ref",
            type="Element",
            min_length=1.0,
            max_length=6.0
        )
    )
    unit_qualifier: str = field(
        default=None,
        metadata=dict(
            name="unitQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ReferencingDetailsType:
    """Referencing details.

    :ivar ref_qualifier: Segment reference qualifier
    :ivar ref_number: Flight or flight group reference
    """
    ref_qualifier: str = field(
        default=None,
        metadata=dict(
            name="refQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    ref_number: int = field(
        default=None,
        metadata=dict(
            name="refNumber",
            type="Element",
            required=True,
            pattern="-?[0-9]{0,3}"
        )
    )


@dataclass
class SegmentRepetitionControlDetailsTypeI:
    """Information about the number of selection segments to be processed.

    :ivar quantity: traveller number
    """
    quantity: int = field(
        default=None,
        metadata=dict(
            name="quantity",
            type="Element",
            pattern="-?[0-9]{1,15}"
        )
    )


@dataclass
class SelectionDetailsInformationType:
    """To specify a selected option and associated information.

    :ivar type: Carrier fee type
    :ivar option_information: Carrier fee status
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
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
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class SelectionDetailsInformationTypeI:
    """To specify a selected option and associated information.

    :ivar option:
    :ivar option_information:
    """
    option: str = field(
        default=None,
        metadata=dict(
            name="option",
            type="Element",
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
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class SpecialRequirementsDataDetailsType:
    """Special requirements data details.

    :ivar seat_characteristics: SSR seat characteristic
    :ivar dummy_net:
    """
    seat_characteristics: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="seatCharacteristics",
            type="Element",
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
            type="Element"
        )
    )


@dataclass
class SpecialRequirementsTypeDetailsType:
    """
    :ivar service_classification: To specify the Service Classification of the Service Requirement.
    :ivar service_status: Status
    :ivar service_number_of_instances: To specify the number of items involved
    :ivar service_marketing_carrier: To specify to which marketing carrier the service applies
    :ivar service_group: Specify the Service group
    :ivar service_sub_group: Specify the Service Sub-Group
    :ivar service_free_text: Free Text attached to the Service.
    """
    service_classification: str = field(
        default=None,
        metadata=dict(
            name="serviceClassification",
            type="Element",
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
            min_length=1.0,
            max_length=3.0
        )
    )
    service_number_of_instances: int = field(
        default=None,
        metadata=dict(
            name="serviceNumberOfInstances",
            type="Element",
            pattern="-?[0-9]{1,15}"
        )
    )
    service_marketing_carrier: str = field(
        default=None,
        metadata=dict(
            name="serviceMarketingCarrier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_group: str = field(
        default=None,
        metadata=dict(
            name="serviceGroup",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_sub_group: str = field(
        default=None,
        metadata=dict(
            name="serviceSubGroup",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_free_text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="serviceFreeText",
            type="Element",
            min_occurs=0,
            max_occurs=99,
            min_length=1.0,
            max_length=70.0
        )
    )


@dataclass
class StationInformationTypeI:
    """To specify departure/arrival information concerning a means of transport.

    :ivar terminal: Departure terminal
    """
    terminal: str = field(
        default=None,
        metadata=dict(
            name="terminal",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class StructuredDateTimeType:
    """Store date and time in a structured way.

    :ivar year: Year number. The format is a little long for short term usage but it can be reduced by implementation if required.
    :ivar month: Month number in the year ( begins to 1 )
    :ivar day: Day number in the month ( begins to 1 )
    """
    year: int = field(
        default=None,
        metadata=dict(
            name="year",
            type="Element",
            pattern="-?[0-9]{4,4}"
        )
    )
    month: int = field(
        default=None,
        metadata=dict(
            name="month",
            type="Element",
            pattern="-?[0-9]{1,2}"
        )
    )
    day: int = field(
        default=None,
        metadata=dict(
            name="day",
            type="Element",
            pattern="-?[0-9]{1,2}"
        )
    )


@dataclass
class TaxDetailsTypeI:
    """
    :ivar rate: Duty/tax/fee rate
    :ivar country: Country, coded
    :ivar currency: Currency, coded
    :ivar type: Duty/Tax fee type, coded
    :ivar amount_qualifier: Amount type qualifier, coded
    """
    rate: str = field(
        default=None,
        metadata=dict(
            name="rate",
            type="Element",
            min_length=1.0,
            max_length=18.0
        )
    )
    country: str = field(
        default=None,
        metadata=dict(
            name="country",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    amount_qualifier: str = field(
        default=None,
        metadata=dict(
            name="amountQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class TicketNumberDetailsTypeI:
    """To specify a ticket number, type of ticket, and related information.

    :ivar number:
    """
    number: str = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class TicketingPriceSchemeType:
    """Price Scheme Information.

    :ivar reference_number: PSR (Price Scheme Reference): unique reference of the price scheme as a 8 digit number.
    :ivar name: Price Scheme Name
    :ivar status: Price Scheme Status. Is the price scheme valid for service fee calculation ?
    :ivar description: free flow description of the price scheme
    """
    reference_number: str = field(
        default=None,
        metadata=dict(
            name="referenceNumber",
            type="Element",
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
            min_length=1.0,
            max_length=35.0
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="status",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            min_length=1.0,
            max_length=250.0
        )
    )


@dataclass
class TrafficRestrictionDetailsTypeI:
    """Coded or free text details which restrict a means of transport.

    :ivar code: Traffic Restriction code
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="code",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class TravellerDetailsType:
    """
    :ivar ref: Direct reference of passenger assigned by requesting system.
    :ivar infant_indicator: Traveller is an infant
    """
    ref: int = field(
        default=None,
        metadata=dict(
            name="ref",
            type="Element",
            required=True,
            pattern="-?[0-9]{1,3}"
        )
    )
    infant_indicator: int = field(
        default=None,
        metadata=dict(
            name="infantIndicator",
            type="Element",
            pattern="-?[0-9]{1,1}"
        )
    )


@dataclass
class UniqueIdDescriptionType:
    """
    :ivar passenger_fee_ref_qualif: Reference qualifier.
    """
    passenger_fee_ref_qualif: str = field(
        default=None,
        metadata=dict(
            name="passengerFeeRefQualif",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ActionIdentificationType:
    """To provide details of action required or taken, the flights to which this
    action refers, and reasons for action taken.

    :ivar action_request_code: Action request code
    :ivar product_details:
    """
    action_request_code: str = field(
        default=None,
        metadata=dict(
            name="actionRequestCode",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    product_details: ProductIdentificationDetailsTypeI50878C = field(
        default=None,
        metadata=dict(
            name="productDetails",
            type="Element"
        )
    )


@dataclass
class AdditionalProductDetailsTypeI:
    """To convey additional information concerning an airline flight.

    :ivar leg_details: Flight details
    :ivar departure_station_info: Departure station
    :ivar arrival_station_info:
    :ivar mileage_time_details: Ground Time Details when connection
    """
    leg_details: AdditionalProductTypeI = field(
        default=None,
        metadata=dict(
            name="legDetails",
            type="Element"
        )
    )
    departure_station_info: StationInformationTypeI = field(
        default=None,
        metadata=dict(
            name="departureStationInfo",
            type="Element"
        )
    )
    arrival_station_info: StationInformationTypeI = field(
        default=None,
        metadata=dict(
            name="arrivalStationInfo",
            type="Element"
        )
    )
    mileage_time_details: MileageTimeDetailsTypeI = field(
        default=None,
        metadata=dict(
            name="mileageTimeDetails",
            type="Element"
        )
    )


@dataclass
class ArrivalLocalizationType:
    """To convey information of the requested arrival location.

    :ivar arrival_point_details: Details on the location of the arrival point
    :ivar arrival_multi_city: Arrival multi city option
    :ivar attribute_details: Attribute details
    """
    arrival_point_details: ArrivalLocationDetailsType = field(
        default=None,
        metadata=dict(
            name="arrivalPointDetails",
            type="Element"
        )
    )
    arrival_multi_city: List[MultiCityOptionType] = field(
        default_factory=list,
        metadata=dict(
            name="arrivalMultiCity",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    attribute_details: List[CodedAttributeInformationType139508C] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class AttributeType:
    """Used to have tag value without code list for tag.

    :ivar selection_details: Option parameters
    """
    selection_details: List[AttributeInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="selectionDetails",
            type="Element",
            min_occurs=1,
            max_occurs=10
        )
    )


@dataclass
class AttributeType61377S:
    """Used to have tag value without code list for tag.

    :ivar attribute_qualifier: Criteria Set Type
    :ivar attribute_details: Criteria details
    """
    attribute_qualifier: str = field(
        default=None,
        metadata=dict(
            name="attributeQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    attribute_details: List[AttributeInformationType97181C] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class BooleanExpressionRuleType:
    """To perform boolean operations.

    :ivar boolean_expression: Boolean expression associated to the decision rule.
    """
    boolean_expression: ArithmeticEvaluationType = field(
        default=None,
        metadata=dict(
            name="booleanExpression",
            type="Element",
            required=True
        )
    )


@dataclass
class BucketDetailsType:
    """
    :ivar code: Code
    :ivar type: Option or distribution
    :ivar attribute: Attribute
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="code",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    attribute: List[AttributeDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="attribute",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class CodedAttributeType:
    """Used to have tag value without code list for tag.

    :ivar attribute_details: Attribute details
    """
    attribute_details: List[CodedAttributeInformationType254574C] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            min_occurs=1,
            max_occurs=9
        )
    )


@dataclass
class CodedAttributeType197696S:
    """Used to have tag value without code list for tag.

    :ivar fee_id: Fee/reduction Id
    """
    fee_id: List[CodedAttributeInformationType275401C] = field(
        default_factory=list,
        metadata=dict(
            name="feeId",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class CodedAttributeType78500S:
    """Used to have tag value without code list for tag.

    :ivar attribute_details: Atrribute details.
    """
    attribute_details: List[CodedAttributeInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class CommercialAgreementsType:
    """To specify commercial agreements between two or more companies related to
    joint, shared, lease operations etc.

    :ivar codeshare_details: Codeshare Details
    :ivar other_codeshare_details: Other codeshare details
    """
    codeshare_details: CompanyRoleIdentificationType = field(
        default=None,
        metadata=dict(
            name="codeshareDetails",
            type="Element",
            required=True
        )
    )
    other_codeshare_details: List[CompanyRoleIdentificationType] = field(
        default_factory=list,
        metadata=dict(
            name="otherCodeshareDetails",
            type="Element",
            min_occurs=0,
            max_occurs=8
        )
    )


@dataclass
class CommercialAgreementsType78540S:
    """To specify commercial agreements between two or more companies related to
    joint, shared, lease operations etc.

    :ivar codeshare_details: Codeshare Details
    :ivar other_codeshare_details: Other codeshare details
    """
    codeshare_details: CompanyRoleIdentificationType120761C = field(
        default=None,
        metadata=dict(
            name="codeshareDetails",
            type="Element"
        )
    )
    other_codeshare_details: List[CompanyRoleIdentificationType120761C] = field(
        default_factory=list,
        metadata=dict(
            name="otherCodeshareDetails",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class ConnectionTypeI:
    """To specify connection city and airline designator.

    :ivar connection_details: Connection details.
    """
    connection_details: List[ConnectionDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="connectionDetails",
            type="Element",
            min_occurs=1,
            max_occurs=17
        )
    )


@dataclass
class ConsumerReferenceInformationType:
    """To specify consumer reference information.

    :ivar customer_references: Customer references
    """
    customer_references: List[ConsumerReferenceIdentificationTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="customerReferences",
            type="Element",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class ConversionRateType:
    """To specify conversion rate details.

    :ivar conversion_rate_detail: Detail of conversion rate of First Monetary Unit
    """
    conversion_rate_detail: List[ConversionRateDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="conversionRateDetail",
            type="Element",
            min_occurs=1,
            max_occurs=2
        )
    )


@dataclass
class CorporateFareInformationType:
    """To specify corporate fare information.

    :ivar corporate_fare_identifiers: Corporate fare identifiers
    """
    corporate_fare_identifiers: CorporateFareIdentifiersType = field(
        default=None,
        metadata=dict(
            name="corporateFareIdentifiers",
            type="Element"
        )
    )


@dataclass
class CorporateIdentificationType:
    """To specify corporate number(s) or name(s)

    :ivar corporate_id: Corporate identity
    """
    corporate_id: List[CorporateIdentityType] = field(
        default_factory=list,
        metadata=dict(
            name="corporateId",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class DateAndTimeInformationType:
    """not the standard only used in fare quote message.

    :ivar stop_details: Details on date and time
    :ivar dummy_net:
    """
    stop_details: List[DateAndTimeDetailsType120762C] = field(
        default_factory=list,
        metadata=dict(
            name="stopDetails",
            type="Element",
            min_occurs=1,
            max_occurs=2
        )
    )
    dummy_net: str = field(
        default=None,
        metadata=dict(
            name="Dummy.NET",
            type="Element"
        )
    )


@dataclass
class DateAndTimeInformationType181295S:
    """Target estimated or actual dates and times.

    :ivar first_date_time_detail: Details on date and Time
    :ivar range_of_date: Details of the Requested Range of Dates
    :ivar trip_details: Details of the trip duration
    """
    first_date_time_detail: DateAndTimeDetailsTypeI = field(
        default=None,
        metadata=dict(
            name="firstDateTimeDetail",
            type="Element",
            required=True
        )
    )
    range_of_date: DateAndTimeDetailsType254619C = field(
        default=None,
        metadata=dict(
            name="rangeOfDate",
            type="Element"
        )
    )
    trip_details: DateAndTimeDetailsType = field(
        default=None,
        metadata=dict(
            name="tripDetails",
            type="Element"
        )
    )


@dataclass
class DateAndTimeInformationTypeI:
    """To convey information regarding estimated or actual dates and times of
    operational events.

    :ivar date_time_details: DATE AND TIME DETAILS.
    """
    date_time_details: List[DateAndTimeDetailsTypeI120740C] = field(
        default_factory=list,
        metadata=dict(
            name="dateTimeDetails",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )


@dataclass
class DepartureLocationType:
    """To convey information of requested departure.

    :ivar departure_point: Details on localization of the departure point
    :ivar dep_multi_city: Departure multi city option
    :ivar first_pnr_segment_ref: To specify a series or a range of PNR segments
    :ivar attribute_details: Attribute details
    """
    departure_point: ArrivalLocationDetailsType120834C = field(
        default=None,
        metadata=dict(
            name="departurePoint",
            type="Element"
        )
    )
    dep_multi_city: List[MultiCityOptionType] = field(
        default_factory=list,
        metadata=dict(
            name="depMultiCity",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    first_pnr_segment_ref: PnrsegmentReferenceType = field(
        default=None,
        metadata=dict(
            name="firstPnrSegmentRef",
            type="Element"
        )
    )
    attribute_details: List[CodedAttributeInformationType139508C] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class FareFamilyCriteriaType:
    """Fare family criteria.

    :ivar carrier_id: Fare publishing carrier.
    :ivar rdb: Reservation booking designator.
    :ivar fare_family_info: Fare family info.
    :ivar fare_product_detail: Fare product detail.
    :ivar corporate_info: Corporate information.
    :ivar cabin_product: Indicates flight cabin details.
    :ivar cabin_processing_identifier: Cabin processing option.
    :ivar date_time_details: Product date or time.
    :ivar other_criteria: Other criteria.
    """
    carrier_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="carrierId",
            type="Element",
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
            min_occurs=0,
            max_occurs=20,
            min_length=1.0,
            max_length=2.0
        )
    )
    fare_family_info: FareQualifierInformationType = field(
        default=None,
        metadata=dict(
            name="fareFamilyInfo",
            type="Element"
        )
    )
    fare_product_detail: List[FareProductDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="fareProductDetail",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    corporate_info: List[MultipleIdentificationNumbersTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="corporateInfo",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    cabin_product: List[CabinClassDesignationType] = field(
        default_factory=list,
        metadata=dict(
            name="cabinProduct",
            type="Element",
            min_occurs=0,
            max_occurs=6
        )
    )
    cabin_processing_identifier: str = field(
        default=None,
        metadata=dict(
            name="cabinProcessingIdentifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    date_time_details: List[ProductDateTimeTypeI194583C] = field(
        default_factory=list,
        metadata=dict(
            name="dateTimeDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    other_criteria: List[CodedAttributeInformationType120742C] = field(
        default_factory=list,
        metadata=dict(
            name="otherCriteria",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class FareFamilyType:
    """NEW FARE SEACH.

    :ivar commercial_family_details: Indicates Commercial Fare Family Short names
    """
    commercial_family_details: List[FareFamilyDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="commercialFamilyDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class FareFamilyType80157S:
    """NEW FARE SEACH.

    :ivar ref_number: Fare Family Reference Number
    :ivar fare_familyname: Fare Family Short Name
    :ivar hierarchy: HIERARCHICAL ORDER WITHIN FARE FAMILY
    :ivar commercial_family_details: Indicates Commercial Fare Family Short names
    """
    ref_number: int = field(
        default=None,
        metadata=dict(
            name="refNumber",
            type="Element",
            pattern="-?[0-9]{1,3}"
        )
    )
    fare_familyname: str = field(
        default=None,
        metadata=dict(
            name="fareFamilyname",
            type="Element",
            min_length=1.0,
            max_length=10.0
        )
    )
    hierarchy: int = field(
        default=None,
        metadata=dict(
            name="hierarchy",
            type="Element",
            pattern="-?[0-9]{1,4}"
        )
    )
    commercial_family_details: List[FareFamilyDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="commercialFamilyDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class FareInformationType:
    """
    :ivar value_qualifier: Value Qualifier
    :ivar value: Value
    :ivar fare_details: Fare Details
    :ivar identity_number: Identity Number
    :ivar fare_type_grouping: Fare Type Grouping
    :ivar rate_category: Rate Category
    """
    value_qualifier: str = field(
        default=None,
        metadata=dict(
            name="valueQualifier",
            type="Element",
            pattern="[0-9A-Z]{1,3}"
        )
    )
    value: int = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            pattern="-?[0-9]{1,15}"
        )
    )
    fare_details: FareDetailsType = field(
        default=None,
        metadata=dict(
            name="fareDetails",
            type="Element"
        )
    )
    identity_number: str = field(
        default=None,
        metadata=dict(
            name="identityNumber",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    fare_type_grouping: FareTypeGroupingInformationType = field(
        default=None,
        metadata=dict(
            name="fareTypeGrouping",
            type="Element"
        )
    )
    rate_category: str = field(
        default=None,
        metadata=dict(
            name="rateCategory",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class FlightProductInformationType:
    """To specify flight product information details.

    :ivar cabin_product: Indicates flight cabin details
    :ivar context_details: To specify additional characteristics.
    """
    cabin_product: List[CabinProductDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="cabinProduct",
            type="Element",
            min_occurs=0,
            max_occurs=26
        )
    )
    context_details: ProductTypeDetailsType205137C = field(
        default=None,
        metadata=dict(
            name="contextDetails",
            type="Element"
        )
    )


@dataclass
class FormOfPaymentTypeI:
    """To convey details describing the form of payment.

    :ivar form_of_payment_details: FORM OF PAYMENT DETAILS
    """
    form_of_payment_details: List[FormOfPaymentDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="formOfPaymentDetails",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class FreeTextInformationType:
    """This segment is used to convey the free text.

    :ivar free_text_details: Details for the free text message
    :ivar free_text: Free text corresponding to the DEI 127 data.
    """
    free_text_details: FreeTextDetailsType = field(
        default=None,
        metadata=dict(
            name="freeTextDetails",
            type="Element",
            required=True
        )
    )
    free_text: str = field(
        default=None,
        metadata=dict(
            name="freeText",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=70.0
        )
    )


@dataclass
class FrequentTravellerIdentificationCodeType:
    """To specify frequent traveler information.

    :ivar frequent_traveller_details: Frequent Traveller Info
    """
    frequent_traveller_details: List[FrequentTravellerIdentificationType] = field(
        default_factory=list,
        metadata=dict(
            name="frequentTravellerDetails",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class FrequentTravellerIdentificationCodeType177150S:
    """To specify frequent traveler information.

    :ivar frequent_traveller_details: Frequent traveller details
    """
    frequent_traveller_details: List[FrequentTravellerIdentificationType249074C] = field(
        default_factory=list,
        metadata=dict(
            name="frequentTravellerDetails",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class HeaderInformationTypeI:
    """To specify header information applicable to the entire message.

    :ivar status: Status
    :ivar date_time_period_details: Date and Time info
    :ivar reference_number: Reference number
    :ivar product_identification: Contains product identification such as UIC code...
    """
    status: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="status",
            type="Element",
            min_occurs=0,
            max_occurs=2,
            min_length=1.0,
            max_length=3.0
        )
    )
    date_time_period_details: DateTimePeriodDetailsTypeI = field(
        default=None,
        metadata=dict(
            name="dateTimePeriodDetails",
            type="Element"
        )
    )
    reference_number: str = field(
        default=None,
        metadata=dict(
            name="referenceNumber",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    product_identification: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="productIdentification",
            type="Element",
            min_occurs=0,
            max_occurs=2,
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class ItemNumberType:
    """To specify an item number.

    :ivar item_number_id: Indicates the fare family combination number
    """
    item_number_id: ItemNumberIdentificationType = field(
        default=None,
        metadata=dict(
            name="itemNumberId",
            type="Element",
            required=True
        )
    )


@dataclass
class ItemNumberType80866S:
    """To specify an item number.

    :ivar item_number_details: Item number details
    """
    item_number_details: ItemNumberIdentificationType = field(
        default=None,
        metadata=dict(
            name="itemNumberDetails",
            type="Element",
            required=True
        )
    )


@dataclass
class ItemReferencesAndVersionsType:
    """Exchange and link unique identifiers.

    :ivar passenger_fee_ref_type: Reference Qualifier.
    :ivar passenger_fee_ref_number: Reference number.
    :ivar other_characteristics: Unique id description.
    """
    passenger_fee_ref_type: str = field(
        default=None,
        metadata=dict(
            name="passengerFeeRefType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    passenger_fee_ref_number: int = field(
        default=None,
        metadata=dict(
            name="passengerFeeRefNumber",
            type="Element",
            pattern="-?[0-9]{1,3}"
        )
    )
    other_characteristics: UniqueIdDescriptionType = field(
        default=None,
        metadata=dict(
            name="otherCharacteristics",
            type="Element"
        )
    )


@dataclass
class MonetaryAndCabinInformationType:
    """
    :ivar money_and_cabin_info: Monetary and cabin information.
    """
    money_and_cabin_info: List[MonetaryAndCabinInformationDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="moneyAndCabinInfo",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class MonetaryInformationType:
    """To specify monetary information details.

    :ivar money_info: MONEY INFORMATION
    :ivar additional_money_info: MONEY INFORMATION
    """
    money_info: MonetaryInformationDetailsTypeI = field(
        default=None,
        metadata=dict(
            name="moneyInfo",
            type="Element",
            required=True
        )
    )
    additional_money_info: List[MonetaryInformationDetailsTypeI194597C] = field(
        default_factory=list,
        metadata=dict(
            name="additionalMoneyInfo",
            type="Element",
            min_occurs=0,
            max_occurs=19
        )
    )


@dataclass
class MonetaryInformationType80162S:
    """To convey monetary amounts, rates and percentages.

    :ivar monetary_details: Monetary info
    """
    monetary_details: List[MonetaryInformationDetailsTypeI65140C] = field(
        default_factory=list,
        metadata=dict(
            name="monetaryDetails",
            type="Element",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class MonetaryInformationTypeI:
    """To convey monetary amounts, rates and percentages.

    :ivar monetary_details: Monetary info
    """
    monetary_details: List[MonetaryInformationDetailsTypeI65141C] = field(
        default_factory=list,
        metadata=dict(
            name="monetaryDetails",
            type="Element",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class NumberOfUnitsType:
    """To specify the number of Units required.

    :ivar unit_number_detail: NUMBER OF UNIT DETAILS
    """
    unit_number_detail: List[NumberOfUnitDetailsType270113C] = field(
        default_factory=list,
        metadata=dict(
            name="unitNumberDetail",
            type="Element",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class NumberOfUnitsType80154S:
    """To specify the number of Units required.

    :ivar unit_number_detail: NUMBER OF UNIT DETAILS
    """
    unit_number_detail: List[NumberOfUnitDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="unitNumberDetail",
            type="Element",
            min_occurs=1,
            max_occurs=20
        )
    )


@dataclass
class OriginAndDestinationRequestType:
    """To convey information regarding Requested Segments.

    :ivar seg_ref: Requested segment number
    :ivar location_forcing: Forces arrival or departure, from/to the same airport/city
    """
    seg_ref: int = field(
        default=None,
        metadata=dict(
            name="segRef",
            type="Element",
            required=True,
            pattern="-?[0-9]{1,2}"
        )
    )
    location_forcing: List[ItineraryDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="locationForcing",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )


@dataclass
class PassengerItineraryInformationType:
    """Contains PNR travel (Reservation Booking code, Booking status). Only present
    in case with-PNR.

    :ivar booking: .
    :ivar identifier: .
    :ivar status: .
    :ivar item_number: .
    :ivar date_time_details: .
    :ivar designator: .
    :ivar movement_type: .
    :ivar product_type_details: .
    """
    booking: str = field(
        default=None,
        metadata=dict(
            name="booking",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    identifier: str = field(
        default=None,
        metadata=dict(
            name="identifier",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="status",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    item_number: int = field(
        default=None,
        metadata=dict(
            name="itemNumber",
            type="Element",
            pattern="-?[0-9]{1,3}"
        )
    )
    date_time_details: ProductDateTimeType = field(
        default=None,
        metadata=dict(
            name="dateTimeDetails",
            type="Element"
        )
    )
    designator: str = field(
        default=None,
        metadata=dict(
            name="designator",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    movement_type: str = field(
        default=None,
        metadata=dict(
            name="movementType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    product_type_details: ProductTypeDetailsType = field(
        default=None,
        metadata=dict(
            name="productTypeDetails",
            type="Element"
        )
    )


@dataclass
class PricingTicketingDetailsType:
    """To specify pricing/ticketing details.

    :ivar pricing_ticketing: Pricing ticketing Details.
    :ivar ticketing_date: PRODUCT DATE OR TIME
    :ivar company_id: COMPANY IDENTIFICATION
    :ivar selling_point: LOCATION DETAILS
    :ivar ticketing_point: LOCATION DETAILS
    :ivar journey_origin_point: Used to Target Transborder Fares
    :ivar corporate_id: Contains the ARC,IATA and ERSP numbers
    """
    pricing_ticketing: PricingTicketingInformationType = field(
        default=None,
        metadata=dict(
            name="pricingTicketing",
            type="Element"
        )
    )
    ticketing_date: ProductDateTimeTypeI194598C = field(
        default=None,
        metadata=dict(
            name="ticketingDate",
            type="Element"
        )
    )
    company_id: CompanyIdentificationType = field(
        default=None,
        metadata=dict(
            name="companyId",
            type="Element"
        )
    )
    selling_point: LocationDetailsTypeI = field(
        default=None,
        metadata=dict(
            name="sellingPoint",
            type="Element"
        )
    )
    ticketing_point: LocationDetailsTypeI = field(
        default=None,
        metadata=dict(
            name="ticketingPoint",
            type="Element"
        )
    )
    journey_origin_point: LocationDetailsTypeI = field(
        default=None,
        metadata=dict(
            name="journeyOriginPoint",
            type="Element"
        )
    )
    corporate_id: AgentIdentificationType = field(
        default=None,
        metadata=dict(
            name="corporateId",
            type="Element"
        )
    )


@dataclass
class ProposedSegmentType:
    """To specify the parameters used for product quality.

    :ivar flight_proposal: Parameters for proposed flight group
    :ivar flight_characteristic: Flight characteristics.
    :ivar maj_cabin: Majority cabin
    """
    flight_proposal: List[ProposedSegmentDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="flightProposal",
            type="Element",
            min_occurs=1,
            max_occurs=9
        )
    )
    flight_characteristic: str = field(
        default=None,
        metadata=dict(
            name="flightCharacteristic",
            type="Element",
            min_length=0.0,
            max_length=3.0
        )
    )
    maj_cabin: str = field(
        default=None,
        metadata=dict(
            name="majCabin",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class ReferenceInfoType:
    """To provide specific reference identification for a traveller.

    :ivar referencing_detail: Referencing details
    :ivar dummy_net:
    """
    referencing_detail: List[ReferencingDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="referencingDetail",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    dummy_net: str = field(
        default=None,
        metadata=dict(
            name="Dummy.NET",
            type="Element"
        )
    )


@dataclass
class RoutingInformationTypeI:
    """To provide routing information.

    :ivar routing_details: Stops details
    """
    routing_details: List[ProductLocationDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="routingDetails",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class SegmentRepetitionControlTypeI:
    """To indicate the number of segment group repetitions.

    :ivar segment_control_details: Segment control details
    """
    segment_control_details: List[SegmentRepetitionControlDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="segmentControlDetails",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class SelectionDetailsType:
    """To specify the details for making a selection.

    :ivar carrier_fee_details: Carrier fees options
    :ivar other_selection_details:
    """
    carrier_fee_details: SelectionDetailsInformationType = field(
        default=None,
        metadata=dict(
            name="carrierFeeDetails",
            type="Element",
            required=True
        )
    )
    other_selection_details: List[SelectionDetailsInformationTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="otherSelectionDetails",
            type="Element",
            min_occurs=0,
            max_occurs=98
        )
    )


@dataclass
class SpecialRequirementsDetailsType:
    """To specify special requests or service s information relating to a
    traveller.

    :ivar service_requirements_info: To specify the Service Requirement of the customer
    :ivar seat_details: Seat details
    """
    service_requirements_info: SpecialRequirementsTypeDetailsType = field(
        default=None,
        metadata=dict(
            name="serviceRequirementsInfo",
            type="Element",
            required=True
        )
    )
    seat_details: List[SpecialRequirementsDataDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="seatDetails",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class SpecificDataInformationType:
    """To specify miscellaneous data by first identifying the type of data to be
    sent and then the actual data.

    :ivar data_type_information: Carrier fee description
    :ivar data_information: Data information
    """
    data_type_information: DataTypeInformationType = field(
        default=None,
        metadata=dict(
            name="dataTypeInformation",
            type="Element",
            required=True
        )
    )
    data_information: List[DataInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="dataInformation",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class StructuredPeriodInformationType:
    """This segment is designed to convey period in a structured way.

    :ivar begin_date_time: Effective date of period of operation
    :ivar end_date_time: Discontinue date of period of operation
    :ivar frequency: It is used with a period to give a restriction for days impacted. It permits for example to indicate on which days, a flight operates.
    """
    begin_date_time: StructuredDateTimeType = field(
        default=None,
        metadata=dict(
            name="beginDateTime",
            type="Element"
        )
    )
    end_date_time: StructuredDateTimeType = field(
        default=None,
        metadata=dict(
            name="endDateTime",
            type="Element"
        )
    )
    frequency: FrequencyType = field(
        default=None,
        metadata=dict(
            name="frequency",
            type="Element"
        )
    )


@dataclass
class TaxType:
    """To specify details realting to tax(es)

    :ivar withhold_tax_surcharge: Duty tax fee category, coded
    :ivar tax_detail: TAX DETAILS
    """
    withhold_tax_surcharge: str = field(
        default=None,
        metadata=dict(
            name="withholdTaxSurcharge",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    tax_detail: List[TaxDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="taxDetail",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class TicketNumberTypeI:
    """To convey information related to a specific ticket.

    :ivar document_details:
    """
    document_details: List[TicketNumberDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="documentDetails",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class TrafficRestrictionTypeI:
    """To convey certain restrictions that apply to a means of transport on all or
    part of a journey.

    :ivar traffic_restriction_details: Traffic Restriction Details
    """
    traffic_restriction_details: List[TrafficRestrictionDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="trafficRestrictionDetails",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )


@dataclass
class TravelFlightInformationType:
    """Information about flight options.

    :ivar cabin_id: Cabin identification
    :ivar company_identity: Company Identification
    :ivar flight_detail: Type of flight details
    :ivar inclusion_detail: Details of included connecting points
    :ivar exclusion_detail: Further connection details
    :ivar unit_number_detail: Nb of connections for each requested segment of the journey.
    """
    cabin_id: CabinIdentificationType = field(
        default=None,
        metadata=dict(
            name="cabinId",
            type="Element"
        )
    )
    company_identity: List[CompanyIdentificationType120719C] = field(
        default_factory=list,
        metadata=dict(
            name="companyIdentity",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    flight_detail: ProductTypeDetailsType120801C = field(
        default=None,
        metadata=dict(
            name="flightDetail",
            type="Element"
        )
    )
    inclusion_detail: List[ConnectPointDetailsType195492C] = field(
        default_factory=list,
        metadata=dict(
            name="inclusionDetail",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    exclusion_detail: List[ConnectPointDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="exclusionDetail",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )
    unit_number_detail: List[NumberOfUnitDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="unitNumberDetail",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class TravelFlightInformationType165053S:
    """Information about flight options.

    :ivar cabin_id: Cabin identification
    :ivar company_identity: Company Identification
    :ivar flight_detail: Type of flight details
    :ivar inclusion_detail: Details of included connect point
    :ivar exclusion_detail: Further connection details
    :ivar unit_number_detail: Nb of connections allowed at requested segment level.
    """
    cabin_id: CabinIdentificationType233500C = field(
        default=None,
        metadata=dict(
            name="cabinId",
            type="Element"
        )
    )
    company_identity: List[CompanyIdentificationType120719C] = field(
        default_factory=list,
        metadata=dict(
            name="companyIdentity",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    flight_detail: ProductTypeDetailsType120801C = field(
        default=None,
        metadata=dict(
            name="flightDetail",
            type="Element"
        )
    )
    inclusion_detail: List[ConnectPointDetailsType195492C] = field(
        default_factory=list,
        metadata=dict(
            name="inclusionDetail",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    exclusion_detail: List[ConnectPointDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="exclusionDetail",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    unit_number_detail: List[NumberOfUnitDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="unitNumberDetail",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class TravelFlightInformationType197722S:
    """Information about flight options.

    :ivar cabin_id: Cabin identification
    :ivar company_identity: Company Identification
    :ivar flight_detail: Type of flight details
    :ivar inclusion_detail: Details of included connect point
    :ivar exclusion_detail: Further connection details
    :ivar unit_number_detail: Added departed flights flag
    """
    cabin_id: CabinIdentificationType233500C = field(
        default=None,
        metadata=dict(
            name="cabinId",
            type="Element"
        )
    )
    company_identity: List[CompanyIdentificationType275415C] = field(
        default_factory=list,
        metadata=dict(
            name="companyIdentity",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    flight_detail: ProductTypeDetailsType120801C = field(
        default=None,
        metadata=dict(
            name="flightDetail",
            type="Element"
        )
    )
    inclusion_detail: List[ConnectPointDetailsType195492C] = field(
        default_factory=list,
        metadata=dict(
            name="inclusionDetail",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    exclusion_detail: List[ConnectPointDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="exclusionDetail",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    unit_number_detail: List[NumberOfUnitDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="unitNumberDetail",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class TravelProductInformationTypeI:
    """To specify details related to a product.

    :ivar flight_date: Flight Date
    :ivar board_point_details: Board point
    :ivar offpoint_details: Off point
    :ivar company_details:
    :ivar flight_identification: Flight identification
    :ivar flight_type_details: Identify flight part of the journey
    """
    flight_date: ProductDateTimeTypeI = field(
        default=None,
        metadata=dict(
            name="flightDate",
            type="Element"
        )
    )
    board_point_details: LocationTypeI = field(
        default=None,
        metadata=dict(
            name="boardPointDetails",
            type="Element",
            required=True
        )
    )
    offpoint_details: LocationTypeI = field(
        default=None,
        metadata=dict(
            name="offpointDetails",
            type="Element",
            required=True
        )
    )
    company_details: CompanyIdentificationTypeI = field(
        default=None,
        metadata=dict(
            name="companyDetails",
            type="Element",
            required=True
        )
    )
    flight_identification: ProductIdentificationDetailsTypeI = field(
        default=None,
        metadata=dict(
            name="flightIdentification",
            type="Element"
        )
    )
    flight_type_details: ProductTypeDetailsTypeI = field(
        default=None,
        metadata=dict(
            name="flightTypeDetails",
            type="Element"
        )
    )


@dataclass
class TravelProductType:
    """Contains flight travel (date, time, flight number,...) and posting
    avaibility information.

    :ivar product_date_time: Date and time of departure and arrival
    :ivar location: Location of departure and arrival
    :ivar company_id: Company identification
    :ivar flight_ortrain_number: Flight number or trainNumber
    :ivar product_detail: Product details
    :ivar add_product_detail: Additional product details
    :ivar attribute_details: Attribute details
    """
    product_date_time: ProductDateTimeType195546C = field(
        default=None,
        metadata=dict(
            name="productDateTime",
            type="Element",
            required=True
        )
    )
    location: List[LocationIdentificationDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="location",
            type="Element",
            min_occurs=1,
            max_occurs=2
        )
    )
    company_id: CompanyIdentificationType195544C = field(
        default=None,
        metadata=dict(
            name="companyId",
            type="Element"
        )
    )
    flight_ortrain_number: str = field(
        default=None,
        metadata=dict(
            name="flightOrtrainNumber",
            type="Element",
            min_length=1.0,
            max_length=8.0
        )
    )
    product_detail: AdditionalProductDetailsType = field(
        default=None,
        metadata=dict(
            name="productDetail",
            type="Element"
        )
    )
    add_product_detail: ProductFacilitiesType = field(
        default=None,
        metadata=dict(
            name="addProductDetail",
            type="Element"
        )
    )
    attribute_details: List[CodedAttributeInformationType247828C] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class TravellerReferenceInformationType:
    """To specify traveller/personal details.

    :ivar ptc: Requested passenger type
    :ivar traveller: Traveller details
    """
    ptc: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ptc",
            type="Element",
            min_occurs=0,
            max_occurs=3,
            min_length=1.0,
            max_length=6.0
        )
    )
    traveller: List[TravellerDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="traveller",
            type="Element",
            min_occurs=1,
            max_occurs=9
        )
    )


@dataclass
class UserIdentificationType:
    """User Identification.

    :ivar office_identification: Originator Identification Details
    :ivar office_type: Used to specify which kind of info is given in DE 9900.
    :ivar office_code: The code given to an agent by the originating reservation system.
    """
    office_identification: OriginatorIdentificationDetailsTypeI = field(
        default=None,
        metadata=dict(
            name="officeIdentification",
            type="Element"
        )
    )
    office_type: str = field(
        default=None,
        metadata=dict(
            name="officeType",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    office_code: str = field(
        default=None,
        metadata=dict(
            name="officeCode",
            type="Element",
            min_length=1.0,
            max_length=30.0
        )
    )


@dataclass
class ValueSearchCriteriaType:
    """To specify Criteria with list of parameters.

    :ivar criteria_name:
    :ivar criteria_code:
    :ivar value:
    :ivar criteria_details:
    """
    criteria_name: str = field(
        default=None,
        metadata=dict(
            name="criteriaName",
            type="Element",
            min_length=1.0,
            max_length=50.0
        )
    )
    criteria_code: str = field(
        default=None,
        metadata=dict(
            name="criteriaCode",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            min_length=1.0,
            max_length=18.0
        )
    )
    criteria_details: List[CriteriaiDetaislType] = field(
        default_factory=list,
        metadata=dict(
            name="criteriaDetails",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class FoprepresentationType:
    """
    :ivar form_of_payment_details: Form of payment information.
    :ivar passenger_fee_reference: Fee/Reduction Passenger reference.
    """
    form_of_payment_details: FormOfPaymentTypeI = field(
        default=None,
        metadata=dict(
            name="formOfPaymentDetails",
            type="Element",
            required=True
        )
    )
    passenger_fee_reference: ItemReferencesAndVersionsType = field(
        default=None,
        metadata=dict(
            name="passengerFeeReference",
            type="Element"
        )
    )


@dataclass
class GroupPassengerDetailsType:
    """Contain passenger information.

    :ivar passenger_reference: Trigger
    :ivar psg_details_info: pricing option at passenger level
    """
    passenger_reference: SegmentRepetitionControlTypeI = field(
        default=None,
        metadata=dict(
            name="passengerReference",
            type="Element",
            required=True
        )
    )
    psg_details_info: List["GroupPassengerDetailsType.PsgDetailsInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="psgDetailsInfo",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )

    @dataclass
    class PsgDetailsInfo:
        """
        :ivar discount_ptc: PTC/Discount Code age
        :ivar flequent_flyer_details: Tier level information
        """
        discount_ptc: FareInformationTypeI = field(
            default=None,
            metadata=dict(
                name="discountPtc",
                type="Element",
                required=True
            )
        )
        flequent_flyer_details: FrequentTravellerIdentificationCodeType = field(
            default=None,
            metadata=dict(
                name="flequentFlyerDetails",
                type="Element"
            )
        )


@dataclass
class FareMasterPricerTravelBoardSearch:
    """Master Pricer Travel Board Search Flex pricer Flex pricer.

    :ivar number_of_unit: Number of seats , recommendations.
    :ivar global_options: Global options
    :ivar pax_reference: Traveler Details
    :ivar customer_ref: Customer references
    :ivar form_of_payment_by_passenger: Fee with different payment forms by passenger.
    :ivar solution_family: Solution Family
    :ivar passenger_info_grp: Passenger info group (9 ADT   9 IN)
    :ivar fare_families: Fare families.
    :ivar fare_options: Fare options
    :ivar price_to_beat: Indicates Price to beat
    :ivar tax_info: Tax Details
    :ivar travel_flight_info: Details of a Flight : Direct, Non stop...
    :ivar value_search:
    :ivar buckets: Buckets
    :ivar itinerary: Itinerary
    :ivar ticket_change_info: Changed ticket information.
    :ivar combination_fare_families: Specify fare family combinations
    :ivar fee_option: Fee option group.
    :ivar office_id_details: List of Office Id Details
    """
    number_of_unit: NumberOfUnitsType = field(
        default=None,
        metadata=dict(
            name="numberOfUnit",
            type="Element"
        )
    )
    global_options: AttributeType = field(
        default=None,
        metadata=dict(
            name="globalOptions",
            type="Element"
        )
    )
    pax_reference: List[TravellerReferenceInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="paxReference",
            type="Element",
            min_occurs=0,
            max_occurs=6
        )
    )
    customer_ref: ConsumerReferenceInformationType = field(
        default=None,
        metadata=dict(
            name="customerRef",
            type="Element"
        )
    )
    form_of_payment_by_passenger: List[FoprepresentationType] = field(
        default_factory=list,
        metadata=dict(
            name="formOfPaymentByPassenger",
            type="Element",
            min_occurs=0,
            max_occurs=60
        )
    )
    solution_family: List[FareInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="solutionFamily",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    passenger_info_grp: List[GroupPassengerDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="passengerInfoGrp",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    fare_families: List["FareMasterPricerTravelBoardSearch.FareFamilies"] = field(
        default_factory=list,
        metadata=dict(
            name="fareFamilies",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    fare_options: "FareMasterPricerTravelBoardSearch.FareOptions" = field(
        default=None,
        metadata=dict(
            name="fareOptions",
            type="Element"
        )
    )
    price_to_beat: MonetaryInformationType = field(
        default=None,
        metadata=dict(
            name="priceToBeat",
            type="Element"
        )
    )
    tax_info: List[TaxType] = field(
        default_factory=list,
        metadata=dict(
            name="taxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    travel_flight_info: TravelFlightInformationType197722S = field(
        default=None,
        metadata=dict(
            name="travelFlightInfo",
            type="Element"
        )
    )
    value_search: List[ValueSearchCriteriaType] = field(
        default_factory=list,
        metadata=dict(
            name="valueSearch",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    buckets: List["FareMasterPricerTravelBoardSearch.Buckets"] = field(
        default_factory=list,
        metadata=dict(
            name="buckets",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )
    itinerary: List["FareMasterPricerTravelBoardSearch.Itinerary"] = field(
        default_factory=list,
        metadata=dict(
            name="itinerary",
            type="Element",
            min_occurs=0,
            max_occurs=18
        )
    )
    ticket_change_info: "FareMasterPricerTravelBoardSearch.TicketChangeInfo" = field(
        default=None,
        metadata=dict(
            name="ticketChangeInfo",
            type="Element"
        )
    )
    combination_fare_families: List["FareMasterPricerTravelBoardSearch.CombinationFareFamilies"] = field(
        default_factory=list,
        metadata=dict(
            name="combinationFareFamilies",
            type="Element",
            min_occurs=0,
            max_occurs=2000
        )
    )
    fee_option: List["FareMasterPricerTravelBoardSearch.FeeOption"] = field(
        default_factory=list,
        metadata=dict(
            name="feeOption",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    office_id_details: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails"] = field(
        default_factory=list,
        metadata=dict(
            name="officeIdDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )

    @dataclass
    class FareFamilies:
        """
        :ivar family_information: Segment used to target Commercial Fare Family.
        :ivar family_criteria: Description of Fare Family Criteria.
        :ivar fare_family_segment: Fare family requested segment details.
        :ivar other_possible_criteria: Description of other possible fare family criteria.
        """
        family_information: FareFamilyType80157S = field(
            default=None,
            metadata=dict(
                name="familyInformation",
                type="Element",
                required=True
            )
        )
        family_criteria: FareFamilyCriteriaType = field(
            default=None,
            metadata=dict(
                name="familyCriteria",
                type="Element"
            )
        )
        fare_family_segment: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment"] = field(
            default_factory=list,
            metadata=dict(
                name="fareFamilySegment",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )
        other_possible_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria"] = field(
            default_factory=list,
            metadata=dict(
                name="otherPossibleCriteria",
                type="Element",
                min_occurs=0,
                max_occurs=20
            )
        )

        @dataclass
        class FareFamilySegment:
            """
            :ivar reference_info: Requested segment reference
            :ivar family_criteria: Description of fare family criteria.
            """
            reference_info: ReferenceInfoType = field(
                default=None,
                metadata=dict(
                    name="referenceInfo",
                    type="Element",
                    required=True
                )
            )
            family_criteria: FareFamilyCriteriaType = field(
                default=None,
                metadata=dict(
                    name="familyCriteria",
                    type="Element"
                )
            )

        @dataclass
        class OtherPossibleCriteria:
            """
            :ivar logical_link: Logical link with other criteria.
            :ivar family_criteria: Description of fare family criteria.
            :ivar fare_family_segment: Fare family requested segment details.
            """
            logical_link: BooleanExpressionRuleType = field(
                default=None,
                metadata=dict(
                    name="logicalLink",
                    type="Element",
                    required=True
                )
            )
            family_criteria: FareFamilyCriteriaType = field(
                default=None,
                metadata=dict(
                    name="familyCriteria",
                    type="Element"
                )
            )
            fare_family_segment: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment"] = field(
                default_factory=list,
                metadata=dict(
                    name="fareFamilySegment",
                    type="Element",
                    min_occurs=0,
                    max_occurs=6
                )
            )

            @dataclass
            class FareFamilySegment:
                """
                :ivar reference_info: Requested segment reference
                :ivar family_criteria: Description of fare family criteria.
                """
                reference_info: ReferenceInfoType = field(
                    default=None,
                    metadata=dict(
                        name="referenceInfo",
                        type="Element",
                        required=True
                    )
                )
                family_criteria: FareFamilyCriteriaType = field(
                    default=None,
                    metadata=dict(
                        name="familyCriteria",
                        type="Element"
                    )
                )

    @dataclass
    class FareOptions:
        """
        :ivar pricing_tick_info: Pricing and ticketing details.
        :ivar corporate: Corporate name/number used to target fares
        :ivar ticketing_price_scheme: Ticketing price scheme.
        :ivar fee_id_description: PSR number
        :ivar conversion_rate: Used to force the currency of pricing
        :ivar form_of_payment: Form of payment information.
        :ivar frequent_traveller_info: Frequent traveller information
        :ivar monetary_cabin_info: Monetary and cabin information.
        """
        pricing_tick_info: PricingTicketingDetailsType = field(
            default=None,
            metadata=dict(
                name="pricingTickInfo",
                type="Element",
                required=True
            )
        )
        corporate: CorporateIdentificationType = field(
            default=None,
            metadata=dict(
                name="corporate",
                type="Element"
            )
        )
        ticketing_price_scheme: TicketingPriceSchemeType = field(
            default=None,
            metadata=dict(
                name="ticketingPriceScheme",
                type="Element"
            )
        )
        fee_id_description: CodedAttributeType197696S = field(
            default=None,
            metadata=dict(
                name="feeIdDescription",
                type="Element"
            )
        )
        conversion_rate: ConversionRateType = field(
            default=None,
            metadata=dict(
                name="conversionRate",
                type="Element"
            )
        )
        form_of_payment: FormOfPaymentTypeI = field(
            default=None,
            metadata=dict(
                name="formOfPayment",
                type="Element"
            )
        )
        frequent_traveller_info: FrequentTravellerIdentificationCodeType177150S = field(
            default=None,
            metadata=dict(
                name="frequentTravellerInfo",
                type="Element"
            )
        )
        monetary_cabin_info: MonetaryAndCabinInformationType = field(
            default=None,
            metadata=dict(
                name="monetaryCabinInfo",
                type="Element"
            )
        )

    @dataclass
    class Buckets:
        """
        :ivar bucket_info: Bucket information: name, priority, weight
        :ivar bucket_details: Bucket details
        """
        bucket_info: BucketInformationType = field(
            default=None,
            metadata=dict(
                name="bucketInfo",
                type="Element",
                required=True
            )
        )
        bucket_details: List[BucketDetailsType] = field(
            default_factory=list,
            metadata=dict(
                name="bucketDetails",
                type="Element",
                min_occurs=0,
                max_occurs=15
            )
        )

    @dataclass
    class Itinerary:
        """
        :ivar requested_segment_ref: Indicates reference of the requested segment
        :ivar departure_localization: Specification of the requested departure point
        :ivar arrival_localization: Specification of the requested arrival point
        :ivar time_details: Details on requested date and time plus range of date trip duration
        :ivar flight_info: Specify Flight options.
        :ivar family_information: Segment used to target Commercial Fare Family at requested segment level
        :ivar value_search:
        :ivar group_of_flights: list of proposed segments per requested segment
        :ivar flight_info_pnr: Info concerning the flights booked in the PNR
        :ivar requested_segment_action: Action identification for the requested segment
        :ivar attributes: Coded attributes
        """
        requested_segment_ref: OriginAndDestinationRequestType = field(
            default=None,
            metadata=dict(
                name="requestedSegmentRef",
                type="Element",
                required=True
            )
        )
        departure_localization: DepartureLocationType = field(
            default=None,
            metadata=dict(
                name="departureLocalization",
                type="Element"
            )
        )
        arrival_localization: ArrivalLocalizationType = field(
            default=None,
            metadata=dict(
                name="arrivalLocalization",
                type="Element"
            )
        )
        time_details: DateAndTimeInformationType181295S = field(
            default=None,
            metadata=dict(
                name="timeDetails",
                type="Element"
            )
        )
        flight_info: TravelFlightInformationType165053S = field(
            default=None,
            metadata=dict(
                name="flightInfo",
                type="Element"
            )
        )
        family_information: FareFamilyType = field(
            default=None,
            metadata=dict(
                name="familyInformation",
                type="Element"
            )
        )
        value_search: List[ValueSearchCriteriaType] = field(
            default_factory=list,
            metadata=dict(
                name="valueSearch",
                type="Element",
                min_occurs=0,
                max_occurs=99
            )
        )
        group_of_flights: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights"] = field(
            default_factory=list,
            metadata=dict(
                name="groupOfFlights",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )
        flight_info_pnr: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr"] = field(
            default_factory=list,
            metadata=dict(
                name="flightInfoPNR",
                type="Element",
                min_occurs=0,
                max_occurs=4
            )
        )
        requested_segment_action: ActionIdentificationType = field(
            default=None,
            metadata=dict(
                name="requestedSegmentAction",
                type="Element"
            )
        )
        attributes: CodedAttributeType = field(
            default=None,
            metadata=dict(
                name="attributes",
                type="Element"
            )
        )

        @dataclass
        class GroupOfFlights:
            """
            :ivar prop_flight_gr_detail: To indicate parameters for proposed flight group.
            :ivar price_to_beat: Indicates Price to beat
            :ivar flight_details: list of flight per proposed segment
            """
            prop_flight_gr_detail: ProposedSegmentType = field(
                default=None,
                metadata=dict(
                    name="propFlightGrDetail",
                    type="Element",
                    required=True
                )
            )
            price_to_beat: MonetaryInformationType = field(
                default=None,
                metadata=dict(
                    name="priceToBeat",
                    type="Element"
                )
            )
            flight_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="flightDetails",
                    type="Element",
                    min_occurs=1,
                    max_occurs=4
                )
            )

            @dataclass
            class FlightDetails:
                """
                :ivar flight_information: Specification of details on the flight and posting availability
                :ivar avl_info: returns booking class and availability context
                :ivar technical_stop: Details on Flight date, time and location of technical stop or change of gauge
                :ivar commercial_agreement: Code Share Agreement description for current flight.
                :ivar add_info: Additional Info about flight, such as Reference number, and several options
                :ivar terminal_equipment_details: Terminal, Equipment and EFT Details. If a Total EFT of the Travel Solution is requested then we will have 2 occurrences of the terminalEquipmentDetails attached to the first leg flightInformation: the 1st occurence will give the EFT of the leg, the 2nd occurrence will give the total EFT of the Travel Solution.
                :ivar reservation_info: PNR flight reservation info
                :ivar price_to_beat: Indicates Price to beat
                """
                flight_information: TravelProductType = field(
                    default=None,
                    metadata=dict(
                        name="flightInformation",
                        type="Element",
                        required=True
                    )
                )
                avl_info: List[FlightProductInformationType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="avlInfo",
                        type="Element",
                        min_occurs=0,
                        max_occurs=6
                    )
                )
                technical_stop: List[DateAndTimeInformationType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="technicalStop",
                        type="Element",
                        min_occurs=0,
                        max_occurs=5
                    )
                )
                commercial_agreement: CommercialAgreementsType78540S = field(
                    default=None,
                    metadata=dict(
                        name="commercialAgreement",
                        type="Element"
                    )
                )
                add_info: HeaderInformationTypeI = field(
                    default=None,
                    metadata=dict(
                        name="addInfo",
                        type="Element"
                    )
                )
                terminal_equipment_details: List[AdditionalProductDetailsTypeI] = field(
                    default_factory=list,
                    metadata=dict(
                        name="terminalEquipmentDetails",
                        type="Element",
                        min_occurs=0,
                        max_occurs=2
                    )
                )
                reservation_info: PassengerItineraryInformationType = field(
                    default=None,
                    metadata=dict(
                        name="reservationInfo",
                        type="Element"
                    )
                )
                price_to_beat: MonetaryInformationType = field(
                    default=None,
                    metadata=dict(
                        name="priceToBeat",
                        type="Element"
                    )
                )

        @dataclass
        class FlightInfoPnr:
            """
            :ivar travel_response_details: Travel Response Details: - Board/Off aiports - Flight number - Part of the journey - Day difference between Board and off - Departure/Arrival dates - Departure/Arrival times
            :ivar time_table_date: Time Table Effective/Discontinue dates and frequency of operating Travel Solution
            :ivar terminal_equipment_details: Terminal, Equipment and EFT Details. If a Total EFT of the Travel Solution is requested then we will have 2 occurrences of the terminalEquipmentDetails attached to the first leg travelResponseDetails: the 1st occurrence will give the EFT of the leg, the 2nd occurrence will give the total EFT of the Travel Solution.
            :ivar codeshare_data: Codeshare data
            :ivar disclosure: Disclosure message from an operating carrier.
            :ivar stop_details: Stops Details
            :ivar traffic_restriction_data: Traffic restriction information
            :ivar reservation_info: PNR flight reservation info
            :ivar incidental_stop_info: Incidental stop information.
            """
            travel_response_details: TravelProductInformationTypeI = field(
                default=None,
                metadata=dict(
                    name="travelResponseDetails",
                    type="Element",
                    required=True
                )
            )
            time_table_date: StructuredPeriodInformationType = field(
                default=None,
                metadata=dict(
                    name="timeTableDate",
                    type="Element"
                )
            )
            terminal_equipment_details: List[AdditionalProductDetailsTypeI] = field(
                default_factory=list,
                metadata=dict(
                    name="terminalEquipmentDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=2
                )
            )
            codeshare_data: CommercialAgreementsType = field(
                default=None,
                metadata=dict(
                    name="codeshareData",
                    type="Element"
                )
            )
            disclosure: FreeTextInformationType = field(
                default=None,
                metadata=dict(
                    name="disclosure",
                    type="Element"
                )
            )
            stop_details: RoutingInformationTypeI = field(
                default=None,
                metadata=dict(
                    name="stopDetails",
                    type="Element"
                )
            )
            traffic_restriction_data: TrafficRestrictionTypeI = field(
                default=None,
                metadata=dict(
                    name="trafficRestrictionData",
                    type="Element"
                )
            )
            reservation_info: PassengerItineraryInformationType = field(
                default=None,
                metadata=dict(
                    name="reservationInfo",
                    type="Element"
                )
            )
            incidental_stop_info: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.IncidentalStopInfo"] = field(
                default_factory=list,
                metadata=dict(
                    name="incidentalStopInfo",
                    type="Element",
                    min_occurs=0,
                    max_occurs=8
                )
            )

            @dataclass
            class IncidentalStopInfo:
                """
                :ivar date_time_info: Incidental stop date/time information
                """
                date_time_info: DateAndTimeInformationTypeI = field(
                    default=None,
                    metadata=dict(
                        name="dateTimeInfo",
                        type="Element",
                        required=True
                    )
                )

    @dataclass
    class TicketChangeInfo:
        """
        :ivar ticket_number_details: Ticket nb details.
        :ivar ticket_requested_segments: Changed ticket requested segments.
        """
        ticket_number_details: TicketNumberTypeI = field(
            default=None,
            metadata=dict(
                name="ticketNumberDetails",
                type="Element",
                required=True
            )
        )
        ticket_requested_segments: List["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments"] = field(
            default_factory=list,
            metadata=dict(
                name="ticketRequestedSegments",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )

        @dataclass
        class TicketRequestedSegments:
            """
            :ivar action_identification: Action identification.
            :ivar connect_point_details: Connected cities in changed ticket requested segment.
            """
            action_identification: ActionIdentificationType = field(
                default=None,
                metadata=dict(
                    name="actionIdentification",
                    type="Element",
                    required=True
                )
            )
            connect_point_details: ConnectionTypeI = field(
                default=None,
                metadata=dict(
                    name="connectPointDetails",
                    type="Element"
                )
            )

    @dataclass
    class CombinationFareFamilies:
        """
        :ivar item_ffcnumber: Specification of the item number
        :ivar nb_of_units: Number of units.
        :ivar reference_info: Requested segment reference
        """
        item_ffcnumber: ItemNumberType = field(
            default=None,
            metadata=dict(
                name="itemFFCNumber",
                type="Element",
                required=True
            )
        )
        nb_of_units: NumberOfUnitsType80154S = field(
            default=None,
            metadata=dict(
                name="nbOfUnits",
                type="Element"
            )
        )
        reference_info: List[ReferenceInfoType] = field(
            default_factory=list,
            metadata=dict(
                name="referenceInfo",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )

    @dataclass
    class FeeOption:
        """
        :ivar fee_type_info: Nature of the fee (OB,OC,..)
        :ivar rate_tax: Associated rate tax.
        :ivar fee_details: Details for each fee.
        """
        fee_type_info: SelectionDetailsType = field(
            default=None,
            metadata=dict(
                name="feeTypeInfo",
                type="Element",
                required=True
            )
        )
        rate_tax: MonetaryInformationType80162S = field(
            default=None,
            metadata=dict(
                name="rateTax",
                type="Element"
            )
        )
        fee_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails"] = field(
            default_factory=list,
            metadata=dict(
                name="feeDetails",
                type="Element",
                min_occurs=0,
                max_occurs=99
            )
        )

        @dataclass
        class FeeDetails:
            """
            :ivar fee_info: Fee information
            :ivar associated_amounts: Associated amounts : amounts to take into account to calculate fee.
            :ivar fee_description_grp: Fee description
            """
            fee_info: SpecificDataInformationType = field(
                default=None,
                metadata=dict(
                    name="feeInfo",
                    type="Element",
                    required=True
                )
            )
            associated_amounts: MonetaryInformationTypeI = field(
                default=None,
                metadata=dict(
                    name="associatedAmounts",
                    type="Element"
                )
            )
            fee_description_grp: "FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp" = field(
                default=None,
                metadata=dict(
                    name="feeDescriptionGrp",
                    type="Element"
                )
            )

            @dataclass
            class FeeDescriptionGrp:
                """
                :ivar item_number_info: Specification of the item number
                :ivar service_attributes_info: Attributes (SSR code EMD, RFIC, SSIM)
                :ivar service_description_info: Other service information (service description, ...)
                """
                item_number_info: ItemNumberType80866S = field(
                    default=None,
                    metadata=dict(
                        name="itemNumberInfo",
                        type="Element",
                        required=True
                    )
                )
                service_attributes_info: AttributeType61377S = field(
                    default=None,
                    metadata=dict(
                        name="serviceAttributesInfo",
                        type="Element"
                    )
                )
                service_description_info: SpecialRequirementsDetailsType = field(
                    default=None,
                    metadata=dict(
                        name="serviceDescriptionInfo",
                        type="Element"
                    )
                )

    @dataclass
    class OfficeIdDetails:
        """
        :ivar office_id_information: Office Id Information
        :ivar nb_of_units: Number of units.
        :ivar uid_option: UID option
        :ivar pricing_tick_info: Pricing and ticketing details.
        :ivar corporate_fare_info: Corporate fare information
        :ivar travel_flight_info: Details of a Flight : Direct, Non stop...
        :ivar airline_distribution_details: Details of airline distribution at requested segment level
        """
        office_id_information: UserIdentificationType = field(
            default=None,
            metadata=dict(
                name="officeIdInformation",
                type="Element",
                required=True
            )
        )
        nb_of_units: NumberOfUnitsType80154S = field(
            default=None,
            metadata=dict(
                name="nbOfUnits",
                type="Element"
            )
        )
        uid_option: CodedAttributeType78500S = field(
            default=None,
            metadata=dict(
                name="uidOption",
                type="Element"
            )
        )
        pricing_tick_info: PricingTicketingDetailsType = field(
            default=None,
            metadata=dict(
                name="pricingTickInfo",
                type="Element"
            )
        )
        corporate_fare_info: CorporateFareInformationType = field(
            default=None,
            metadata=dict(
                name="corporateFareInfo",
                type="Element"
            )
        )
        travel_flight_info: TravelFlightInformationType = field(
            default=None,
            metadata=dict(
                name="travelFlightInfo",
                type="Element"
            )
        )
        airline_distribution_details: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails"] = field(
            default_factory=list,
            metadata=dict(
                name="airlineDistributionDetails",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )

        @dataclass
        class AirlineDistributionDetails:
            """
            :ivar requested_segment_ref: Indicates reference of the requested segment
            :ivar flight_info: Specify Flight options.
            """
            requested_segment_ref: OriginAndDestinationRequestType = field(
                default=None,
                metadata=dict(
                    name="requestedSegmentRef",
                    type="Element",
                    required=True
                )
            )
            flight_info: TravelFlightInformationType = field(
                default=None,
                metadata=dict(
                    name="flightInfo",
                    type="Element"
                )
            )