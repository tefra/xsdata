from dataclasses import dataclass, field
from typing import List

from ..common_v48_0.common import *


@dataclass
class AttrRailInfoOrgDesAndRailLoc:
    """
    Basic attributes used to describe an origin destination pair
    """

    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="The IATA location code for this origination of this entity.",
        )
    )
    rail_loc_origin: TypeRailLocationCode = field(
        default=None,
        metadata=dict(
            name="RailLocOrigin",
            type="Attribute",
            help="RCH specific origin code (a.k.a UCodes) which uniquely identifies a train station.",
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="The IATA location code for this destination of this entity.",
        )
    )
    rail_loc_destination: TypeRailLocationCode = field(
        default=None,
        metadata=dict(
            name="RailLocDestination",
            type="Attribute",
            help="RCH specific destination code (a.k.a UCodes) which uniquely identifies a train station.",
        )
    )
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            help="The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
            required=True
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute",
            help="The date and time at which this entity arrives at the destination. This does not include time zone information since it can be derived from the origin location.",
        )
    )


@dataclass
class AttrRailOrigDestInfo:
    """
    Holds all relevant origin/destination and departure/arrival details.
    """

    origin_station_name: str = field(
        default=None,
        metadata=dict(
            name="OriginStationName",
            type="Attribute",
            help="The origin station name for the Journey.",
        )
    )
    destination_station_name: str = field(
        default=None,
        metadata=dict(
            name="DestinationStationName",
            type="Attribute",
            help="The destination station name for the Journey.",
        )
    )


@dataclass
class AttrRailSegmentOrigDestInfo:
    """
    Holds all relevant origin/destination and departure/arrival details.
    """

    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="The IATA location code for this origination of this entity.",
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="The IATA location code for this destination of this entity.",
        )
    )
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            help="The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
            required=True
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute",
            help="The date and time at which this entity arrives at the destination. This does not include time zone information since it can be derived from the origin location.",
        )
    )
    origin_station_name: str = field(
        default=None,
        metadata=dict(
            name="OriginStationName",
            type="Attribute",
            help="The origin station name for the Journey.",
        )
    )
    destination_station_name: str = field(
        default=None,
        metadata=dict(
            name="DestinationStationName",
            type="Attribute",
            help="The destination station name for the Journey.",
        )
    )
    rail_loc_origin: TypeRailLocationCode = field(
        default=None,
        metadata=dict(
            name="RailLocOrigin",
            type="Attribute",
            help="RCH specific origin code (a.k.a UCodes) which uniquely identifies a train station.",
        )
    )
    rail_loc_destination: TypeRailLocationCode = field(
        default=None,
        metadata=dict(
            name="RailLocDestination",
            type="Attribute",
            help="RCH specific destination code (a.k.a UCodes) which uniquely identifies a train station.",
        )
    )


@dataclass
class FareValidity:
    """
    Associates fare validity dates with journeys.
    """

    rail_journey_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="RailJourneyRef",
            type="Attribute",
            help="Reference to a journey to which this fare validity refers.",
            required=True
        )
    )
    not_valid_before: str = field(
        default=None,
        metadata=dict(
            name="NotValidBefore",
            type="Attribute",
            help="Fare not valid before this date.",
        )
    )
    not_valid_after: str = field(
        default=None,
        metadata=dict(
            name="NotValidAfter",
            type="Attribute",
            help="Fare not valid after this date.",
        )
    )


@dataclass
class FulFillmentType:
    """
    Fulfillment options for this segment. the options will be one of "Ticket on Departure", "Ticketless", "Ticket By Email", "Travel Agency"
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=0.0,
            max_length=255.0
        )
    )


@dataclass
class JourneyRemark(str):
    """
    A Remark for a Journey.
    """

    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class OperatingCompany(str):
    """
    A textual remark identifying the OperatingCompany/Train Service other than BN orTL
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="Company Short Text",
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="Name Identifying the Train Service other than BN orTL",
            required=True
        )
    )


