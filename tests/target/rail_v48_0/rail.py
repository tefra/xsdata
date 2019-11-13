from dataclasses import dataclass, field
from typing import List

from ..common_v48_0.common import *


@dataclass
class AttrRailInfoOrgDesAndRailLoc:
    """Basic attributes used to describe an origin destination pair.

    :ivar origin: The IATA location code for this origination of this entity.
    :ivar rail_loc_origin: RCH specific origin code (a.k.a UCodes) which uniquely identifies a train station.
    :ivar destination: The IATA location code for this destination of this entity.
    :ivar rail_loc_destination: RCH specific destination code (a.k.a UCodes) which uniquely identifies a train station.
    :ivar departure_time: The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.
    :ivar arrival_time: The date and time at which this entity arrives at the destination. This does not include time zone information since it can be derived from the origin location.
    """
    origin: str = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    rail_loc_origin: str = field(
        default=None,
        metadata=dict(
            name="RailLocOrigin",
            type="Attribute",
            min_length=3.0,
            max_length=8.0,
            white_space="collapse"
        )
    )
    destination: str = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    rail_loc_destination: str = field(
        default=None,
        metadata=dict(
            name="RailLocDestination",
            type="Attribute",
            min_length=3.0,
            max_length=8.0,
            white_space="collapse"
        )
    )
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            required=True
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute"
        )
    )


@dataclass
class AttrRailOrigDestInfo:
    """Holds all relevant origin/destination and departure/arrival details.

    :ivar origin_station_name: The origin station name for the Journey.
    :ivar destination_station_name: The destination station name for the Journey.
    """
    origin_station_name: str = field(
        default=None,
        metadata=dict(
            name="OriginStationName",
            type="Attribute"
        )
    )
    destination_station_name: str = field(
        default=None,
        metadata=dict(
            name="DestinationStationName",
            type="Attribute"
        )
    )


@dataclass
class AttrRailSegmentOrigDestInfo:
    """Holds all relevant origin/destination and departure/arrival details.

    :ivar origin: The IATA location code for this origination of this entity.
    :ivar destination: The IATA location code for this destination of this entity.
    :ivar departure_time: The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.
    :ivar arrival_time: The date and time at which this entity arrives at the destination. This does not include time zone information since it can be derived from the origin location.
    :ivar origin_station_name: The origin station name for the Journey.
    :ivar destination_station_name: The destination station name for the Journey.
    :ivar rail_loc_origin: RCH specific origin code (a.k.a UCodes) which uniquely identifies a train station.
    :ivar rail_loc_destination: RCH specific destination code (a.k.a UCodes) which uniquely identifies a train station.
    """
    origin: str = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    destination: str = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            required=True
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute"
        )
    )
    origin_station_name: str = field(
        default=None,
        metadata=dict(
            name="OriginStationName",
            type="Attribute"
        )
    )
    destination_station_name: str = field(
        default=None,
        metadata=dict(
            name="DestinationStationName",
            type="Attribute"
        )
    )
    rail_loc_origin: str = field(
        default=None,
        metadata=dict(
            name="RailLocOrigin",
            type="Attribute",
            min_length=3.0,
            max_length=8.0,
            white_space="collapse"
        )
    )
    rail_loc_destination: str = field(
        default=None,
        metadata=dict(
            name="RailLocDestination",
            type="Attribute",
            min_length=3.0,
            max_length=8.0,
            white_space="collapse"
        )
    )


@dataclass
class Characteristic:
    """Defines coach characteristics such as accommodation class, smoking choice,
    etc.

    :ivar smoking:
    :ivar class_value:
    """
    smoking: bool = field(
        default="false",
        metadata=dict(
            name="Smoking",
            type="Attribute"
        )
    )
    class_value: str = field(
        default=None,
        metadata=dict(
            name="Class",
            type="Attribute"
        )
    )


@dataclass
class FareValidity:
    """Associates fare validity dates with journeys.

    :ivar rail_journey_ref: Reference to a journey to which this fare validity refers.
    :ivar not_valid_before: Fare not valid before this date.
    :ivar not_valid_after: Fare not valid after this date.
    """
    rail_journey_ref: str = field(
        default=None,
        metadata=dict(
            name="RailJourneyRef",
            type="Attribute",
            required=True
        )
    )
    not_valid_before: str = field(
        default=None,
        metadata=dict(
            name="NotValidBefore",
            type="Attribute"
        )
    )
    not_valid_after: str = field(
        default=None,
        metadata=dict(
            name="NotValidAfter",
            type="Attribute"
        )
    )


