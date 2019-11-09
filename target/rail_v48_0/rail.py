from dataclasses import dataclass, field
from typing import List


@dataclass
class FareValidity:
    """
    Associates fare validity dates with journeys.
    """

    rail_journey_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "RailJourneyRef",
            "type": "Attribute",
            "help": "Reference to a journey to which this fare validity refers.",
        },
    )
    not_valid_before: str = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
            "help": "Fare not valid before this date.",
        },
    )
    not_valid_after: str = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
            "help": "Fare not valid after this date.",
        },
    )


@dataclass
class FulFillmentType:
    """
    Fulfillment options for this segment. the options will be one of "Ticket on Departure", "Ticketless", "Ticket By Email", "Travel Agency"
    """

    value: str = field(
        default=None,
        metadata={
            "min_length": "0",
            "max_length": "255",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class JourneyRemark:
    """
    A Remark for a Journey.
    """

    category: str = field(
        default=None, metadata={"name": "Category", "type": "Attribute"}
    )


@dataclass
class OperatingCompany:
    """
    A textual remark identifying the OperatingCompany/Train Service other than BN orTL
    """

    code: str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "help": "Company Short Text",
        },
    )
    name: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Name",
            "type": "Attribute",
            "help": "Name Identifying the Train Service other than BN orTL",
        },
    )


@dataclass
class RailAutoSeatAssignment:
    """
    Request object used to request seats automatically by seat type
    """

    seat_type: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "SeatType",
            "type": "Attribute",
            "help": "Indicates codeset of values such as Seat Type like Place,Position, Smoking Choice, Place Arrangement, Place Direction, Compartment.",
        },
    )
    seat_value: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "SeatValue",
            "type": "Attribute",
            "help": "Indicates the value specific to the selected type.",
        },
    )
    rail_segment_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
            "type": "Attribute",
            "help": "The rail segment that this assignment belongs to",
        },
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "help": "The booking traveler that this seat assignment is for. If not entered, this applies to the primary booking traveler and other passengers are adjacent.",
        },
    )


@dataclass
class RailAvailInfo:
    class_code: TypeRailClass = field(
        default=None,
        metadata={
            "name": "ClassCode",
            "type": "Attribute",
            "help": "A booking code or fare basis code or fare class.",
        },
    )
    quantity: int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
            "help": "Available fare basis code or fare class quantity.",
        },
    )
    cabin_class: TypeRailCabin = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "help": "The fare basis code or fare class for this fare.",
        },
    )


@dataclass
class RailBookingInfo:
    """
    Links journeys and fares together
    """

    rail_fare_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "RailFareRef",
            "type": "Attribute",
            "help": "Reference to a fare that applies to the journey below.",
        },
    )
    rail_journey_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "RailJourneyRef",
            "type": "Attribute",
            "help": "Reference to a journeys on which the above fare applies.",
        },
    )
    optional_service: bool = field(
        default=false,
        metadata={
            "name": "OptionalService",
            "type": "Attribute",
            "help": "Indicate the OfferFareItem elements will be Optional or not.",
        },
    )


@dataclass
class RailExchangeInfo:
    """
    Exchange information for the rail booking.
    """

    refund_amount: TypeMoney = field(
        default=None, metadata={"name": "RefundAmount", "type": "Attribute"}
    )
    cancellation_fee: TypeMoney = field(
        default=None, metadata={"name": "CancellationFee", "type": "Attribute"}
    )
    exchange_amount: TypeMoney = field(
        default=None, metadata={"name": "ExchangeAmount", "type": "Attribute"}
    )
    approximate_refund_amount: TypeMoney = field(
        default=None,
        metadata={"name": "ApproximateRefundAmount", "type": "Attribute"},
    )
    approximate_cancellation_fee: TypeMoney = field(
        default=None,
        metadata={"name": "ApproximateCancellationFee", "type": "Attribute"},
    )
    approximate_exchange_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "ApproximateExchangeAmount",
            "type": "Attribute",
            "help": "The Converted total price in Default Currency for this entity including base price and all taxes.",
        },
    )
    retain_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "RetainAmount",
            "type": "Attribute",
            "help": "Amount retained by a rail vendor for future use at the vendor’s site.",
        },
    )