@dataclass
class RailAutoSeatAssignment:
    """
    Request object used to request seats automatically by seat type
    """

    seat_type: str = field(
        default=None,
        metadata=dict(
            name="SeatType",
            type="Attribute",
            help="Indicates codeset of values such as Seat Type like Place,Position, Smoking Choice, Place Arrangement, Place Direction, Compartment.",
            required=True,
            min_length=0.0,
            max_length=255.0
        )
    )
    seat_value: str = field(
        default=None,
        metadata=dict(
            name="SeatValue",
            type="Attribute",
            help="Indicates the value specific to the selected type.",
            required=True,
            min_length=0.0,
            max_length=255.0
        )
    )
    rail_segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="RailSegmentRef",
            type="Attribute",
            help="The rail segment that this assignment belongs to",
        )
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="The booking traveler that this seat assignment is for. If not entered, this applies to the primary booking traveler and other passengers are adjacent.",
        )
    )


@dataclass
class RailAvailInfo:
    class_code: TypeRailClass = field(
        default=None,
        metadata=dict(
            name="ClassCode",
            type="Attribute",
            help="A booking code or fare basis code or fare class.",
        )
    )
    quantity: int = field(
        default=None,
        metadata=dict(
            name="Quantity",
            type="Attribute",
            help="Available fare basis code or fare class quantity.",
        )
    )
    cabin_class: TypeRailCabin = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            help="The fare basis code or fare class for this fare.",
        )
    )


@dataclass
class RailBookingInfo:
    """
    Links journeys and fares together
    """

    rail_fare_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="RailFareRef",
            type="Attribute",
            help="Reference to a fare that applies to the journey below.",
            required=True
        )
    )
    rail_journey_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="RailJourneyRef",
            type="Attribute",
            help="Reference to a journeys on which the above fare applies.",
            required=True
        )
    )
    optional_service: bool = field(
        default="false",
        metadata=dict(
            name="OptionalService",
            type="Attribute",
            help="Indicate the OfferFareItem elements will be Optional or not.",
        )
    )


@dataclass
class RailExchangeInfo:
    """
    Exchange information for the rail booking.
    """

    refund_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="RefundAmount",
            type="Attribute",
            help=None,
        )
    )
    cancellation_fee: TypeMoney = field(
        default=None,
        metadata=dict(
            name="CancellationFee",
            type="Attribute",
            help=None,
        )
    )
    exchange_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ExchangeAmount",
            type="Attribute",
            help=None,
        )
    )
    approximate_refund_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ApproximateRefundAmount",
            type="Attribute",
            help=None,
        )
    )
    approximate_cancellation_fee: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ApproximateCancellationFee",
            type="Attribute",
            help=None,
        )
    )
    approximate_exchange_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ApproximateExchangeAmount",
            type="Attribute",
            help="The Converted total price in Default Currency for this entity including base price and all taxes.",
        )
    )
    retain_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="RetainAmount",
            type="Attribute",
            help="Amount retained by a rail vendor for future use at the vendor’s site.",
        )
    )


@dataclass
class RailFareComponent:
    """
    Contains fare and discount information for each passenger type
    """

    discount: List["RailFareComponent.Discount"] = field(
        default_factory=list,
        metadata=dict(
            name="Discount",
            type="Element",
            help="Discount information specific to the fare component",
            min_occurs=0,
            max_occurs=5
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="FareComponent amount",
        )
    )
    age: int = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute",
            help=None,
        )
    )
    passenger_type_code: TypePtc = field(
        default=None,
        metadata=dict(
            name="PassengerTypeCode",
            type="Attribute",
            help="The three character passenger code",
        )
    )
    supplier_passenger_type: str = field(
        default=None,
        metadata=dict(
            name="SupplierPassengerType",
            type="Attribute",
            help="Supplier passenger type code",
        )
    )
    quantity: int = field(
        default=None,
        metadata=dict(
            name="Quantity",
            type="Attribute",
            help=None,
        )
    )

    @dataclass
    class Discount:
        discount_card: List[DiscountCard] = field(
            default_factory=list,
            metadata=dict(
                name="DiscountCard",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=9
            )
        )
        key: TypeRef = field(
            default=None,
            metadata=dict(
                name="Key",
                type="Attribute",
                help=None,
            )
        )