@dataclass
class FulFillmentType:
    """Fulfillment options for this segment. the options will be one of "Ticket on
    Departure", "Ticketless", "Ticket By Email", "Travel Agency".

    :ivar value:
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_length=0.0,
            max_length=255.0
        )
    )


@dataclass
class JourneyRemark(str):
    """A Remark for a Journey.

    :ivar category:
    """
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute"
        )
    )


@dataclass
class OperatingCompany(str):
    """A textual remark identifying the OperatingCompany/Train Service other than
    BN orTL.

    :ivar code: Company Short Text
    :ivar name: Name Identifying the Train Service other than BN orTL
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute"
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RailAutoSeatAssignment:
    """Request object used to request seats automatically by seat type.

    :ivar seat_type: Indicates codeset of values such as Seat Type like Place,Position, Smoking Choice, Place Arrangement, Place Direction, Compartment.
    :ivar seat_value: Indicates the value specific to the selected type.
    :ivar rail_segment_ref: The rail segment that this assignment belongs to
    :ivar booking_traveler_ref: The booking traveler that this seat assignment is for. If not entered, this applies to the primary booking traveler and other passengers are adjacent.
    """
    seat_type: str = field(
        default=None,
        metadata=dict(
            name="SeatType",
            type="Attribute",
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
            required=True,
            min_length=0.0,
            max_length=255.0
        )
    )
    rail_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="RailSegmentRef",
            type="Attribute"
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute"
        )
    )