@dataclass
class RailFareComponent:
    """
    Contains fare and discount information for each passenger type
    """

    discount: List["Discount"] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "Discount",
            "type": "Element",
            "help": "Discount information specific to the fare component",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "help": "FareComponent amount",
        },
    )
    age: int = field(
        default=None, metadata={"name": "Age", "type": "Attribute"}
    )
    passenger_type_code: TypePtc = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "help": "The three character passenger code",
        },
    )
    supplier_passenger_type: str = field(
        default=None,
        metadata={
            "name": "SupplierPassengerType",
            "type": "Attribute",
            "help": "Supplier passenger type code",
        },
    )
    quantity: int = field(
        default=None, metadata={"name": "Quantity", "type": "Attribute"}
    )

    @dataclass
    class Discount:
        discount_card: List[DiscountCard] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 9,
                "name": "DiscountCard",
                "type": "Element",
            },
        )
        key: TypeRef = field(
            default=None, metadata={"name": "Key", "type": "Attribute"}
        )


@dataclass
class RailFareId:
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    category: str = field(
        default=None, metadata={"name": "Category", "type": "Attribute"}
    )


@dataclass
class RailFareIdref:
    """
    Reference to a complete FareID from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class RailFareNote:
    """
    A simple textual fare note. Used within several other objects.
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    note_name: str = field(
        default=None,
        metadata={"required": True, "name": "NoteName", "type": "Attribute"},
    )


@dataclass
class RailFareNoteRef:
    """
    A reference to a fare note from a shared list. Used to minimize xml results.
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class RailFareRef:
    """
    Reference to a complete FareInfo from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class RailJourneyRef:
    """
    Reference to a RailJourney
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class RailLegModifiers:
    permitted_connection_points: "PermittedConnectionPoints" = field(
        default=None,
        metadata={"name": "PermittedConnectionPoints", "type": "Element"},
    )
    prohibited_connection_points: "ProhibitedConnectionPoints" = field(
        default=None,
        metadata={"name": "ProhibitedConnectionPoints", "type": "Element"},
    )
    class_value: str = field(
        default=None, metadata={"name": "Class", "type": "Attribute"}
    )

    @dataclass
    class ProhibitedConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "ConnectionPoint",
                "type": "Element",
            },
        )

    @dataclass
    class PermittedConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "ConnectionPoint",
                "type": "Element",
            },
        )


@dataclass
class RailPricingModifiers:
    """
    Search flexibiity criteria .
    """

    discount_card: List[DiscountCard] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "DiscountCard",
            "type": "Element",
            "help": "Discount request for rail.",
        },
    )
    prohibit_non_refundable_fares: bool = field(
        default=false,
        metadata={
            "name": "ProhibitNonRefundableFares",
            "type": "Attribute",
            "help": "Indicates whether it prohibits NonRefundable Fares.",
        },
    )
    prohibit_non_exchangeable_fares: bool = field(
        default=false,
        metadata={
            "name": "ProhibitNonExchangeableFares",
            "type": "Attribute",
            "help": "Indicates whether it prohibits NonExchangeable Fares .",
        },
    )
    currency_type: TypeCurrency = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "help": "3 Letter Currency Code",
        },
    )
    rail_search_type: TypeRailSearchType = field(
        default=None,
        metadata={
            "name": "RailSearchType",
            "type": "Attribute",
            "help": 'RailSearchType options are "All Fares" "Fastest" "Lowest Fare" "One Fare Per Class" "Seasons". Supported by NTV/VF only for "All Fares" "Lowest Fare" and "One Fare Per Class". Provider : RCH',
        },
    )


@dataclass
class RailRefundInfo:
    """
    Information about refund.
    """

    refund_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
            "help": "Amount refunded back to customer.",
        },
    )
    cancellation_fee: TypeMoney = field(
        default=None,
        metadata={
            "name": "CancellationFee",
            "type": "Attribute",
            "help": "Cancellation penalty imposed by the distributor.",
        },
    )
    refund: bool = field(
        default=None,
        metadata={
            "name": "Refund",
            "type": "Attribute",
            "help": "Indicates whether vendor offers refund on rail reservation.",
        },
    )
    retain: bool = field(
        default=None,
        metadata={
            "name": "Retain",
            "type": "Attribute",
            "help": "Indicates whether vendor retains the amount to be used later.",
        },
    )
    retain_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "RetainAmount",
            "type": "Attribute",
            "help": "Amount retained by rail vendor for futute exchange/rail book at rail vendor site.",
        },
    )
    net_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "NetAmount",
            "type": "Attribute",
            "help": "Net total amount to be refunded or retained by the vendor.",
        },
    )


@dataclass
class RailSegmentRef:
    """
    Reference to a RaiLSegment
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class RailSpecificSeatAssignment:
    """
    Request object used to request a specific coach and seat number or a seat near-to a specific seat number.
    """

    coach_label: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "CoachLabel",
            "type": "Attribute",
            "help": "The coach number of the train being requested.",
        },
    )
    place_label: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "PlaceLabel",
            "type": "Attribute",
            "help": "The actual seat number or the close-to seat number based on the Assignment.",
        },
    )
    assignment: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Assignment",
            "type": "Attribute",
            "help": "Defines how the PlaceLabel should be applied. The values are \x936.STP\x94 for actual seat or \x932.STP\x94 for close-to seat. Default is 2.STP.",
        },
    )
    rail_segment_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "RailSegmentRef",
            "type": "Attribute",
            "help": "The rail segment to which this assignment belongs.",
        },
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "help": "The BookingTraveler for this seat assignment.",
        },
    )