@dataclass
class RailFareId(str):
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class RailFareIdref:
    """
    Reference to a complete FareID from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class RailFareNote(str):
    """
    A simple textual fare note. Used within several other objects.
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    note_name: str = field(
        default=None,
        metadata=dict(
            name="NoteName",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class RailFareNoteRef:
    """
    A reference to a fare note from a shared list. Used to minimize xml results.
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class RailFareRef:
    """
    Reference to a complete FareInfo from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class RailJourneyRef:
    """
    Reference to a RailJourney
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class RailLegModifiers:
    permitted_connection_points: "RailLegModifiers.PermittedConnectionPoints" = field(
        default=None,
        metadata=dict(
            name="PermittedConnectionPoints",
            type="Element",
            help=None,
        )
    )
    prohibited_connection_points: "RailLegModifiers.ProhibitedConnectionPoints" = field(
        default=None,
        metadata=dict(
            name="ProhibitedConnectionPoints",
            type="Element",
            help=None,
        )
    )
    class_value: str = field(
        default=None,
        metadata=dict(
            name="Class",
            type="Attribute",
            help=None,
        )
    )

    @dataclass
    class PermittedConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata=dict(
                name="ConnectionPoint",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata=dict(
                name="ConnectionPoint",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class RailPricingModifiers:
    """
    Search flexibiity criteria .
    """

    discount_card: List[DiscountCard] = field(
        default_factory=list,
        metadata=dict(
            name="DiscountCard",
            type="Element",
            help="Discount request for rail.",
            min_occurs=0,
            max_occurs=9
        )
    )
    prohibit_non_refundable_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitNonRefundableFares",
            type="Attribute",
            help="Indicates whether it prohibits NonRefundable Fares.",
        )
    )
    prohibit_non_exchangeable_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitNonExchangeableFares",
            type="Attribute",
            help="Indicates whether it prohibits NonExchangeable Fares .",
        )
    )
    currency_type: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            help="3 Letter Currency Code",
        )
    )
    rail_search_type: TypeRailSearchType = field(
        default=None,
        metadata=dict(
            name="RailSearchType",
            type="Attribute",
            help="RailSearchType options are 'All Fares' 'Fastest' 'Lowest Fare' 'One Fare Per Class' 'Seasons'. Supported by NTV/VF only for 'All Fares' 'Lowest Fare' and 'One Fare Per Class'. Provider : RCH",
        )
    )


@dataclass
class RailRefundInfo:
    """
    Information about refund.
    """

    refund_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="RefundAmount",
            type="Attribute",
            help="Amount refunded back to customer.",
        )
    )
    cancellation_fee: TypeMoney = field(
        default=None,
        metadata=dict(
            name="CancellationFee",
            type="Attribute",
            help="Cancellation penalty imposed by the distributor.",
        )
    )
    refund: bool = field(
        default=None,
        metadata=dict(
            name="Refund",
            type="Attribute",
            help="Indicates whether vendor offers refund on rail reservation.",
        )
    )
    retain: bool = field(
        default=None,
        metadata=dict(
            name="Retain",
            type="Attribute",
            help="Indicates whether vendor retains the amount to be used later.",
        )
    )
    retain_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="RetainAmount",
            type="Attribute",
            help="Amount retained by rail vendor for futute exchange/rail book at rail vendor site.",
        )
    )
    net_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="NetAmount",
            type="Attribute",
            help="Net total amount to be refunded or retained by the vendor.",
        )
    )


@dataclass
class RailSegmentRef:
    """
    Reference to a RaiLSegment
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class RailSpecificSeatAssignment:
    """
    Request object used to request a specific coach and seat number or a seat near-to a specific seat number.
    """

    coach_label: str = field(
        default=None,
        metadata=dict(
            name="CoachLabel",
            type="Attribute",
            help="The coach number of the train being requested.",
            required=True
        )
    )
    place_label: str = field(
        default=None,
        metadata=dict(
            name="PlaceLabel",
            type="Attribute",
            help="The actual seat number or the close-to seat number based on the Assignment.",
            required=True
        )
    )
    assignment: str = field(
        default=None,
        metadata=dict(
            name="Assignment",
            type="Attribute",
            help="Defines how the PlaceLabel should be applied. The values are 6.STP for actual seat or 2.STP for close-to seat. Default is 2.STP.",
            required=True
        )
    )
    rail_segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="RailSegmentRef",
            type="Attribute",
            help="The rail segment to which this assignment belongs.",
            required=True
        )
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="The BookingTraveler for this seat assignment.",
            required=True
        )
    )