@dataclass
class RailAvailInfo:
    """
    :ivar class_code: A booking code or fare basis code or fare class.
    :ivar quantity: Available fare basis code or fare class quantity.
    :ivar cabin_class: The fare basis code or fare class for this fare.
    """
    class_code: str = field(
        default=None,
        metadata=dict(
            name="ClassCode",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )
    quantity: int = field(
        default=None,
        metadata=dict(
            name="Quantity",
            type="Attribute"
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            min_length=1.0,
            max_length=128.0
        )
    )


@dataclass
class RailBookingInfo:
    """Links journeys and fares together.

    :ivar rail_fare_ref: Reference to a fare that applies to the journey below.
    :ivar rail_journey_ref: Reference to a journeys on which the above fare applies.
    :ivar optional_service: Indicate the OfferFareItem elements will be Optional or not.
    """
    rail_fare_ref: str = field(
        default=None,
        metadata=dict(
            name="RailFareRef",
            type="Attribute",
            required=True
        )
    )
    rail_journey_ref: str = field(
        default=None,
        metadata=dict(
            name="RailJourneyRef",
            type="Attribute",
            required=True
        )
    )
    optional_service: bool = field(
        default="false",
        metadata=dict(
            name="OptionalService",
            type="Attribute"
        )
    )


@dataclass
class RailExchangeInfo:
    """Exchange information for the rail booking.

    :ivar refund_amount:
    :ivar cancellation_fee:
    :ivar exchange_amount:
    :ivar approximate_refund_amount:
    :ivar approximate_cancellation_fee:
    :ivar approximate_exchange_amount: The Converted total price in Default Currency for this entity including base price and all taxes.
    :ivar retain_amount: Amount retained by a rail vendor for future use at the vendor’s site.
    """
    refund_amount: str = field(
        default=None,
        metadata=dict(
            name="RefundAmount",
            type="Attribute"
        )
    )
    cancellation_fee: str = field(
        default=None,
        metadata=dict(
            name="CancellationFee",
            type="Attribute"
        )
    )
    exchange_amount: str = field(
        default=None,
        metadata=dict(
            name="ExchangeAmount",
            type="Attribute"
        )
    )
    approximate_refund_amount: str = field(
        default=None,
        metadata=dict(
            name="ApproximateRefundAmount",
            type="Attribute"
        )
    )
    approximate_cancellation_fee: str = field(
        default=None,
        metadata=dict(
            name="ApproximateCancellationFee",
            type="Attribute"
        )
    )
    approximate_exchange_amount: str = field(
        default=None,
        metadata=dict(
            name="ApproximateExchangeAmount",
            type="Attribute"
        )
    )
    retain_amount: str = field(
        default=None,
        metadata=dict(
            name="RetainAmount",
            type="Attribute"
        )
    )


@dataclass
class RailFareComponent:
    """Contains fare and discount information for each passenger type.

    :ivar discount: Discount information specific to the fare component
    :ivar key:
    :ivar amount: FareComponent amount
    :ivar age:
    :ivar passenger_type_code: The three character passenger code
    :ivar supplier_passenger_type: Supplier passenger type code
    :ivar quantity:
    """
    discount: List["RailFareComponent.Discount"] = field(
        default_factory=list,
        metadata=dict(
            name="Discount",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    age: int = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute"
        )
    )
    passenger_type_code: str = field(
        default=None,
        metadata=dict(
            name="PassengerTypeCode",
            type="Attribute",
            min_length=3.0,
            max_length=5.0
        )
    )
    supplier_passenger_type: str = field(
        default=None,
        metadata=dict(
            name="SupplierPassengerType",
            type="Attribute"
        )
    )
    quantity: int = field(
        default=None,
        metadata=dict(
            name="Quantity",
            type="Attribute"
        )
    )

    @dataclass
    class Discount:
        """
        :ivar discount_card:
        :ivar key:
        """
        discount_card: List[DiscountCard] = field(
            default_factory=list,
            metadata=dict(
                name="DiscountCard",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=9
            )
        )
        key: str = field(
            default=None,
            metadata=dict(
                name="Key",
                type="Attribute"
            )
        )


@dataclass
class RailFareId(str):
    """
    :ivar key:
    :ivar category:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute"
        )
    )


@dataclass
class RailFareIdref:
    """Reference to a complete FareID from a shared list.

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RailFareNote(str):
    """A simple textual fare note. Used within several other objects.

    :ivar key:
    :ivar note_name:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    note_name: str = field(
        default=None,
        metadata=dict(
            name="NoteName",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RailFareNoteRef:
    """A reference to a fare note from a shared list. Used to minimize xml results.

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RailFareRef:
    """Reference to a complete FareInfo from a shared list.

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RailJourneyRef:
    """Reference to a RailJourney.

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RailLegModifiers:
    """
    :ivar permitted_connection_points:
    :ivar prohibited_connection_points:
    :ivar class_value:
    """
    permitted_connection_points: "RailLegModifiers.PermittedConnectionPoints" = field(
        default=None,
        metadata=dict(
            name="PermittedConnectionPoints",
            type="Element"
        )
    )
    prohibited_connection_points: "RailLegModifiers.ProhibitedConnectionPoints" = field(
        default=None,
        metadata=dict(
            name="ProhibitedConnectionPoints",
            type="Element"
        )
    )
    class_value: str = field(
        default=None,
        metadata=dict(
            name="Class",
            type="Attribute"
        )
    )

    @dataclass
    class PermittedConnectionPoints:
        """
        :ivar connection_point:
        """
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata=dict(
                name="ConnectionPoint",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedConnectionPoints:
        """
        :ivar connection_point:
        """
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata=dict(
                name="ConnectionPoint",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class RailPricingModifiers:
    """Search flexibiity criteria .

    :ivar discount_card: Discount request for rail.
    :ivar prohibit_non_refundable_fares: Indicates whether it prohibits NonRefundable Fares.
    :ivar prohibit_non_exchangeable_fares: Indicates whether it prohibits NonExchangeable Fares .
    :ivar currency_type: 3 Letter Currency Code
    :ivar rail_search_type: RailSearchType options are "All Fares" "Fastest" "Lowest Fare" "One Fare Per Class" "Seasons". Supported by NTV/VF only for "All Fares" "Lowest Fare" and "One Fare Per Class". Provider : RCH
    """
    discount_card: List[DiscountCard] = field(
        default_factory=list,
        metadata=dict(
            name="DiscountCard",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=9
        )
    )
    prohibit_non_refundable_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitNonRefundableFares",
            type="Attribute"
        )
    )
    prohibit_non_exchangeable_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitNonExchangeableFares",
            type="Attribute"
        )
    )
    currency_type: str = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            length=3
        )
    )
    rail_search_type: str = field(
        default=None,
        metadata=dict(
            name="RailSearchType",
            type="Attribute"
        )
    )