@dataclass
class RailSupplier:
    code: TypeSupplierCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Code",
            "type": "Attribute",
            "help": "2 character Rail distributor code.",
        },
    )


@dataclass
class TicketAdvisory:
    """
    Additional ticket information.
    """

    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )
    language_code: Language = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Attribute",
            "help": "ISO 639 two-character language codes are used to retrieve specific information in the requested language. For Rich Content and Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE, DECH can also be used. Only certain services support this attribute. Providers: ACH, RCH, 1G, 1V, 1P, 1J.",
        },
    )


@dataclass
class TypeCoachClassType:
    """
    Values for accommodation class.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeJourneyDirection:
    """
    Outbound and Return directions.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeRailDirection:
    """
    The direction of travel.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeRailSegmentInfo:
    """
    Extra for ExtraSegmentInfo and Vendor for VendorMessages
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeRailTicketStatus:
    """
    Status Types for Ticket Info.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeResponseType:
    """
    Indicates the type of information to be returned in RailShopModifyAPIResponse. Values are “Schedules” or “Availability” or “Fares”. If not sent, “Fares” will be mapped if the request is for a specific rail segments, otherwise “Availability” will be mapped. Provider Supported RCH.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeTrainNumber:
    """
    The number that this train route operates under
    """

    value: str = field(
        default=None,
        metadata={
            "min_length": "1",
            "max_length": "8",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class TypeTrainType:
    """
    Code for type of train used. Same as TrainServiceType
    """

    value: str = field(
        default=None,
        metadata={
            "min_length": "1",
            "max_length": "8",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class TypeTransportMode:
    """
    Enumeration of all Train Transport Modes
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class Characteristic:
    """
    Defines coach characteristics such as accommodation class, smoking choice, etc.
    """

    smoking: bool = field(
        default=false, metadata={"name": "Smoking", "type": "Attribute"}
    )
    class_value: TypeCoachClassType = field(
        default=None, metadata={"name": "Class", "type": "Attribute"}
    )


@dataclass
class RailFare:
    """
    Information about this fare component
    """

    rail_fare_note_ref: List[RailFareNoteRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailFareNoteRef",
            "type": "Element",
            "help": "Key reference to RailFareNote present in RailFareNotList",
        },
    )
    fare_validity: List[FareValidity] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareValidity",
            "type": "Element",
        },
    )
    host_token: HostToken = field(
        default=None, metadata={"name": "HostToken", "type": "Element"}
    )
    ful_fillment_type: List[FulFillmentType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FulFillmentType",
            "type": "Element",
        },
    )
    rail_fare_component: List[RailFareComponent] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "RailFareComponent",
            "type": "Element",
        },
    )
    rail_fare_id: List[RailFareId] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailFareID",
            "type": "Element",
        },
    )
    rail_fare_idref: List[RailFareIdref] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailFareIDRef",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    fare_basis: str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "help": "The fare basis code or fare description for this fare",
        },
    )
    cabin_class: TypeRailCabin = field(
        default=None,
        metadata={
            "required": True,
            "name": "CabinClass",
            "type": "Attribute",
            "help": "The fare basis code or fare class for this fare",
        },
    )
    passenger_type_code: TypePtc = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "help": "The PTC that is associated with this fare. Default to ADT",
        },
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "help": "Returns the airport or city code that defines the origin market for this fare.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "help": "Returns the airport or city code that defines the destination market for this fare.",
        },
    )
    effective_date: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "EffectiveDate",
            "type": "Attribute",
            "help": "Returns the date on which this fare was quoted. Set as current date",
        },
    )
    amount: TypeMoney = field(
        default=None, metadata={"name": "Amount", "type": "Attribute"}
    )
    route_description: str = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Attribute",
            "help": "Describes the route of the train fare.",
        },
    )
    ticket_type_code: str = field(
        default=None,
        metadata={
            "name": "TicketTypeCode",
            "type": "Attribute",
            "help": "Describes the main identifier code of the fare.",
        },
    )
    fare_reference: str = field(
        default=None,
        metadata={
            "name": "FareReference",
            "type": "Attribute",
            "help": "Unique reference for the fare that is required in RailExchangeQuote request.",
        },
    )
    cross_city_fare: bool = field(
        default=false,
        metadata={
            "name": "CrossCityFare",
            "type": "Attribute",
            "help": "Set to 'true' if the fare is valid across a Metropolitan Area, eg. Cross-London travel via the London Underground.",
        },
    )
    origin_station_name: str = field(
        default=None,
        metadata={
            "name": "OriginStationName",
            "type": "Attribute",
            "help": "The origin station name for the Rail Fare.",
        },
    )
    destination_station_name: str = field(
        default=None,
        metadata={
            "name": "DestinationStationName",
            "type": "Attribute",
            "help": "The destination station name for the Rail Fare.",
        },
    )
    reservation_required: bool = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Attribute",
            "help": "Set to true if a seat reservation is required while booking.",
        },
    )
    journey_direction: TypeJourneyDirection = field(
        default=None,
        metadata={
            "name": "JourneyDirection",
            "type": "Attribute",
            "help": "The direction of the Journey (Outward or Return) associated with the Rail fare.",
        },
    )
    rail_loc_origin: TypeRailLocationCode = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "help": "RCH specific origin code (a.k.a UCodes) which uniquely identifies a train station.",
        },
    )
    rail_loc_destination: TypeRailLocationCode = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "help": "RCH specific destination code (a.k.a UCodes) which uniquely identifies a train station.",
        },
    )


@dataclass
class RailFareIdlist:
    """
    The shared object list of FareIDs
    """

    rail_fare_id: List[RailFareId] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "RailFareID",
            "type": "Element",
        },
    )


@dataclass
class RailFareNoteList:
    """
    The shared object list of Notes
    """

    rail_fare_note: List[RailFareNote] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailFareNote",
            "type": "Element",
        },
    )


@dataclass
class RailInfo:
    """
    Container for rail-related information required for retrieving a rail seat map/coach map
    """

    train_number: TypeTrainNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "TrainNumber",
            "type": "Attribute",
        },
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderCode",
            "type": "Attribute",
        },
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "SupplierCode",
            "type": "Attribute",
        },
    )


@dataclass
class RailSearchModifiers:
    """
    Controls and switches for the Rail Availability Search request
    """

    preferred_suppliers: "PreferredSuppliers" = field(
        default=None,
        metadata={"name": "PreferredSuppliers", "type": "Element"},
    )
    max_changes: int = field(
        default=2,
        metadata={
            "name": "MaxChanges",
            "type": "Attribute",
            "help": "The maximum number of stops within a connection.",
        },
    )
    direction: TypeRailDirection = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
            "help": "The direction of travel.",
        },
    )
    class_value: str = field(
        default=None, metadata={"name": "Class", "type": "Attribute"}
    )
    max_solutions: int = field(
        default=300,
        metadata={
            "name": "MaxSolutions",
            "type": "Attribute",
            "help": "The maximum number of solutions to return. Decreasing this number",
        },
    )

    @dataclass
    class PreferredSuppliers:
        rail_supplier: List[RailSupplier] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "RailSupplier",
                "type": "Element",
            },
        )


@dataclass
class RailSegmentInfo:
    """
    Holds the ExtraSegmentInfo and VendorMessages from RCH response.
    """

    category: str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "help": "Supplier specific category.",
        },
    )
    type: TypeRailSegmentInfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Attribute",
            "help": "Either Extra for ExtraSegmentInfo or Vendor for VendorMessages.",
        },
    )


@dataclass
class RailTicketInfo:
    rail_journey_ref: List[RailJourneyRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailJourneyRef",
            "type": "Element",
        },
    )
    ticket_advisory: List[TicketAdvisory] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 10,
            "name": "TicketAdvisory",
            "type": "Element",
        },
    )
    number: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Number",
            "type": "Attribute",
            "help": "Ticket number.",
        },
    )
    issue_location: str = field(
        default=None,
        metadata={
            "name": "IssueLocation",
            "type": "Attribute",
            "help": "Issue location is internal distributor code associated with the PCC.",
        },
    )
    ticket_status: StringLength1to255 = field(
        default=None,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
            "help": "Status of Ticket.",
        },
    )
    ticket_form_type: str = field(
        default=None,
        metadata={
            "name": "TicketFormType",
            "type": "Attribute",
            "help": "FormType of Ticket.",
        },
    )
    traffic_type: StringLength1to255 = field(
        default=None,
        metadata={
            "name": "TrafficType",
            "type": "Attribute",
            "help": "Type of traffic.",
        },
    )
    issued_date: DateTime = field(
        default=None,
        metadata={
            "name": "IssuedDate",
            "type": "Attribute",
            "help": "Ticket issue date.",
        },
    )
    ticket_type: StringLength1to255 = field(
        default=None,
        metadata={
            "name": "TicketType",
            "type": "Attribute",
            "help": "Type of ticket. Paper, eTicket etc.",
        },
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "help": "Reference to a BookingTraveler.",
        },
    )


@dataclass
class Coach:
    """
    Captures rail seat map/coach map information
    """

    characteristic: Characteristic = field(
        default=None, metadata={"name": "Characteristic", "type": "Element"}
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Remark",
            "type": "Element",
        },
    )
    coach_number: str = field(
        default=None,
        metadata={
            "name": "CoachNumber",
            "type": "Attribute",
            "help": "Coach number for which seat map/coach map is returned.",
        },
    )


@dataclass
class RailFareList:
    """
    The shared object list of FareInfos
    """

    rail_fare: List[RailFare] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "RailFare",
            "type": "Element",
        },
    )


@dataclass
class RailPricingInfo:
    """
    Per traveler type pricing breakdown.
    """

    rail_booking_info: List[RailBookingInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailBookingInfo",
            "type": "Element",
        },
    )
    passenger_type: List[TypePassengerType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "PassengerType",
            "type": "Element",
        },
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BookingTravelerRef",
            "type": "Element",
        },
    )
    rail_fare: List[RailFare] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailFare",
            "type": "Element",
        },
    )
    rail_fare_ref: List[RailFareRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailFareRef",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    exchange_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
            "help": "The amount to pay to cover the exchange of the fare (includes penalties).",
        },
    )
    approximate_exchange_amount: TypeMoney = field(
        default=None,
        metadata={"name": "ApproximateExchangeAmount", "type": "Attribute"},
    )


@dataclass
class RailSegment(CommonSegment):
    """
    Rail Segment
    """

    rail_segment_info: List[RailSegmentInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailSegmentInfo",
            "type": "Element",
        },
    )
    operating_company: OperatingCompany = field(
        default=None, metadata={"name": "OperatingCompany", "type": "Element"}
    )
    rail_avail_info: List[RailAvailInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailAvailInfo",
            "type": "Element",
        },
    )
    ful_fillment_type: List[FulFillmentType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FulFillmentType",
            "type": "Element",
        },
    )
    train_number: TypeTrainNumber = field(
        default=None, metadata={"name": "TrainNumber", "type": "Attribute"}
    )
    train_type: str = field(
        default=None,
        metadata={
            "name": "TrainType",
            "type": "Attribute",
            "help": "Type of train used. Same as TrainServiceType.",
        },
    )
    train_type_code: TypeTrainType = field(
        default=None,
        metadata={
            "name": "TrainTypeCode",
            "type": "Attribute",
            "help": "Code for type of train used. Same as TrainServiceType.",
        },
    )
    transport_mode: TypeTransportMode = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Attribute",
            "help": "Type of Transport Mode used.",
        },
    )
    seat_assignable: bool = field(
        default=None,
        metadata={
            "name": "SeatAssignable",
            "type": "Attribute",
            "help": "Set to true if there exists seats to be booked",
        },
    )
    transport_code: str = field(
        default=None,
        metadata={
            "name": "TransportCode",
            "type": "Attribute",
            "help": "Supplier specific train code",
        },
    )
    reservation_required: bool = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Attribute",
            "help": "Set to true if a reservation is required for booking.",
        },
    )
    travel_time: int = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
            "help": "Total time spent (minutes) traveling",
        },
    )
    host_token_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
            "help": "The reference key for the host token. From the HostTokenList Providers RCH.",
        },
    )
    cabin_class: TypeRailCabin = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "help": "Rail Cabin class specification. The valid values are Economy, Business, First and Other",
        },
    )
    class_code: TypeRailClass = field(
        default=None,
        metadata={
            "name": "ClassCode",
            "type": "Attribute",
            "help": "A booking code or fare basis code or fare class.",
        },
    )


@dataclass
class RailJourney:
    """
    Captures all journey-related data
    """

    journey_remark: List[JourneyRemark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "JourneyRemark",
            "type": "Element",
        },
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "HostToken",
            "type": "Element",
        },
    )
    rail_segment: List[RailSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "RailSegment",
            "type": "Element",
        },
    )
    rail_segment_ref: List[RailSegmentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "RailSegmentRef",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    route_description: str = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Attribute",
            "help": "The description of the route.",
        },
    )
    journey_direction: TypeJourneyDirection = field(
        default=None,
        metadata={
            "name": "JourneyDirection",
            "type": "Attribute",
            "help": "The direction of the Journey (Outward or Return).",
        },
    )
    journey_duration: int = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
            "type": "Attribute",
            "help": "The duration of the entire Journey in minutes",
        },
    )
    status: str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "help": "Status of this Journey.",
        },
    )
    provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
            "help": "Provider reservation reference key.",
        },
    )
    passive_provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
            "help": "Passive provider reservation reference key.",
        },
    )
    travel_order: int = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
            "help": "To identify the appropriate travel sequence for Air/Car/Hotel/Rail segments/reservations/Journeys based on travel dates. This ordering is applicable across the UR not provider or traveler specific",
        },
    )
    route_reference: str = field(
        default=None,
        metadata={
            "name": "RouteReference",
            "type": "Attribute",
            "help": "RouteReference is required in seat assignment purpose",
        },
    )
    operation: str = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Attribute",
            "help": '"Type of exchange. Add - Add new Journey. Update - Modify existing Journey. Delete - Remove existing Journey"',
        },
    )


@dataclass
class RailSegmentList:
    """
    List of Rail Segments
    """

    rail_segment: List[RailSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailSegment",
            "type": "Element",
        },
    )


@dataclass
class RailJourneyList:
    """
    List of Rail Journeys
    """

    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailJourney",
            "type": "Element",
        },
    )


@dataclass
class RailReservation(CommonBaseReservation):
    """
    The parent container for all Rail booking data
    """

    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 9,
            "name": "BookingTravelerRef",
            "type": "Element",
        },
    )
    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "RailJourney",
            "type": "Element",
        },
    )
    rail_pricing_info: List[RailPricingInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailPricingInfo",
            "type": "Element",
        },
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Payment",
            "type": "Element",
        },
    )
    rail_ticket_info: List[RailTicketInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailTicketInfo",
            "type": "Element",
        },
    )
    rail_fare_note_list: RailFareNoteList = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
            "help": "List of RailFareNote(s) that is referenced by key in RailFare.",
        },
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SupplierLocator",
            "type": "Element",
        },
    )
    booking_status: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "BookingStatus",
            "type": "Attribute",
            "help": "The Current Status of the rail booking.",
        },
    )


@dataclass
class SearchRailLeg:
    """
    Holds Origin, Destination, and Departure times for a Rail Leg to search for.
    """

    search_origin: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "SearchOrigin",
            "type": "Element",
        },
    )
    search_destination: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "SearchDestination",
            "type": "Element",
        },
    )
    rail_segment_list: RailSegmentList = field(
        default=None, metadata={"name": "RailSegmentList", "type": "Element"}
    )
    rail_leg_modifiers: RailLegModifiers = field(
        default=None, metadata={"name": "RailLegModifiers", "type": "Element"}
    )
    search_dep_time: List[TypeFlexibleTimeSpec] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "SearchDepTime",
            "type": "Element",
        },
    )
    search_arv_time: List[TypeTimeSpec] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "SearchArvTime",
            "type": "Element",
        },
    )


@dataclass
class TypeRailPricingSolution:
    """
    Common RailPricingSolution container
    """

    rail_pricing_info: List[RailPricingInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailPricingInfo",
            "type": "Element",
        },
    )
    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "RailJourney",
            "type": "Element",
        },
    )
    rail_journey_ref: List[RailJourneyRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "RailJourneyRef",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    offer_id: int = field(
        default=None,
        metadata={
            "name": "OfferId",
            "type": "Attribute",
            "help": "OfferID must be included if the RailCreateReq contains a price. If the RailCreateReq is used for the Direct Book function, the OfferID is not included.",
        },
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderCode",
            "type": "Attribute",
        },
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "SupplierCode",
            "type": "Attribute",
        },
    )
    host_token_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
            "help": "HostTokenRef will reference the value in HostTokenList/HostToken @ Key",
        },
    )
    reference: str = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Attribute",
            "help": "Offer Reference required for Booking(eg.TL).",
        },
    )


@dataclass
class RailExchangeSolution(TypeRailPricingSolution):
    """
    Contains the fares and segments for a particular offer.
    """

    rail_exchange_info: RailExchangeInfo = field(
        default=None, metadata={"name": "RailExchangeInfo", "type": "Element"}
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
        metadata={
            "required": True,
            "name": "RailPricingSolution",
            "type": "Element",
        },
    )
    reason_code: str = field(
        default=None,
        metadata={"required": True, "name": "ReasonCode", "type": "Attribute"},
    )