@dataclass
class RailSupplier:
    code: TypeSupplierCode = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="2 character Rail distributor code.",
            required=True
        )
    )


@dataclass
class TicketAdvisory(StringLength1to500):
    """
    Additional ticket information.
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    language_code: str = field(
        default=None,
        metadata=dict(
            name="LanguageCode",
            type="Attribute",
            help="ISO 639 two-character language codes are used to retrieve specific information in the requested language. For Rich Content and Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE, DECH can also be used. Only certain services support this attribute. Providers: ACH, RCH, 1G, 1V, 1P, 1J.",
        )
    )


@dataclass
class TypeCoachClassType:
    """
    Values for accommodation class.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeJourneyDirection:
    """
    Outbound and Return directions.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeRailDirection:
    """
    The direction of travel.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeRailSegmentInfo:
    """
    Extra for ExtraSegmentInfo and Vendor for VendorMessages
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeRailTicketStatus:
    """
    Status Types for Ticket Info.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeResponseType:
    """
    Indicates the type of information to be returned in RailShopModifyAPIResponse. Values are “Schedules” or “Availability” or “Fares”. If not sent, “Fares” will be mapped if the request is for a specific rail segments, otherwise “Availability” will be mapped. Provider Supported RCH.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeTrainNumber:
    """
    The number that this train route operates under
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            max_length=8.0
        )
    )