@dataclass
class RailRefundInfo:
    """Information about refund.

    :ivar refund_amount: Amount refunded back to customer.
    :ivar cancellation_fee: Cancellation penalty imposed by the distributor.
    :ivar refund: Indicates whether vendor offers refund on rail reservation.
    :ivar retain: Indicates whether vendor retains the amount to be used later.
    :ivar retain_amount: Amount retained by rail vendor for futute exchange/rail book at rail vendor site.
    :ivar net_amount: Net total amount to be refunded or retained by the vendor.
    """
    refund_amount: str = field(
        default=None,
        metadata=dict(
            name="RefundAmount",
            type="Attribute"
        )
    )
    cancellation_fee: str = field(
        default=None,
        metadata=dict(
            name="CancellationFee",
            type="Attribute"
        )
    )
    refund: bool = field(
        default=None,
        metadata=dict(
            name="Refund",
            type="Attribute"
        )
    )
    retain: bool = field(
        default=None,
        metadata=dict(
            name="Retain",
            type="Attribute"
        )
    )
    retain_amount: str = field(
        default=None,
        metadata=dict(
            name="RetainAmount",
            type="Attribute"
        )
    )
    net_amount: str = field(
        default=None,
        metadata=dict(
            name="NetAmount",
            type="Attribute"
        )
    )


@dataclass
class RailSegmentInfo(str):
    """A textual remark container to hold any printable text. (max 512 chars) Holds
    the ExtraSegmentInfo and VendorMessages from RCH response.

    :ivar category: Supplier specific category.
    :ivar type: Either Extra for ExtraSegmentInfo or Vendor for VendorMessages.
    """
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute"
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RailSegmentRef:
    """Reference to a RaiLSegment.

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RailSpecificSeatAssignment:
    """Request object used to request a specific coach and seat number or a seat
    near-to a specific seat number.

    :ivar coach_label: The coach number of the train being requested.
    :ivar place_label: The actual seat number or the close-to seat number based on the Assignment.
    :ivar assignment: Defines how the PlaceLabel should be applied. The values are 6.STP for actual seat or 2.STP for close-to seat. Default is 2.STP.
    :ivar rail_segment_ref: The rail segment to which this assignment belongs.
    :ivar booking_traveler_ref: The BookingTraveler for this seat assignment.
    """
    coach_label: str = field(
        default=None,
        metadata=dict(
            name="CoachLabel",
            type="Attribute",
            required=True
        )
    )
    place_label: str = field(
        default=None,
        metadata=dict(
            name="PlaceLabel",
            type="Attribute",
            required=True
        )
    )
    assignment: str = field(
        default=None,
        metadata=dict(
            name="Assignment",
            type="Attribute",
            required=True
        )
    )
    rail_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="RailSegmentRef",
            type="Attribute",
            required=True
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RailSupplier:
    """
    :ivar code: 2 character Rail distributor code.
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )


@dataclass
class TicketAdvisory:
    """Additional ticket information.

    :ivar value:
    :ivar key:
    :ivar language_code: ISO 639 two-character language codes are used to retrieve specific information in the requested language. For Rich Content and Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE, DECH can also be used. Only certain services support this attribute. Providers: ACH, RCH, 1G, 1V, 1P, 1J.
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_length=1.0,
            max_length=500.0
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    language_code: str = field(
        default=None,
        metadata=dict(
            name="LanguageCode",
            type="Attribute"
        )
    )


@dataclass
class Coach:
    """Captures rail seat map/coach map information.

    :ivar characteristic:
    :ivar remark:
    :ivar coach_number: Coach number for which seat map/coach map is returned.
    """
    characteristic: Characteristic = field(
        default=None,
        metadata=dict(
            name="Characteristic",
            type="Element"
        )
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata=dict(
            name="Remark",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    coach_number: str = field(
        default=None,
        metadata=dict(
            name="CoachNumber",
            type="Attribute"
        )
    )


@dataclass
class RailFare(AttrElementKeyResults):
    """Information about this fare component.

    :ivar rail_fare_note_ref: Key reference to RailFareNote present in RailFareNotList
    :ivar fare_validity:
    :ivar host_token:
    :ivar ful_fillment_type:
    :ivar rail_fare_component:
    :ivar rail_fare_id:
    :ivar rail_fare_idref:
    :ivar key:
    :ivar fare_basis: The fare basis code or fare description for this fare
    :ivar cabin_class: The fare basis code or fare class for this fare
    :ivar passenger_type_code: The PTC that is associated with this fare. Default to ADT
    :ivar origin: Returns the airport or city code that defines the origin market for this fare.
    :ivar destination: Returns the airport or city code that defines the destination market for this fare.
    :ivar effective_date: Returns the date on which this fare was quoted. Set as current date
    :ivar amount:
    :ivar route_description: Describes the route of the train fare.
    :ivar ticket_type_code: Describes the main identifier code of the fare.
    :ivar fare_reference: Unique reference for the fare that is required in RailExchangeQuote request.
    :ivar cross_city_fare: Set to 'true' if the fare is valid across a Metropolitan Area, eg. Cross-London travel via the London Underground.
    :ivar origin_station_name: The origin station name for the Rail Fare.
    :ivar destination_station_name: The destination station name for the Rail Fare.
    :ivar reservation_required: Set to true if a seat reservation is required while booking.
    :ivar journey_direction: The direction of the Journey (Outward or Return) associated with the Rail fare.
    :ivar rail_loc_origin: RCH specific origin code (a.k.a UCodes) which uniquely identifies a train station.
    :ivar rail_loc_destination: RCH specific destination code (a.k.a UCodes) which uniquely identifies a train station.
    """
    rail_fare_note_ref: List[RailFareNoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareNoteRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_validity: List[FareValidity] = field(
        default_factory=list,
        metadata=dict(
            name="FareValidity",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: HostToken = field(
        default=None,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    ful_fillment_type: List[FulFillmentType] = field(
        default_factory=list,
        metadata=dict(
            name="FulFillmentType",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_fare_component: List[RailFareComponent] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareComponent",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    rail_fare_id: List[RailFareId] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareID",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_fare_idref: List[RailFareIdref] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareIDRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute"
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=128.0
        )
    )
    passenger_type_code: str = field(
        default=None,
        metadata=dict(
            name="PassengerTypeCode",
            type="Attribute",
            min_length=3.0,
            max_length=5.0
        )
    )
    origin: str = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    destination: str = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    effective_date: str = field(
        default=None,
        metadata=dict(
            name="EffectiveDate",
            type="Attribute",
            required=True
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    route_description: str = field(
        default=None,
        metadata=dict(
            name="RouteDescription",
            type="Attribute"
        )
    )
    ticket_type_code: str = field(
        default=None,
        metadata=dict(
            name="TicketTypeCode",
            type="Attribute"
        )
    )
    fare_reference: str = field(
        default=None,
        metadata=dict(
            name="FareReference",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    cross_city_fare: bool = field(
        default="false",
        metadata=dict(
            name="CrossCityFare",
            type="Attribute"
        )
    )
    origin_station_name: str = field(
        default=None,
        metadata=dict(
            name="OriginStationName",
            type="Attribute"
        )
    )
    destination_station_name: str = field(
        default=None,
        metadata=dict(
            name="DestinationStationName",
            type="Attribute"
        )
    )
    reservation_required: bool = field(
        default=None,
        metadata=dict(
            name="ReservationRequired",
            type="Attribute"
        )
    )
    journey_direction: str = field(
        default=None,
        metadata=dict(
            name="JourneyDirection",
            type="Attribute"
        )
    )
    rail_loc_origin: str = field(
        default=None,
        metadata=dict(
            name="RailLocOrigin",
            type="Attribute",
            min_length=3.0,
            max_length=8.0,
            white_space="collapse"
        )
    )
    rail_loc_destination: str = field(
        default=None,
        metadata=dict(
            name="RailLocDestination",
            type="Attribute",
            min_length=3.0,
            max_length=8.0,
            white_space="collapse"
        )
    )


@dataclass
class RailFareIdlist:
    """The shared object list of FareIDs.

    :ivar rail_fare_id:
    """
    rail_fare_id: List[RailFareId] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareID",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class RailFareNoteList:
    """The shared object list of Notes.

    :ivar rail_fare_note:
    """
    rail_fare_note: List[RailFareNote] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareNote",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class RailInfo(AttrRailInfoOrgDesAndRailLoc):
    """Container for rail-related information required for retrieving a rail seat
    map/coach map.

    :ivar train_number:
    :ivar provider_code:
    :ivar supplier_code:
    """
    train_number: str = field(
        default=None,
        metadata=dict(
            name="TrainNumber",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2.0,
            max_length=5.0
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )


@dataclass
class RailSearchModifiers:
    """Controls and switches for the Rail Availability Search request.

    :ivar preferred_suppliers:
    :ivar max_changes: The maximum number of stops within a connection.
    :ivar direction: The direction of travel.
    :ivar class_value:
    :ivar max_solutions: The maximum number of solutions to return. Decreasing this number
    """
    preferred_suppliers: "RailSearchModifiers.PreferredSuppliers" = field(
        default=None,
        metadata=dict(
            name="PreferredSuppliers",
            type="Element"
        )
    )
    max_changes: int = field(
        default="2",
        metadata=dict(
            name="MaxChanges",
            type="Attribute",
            min_inclusive=0.0,
            max_inclusive=3.0
        )
    )
    direction: str = field(
        default=None,
        metadata=dict(
            name="Direction",
            type="Attribute"
        )
    )
    class_value: str = field(
        default=None,
        metadata=dict(
            name="Class",
            type="Attribute"
        )
    )
    max_solutions: int = field(
        default="300",
        metadata=dict(
            name="MaxSolutions",
            type="Attribute"
        )
    )

    @dataclass
    class PreferredSuppliers:
        """
        :ivar rail_supplier:
        """
        rail_supplier: List[RailSupplier] = field(
            default_factory=list,
            metadata=dict(
                name="RailSupplier",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class RailSegment(Segment):
    """Rail Segment.

    :ivar rail_segment_info:
    :ivar operating_company:
    :ivar rail_avail_info:
    :ivar ful_fillment_type:
    :ivar train_number:
    :ivar train_type: Type of train used. Same as TrainServiceType.
    :ivar train_type_code: Code for type of train used. Same as TrainServiceType.
    :ivar transport_mode: Type of Transport Mode used.
    :ivar seat_assignable: Set to true if there exists seats to be booked
    :ivar transport_code: Supplier specific train code
    :ivar reservation_required: Set to true if a reservation is required for booking.
    :ivar travel_time: Total time spent (minutes) traveling
    :ivar host_token_ref: The reference key for the host token. From the HostTokenList Providers RCH.
    :ivar cabin_class: Rail Cabin class specification. The valid values are Economy, Business, First and Other
    :ivar class_code: A booking code or fare basis code or fare class.
    """
    rail_segment_info: List[RailSegmentInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailSegmentInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    operating_company: OperatingCompany = field(
        default=None,
        metadata=dict(
            name="OperatingCompany",
            type="Element"
        )
    )
    rail_avail_info: List[RailAvailInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailAvailInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ful_fillment_type: List[FulFillmentType] = field(
        default_factory=list,
        metadata=dict(
            name="FulFillmentType",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    train_number: str = field(
        default=None,
        metadata=dict(
            name="TrainNumber",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )
    train_type: str = field(
        default=None,
        metadata=dict(
            name="TrainType",
            type="Attribute"
        )
    )
    train_type_code: str = field(
        default=None,
        metadata=dict(
            name="TrainTypeCode",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )
    transport_mode: str = field(
        default=None,
        metadata=dict(
            name="TransportMode",
            type="Attribute"
        )
    )
    seat_assignable: bool = field(
        default=None,
        metadata=dict(
            name="SeatAssignable",
            type="Attribute"
        )
    )
    transport_code: str = field(
        default=None,
        metadata=dict(
            name="TransportCode",
            type="Attribute"
        )
    )
    reservation_required: bool = field(
        default=None,
        metadata=dict(
            name="ReservationRequired",
            type="Attribute"
        )
    )
    travel_time: int = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute"
        )
    )
    host_token_ref: str = field(
        default=None,
        metadata=dict(
            name="HostTokenRef",
            type="Attribute"
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            min_length=1.0,
            max_length=128.0
        )
    )
    class_code: str = field(
        default=None,
        metadata=dict(
            name="ClassCode",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )


@dataclass
class RailTicketInfo:
    """
    :ivar rail_journey_ref:
    :ivar ticket_advisory:
    :ivar number: Ticket number.
    :ivar issue_location: Issue location is internal distributor code associated with the PCC.
    :ivar ticket_status: Status of Ticket.
    :ivar ticket_form_type: FormType of Ticket.
    :ivar traffic_type: Type of traffic.
    :ivar issued_date: Ticket issue date.
    :ivar ticket_type: Type of ticket. Paper, eTicket etc.
    :ivar booking_traveler_ref: Reference to a BookingTraveler.
    """
    rail_journey_ref: List[RailJourneyRef] = field(
        default_factory=list,
        metadata=dict(
            name="RailJourneyRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticket_advisory: List[TicketAdvisory] = field(
        default_factory=list,
        metadata=dict(
            name="TicketAdvisory",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
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
            min_length=0.0,
            max_length=128.0
        )
    )
    ticket_status: str = field(
        default=None,
        metadata=dict(
            name="TicketStatus",
            type="Attribute",
            min_length=1.0,
            max_length=255.0
        )
    )
    ticket_form_type: str = field(
        default=None,
        metadata=dict(
            name="TicketFormType",
            type="Attribute",
            min_length=0.0,
            max_length=255.0
        )
    )
    traffic_type: str = field(
        default=None,
        metadata=dict(
            name="TrafficType",
            type="Attribute",
            min_length=1.0,
            max_length=255.0
        )
    )
    issued_date: str = field(
        default=None,
        metadata=dict(
            name="IssuedDate",
            type="Attribute"
        )
    )
    ticket_type: str = field(
        default=None,
        metadata=dict(
            name="TicketType",
            type="Attribute",
            min_length=1.0,
            max_length=255.0
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute"
        )
    )


@dataclass
class RailFareList:
    """The shared object list of FareInfos.

    :ivar rail_fare:
    """
    rail_fare: List[RailFare] = field(
        default_factory=list,
        metadata=dict(
            name="RailFare",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class RailJourney(AttrRailSegmentOrigDestInfo, AttrPrices, AttrProviderSupplier, AttrElementKeyResults):
    """Captures all journey-related data.

    :ivar journey_remark:
    :ivar host_token:
    :ivar rail_segment:
    :ivar rail_segment_ref:
    :ivar key:
    :ivar route_description: The description of the route.
    :ivar journey_direction: The direction of the Journey (Outward or Return).
    :ivar journey_duration: The duration of the entire Journey in minutes
    :ivar status: Status of this Journey.
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar passive_provider_reservation_info_ref: Passive provider reservation reference key.
    :ivar travel_order: To identify the appropriate travel sequence for Air/Car/Hotel/Rail segments/reservations/Journeys based on travel dates. This ordering is applicable across the UR not provider or traveler specific
    :ivar route_reference: RouteReference is required in seat assignment purpose
    :ivar operation: "Type of exchange. Add - Add new Journey. Update - Modify existing Journey. Delete - Remove existing Journey"
    """
    journey_remark: List[JourneyRemark] = field(
        default_factory=list,
        metadata=dict(
            name="JourneyRemark",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_segment: List[RailSegment] = field(
        default_factory=list,
        metadata=dict(
            name="RailSegment",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    rail_segment_ref: List[RailSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="RailSegmentRef",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    route_description: str = field(
        default=None,
        metadata=dict(
            name="RouteDescription",
            type="Attribute",
            max_length=255.0
        )
    )
    journey_direction: str = field(
        default=None,
        metadata=dict(
            name="JourneyDirection",
            type="Attribute"
        )
    )
    journey_duration: int = field(
        default=None,
        metadata=dict(
            name="JourneyDuration",
            type="Attribute"
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute"
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute"
        )
    )
    passive_provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="PassiveProviderReservationInfoRef",
            type="Attribute"
        )
    )
    travel_order: int = field(
        default=None,
        metadata=dict(
            name="TravelOrder",
            type="Attribute"
        )
    )
    route_reference: str = field(
        default=None,
        metadata=dict(
            name="RouteReference",
            type="Attribute",
            min_length=0.0,
            max_length=255.0
        )
    )
    operation: str = field(
        default=None,
        metadata=dict(
            name="Operation",
            type="Attribute"
        )
    )


@dataclass
class RailPricingInfo(AttrPrices, AttrElementKeyResults):
    """Per traveler type pricing breakdown.

    :ivar rail_booking_info:
    :ivar passenger_type:
    :ivar booking_traveler_ref:
    :ivar rail_fare:
    :ivar rail_fare_ref:
    :ivar key:
    :ivar exchange_amount: The amount to pay to cover the exchange of the fare (includes penalties).
    :ivar approximate_exchange_amount:
    """
    rail_booking_info: List[RailBookingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailBookingInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    passenger_type: List[TypePassengerType] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerType",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_fare: List[RailFare] = field(
        default_factory=list,
        metadata=dict(
            name="RailFare",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_fare_ref: List[RailFareRef] = field(
        default_factory=list,
        metadata=dict(
            name="RailFareRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    exchange_amount: str = field(
        default=None,
        metadata=dict(
            name="ExchangeAmount",
            type="Attribute"
        )
    )
    approximate_exchange_amount: str = field(
        default=None,
        metadata=dict(
            name="ApproximateExchangeAmount",
            type="Attribute"
        )
    )


@dataclass
class RailSegmentList:
    """List of Rail Segments.

    :ivar rail_segment:
    """
    rail_segment: List[RailSegment] = field(
        default_factory=list,
        metadata=dict(
            name="RailSegment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class RailJourneyList:
    """List of Rail Journeys.

    :ivar rail_journey:
    """
    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata=dict(
            name="RailJourney",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class RailReservation(BaseReservation):
    """The parent container for all Rail booking data.

    :ivar booking_traveler_ref:
    :ivar rail_journey:
    :ivar rail_pricing_info:
    :ivar payment:
    :ivar rail_ticket_info:
    :ivar rail_fare_note_list: List of RailFareNote(s) that is referenced by key in RailFare.
    :ivar supplier_locator:
    :ivar booking_status: The Current Status of the rail booking.
    """
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=9
        )
    )
    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata=dict(
            name="RailJourney",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    rail_pricing_info: List[RailPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailPricingInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_ticket_info: List[RailTicketInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailTicketInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_fare_note_list: RailFareNoteList = field(
        default=None,
        metadata=dict(
            name="RailFareNoteList",
            type="Element"
        )
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_status: str = field(
        default=None,
        metadata=dict(
            name="BookingStatus",
            type="Attribute",
            required=True
        )
    )


@dataclass
class SearchRailLeg:
    """Holds Origin, Destination, and Departure times for a Rail Leg to search for.

    :ivar search_origin:
    :ivar search_destination:
    :ivar rail_segment_list:
    :ivar rail_leg_modifiers:
    :ivar search_dep_time:
    :ivar search_arv_time:
    """
    search_origin: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata=dict(
            name="SearchOrigin",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=999
        )
    )
    search_destination: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata=dict(
            name="SearchDestination",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=999
        )
    )
    rail_segment_list: RailSegmentList = field(
        default=None,
        metadata=dict(
            name="RailSegmentList",
            type="Element"
        )
    )
    rail_leg_modifiers: RailLegModifiers = field(
        default=None,
        metadata=dict(
            name="RailLegModifiers",
            type="Element"
        )
    )
    search_dep_time: List[TypeFlexibleTimeSpec] = field(
        default_factory=list,
        metadata=dict(
            name="SearchDepTime",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=999
        )
    )
    search_arv_time: List[TypeTimeSpec] = field(
        default_factory=list,
        metadata=dict(
            name="SearchArvTime",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class TypeRailPricingSolution(AttrPrices):
    """Common RailPricingSolution container.

    :ivar rail_pricing_info:
    :ivar rail_journey:
    :ivar rail_journey_ref:
    :ivar key:
    :ivar offer_id: OfferID must be included if the RailCreateReq contains a price. If the RailCreateReq is used for the Direct Book function, the OfferID is not included.
    :ivar provider_code:
    :ivar supplier_code:
    :ivar host_token_ref: HostTokenRef will reference the value in HostTokenList/HostToken @ Key
    :ivar reference: Offer Reference required for Booking(eg.TL).
    """
    rail_pricing_info: List[RailPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RailPricingInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata=dict(
            name="RailJourney",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    rail_journey_ref: List[RailJourneyRef] = field(
        default_factory=list,
        metadata=dict(
            name="RailJourneyRef",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    offer_id: int = field(
        default=None,
        metadata=dict(
            name="OfferId",
            type="Attribute"
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2.0,
            max_length=5.0
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    host_token_ref: str = field(
        default=None,
        metadata=dict(
            name="HostTokenRef",
            type="Attribute"
        )
    )
    reference: str = field(
        default=None,
        metadata=dict(
            name="Reference",
            type="Attribute"
        )
    )


@dataclass
class RailExchangeSolution(TypeRailPricingSolution):
    """Contains the fares and segments for a particular offer.

    :ivar rail_exchange_info:
    """
    rail_exchange_info: RailExchangeInfo = field(
        default=None,
        metadata=dict(
            name="RailExchangeInfo",
            type="Element"
        )
    )


@dataclass
class RailPricingSolution(TypeRailPricingSolution):
    """Contains the fares and segments for a particular offer."""
    pass


@dataclass
class RailSolutionChangedInfo:
    """If RetainReservation is None, this will contain the new values returned from
    the provider. If RetainReservation is Price, Schedule, or Both and there is a
    price/schedule change, this will contain the new values that were returned from
    the provider. If RetainReservation is Price, Schedule, or Both and there isn’t
    a price/schedule change, this element will not be returned.

    :ivar rail_pricing_solution:
    :ivar reason_code:
    """
    rail_pricing_solution: RailPricingSolution = field(
        default=None,
        metadata=dict(
            name="RailPricingSolution",
            type="Element",
            required=True
        )
    )
    reason_code: str = field(
        default=None,
        metadata=dict(
            name="ReasonCode",
            type="Attribute",
            required=True
        )
    )