@dataclass
class TypeTrainType:
    """
    Code for type of train used. Same as TrainServiceType
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            max_length=8.0
        )
    )


@dataclass
class TypeTransportMode:
    """
    Enumeration of all Train Transport Modes
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class Characteristic:
    """
    Defines coach characteristics such as accommodation class, smoking choice, etc.
    """

    smoking: bool = field(
        default="false",
        metadata=dict(
            name="Smoking",
            type="Attribute",
            help=None,
        )
    )
    class_value: TypeCoachClassType = field(
        default=None,
        metadata=dict(
            name="Class",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class RailFare(AttrElementKeyResults):
    """
    Information about this fare component
    """

    rail_fare_note_ref: List[RailFareNoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareNoteRef",
            type="Element",
            help="Key reference to RailFareNote present in RailFareNotList",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_validity: List[FareValidity] = field(
        default_factory=list,
        metadata=dict(
            name="FareValidity",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: HostToken = field(
        default=None,
        metadata=dict(
            name="HostToken",
            type="Element",
            help=None,
        )
    )
    ful_fillment_type: List[FulFillmentType] = field(
        default_factory=list,
        metadata=dict(
            name="FulFillmentType",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_fare_component: List[RailFareComponent] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareComponent",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    rail_fare_id: List[RailFareId] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareID",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_fare_idref: List[RailFareIdref] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareIDRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            help="The fare basis code or fare description for this fare",
        )
    )
    cabin_class: TypeRailCabin = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            help="The fare basis code or fare class for this fare",
            required=True
        )
    )
    passenger_type_code: TypePtc = field(
        default=None,
        metadata=dict(
            name="PassengerTypeCode",
            type="Attribute",
            help="The PTC that is associated with this fare. Default to ADT",
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="Returns the airport or city code that defines the origin market for this fare.",
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="Returns the airport or city code that defines the destination market for this fare.",
        )
    )
    effective_date: str = field(
        default=None,
        metadata=dict(
            name="EffectiveDate",
            type="Attribute",
            help="Returns the date on which this fare was quoted. Set as current date",
            required=True
        )
    )
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
        )
    )
    route_description: str = field(
        default=None,
        metadata=dict(
            name="RouteDescription",
            type="Attribute",
            help="Describes the route of the train fare.",
        )
    )
    ticket_type_code: str = field(
        default=None,
        metadata=dict(
            name="TicketTypeCode",
            type="Attribute",
            help="Describes the main identifier code of the fare.",
        )
    )
    fare_reference: str = field(
        default=None,
        metadata=dict(
            name="FareReference",
            type="Attribute",
            help="Unique reference for the fare that is required in RailExchangeQuote request.",
            min_length=1.0,
            max_length=32.0
        )
    )
    cross_city_fare: bool = field(
        default="false",
        metadata=dict(
            name="CrossCityFare",
            type="Attribute",
            help="Set to 'true' if the fare is valid across a Metropolitan Area, eg. Cross-London travel via the London Underground.",
        )
    )
    origin_station_name: str = field(
        default=None,
        metadata=dict(
            name="OriginStationName",
            type="Attribute",
            help="The origin station name for the Rail Fare.",
        )
    )
    destination_station_name: str = field(
        default=None,
        metadata=dict(
            name="DestinationStationName",
            type="Attribute",
            help="The destination station name for the Rail Fare.",
        )
    )
    reservation_required: bool = field(
        default=None,
        metadata=dict(
            name="ReservationRequired",
            type="Attribute",
            help="Set to true if a seat reservation is required while booking.",
        )
    )
    journey_direction: TypeJourneyDirection = field(
        default=None,
        metadata=dict(
            name="JourneyDirection",
            type="Attribute",
            help="The direction of the Journey (Outward or Return) associated with the Rail fare.",
        )
    )
    rail_loc_origin: TypeRailLocationCode = field(
        default=None,
        metadata=dict(
            name="RailLocOrigin",
            type="Attribute",
            help="RCH specific origin code (a.k.a UCodes) which uniquely identifies a train station.",
        )
    )
    rail_loc_destination: TypeRailLocationCode = field(
        default=None,
        metadata=dict(
            name="RailLocDestination",
            type="Attribute",
            help="RCH specific destination code (a.k.a UCodes) which uniquely identifies a train station.",
        )
    )


@dataclass
class RailFareIdlist:
    """
    The shared object list of FareIDs
    """

    rail_fare_id: List[RailFareId] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareID",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class RailFareNoteList:
    """
    The shared object list of Notes
    """

    rail_fare_note: List[RailFareNote] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareNote",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class RailInfo(AttrRailInfoOrgDesAndRailLoc):
    """
    Container for rail-related information required for retrieving a rail seat map/coach map
    """

    train_number: TypeTrainNumber = field(
        default=None,
        metadata=dict(
            name="TrainNumber",
            type="Attribute",
            help=None,
            required=True
        )
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
            required=True
        )
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class RailSearchModifiers:
    """
    Controls and switches for the Rail Availability Search request
    """

    preferred_suppliers: "RailSearchModifiers.PreferredSuppliers" = field(
        default=None,
        metadata=dict(
            name="PreferredSuppliers",
            type="Element",
            help=None,
        )
    )
    max_changes: int = field(
        default="2",
        metadata=dict(
            name="MaxChanges",
            type="Attribute",
            help="The maximum number of stops within a connection.",
            min_inclusive=0.0,
            max_inclusive=3.0
        )
    )
    direction: TypeRailDirection = field(
        default=None,
        metadata=dict(
            name="Direction",
            type="Attribute",
            help="The direction of travel.",
        )
    )
    class_value: str = field(
        default=None,
        metadata=dict(
            name="Class",
            type="Attribute",
            help=None,
        )
    )
    max_solutions: int = field(
        default="300",
        metadata=dict(
            name="MaxSolutions",
            type="Attribute",
            help="The maximum number of solutions to return. Decreasing this number",
        )
    )

    @dataclass
    class PreferredSuppliers:
        rail_supplier: List[RailSupplier] = field(
            default_factory=list,
            metadata=dict(
                name="RailSupplier",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class RailSegmentInfo(str):
    """
    Holds the ExtraSegmentInfo and VendorMessages from RCH response.
    """

    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="Supplier specific category.",
        )
    )
    type: TypeRailSegmentInfo = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Either Extra for ExtraSegmentInfo or Vendor for VendorMessages.",
            required=True
        )
    )


@dataclass
class RailTicketInfo:
    rail_journey_ref: List[RailJourneyRef] = field(
        default_factory=list,
        metadata=dict(
            name="RailJourneyRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    ticket_advisory: List[TicketAdvisory] = field(
        default_factory=list,
        metadata=dict(
            name="TicketAdvisory",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=10
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="Ticket number.",
            required=True,
            min_length=1.0,
            max_length=19.0
        )
    )
    issue_location: str = field(
        default=None,
        metadata=dict(
            name="IssueLocation",
            type="Attribute",
            help="Issue location is internal distributor code associated with the PCC.",
            min_length=0.0,
            max_length=128.0
        )
    )
    ticket_status: StringLength1to255 = field(
        default=None,
        metadata=dict(
            name="TicketStatus",
            type="Attribute",
            help="Status of Ticket.",
        )
    )
    ticket_form_type: str = field(
        default=None,
        metadata=dict(
            name="TicketFormType",
            type="Attribute",
            help="FormType of Ticket.",
            min_length=0.0,
            max_length=255.0
        )
    )
    traffic_type: StringLength1to255 = field(
        default=None,
        metadata=dict(
            name="TrafficType",
            type="Attribute",
            help="Type of traffic.",
        )
    )
    issued_date: str = field(
        default=None,
        metadata=dict(
            name="IssuedDate",
            type="Attribute",
            help="Ticket issue date.",
        )
    )
    ticket_type: StringLength1to255 = field(
        default=None,
        metadata=dict(
            name="TicketType",
            type="Attribute",
            help="Type of ticket. Paper, eTicket etc.",
        )
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="Reference to a BookingTraveler.",
        )
    )


@dataclass
class Coach:
    """
    Captures rail seat map/coach map information
    """

    characteristic: Characteristic = field(
        default=None,
        metadata=dict(
            name="Characteristic",
            type="Element",
            help=None,
        )
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata=dict(
            name="Remark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    coach_number: str = field(
        default=None,
        metadata=dict(
            name="CoachNumber",
            type="Attribute",
            help="Coach number for which seat map/coach map is returned.",
        )
    )


@dataclass
class RailFareList:
    """
    The shared object list of FareInfos
    """

    rail_fare: List[RailFare] = field(
        default_factory=list,
        metadata=dict(
            name="RailFare",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class RailPricingInfo(AttrPrices, AttrElementKeyResults):
    """
    Per traveler type pricing breakdown.
    """

    rail_booking_info: List[RailBookingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailBookingInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    passenger_type: List[TypePassengerType] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerType",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_fare: List[RailFare] = field(
        default_factory=list,
        metadata=dict(
            name="RailFare",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_fare_ref: List[RailFareRef] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    exchange_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ExchangeAmount",
            type="Attribute",
            help="The amount to pay to cover the exchange of the fare (includes penalties).",
        )
    )
    approximate_exchange_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ApproximateExchangeAmount",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class RailSegment(Segment):
    """
    Rail Segment
    """

    rail_segment_info: List[RailSegmentInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailSegmentInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    operating_company: OperatingCompany = field(
        default=None,
        metadata=dict(
            name="OperatingCompany",
            type="Element",
            help=None,
        )
    )
    rail_avail_info: List[RailAvailInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailAvailInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    ful_fillment_type: List[FulFillmentType] = field(
        default_factory=list,
        metadata=dict(
            name="FulFillmentType",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    train_number: TypeTrainNumber = field(
        default=None,
        metadata=dict(
            name="TrainNumber",
            type="Attribute",
            help=None,
        )
    )
    train_type: str = field(
        default=None,
        metadata=dict(
            name="TrainType",
            type="Attribute",
            help="Type of train used. Same as TrainServiceType.",
        )
    )
    train_type_code: TypeTrainType = field(
        default=None,
        metadata=dict(
            name="TrainTypeCode",
            type="Attribute",
            help="Code for type of train used. Same as TrainServiceType.",
        )
    )
    transport_mode: TypeTransportMode = field(
        default=None,
        metadata=dict(
            name="TransportMode",
            type="Attribute",
            help="Type of Transport Mode used.",
        )
    )
    seat_assignable: bool = field(
        default=None,
        metadata=dict(
            name="SeatAssignable",
            type="Attribute",
            help="Set to true if there exists seats to be booked",
        )
    )
    transport_code: str = field(
        default=None,
        metadata=dict(
            name="TransportCode",
            type="Attribute",
            help="Supplier specific train code",
        )
    )
    reservation_required: bool = field(
        default=None,
        metadata=dict(
            name="ReservationRequired",
            type="Attribute",
            help="Set to true if a reservation is required for booking.",
        )
    )
    travel_time: int = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute",
            help="Total time spent (minutes) traveling",
        )
    )
    host_token_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="HostTokenRef",
            type="Attribute",
            help="The reference key for the host token. From the HostTokenList Providers RCH.",
        )
    )
    cabin_class: TypeRailCabin = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            help="Rail Cabin class specification. The valid values are Economy, Business, First and Other",
        )
    )
    class_code: TypeRailClass = field(
        default=None,
        metadata=dict(
            name="ClassCode",
            type="Attribute",
            help="A booking code or fare basis code or fare class.",
        )
    )


@dataclass
class RailJourney(AttrRailSegmentOrigDestInfo, AttrPrices, AttrProviderSupplier, AttrElementKeyResults):
    """
    Captures all journey-related data
    """

    journey_remark: List[JourneyRemark] = field(
        default_factory=list,
        metadata=dict(
            name="JourneyRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_segment: List[RailSegment] = field(
        default_factory=list,
        metadata=dict(
            name="RailSegment",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    rail_segment_ref: List[RailSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="RailSegmentRef",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    route_description: str = field(
        default=None,
        metadata=dict(
            name="RouteDescription",
            type="Attribute",
            help="The description of the route.",
            max_length=255.0
        )
    )
    journey_direction: TypeJourneyDirection = field(
        default=None,
        metadata=dict(
            name="JourneyDirection",
            type="Attribute",
            help="The direction of the Journey (Outward or Return).",
        )
    )
    journey_duration: int = field(
        default=None,
        metadata=dict(
            name="JourneyDuration",
            type="Attribute",
            help="The duration of the entire Journey in minutes",
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help="Status of this Journey.",
        )
    )
    provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    passive_provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="PassiveProviderReservationInfoRef",
            type="Attribute",
            help="Passive provider reservation reference key.",
        )
    )
    travel_order: int = field(
        default=None,
        metadata=dict(
            name="TravelOrder",
            type="Attribute",
            help="To identify the appropriate travel sequence for Air/Car/Hotel/Rail segments/reservations/Journeys based on travel dates. This ordering is applicable across the UR not provider or traveler specific",
        )
    )
    route_reference: str = field(
        default=None,
        metadata=dict(
            name="RouteReference",
            type="Attribute",
            help="RouteReference is required in seat assignment purpose",
            min_length=0.0,
            max_length=255.0
        )
    )
    operation: str = field(
        default=None,
        metadata=dict(
            name="Operation",
            type="Attribute",
            help="'Type of exchange. Add - Add new Journey. Update - Modify existing Journey. Delete - Remove existing Journey'",
        )
    )


@dataclass
class RailSegmentList:
    """
    List of Rail Segments
    """

    rail_segment: List[RailSegment] = field(
        default_factory=list,
        metadata=dict(
            name="RailSegment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class RailJourneyList:
    """
    List of Rail Journeys
    """

    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata=dict(
            name="RailJourney",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class RailReservation(BaseReservation):
    """
    The parent container for all Rail booking data
    """

    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=9
        )
    )
    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata=dict(
            name="RailJourney",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    rail_pricing_info: List[RailPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailPricingInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_ticket_info: List[RailTicketInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailTicketInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_fare_note_list: RailFareNoteList = field(
        default=None,
        metadata=dict(
            name="RailFareNoteList",
            type="Element",
            help="List of RailFareNote(s) that is referenced by key in RailFare.",
        )
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_status: str = field(
        default=None,
        metadata=dict(
            name="BookingStatus",
            type="Attribute",
            help="The Current Status of the rail booking.",
            required=True
        )
    )


@dataclass
class SearchRailLeg:
    """
    Holds Origin, Destination, and Departure times for a Rail Leg to search for.
    """

    search_origin: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata=dict(
            name="SearchOrigin",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    search_destination: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata=dict(
            name="SearchDestination",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    rail_segment_list: RailSegmentList = field(
        default=None,
        metadata=dict(
            name="RailSegmentList",
            type="Element",
            help=None,
        )
    )
    rail_leg_modifiers: RailLegModifiers = field(
        default=None,
        metadata=dict(
            name="RailLegModifiers",
            type="Element",
            help=None,
        )
    )
    search_dep_time: List[TypeFlexibleTimeSpec] = field(
        default_factory=list,
        metadata=dict(
            name="SearchDepTime",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    search_arv_time: List[TypeTimeSpec] = field(
        default_factory=list,
        metadata=dict(
            name="SearchArvTime",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class TypeRailPricingSolution(AttrPrices):
    """
    Common RailPricingSolution container
    """

    rail_pricing_info: List[RailPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailPricingInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata=dict(
            name="RailJourney",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    rail_journey_ref: List[RailJourneyRef] = field(
        default_factory=list,
        metadata=dict(
            name="RailJourneyRef",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    offer_id: int = field(
        default=None,
        metadata=dict(
            name="OfferId",
            type="Attribute",
            help="OfferID must be included if the RailCreateReq contains a price. If the RailCreateReq is used for the Direct Book function, the OfferID is not included.",
        )
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
            required=True
        )
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help=None,
            required=True
        )
    )
    host_token_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="HostTokenRef",
            type="Attribute",
            help="HostTokenRef will reference the value in HostTokenList/HostToken @ Key",
        )
    )
    reference: str = field(
        default=None,
        metadata=dict(
            name="Reference",
            type="Attribute",
            help="Offer Reference required for Booking(eg.TL).",
        )
    )


@dataclass
class RailExchangeSolution(TypeRailPricingSolution):
    """
    Contains the fares and segments for a particular offer.
    """

    rail_exchange_info: RailExchangeInfo = field(
        default=None,
        metadata=dict(
            name="RailExchangeInfo",
            type="Element",
            help=None,
        )
    )


@dataclass
class RailPricingSolution(TypeRailPricingSolution):
    """
    Contains the fares and segments for a particular offer.
    """

    pass


@dataclass
class RailSolutionChangedInfo:
    """
    If RetainReservation is None, this will contain the new values returned from the provider. If RetainReservation is Price, Schedule, or Both and there is a price/schedule change, this will contain the new values that were returned from the provider. If RetainReservation is Price, Schedule, or Both and there isn’t a price/schedule change, this element will not be returned.
    """

    rail_pricing_solution: RailPricingSolution = field(
        default=None,
        metadata=dict(
            name="RailPricingSolution",
            type="Element",
            help=None,
            required=True
        )
    )
    reason_code: str = field(
        default=None,
        metadata=dict(
            name="ReasonCode",
            type="Attribute",
            help=None,
            required=True
        )
    )