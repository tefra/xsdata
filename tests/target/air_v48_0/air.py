from dataclasses import dataclass, field
from typing import List

from ..common_v48_0.common import *


@dataclass
class AddlBookingCodeInformation:
    """
    Returns additional booking codes for the selected fare
    """

    pass


@dataclass
class AirReservationLocatorCode:
    """
    Identifies the AirReservation LocatorCode within the Universal Record
    """

    pass


@dataclass
class CarrierCode:
    pass


@dataclass
class CustomerSearch:
    """
    Detailed customer information for searching pre pay profiles
    """

    pass


@dataclass
class PassengerReceiptOverride:
    """
    It is required when a passenger receipt is required immediately ,GDS overrides the default value
    """

    pass


@dataclass
class TicketAgency:
    """
    This modifier will override the pseudo of the ticketing agency found in the AAT (TKAG). Used for all plating carrier validation.
    """

    pass


@dataclass
class TypeDaysOfOperation:
    pass


@dataclass
class VoidDocumentInfo:
    """
    Container to represent document information.
    """

    pass


@dataclass
class ActionDetails:
    """
    Information related to the storing of the fare: Agent, Date and Action for Provider: 1P/1J
    """

    pseudo_city_code: TypePcc = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "help": "PCC in the host of the agent who stored the fare for Provider: 1P/1J",
        },
    )
    agent_sine: str = field(
        default=None,
        metadata={
            "name": "AgentSine",
            "type": "Attribute",
            "help": "The sign in of the user who stored the fare for Provider: 1P/1J",
        },
    )
    event_date: str = field(
        default=None,
        metadata={
            "name": "EventDate",
            "type": "Attribute",
            "help": "Date at which the fare was stored for Provider: 1P/1J",
        },
    )
    event_time: str = field(
        default=None,
        metadata={
            "name": "EventTime",
            "type": "Attribute",
            "help": "Time at which the fare was stored for Provider: 1P/1J",
        },
    )
    text: str = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
            "help": "The type of action the agent performed for Provider: 1P/1J",
        },
    )


@dataclass
class AdditionalInfo:
    category: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Category",
            "type": "Attribute",
            "help": "The category code is the code the AdditionalInfo text came from, e.g. S5 or S7.",
        },
    )


@dataclass
class Adjustment:
    """
    An indentifier which indentifies adjustment made on original pricing. It can a flat amount or percentage of original price. The value of Amount/Percent can be negetive. Negative value implies a discount.
    """

    amount: TypeMoney = field(
        default=None,
        metadata={
            "required": True,
            "name": "Amount",
            "type": "Element",
            "help": "Implies a flat amount to be adjusted. Negetive value implies a discount.",
        },
    )
    percent: float = field(
        default=None,
        metadata={
            "required": True,
            "name": "Percent",
            "type": "Element",
            "help": "Implies an adjustment to be made on original price. Negetive value implies a discount.",
        },
    )
    adjusted_total_price: TypeMoney = field(
        default=None,
        metadata={
            "required": True,
            "name": "AdjustedTotalPrice",
            "type": "Attribute",
            "help": "The adjusted price after applying adjustment on Total price",
        },
    )
    approximate_adjusted_total_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "ApproximateAdjustedTotalPrice",
            "type": "Attribute",
            "help": "The Converted adjusted total price in Default Currency for this entity.",
        },
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "help": "Reference to a booking traveler for which adjustment is applied.",
        },
    )


@dataclass
class Advtype:
    adv_rsvn_only_if_tk: bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnOnlyIfTk",
            "type": "Attribute",
            "help": "Reservation only if ticketed. True is advanced reservations only if tickets. False is no advanced reservations",
        },
    )
    adv_rsvn_any_tm: bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnAnyTm",
            "type": "Attribute",
            "help": "Reservation anytime. True if advanced reservatiosn anytime. False if advanced reservations for a limited time.",
        },
    )
    adv_rsvn_hrs: bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnHrs",
            "type": "Attribute",
            "help": "Reservation hours. True if advanced reservation time in hours. False if advanced reservation time not in hours.",
        },
    )
    adv_rsvn_days: bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnDays",
            "type": "Attribute",
            "help": "Reservation days. True if advanced reservation time in days. False if advanced reservation time not in days.",
        },
    )
    adv_rsvn_months: bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnMonths",
            "type": "Attribute",
            "help": "Reservation months. True if advanced reservation time in months. False if advanced reservation time not in months.",
        },
    )
    adv_rsvn_earliest_tm: bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnEarliestTm",
            "type": "Attribute",
            "help": "Earliest reservation time. True if advanced reservations time is earliest permitted. False is advanced reservation time not earliest permitted time.",
        },
    )
    adv_rsvn_latest_tm: bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnLatestTm",
            "type": "Attribute",
            "help": "Latest reservation time. True if advanced reservations time is latest permitted. False is advanced reservation time not latest permitted time.",
        },
    )
    adv_rsvn_waived: bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnWaived",
            "type": "Attribute",
            "help": "Reservation Waived. True if advanced reservation waived. False if advanced reservation not waived.",
        },
    )
    adv_rsvn_data_exists: bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnDataExists",
            "type": "Attribute",
            "help": "Reservation data exists. True if advanced reservation data exists. False if advanced reservation data does not exist.",
        },
    )
    adv_rsvn_end_item: bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnEndItem",
            "type": "Attribute",
            "help": "Reservation end item. True if advanced reservation end item and more values. False if it does not exist.",
        },
    )
    adv_tk_earliest_tm: bool = field(
        default=None,
        metadata={
            "name": "AdvTkEarliestTm",
            "type": "Attribute",
            "help": "Earliest ticketing time. True if earliest permitted. False if not earliest permitted.",
        },
    )
    adv_tk_latest_tm: bool = field(
        default=None,
        metadata={
            "name": "AdvTkLatestTm",
            "type": "Attribute",
            "help": "Latest ticketing time. True if time is latest permitted. False if time is not latest permitted.",
        },
    )
    adv_tk_rsvn_hrs: bool = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnHrs",
            "type": "Attribute",
            "help": "Ticketing reservation hours. True if in hours. False if not in hours.",
        },
    )
    adv_tk_rsvn_days: bool = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnDays",
            "type": "Attribute",
            "help": "Ticketing reservation days. True if in days. False if not in days.",
        },
    )
    adv_tk_rsvn_months: bool = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnMonths",
            "type": "Attribute",
            "help": "Ticketing reservation months. True if in months. False if not in months.",
        },
    )
    adv_tk_start_hrs: bool = field(
        default=None,
        metadata={
            "name": "AdvTkStartHrs",
            "type": "Attribute",
            "help": "Latest ticketing departure. True if time is latest permitted. False if time is not latest permitted.",
        },
    )
    adv_tk_start_days: bool = field(
        default=None,
        metadata={
            "name": "AdvTkStartDays",
            "type": "Attribute",
            "help": "Ticketing departure days. True if in days. False if not in days.",
        },
    )
    adv_tk_start_months: bool = field(
        default=None,
        metadata={
            "name": "AdvTkStartMonths",
            "type": "Attribute",
            "help": "Ticketing reservation months. True if in months. False if not in months.",
        },
    )
    adv_tk_waived: bool = field(
        default=None,
        metadata={
            "name": "AdvTkWaived",
            "type": "Attribute",
            "help": "Ticketing waived. True if waived. False if not waived.",
        },
    )
    adv_tk_any_tm: bool = field(
        default=None,
        metadata={
            "name": "AdvTkAnyTm",
            "type": "Attribute",
            "help": "Ticketing anytime. True if anytime. False if limited time.",
        },
    )
    adv_tk_end_item: bool = field(
        default=None,
        metadata={
            "name": "AdvTkEndItem",
            "type": "Attribute",
            "help": "Ticketing end item. True if advanced ticketing item and more values. False if end item does not exist.",
        },
    )
    adv_rsvn_tm: int = field(
        default=None,
        metadata={
            "name": "AdvRsvnTm",
            "type": "Attribute",
            "help": "Advanced reservation time.",
        },
    )
    adv_tk_rsvn_tm: int = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnTm",
            "type": "Attribute",
            "help": "Advanced ticketing reservation time.",
        },
    )
    adv_tk_start_tm: int = field(
        default=None,
        metadata={
            "name": "AdvTkStartTm",
            "type": "Attribute",
            "help": "Advanced ticketing departure time.",
        },
    )
    earliest_rsvn_dt_present: bool = field(
        default=None,
        metadata={
            "name": "EarliestRsvnDtPresent",
            "type": "Attribute",
            "help": "Earliest reservation date. True if date is present. False if date is not present.",
        },
    )
    earliest_tk_dt_present: bool = field(
        default=None,
        metadata={
            "name": "EarliestTkDtPresent",
            "type": "Attribute",
            "help": "Earliest ticketing date. True if date is present. False if date is not present.",
        },
    )
    latest_rsvn_dt_present: bool = field(
        default=None,
        metadata={
            "name": "LatestRsvnDtPresent",
            "type": "Attribute",
            "help": "Latest reservation date. True if date is present. False if date is not present.",
        },
    )
    latest_tk_dt_present: bool = field(
        default=None,
        metadata={
            "name": "LatestTkDtPresent",
            "type": "Attribute",
            "help": "Latest ticketing date. True if date is present. False if date is not present.",
        },
    )
    earliest_rsvn_dt: str = field(
        default=None,
        metadata={
            "name": "EarliestRsvnDt",
            "type": "Attribute",
            "help": "Earliest reservation date.",
        },
    )
    earliest_tk_dt: str = field(
        default=None,
        metadata={
            "name": "EarliestTkDt",
            "type": "Attribute",
            "help": "Earliest ticketing date.",
        },
    )
    latest_rsvn_dt: str = field(
        default=None,
        metadata={
            "name": "LatestRsvnDt",
            "type": "Attribute",
            "help": "Latest reservation date.",
        },
    )
    latest_tk_dt: str = field(
        default=None,
        metadata={
            "name": "LatestTkDt",
            "type": "Attribute",
            "help": "Latest ticketing date.",
        },
    )


@dataclass
class AirFareDisplayRuleKey:
    """
    The Tariff Fare Rule requested using a Key. The key is typically a provider specific string which is required to make either a following Air Fare Tariff request for Mileage/Routing information or Air Fare Tariff Rule Request.
    """

    provider_code: TypeProviderCode = field(
        default=None, metadata={"name": "ProviderCode", "type": "Attribute"}
    )


@dataclass
class AirItinerarySolutionRef:
    """
    Reference to a complete AirItinerarySolution from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class AirPricingInfoRef:
    """
    Reference to a AirPricing from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class AirRefundInfo:
    """
    Provides results of a refund quote
    """

    refund_remark: List[RefundRemark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RefundRemark",
            "type": "Element",
        },
    )
    refund_amount: TypeMoney = field(
        default=None, metadata={"name": "RefundAmount", "type": "Attribute"}
    )
    retain_amount: TypeMoney = field(
        default=None, metadata={"name": "RetainAmount", "type": "Attribute"}
    )
    refund_fee: TypeMoney = field(
        default=None,
        metadata={
            "name": "RefundFee",
            "type": "Attribute",
            "help": "Refund fee for ACH/1P",
        },
    )
    refundable_taxes: str = field(
        default=None,
        metadata={
            "name": "RefundableTaxes",
            "type": "Attribute",
            "help": "1P - None : All taxes are not refundable. Unknown : Refundability of taxes are not known.",
        },
    )
    filed_currency: TypeCurrency = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "help": "1P Currency of filed CAT33 refund fee",
        },
    )
    conversion_rate: float = field(
        default=None,
        metadata={
            "name": "ConversionRate",
            "type": "Attribute",
            "help": "1P - Currency conversion rate used for conversion between FiledCurrency and PCC base currency in which the response is returned.",
        },
    )
    taxes: TypeMoney = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
            "help": "1P - The total value of taxes.",
        },
    )
    original_ticket_total: TypeMoney = field(
        default=None,
        metadata={
            "name": "OriginalTicketTotal",
            "type": "Attribute",
            "help": "1P - The original ticket amount.",
        },
    )
    forfeit_amount: TypeMoney = field(
        default=None, metadata={"name": "ForfeitAmount", "type": "Attribute"}
    )
    retain: bool = field(
        default="false",
        metadata={
            "name": "Retain",
            "type": "Attribute",
            "help": "This indicates whether any amount is retained by the provider.",
        },
    )
    refund: bool = field(
        default="false",
        metadata={
            "name": "Refund",
            "type": "Attribute",
            "help": "This indicates whether carrier/host supports refund for the correcponding pnr.",
        },
    )


@dataclass
class AirSearchAsynchModifiers:
    """
    Controls and switches for the Air Search request for Asynch Request
    """

    initial_asynch_result: "AirSearchAsynchModifiers.InitialAsynchResult" = field(
        default=None,
        metadata={"name": "InitialAsynchResult", "type": "Element"},
    )

    @dataclass
    class InitialAsynchResult:
        max_wait: int = field(
            default=None,
            metadata={
                "name": "MaxWait",
                "type": "Attribute",
                "help": "Max wait time in seconds.",
            },
        )


@dataclass
class AirSegmentRef:
    """
    Reference to a complete AirSegment from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class AirSegmentTicketingModifiers:
    """
    Specifies modifiers that a particular segment should be priced with. If this is used, then there must be one for each AirSegment in the AirItinerary.
    """

    air_segment_ref: TypeRef = field(
        default=None, metadata={"name": "AirSegmentRef", "type": "Attribute"}
    )
    brand_tier: StringLength1to10 = field(
        default=None,
        metadata={
            "required": True,
            "name": "BrandTier",
            "type": "Attribute",
            "help": "Modifier to price by specific brand tier number.",
        },
    )


@dataclass
class Alliance:
    """
    Alliance Code
    """

    code: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Code",
            "type": "Attribute",
            "help": "The possible values are *A for Star Alliance,*O for One world,*S for Sky team etc.",
        },
    )


@dataclass
class AlternateLocationDistance:
    """
    Information about the Original Search Airport to Alternate Search Airport.
    """

    distance: Distance = field(
        default=None,
        metadata={"required": True, "name": "Distance", "type": "Element"},
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    search_location: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "SearchLocation",
            "type": "Attribute",
            "help": "The Searching City or Airport specified in the Request.",
        },
    )
    alternate_location: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "AlternateLocation",
            "type": "Attribute",
            "help": "The nearby Alternate City or Airport to SearchLocation.",
        },
    )


@dataclass
class AlternateLocationDistanceRef:
    """
    Reference to a AlternateLocationDistance
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class AssociatedRemark(TypeAssociatedRemarkWithSegmentRef):
    pass


@dataclass
class AsyncProviderSpecificResponse(BaseAsyncProviderSpecificResponse):
    """
    Identifies pending responses from a specific provider using MoreResults attribute
    """

    pass


@dataclass
class AutoSeatAssignment:
    """
    Request object used to request seats automatically by seat type
    """

    segment_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
            "help": "The segment that this assignment belongs to",
        },
    )
    smoking: bool = field(
        default="false",
        metadata={
            "name": "Smoking",
            "type": "Attribute",
            "help": "Indicates that the requested seat type should be a smoking seat.",
        },
    )
    seat_type: TypeReqSeat = field(
        default=None,
        metadata={
            "required": True,
            "name": "SeatType",
            "type": "Attribute",
            "help": "The type of seat that is requested",
        },
    )
    group: bool = field(
        default="false",
        metadata={
            "name": "Group",
            "type": "Attribute",
            "help": "Indicates that this seat request is for group seating for all passengers. If no SegmentRef is included, group seating will be requested for all segments.",
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
class AvailableDiscount:
    loyalty_program: List[LoyaltyProgram] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "LoyaltyProgram",
            "type": "Element",
            "help": "Customer Loyalty Program Detail.",
        },
    )
    amount: TypeMoney = field(
        default=None, metadata={"name": "Amount", "type": "Attribute"}
    )
    percent: TypePercentageWithDecimal = field(
        default=None, metadata={"name": "Percent", "type": "Attribute"}
    )
    description: str = field(
        default=None, metadata={"name": "Description", "type": "Attribute"}
    )
    discount_qualifier: str = field(
        default=None,
        metadata={"name": "DiscountQualifier", "type": "Attribute"},
    )


@dataclass
class AvailableSsr:
    """
    A wrapper for all the information regarding each of the available SSR
    """

    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SSR",
            "type": "Element",
        },
    )
    ssrrules: List[ServiceRuleType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SSRRules",
            "type": "Element",
            "help": "Holds the rules for selecting the SSR in the itinerary",
        },
    )
    industry_standard_ssr: List[IndustryStandardSsr] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "IndustryStandardSSR",
            "type": "Element",
        },
    )


@dataclass
class BookingCode:
    """
    The Booking Code (Class of Service) for a segment
    """

    code: TypeClassOfService = field(
        default=None,
        metadata={"required": True, "name": "Code", "type": "Attribute"},
    )


@dataclass
class BookingCodeInfo:
    """
    Details Cabin class info and class of service information with availability counts. Only provided on search results and grouped by Cabin class
    """

    cabin_class: str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "help": "Specifies Cabin class for a group of class of services. Cabin class is not identified if it is not present.",
        },
    )
    booking_counts: str = field(
        default=None,
        metadata={
            "name": "BookingCounts",
            "type": "Attribute",
            "help": "Lists class of service and their counts for specific cabin class",
        },
    )


@dataclass
class BookingInfo:
    """
    Links segments and fares together
    """

    booking_code: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "BookingCode",
            "type": "Attribute",
        },
    )
    booking_count: str = field(
        default=None,
        metadata={
            "name": "BookingCount",
            "type": "Attribute",
            "help": "Seat availability of the BookingCode",
        },
    )
    cabin_class: str = field(
        default=None, metadata={"name": "CabinClass", "type": "Attribute"}
    )
    fare_info_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "FareInfoRef",
            "type": "Attribute",
        },
    )
    segment_ref: TypeRef = field(
        default=None, metadata={"name": "SegmentRef", "type": "Attribute"}
    )
    coupon_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "CouponRef",
            "type": "Attribute",
            "help": "The coupon to which that booking is relative (if applicable)",
        },
    )
    air_itinerary_solution_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "AirItinerarySolutionRef",
            "type": "Attribute",
            "help": "Reference to an Air Itinerary Solution",
        },
    )
    host_token_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
            "help": "HostToken Reference for this segment and fare combination.",
        },
    )


@dataclass
class BrandId:
    """
    Brand ids for Merchandising details.
    """

    id: str = field(
        default=None,
        metadata={"required": True, "name": "Id", "type": "Attribute"},
    )


@dataclass
class BrandModifiers:
    """
    Used to specify the level of branding requested.
    """

    fare_family_display: "BrandModifiers.FareFamilyDisplay" = field(
        default=None,
        metadata={
            "required": True,
            "name": "FareFamilyDisplay",
            "type": "Element",
            "help": "Used to request a fare family display.",
        },
    )
    basic_details_only: "BrandModifiers.BasicDetailsOnly" = field(
        default=None,
        metadata={
            "required": True,
            "name": "BasicDetailsOnly",
            "type": "Element",
            "help": "Used to request basic details of the brand.",
        },
    )

    @dataclass
    class FareFamilyDisplay:
        modifier_type: str = field(
            default=None,
            metadata={
                "required": True,
                "name": "ModifierType",
                "type": "Attribute",
                "help": '"FareFamily" returns the lowest branded fares in a fare family. "MaintainBookingCode" attempts to return the lowest branded fare in a fare family display based on the permitted booking code. Any brand that does not have a fare for the permitted booking code will then have the lowest fare returned. "LowestFareInBrand" returns the lowest fare within each branded fare in a fare family display.',
            },
        )

    @dataclass
    class BasicDetailsOnly:
        return_basic_details: bool = field(
            default=None,
            metadata={
                "required": True,
                "name": "ReturnBasicDetails",
                "type": "Attribute",
            },
        )


@dataclass
class CarrierList:
    carrier_code: List[CarrierCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 6,
            "name": "CarrierCode",
            "type": "Element",
        },
    )
    include_carrier: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "IncludeCarrier",
            "type": "Attribute",
        },
    )


@dataclass
class Co2Emission:
    """
    Carbon emission values
    """

    air_segment_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Attribute",
            "help": "The segment reference",
        },
    )
    value: float = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "help": "The CO2 emission value for the air segment",
        },
    )


@dataclass
class CodeshareInfo:
    """
    Describes the codeshare disclosure (simple text string) or the specific operating flight information (as attributes).
    """

    operating_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "help": "The actual carrier that is operating the flight.",
        },
    )
    operating_flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "name": "OperatingFlightNumber",
            "type": "Attribute",
            "help": "The actual flight number of the carrier that is operating the flight.",
        },
    )


@dataclass
class CompanyName:
    """
    Supplier info that is specific to the Unique Id
    """

    supplier_code: TypeCarrier = field(
        default=None,
        metadata={
            "required": True,
            "name": "SupplierCode",
            "type": "Attribute",
        },
    )


@dataclass
class ConjunctedTicketInfo:
    number: str = field(
        default=None,
        metadata={"required": True, "name": "Number", "type": "Attribute"},
    )
    iatanumber: TypeIata = field(
        default=None, metadata={"name": "IATANumber", "type": "Attribute"}
    )
    ticket_issue_date: str = field(
        default=None, metadata={"name": "TicketIssueDate", "type": "Attribute"}
    )
    ticketing_agent_sign_on: str = field(
        default=None,
        metadata={"name": "TicketingAgentSignOn", "type": "Attribute"},
    )
    country_code: TypeCountry = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "help": "Contains Ticketed PCC’s Country code.",
        },
    )
    status: TypeTicketStatus = field(
        default=None,
        metadata={"required": True, "name": "Status", "type": "Attribute"},
    )


@dataclass
class ContractCode:
    """
    Some private fares (non-ATPCO) are secured to a contract code.
    """

    code: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Code",
            "type": "Attribute",
            "help": "The 1-64 character string which uniquely identifies a Contract.",
        },
    )
    company_name: str = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Attribute",
            "help": "Providers supported : ACH",
        },
    )


@dataclass
class CreditSummary:
    """
    Credit summary associated with the account
    """

    currency_code: TypeCurrency = field(
        default=None, metadata={"name": "CurrencyCode", "type": "Attribute"}
    )
    current_balance: float = field(
        default=None,
        metadata={
            "required": True,
            "name": "CurrentBalance",
            "type": "Attribute",
        },
    )
    initial_credit: float = field(
        default=None,
        metadata={
            "required": True,
            "name": "InitialCredit",
            "type": "Attribute",
        },
    )


@dataclass
class CustomerReceiptInfo:
    """
    Information about customer receipt via email. Supported providers are 1V/1G/1P/1J
    """

    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "help": "Refererence of the Booking Traveler related to the email.",
        },
    )
    email_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "EmailRef",
            "type": "Attribute",
            "help": "Reference to the email address used for receipt of EMD.",
        },
    )


@dataclass
class Document:
    """
    APIS Document Details.
    """

    sequence: int = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Attribute",
            "help": "Sequence number for the document.",
        },
    )
    type: str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "help": "Type of the Document. Visa, Passport, DriverLicense etc.",
        },
    )
    level: str = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
            "help": "Applicability level of the Document. Required, Supported, API_Supported or Unknown.",
        },
    )


@dataclass
class DocumentModifiers:
    generate_itinerary_invoice: bool = field(
        default="false",
        metadata={
            "name": "GenerateItineraryInvoice",
            "type": "Attribute",
            "help": "Generate itinerary/invoice documents along with ticket",
        },
    )
    generate_accounting_interface: bool = field(
        default="false",
        metadata={
            "name": "GenerateAccountingInterface",
            "type": "Attribute",
            "help": "Generate interface message along with ticket",
        },
    )


@dataclass
class DocumentRequired:
    """
    Additional Details, Documents , Project IDs
    """

    doc_type: str = field(
        default=None, metadata={"name": "DocType", "type": "Attribute"}
    )
    include_exclude_use_ind: bool = field(
        default=None,
        metadata={"name": "IncludeExcludeUseInd", "type": "Attribute"},
    )
    doc_id: str = field(
        default=None, metadata={"name": "DocId", "type": "Attribute"}
    )
    allowed_ids: str = field(
        default=None, metadata={"name": "AllowedIds", "type": "Attribute"}
    )


@dataclass
class Embargo:
    """
    Embargo details. Provider: 1G, 1V, 1P, 1J
    """

    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )
    carrier: TypeCarrier = field(
        default=None, metadata={"name": "Carrier", "type": "Attribute"}
    )
    segment_ref: TypeRef = field(
        default=None, metadata={"name": "SegmentRef", "type": "Attribute"}
    )
    name: str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "help": "The commercial name of the optional service on which the embargo applies. Provider: 1G, 1V, 1P, 1J",
        },
    )
    text: str = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
            "help": "Brief description of the embargo. Provider: 1G, 1V, 1P, 1J",
        },
    )
    secondary_type: str = field(
        default=None,
        metadata={
            "name": "SecondaryType",
            "type": "Attribute",
            "help": "The secondary type of the optional service on which the embargo applies. Provider: 1G, 1V, 1P, 1J",
        },
    )
    type: TypeMerchandisingService = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "help": "The type of optional service on which the embargo applies. Provider: 1G, 1V, 1P, 1J",
        },
    )
    url: str = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Attribute",
            "help": "Website of the operating carrier. Provider: 1G, 1V, 1P, 1J",
        },
    )
    service_sub_code: str = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "help": "The service sub code of the optional service on which the embargo applies. Provider: 1G, 1V, 1P, 1J",
        },
    )


@dataclass
class Emdcommission:
    """
    Commission information to be used for EMD issuance. Supported providers are 1V/1G/1P/1J
    """

    type: TypeAdjustmentType = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Attribute",
            "help": "Type of the commission applied.One of Amount/Percentage",
        },
    )
    value: float = field(
        default=None,
        metadata={
            "required": True,
            "name": "Value",
            "type": "Attribute",
            "help": "Value of the commission applied for EMD issuance.Could represent amount or percentage depending on the type",
        },
    )
    currency_code: TypeCurrency = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "help": "Currency of the commission amount applied.Applicable only with type - Amount",
        },
    )


@dataclass
class Emdcoupon:
    """
    The coupon information for the EMD issued. Supported providers are 1G/1V/1P/1J
    """

    number: int = field(
        default=None,
        metadata={
            "required": True,
            "name": "Number",
            "type": "Attribute",
            "help": "Number of the EMD coupon",
        },
    )
    status: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Status",
            "type": "Attribute",
            "help": "Status of the coupon. Possible values Open, Void, Refunded, Exchanged, Irregular Operations,Airport Control, Checked In, Flown/Used, Boarded/Lifted, Suspended, Unknown",
        },
    )
    svc_description: str = field(
        default=None,
        metadata={
            "name": "SvcDescription",
            "type": "Attribute",
            "help": "Description of the service related to the EMD Coupon",
        },
    )
    consumed_at_issuance_ind: bool = field(
        default=None,
        metadata={
            "name": "ConsumedAtIssuanceInd",
            "type": "Attribute",
            "help": "Indicates if the EMD coupon has been considered used as soon as issued.",
        },
    )
    rfic: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "RFIC",
            "type": "Attribute",
            "help": "Reason For Issuance Code for the EMD coupon",
        },
    )
    rfisc: str = field(
        default=None,
        metadata={
            "name": "RFISC",
            "type": "Attribute",
            "help": "Reason For Issueance Sub code for the EMD coupon",
        },
    )
    rfidescription: str = field(
        default=None,
        metadata={
            "name": "RFIDescription",
            "type": "Attribute",
            "help": "Reason for Issueance Description for the EMD coupon",
        },
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "help": "Departure Airport Code for the flight with which the Coupon is associated",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "help": "Destination Airport Code for the flight with which the Coupon is associated",
        },
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "help": "Flight Number of the flight with which the coupon is associated.",
        },
    )
    present_to: str = field(
        default=None,
        metadata={
            "name": "PresentTo",
            "type": "Attribute",
            "help": "Service provider to present the coupon to",
        },
    )
    present_at: str = field(
        default=None,
        metadata={
            "name": "PresentAt",
            "type": "Attribute",
            "help": "Location of service provider where this coupon should be presented at",
        },
    )
    non_refundable_ind: bool = field(
        default=None,
        metadata={
            "name": "NonRefundableInd",
            "type": "Attribute",
            "help": "Indicates whether the coupon is non-refundable",
        },
    )
    marketing_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "MarketingCarrier",
            "type": "Attribute",
            "help": "Marketing carrier associated with the coupon",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "help": "System generated Key",
        },
    )


@dataclass
class Emdendorsement:
    """
    Endorsement for EMD. Supported providers are 1V/1G/1P/1J
    """

    value: str = field(
        default=None,
        metadata={
            "min_length": "1",
            "max_length": "255",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class EmdtravelerInfo:
    """
    EMD traveler information. Supported providers are 1G/1V/1P/1J
    """

    name_info: "EmdtravelerInfo.NameInfo" = field(
        default=None,
        metadata={
            "required": True,
            "name": "NameInfo",
            "type": "Element",
            "help": "Name information of the EMD traveler.",
        },
    )
    traveler_type: TypePtc = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "help": "Defines the type of traveler used for booking which could be a non-defining type (Companion, Web-fare, etc), or a standard type (Adult, Child, etc).",
        },
    )
    age: int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
            "help": "Age of the traveler",
        },
    )

    @dataclass
    class NameInfo:
        pass


@dataclass
class ExchangedTicketInfo:
    """
    Contains Exchanged/Reissued Ticket Information
    """

    number: TypeTicketNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "Number",
            "type": "Attribute",
            "help": "Original Ticket that was Exchange/Reissued",
        },
    )


@dataclass
class ExcludeTicketing:
    """
    Exclude ticketing of traveler referenced. Supported Provider: JAL.
    """

    booking_traveler_ref: List[TypeRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BookingTravelerRef",
            "type": "Element",
            "help": "Reference to a booking traveler for which ticketing modifier is applied.",
        },
    )


@dataclass
class ExemptTaxes:
    """
    Request tax exemption for specific tax category and/or all taxes of a specific country
    """

    country_code: List[TypeCountry] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "CountryCode",
            "type": "Element",
            "help": "Specify ISO country code for which tax exemption is requested.",
        },
    )
    tax_category: List[str] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxCategory",
            "type": "Element",
            "help": "Specify tax category for which tax exemption is requested.",
        },
    )
    all_taxes: bool = field(
        default=None,
        metadata={
            "name": "AllTaxes",
            "type": "Attribute",
            "help": "Request exemption of all taxes.",
        },
    )
    tax_territory: str = field(
        default=None,
        metadata={
            "name": "TaxTerritory",
            "type": "Attribute",
            "help": "exemption is achieved by sending in the TaxTerritory in the tax exempt price request.",
        },
    )
    company_name: str = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Attribute",
            "help": "The federal government body name must be provided in this element. This field is required by AC",
        },
    )


@dataclass
class FareBasis:
    """
    Fare Basis Code
    """

    code: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Code",
            "type": "Attribute",
            "help": "The fare basis code for this fare",
        },
    )
    segment_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
            "help": "The segment to which this FareBasis Code is to connected",
        },
    )


@dataclass
class FareCalc(str):
    """
    The complete fare calculation line.
    """

    pass


@dataclass
class FareDetailsRef:
    """
    Reference of the Fare
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class FareInfoMessage:
    """
    A simple textual fare information message.Providers supported : 1G/1V/1P/1J
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class FareInfoRef:
    """
    Reference to a complete FareInfo from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class FareMileageInformation(str):
    """
    Contains Fare/Tariff Display Mileage Information
    """

    pass


@dataclass
class FareNote:
    """
    A simple textual fare note. Used within several other objects.
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    precedence: int = field(
        default=None, metadata={"name": "Precedence", "type": "Attribute"}
    )
    note_name: str = field(
        default=None, metadata={"name": "NoteName", "type": "Attribute"}
    )
    fare_info_message_ref: TypeRef = field(
        default=None,
        metadata={"name": "FareInfoMessageRef", "type": "Attribute"},
    )


@dataclass
class FareNoteRef:
    """
    A reference to a fare note from a shared list. Used to minimize xml results.
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class FarePricing:
    """
    Container for Fare Pricing Information. One per PTC type.
    """

    passenger_type: TypePtc = field(
        default=None, metadata={"name": "PassengerType", "type": "Attribute"}
    )
    total_fare_amount: TypeMoney = field(
        default=None, metadata={"name": "TotalFareAmount", "type": "Attribute"}
    )
    private_fare: bool = field(
        default=None,
        metadata={
            "name": "PrivateFare",
            "type": "Attribute",
            "help": "NegotiatedFare attribute from earlier version of schema used to imply whether the fare is private fare or not. So, this attribute is renamed to PrivateFare as it best suited.",
        },
    )
    negotiated_fare: bool = field(
        default=None,
        metadata={
            "name": "NegotiatedFare",
            "type": "Attribute",
            "help": "Identifies the fare as a Negotiated Fare.",
        },
    )
    auto_priceable: bool = field(
        default=None,
        metadata={
            "name": "AutoPriceable",
            "type": "Attribute",
            "help": "Identifies the fare as Autopriceable or not. False value means the fare filing is incomplete and the fare should not be used.",
        },
    )
    total_net_fare_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "TotalNetFareAmount",
            "type": "Attribute",
            "help": "Total Net fare amount.",
        },
    )
    base_fare: TypeMoney = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Attribute",
            "help": "Base fare amount.",
        },
    )
    taxes: TypeMoney = field(
        default=None, metadata={"name": "Taxes", "type": "Attribute"}
    )
    mmid: TypeRef = field(
        default=None,
        metadata={
            "name": "MMid",
            "type": "Attribute",
            "help": "Contains the Reference id which is generated when the request was ReturnMM=”true”.",
        },
    )


@dataclass
class FareRemarkRef:
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class FareRestrictionSaleDate:
    """
    Restrict when this fare can be sold
    """

    start_date: str = field(
        default=None, metadata={"name": "StartDate", "type": "Attribute"}
    )
    end_date: str = field(
        default=None, metadata={"name": "EndDate", "type": "Attribute"}
    )


@dataclass
class FareRestrictionSeasonal:
    """
    Fares Restricted based on the season requested. StartDate and EndDate are strings representing respective dates. If a year component is present then it signifies an exact date. If only day and month components are present then it signifies a seasonal date, which means applicable for that date in any year
    """

    comment: str = field(
        default=None, metadata={"name": "Comment", "type": "Attribute"}
    )
    variation_by_travel_dates: str = field(
        default=None,
        metadata={"name": "VariationByTravelDates", "type": "Attribute"},
    )
    seasonal_range1_ind: str = field(
        default=None,
        metadata={"name": "SeasonalRange1Ind", "type": "Attribute"},
    )
    seasonal_range1_start_date: str = field(
        default=None,
        metadata={"name": "SeasonalRange1StartDate", "type": "Attribute"},
    )
    seasonal_range1_end_date: str = field(
        default=None,
        metadata={"name": "SeasonalRange1EndDate", "type": "Attribute"},
    )
    seasonal_range2_ind: str = field(
        default=None,
        metadata={"name": "SeasonalRange2Ind", "type": "Attribute"},
    )
    seasonal_range2_start_date: str = field(
        default=None,
        metadata={"name": "SeasonalRange2StartDate", "type": "Attribute"},
    )
    seasonal_range2_end_date: str = field(
        default=None,
        metadata={"name": "SeasonalRange2EndDate", "type": "Attribute"},
    )


@dataclass
class FareRoutingInformation(str):
    """
    Contains Fare/Tariff Display Routing Information
    """

    pass


@dataclass
class FareRuleCategory:
    """
    Rule Categories to filter on.
    """

    category: int = field(
        default=None,
        metadata={"required": True, "name": "Category", "type": "Attribute"},
    )


@dataclass
class FareRuleKey:
    """
    The Fare Rule requested using a Key. The key is typically a provider specific string which is required to make a following Air Fare Rule Request. This Key is returned in Low Fare Shop or Air Price Response
    """

    fare_info_ref: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "FareInfoRef",
            "type": "Attribute",
            "help": "The Fare Component to which this Rule Key applies",
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


@dataclass
class FareRuleLong:
    """
    Long Text Fare Rule
    """

    category: int = field(
        default=None,
        metadata={"required": True, "name": "Category", "type": "Attribute"},
    )
    type: str = field(
        default=None, metadata={"name": "Type", "type": "Attribute"}
    )


@dataclass
class FareRuleLongRef:
    """
    A reference to an Long Text Rule in a Shared List
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class FareRuleLookup:
    """
    Parameters to use for a fare rule lookup that is not associated with an Air Reservation Locator Code.
    """

    account_code: AccountCode = field(
        default=None, metadata={"name": "AccountCode", "type": "Element"}
    )
    point_of_sale: PointOfSale = field(
        default=None, metadata={"name": "PointOfSale", "type": "Element"}
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={"required": True, "name": "Origin", "type": "Attribute"},
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Destination",
            "type": "Attribute",
        },
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata={"required": True, "name": "Carrier", "type": "Attribute"},
    )
    fare_basis: str = field(
        default=None,
        metadata={"required": True, "name": "FareBasis", "type": "Attribute"},
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderCode",
            "type": "Attribute",
        },
    )
    departure_date: str = field(
        default=None, metadata={"name": "DepartureDate", "type": "Attribute"}
    )
    ticketing_date: str = field(
        default=None, metadata={"name": "TicketingDate", "type": "Attribute"}
    )


@dataclass
class FareRuleNameValue:
    """
    Fare Rule Name Value Pair, used in Short Rules
    """

    name: str = field(
        default=None,
        metadata={"required": True, "name": "Name", "type": "Attribute"},
    )
    value: str = field(
        default=None,
        metadata={"required": True, "name": "Value", "type": "Attribute"},
    )


@dataclass
class FareRuleShortRef:
    """
    A reference to an Short Text Rule in a Shared List
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class FareRulesFilterCategory:
    """
    Fare Rules Filter if requested will return rules for requested category in the response. Applicable for providers 1G,1V,1P,1J.
    """

    category_code: List[str] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 35,
            "name": "CategoryCode",
            "type": "Element",
            "help": "Fare Rules Filter category can be requested. Currently only '˜MIN, MAX, ADV, CHG, OTH' is supported. Applicable for Providers 1G,1V,1P,1J.",
        },
    )
    fare_info_ref: str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
            "help": "This tells if Low Fare Finder was used.",
        },
    )


@dataclass
class FareStatusFailureInfo:
    """
    Denotes the failure reason of a particular fare.
    """

    code: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Code",
            "type": "Attribute",
            "help": "The failure code of the fare.",
        },
    )
    reason: str = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Attribute",
            "help": "The reason for the failure.",
        },
    )


@dataclass
class FareSurcharge:
    """
    Surcharges for a fare component
    """

    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )
    type: str = field(
        default=None,
        metadata={"required": True, "name": "Type", "type": "Attribute"},
    )
    amount: TypeMoney = field(
        default=None,
        metadata={"required": True, "name": "Amount", "type": "Attribute"},
    )
    segment_ref: TypeRef = field(
        default=None, metadata={"name": "SegmentRef", "type": "Attribute"}
    )
    coupon_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "CouponRef",
            "type": "Attribute",
            "help": "The coupon to which that surcharge is relative (if applicable)",
        },
    )


@dataclass
class FeeApplication:
    code: str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "help": "The code associated to the fee application. The choices are: 1, 2, 3, 4, 5, K, F",
        },
    )


@dataclass
class FeeInfo(TypeFeeInfo):
    """
    A generic type of fee for those charges which are incurred by the passenger, but not necessarily shown on tickets
    """

    pass


@dataclass
class FlexExploreModifiers:
    """
    This is the container for a set of modifiers which allow the user to perform a special kind of low fare search, depicted as flex explore, based on different parameters like Area, Zone, Country, State, Specific locations, Distance around the actual destination of the itinerary. Applicable for providers 1G,1V,1P
    """

    destination: List[TypeIatacode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 59,
            "name": "Destination",
            "type": "Element",
            "help": "List of specific destinations for performing flex explore. Applicable only with flex explore type - Destination",
        },
    )
    type: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Attribute",
            "help": "Type of flex explore to be performed",
        },
    )
    radius: int = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Attribute",
            "help": "Radius around the destination of actual itinerary in which the search would be performed. Supported only with types - DistanceInMiles and DistanceInKilometers",
        },
    )
    group_name: str = field(
        default=None,
        metadata={
            "name": "GroupName",
            "type": "Attribute",
            "help": "Group name for a set of destinations to be searched. Use with Type=Group. Group names are defined in the Search Control Console. Supported Providers: 1G/1V/1P",
        },
    )


@dataclass
class FlightDetailsRef:
    """
    Reference to a complete FlightDetails from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class FlightInfoCriteria:
    key: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "Key",
            "type": "Attribute",
            "help": "An identifier to link the flightinfo responses to the criteria. The value passed here will be returned in the resulting flightinfo(s) from this command.",
        },
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata={
            "required": True,
            "name": "Carrier",
            "type": "Attribute",
            "help": "The carrier that is marketing this segment",
        },
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "FlightNumber",
            "type": "Attribute",
            "help": "The flight number under which the marketing carrier is marketing this flight",
        },
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "help": "The IATA location code for this origination of this entity.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "help": "The IATA location code for this destination of this entity.",
        },
    )
    departure_date: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "DepartureDate",
            "type": "Attribute",
            "help": "The date at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
        },
    )
    class_of_service: TypeClassOfService = field(
        default=None, metadata={"name": "ClassOfService", "type": "Attribute"}
    )


@dataclass
class FlightType:
    """
    Modifier to request flight type options example non-stop only, non-stop and direct only, include single online connection etc.
    """

    require_single_carrier: bool = field(
        default="false",
        metadata={"name": "RequireSingleCarrier", "type": "Attribute"},
    )
    max_connections: int = field(
        default="-1",
        metadata={
            "name": "MaxConnections",
            "type": "Attribute",
            "help": "The maximum number of connections within a segment group.",
        },
    )
    max_stops: int = field(
        default="-1",
        metadata={
            "name": "MaxStops",
            "type": "Attribute",
            "help": "The maximum number of stops within a connection.",
        },
    )
    non_stop_directs: bool = field(
        default=None, metadata={"name": "NonStopDirects", "type": "Attribute"}
    )
    stop_directs: bool = field(
        default=None, metadata={"name": "StopDirects", "type": "Attribute"}
    )
    single_online_con: bool = field(
        default=None, metadata={"name": "SingleOnlineCon", "type": "Attribute"}
    )
    double_online_con: bool = field(
        default=None, metadata={"name": "DoubleOnlineCon", "type": "Attribute"}
    )
    triple_online_con: bool = field(
        default=None, metadata={"name": "TripleOnlineCon", "type": "Attribute"}
    )
    single_interline_con: bool = field(
        default=None,
        metadata={"name": "SingleInterlineCon", "type": "Attribute"},
    )
    double_interline_con: bool = field(
        default=None,
        metadata={"name": "DoubleInterlineCon", "type": "Attribute"},
    )
    triple_interline_con: bool = field(
        default=None,
        metadata={"name": "TripleInterlineCon", "type": "Attribute"},
    )


@dataclass
class GroupedOption:
    optional_service_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "OptionalServiceRef",
            "type": "Attribute",
            "help": "Reference to a optionalService which is paired with other optional services in the parent PairedOptions element.",
        },
    )


@dataclass
class HostReservation:
    """
    Defines a reservation that already exists in the host system (e.g an agent using Galileo Desktop already booked a reservation on Midwest in Sabre host system).
    """

    carrier: TypeCarrier = field(
        default=None,
        metadata={
            "required": True,
            "name": "Carrier",
            "type": "Attribute",
            "help": "The carrier code (e.g. YX, UA, ...) that is providing the merchandising",
        },
    )
    carrier_locator_code: TypeLocatorCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "CarrierLocatorCode",
            "type": "Attribute",
            "help": "The locator code in the supplier system (also could be defined as locator in the carrier host system).",
        },
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderCode",
            "type": "Attribute",
            "help": "Contains the GDS or other provider code of the entity actually housing the reservation. This is optional when used on Merchandising Availability but required on MerchandisingFulfillment.",
        },
    )
    provider_locator_code: TypeProviderLocatorCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "help": "Contains the locator of the reservation actually housed in the provider.",
        },
    )
    universal_locator_code: TypeLocatorCode = field(
        default=None,
        metadata={
            "name": "UniversalLocatorCode",
            "type": "Attribute",
            "help": "The locator of the Universal Record, if one exists.",
        },
    )
    eticket: bool = field(
        default="false",
        metadata={
            "name": "ETicket",
            "type": "Attribute",
            "help": "An flag to indicate if ticket has been issued for the PNR.",
        },
    )


@dataclass
class HostTokenList:
    """
    The shared object list of Host Tokens
    """

    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "HostToken",
            "type": "Element",
        },
    )


@dataclass
class ImageLocation:
    type: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Attribute",
            "help": 'Type of Image Location. E.g., "Agent", "Consumer".',
        },
    )
    image_width: int = field(
        default=None,
        metadata={
            "required": True,
            "name": "ImageWidth",
            "type": "Attribute",
            "help": "The width of the image",
        },
    )
    image_height: int = field(
        default=None,
        metadata={
            "required": True,
            "name": "ImageHeight",
            "type": "Attribute",
            "help": "The height of the image",
        },
    )


@dataclass
class InFlightServices(str):
    """
    Available InFlight Services. They are: 'Movie', 'Telephone', 'Telex', 'AudioProgramming', 'Television' ,'ResvBookingService' ,'DutyFreeSales' ,'Smoking' ,'NonSmoking' ,'ShortFeatureVideo' ,'NoDutyFree' ,'InSeatPowerSource' ,'InternetAccess' ,'Email' ,'Library' ,'LieFlatSeat' ,'Additional service(s) exists' ,'WiFi' ,'Lie-Flat seat first' ,'Lie-Flat seat business' ,'Lie-Flat seat premium economy' ,'Amenities subject to change' etc.. These follow the IATA standard. Please see the IATA standards for a more complete list.
    """

    pass


@dataclass
class LanguageOption:
    """
    Enables itineraries and invoices to print in different languages.
    """

    language: TypeLanguage = field(
        default=None,
        metadata={
            "required": True,
            "name": "Language",
            "type": "Attribute",
            "help": "2 Letter ISO Language code",
        },
    )
    country: TypeCountry = field(
        default=None,
        metadata={
            "required": True,
            "name": "Country",
            "type": "Attribute",
            "help": "2 Letter ISO Country code",
        },
    )


@dataclass
class LegDetail:
    """
    Information about the journey Leg, Shared by Leg and LegPrice Elements
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    origin_airport: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "OriginAirport",
            "type": "Attribute",
            "help": "Returns the origin airport code for the Leg Detail.",
        },
    )
    destination_airport: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "DestinationAirport",
            "type": "Attribute",
            "help": "Returns the destination airport code for the Leg Detail.",
        },
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata={
            "required": True,
            "name": "Carrier",
            "type": "Attribute",
            "help": "Carrier for the Search Leg Detail.",
        },
    )
    travel_date: str = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Attribute",
            "help": "The Departure date and time for this Leg Detail.",
        },
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "help": "Flight Number for the Search Leg Detail.",
        },
    )


@dataclass
class LegRef:
    """
    Reference to a Leg
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class LoyaltyCardDetails:
    """
    Passenger Loyalty card details
    """

    supplier_code: TypeCarrier = field(
        default=None,
        metadata={
            "required": True,
            "name": "SupplierCode",
            "type": "Attribute",
            "help": "Carrier Code",
        },
    )
    priority_code: TypePriorityCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "PriorityCode",
            "type": "Attribute",
        },
    )


@dataclass
class MaxLayoverDurationRangeType:
    """
    Layover duration range of valid values 0-9999
    """

    value: int = field(
        default=None,
        metadata={
            "min_inclusive": "0",
            "max_inclusive": "9999",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class Maxtype:
    hours_max: bool = field(
        default=None,
        metadata={
            "name": "HoursMax",
            "type": "Attribute",
            "help": "Maximum hours. True if unit of time is hours. False if unit of time is not hours.",
        },
    )
    days_max: bool = field(
        default=None,
        metadata={
            "name": "DaysMax",
            "type": "Attribute",
            "help": "Maximum days. True if unit of time is days. False if unit of time is not days.",
        },
    )
    months_max: bool = field(
        default=None,
        metadata={
            "name": "MonthsMax",
            "type": "Attribute",
            "help": "Maximum months. True if unit of time is months. False if unit of time is not months.",
        },
    )
    occur_ind_max: bool = field(
        default=None,
        metadata={
            "name": "OccurIndMax",
            "type": "Attribute",
            "help": "Maximum cccurance indicator. True if day of the week is used. False if day of the week is not used.",
        },
    )
    same_day_max: bool = field(
        default=None,
        metadata={
            "name": "SameDayMax",
            "type": "Attribute",
            "help": "Same day maximum. True if Stay is same day. False if Stay is not same day.",
        },
    )
    start_ind_max: bool = field(
        default=None,
        metadata={
            "name": "StartIndMax",
            "type": "Attribute",
            "help": "Start indicator. True if start indicator. False if not a start indicator.",
        },
    )
    completion_ind: bool = field(
        default=None,
        metadata={
            "name": "CompletionInd",
            "type": "Attribute",
            "help": "Completion indicator. True if Completion C Indicator. False if not Completion C Indicator.",
        },
    )
    tm_dowmax: int = field(
        default=None,
        metadata={
            "name": "TmDOWMax",
            "type": "Attribute",
            "help": "If a max unit of time is true then number corrolates to day of the week starting with 1 for Sunday.",
        },
    )
    num_occur_max: int = field(
        default=None,
        metadata={
            "name": "NumOccurMax",
            "type": "Attribute",
            "help": "Number of maximum occurances.",
        },
    )


@dataclass
class MerchandisingPricingModifiers:
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 10,
            "name": "AccountCode",
            "type": "Element",
            "help": "The account code is used to get corporate discounted pricing on paid seats. Provider:ACH",
        },
    )


@dataclass
class Mintype:
    hours_min: bool = field(
        default=None,
        metadata={
            "name": "HoursMin",
            "type": "Attribute",
            "help": "Minimum hours. True if unit of time is hours. False if unit of time is not hours.",
        },
    )
    days_min: bool = field(
        default=None,
        metadata={
            "name": "DaysMin",
            "type": "Attribute",
            "help": "Minimum days. True if unit of time is days. False if unit of time is not days.",
        },
    )
    months_min: bool = field(
        default=None,
        metadata={
            "name": "MonthsMin",
            "type": "Attribute",
            "help": "Minimum months. True if unit of time is months. False if unit of time is not months.",
        },
    )
    occur_ind_min: bool = field(
        default=None,
        metadata={
            "name": "OccurIndMin",
            "type": "Attribute",
            "help": "Minimum occurance indicator. True if day of the week is used. False if day of the week is not used.",
        },
    )
    same_day_min: bool = field(
        default=None,
        metadata={
            "name": "SameDayMin",
            "type": "Attribute",
            "help": "Same day minimum. True if Stay is same day. False if Stay is not same day.",
        },
    )
    tm_dowmin: int = field(
        default=None,
        metadata={
            "name": "TmDOWMin",
            "type": "Attribute",
            "help": "If a min unit of time is true then number corrolates to day of the week starting with 1 for Sunday.",
        },
    )
    fare_component: int = field(
        default=None,
        metadata={
            "name": "FareComponent",
            "type": "Attribute",
            "help": "Fare component number of the most restrictive fare.",
        },
    )
    num_occur_min: int = field(
        default=None,
        metadata={
            "name": "NumOccurMin",
            "type": "Attribute",
            "help": "Number of min occurances. This field is used in conjunction with the Day of Week.",
        },
    )


@dataclass
class MultiGdssearchIndicator:
    """
    Indicates whether public fares and/or private fares should be returned.
    """

    type: str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "help": "Indicates whether only public fares or both public and private fares should be returned or a specific type of private fares. Examples of valid values are PublicFaresOnly, PrivateFaresOnly, AirlinePrivateFaresOnly, AgencyPrivateFaresOnly, PublicandPrivateFares, and NetFaresOnly.",
        },
    )
    provider_code: TypeProviderCode = field(
        default=None, metadata={"name": "ProviderCode", "type": "Attribute"}
    )
    default_provider: bool = field(
        default=None,
        metadata={
            "name": "DefaultProvider",
            "type": "Attribute",
            "help": "Use the value “true” if the provider is the default (primary) provider. Use the value “false” if the provider is the alternate (secondary). Use of this attribute requires specifically provisioned credentials.",
        },
    )
    private_fare_code: str = field(
        default=None,
        metadata={
            "name": "PrivateFareCode",
            "type": "Attribute",
            "help": "The code of the corporate private fare. This is the same as an account code. Use of this attribute requires specifically provisioned credentials.",
        },
    )
    private_fare_code_only: bool = field(
        default=None,
        metadata={
            "name": "PrivateFareCodeOnly",
            "type": "Attribute",
            "help": ": Indicates whether or not the private fares returned should be restricted to only those specific to the PrivateFareCode in the previous attribute. This has the same validation as the AccountCodeFaresOnly attribute. Use of this attribute requires specifically provisioned credentials.",
        },
    )


@dataclass
class OfferAvailabilityModifiers:
    service_type: List[TypeMerchandisingService] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ServiceType",
            "type": "Element",
            "help": "To restrict offers to only this type.",
        },
    )
    carrier: List[TypeCarrier] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Carrier",
            "type": "Element",
            "help": "The carrier whose paid seat optional services is to be returned by uAPI.",
        },
    )
    currency_type: TypeCurrency = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "help": "Currency code override. Providers: ACH, 1G, 1V, 1P, 1J",
        },
    )


@dataclass
class OptionalServiceModifier:
    """
    Optional service modifiers
    """

    type: TypeMerchandisingService = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Attribute",
            "help": "Optional service type",
        },
    )
    secondary_type: TypeMerchandisingService = field(
        default=None,
        metadata={
            "name": "SecondaryType",
            "type": "Attribute",
            "help": "Secondary optional service type",
        },
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "SupplierCode",
            "type": "Attribute",
            "help": "Optional service supplier code",
        },
    )
    service_sub_code: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "ServiceSubCode",
            "type": "Attribute",
            "help": "As published by ATPCO",
        },
    )
    travel_date: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "TravelDate",
            "type": "Attribute",
            "help": "The departure date of the air segment the optional service is valid for.",
        },
    )
    description: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Description",
            "type": "Attribute",
            "help": "This allows MDS to return specific image and text corresponding to the ancillary name (S5 ancillary name).",
        },
    )


@dataclass
class OptionalServiceRef(TypeRef):
    """
    Reference to optional service
    """

    pass


@dataclass
class Othtype:
    cat0: bool = field(
        default=None,
        metadata={
            "name": "Cat0",
            "type": "Attribute",
            "help": "Category 0 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat1: bool = field(
        default=None,
        metadata={
            "name": "Cat1",
            "type": "Attribute",
            "help": "Category 1 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat2: bool = field(
        default=None,
        metadata={
            "name": "Cat2",
            "type": "Attribute",
            "help": "Category 2 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat3: bool = field(
        default=None,
        metadata={
            "name": "Cat3",
            "type": "Attribute",
            "help": "Category 3 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat4: bool = field(
        default=None,
        metadata={
            "name": "Cat4",
            "type": "Attribute",
            "help": "Category 4 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat5: bool = field(
        default=None,
        metadata={
            "name": "Cat5",
            "type": "Attribute",
            "help": "Category 5 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat6: bool = field(
        default=None,
        metadata={
            "name": "Cat6",
            "type": "Attribute",
            "help": "Category 6 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat7: bool = field(
        default=None,
        metadata={
            "name": "Cat7",
            "type": "Attribute",
            "help": "Category 7 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat8: bool = field(
        default=None,
        metadata={
            "name": "Cat8",
            "type": "Attribute",
            "help": "Category 8 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat9: bool = field(
        default=None,
        metadata={
            "name": "Cat9",
            "type": "Attribute",
            "help": "Category 9 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat10: bool = field(
        default=None,
        metadata={
            "name": "Cat10",
            "type": "Attribute",
            "help": "Category 10 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat11: bool = field(
        default=None,
        metadata={
            "name": "Cat11",
            "type": "Attribute",
            "help": "Category 11 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat12: bool = field(
        default=None,
        metadata={
            "name": "Cat12",
            "type": "Attribute",
            "help": "Category 12 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat13: bool = field(
        default=None,
        metadata={
            "name": "Cat13",
            "type": "Attribute",
            "help": "Category 13 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat14: bool = field(
        default=None,
        metadata={
            "name": "Cat14",
            "type": "Attribute",
            "help": "Category 14 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat15: bool = field(
        default=None,
        metadata={
            "name": "Cat15",
            "type": "Attribute",
            "help": "Category 15 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat16: bool = field(
        default=None,
        metadata={
            "name": "Cat16",
            "type": "Attribute",
            "help": "Category 16 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat17: bool = field(
        default=None,
        metadata={
            "name": "Cat17",
            "type": "Attribute",
            "help": "Category 17 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat18: bool = field(
        default=None,
        metadata={
            "name": "Cat18",
            "type": "Attribute",
            "help": "Category 18 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat19: bool = field(
        default=None,
        metadata={
            "name": "Cat19",
            "type": "Attribute",
            "help": "Category 19 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat20: bool = field(
        default=None,
        metadata={
            "name": "Cat20",
            "type": "Attribute",
            "help": "Category 20 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat21: bool = field(
        default=None,
        metadata={
            "name": "Cat21",
            "type": "Attribute",
            "help": "Category 21 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat22: bool = field(
        default=None,
        metadata={
            "name": "Cat22",
            "type": "Attribute",
            "help": "Category 22 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat23: bool = field(
        default=None,
        metadata={
            "name": "Cat23",
            "type": "Attribute",
            "help": "Category 23 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat24: bool = field(
        default=None,
        metadata={
            "name": "Cat24",
            "type": "Attribute",
            "help": "Category 24 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat25: bool = field(
        default=None,
        metadata={
            "name": "Cat25",
            "type": "Attribute",
            "help": "Category 25 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat26: bool = field(
        default=None,
        metadata={
            "name": "Cat26",
            "type": "Attribute",
            "help": "Category 26 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat27: bool = field(
        default=None,
        metadata={
            "name": "Cat27",
            "type": "Attribute",
            "help": "Category 27 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat28: bool = field(
        default=None,
        metadata={
            "name": "Cat28",
            "type": "Attribute",
            "help": "Category 28 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat29: bool = field(
        default=None,
        metadata={
            "name": "Cat29",
            "type": "Attribute",
            "help": "Category 29 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat30: bool = field(
        default=None,
        metadata={
            "name": "Cat30",
            "type": "Attribute",
            "help": "Category 30 rules. True if category applies. False if rules do not apply.",
        },
    )
    cat31: bool = field(
        default=None,
        metadata={
            "name": "Cat31",
            "type": "Attribute",
            "help": "Category 31 rules. True if category applies. False if rules do not apply.",
        },
    )
    restrictive_dt: str = field(
        default=None,
        metadata={
            "name": "RestrictiveDt",
            "type": "Attribute",
            "help": "Most restrictive ticketing date.",
        },
    )
    surcharge_amt: float = field(
        default=None,
        metadata={
            "name": "SurchargeAmt",
            "type": "Attribute",
            "help": "Surcharge amount",
        },
    )
    not_usacity: bool = field(
        default=None,
        metadata={
            "name": "NotUSACity",
            "type": "Attribute",
            "help": "Not USA city. True if Origin or final destination not a continental U.S. City. False if Origin or final destination a continental U.S. City.",
        },
    )
    missing_rules: bool = field(
        default=None,
        metadata={
            "name": "MissingRules",
            "type": "Attribute",
            "help": "Missing rules. True if rules are missing. False if rules are not missing.",
        },
    )


@dataclass
class OverrideCode:
    """
    Code corresponding to the type of OverridableException the user wishes to override.
    """

    value: str = field(
        default=None,
        metadata={"length": 4, "name": "value", "type": "Restriction"},
    )


@dataclass
class PassengerDetailsRef:
    """
    Reference of the Passenger
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class PassengerSeatPrice:
    """
    Only used when a passenger has a different price than the default.
    """

    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
    amount: TypeMoney = field(
        default=None,
        metadata={"required": True, "name": "Amount", "type": "Attribute"},
    )


@dataclass
class PaymentRef:
    """
    Reference to one of the air reservation payments
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class Pcc:
    """
    Specify pseudo City
    """

    override_pcc: OverridePcc = field(
        default=None, metadata={"name": "OverridePCC", "type": "Element"}
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "PointOfSale",
            "type": "Element",
        },
    )
    ticket_agency: TicketAgency = field(
        default=None, metadata={"name": "TicketAgency", "type": "Element"}
    )


@dataclass
class PenFeeType:
    dep_required: bool = field(
        default=None,
        metadata={
            "name": "DepRequired",
            "type": "Attribute",
            "help": "Deposit required. True if require. False if not required.",
        },
    )
    dep_non_ref: bool = field(
        default=None,
        metadata={
            "name": "DepNonRef",
            "type": "Attribute",
            "help": "Deposit non-refundable. True is non-refundanbe. False is refundable.",
        },
    )
    tk_non_ref: bool = field(
        default=None,
        metadata={
            "name": "TkNonRef",
            "type": "Attribute",
            "help": "Ticket non-refundable. True if non-refundanbe. False if refundable.",
        },
    )
    air_vfee: bool = field(
        default=None,
        metadata={
            "name": "AirVFee",
            "type": "Attribute",
            "help": "Carrier fee. True if carrier fee is assessed should passenger for complete all conditions for travel at fare. False if it does not exist.",
        },
    )
    cancellation: bool = field(
        default=None,
        metadata={
            "name": "Cancellation",
            "type": "Attribute",
            "help": "Cancellation. True if subject to penalty. False if no penalty.",
        },
    )
    fail_confirm_space: bool = field(
        default=None,
        metadata={
            "name": "FailConfirmSpace",
            "type": "Attribute",
            "help": "Failure to confirm space. True if subject to penalty if seats are not confirmed. False if subject to penalty if seats are confirmed.",
        },
    )
    itin_chg: bool = field(
        default=None,
        metadata={
            "name": "ItinChg",
            "type": "Attribute",
            "help": "Subject to penalty if Itinerary is changed requiring reissue of ticket. True if subject to penalty. False if no penalty if reissue required.",
        },
    )
    replace_tk: bool = field(
        default=None,
        metadata={
            "name": "ReplaceTk",
            "type": "Attribute",
            "help": "Replace ticket. True if subject to penalty, if replacement of lost ticket / exchange order. False if no penalty, if replacement of lost ticket or exchange order.",
        },
    )
    applicable: bool = field(
        default=None,
        metadata={
            "name": "Applicable",
            "type": "Attribute",
            "help": "Applicable. True if amount specified is applicable. Flase if amount specified is not applicable.",
        },
    )
    applicable_to: bool = field(
        default=None,
        metadata={
            "name": "ApplicableTo",
            "type": "Attribute",
            "help": "Applicable to penalty or deposit. True if amount specified applies to penalty. False if amount specified applies to deposit.",
        },
    )
    amt: float = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Attribute",
            "help": "Amount of penalty. If XXX.XX then it is an amount. If it is XX then is is a percenatge. Eg 100.00 or 000100.",
        },
    )
    type: str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "help": "Type of penalty. If it is D then dollar. If it is P then percentage.",
        },
    )
    currency: str = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "help": "Currency code of penalty (e.g. USD).",
        },
    )


@dataclass
class Penalty:
    amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "help": "Penalty Amount",
        },
    )
    penalty_type: str = field(
        default=None,
        metadata={
            "name": "PenaltyType",
            "type": "Attribute",
            "help": "This is the PPC (Price Processing Code)code.",
        },
    )


@dataclass
class PenaltyInformation:
    carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "help": "Fare-owning carrier",
        },
    )
    fare_basis: str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "help": "Unique identifier that provides the association to the fare amount and fare rules.",
        },
    )
    fare_component: int = field(
        default=None,
        metadata={
            "name": "FareComponent",
            "type": "Attribute",
            "help": "A portion of a journey or itinerary between two consecutive fare break points.",
        },
    )
    priceable_unit: int = field(
        default=None,
        metadata={
            "name": "PriceableUnit",
            "type": "Attribute",
            "help": "Identifies FareComponents that are priced together",
        },
    )
    board_point: TypeIatacode = field(
        default=None,
        metadata={
            "name": "BoardPoint",
            "type": "Attribute",
            "help": "Origin for the FareComponent",
        },
    )
    off_point: TypeIatacode = field(
        default=None,
        metadata={
            "name": "OffPoint",
            "type": "Attribute",
            "help": "Destination for the FareComponent",
        },
    )
    minimum_change_fee: TypeMoney = field(
        default=None,
        metadata={
            "name": "MinimumChangeFee",
            "type": "Attribute",
            "help": "Estimated minimum change fee associated with the fare component. Can be overridden by ChangeFeeApplicationCodes for other fare components.",
        },
    )
    maximum_change_fee: TypeMoney = field(
        default=None,
        metadata={
            "name": "MaximumChangeFee",
            "type": "Attribute",
            "help": "Estimated maximum change fee associated with the fare component. Can be overridden by ChangeFeeApplicationCodes for other fare components.",
        },
    )
    filed_currency: TypeCurrency = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "help": "Currency of the filed change fee",
        },
    )
    conversion_rate: float = field(
        default=None,
        metadata={
            "name": "ConversionRate",
            "type": "Attribute",
            "help": "Conversion rate from filed change fee currency to reissue location currency",
        },
    )
    refundable: bool = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
            "help": "Answers whether the FareComponent is refundable",
        },
    )
    change_fee_application_code: str = field(
        default=None,
        metadata={
            "name": "ChangeFeeApplicationCode",
            "type": "Attribute",
            "help": 'Unique code associated with the PenaltyInformation text which defines how fees will be applied/calculated. E.g. J2 translates to "From among all fare components, changed and unchanged...."',
        },
    )


@dataclass
class PermittedCabins:
    cabin_class: List[CabinClass] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 5,
            "name": "CabinClass",
            "type": "Element",
        },
    )


@dataclass
class PermittedCarriers:
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "Carrier",
            "type": "Element",
        },
    )


@dataclass
class PersonName:
    """
    Customer name field
    """

    first: StringLength1to64 = field(
        default=None,
        metadata={
            "name": "First",
            "type": "Attribute",
            "help": "Person First Name.",
        },
    )
    last: StringLength1to64 = field(
        default=None,
        metadata={
            "required": True,
            "name": "Last",
            "type": "Attribute",
            "help": "Person Last Name.",
        },
    )
    prefix: StringLength1to16 = field(
        default=None,
        metadata={
            "name": "Prefix",
            "type": "Attribute",
            "help": "Person Name prefix.",
        },
    )


@dataclass
class PersonNameSearch:
    """
    Customer name field
    """

    last: StringLength1to64 = field(
        default=None,
        metadata={
            "required": True,
            "name": "Last",
            "type": "Attribute",
            "help": "Person Last Name to be searched for Flight Pass content.",
        },
    )


@dataclass
class PocketItineraryRemark(TypeAssociatedRemarkWithSegmentRef):
    pass


@dataclass
class PolicyCodesList:
    policy_code: List[TypePolicyCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 10,
            "name": "PolicyCode",
            "type": "Element",
            "help": "A code that indicates why an item was determined to be ‘out of policy’.",
        },
    )


@dataclass
class PreferredCabins:
    cabin_class: CabinClass = field(
        default=None,
        metadata={"required": True, "name": "CabinClass", "type": "Element"},
    )


@dataclass
class PreferredCarriers:
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "Carrier",
            "type": "Element",
        },
    )


@dataclass
class PriceChangeType:
    """
    Indicates a price change is found in Fare Control Manager
    """

    amount: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Amount",
            "type": "Attribute",
            "help": "Contains the currency and amount information. Assume the amount is added unless a hyphen is present to indicate subtraction.",
        },
    )
    carrier: str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "help": "Contains carrier code information",
        },
    )
    segment_ref: str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
            "help": "Contains segment reference information",
        },
    )


@dataclass
class PriceRange:
    default_currency: bool = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Attribute",
            "help": "Indicates if the currency code of StartPrice / EndPrice is the default currency code",
        },
    )
    start_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "StartPrice",
            "type": "Attribute",
            "help": "Price range start value",
        },
    )
    end_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "EndPrice",
            "type": "Attribute",
            "help": "Price range end value",
        },
    )


@dataclass
class PricingDetails:
    """
    Used for rapid reprice. This is a response element. Additional information about how pricing was obtain, messages, etc. Providers: 1G/1V/1P/1S/1A
    """

    advisory_message: List[str] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AdvisoryMessage",
            "type": "Element",
            "help": "Advisory messages returned from the host.",
        },
    )
    endorsement_text: List[str] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "EndorsementText",
            "type": "Element",
            "help": "Endorsement text returned from the host.",
        },
    )
    waiver_text: str = field(
        default=None,
        metadata={
            "name": "WaiverText",
            "type": "Element",
            "help": "Waiver text returned from the host.",
        },
    )
    low_fare_pricing: bool = field(
        default="false",
        metadata={
            "name": "LowFarePricing",
            "type": "Attribute",
            "help": "This tells if Low Fare Finder was used.",
        },
    )
    low_fare_found: bool = field(
        default="false",
        metadata={
            "name": "LowFareFound",
            "type": "Attribute",
            "help": "This tells if the lowest fare was found.",
        },
    )
    penalty_applies: bool = field(
        default="false",
        metadata={
            "name": "PenaltyApplies",
            "type": "Attribute",
            "help": "This tells if penalties apply.",
        },
    )
    discount_applies: bool = field(
        default="false",
        metadata={
            "name": "DiscountApplies",
            "type": "Attribute",
            "help": "This tells if a discount applies.",
        },
    )
    itinerary_type: TypeItineraryCode = field(
        default=None,
        metadata={
            "name": "ItineraryType",
            "type": "Attribute",
            "help": "Values allowed are International or Domestic. This tells if the itinerary is international or domestic.",
        },
    )
    validating_vendor_code: TypeCarrier = field(
        default=None,
        metadata={
            "name": "ValidatingVendorCode",
            "type": "Attribute",
            "help": "The vendor code of the validating carrier.",
        },
    )
    for_ticketing_on_date: str = field(
        default=None,
        metadata={
            "name": "ForTicketingOnDate",
            "type": "Attribute",
            "help": "The ticketing date of the itinerary.",
        },
    )
    last_date_to_ticket: str = field(
        default=None,
        metadata={
            "name": "LastDateToTicket",
            "type": "Attribute",
            "help": "The last date to issue the ticket.",
        },
    )
    form_of_refund: TypeFormOfRefund = field(
        default=None,
        metadata={
            "name": "FormOfRefund",
            "type": "Attribute",
            "help": "How the refund will be issued. Values will be MCO or FormOfPayment",
        },
    )
    account_code: str = field(
        default=None, metadata={"name": "AccountCode", "type": "Attribute"}
    )
    bankers_selling_rate: float = field(
        default=None,
        metadata={
            "name": "BankersSellingRate",
            "type": "Attribute",
            "help": "The selling rate at time of quote.",
        },
    )
    pricing_type: TypePricingType = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Attribute",
            "help": "Ties with the RepricingModifiers sent in the request and tells how the itinerary was priced.",
        },
    )
    conversion_rate: float = field(
        default=None,
        metadata={
            "name": "ConversionRate",
            "type": "Attribute",
            "help": "The conversion rate at the time of quote.",
        },
    )
    rate_of_exchange: float = field(
        default=None,
        metadata={
            "name": "RateOfExchange",
            "type": "Attribute",
            "help": "The exchange rate at time of quote.",
        },
    )
    original_ticket_currency: TypeCurrency = field(
        default=None,
        metadata={
            "name": "OriginalTicketCurrency",
            "type": "Attribute",
            "help": "The currency of the original ticket.",
        },
    )


@dataclass
class PrintBlankFormItinerary:
    """
    Produce a customized itinerary/Invoice document in blank form format.
    """

    include_description: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "IncludeDescription",
            "type": "Attribute",
            "help": "If it is true then document will be printed including descriptions.",
        },
    )
    include_header: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "IncludeHeader",
            "type": "Attribute",
            "help": "If it is true then document will be printed including it's header.",
        },
    )


@dataclass
class ProhibitedCabins:
    cabin_class: List[CabinClass] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 3,
            "name": "CabinClass",
            "type": "Element",
        },
    )


@dataclass
class ProhibitedCarriers:
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "Carrier",
            "type": "Element",
        },
    )


@dataclass
class PromoCode:
    """
    A container to specify Promotional code with Provider code and Supplier code.
    """

    code: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Code",
            "type": "Attribute",
            "help": "To be used to specify Promotional Code.",
        },
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderCode",
            "type": "Attribute",
            "help": "To be used to specify Provider Code.",
        },
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "SupplierCode",
            "type": "Attribute",
            "help": "To be used to specify Supplier Code.",
        },
    )


@dataclass
class RailCoachDetails:
    rail_coach_number: str = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
            "help": "Rail coach number for the returned coach details.",
        },
    )
    available_rail_seats: str = field(
        default=None,
        metadata={
            "name": "AvailableRailSeats",
            "type": "Attribute",
            "help": "Number of available seats present in this rail coach.",
        },
    )
    rail_seat_map_availability: bool = field(
        default=None,
        metadata={
            "name": "RailSeatMapAvailability",
            "type": "Attribute",
            "help": "Indicates if seats are available in this rail coach which can be mapped.",
        },
    )


@dataclass
class RefundAccessCode:
    """
    For some vendors a code/password is required to avail any amount retained during refund.User can define their own password too This attribute will be used to show/accept this code.
    """

    value: str = field(
        default=None,
        metadata={
            "min_length": "1",
            "max_length": "32",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class Restriction:
    """
    Fare Reference associated with the BookingRules
    """

    days_of_week_restriction: List[
        "Restriction.DaysOfWeekRestriction"
    ] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "DaysOfWeekRestriction",
            "type": "Element",
        },
    )
    restriction_passenger_types: List[
        "Restriction.RestrictionPassengerTypes"
    ] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RestrictionPassengerTypes",
            "type": "Element",
        },
    )

    @dataclass
    class DaysOfWeekRestriction:
        restriction_exists_ind: bool = field(
            default=None,
            metadata={"name": "RestrictionExistsInd", "type": "Attribute"},
        )
        application: str = field(
            default=None, metadata={"name": "Application", "type": "Attribute"}
        )
        include_exclude_use_ind: bool = field(
            default=None,
            metadata={"name": "IncludeExcludeUseInd", "type": "Attribute"},
        )

    @dataclass
    class RestrictionPassengerTypes:
        max_nbr_travelers: str = field(
            default=None,
            metadata={"name": "MaxNbrTravelers", "type": "Attribute"},
        )
        total_nbr_ptc: str = field(
            default=None, metadata={"name": "TotalNbrPTC", "type": "Attribute"}
        )


@dataclass
class RoutingRules:
    """
    Rules related to routing
    """

    routing: List["RoutingRules.Routing"] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Routing",
            "type": "Element",
        },
    )

    @dataclass
    class Routing:
        direction_info: List["RoutingRules.Routing.DirectionInfo"] = field(
            default_factory=list,
            metadata={
                "min_occurs": 0,
                "max_occurs": 999,
                "name": "DirectionInfo",
                "type": "Element",
            },
        )
        routing_constructed_ind: bool = field(
            default=None,
            metadata={"name": "RoutingConstructedInd", "type": "Attribute"},
        )
        number: str = field(
            default=None, metadata={"name": "Number", "type": "Attribute"}
        )
        routing_restriction: str = field(
            default=None,
            metadata={"name": "RoutingRestriction", "type": "Attribute"},
        )

        @dataclass
        class DirectionInfo:
            location_code: TypeIatacode = field(
                default=None,
                metadata={"name": "LocationCode", "type": "Attribute"},
            )
            direction: str = field(
                default=None,
                metadata={"name": "Direction", "type": "Attribute"},
            )


@dataclass
class RuleCharges:
    """
    Container for rules related to charges such as deposits, surcharges, penalities, etc..
    """

    penalty_type: str = field(
        default=None, metadata={"name": "PenaltyType", "type": "Attribute"}
    )
    departure_status: str = field(
        default=None, metadata={"name": "DepartureStatus", "type": "Attribute"}
    )
    amount: TypeMoney = field(
        default=None, metadata={"name": "Amount", "type": "Attribute"}
    )
    percent: float = field(
        default=None, metadata={"name": "Percent", "type": "Attribute"}
    )
    more_rules_present: bool = field(
        default=None,
        metadata={
            "name": "MoreRulesPresent",
            "type": "Attribute",
            "help": "If true, specifies that advance purchase information will be present in fare rules.",
        },
    )


@dataclass
class Rules:
    rules_text: str = field(
        default=None,
        metadata={
            "name": "RulesText",
            "type": "Element",
            "help": "Rules text",
        },
    )


@dataclass
class SearchTraveler(TypePassengerType):
    air_seat_assignment: List[AirSeatAssignment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSeatAssignment",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )


@dataclass
class SeatInformation:
    """
    Additional information about seats. Providers: 1G, 1V, 1P, 1J,ACH
    """

    power: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Power",
            "type": "Element",
            "help": "Detail about any electrical power the seat might have. For example: No Power Providers: 1G, 1V, 1P, 1J",
        },
    )
    video: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Video",
            "type": "Element",
            "help": "Detail about any video components the seat might have. For example: No Video Providers: 1G, 1V, 1P, 1J",
        },
    )
    type: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Element",
            "help": "Detail about the type of seat. For example: Exit Row, Standard, etc. Providers: 1G, 1V, 1P, 1J",
        },
    )
    description: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Description",
            "type": "Element",
            "help": "Detailed description of the seat. Providers: 1G, 1V, 1P, 1J",
        },
    )
    rating: "SeatInformation.Rating" = field(
        default=None,
        metadata={
            "required": True,
            "name": "Rating",
            "type": "Element",
            "help": "Definition of the seat rating. Providers: 1G, 1V, 1P, 1J",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )

    @dataclass
    class Rating:
        number: int = field(
            default=None,
            metadata={
                "required": True,
                "name": "Number",
                "type": "Attribute",
                "help": "Numerical rating of the seat from 1 to 5 with 1 being bad and 5 being good. Providers: 1G, 1V, 1P, 1J",
            },
        )


@dataclass
class SegmentIndex(int):
    """
    Identifies the segment that is part of this group
    """

    pass


@dataclass
class ServiceSubGroup:
    """
    The Service Sub Group of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH
    """

    code: str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "help": "The Service Sub Group Code of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        },
    )


@dataclass
class SpecificSeatAssignment:
    """
    Request object used to specify a specific seat
    """

    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "help": "The passenger that this seat assignment is for",
        },
    )
    segment_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "SegmentRef",
            "type": "Attribute",
            "help": "The segment that we will assign this seat on",
        },
    )
    flight_detail_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "FlightDetailRef",
            "type": "Attribute",
            "help": "The Flight Detail ref of the AirSegment used when requesting seats on Change of Guage flights",
        },
    )
    seat_id: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "SeatId",
            "type": "Attribute",
            "help": "The actual seat ID that is being requested. Special Characters are not supported in this field.",
        },
    )
    rail_coach_number: str = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
            "help": "Coach number for which rail seatmap/coachmap is returned.",
        },
    )


@dataclass
class SpecificTimeTable:
    flight_origin: "SpecificTimeTable.FlightOrigin" = field(
        default=None, metadata={"name": "FlightOrigin", "type": "Element"}
    )
    flight_destination: "SpecificTimeTable.FlightDestination" = field(
        default=None, metadata={"name": "FlightDestination", "type": "Element"}
    )
    start_date: str = field(
        default=None,
        metadata={"required": True, "name": "StartDate", "type": "Attribute"},
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata={"required": True, "name": "Carrier", "type": "Attribute"},
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "FlightNumber",
            "type": "Attribute",
        },
    )

    @dataclass
    class FlightOrigin:
        airport: Airport = field(
            default=None,
            metadata={"required": True, "name": "Airport", "type": "Element"},
        )

    @dataclass
    class FlightDestination:
        airport: Airport = field(
            default=None,
            metadata={"required": True, "name": "Airport", "type": "Element"},
        )


@dataclass
class SplitTicketingSearch:
    """
    SplitTicketingSearch is optional. Used to return both One-Way and Roundtrip fares in a single search response. Applicable to 1G, 1V, 1P only, the price points results path, and a simple roundtrip search only. Cannot be used in combination with Flex options.
    """

    round_trip: int = field(
        default=None,
        metadata={
            "name": "RoundTrip",
            "type": "Attribute",
            "help": "Percentage of Roundtrip price points to be returned in the search response. This should be an even number. The One-Way price points returned in the response would be evenly distributed between the outbound and the inbound.",
        },
    )


@dataclass
class SponsoredFltInfo:
    """
    This describes whether the segment is determined to be a sponsored flight. The SponsoredFltInfo node will only come back for Travelport UIs and not for other customers.
    """

    sponsored_lnb: int = field(
        default=None,
        metadata={
            "required": True,
            "name": "SponsoredLNB",
            "type": "Attribute",
            "help": "The line number of the sponsored flight item",
        },
    )
    neutral_lnb: int = field(
        default=None,
        metadata={
            "required": True,
            "name": "NeutralLNB",
            "type": "Attribute",
            "help": "The neutral line number for the flight item.",
        },
    )
    flt_key: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "FltKey",
            "type": "Attribute",
            "help": "The unique identifying key for the sponsored flight.",
        },
    )


@dataclass
class Tax:
    """
    Taxes for Land Charges
    """

    category: str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "help": "The tax category represents a valid IATA tax code.",
        },
    )
    amount: TypeMoney = field(
        default=None,
        metadata={"required": True, "name": "Amount", "type": "Attribute"},
    )


@dataclass
class TaxInfo(TypeTaxInfo):
    """
    The tax information for a
    """

    pass


@dataclass
class TextInfo:
    """
    Information on baggage as published by carrier.
    """

    text: List[TypeGeneralText] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Text",
            "type": "Element",
        },
    )
    title: str = field(
        default=None, metadata={"name": "Title", "type": "Attribute"}
    )


@dataclass
class TicketEndorsement:
    value: TypeEndorsement = field(
        default=None,
        metadata={"required": True, "name": "Value", "type": "Attribute"},
    )


@dataclass
class TicketValidity:
    """
    To be used to pass the selected segment
    """

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
class TicketingModifiersRef:
    """
    Reference to a shared list of Ticketing Modifers
    """

    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class TravelArranger:
    """
    Details of Travel Arranger
    """

    company_short_name: str = field(
        default=None,
        metadata={
            "name": "CompanyShortName",
            "type": "Attribute",
            "help": "Company Name",
        },
    )
    code: str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "help": "IATA Code for Arranger",
        },
    )


@dataclass
class TypeAlliance:
    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeAnchorFlightData:
    """
    To support Anchor flight search contain the anchor flight details. Supported providers 1P, 1J
    """

    airline_code: TypeCarrier = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirlineCode",
            "type": "Attribute",
            "help": "Indicates Anchor flight carrier code",
        },
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "FlightNumber",
            "type": "Attribute",
            "help": "Indicates Anchor flight number",
        },
    )
    connection_indicator: bool = field(
        default=None,
        metadata={
            "name": "ConnectionIndicator",
            "type": "Attribute",
            "help": "Indicates that the Anchor flight has any connecting flight or not",
        },
    )


@dataclass
class TypeApplicableSegment:
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    air_itinerary_details_ref: TypeRef = field(
        default=None,
        metadata={"name": "AirItineraryDetailsRef", "type": "Attribute"},
    )
    booking_counts: str = field(
        default=None,
        metadata={
            "name": "BookingCounts",
            "type": "Attribute",
            "help": "Classes of service and their counts.",
        },
    )


@dataclass
class TypeAssessIndicator:
    """
    The type of AssessIndicator
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeAtpcoglobalIndicator:
    """
    Enumeration of ATPCO global indicators
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeAvailabilitySource:
    """
    Availability Source value for Sell.
    """

    value: str = field(
        default=None,
        metadata={"max_length": "1", "name": "value", "type": "Restriction"},
    )


@dataclass
class TypeBackOffice:
    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeBillingDetailsDataType:
    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeBillingDetailsName:
    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeBooking:
    """
    Type of booking
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeBrandId:
    """
    The unique identifier of the brand
    """

    value: str = field(
        default=None,
        metadata={
            "min_length": "1",
            "max_length": "19",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class TypeBulkTicketModifierType:
    """
    Bulk ticketing modifier type.
    """

    suppress_on_fare_calc: bool = field(
        default=None,
        metadata={
            "name": "SuppressOnFareCalc",
            "type": "Attribute",
            "help": "Optional attribute to allow a modifier impact such as Bulk Ticketing to have information suppressed on the Fare Calc when generating supporting documents Check the specific host system which may or may not support this function",
        },
    )


@dataclass
class TypeCarCode:
    """
    Car code value. Maximum 15 characters. Applicable provider is 1G and 1V
    """

    value: str = field(
        default=None,
        metadata={"max_length": "15", "name": "value", "type": "Restriction"},
    )


@dataclass
class TypeCarrierCode:
    """
    Defines the type of booking codes (Primary or Secondary)
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeConnectionIndicator:
    """
    Types of connection indicator : AvailabilityAndPricing : Specified availability and pricing connection; TurnAround : Specified turn around; Stopover : Specified stopover;
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeCouponStatus:
    """
    ATA/IATA Standard coupon status.
    """

    value: str = field(
        default=None,
        metadata={"length": 1, "name": "value", "type": "Restriction"},
    )


@dataclass
class TypeDestinationCode:
    """
    List of valid Destination Codes.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeDisplayCategory:
    """
    Type of booking
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeDiversity:
    """
    Used in Low Fare Search to better promote unique results
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeEmdnumber:
    """
    13 character EMD number
    """

    value: str = field(
        default=None,
        metadata={"length": 13, "name": "value", "type": "Restriction"},
    )


@dataclass
class TypeEquipment:
    """
    3 Letter equipment code (sometimes vary by carrier)
    """

    value: str = field(
        default=None,
        metadata={"length": 3, "name": "value", "type": "Restriction"},
    )


@dataclass
class TypeEticketability:
    """
    Defines the ability to eticket an entity (Yes, No, Required, Ticketless)
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFacility:
    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFailureInfo:
    code: int = field(
        default=None,
        metadata={"required": True, "name": "Code", "type": "Attribute"},
    )
    message: str = field(
        default=None,
        metadata={"required": True, "name": "Message", "type": "Attribute"},
    )


@dataclass
class TypeFareBreak:
    """
    Types of fare break.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFareDirectionality:
    """
    A fare's directionality (e.g. one-way, return )
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFareDiscount:
    """
    Fare Discount Calculation Method
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFareGuarantee:
    """
    The status of a fare
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFarePenalty:
    """
    Penalty applicable on a Fare for change/ cancellation etc- expressed in both Money and Percentage.
    """

    amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "help": "The penalty (if any) - expressed as the actual amount of money. Both Amount and Percentage can be present.",
        },
    )
    percentage: TypePercentageWithDecimal = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "help": "The penalty (if any) - expressed in percentage. Both Amount and Percentage can be present.",
        },
    )
    penalty_applies: str = field(
        default=None, metadata={"name": "PenaltyApplies", "type": "Attribute"}
    )
    no_show: bool = field(
        default=None,
        metadata={
            "name": "NoShow",
            "type": "Attribute",
            "help": "The No Show penalty (if any) to change/cancel the fare.",
        },
    )


@dataclass
class TypeFareRestrictionType:
    """
    The type of fare restriction
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFareRuleCategoryCode:
    """
    Kestrel Long Fare Rule Category Codes
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFareRuleFailureInfoReason:
    """
    Reason codes for Fare rule failure. Following values will be supported. MinimumStayFailure, AdvPurchaseFailure, PICTypeFailure [Passenger Identification Code Failure], StopoverTransferFailure, DateSeasonalityFailure, RoutingFailure, MileageFailure, DayTimeFailure, OpenJawUsageFailure, IndirectTravelProvision, SalesRestrictionNotMet, FICNAFare, HIFFailure [Higher Intermediate Fare/Point or Mileage Exceptions failures], IntlSurfaceSector, CurrencyUsageFailure, DiscountApplFailure, FootNoteFailure, DayTimeApplCatNotMet, DayTimeApplCatIncomplete, SeasonalityCatNotMet, SeasonalityCatIncomplete, FlightApplCatNotMet, FlightApplCatIncomplete, AdvResvAdvTicketCatNotMet, AdvResvAdvTicketCatIncomplete, BookingClassFailure, MinStayCatNotMet, MinStayCatIncomplete, StopoverCatNotMet, StopoverCatIncomplete, PermittedCombinationCatNotMet, PermittedCombinationCatNotIncomplete, BlackoutCatNotMet, BlackoutCatNotIncomplete, AccomTvlReqCatNotMet, AccomTvlReqCatIncomplete, SalesRestCatNotMet, SalesRestCatIncomplete, EligibilityCatNotMet, EligibilityCatIncomplete, TransfersCatNotMet, TransfersCatIncomplete, TransfersRoutingFailure, HIPMileageCatNotMet [Higher Intermediate Point or Mileage Exception categories not met], HIPMileageCatIncomplete [Higher Intermediate Point or Mileage Exceptions categories incomplete], ChildDiscountCatNotMet, ChildDiscountCatIncomplete, TourConductorDiscCatNotMet, TourConductorDiscCatIncomplete, AgentDiscountCatNotMet, AgentDiscountCatIncomplete, OtherDiscountCatNotMet, OtherDiscountCatIncomplete, MiscFareTagCatNotMet, MiscFareTagCatIncomplete, FareByRuleCatNotMet, FareByRuleCatIncomplete, VisitCountryCatNotMet, VisitCountryCatIncomplete, NegFaresCatNotMet, NegFaresCatIncomplete, OthFailurePTCFailed, OthFailureRecFailed, CombineabilityFailure, TravelRestrictionNotMet, SurchargesNotMet, MaximumStayFailure, FareUsageFailure, IATAFareNotValid, RecordOneFailure, Cat01EligibilityFailure, FlightApplicationsFailure, FootNoteFailure, Cat11BlackOutfailure, Cat13AccompaniedTravelRequirementFailure, Cat19ChildDiscountFailure, Cat20TourDiscountFailure, Cat21AgentDiscountApplicationFail, YYSuppressionTableFailure, HostUseOnly87, HostUseOnly88, HostUseOnly89, HostUseOnly90, HostUseOnly99, HostUseOnly100, HostUseOnly105, HostUseOnly108, HostUseOnly111, HostUseOnly112, HostUseOnly113, HostUseOnly114, HostUseOnly121, HostUseOnly122, SpareForFutureIndicators, YYSuppressionTableFailed, HIPCheckFailed, TourCodeFail, AbonnmentFareFailure, FailedSurfaceSector, IndirectTravelFailed, FailedCurrencyUsage, CAT12NotMet
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFareRuleType:
    """
    The valid rule types
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFareSearchOption:
    """
    Fare Search option indicator.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFareStatusCode:
    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFareTripType:
    """
    RoundTheWorld -- round the world fare
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFareTypeCode:
    """
    ATPCO fare type code (e.g. XPN)
    """

    value: str = field(
        default=None,
        metadata={
            "min_length": "1",
            "max_length": "5",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class TypeFaresIndicator:
    """
    Defines the type of fares to return (Only public fares, Only private fares, Only agency private fares, Only airline private fares or all fares)
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeFeeApplication:
    """
    The type of FeeApplication
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeIgnoreStopOver:
    """
    The stop over inluded to quote fare.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeInventoryRequest:
    """
    The valid inventory types are Seamless - A, DirectAccess - B, Basic - C
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeItinerary:
    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeItineraryOption:
    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeLowFareSearchId:
    """
    Low Fare Search Id
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeMaxJourneyTime:
    """
    Maximum Journey Time for this leg (in hours) 0-99.
    """

    value: int = field(
        default=None,
        metadata={
            "min_inclusive": "0",
            "max_inclusive": "99",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class TypeMealService:
    """
    Available Meal Service
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeMileOrRouteBasedFare:
    """
    Whether the fare is Mile or Route based
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeNativeSearchModifier:
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderCode",
            "type": "Attribute",
            "help": "The host for which the NativeModfier being added to",
        },
    )


@dataclass
class TypeNonAirReservationRef:
    locator_code: TypeLocatorCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "LocatorCode",
            "type": "Attribute",
        },
    )


@dataclass
class TypeNumberOfPassengers:
    value: int = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeOverrideOption:
    """
    Below mentioned values are only supported in schema. "SuppressItineraryInvoicePrinting" - Suppress sending itinerary/invoice document to a printer. The itinerary/invoice can be sent to a printer at a future time using duplicate itinerary/invoice. This is used by Worldspan. "PrintTerminalCodes" - Produces an itinerary/invoice or pocket itinerary that includes departure and /or arrival terminal codes. This is used by Worldspan. "PrintDirectAccessRecordLocator" - Print record locator for direct access carriers. This option prints the record locator below the segmnet information. This option can be used along with PrintProviderReservationRecordLocator as well. This is used by Worldspan. "PrintProviderReservationRecordLocator" - Print PNR record locator on documents. This option can be used along with PrintDirectAccessRecordLocator as well. This is used by Worldspan. "ReIssueTicketedStoredFare" - This modifier is used to issue a ticket against a ticket record that was previously issued. This is used by Worldspan. "PrintFrequentTravelerNumber" - This modifier is used to print frequent traveller number. This is used by Worldspan. "SuppressInvoiceNumberPrinting" - This modifier prevents the invoice number from printing on documents. This is used by Worldspan. "PrintItineraryInvoicePerTraveler" - Issues itinerary/invoice for per traveler. This is used by Worldspan. "PrintItineraryInvoicePerSurname" - Issues itinerary/invoice for per surname. This is used by Worldspan. "PrintMultipleCustomizedNameData" - Prints names individually with associated customized name data on documents. This is used by Worldspan. "PrintInvoiceRemarkOnly" - Prints invoice remark only. overrides the system remarks and directs only specific remarks selected to print on documents. This is used by Worldspan. "PrintItineraryRemarkOnly" - Prints itinerary remark only. This is used by Worldspan. "PrintBaggageAllowance" - Print the baggage allowance field with the autoprice or stored in the ticket record on credit memos/pocket Itineraries or itinerary invoices issued in conjunction with a non electronic ticket. This is used by Worldspan.
    """

    value: str = field(
        default=None,
        metadata={"max_length": "50", "name": "value", "type": "Restriction"},
    )


@dataclass
class TypePassengerTicketNumber:
    """
    Reference Ticket Number
    """

    value: str = field(
        default=None,
        metadata={
            "min_length": "1",
            "max_length": "13",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class TypePosition:
    """
    Facility position with respect to position within the aircraft cabin. Possible values are – Left, Right, Center, Left Center, Right Center
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypePricingMethod:
    """
    The method at which the pricing data was acquired
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypePrivateFare:
    """
    List the types of private fares, Agency private fare, Airline private Fare and Unknown. Also, this enumaration list includes PrivateFare to indetify private fares for GDSs where we can not identify specific private fares.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypePurposeCode:
    """
    List of valid Purpose Codes.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeRefundabilityValue:
    """
    Currently returned: FullyRefundable (1G,1V), RefundableWithPenalty (1G,1V), Refundable (1P,1J), NonRefundable (1G,1V,1P,1J).
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeReportingType:
    """
    The valid reporting types
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeRowLocation:
    """
    Facility Position with respect to a Row. Possible values are Rear, Front
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeSeatAvailability:
    """
    Seat availability info of a seat map
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeSegmentRef:
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class TypeStayUnit:
    """
    Units for the Length of Stay
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeSubCode:
    """
    Used to specify an OB fee as exempt.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeTcrnumber:
    """
    The identifying number for a Ticketless Air Reservation
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeTcrstatus:
    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeTextElement:
    type: str = field(
        default=None,
        metadata={"required": True, "name": "Type", "type": "Attribute"},
    )
    language_code: str = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Attribute",
            "help": "ISO 639 two-character language codes are used to retrieve specific information in the requested language. For Rich Content and Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE, DECH can also be used. Only certain services support this attribute. Providers: ACH, RCH, 1G, 1V, 1P, 1J.",
        },
    )


@dataclass
class TypeTicketDesignator:
    """
    Ticket Designator type.Size can be up to 20 characters
    """

    value: str = field(
        default=None,
        metadata={
            "min_length": "0",
            "max_length": "20",
            "name": "value",
            "type": "Restriction",
        },
    )


@dataclass
class TypeTicketModifierAccountingType:
    """
    Ticketing Modifier used to add accounting - discount information.
    """

    value: str = field(
        default=None,
        metadata={"required": True, "name": "Value", "type": "Element"},
    )


@dataclass
class TypeTicketModifierAmountType:
    """
    Ticketing Modifier used to alter a fare amount before or during the ticketing operation.
    """

    amount: TypeMoney = field(
        default=None,
        metadata={
            "required": True,
            "name": "Amount",
            "type": "Attribute",
            "help": "Amount associated with a ticketing modifier",
        },
    )


@dataclass
class TypeTicketModifierPercentType:
    """
    Ticketing Modifier used to alter a fare percentage before or during the ticketing operation.
    """

    percent: TypePercentageWithDecimal = field(
        default=None,
        metadata={
            "required": True,
            "name": "Percent",
            "type": "Attribute",
            "help": "Percent associated with a ticketing modifier",
        },
    )


@dataclass
class TypeTicketModifierValueType:
    """
    Ticketing Modifier used to add value discount information.
    """

    value: str = field(
        default=None,
        metadata={"required": True, "name": "Value", "type": "Element"},
    )
    net_fare_value: bool = field(
        default=None,
        metadata={
            "name": "NetFareValue",
            "type": "Attribute",
            "help": "Treat the value as net fare discount information",
        },
    )


@dataclass
class TypeTourCode:
    """
    Tour code value. Maximum 15 characters
    """

    value: str = field(
        default=None,
        metadata={"max_length": "15", "name": "value", "type": "Restriction"},
    )


@dataclass
class TypeTripType:
    """
    Used in Low Fare Search to better target the results
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeUnitOfMeasure:
    value: float = field(
        default=None, metadata={"name": "Value", "type": "Attribute"}
    )
    unit: str = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Attribute",
            "help": "Unit values would be lb,Lb,kg etc.",
        },
    )


@dataclass
class TypeUnitWeight:
    """
    The available units of weight
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeValueCode:
    """
    Value code value. Maximum 15 characters. Applicable provider is 1G and 1V
    """

    value: str = field(
        default=None,
        metadata={"max_length": "15", "name": "value", "type": "Restriction"},
    )


@dataclass
class TypeVarianceIndicator:
    """
    Type code for Variance.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class TypeVarianceType:
    """
    Type code for Variance.
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class UpsellBrand:
    """
    Upsell brand reference
    """

    fare_basis: str = field(
        default=None, metadata={"name": "FareBasis", "type": "Attribute"}
    )
    fare_info_ref: str = field(
        default=None, metadata={"name": "FareInfoRef", "type": "Attribute"}
    )


@dataclass
class Url:
    type: str = field(
        default=None, metadata={"name": "Type", "type": "Attribute"}
    )


@dataclass
class Urlinfo:
    """
    Contains the text and URL of baggage as published by carrier.
    """

    text: List[TypeGeneralText] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Text",
            "type": "Element",
        },
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "URL",
            "type": "Element",
        },
    )


@dataclass
class ValueDetails:
    name: str = field(
        default=None,
        metadata={"required": True, "name": "Name", "type": "Attribute"},
    )
    value: str = field(
        default=None,
        metadata={"required": True, "name": "Value", "type": "Attribute"},
    )


@dataclass
class VoidFailureInfo:
    ticket_number: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "TicketNumber",
            "type": "Attribute",
        },
    )
    code: int = field(
        default=None, metadata={"name": "Code", "type": "Attribute"}
    )


@dataclass
class VoidResultInfo:
    """
    List of Successful Or Failed void document results.
    """

    failure_remark: str = field(
        default=None,
        metadata={
            "name": "FailureRemark",
            "type": "Element",
            "help": "Container to show all provider failure information.",
        },
    )
    result_type: str = field(
        default=None,
        metadata={
            "name": "ResultType",
            "type": "Attribute",
            "help": "Successful Or Failed result indicator.",
        },
    )


@dataclass
class Yield:
    """
    An identifier which identifies yield made on original pricing. It can be a flat amount of original price. The value of Amount can be negative. Negative value implies a discount.
    """

    amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "help": "Yield per passenger level in Default Currency for this entity.",
        },
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "help": "Reference to a booking traveler for which Yield is applied.",
        },
    )


@dataclass
class Affiliations:
    """
    Affiliations related for pre pay profiles
    """

    travel_arranger: List[TravelArranger] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TravelArranger",
            "type": "Element",
        },
    )


@dataclass
class AirAvailInfo:
    """
    Matches class of service information with availability counts. Only provided on search results.
    """

    booking_code_info: List[BookingCodeInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BookingCodeInfo",
            "type": "Element",
        },
    )
    fare_token_info: List["AirAvailInfo.FareTokenInfo"] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareTokenInfo",
            "type": "Element",
            "help": "Associates Fare with HostToken",
        },
    )
    provider_code: TypeProviderCode = field(
        default=None, metadata={"name": "ProviderCode", "type": "Attribute"}
    )
    host_token_ref: str = field(
        default=None, metadata={"name": "HostTokenRef", "type": "Attribute"}
    )

    @dataclass
    class FareTokenInfo:
        fare_info_ref: str = field(
            default=None,
            metadata={
                "required": True,
                "name": "FareInfoRef",
                "type": "Attribute",
            },
        )
        host_token_ref: str = field(
            default=None,
            metadata={
                "required": True,
                "name": "HostTokenRef",
                "type": "Attribute",
            },
        )


@dataclass
class AirExchangeBundle:
    """
    Used both in request and response
    """

    air_exchange_info: AirExchangeInfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirExchangeInfo",
            "type": "Element",
        },
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingInfoRef",
            "type": "Element",
        },
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
        },
    )
    penalty: List[Penalty] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Penalty",
            "type": "Element",
            "help": "Only used within an AirExchangeQuoteRsp",
        },
    )


@dataclass
class AirExchangeBundleTotal:
    """
    Total exchange and penalty information for one ticket number
    """

    air_exchange_info: AirExchangeInfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirExchangeInfo",
            "type": "Element",
        },
    )
    penalty: List[Penalty] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Penalty",
            "type": "Element",
            "help": "Only used within an AirExchangeQuoteRsp",
        },
    )


@dataclass
class AirExchangeModifiers:
    """
    Provides controls and switches for the Exchange process
    """

    contract_codes: "AirExchangeModifiers.ContractCodes" = field(
        default=None, metadata={"name": "ContractCodes", "type": "Element"}
    )
    booking_date: str = field(
        default=None, metadata={"name": "BookingDate", "type": "Attribute"}
    )
    ticketing_date: str = field(
        default=None, metadata={"name": "TicketingDate", "type": "Attribute"}
    )
    account_code: str = field(
        default=None, metadata={"name": "AccountCode", "type": "Attribute"}
    )
    ticket_designator: TypeTicketDesignator = field(
        default=None,
        metadata={"name": "TicketDesignator", "type": "Attribute"},
    )
    allow_penalty_fares: bool = field(
        default="true",
        metadata={"name": "AllowPenaltyFares", "type": "Attribute"},
    )
    private_fares_only: bool = field(
        default="false",
        metadata={"name": "PrivateFaresOnly", "type": "Attribute"},
    )
    universal_record_locator_code: TypeLocatorCode = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "help": "Which UniversalRecord should this new reservation be applied to. If blank, then a new one is created.",
        },
    )
    provider_locator_code: TypeLocatorCode = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "help": "Which Provider reservation does this reservation get added to.",
        },
    )
    provider_code: str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "help": "To be used with ProviderLocatorCode, which host the reservation being added to belongs to.",
        },
    )

    @dataclass
    class ContractCodes:
        contract_code: List[ContractCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "ContractCode",
                "type": "Element",
            },
        )


@dataclass
class AirFareDiscount:
    """
    Fare Discounts
    """

    percentage: float = field(
        default=None, metadata={"name": "Percentage", "type": "Attribute"}
    )
    amount: TypeMoney = field(
        default=None, metadata={"name": "Amount", "type": "Attribute"}
    )
    discount_method: TypeFareDiscount = field(
        default=None, metadata={"name": "DiscountMethod", "type": "Attribute"}
    )


@dataclass
class AirFareRuleCategory:
    """
    A collection of fare rule category codes.
    """

    category_code: List[TypeFareRuleCategoryCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 10,
            "name": "CategoryCode",
            "type": "Element",
            "help": "The Category Code for Air Fare Rule.",
        },
    )
    fare_info_ref: TypeRef = field(
        default=None, metadata={"name": "FareInfoRef", "type": "Attribute"}
    )


@dataclass
class AirPricingAdjustment:
    """
    This is a container to adjust price of AirPricingInfo. Pass zero values to remove existing adjustment.
    """

    adjustment: Adjustment = field(
        default=None,
        metadata={"required": True, "name": "Adjustment", "type": "Element"},
    )
    key: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "Key",
            "type": "Attribute",
            "help": "Key of AirPricingInfo from booking.",
        },
    )


@dataclass
class AirPricingPayment:
    """
    AirPricing Payment information - used to associate a FormOfPayment withiin the UR with one or more AirPricingInfos
    """

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirPricingInfoRef",
            "type": "Element",
        },
    )


@dataclass
class AirRefundModifiers:
    """
    Provides controls and switches for the Refund process
    """

    refund_date: str = field(
        default=None, metadata={"name": "RefundDate", "type": "Attribute"}
    )
    account_code: str = field(
        default=None, metadata={"name": "AccountCode", "type": "Attribute"}
    )
    ticket_designator: TypeTicketDesignator = field(
        default=None,
        metadata={"name": "TicketDesignator", "type": "Attribute"},
    )


@dataclass
class AirSegmentDetails:
    """
    An Air marketable travel segment.
    """

    passenger_details_ref: List[PassengerDetailsRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "PassengerDetailsRef",
            "type": "Element",
        },
    )
    brand_id: List[BrandId] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "BrandID",
            "type": "Element",
        },
    )
    booking_code_list: str = field(
        default=None,
        metadata={
            "name": "BookingCodeList",
            "type": "Element",
            "help": "Lists classes of service and their counts separated by delimiter |.",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderCode",
            "type": "Attribute",
        },
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata={"required": True, "name": "Carrier", "type": "Attribute"},
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Origin",
            "type": "Attribute",
            "help": "The IATA location code for this origination of this entity.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Destination",
            "type": "Attribute",
            "help": "The IATA location code for this destination of this entity.",
        },
    )
    departure_time: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "DepartureTime",
            "type": "Attribute",
            "help": "The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
        },
    )
    arrival_time: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "ArrivalTime",
            "type": "Attribute",
            "help": "The date and time at which this entity arrives at the destination. This does not include time zone information since it can be derived from the origin location.",
        },
    )
    equipment: TypeEquipment = field(
        default=None, metadata={"name": "Equipment", "type": "Attribute"}
    )
    class_of_service: TypeClassOfService = field(
        default=None, metadata={"name": "ClassOfService", "type": "Attribute"}
    )
    cabin_class: str = field(
        default=None, metadata={"name": "CabinClass", "type": "Attribute"}
    )
    operating_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "help": "The actual carrier that is operating the flight.",
        },
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "FlightNumber",
            "type": "Attribute",
            "help": "Flight Number for the Search Leg Detail.",
        },
    )


@dataclass
class AirSegmentPricingModifiers:
    """
    Specifies modifiers that a particular segment should be priced in. If this is used, then there must be one for each AirSegment in the AirItinerary.
    """

    permitted_booking_codes: "AirSegmentPricingModifiers.PermittedBookingCodes" = field(
        default=None,
        metadata={"name": "PermittedBookingCodes", "type": "Element"},
    )
    air_segment_ref: TypeRef = field(
        default=None, metadata={"name": "AirSegmentRef", "type": "Attribute"}
    )
    cabin_class: str = field(
        default=None, metadata={"name": "CabinClass", "type": "Attribute"}
    )
    account_code: str = field(
        default=None, metadata={"name": "AccountCode", "type": "Attribute"}
    )
    prohibit_advance_purchase_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitAdvancePurchaseFares", "type": "Attribute"},
    )
    prohibit_non_refundable_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitNonRefundableFares", "type": "Attribute"},
    )
    prohibit_penalty_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitPenaltyFares", "type": "Attribute"},
    )
    fare_basis_code: str = field(
        default=None,
        metadata={
            "name": "FareBasisCode",
            "type": "Attribute",
            "help": "The fare basis code to be used for pricing.",
        },
    )
    fare_break: TypeFareBreak = field(
        default=None,
        metadata={
            "name": "FareBreak",
            "type": "Attribute",
            "help": "Fare break point modifier to instruct Fares where it should or should not break the fare.",
        },
    )
    connection_indicator: TypeConnectionIndicator = field(
        default=None,
        metadata={
            "name": "ConnectionIndicator",
            "type": "Attribute",
            "help": "ConnectionIndicator attribute will be used to map connection indicators AvailabilityAndPricing, TurnAround and Stopover. This attribute is for Wordspan/1P only.",
        },
    )
    brand_tier: StringLength1to10 = field(
        default=None,
        metadata={
            "name": "BrandTier",
            "type": "Attribute",
            "help": "Modifier to price by specific brand tier number.",
        },
    )

    @dataclass
    class PermittedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "BookingCode",
                "type": "Element",
            },
        )


@dataclass
class AlternateLocationDistanceList:
    """
    Provides the Distance Information between Original Search Airports or City to Alternate Search Airports
    """

    alternate_location_distance: List[AlternateLocationDistance] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AlternateLocationDistance",
            "type": "Element",
        },
    )


@dataclass
class Apisrequirements:
    """
    Specific details for APIS Requirements.
    """

    document: List[Document] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Document",
            "type": "Element",
        },
    )
    level: str = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
            "help": "Applicability level of the Document. Required, Supported, API_Supported or Unknown",
        },
    )
    gender_required: bool = field(
        default=None, metadata={"name": "GenderRequired", "type": "Attribute"}
    )
    date_of_birth_required: bool = field(
        default=None,
        metadata={"name": "DateOfBirthRequired", "type": "Attribute"},
    )
    required_documents: str = field(
        default=None,
        metadata={
            "name": "RequiredDocuments",
            "type": "Attribute",
            "help": "What are required documents for the APIS Requirement. One, FirstAndOneOther or All",
        },
    )
    nationality_required: bool = field(
        default=None,
        metadata={
            "name": "NationalityRequired",
            "type": "Attribute",
            "help": "Nationality of the traveler is required for booking for some suppliers.",
        },
    )


@dataclass
class ApplicableSegment(TypeApplicableSegment):
    """
    Applicable air segment.
    """

    pass


@dataclass
class AuditData:
    """
    Container for Pricing Audit Data.For providers 1P/1J
    """

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )


@dataclass
class BackOfficeHandOff:
    """
    Allows an agency to select the back office documents and also route to different host to produce for the itinerary.
    """

    type: TypeBackOffice = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Attribute",
            "help": "The type of back office document,valid options are Accounting,Global,NonAccounting,NonAccountingRemote,Dual.",
        },
    )
    location: str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "help": "This is required for NonAccountingRemote,Dual and Global type back office.",
        },
    )
    pseudo_city_code: TypePcc = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "help": "The PCC of the host system where it would be routed.",
        },
    )


@dataclass
class BaseBaggageAllowanceInfo:
    """
    This contains common elements that are used for Baggage Allowance info, carry-on allowance info and embargo Info. Supported providers are 1V/1G/1P/1J
    """

    urlinfo: List[Urlinfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "URLInfo",
            "type": "Element",
            "help": "Contains the text and URL information as published by carrier.",
        },
    )
    text_info: List[TextInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TextInfo",
            "type": "Element",
            "help": "Text information as published by carrier.",
        },
    )
    origin: TypeIatacode = field(
        default=None, metadata={"name": "Origin", "type": "Attribute"}
    )
    destination: TypeIatacode = field(
        default=None, metadata={"name": "Destination", "type": "Attribute"}
    )
    carrier: TypeCarrier = field(
        default=None, metadata={"name": "Carrier", "type": "Attribute"}
    )


@dataclass
class BillingDetailItem:
    """
    The Billing Details Information
    """

    name: TypeBillingDetailsName = field(
        default=None,
        metadata={
            "required": True,
            "name": "Name",
            "type": "Attribute",
            "help": "Detailed Billing Information Name(e.g Personal ID, Account Number)",
        },
    )
    data_type: TypeBillingDetailsDataType = field(
        default=None,
        metadata={
            "required": True,
            "name": "DataType",
            "type": "Attribute",
            "help": "Detailed Billing Information DataType (Alpha, Numeric, etc.)",
        },
    )
    min_length: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "MinLength",
            "type": "Attribute",
            "help": "Detailed Billing Information Minimum Length.",
        },
    )
    max_length: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "MaxLength",
            "type": "Attribute",
            "help": "Detailed Billing Information Maximum Length.",
        },
    )
    value: str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "help": "Detailed Billing Information Value",
        },
    )


@dataclass
class BookingRulesFareReference:
    """
    Fare Reference associated with the BookingRules. Containing a text container for vendor response text.
    """

    class_of_service: TypeClassOfService = field(
        default=None, metadata={"name": "ClassOfService", "type": "Attribute"}
    )
    ticket_designator_code: TypeTicketDesignator = field(
        default=None,
        metadata={"name": "TicketDesignatorCode", "type": "Attribute"},
    )
    account_code: str = field(
        default=None, metadata={"name": "AccountCode", "type": "Attribute"}
    )
    upgrage_allowed: bool = field(
        default=None, metadata={"name": "UpgrageAllowed", "type": "Attribute"}
    )
    upgrade_class_of_service: TypeClassOfService = field(
        default=None,
        metadata={"name": "UpgradeClassOfService", "type": "Attribute"},
    )


@dataclass
class BrandInfo:
    """
    Commercially recognized product offered by an airline
    """

    key: TypeRef = field(
        default=None,
        metadata={"name": "Key", "type": "Attribute", "help": "Brand Key"},
    )
    brand_id: TypeBrandId = field(
        default=None,
        metadata={
            "required": True,
            "name": "BrandID",
            "type": "Attribute",
            "help": "The unique identifier of the brand",
        },
    )
    air_pricing_info_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Attribute",
            "help": "A reference to a AirPricing. Providers: ACH, 1G, 1V, 1P, 1J.",
        },
    )
    fare_info_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
            "help": "A reference to a FareInfo. Providers: ACH, 1G, 1V, 1P, 1J.",
        },
    )


@dataclass
class BundledService:
    """
    Displays the services bundled together
    """

    carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "help": "Carrier the service is applicable.",
        },
    )
    carrier_sub_code: bool = field(
        default=None,
        metadata={
            "name": "CarrierSubCode",
            "type": "Attribute",
            "help": "Carrier sub code. True means the carrier used their own sub code. False means the carrier used an ATPCO sub code",
        },
    )
    service_type: str = field(
        default=None,
        metadata={
            "name": "ServiceType",
            "type": "Attribute",
            "help": "The type of service or what the service is used for, e.g. F type is flight type, meaning the service is used on a flight",
        },
    )
    service_sub_code: str = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "help": "The sub code of the service, e.g. OAA for Pre paid baggage",
        },
    )
    name: str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "help": "Name of the bundled service.",
        },
    )
    booking: TypeBooking = field(
        default=None,
        metadata={
            "name": "Booking",
            "type": "Attribute",
            "help": "Booking method for the bundled service, e..g SSR.",
        },
    )
    occurrence: int = field(
        default=None,
        metadata={
            "name": "Occurrence",
            "type": "Attribute",
            "help": "How many of the service are included in the bundled service.",
        },
    )


@dataclass
class CategoryDetailsType:
    category_details: List[ValueDetails] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "CategoryDetails",
            "type": "Element",
            "help": "For each category Details of Structured Fare Rules",
        },
    )
    value: str = field(
        default=None,
        metadata={"required": True, "name": "Value", "type": "Attribute"},
    )


@dataclass
class Characteristic:
    value: str = field(
        default=None,
        metadata={"required": True, "name": "Value", "type": "Attribute"},
    )
    position: TypePosition = field(
        default=None, metadata={"name": "Position", "type": "Attribute"}
    )
    row_location: TypeRowLocation = field(
        default=None, metadata={"name": "RowLocation", "type": "Attribute"}
    )
    padiscode: StringLength1to99 = field(
        default=None,
        metadata={
            "name": "PADISCode",
            "type": "Attribute",
            "help": "Industry standard code that defines seat and row characteristic.",
        },
    )


@dataclass
class ChargesRules:
    """
    Fare Reference associated with the BookingRules
    """

    voluntary_changes: List["ChargesRules.VoluntaryChanges"] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "VoluntaryChanges",
            "type": "Element",
        },
    )
    voluntary_refunds: List["ChargesRules.VoluntaryRefunds"] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "VoluntaryRefunds",
            "type": "Element",
        },
    )

    @dataclass
    class VoluntaryChanges:
        penalty: Penalty = field(
            default=None, metadata={"name": "Penalty", "type": "Element"}
        )
        vol_change_ind: bool = field(
            default=None,
            metadata={"name": "VolChangeInd", "type": "Attribute"},
        )

    @dataclass
    class VoluntaryRefunds:
        penalty: Penalty = field(
            default=None, metadata={"name": "Penalty", "type": "Element"}
        )
        vol_change_ind: bool = field(
            default=None,
            metadata={"name": "VolChangeInd", "type": "Attribute"},
        )


@dataclass
class Chgtype:
    """
    PenFee list will be populated
    """

    pen_fee: List[PenFeeType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "PenFee",
            "type": "Element",
        },
    )


@dataclass
class Co2Emissions:
    """
    The carbon emissions produced by the journey
    """

    co2_emission: List[Co2Emission] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "CO2Emission",
            "type": "Element",
        },
    )
    total_value: float = field(
        default=None,
        metadata={
            "name": "TotalValue",
            "type": "Attribute",
            "help": "The total CO2 emission value for the journey",
        },
    )
    unit: StringLength1to64 = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Attribute",
            "help": "The unit used in the TotalValue attribute",
        },
    )
    category: StringLength1to64 = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "help": "The category name of the type of cabin, either Economy or Premium. Premium is any cabin that is not considered Economy",
        },
    )
    source: StringLength1to64 = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "help": "The source responsible for the values",
        },
    )


@dataclass
class Connection:
    """
    Flight Connection Information
    """

    fare_note: FareNote = field(
        default=None, metadata={"name": "FareNote", "type": "Element"}
    )
    change_of_plane: bool = field(
        default="false",
        metadata={
            "name": "ChangeOfPlane",
            "type": "Attribute",
            "help": "Indicates the traveler must change planes between flights.",
        },
    )
    change_of_terminal: bool = field(
        default="false",
        metadata={
            "name": "ChangeOfTerminal",
            "type": "Attribute",
            "help": "Indicates the traveler must change terminals between flights.",
        },
    )
    change_of_airport: bool = field(
        default="false",
        metadata={
            "name": "ChangeOfAirport",
            "type": "Attribute",
            "help": "Indicates the traveler must change airports between flights.",
        },
    )
    stop_over: bool = field(
        default="false",
        metadata={
            "name": "StopOver",
            "type": "Attribute",
            "help": "Indicates that there is a significant delay between flights (usually 12 hours or more)",
        },
    )
    min_connection_time: int = field(
        default=None,
        metadata={
            "name": "MinConnectionTime",
            "type": "Attribute",
            "help": "The minimum time needed to connect between the two different destinations.",
        },
    )
    duration: int = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Attribute",
            "help": "The actual duration (in minutes) between flights.",
        },
    )
    segment_index: int = field(
        default=None,
        metadata={
            "name": "SegmentIndex",
            "type": "Attribute",
            "help": "The sequential AirSegment number that this connection information applies to.",
        },
    )
    flight_details_index: int = field(
        default=None,
        metadata={
            "name": "FlightDetailsIndex",
            "type": "Attribute",
            "help": "The sequential FlightDetails number that this connection information applies to.",
        },
    )
    include_stop_over_to_fare_quote: TypeIgnoreStopOver = field(
        default=None,
        metadata={
            "name": "IncludeStopOverToFareQuote",
            "type": "Attribute",
            "help": "The field determines to quote fares with or without stop overs,the values can be NoStopOver,StopOver and IgnoreSegment.",
        },
    )


@dataclass
class DestinationPurposeCode:
    """
    This code is required to indicate destination and purpose of Travel. It is applicable for Canada and Bermuda agency only. This is used by Worldspan.
    """

    destination: TypeDestinationCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Destination",
            "type": "Attribute",
        },
    )
    purpose: TypePurposeCode = field(
        default=None,
        metadata={"required": True, "name": "Purpose", "type": "Attribute"},
    )


@dataclass
class Dimension(TypeUnitOfMeasure):
    """
    Information related to Length,Height,Width of a baggage.
    """

    type: str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "help": "Type denotes Length,Height,Width of a baggage.",
        },
    )


@dataclass
class DocumentOptions:
    """
    Allows an agency to set different document options for the itinerary.
    """

    passenger_receipt_override: PassengerReceiptOverride = field(
        default=None,
        metadata={"name": "PassengerReceiptOverride", "type": "Element"},
    )
    override_option: List[TypeOverrideOption] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "OverrideOption",
            "type": "Element",
            "help": "Allows an agency to override print options for documents during document generation.",
        },
    )
    suppress_itinerary_remarks: bool = field(
        default=None,
        metadata={
            "name": "SuppressItineraryRemarks",
            "type": "Attribute",
            "help": "True when itinerary remarks are suppressed.",
        },
    )
    generate_itin_numbers: bool = field(
        default=None,
        metadata={
            "name": "GenerateItinNumbers",
            "type": "Attribute",
            "help": "True when itinerary numbers are system generated.",
        },
    )


@dataclass
class ElectronicMiscDocument:
    """
    Electronic miscellaneous document. Supported providers are 1G/1V/1P/1J
    """

    emdcoupon: List[Emdcoupon] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "EMDCoupon",
            "type": "Element",
            "help": "The coupon information for the EMD issued.",
        },
    )
    status: str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "help": "Status of the EMD calculated on the basis of coupon status. Possible values Open, Void, Refunded, Exchanged, Irregular Operations,Airport Control, Checked In, Flown/Used, Boarded/Lifted, Suspended, Unknown",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "help": "System generated Key",
        },
    )


@dataclass
class EmbargoList:
    """
    List of embargoes. Provider: 1G, 1V, 1P, 1J
    """

    embargo: List[Embargo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 99,
            "name": "Embargo",
            "type": "Element",
        },
    )


@dataclass
class Emd:
    fulfillment_type: int = field(
        default=None,
        metadata={
            "name": "FulfillmentType",
            "type": "Attribute",
            "help": "A one digit code specifying how the service must be fulfilled. See FulfillmentTypeDescription for the description of this value.",
        },
    )
    fulfillment_type_description: str = field(
        default=None,
        metadata={
            "name": "FulfillmentTypeDescription",
            "type": "Attribute",
            "help": "EMD description.",
        },
    )
    associated_item: str = field(
        default=None,
        metadata={
            "name": "AssociatedItem",
            "type": "Attribute",
            "help": "The type of Optional Service. The choices are Flight, Ticket, Merchandising, Rule Buster, Allowance, Chargeable Baggage, Carry On Baggage Allowance, Prepaid Baggage. Provider: 1G, 1V, 1P, 1J",
        },
    )
    availability_charge_indicator: str = field(
        default=None,
        metadata={
            "name": "AvailabilityChargeIndicator",
            "type": "Attribute",
            "help": "A one-letter code specifying whether the service is available or if there is a charge associated with it. X = Service not available F = No charge for service (free) and an EMD is not issued to reflect free service E = No charge for service (free) and an EMD is issued to reflect the free service. G = No charge for service (free), booking is not required and an EMD is not issued to reflect free service H = No charge for service (free), booking is not required, and an EMD is issued to reflect the free service. Blank = No application. Charges apply according to the data in the Service Fee fields.",
        },
    )
    refund_reissue_indicator: str = field(
        default=None,
        metadata={
            "name": "RefundReissueIndicator",
            "type": "Attribute",
            "help": "An attribute specifying whether the service is refundable or reissuable.",
        },
    )
    commissionable: bool = field(
        default=None,
        metadata={
            "name": "Commissionable",
            "type": "Attribute",
            "help": "True/False value to whether or not the service is comissionable.",
        },
    )
    mileage_indicator: bool = field(
        default=None,
        metadata={
            "name": "MileageIndicator",
            "type": "Attribute",
            "help": "True/False value to whether or not the service has miles.",
        },
    )
    location: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "help": "3 letter location code where the service will be availed.",
        },
    )
    date: str = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Attribute",
            "help": "The date at which the service will be used.",
        },
    )
    booking: TypeBooking = field(
        default=None,
        metadata={
            "name": "Booking",
            "type": "Attribute",
            "help": "Holds the booking description for the service, e.g., SSR.",
        },
    )
    display_category: TypeDisplayCategory = field(
        default=None,
        metadata={
            "name": "DisplayCategory",
            "type": "Attribute",
            "help": "Describes when the service should be displayed.",
        },
    )
    reusable: bool = field(
        default=None,
        metadata={
            "name": "Reusable",
            "type": "Attribute",
            "help": "Identifies if the service can be re-used towards a future purchase.",
        },
    )


@dataclass
class EmdpricingInfo:
    """
    Fare related information for these electronic miscellaneous documents. Supported providers are 1G/1V/1P/1J
    """

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
        },
    )
    base_fare: TypeMoney = field(
        default=None, metadata={"name": "BaseFare", "type": "Attribute"}
    )
    total_fare: TypeMoney = field(
        default=None, metadata={"name": "TotalFare", "type": "Attribute"}
    )
    total_tax: TypeMoney = field(
        default=None, metadata={"name": "TotalTax", "type": "Attribute"}
    )
    equiv_fare: TypeMoney = field(
        default=None, metadata={"name": "EquivFare", "type": "Attribute"}
    )


@dataclass
class Emdsummary:
    """
    EMD summary information. Supported providers are 1G/1V/1P/1J
    """

    emdcoupon: List[Emdcoupon] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "EMDCoupon",
            "type": "Element",
            "help": "The coupon information for the EMD issued.",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "help": "System generated Key",
        },
    )


@dataclass
class ExchangePenaltyInfo:
    penalty_information: List[PenaltyInformation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "PenaltyInformation",
            "type": "Element",
        },
    )
    ptc: TypePtc = field(
        default=None, metadata={"name": "PTC", "type": "Attribute"}
    )
    minimum_change_fee: TypeMoney = field(
        default=None,
        metadata={
            "name": "MinimumChangeFee",
            "type": "Attribute",
            "help": "Minimum change fee for changes to the itinerary.",
        },
    )
    maximum_change_fee: TypeMoney = field(
        default=None,
        metadata={
            "name": "MaximumChangeFee",
            "type": "Attribute",
            "help": "Maximum change fee for changes to the itinerary.",
        },
    )


@dataclass
class ExemptObfee:
    """
    Used to specify which OB fees are exempt; if none are listed, it means all should be exempt.
    """

    sub_code: List[TypeSubCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 8,
            "name": "SubCode",
            "type": "Element",
        },
    )


@dataclass
class FareGuaranteeInfo:
    """
    The information related to fare guarantee details.
    """

    guarantee_date: str = field(
        default=None,
        metadata={
            "name": "GuaranteeDate",
            "type": "Attribute",
            "help": "The date till which the fare is guaranteed.",
        },
    )
    guarantee_type: TypeFareGuarantee = field(
        default=None,
        metadata={
            "required": True,
            "name": "GuaranteeType",
            "type": "Attribute",
            "help": "Determines the status of a fare for a passenger.",
        },
    )


@dataclass
class FareNoteList:
    """
    The shared object list of Notes
    """

    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareNote",
            "type": "Element",
        },
    )


@dataclass
class FareRemark:
    text: List[str] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Text",
            "type": "Element",
        },
    )
    url: List[Url] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "URL",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )
    name: str = field(
        default=None, metadata={"name": "Name", "type": "Attribute"}
    )


@dataclass
class FareRestrictionDate:
    """
    Fare restriction based on date ranges. StartDate and EndDate are strings representing respective dates. If a year component is present then it signifies an exact date. If only day and month components are present then it signifies a seasonal date, which means applicable for that date in any year
    """

    direction: TypeFareDirectionality = field(
        default=None, metadata={"name": "Direction", "type": "Attribute"}
    )
    start_date: str = field(
        default=None, metadata={"name": "StartDate", "type": "Attribute"}
    )
    end_date: str = field(
        default=None, metadata={"name": "EndDate", "type": "Attribute"}
    )
    end_date_indicator: str = field(
        default=None,
        metadata={
            "name": "EndDateIndicator",
            "type": "Attribute",
            "help": "This field indicates the end date/last date for which travel on the fare component being validated must be commenced or completed",
        },
    )


@dataclass
class FareRestrictionDaysOfWeek:
    """
    Days of the week that the restriction applies too.
    """

    direction: TypeFareDirectionality = field(
        default=None, metadata={"name": "Direction", "type": "Attribute"}
    )
    trip_type: TypeFareTripType = field(
        default=None, metadata={"name": "TripType", "type": "Attribute"}
    )
    monday: bool = field(
        default=None, metadata={"name": "Monday", "type": "Attribute"}
    )
    tuesday: bool = field(
        default=None, metadata={"name": "Tuesday", "type": "Attribute"}
    )
    wednesday: bool = field(
        default=None, metadata={"name": "Wednesday", "type": "Attribute"}
    )
    thursday: bool = field(
        default=None, metadata={"name": "Thursday", "type": "Attribute"}
    )
    friday: bool = field(
        default=None, metadata={"name": "Friday", "type": "Attribute"}
    )
    saturday: bool = field(
        default=None, metadata={"name": "Saturday", "type": "Attribute"}
    )
    sunday: bool = field(
        default=None, metadata={"name": "Sunday", "type": "Attribute"}
    )


@dataclass
class FareRuleFailureInfo:
    """
    Returns fare rule failure reason codes when fare basis code is forced.
    """

    reason: List[TypeFareRuleFailureInfoReason] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "Reason",
            "type": "Element",
        },
    )


@dataclass
class FareRuleShort:
    """
    Short Text Fare Rule
    """

    fare_rule_name_value: List[FareRuleNameValue] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "FareRuleNameValue",
            "type": "Element",
        },
    )
    category: int = field(
        default=None,
        metadata={"required": True, "name": "Category", "type": "Attribute"},
    )
    table_number: str = field(
        default=None, metadata={"name": "TableNumber", "type": "Attribute"}
    )


@dataclass
class FareStatus:
    """
    Denotes the status of a particular fare.
    """

    fare_status_failure_info: FareStatusFailureInfo = field(
        default=None,
        metadata={"name": "FareStatusFailureInfo", "type": "Element"},
    )
    code: TypeFareStatusCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Code",
            "type": "Attribute",
            "help": "The status of the fare.",
        },
    )


@dataclass
class FareTicketDesignator:
    """
    Ticket Designator used to further qualify a Fare
    """

    value: TypeTicketDesignator = field(
        default=None, metadata={"name": "Value", "type": "Attribute"}
    )


@dataclass
class FareType:
    """
    Used to request fares based on the ATPCO type code
    """

    code: TypeFareTypeCode = field(
        default=None,
        metadata={"required": True, "name": "Code", "type": "Attribute"},
    )


@dataclass
class GeneralTimeTable:
    days_of_operation: TypeDaysOfOperation = field(
        default=None, metadata={"name": "DaysOfOperation", "type": "Element"}
    )
    flight_origin: TypeLocation = field(
        default=None,
        metadata={"required": True, "name": "FlightOrigin", "type": "Element"},
    )
    flight_destination: TypeLocation = field(
        default=None,
        metadata={
            "required": True,
            "name": "FlightDestination",
            "type": "Element",
        },
    )
    carrier_list: CarrierList = field(
        default=None, metadata={"name": "CarrierList", "type": "Element"}
    )
    start_date: str = field(
        default=None,
        metadata={"required": True, "name": "StartDate", "type": "Attribute"},
    )
    end_date: str = field(
        default=None, metadata={"name": "EndDate", "type": "Attribute"}
    )
    start_time: str = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Attribute",
            "help": "Flight start time of flight time tabel .",
        },
    )
    end_time: str = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Attribute",
            "help": "Flight end time of flight time tabel .",
        },
    )
    include_connection: bool = field(
        default=None,
        metadata={
            "name": "IncludeConnection",
            "type": "Attribute",
            "help": "Include or exclude connecting flights.",
        },
    )


@dataclass
class GroupedOptionInfo:
    grouped_option: List[GroupedOption] = field(
        default_factory=list,
        metadata={
            "min_occurs": 2,
            "max_occurs": 999,
            "name": "GroupedOption",
            "type": "Element",
        },
    )


@dataclass
class IncludeAddlBookingCodeInfo:
    """
    Used to include primary or secondary carrier's booking code details
    """

    type: TypeCarrierCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Attribute",
            "help": "The type defines that the booking code info is for primary or secondary carrier.",
        },
    )
    secondary_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "SecondaryCarrier",
            "type": "Attribute",
            "help": "The secondary carrier code is required when type is secondary .",
        },
    )


@dataclass
class InvoluntaryChange:
    """
    Specify the Ticket Endorsement value
    """

    ticket_endorsement: TicketEndorsement = field(
        default=None,
        metadata={
            "required": True,
            "name": "TicketEndorsement",
            "type": "Element",
        },
    )


@dataclass
class IssuanceModifiers:
    """
    General modifiers supported for EMD Issuance.Supported providers are 1V/1G/1P/1J
    """

    customer_receipt_info: CustomerReceiptInfo = field(
        default=None,
        metadata={
            "name": "CustomerReceiptInfo",
            "type": "Element",
            "help": "Information about customer receipt via email.",
        },
    )
    emdendorsement: Emdendorsement = field(
        default=None,
        metadata={
            "name": "EMDEndorsement",
            "type": "Element",
            "help": "Endorsement details to be used during EMD issuance.",
        },
    )
    emdcommission: Emdcommission = field(
        default=None,
        metadata={
            "name": "EMDCommission",
            "type": "Element",
            "help": "Commission information to be used for EMD issuance.",
        },
    )
    form_of_payment_ref: FormOfPaymentRef = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "help": "Reference to FormOfPayment present in the UR to be used for EMD issuance.",
        },
    )
    form_of_payment: FormOfPayment = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "help": "FormOfPayment information to be used for EMD issuance.",
        },
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "help": "Plating carrier code for which this EMD is issued.",
        },
    )


@dataclass
class Itinerary:
    """
    Allows an agency to select the itinenary option for ticket.
    """

    type: TypeItinerary = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "help": "Specifies the type of itinenary option for ticket like Invoice type or Pocket itinenary.",
        },
    )
    option: TypeItineraryOption = field(
        default=None,
        metadata={
            "name": "Option",
            "type": "Attribute",
            "help": "Specifies the itinerary option like NoFare,NoAmount.",
        },
    )
    separate_indicator: bool = field(
        default=None,
        metadata={
            "name": "SeparateIndicator",
            "type": "Attribute",
            "help": "Set to true if one itinerary to be printed per passenger.",
        },
    )


@dataclass
class Journey:
    """
    Information about all connecting segment list and total traveling time
    """

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentRef",
            "type": "Element",
        },
    )
    travel_time: str = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
            "help": "Total traveling time that is difference between the departure time of the first segment and the arrival time of the last segments for that particular entire set of connection.",
        },
    )


@dataclass
class LandCharges:
    """
    Prints non-air charges on a document.
    """

    tax: List[Tax] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "Tax",
            "type": "Element",
        },
    )
    base: TypeMoney = field(
        default=None, metadata={"name": "Base", "type": "Attribute"}
    )
    total: TypeMoney = field(
        default=None, metadata={"name": "Total", "type": "Attribute"}
    )
    miscellaneous: TypeMoney = field(
        default=None, metadata={"name": "Miscellaneous", "type": "Attribute"}
    )
    pre_paid: TypeMoney = field(
        default=None, metadata={"name": "PrePaid", "type": "Attribute"}
    )
    deposit: TypeMoney = field(
        default=None, metadata={"name": "Deposit", "type": "Attribute"}
    )


@dataclass
class Leg:
    """
    Information about the journey Leg
    """

    leg_detail: List[LegDetail] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "LegDetail",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    group: int = field(
        default=None,
        metadata={
            "required": True,
            "name": "Group",
            "type": "Attribute",
            "help": "Returns the Group Number for the leg.",
        },
    )
    origin: TypeRailLocationCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Origin",
            "type": "Attribute",
            "help": "Returns the origin airport or city code for the leg.",
        },
    )
    destination: TypeRailLocationCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Destination",
            "type": "Attribute",
            "help": "Returns the destination airport or city code for the leg.",
        },
    )


@dataclass
class LegPrice:
    """
    Information about the journey Leg Price
    """

    leg_detail: List[LegDetail] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "LegDetail",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    total_price: TypeMoney = field(
        default=None,
        metadata={
            "required": True,
            "name": "TotalPrice",
            "type": "Attribute",
            "help": "The Total Prices for the Combination of Journey legs for this Price.",
        },
    )
    approximate_total_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
            "help": "The Converted Total Price in Agency's Default Currency Value",
        },
    )


@dataclass
class ManualFareAdjustment:
    applied_on: TypeAdjustmentTarget = field(
        default=None,
        metadata={
            "required": True,
            "name": "AppliedOn",
            "type": "Attribute",
            "help": "Represents pricing component upon which manual increment/discount to be applied. Presently supported values are Base and Total. Other is present as a future place holder but presently no request processing logic is available for value Other",
        },
    )
    adjustment_type: TypeAdjustmentType = field(
        default=None,
        metadata={
            "required": True,
            "name": "AdjustmentType",
            "type": "Attribute",
            "help": "Represents process used for applying manual discount/increment. Presently supported values are Flat, Percentage.",
        },
    )
    value: float = field(
        default=None,
        metadata={
            "required": True,
            "name": "Value",
            "type": "Attribute",
            "help": "Represents value of increment/discount applied. Negative value is considered as discount whereas positive value represents increment",
        },
    )
    passenger_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "PassengerRef",
            "type": "Attribute",
            "help": "Represents passenger association.",
        },
    )
    ticket_designator: TypeTicketDesignator = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Attribute",
            "help": "Providers: 1p/1j",
        },
    )
    fare_type: TypeFareTypeCode = field(
        default=None,
        metadata={
            "name": "FareType",
            "type": "Attribute",
            "help": "Providers: 1p/1j",
        },
    )


@dataclass
class MaxLayoverDurationType:
    """
    User can specify its attribute's value in Minutes. Maximum size of each attribute is 4.
    """

    domestic: MaxLayoverDurationRangeType = field(
        default=None,
        metadata={
            "name": "Domestic",
            "type": "Attribute",
            "help": "It will be applied for all Domestic-to-Domestic connections.",
        },
    )
    gateway: MaxLayoverDurationRangeType = field(
        default=None,
        metadata={
            "name": "Gateway",
            "type": "Attribute",
            "help": "It will be applied for all Domestic to International and International to Domestic connections.",
        },
    )
    international: MaxLayoverDurationRangeType = field(
        default=None,
        metadata={
            "name": "International",
            "type": "Attribute",
            "help": "It will be applied for all International-to-International connections.",
        },
    )


@dataclass
class Meals(TypeMealService):
    """
    Available Meal Service.
    """

    pass


@dataclass
class OptionalServiceModifiers:
    """
    Rich Content and Branding for an optional service
    """

    optional_service_modifier: List[OptionalServiceModifier] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 99,
            "name": "OptionalServiceModifier",
            "type": "Element",
        },
    )


@dataclass
class OriginalItineraryDetails:
    """
    Used for rapid reprice to provide additional information about the original itinerary. Providers: 1G/1V/1P/1S/1A
    """

    itinerary_type: TypeItineraryCode = field(
        default=None,
        metadata={
            "name": "ItineraryType",
            "type": "Attribute",
            "help": "Values allowed are International or Domestic. This tells if the itinerary is international or domestic.",
        },
    )
    bulk_ticket: bool = field(
        default="false",
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
            "help": "Set to true and the itinerary is/will be a bulk ticket. Set to false and the itinerary being repriced will not be a bulk ticket. Default is false.",
        },
    )
    ticketing_pcc: TypePcc = field(
        default=None,
        metadata={
            "name": "TicketingPCC",
            "type": "Attribute",
            "help": "This is the PCC or SID where the ticket was issued",
        },
    )
    ticketing_iata: TypeIata = field(
        default=None,
        metadata={
            "name": "TicketingIATA",
            "type": "Attribute",
            "help": "This is the IATA where the ticket was issued.",
        },
    )
    ticketing_country: TypeCountry = field(
        default=None,
        metadata={
            "name": "TicketingCountry",
            "type": "Attribute",
            "help": "This is the country where the ticket was issued.",
        },
    )
    tour_code: TypeTourCode = field(
        default=None, metadata={"name": "TourCode", "type": "Attribute"}
    )
    ticketing_date: str = field(
        default=None,
        metadata={
            "name": "TicketingDate",
            "type": "Attribute",
            "help": "The date the repriced itinerary was ticketed",
        },
    )


@dataclass
class PassengerDetails:
    """
    Details of passenger
    """

    loyalty_card_details: List[LoyaltyCardDetails] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "LoyaltyCardDetails",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "Key",
            "type": "Attribute",
            "help": "Passenger key",
        },
    )
    code: TypePtc = field(
        default=None,
        metadata={
            "required": True,
            "name": "Code",
            "type": "Attribute",
            "help": "Passenger code",
        },
    )
    age: int = field(
        default=None,
        metadata={"name": "Age", "type": "Attribute", "help": "Passenger age"},
    )


@dataclass
class PassengerTicketNumber:
    """
    Information related to Ticket Number
    """

    ticket_number: TypePassengerTicketNumber = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
            "help": "The identifying number for a Ticket for a passenger.",
        },
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "help": "Reference to a passenger associated with a ticket.",
        },
    )


@dataclass
class PenaltyFareInformation:
    penalty_info: TypeFarePenalty = field(
        default=None,
        metadata={
            "name": "PenaltyInfo",
            "type": "Element",
            "help": "Penalty Limit if requested.",
        },
    )
    prohibit_penalty_fares: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProhibitPenaltyFares",
            "type": "Attribute",
            "help": "Indicates whether user wants penalty fares to be returned.",
        },
    )


@dataclass
class PrePayId:
    """
    Pre pay unique identifier , example Flight Pass Number
    """

    company_name: CompanyName = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Element",
            "help": "Supplier info that is specific to the pre pay Id",
        },
    )
    id: TypeCardNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "Id",
            "type": "Attribute",
            "help": "This is the exact pre pay number. Example flight pass number",
        },
    )
    type: str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "help": "Type of pre pay unique identifier,presently only available value is FlightPass.",
        },
    )


@dataclass
class PrePayPriceInfo:
    """
    Pricing detail for the Pre Pay Account
    """

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
            "help": "Detailed tax information for the pre pay account",
        },
    )
    base_fare: TypeMoney = field(
        default=None, metadata={"name": "BaseFare", "type": "Attribute"}
    )
    total_fare: TypeMoney = field(
        default=None, metadata={"name": "TotalFare", "type": "Attribute"}
    )
    total_tax: TypeMoney = field(
        default=None, metadata={"name": "TotalTax", "type": "Attribute"}
    )


@dataclass
class PreferredBookingCodes:
    """
    This is the container to specify all preferred booking codes
    """

    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "BookingCode",
            "type": "Element",
        },
    )


@dataclass
class RefundFailureInfo:
    """
    Will be optionally returned as part of AirRefunTicketingRsp if one or all ticket refund requests fail.
    """

    booking_traveler_ref: List[TypeRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "BookingTravelerRef",
            "type": "Element",
        },
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "TCRNumber",
            "type": "Element",
            "help": "The identifying number for a Ticketless Air Reservation.",
        },
    )
    ticket_number: TicketNumber = field(
        default=None,
        metadata={"required": True, "name": "TicketNumber", "type": "Element"},
    )
    name: str = field(
        default=None,
        metadata={"required": True, "name": "Name", "type": "Element"},
    )
    code: int = field(
        default=None,
        metadata={"required": True, "name": "Code", "type": "Attribute"},
    )
    message: str = field(
        default=None, metadata={"name": "Message", "type": "Attribute"}
    )


@dataclass
class RelatedTraveler:
    """
    Detailed related Traveler information for pre pay profiles
    """

    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "LoyaltyCard",
            "type": "Element",
            "help": "Traveler loyalty card detail",
        },
    )
    person_name: PersonName = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
            "help": "Traveler name detail",
        },
    )
    credits_used: "RelatedTraveler.CreditsUsed" = field(
        default=None,
        metadata={
            "name": "CreditsUsed",
            "type": "Element",
            "help": "Traveler pre pay credit detail",
        },
    )
    status_code: str = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Attribute",
            "help": "Traveler status code(One of Marked for deletion,Lapsed,Terminated,Active,Inactive)",
        },
    )
    relation: str = field(
        default=None,
        metadata={
            "name": "Relation",
            "type": "Attribute",
            "help": "Relation to the pre pay id. Example flight pass user",
        },
    )

    @dataclass
    class CreditsUsed:
        used_credit: float = field(
            default=None, metadata={"name": "UsedCredit", "type": "Attribute"}
        )
        currency_code: TypeCurrency = field(
            default=None,
            metadata={"name": "CurrencyCode", "type": "Attribute"},
        )


@dataclass
class RuleAdvancedPurchase:
    """
    Container for rules regarding advance purchase restrictions. TicketingEarliestDate and TicketingLatestDate are strings representing respective dates. If a year component is present then it signifies an exact date. If only day and month components are present then it signifies a seasonal date, which means applicable for that date in any year
    """

    reservation_latest_period: str = field(
        default=None,
        metadata={"name": "ReservationLatestPeriod", "type": "Attribute"},
    )
    reservation_latest_unit: TypeStayUnit = field(
        default=None,
        metadata={"name": "ReservationLatestUnit", "type": "Attribute"},
    )
    ticketing_earliest_date: str = field(
        default=None,
        metadata={"name": "TicketingEarliestDate", "type": "Attribute"},
    )
    ticketing_latest_date: str = field(
        default=None,
        metadata={"name": "TicketingLatestDate", "type": "Attribute"},
    )
    more_rules_present: bool = field(
        default=None,
        metadata={
            "name": "MoreRulesPresent",
            "type": "Attribute",
            "help": "If true, specifies that advance purchase information will be present in fare rules.",
        },
    )


@dataclass
class SegmentSelect:
    """
    To be used to pass the selected segment.
    """

    air_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentRef",
            "type": "Element",
            "help": "Reference to AirSegment from an Air Reservation.",
        },
    )
    hotel_reservation_ref: List[TypeNonAirReservationRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "HotelReservationRef",
            "type": "Element",
            "help": "Specify the locator code of Hotel reservation if it needs to be considered as Auxiliary segment",
        },
    )
    vehicle_reservation_ref: List[TypeNonAirReservationRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "VehicleReservationRef",
            "type": "Element",
            "help": "Specify the locator code of Vehicle reservation if it needs to be considered as Auxiliary segment",
        },
    )
    passive_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "PassiveSegmentRef",
            "type": "Element",
            "help": "Reference to PassiveSegment from a Passive Reservation.Specify the passive segment if it needs to be considered as Auxiliary segment",
        },
    )
    all_confirmed_air: bool = field(
        default=None,
        metadata={
            "name": "AllConfirmedAir",
            "type": "Attribute",
            "help": "Set to true to consider all Confirmed segments including active and passive and set to false to discard confirmed segments",
        },
    )
    all_waitlisted_air: bool = field(
        default=None,
        metadata={
            "name": "AllWaitlistedAir",
            "type": "Attribute",
            "help": "Set to true to consider all Waitlisted segments and false to discard all waitlisted segments",
        },
    )
    all_hotel: bool = field(
        default=None,
        metadata={
            "name": "AllHotel",
            "type": "Attribute",
            "help": "Set to true to consider all Hotel reservations as Auxiliary segment and false to discard all Hotel reservations",
        },
    )
    all_vehicle: bool = field(
        default=None, metadata={"name": "AllVehicle", "type": "Attribute"}
    )
    all_passive: bool = field(
        default=None,
        metadata={
            "name": "AllPassive",
            "type": "Attribute",
            "help": "Set to true to consider all Passive segments as Auxiliary segment and false to discard passive segments",
        },
    )


@dataclass
class SelectionModifiers:
    """
    Modifiers supported for selection of services during EMD Issuance. Supported providers are 1V/1G/1P/1J
    """

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentRef",
            "type": "Element",
            "help": "References to airsegments for which EMDs will be generated on all the associated services.",
        },
    )
    svc_segment_ref: List[TypeRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SvcSegmentRef",
            "type": "Element",
            "help": "SVC segment reference to which the EMD is being issued",
        },
    )
    supplier_code: TypeCarrier = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "help": "Supplier/Vendor code for which EMDs will be generated on all the associated services. Required if PNR contains more than one supplier.",
        },
    )
    rfic: str = field(
        default=None,
        metadata={
            "name": "RFIC",
            "type": "Attribute",
            "help": "Reason for issuance code for which EMDs will be generated on all the associated services.",
        },
    )


@dataclass
class ServiceGroup:
    """
    The Service Group of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH
    """

    service_sub_group: List[ServiceSubGroup] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 15,
            "name": "ServiceSubGroup",
            "type": "Element",
        },
    )
    code: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Code",
            "type": "Attribute",
            "help": "The Service Group Code of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        },
    )


@dataclass
class SolutionGroup:
    """
    Specifies the trip type and diversity of all or a subset of the result solutions.
    """

    permitted_account_codes: "SolutionGroup.PermittedAccountCodes" = field(
        default=None,
        metadata={"name": "PermittedAccountCodes", "type": "Element"},
    )
    preferred_account_codes: "SolutionGroup.PreferredAccountCodes" = field(
        default=None,
        metadata={"name": "PreferredAccountCodes", "type": "Element"},
    )
    prohibited_account_codes: "SolutionGroup.ProhibitedAccountCodes" = field(
        default=None,
        metadata={"name": "ProhibitedAccountCodes", "type": "Element"},
    )
    permitted_point_of_sales: "SolutionGroup.PermittedPointOfSales" = field(
        default=None,
        metadata={"name": "PermittedPointOfSales", "type": "Element"},
    )
    prohibited_point_of_sales: "SolutionGroup.ProhibitedPointOfSales" = field(
        default=None,
        metadata={"name": "ProhibitedPointOfSales", "type": "Element"},
    )
    count: int = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "help": "The number of solution to include in this group. If only one group specified, this can be left blank. If multiple groups specified, all counts must add up to the MaxResults of the request.",
        },
    )
    trip_type: TypeTripType = field(
        default=None,
        metadata={
            "required": True,
            "name": "TripType",
            "type": "Attribute",
            "help": "Specifies the trip type for this group of results. Allows targeting a result set to a particular set of characterists.",
        },
    )
    diversification: TypeDiversity = field(
        default=None,
        metadata={
            "name": "Diversification",
            "type": "Attribute",
            "help": "Specifies the diversification of this group of results, if specified. Allows targeting a result set to ensure they contain more unique results.",
        },
    )
    tag: str = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Attribute",
            "help": "An arbitrary name for this group of solutions. Will be returned with the solution for idetification.",
        },
    )
    primary: bool = field(
        default="false",
        metadata={
            "name": "Primary",
            "type": "Attribute",
            "help": "Indicates that this is a primary SolutionGroup when using alternate pricing concepts",
        },
    )

    @dataclass
    class PermittedAccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "AccountCode",
                "type": "Element",
            },
        )

    @dataclass
    class PreferredAccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "AccountCode",
                "type": "Element",
            },
        )

    @dataclass
    class ProhibitedAccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "AccountCode",
                "type": "Element",
            },
        )

    @dataclass
    class PermittedPointOfSales:
        point_of_sale: List[PointOfSale] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "PointOfSale",
                "type": "Element",
            },
        )

    @dataclass
    class ProhibitedPointOfSales:
        point_of_sale: List[PointOfSale] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "PointOfSale",
                "type": "Element",
            },
        )


@dataclass
class SvcSegment:
    """
    Service segment added to collect additional fee. 1P only
    """

    key: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "Key",
            "type": "Attribute",
            "help": "The Key of SVC Segment.",
        },
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "help": "The platting carrier",
        },
    )
    status: str = field(
        default=None, metadata={"name": "Status", "type": "Attribute"}
    )
    number_of_items: int = field(
        default=None, metadata={"name": "NumberOfItems", "type": "Attribute"}
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "help": "Origin location - Airport code. 1P only.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "help": "Destination location - Airport code. 1P only.",
        },
    )
    start_date: str = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "help": "Start date of the segment. Generally it is the next date after the last air segment. 1P only",
        },
    )
    travel_order: int = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
            "help": "To identify the appropriate travel sequence for Air/Car/Hotel/Passive segments/reservations based on travel dates. This ordering is applicable across the UR not provider or traveler specific",
        },
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={"name": "BookingTravelerRef", "type": "Attribute"},
    )
    rfic: str = field(
        default=None,
        metadata={
            "name": "RFIC",
            "type": "Attribute",
            "help": "1P - Reason for issuance",
        },
    )
    rfisc: str = field(
        default=None,
        metadata={
            "name": "RFISC",
            "type": "Attribute",
            "help": "1P - Resaon for issuance sub-code",
        },
    )
    svc_description: str = field(
        default=None,
        metadata={
            "name": "SvcDescription",
            "type": "Attribute",
            "help": "1P - SVC fee description",
        },
    )
    fee: TypeMoney = field(
        default=None,
        metadata={
            "name": "Fee",
            "type": "Attribute",
            "help": "The fee to be collected using SVC segment",
        },
    )
    emdnumber: TypeEmdnumber = field(
        default=None,
        metadata={
            "name": "EMDNumber",
            "type": "Attribute",
            "help": "Generated EMD number, if EMD is issued on the SVC",
        },
    )


@dataclass
class TcrexchangeBundle:
    """
    Used in AirExchangeReq request and AirExchangeQuoteRsp response
    """

    air_exchange_info: AirExchangeInfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirExchangeInfo",
            "type": "Element",
        },
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirPricingInfoRef",
            "type": "Element",
        },
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FeeInfo",
            "type": "Element",
        },
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
            "help": "Itinerary level taxes",
        },
    )
    penalty: List[Penalty] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Penalty",
            "type": "Element",
            "help": "Only used within an AirExchangeQuoteRsp",
        },
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "TCRNumber",
            "type": "Attribute",
            "help": "The identifying number for a Ticketless Air Reservation.",
        },
    )


@dataclass
class Tcrinfo:
    status: TypeTcrstatus = field(
        default=None,
        metadata={"required": True, "name": "Status", "type": "Attribute"},
    )
    date: str = field(
        default=None, metadata={"name": "Date", "type": "Attribute"}
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "TCRNumber",
            "type": "Attribute",
            "help": "The identifying number for a Ticketless Air Reservation.",
        },
    )
    provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
            "help": "Provider reservation reference key.",
        },
    )


@dataclass
class TermConditions:
    """
    The terms and conditions to be included in Fax details
    """

    language_option: List[LanguageOption] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "LanguageOption",
            "type": "Element",
        },
    )
    include_term_conditions: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "IncludeTermConditions",
            "type": "Attribute",
            "help": "Specifies whether Term and Conditions included in the Fax or not .",
        },
    )


@dataclass
class Text(TypeTextElement):
    """
    Type of Text, Eg-'Upsell','Marketing Agent','Marketing Consumer','Strapline','Rule'.
    """

    pass


@dataclass
class TicketDesignator:
    """
    Ticket Designator used to further qualify a Fare Basis Code.
    """

    value: TypeTicketDesignator = field(
        default=None,
        metadata={"required": True, "name": "Value", "type": "Attribute"},
    )


@dataclass
class TicketFailureInfo:
    """
    Will be optionally returned as part of AirTicketingRsp if one or all ticket requests fail. Atrributes are faiilure code, failure message, and passenger reference key. Passenger name is a child element.
    """

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirPricingInfoRef",
            "type": "Element",
            "help": "Returns related air pricing infos.",
        },
    )
    name: str = field(
        default=None,
        metadata={"required": True, "name": "Name", "type": "Element"},
    )
    code: int = field(
        default=None,
        metadata={"required": True, "name": "Code", "type": "Attribute"},
    )
    message: str = field(
        default=None, metadata={"name": "Message", "type": "Attribute"}
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )


@dataclass
class TicketInfo:
    name: str = field(
        default=None,
        metadata={"required": True, "name": "Name", "type": "Element"},
    )
    conjuncted_ticket_info: List[ConjunctedTicketInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "ConjunctedTicketInfo",
            "type": "Element",
        },
    )
    exchanged_ticket_info: List[ExchangedTicketInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ExchangedTicketInfo",
            "type": "Element",
        },
    )
    number: str = field(
        default=None,
        metadata={"required": True, "name": "Number", "type": "Attribute"},
    )
    iatanumber: TypeIata = field(
        default=None, metadata={"name": "IATANumber", "type": "Attribute"}
    )
    ticket_issue_date: str = field(
        default=None, metadata={"name": "TicketIssueDate", "type": "Attribute"}
    )
    ticketing_agent_sign_on: str = field(
        default=None,
        metadata={"name": "TicketingAgentSignOn", "type": "Attribute"},
    )
    country_code: TypeCountry = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "help": "Contains Ticketed PCC’s Country code.",
        },
    )
    status: TypeTicketStatus = field(
        default=None,
        metadata={"required": True, "name": "Status", "type": "Attribute"},
    )
    bulk_ticket: bool = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
            "help": "Whether the ticket was issued as bulk.",
        },
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "help": "A reference to a passenger.",
        },
    )
    air_pricing_info_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Attribute",
            "help": "A reference to a AirPricing.Applicable Providers 1G and 1V.",
        },
    )


@dataclass
class Title(TypeTextElement):
    """
    The additional titles associated to the brand or optional service. Providers: ACH, RCH, 1G, 1V, 1P, 1J.
    """

    pass


@dataclass
class TourCode:
    """
    Tour Code Fare Basis
    """

    value: TypeTourCode = field(
        default=None,
        metadata={"required": True, "name": "Value", "type": "Attribute"},
    )


@dataclass
class TypeRestrictionLengthOfStay:
    """
    Length Of Stay Restriction ( e.g. 2 day minimum..)
    """

    length: int = field(
        default=None, metadata={"name": "Length", "type": "Attribute"}
    )
    stay_unit: TypeStayUnit = field(
        default=None, metadata={"name": "StayUnit", "type": "Attribute"}
    )
    stay_date: str = field(
        default=None, metadata={"name": "StayDate", "type": "Attribute"}
    )
    more_rules_present: bool = field(
        default=None,
        metadata={
            "name": "MoreRulesPresent",
            "type": "Attribute",
            "help": "If true, specifies that advance purchase information will be present in fare rules.",
        },
    )


@dataclass
class TypeTaxInfoWithPaymentRef(TypeTaxInfo):
    payment_ref: List[PaymentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "PaymentRef",
            "type": "Element",
            "help": "This reference elements will associate relevant payment to this tax",
        },
    )


@dataclass
class TypeTicketFailureInfo:
    """
    Will be optionally returned as part if one or all ticketing requests fail.
    """

    booking_traveler_ref: List[TypeRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "BookingTravelerRef",
            "type": "Element",
        },
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "TCRNumber",
            "type": "Element",
            "help": "The identifying number for a Ticketless Air Reservation.",
        },
    )
    ticket_number: TicketNumber = field(
        default=None,
        metadata={"required": True, "name": "TicketNumber", "type": "Element"},
    )
    name: str = field(
        default=None,
        metadata={"required": True, "name": "Name", "type": "Element"},
    )
    code: int = field(
        default=None,
        metadata={"required": True, "name": "Code", "type": "Attribute"},
    )
    message: str = field(
        default=None, metadata={"name": "Message", "type": "Attribute"}
    )


@dataclass
class TypeTicketingModifiersRef:
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingInfoRef",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class TypeWeight:
    value: int = field(
        default=None, metadata={"name": "Value", "type": "Attribute"}
    )
    unit: TypeUnitWeight = field(
        default=None, metadata={"name": "Unit", "type": "Attribute"}
    )


@dataclass
class Variance:
    """
    Indicates any variance in the requested flight.
    """

    type: TypeVarianceType = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Attribute",
            "help": "Indicates type Variance, i.e. Actual, Estimated, Canceled and Diversion.",
        },
    )
    time: str = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
            "help": "Indicates time for Variance.",
        },
    )
    indicator: TypeVarianceIndicator = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
            "help": "Indicates VAriance Indicator, i.e. Early, Late.",
        },
    )
    reason: str = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Attribute",
            "help": "Reason for Variance",
        },
    )


@dataclass
class WaiverCode:
    """
    Waiver code to override fare validations
    """

    tour_code: TypeTourCode = field(
        default=None, metadata={"name": "TourCode", "type": "Attribute"}
    )
    ticket_designator: TypeTicketDesignator = field(
        default=None,
        metadata={"name": "TicketDesignator", "type": "Attribute"},
    )
    endorsement: str = field(
        default=None,
        metadata={
            "name": "Endorsement",
            "type": "Attribute",
            "help": "Endorsement. Size can be up to 100 characters",
        },
    )


@dataclass
class AirExchangeBundleList:
    """
    The shared object list of AirsegmentData
    """

    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirExchangeBundle",
            "type": "Element",
        },
    )


@dataclass
class AirExchangeTicketBundle:
    ticket_number: TicketNumber = field(
        default=None,
        metadata={"required": True, "name": "TicketNumber", "type": "Element"},
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "FormOfPayment",
            "type": "Element",
        },
    )
    form_of_payment_ref: FormOfPaymentRef = field(
        default=None, metadata={"name": "FormOfPaymentRef", "type": "Element"}
    )
    waiver_code: WaiverCode = field(
        default=None, metadata={"name": "WaiverCode", "type": "Element"}
    )


@dataclass
class AirFareDisplayModifiers:
    trip_type: List[TypeFareTripType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "TripType",
            "type": "Element",
        },
    )
    cabin_class: CabinClass = field(
        default=None, metadata={"name": "CabinClass", "type": "Element"}
    )
    penalty_fare_information: PenaltyFareInformation = field(
        default=None,
        metadata={
            "name": "PenaltyFareInformation",
            "type": "Element",
            "help": "Request Fares with specific Penalty Information.",
        },
    )
    fare_search_option: List[TypeFareSearchOption] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "FareSearchOption",
            "type": "Element",
        },
    )
    max_responses: int = field(
        default="200", metadata={"name": "MaxResponses", "type": "Attribute"}
    )
    departure_date: str = field(
        default=None, metadata={"name": "DepartureDate", "type": "Attribute"}
    )
    ticketing_date: str = field(
        default=None, metadata={"name": "TicketingDate", "type": "Attribute"}
    )
    return_date: str = field(
        default=None, metadata={"name": "ReturnDate", "type": "Attribute"}
    )
    base_fare_only: bool = field(
        default="false", metadata={"name": "BaseFareOnly", "type": "Attribute"}
    )
    unrestricted_fares_only: bool = field(
        default="false",
        metadata={"name": "UnrestrictedFaresOnly", "type": "Attribute"},
    )
    fares_indicator: TypeFaresIndicator = field(
        default=None,
        metadata={
            "name": "FaresIndicator",
            "type": "Attribute",
            "help": "Indicates whether only public fares should be returned or specific type of private fares",
        },
    )
    currency_type: TypeCurrency = field(
        default=None, metadata={"name": "CurrencyType", "type": "Attribute"}
    )
    include_taxes: bool = field(
        default=None, metadata={"name": "IncludeTaxes", "type": "Attribute"}
    )
    include_estimated_taxes: bool = field(
        default=None,
        metadata={
            "name": "IncludeEstimatedTaxes",
            "type": "Attribute",
            "help": "Indicates to include estimated taxes i.e. if set to true estimated total fare,base fare and taxes would be returned.",
        },
    )
    include_surcharges: bool = field(
        default=None,
        metadata={"name": "IncludeSurcharges", "type": "Attribute"},
    )
    global_indicator: TypeAtpcoglobalIndicator = field(
        default=None, metadata={"name": "GlobalIndicator", "type": "Attribute"}
    )
    prohibit_min_stay_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitMinStayFares", "type": "Attribute"},
    )
    prohibit_max_stay_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitMaxStayFares", "type": "Attribute"},
    )
    prohibit_advance_purchase_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitAdvancePurchaseFares", "type": "Attribute"},
    )
    prohibit_non_refundable_fares: bool = field(
        default="false",
        metadata={
            "name": "ProhibitNonRefundableFares",
            "type": "Attribute",
            "help": "Indicates whether it prohibits NonRefundable Fares.",
        },
    )
    validated_fares_only: bool = field(
        default=None,
        metadata={
            "name": "ValidatedFaresOnly",
            "type": "Attribute",
            "help": "Indicates that the requested Fares should be Validated Fares only. If set to true, then only valid fares will be returned. If set to false, both valid and non valid fares will be returned. If not sent, then no validation will be done. All fares will be returned.",
        },
    )
    prohibit_travel_restricted_fares: bool = field(
        default="true",
        metadata={
            "name": "ProhibitTravelRestrictedFares",
            "type": "Attribute",
            "help": "Indicates that the Fares not complying Travel Restrictions and Seasonality fare rules are prohibited",
        },
    )
    filed_currency: TypeCurrency = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "help": "Represents the filed currency of the fare",
        },
    )


@dataclass
class AirFareRulesModifier:
    """
    The modifiers for Air Fare Rules
    """

    air_fare_rule_category: List[AirFareRuleCategory] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirFareRuleCategory",
            "type": "Element",
        },
    )


@dataclass
class AirItineraryDetails:
    """
    Itinerary details containing brand details
    """

    air_segment_details: List[AirSegmentDetails] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 16,
            "name": "AirSegmentDetails",
            "type": "Element",
        },
    )
    passenger_details: List[PassengerDetails] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 15,
            "name": "PassengerDetails",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "Key",
            "type": "Attribute",
            "help": "Air itinerary details key",
        },
    )


@dataclass
class AirItinerarySolution:
    """
    The pricing container for an air travel itinerary
    """

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentRef",
            "type": "Element",
        },
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Connection",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class AirLegModifiers:
    permitted_cabins: PermittedCabins = field(
        default=None, metadata={"name": "PermittedCabins", "type": "Element"}
    )
    preferred_cabins: PreferredCabins = field(
        default=None, metadata={"name": "PreferredCabins", "type": "Element"}
    )
    permitted_carriers: PermittedCarriers = field(
        default=None, metadata={"name": "PermittedCarriers", "type": "Element"}
    )
    prohibited_carriers: ProhibitedCarriers = field(
        default=None,
        metadata={"name": "ProhibitedCarriers", "type": "Element"},
    )
    preferred_carriers: PreferredCarriers = field(
        default=None, metadata={"name": "PreferredCarriers", "type": "Element"}
    )
    permitted_connection_points: "AirLegModifiers.PermittedConnectionPoints" = field(
        default=None,
        metadata={
            "name": "PermittedConnectionPoints",
            "type": "Element",
            "help": "This is the container to specify all permitted connection points. Applicable for 1G/1V/1P/1J.",
        },
    )
    prohibited_connection_points: "AirLegModifiers.ProhibitedConnectionPoints" = field(
        default=None,
        metadata={
            "name": "ProhibitedConnectionPoints",
            "type": "Element",
            "help": "This is the container to specify all prohibited connection points. Applicable for 1G/1V/1P/1J.",
        },
    )
    preferred_connection_points: "AirLegModifiers.PreferredConnectionPoints" = field(
        default=None,
        metadata={
            "name": "PreferredConnectionPoints",
            "type": "Element",
            "help": "This is the container to specify all preferred connection points. Applicable for 1G/1V only.",
        },
    )
    permitted_booking_codes: "AirLegModifiers.PermittedBookingCodes" = field(
        default=None,
        metadata={
            "name": "PermittedBookingCodes",
            "type": "Element",
            "help": "This is the container to specify all permitted booking codes",
        },
    )
    preferred_booking_codes: PreferredBookingCodes = field(
        default=None,
        metadata={"name": "PreferredBookingCodes", "type": "Element"},
    )
    preferred_alliances: "AirLegModifiers.PreferredAlliances" = field(
        default=None,
        metadata={"name": "PreferredAlliances", "type": "Element"},
    )
    prohibited_booking_codes: "AirLegModifiers.ProhibitedBookingCodes" = field(
        default=None,
        metadata={
            "name": "ProhibitedBookingCodes",
            "type": "Element",
            "help": "This is the container to specify all prohibited booking codes",
        },
    )
    disfavored_alliances: "AirLegModifiers.DisfavoredAlliances" = field(
        default=None,
        metadata={"name": "DisfavoredAlliances", "type": "Element"},
    )
    flight_type: FlightType = field(
        default=None, metadata={"name": "FlightType", "type": "Element"}
    )
    anchor_flight_data: TypeAnchorFlightData = field(
        default=None, metadata={"name": "AnchorFlightData", "type": "Element"}
    )
    prohibit_overnight_layovers: bool = field(
        default="false",
        metadata={
            "name": "ProhibitOvernightLayovers",
            "type": "Attribute",
            "help": "If true, excludes connections if arrival time of first flight and departure time of second flight is on 2 different calendar days. When used in conjunction with MaxConnectionTime, it would exclude all connections if the connecting flights wait time exceeds the time specified in MaxConnectionTime.",
        },
    )
    max_connection_time: int = field(
        default=None,
        metadata={"name": "MaxConnectionTime", "type": "Attribute"},
    )
    return_first_available_only: bool = field(
        default=None,
        metadata={
            "name": "ReturnFirstAvailableOnly",
            "type": "Attribute",
            "help": "If it is true then it will search for first available for the booking code designated or any booking code in same cabin.",
        },
    )
    allow_direct_access: bool = field(
        default="false",
        metadata={
            "name": "AllowDirectAccess",
            "type": "Attribute",
            "help": "If it is true request will be sent directly to the carrier.",
        },
    )
    prohibit_multi_airport_connection: bool = field(
        default=None,
        metadata={
            "name": "ProhibitMultiAirportConnection",
            "type": "Attribute",
            "help": "Indicates whether to restrict multi-airport connections",
        },
    )
    prefer_non_stop: bool = field(
        default="false",
        metadata={
            "name": "PreferNonStop",
            "type": "Attribute",
            "help": "When non-stops are preferred, the distribution of search results should skew heavily toward non-stop flights while still returning some one stop flights for comparison and price competitiveness. The search request will ‘boost' the preference towards non-stops. If true then Non Stop flights will be preferred.",
        },
    )
    order_by: str = field(
        default=None,
        metadata={
            "name": "OrderBy",
            "type": "Attribute",
            "help": "Indicates whether to sort by Journey Time, Deparature Time or Arrival Time",
        },
    )
    max_journey_time: TypeMaxJourneyTime = field(
        default=None,
        metadata={
            "name": "MaxJourneyTime",
            "type": "Attribute",
            "help": "Maximum Journey Time for this leg (in hours) 0-99. Supported Providers 1G,1V.",
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
    class PreferredConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 99,
                "name": "ConnectionPoint",
                "type": "Element",
            },
        )

    @dataclass
    class PermittedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "BookingCode",
                "type": "Element",
            },
        )

    @dataclass
    class PreferredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "Alliance",
                "type": "Element",
            },
        )

    @dataclass
    class ProhibitedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "BookingCode",
                "type": "Element",
            },
        )

    @dataclass
    class DisfavoredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "Alliance",
                "type": "Element",
            },
        )


@dataclass
class AirPricingModifiers:
    """
    Controls and switches for a Air Search request that contains Pricing Information
    """

    prohibited_rule_categories: "AirPricingModifiers.ProhibitedRuleCategories" = field(
        default=None,
        metadata={"name": "ProhibitedRuleCategories", "type": "Element"},
    )
    account_codes: "AirPricingModifiers.AccountCodes" = field(
        default=None, metadata={"name": "AccountCodes", "type": "Element"}
    )
    permitted_cabins: PermittedCabins = field(
        default=None, metadata={"name": "PermittedCabins", "type": "Element"}
    )
    contract_codes: "AirPricingModifiers.ContractCodes" = field(
        default=None, metadata={"name": "ContractCodes", "type": "Element"}
    )
    exempt_taxes: ExemptTaxes = field(
        default=None, metadata={"name": "ExemptTaxes", "type": "Element"}
    )
    penalty_fare_information: PenaltyFareInformation = field(
        default=None,
        metadata={
            "name": "PenaltyFareInformation",
            "type": "Element",
            "help": "Request Fares with specific Penalty Information.",
        },
    )
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
    promo_codes: "AirPricingModifiers.PromoCodes" = field(
        default=None, metadata={"name": "PromoCodes", "type": "Element"}
    )
    manual_fare_adjustment: List[ManualFareAdjustment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ManualFareAdjustment",
            "type": "Element",
            "help": "Represents increment/discount applied manually by agent.",
        },
    )
    point_of_sale: PointOfSale = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "help": "User can use this node to send a specific PCC to access fares allowed only for that PCC. This node gives the capability for fare redistribution at stored fare level. As multiple UAPI AirPricingInfos (all having same AirPricingInfoGroup) can converge to a single stored fare, UAPI will map PoinOfSale information from the first available one from each group",
        },
    )
    brand_modifiers: BrandModifiers = field(
        default=None,
        metadata={
            "name": "BrandModifiers",
            "type": "Element",
            "help": "Used to specify the level of branding requested.",
        },
    )
    multi_gdssearch_indicator: List[MultiGdssearchIndicator] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "MultiGDSSearchIndicator",
            "type": "Element",
        },
    )
    preferred_cabins: List[PreferredCabins] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "PreferredCabins",
            "type": "Element",
        },
    )
    prohibit_min_stay_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitMinStayFares", "type": "Attribute"},
    )
    prohibit_max_stay_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitMaxStayFares", "type": "Attribute"},
    )
    currency_type: TypeCurrency = field(
        default=None, metadata={"name": "CurrencyType", "type": "Attribute"}
    )
    prohibit_advance_purchase_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitAdvancePurchaseFares", "type": "Attribute"},
    )
    prohibit_non_refundable_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitNonRefundableFares", "type": "Attribute"},
    )
    prohibit_restricted_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitRestrictedFares", "type": "Attribute"},
    )
    fares_indicator: TypeFaresIndicator = field(
        default=None,
        metadata={
            "name": "FaresIndicator",
            "type": "Attribute",
            "help": "Indicates whether only public fares should be returned or specific type of private fares",
        },
    )
    filed_currency: TypeCurrency = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "help": "Currency in which Fares/Prices will be filed if supported by the supplier else approximated to.",
        },
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "help": "The Plating Carrier for this journey.",
        },
    )
    override_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "OverrideCarrier",
            "type": "Attribute",
            "help": "The Plating Carrier for this journey.",
        },
    )
    eticketability: TypeEticketability = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
            "help": "Request a search based on whether only E-ticketable fares are required.",
        },
    )
    account_code_fares_only: bool = field(
        default=None,
        metadata={
            "name": "AccountCodeFaresOnly",
            "type": "Attribute",
            "help": "Indicates whether or not the private fares returned should be restricted to only those specific to the input account code and contract code.",
        },
    )
    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )
    prohibit_non_exchangeable_fares: bool = field(
        default="false",
        metadata={"name": "ProhibitNonExchangeableFares", "type": "Attribute"},
    )
    force_segment_select: bool = field(
        default="false",
        metadata={
            "name": "ForceSegmentSelect",
            "type": "Attribute",
            "help": "This indicator allows agent to force segment select option in host while selecting all air segments to store price on a PNR. This is relevent only when agent selects all air segmnets to price. if agent selects specific segments to price then this attribute will be ignored by the system. This is currently used by Worldspan only.",
        },
    )
    inventory_request_type: TypeInventoryRequest = field(
        default=None,
        metadata={
            "name": "InventoryRequestType",
            "type": "Attribute",
            "help": "This allows user to make request for a particular source of inventory for pricing modifier purposes. This is currently used by Worldspan only.",
        },
    )
    one_way_shop: bool = field(
        default="false",
        metadata={
            "name": "OneWayShop",
            "type": "Attribute",
            "help": "Via this attribute one way shop can be requested. Applicable provider is 1G",
        },
    )
    prohibit_unbundled_fare_types: bool = field(
        default=None,
        metadata={
            "name": "ProhibitUnbundledFareTypes",
            "type": "Attribute",
            "help": 'A "True" value wiill remove fares with EOU and ERU fare types from consideration. A "False" value is the same as no value. Default is no value. Applicable providers: 1P/1J/1G/1V',
        },
    )
    return_services: bool = field(
        default="true",
        metadata={
            "name": "ReturnServices",
            "type": "Attribute",
            "help": "When set to false, ATPCO filed Optional Services will not be returned. Default is true. Provider: 1G, 1V, 1P, 1J",
        },
    )
    channel_id: str = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "help": "A Channel ID is 2 to 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.",
        },
    )
    return_fare_attributes: bool = field(
        default="false",
        metadata={
            "name": "ReturnFareAttributes",
            "type": "Attribute",
            "help": "Returns attributes that are associated to a fare",
        },
    )
    sell_check: bool = field(
        default="false",
        metadata={
            "name": "SellCheck",
            "type": "Attribute",
            "help": "Checks if the segment is bookable before pricing",
        },
    )
    return_failed_segments: bool = field(
        default="false",
        metadata={
            "name": "ReturnFailedSegments",
            "type": "Attribute",
            "help": 'If "true", returns failed segments information.',
        },
    )

    @dataclass
    class ProhibitedRuleCategories:
        fare_rule_category: List[FareRuleCategory] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "FareRuleCategory",
                "type": "Element",
            },
        )

    @dataclass
    class AccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "AccountCode",
                "type": "Element",
                "help": "Used to get negotiated pricing. Provider:ACH.",
            },
        )

    @dataclass
    class ContractCodes:
        contract_code: List[ContractCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "ContractCode",
                "type": "Element",
            },
        )

    @dataclass
    class PromoCodes:
        promo_code: List[PromoCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "PromoCode",
                "type": "Element",
            },
        )


@dataclass
class AirRefundBundle:
    """
    Used both in request and response
    """

    air_refund_info: AirRefundInfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirRefundInfo",
            "type": "Element",
        },
    )
    name: List[str] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Name",
            "type": "Element",
        },
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
        },
    )
    waiver_code: WaiverCode = field(
        default=None, metadata={"name": "WaiverCode", "type": "Element"}
    )
    ticket_number: str = field(
        default=None, metadata={"name": "TicketNumber", "type": "Attribute"}
    )
    refund_type: str = field(
        default=None,
        metadata={
            "name": "RefundType",
            "type": "Attribute",
            "help": "Specifies whether this bundle was auto or manually generated",
        },
    )


@dataclass
class AirSearchModifiers:
    """
    Controls and switches for the Air Search request
    """

    disfavored_providers: "AirSearchModifiers.DisfavoredProviders" = field(
        default=None,
        metadata={"name": "DisfavoredProviders", "type": "Element"},
    )
    preferred_providers: "AirSearchModifiers.PreferredProviders" = field(
        default=None,
        metadata={"name": "PreferredProviders", "type": "Element"},
    )
    disfavored_carriers: "AirSearchModifiers.DisfavoredCarriers" = field(
        default=None,
        metadata={"name": "DisfavoredCarriers", "type": "Element"},
    )
    permitted_carriers: PermittedCarriers = field(
        default=None, metadata={"name": "PermittedCarriers", "type": "Element"}
    )
    prohibited_carriers: ProhibitedCarriers = field(
        default=None,
        metadata={"name": "ProhibitedCarriers", "type": "Element"},
    )
    preferred_carriers: PreferredCarriers = field(
        default=None, metadata={"name": "PreferredCarriers", "type": "Element"}
    )
    permitted_cabins: PermittedCabins = field(
        default=None, metadata={"name": "PermittedCabins", "type": "Element"}
    )
    preferred_cabins: PreferredCabins = field(
        default=None, metadata={"name": "PreferredCabins", "type": "Element"}
    )
    preferred_alliances: "AirSearchModifiers.PreferredAlliances" = field(
        default=None,
        metadata={"name": "PreferredAlliances", "type": "Element"},
    )
    disfavored_alliances: "AirSearchModifiers.DisfavoredAlliances" = field(
        default=None,
        metadata={"name": "DisfavoredAlliances", "type": "Element"},
    )
    permitted_booking_codes: "AirSearchModifiers.PermittedBookingCodes" = field(
        default=None,
        metadata={
            "name": "PermittedBookingCodes",
            "type": "Element",
            "help": "This is the container to specify all permitted booking codes",
        },
    )
    preferred_booking_codes: PreferredBookingCodes = field(
        default=None,
        metadata={"name": "PreferredBookingCodes", "type": "Element"},
    )
    prohibited_booking_codes: "AirSearchModifiers.ProhibitedBookingCodes" = field(
        default=None,
        metadata={
            "name": "ProhibitedBookingCodes",
            "type": "Element",
            "help": "This is the container to specify all prohibited booking codes",
        },
    )
    flight_type: FlightType = field(
        default=None, metadata={"name": "FlightType", "type": "Element"}
    )
    max_layover_duration: MaxLayoverDurationType = field(
        default=None,
        metadata={
            "name": "MaxLayoverDuration",
            "type": "Element",
            "help": "This is the maximum duration the layover may have for each trip in the request. Supported providers 1P, 1J.",
        },
    )
    native_search_modifier: TypeNativeSearchModifier = field(
        default=None,
        metadata={
            "name": "NativeSearchModifier",
            "type": "Element",
            "help": "Container for Native command modifiers. Providers supported : 1P",
        },
    )
    distance_type: TypeDistance = field(
        default="MI", metadata={"name": "DistanceType", "type": "Attribute"}
    )
    include_flight_details: bool = field(
        default="true",
        metadata={"name": "IncludeFlightDetails", "type": "Attribute"},
    )
    allow_change_of_airport: bool = field(
        default="true",
        metadata={"name": "AllowChangeOfAirport", "type": "Attribute"},
    )
    prohibit_overnight_layovers: bool = field(
        default="false",
        metadata={
            "name": "ProhibitOvernightLayovers",
            "type": "Attribute",
            "help": "If true, excludes connections if arrival time of first flight and departure time of second flight is on 2 different calendar days. When used in conjunction with MaxConnectionTime, it would exclude all connections if the connecting flights wait time exceeds the time specified in MaxConnectionTime.",
        },
    )
    max_solutions: int = field(
        default=None,
        metadata={
            "name": "MaxSolutions",
            "type": "Attribute",
            "help": "The maximum number of solutions to return. Decreasing this number",
        },
    )
    max_connection_time: int = field(
        default=None,
        metadata={
            "name": "MaxConnectionTime",
            "type": "Attribute",
            "help": "The maximum anount of time (in minutes) that a solution can contain for connections between flights.",
        },
    )
    search_weekends: bool = field(
        default=None,
        metadata={
            "name": "SearchWeekends",
            "type": "Attribute",
            "help": "A value of true indicates that search should be expanded to include weekend combinations, if applicable.",
        },
    )
    include_extra_solutions: bool = field(
        default=None,
        metadata={
            "name": "IncludeExtraSolutions",
            "type": "Attribute",
            "help": "If true, indicates that search should be made for returning more solutions, if available. For example, for certain providers, premium members may have the facility to get more solutions. This attribute may have to be combined with other applicable modifiers (like SearchWeekends) to return more results.",
        },
    )
    prohibit_multi_airport_connection: bool = field(
        default=None,
        metadata={
            "name": "ProhibitMultiAirportConnection",
            "type": "Attribute",
            "help": "Indicates whether to restrict multi-airport connections",
        },
    )
    prefer_non_stop: bool = field(
        default="false",
        metadata={
            "name": "PreferNonStop",
            "type": "Attribute",
            "help": "When non-stops are preferred, the distribution of search results should skew heavily toward non-stop flights while still returning some one stop flights for comparison and price competitiveness. The search request will ‘boost' the preference towards non-stops. If true then Non Stop flights will be preferred.",
        },
    )
    order_by: str = field(
        default=None,
        metadata={
            "name": "OrderBy",
            "type": "Attribute",
            "help": "Indicates whether to sort by Journey Time, Deparature Time or Arrival Time. Applicable to air availability only.",
        },
    )
    exclude_open_jaw_airport: bool = field(
        default="false",
        metadata={
            "name": "ExcludeOpenJawAirport",
            "type": "Attribute",
            "help": "This option ensures that travel into/out of each location will be into/out of the same airport of that location. Values are true or false. Default value is 'false'. If value is true then open jaws are exclude. If false the open jaws are included. The supported providers: 1P, 1J",
        },
    )
    exclude_ground_transportation: bool = field(
        default="false",
        metadata={
            "name": "ExcludeGroundTransportation",
            "type": "Attribute",
            "help": "Indicates whether to allow the user to exclude ground transportation or not. Default value is 'false'. If value is true then ground transportations are excluded. If false then ground transportations are included. The supported providers: 1P, 1J",
        },
    )
    max_journey_time: TypeMaxJourneyTime = field(
        default=None,
        metadata={
            "name": "MaxJourneyTime",
            "type": "Attribute",
            "help": "Maximum Journey Time for all legs (in hours) 0-99. For LFS Supported Providers are 1G,1V,1P,1J. For AirAvail Supported Providers are 1G,1V.",
        },
    )
    jet_service_only: bool = field(
        default=None,
        metadata={
            "name": "JetServiceOnly",
            "type": "Attribute",
            "help": "Restricts results to Jet service flights only.",
        },
    )

    @dataclass
    class DisfavoredProviders:
        provider: List[Provider] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "Provider",
                "type": "Element",
            },
        )

    @dataclass
    class PreferredProviders:
        provider: List[Provider] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "Provider",
                "type": "Element",
            },
        )

    @dataclass
    class DisfavoredCarriers:
        carrier: List[Carrier] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "Carrier",
                "type": "Element",
            },
        )

    @dataclass
    class PreferredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "Alliance",
                "type": "Element",
            },
        )

    @dataclass
    class DisfavoredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "Alliance",
                "type": "Element",
            },
        )

    @dataclass
    class PermittedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "BookingCode",
                "type": "Element",
            },
        )

    @dataclass
    class ProhibitedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "BookingCode",
                "type": "Element",
            },
        )


@dataclass
class AirTicketingModifiers:
    """
    Modifiers used during ticketing
    """

    document_modifiers: DocumentModifiers = field(
        default=None, metadata={"name": "DocumentModifiers", "type": "Element"}
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingInfoRef",
            "type": "Element",
        },
    )
    tour_code: TourCode = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Element",
            "help": "Allows an agency to modify the tour code information during ticket issuance. Providers supported: Worldspan and JAL.",
        },
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "TicketEndorsement",
            "type": "Element",
            "help": "Allows an agency to add user defined ticketing endorsements in the ticket. Providers supported: Worldspan and JAL.",
        },
    )
    commission: Commission = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "help": "Allows an agency to add the commission to a new or different commission rate which will be applied at time of ticketing. The commission Modifier allows the user specify how the commission change is to applied. Providers supported: Worldspan and JAL.",
        },
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FormOfPayment",
            "type": "Element",
            "help": "FormOfPayment information to be used as ticketing modifier at the time of ticketing. Providers supported: Galileo, Apollo, Worldspan and JAL.",
        },
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "CreditCardAuth",
            "type": "Element",
            "help": "CreditCardAuth information to be used as ticketing modifier at the time of ticketing. Providers supported: Galileo, Apollo, Worldspan and JAL.",
        },
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Payment",
            "type": "Element",
            "help": "Provide Payment for FOP. Providers supported: Galileo, Apollo, Worldspan and JAL.",
        },
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "help": "The Plating Carrier used for this ticket",
        },
    )
    ticketed_fare_override: bool = field(
        default="false",
        metadata={
            "name": "TicketedFareOverride",
            "type": "Attribute",
            "help": "It is a modifier to allow re-issuance of tickets for stored fares which are already ticketed. Providers supported are 1P/1J",
        },
    )
    suppress_tax_and_fee: bool = field(
        default="false",
        metadata={
            "name": "SuppressTaxAndFee",
            "type": "Attribute",
            "help": "Allow to suppress Taxand Fee in ticketing response.Providers supported: Worldspan and JAL.",
        },
    )
    no_comparison_sfq: bool = field(
        default="false",
        metadata={
            "name": "NoComparisonSFQ",
            "type": "Attribute",
            "help": '1P/1J - Set to "true" to include the no comparison overide #NC to override the existing SFQ and issue the ticket. Only valid for AirTicketingReq, not valid for AirExchangeTicketingReq.',
        },
    )


@dataclass
class AlternateRoute:
    """
    Information about this Alternate Route component
    """

    leg: List[Leg] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "Leg",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class ApisrequirementsList:
    """
    The shared object list of APISRequirements
    """

    apisrequirements: List[Apisrequirements] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "APISRequirements",
            "type": "Element",
        },
    )


@dataclass
class BaggageAllowance:
    """
    Free Baggage Allowance
    """

    number_of_pieces: int = field(
        default=None, metadata={"name": "NumberOfPieces", "type": "Element"}
    )
    max_weight: TypeWeight = field(
        default=None, metadata={"name": "MaxWeight", "type": "Element"}
    )


@dataclass
class BaggageRestriction:
    """
    Information related to Baggage restriction rules .
    """

    dimension: List[Dimension] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Dimension",
            "type": "Element",
        },
    )
    max_weight: List[TypeUnitOfMeasure] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "MaxWeight",
            "type": "Element",
        },
    )
    text_info: List[TextInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TextInfo",
            "type": "Element",
        },
    )


@dataclass
class BookingRules:
    """
    Rules related to pre pay booking
    """

    booking_rules_fare_reference: List[BookingRulesFareReference] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BookingRulesFareReference",
            "type": "Element",
        },
    )
    rule_info: List["BookingRules.RuleInfo"] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RuleInfo",
            "type": "Element",
            "help": "Pre pay booking rule information",
        },
    )
    restriction: List[Restriction] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Restriction",
            "type": "Element",
            "help": "Booking restrictions for associated pre pay account",
        },
    )
    document_required: List[DocumentRequired] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "DocumentRequired",
            "type": "Element",
            "help": "Detail about required documents for this pre pay id",
        },
    )
    gender_dob_required: bool = field(
        default=None,
        metadata={
            "name": "GenderDobRequired",
            "type": "Attribute",
            "help": "Vendor populates if gender/DOB data is required in book.",
        },
    )

    @dataclass
    class RuleInfo:
        charges_rules: ChargesRules = field(
            default=None, metadata={"name": "ChargesRules", "type": "Element"}
        )


@dataclass
class BrandingInfo:
    """
    Branding information for the Ancillary Service. Returned in Seat Map only. Providers: 1G, 1V, 1P, 1J, ACH
    """

    price_range: List[PriceRange] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "PriceRange",
            "type": "Element",
            "help": "The price range of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        },
    )
    text: List[Text] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "Text",
            "type": "Element",
        },
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "Title",
            "type": "Element",
            "help": "The additional titles associated to the brand or optional service. Providers: ACH, 1G, 1V, 1P, 1J",
        },
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "ImageLocation",
            "type": "Element",
        },
    )
    service_group: ServiceGroup = field(
        default=None, metadata={"name": "ServiceGroup", "type": "Element"}
    )
    air_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 99,
            "name": "AirSegmentRef",
            "type": "Element",
            "help": "Specifies the AirSegment the branding information is for. Providers: ACH, 1G, 1V, 1P, 1J",
        },
    )
    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )
    service_sub_code: str = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "help": "The Service Sub Code of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        },
    )
    external_service_name: str = field(
        default=None,
        metadata={
            "name": "ExternalServiceName",
            "type": "Attribute",
            "help": "The external name of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        },
    )
    service_type: str = field(
        default=None,
        metadata={
            "name": "ServiceType",
            "type": "Attribute",
            "help": "The type of Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        },
    )
    commercial_name: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "CommercialName",
            "type": "Attribute",
            "help": "The commercial name of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        },
    )
    chargeable: str = field(
        default=None,
        metadata={
            "name": "Chargeable",
            "type": "Attribute",
            "help": "Indicates if the optional service is not offered, is available for a charge, or is included in the brand. Providers: 1G, 1V, 1P, 1J, ACH",
        },
    )


@dataclass
class BundledServices:
    bundled_service: List[BundledService] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 16,
            "name": "BundledService",
            "type": "Element",
        },
    )


@dataclass
class Coupon:
    """
    The flight coupon that resulted from the ticketing operation.
    """

    ticket_designator: List[TicketDesignator] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketDesignator",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )
    coupon_number: int = field(
        default=None,
        metadata={
            "name": "CouponNumber",
            "type": "Attribute",
            "help": "The sequential number of this coupon.",
        },
    )
    operating_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "help": "The true carrier.",
        },
    )
    operating_flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "name": "OperatingFlightNumber",
            "type": "Attribute",
            "help": "The true carrier's flight number.",
        },
    )
    marketing_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "MarketingCarrier",
            "type": "Attribute",
            "help": "If codeshare applies to this, this is the marketing carrier (as opposed to the operating carrier).",
        },
    )
    marketing_flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "name": "MarketingFlightNumber",
            "type": "Attribute",
            "help": "If codeshare applies to this, this is the marketing flight number (as opposed to the operating flight number).",
        },
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Origin",
            "type": "Attribute",
            "help": "Returns the airport or city code that defines the origin market for this fare.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Destination",
            "type": "Attribute",
            "help": "Returns the airport or city code that defines the destination market for this fare.",
        },
    )
    departure_time: str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "help": "The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location. In case of open segment this will not be returned.",
        },
    )
    arrival_time: str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
            "help": "The date and time at which this entity arrives at the destination. This does not include time zone information since it can be derived from the origin location.",
        },
    )
    stopover_code: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "StopoverCode",
            "type": "Attribute",
            "help": "Stopover code - indicator that stopover is allowed at Origin Airport or City.",
        },
    )
    booking_class: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "BookingClass",
            "type": "Attribute",
            "help": "Booked fare class for coupon.",
        },
    )
    fare_basis: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "FareBasis",
            "type": "Attribute",
            "help": "The fare basis code for this fare",
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
    status: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "Status",
            "type": "Attribute",
            "help": 'The status of this coupon returend from host is mapped as follows Code="A" Status="Airport Controlled" Code="C" Status="Checked In" Code="F" Status="Flown/Used" Code="L" Status="Boarded/Lifted" Code="O" Status="Open" Code="P" Status="Printed" Code="R" Status="Refunded" Code="E" Status="Exchanged" Code="V" Status="Void" Code="Z" Status="Archived/Carrier Modified" Code="U" Status="Unavailable" Code="S" Status="Suspended" Code="I" Status="Irregular Ops" Code="D" Status="Deleted/Removed" Code="X" Status="Unknown"',
        },
    )
    segment_group: int = field(
        default=None,
        metadata={
            "name": "SegmentGroup",
            "type": "Attribute",
            "help": "Indicates the grouping in which this segment resides based on Origin/Destination pairs in itinerary",
        },
    )
    marriage_group: int = field(
        default=None,
        metadata={
            "name": "MarriageGroup",
            "type": "Attribute",
            "help": "Airline Marrraige group indicator",
        },
    )


@dataclass
class DetailedBillingInformation:
    """
    Container to send Detailed Billing Information for ticketing
    """

    form_of_payment_ref: FormOfPaymentRef = field(
        default=None, metadata={"name": "FormOfPaymentRef", "type": "Element"}
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirPricingInfoRef",
            "type": "Element",
            "help": "Returns related air pricing infos.",
        },
    )
    billing_detail_item: List[BillingDetailItem] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "BillingDetailItem",
            "type": "Element",
        },
    )


@dataclass
class DocumentInfo:
    """
    Container for the document information summary line.
    """

    ticket_info: List[TicketInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketInfo",
            "type": "Element",
        },
    )
    mcoinfo: List[Mcoinformation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "MCOInfo",
            "type": "Element",
        },
    )
    tcrinfo: List[Tcrinfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TCRInfo",
            "type": "Element",
        },
    )


@dataclass
class DocumentSelect:
    """
    Allows an agency to select the documents to produce for the itinerary.
    """

    back_office_hand_off: BackOfficeHandOff = field(
        default=None, metadata={"name": "BackOfficeHandOff", "type": "Element"}
    )
    itinerary: Itinerary = field(
        default=None, metadata={"name": "Itinerary", "type": "Element"}
    )
    issue_ticket_only: bool = field(
        default=None,
        metadata={
            "name": "IssueTicketOnly",
            "type": "Attribute",
            "help": "Set to true to alter system default of itinerary,ticket and back office.",
        },
    )
    issue_electronic_ticket: bool = field(
        default=None,
        metadata={
            "name": "IssueElectronicTicket",
            "type": "Attribute",
            "help": "Set to true for electronic tickets.",
        },
    )
    fax_indicator: bool = field(
        default=None,
        metadata={
            "name": "FaxIndicator",
            "type": "Attribute",
            "help": "Set to true for providing fax details.",
        },
    )


@dataclass
class EmbargoInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Embargo
    """

    pass


@dataclass
class Emdinfo:
    """
    This is the parent container to display EMD information. Occurrence of multiple unique EMDs inside this container indicate that those EMDs are conjunctive to each other. Supported providers are 1G/1V/1P/1J
    """

    emdtraveler_info: EmdtravelerInfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "EMDTravelerInfo",
            "type": "Element",
            "help": "Basic information of the traveler associated with this EMDInfo.",
        },
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SupplierLocator",
            "type": "Element",
            "help": "List of Supplier Locator information that is associated with this document",
        },
    )
    electronic_misc_document: List[ElectronicMiscDocument] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "ElectronicMiscDocument",
            "type": "Element",
            "help": "Electronic miscellaneous documents.As an EMDInfo container displays all the EMDs which are in conjunction, there can be maximum 4 ElectronicMiscDocuments present in an EMDInfo",
        },
    )
    payment: Payment = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "help": "Payment charged for EMD isuance",
        },
    )
    form_of_payment: FormOfPayment = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "help": "FormOfPayment used for issuing these electronic miscellaneous documents",
        },
    )
    emdpricing_info: EmdpricingInfo = field(
        default=None,
        metadata={
            "name": "EMDPricingInfo",
            "type": "Element",
            "help": "Fare related information for these electronic miscellaneous documents",
        },
    )
    emdendorsement: List[Emdendorsement] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "EMDEndorsement",
            "type": "Element",
        },
    )
    fare_calc: FareCalc = field(
        default=None,
        metadata={
            "name": "FareCalc",
            "type": "Element",
            "help": "Infomration about the fare calculation",
        },
    )
    emdcommission: Emdcommission = field(
        default=None,
        metadata={
            "name": "EMDCommission",
            "type": "Element",
            "help": "Commission information applied during EMD issuance",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "help": "System generated Key",
        },
    )


@dataclass
class EmdsummaryInfo:
    """
    Container for EMD summary information. Supported providers are 1G/1V/1P/1J
    """

    emdsummary: List[Emdsummary] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "EMDSummary",
            "type": "Element",
            "help": "Summary information for EMDs conjuncted to each other.",
        },
    )
    emdtraveler_info: EmdtravelerInfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "EMDTravelerInfo",
            "type": "Element",
            "help": "EMD traveler information.",
        },
    )
    payment: Payment = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "help": "Payment charged to issue EMD.",
        },
    )
    provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
            "help": "A reference to the provider reservation with which the document is associated.Displayed when shown as part of UR.Not displayed in EMDRetrieveRsp",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "help": "System generated Key",
        },
    )


@dataclass
class Enumeration:
    """
    Provides the capability to group the results into differnt trip type and diversification strategies.
    """

    solution_group: List[SolutionGroup] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "SolutionGroup",
            "type": "Element",
        },
    )


@dataclass
class ExchangeEligibilityInfo:
    exchange_penalty_info: List[ExchangePenaltyInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ExchangePenaltyInfo",
            "type": "Element",
        },
    )
    eligible_fares: str = field(
        default=None,
        metadata={
            "name": "EligibleFares",
            "type": "Attribute",
            "help": "Identifies which fares are eligible for Exchange",
        },
    )
    refundable_fares: str = field(
        default=None,
        metadata={
            "name": "RefundableFares",
            "type": "Attribute",
            "help": "Fares eligible for refund: All, Some, None",
        },
    )
    passed_automation_checks: bool = field(
        default=None,
        metadata={
            "name": "PassedAutomationChecks",
            "type": "Attribute",
            "help": "Indicates whether the itinerary passed initial validation for automated exchange",
        },
    )


@dataclass
class ExpertSolution:
    """
    Information about Expert Solution Route component retrieved from Knowledge Base
    """

    leg_price: List[LegPrice] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "LegPrice",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    total_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
            "help": "The Total Price for the Solution.",
        },
    )
    approximate_total_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
            "help": "The Converted Total Price in Agency's Default Currency Value",
        },
    )
    created_date: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "CreatedDate",
            "type": "Attribute",
            "help": "The Date on which this solution was created",
        },
    )


@dataclass
class Facility:
    """
    The facility definition for a part of a row or a seat map
    """

    characteristic: List[Characteristic] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Characteristic",
            "type": "Element",
        },
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
    passenger_seat_price: List[PassengerSeatPrice] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "PassengerSeatPrice",
            "type": "Element",
        },
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
            "help": "Tax information related to seat price. This is presently populated for MCH and ACH content. Applicable providers are MCH/ACH",
        },
    )
    emd: Emd = field(default=None, metadata={"name": "EMD", "type": "Element"})
    service_data: List[ServiceData] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ServiceData",
            "type": "Element",
        },
    )
    tour_code: TourCode = field(
        default=None, metadata={"name": "TourCode", "type": "Element"}
    )
    type: TypeFacility = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Attribute",
            "help": "The type of facility",
        },
    )
    seat_code: str = field(
        default=None,
        metadata={
            "name": "SeatCode",
            "type": "Attribute",
            "help": "If a seat type, the seat identifier",
        },
    )
    availability: TypeSeatAvailability = field(
        default=None,
        metadata={
            "name": "Availability",
            "type": "Attribute",
            "help": "If a seat type, the availability of the seat",
        },
    )
    seat_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "SeatPrice",
            "type": "Attribute",
            "help": "The price of the seat, if applicable.",
        },
    )
    paid: bool = field(
        default=None,
        metadata={
            "name": "Paid",
            "type": "Attribute",
            "help": "Set to True if either SeatPrice or GroupSeatPrice are returned.",
        },
    )
    service_sub_code: str = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "help": "The service subcode associated with the Facility",
        },
    )
    ssrcode: TypeSsrcode = field(
        default=None,
        metadata={
            "name": "SSRCode",
            "type": "Attribute",
            "help": "The SSR Code associated with the Facility",
        },
    )
    issuance_reason: str = field(
        default=None,
        metadata={
            "name": "IssuanceReason",
            "type": "Attribute",
            "help": "A one-letter RFIC value filed by the airline in each Optional Service will be mapped to this attribute. RFIC is IATA Reason for Issuance Code. Possible codes are A (Air transportation),B (Surface Transportation),C(Bagage), D(Financial Impact),E(Airport Services),F(Merchandise),G(Inflight Services),I (Individual Airline use).",
        },
    )
    base_seat_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "BaseSeatPrice",
            "type": "Attribute",
            "help": "Price of the seats excluding Taxes.",
        },
    )
    taxes: TypeMoney = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
            "help": "Tax amount for the seat price.",
        },
    )
    quantity: int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
            "help": "The number of units availed for each optional service (e.g. 2 baggage availed will be specified as 2 in quantity for optional service BAGGAGE)",
        },
    )
    sequence_number: int = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Attribute",
            "help": "The sequence number associated with the OptionalService",
        },
    )
    inclusive_of_tax: bool = field(
        default=None,
        metadata={
            "name": "InclusiveOfTax",
            "type": "Attribute",
            "help": "Identifies if the service was filed with a fee that is inclusive of tax.",
        },
    )
    interline_settlement_allowed: bool = field(
        default=None,
        metadata={
            "name": "InterlineSettlementAllowed",
            "type": "Attribute",
            "help": "Identifies if the interline settlement is allowed in service .",
        },
    )
    geography_specification: str = field(
        default=None,
        metadata={
            "name": "GeographySpecification",
            "type": "Attribute",
            "help": "Sector, Portion, Journey.",
        },
    )
    source: str = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "help": "The Source of the optional service. The source can be ACH, MCE, or MCH.",
        },
    )
    optional_service_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "OptionalServiceRef",
            "type": "Attribute",
            "help": "References the OptionalService for the Row/Facility. Providers: ACH, 1G, 1V, 1P, 1J",
        },
    )
    seat_information_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "SeatInformationRef",
            "type": "Attribute",
            "help": "Specifies the seat information for the seat. Providers: ACH, 1G, 1V, 1P, 1J",
        },
    )


@dataclass
class FareDetails:
    """
    Information about this fare component
    """

    fare_ticket_designator: FareTicketDesignator = field(
        default=None,
        metadata={"name": "FareTicketDesignator", "type": "Element"},
    )
    key: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "Key",
            "type": "Attribute",
            "help": "Fare key",
        },
    )
    passenger_detail_ref: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "PassengerDetailRef",
            "type": "Attribute",
            "help": "PassengerRef key",
        },
    )
    fare_basis: TypeFareBasisCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "FareBasis",
            "type": "Attribute",
            "help": "The fare basis code for this fare",
        },
    )


@dataclass
class FareRemarkList:
    """
    The shared object list of FareInfos
    """

    fare_remark: List[FareRemark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "FareRemark",
            "type": "Element",
        },
    )


@dataclass
class FareRestriction:
    """
    Fare Restriction
    """

    fare_restriction_days_of_week: List[FareRestrictionDaysOfWeek] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "FareRestrictionDaysOfWeek",
            "type": "Element",
        },
    )
    fare_restriction_date: List[FareRestrictionDate] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareRestrictionDate",
            "type": "Element",
        },
    )
    fare_restriction_sale_date: FareRestrictionSaleDate = field(
        default=None,
        metadata={"name": "FareRestrictionSaleDate", "type": "Element"},
    )
    fare_restriction_seasonal: List[FareRestrictionSeasonal] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareRestrictionSeasonal",
            "type": "Element",
        },
    )
    fare_restrictiontype: TypeFareRestrictionType = field(
        default=None,
        metadata={"name": "FareRestrictiontype", "type": "Attribute"},
    )


@dataclass
class FareRuleCategoryTypes:
    category_details: List[ValueDetails] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "CategoryDetails",
            "type": "Element",
            "help": "To indicate details of which category is displayed",
        },
    )
    variable_category_details: List[CategoryDetailsType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "VariableCategoryDetails",
            "type": "Element",
            "help": "If the specified category of Structured Fare Rules is of variable lenght",
        },
    )
    value: str = field(
        default=None,
        metadata={"required": True, "name": "Value", "type": "Attribute"},
    )


@dataclass
class FareRulesFilter:
    """
    Fare Rules Filter about this fare component. Applicable Providers are 1P,1J,1G,1V.
    """

    refundability: "FareRulesFilter.Refundability" = field(
        default=None,
        metadata={
            "name": "Refundability",
            "type": "Element",
            "help": "Refundability/Penalty Fare Rules about this fare component.",
        },
    )
    latest_ticketing_time: str = field(
        default=None,
        metadata={
            "name": "LatestTicketingTime",
            "type": "Element",
            "help": "For Future Use",
        },
    )
    chg: Chgtype = field(
        default=None,
        metadata={"name": "CHG", "type": "Element", "help": "For Penalties"},
    )
    min: Mintype = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Element",
            "help": "For Minimum Stay",
        },
    )
    max: Maxtype = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Element",
            "help": "For Maximum Stay",
        },
    )
    adv: Advtype = field(
        default=None,
        metadata={
            "name": "ADV",
            "type": "Element",
            "help": "For Advance Res/Tkt",
        },
    )
    oth: Othtype = field(
        default=None,
        metadata={"name": "OTH", "type": "Element", "help": "Other"},
    )

    @dataclass
    class Refundability:
        value: TypeRefundabilityValue = field(
            default=None,
            metadata={
                "required": True,
                "name": "Value",
                "type": "Attribute",
                "help": "Currently returned: FullyRefundable (1G,1V), RefundableWithPenalty (1G,1V), Refundable (1P,1J), NonRefundable (1G,1V,1P,1J).Refundable.",
            },
        )


@dataclass
class FaxDetails:
    """
    The Fax Details Information
    """

    phone_number: PhoneNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "PhoneNumber",
            "type": "Element",
            "help": "Send type as Fax for fax number.",
        },
    )
    term_conditions: TermConditions = field(
        default=None,
        metadata={
            "name": "TermConditions",
            "type": "Element",
            "help": "Term and Conditions for the fax .",
        },
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
    include_cover_sheet: bool = field(
        default=None,
        metadata={
            "name": "IncludeCoverSheet",
            "type": "Attribute",
            "help": "Specifies whether to include a cover page with fax or not.",
        },
    )
    to: str = field(
        default=None,
        metadata={"name": "To", "type": "Attribute", "help": "To address."},
    )
    from_value: str = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Attribute",
            "help": "From address.",
        },
    )
    dept_billing_code: str = field(
        default=None,
        metadata={
            "name": "DeptBillingCode",
            "type": "Attribute",
            "help": "Department billing code.",
        },
    )
    invoice_number: str = field(
        default=None,
        metadata={
            "name": "InvoiceNumber",
            "type": "Attribute",
            "help": "Invoice number.",
        },
    )


@dataclass
class FlightDetails:
    """
    Specific details within a flight segment.
    """

    connection: Connection = field(
        default=None, metadata={"name": "Connection", "type": "Element"}
    )
    meals: List[Meals] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Meals",
            "type": "Element",
        },
    )
    in_flight_services: List[InFlightServices] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "InFlightServices",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    equipment: TypeEquipment = field(
        default=None, metadata={"name": "Equipment", "type": "Attribute"}
    )
    on_time_performance: int = field(
        default=None,
        metadata={
            "name": "OnTimePerformance",
            "type": "Attribute",
            "help": "Represents flight on time performance as a percentage from 0 to 100",
        },
    )
    origin_terminal: str = field(
        default=None, metadata={"name": "OriginTerminal", "type": "Attribute"}
    )
    destination_terminal: str = field(
        default=None,
        metadata={"name": "DestinationTerminal", "type": "Attribute"},
    )
    ground_time: int = field(
        default=None, metadata={"name": "GroundTime", "type": "Attribute"}
    )
    automated_checkin: bool = field(
        default="false",
        metadata={
            "name": "AutomatedCheckin",
            "type": "Attribute",
            "help": "“True” indicates that the flight allows automated check-in. The default is “False”.",
        },
    )


@dataclass
class FlightInfoDetail:
    codeshare_info: CodeshareInfo = field(
        default=None, metadata={"name": "CodeshareInfo", "type": "Element"}
    )
    meals: List[Meals] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Meals",
            "type": "Element",
        },
    )
    in_flight_services: List[InFlightServices] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "InFlightServices",
            "type": "Element",
        },
    )
    variance: List[Variance] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Variance",
            "type": "Element",
        },
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Origin",
            "type": "Attribute",
            "help": "The IATA location code for this origination of this entity.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Destination",
            "type": "Attribute",
            "help": "The IATA location code for this destination of this entity.",
        },
    )
    scheduled_departure_time: str = field(
        default=None,
        metadata={
            "name": "ScheduledDepartureTime",
            "type": "Attribute",
            "help": "The date and time at which this entity is scheduled to depart. This does not include time zone information since it can be derived from the origin location.",
        },
    )
    scheduled_arrival_time: str = field(
        default=None,
        metadata={
            "name": "ScheduledArrivalTime",
            "type": "Attribute",
            "help": "The date and time at which this entity is scheduled to arrive at the destination. This does not include time zone information since it can be derived from the origin location.",
        },
    )
    travel_time: int = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
            "help": "Total time spent (minutes) traveling including flight time and ground time.",
        },
    )
    eticketability: TypeEticketability = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
            "help": "Identifies if this particular segment is E-Ticketable",
        },
    )
    equipment: TypeEquipment = field(
        default=None, metadata={"name": "Equipment", "type": "Attribute"}
    )
    origin_terminal: str = field(
        default=None, metadata={"name": "OriginTerminal", "type": "Attribute"}
    )
    origin_gate: str = field(
        default=None,
        metadata={
            "name": "OriginGate",
            "type": "Attribute",
            "help": "To be used to display origin flight gate number",
        },
    )
    destination_terminal: str = field(
        default=None,
        metadata={"name": "DestinationTerminal", "type": "Attribute"},
    )
    destination_gate: str = field(
        default=None,
        metadata={
            "name": "DestinationGate",
            "type": "Attribute",
            "help": "To be used to display destination flight gate number",
        },
    )
    automated_checkin: bool = field(
        default="false",
        metadata={
            "name": "AutomatedCheckin",
            "type": "Attribute",
            "help": "“True” indicates that the flight allows automated check-in. The default is “False”.",
        },
    )


@dataclass
class FlightTimeDetail:
    """
    Flight Time Table Response Details
    """

    days_of_operation: TypeDaysOfOperation = field(
        default=None, metadata={"name": "DaysOfOperation", "type": "Element"}
    )
    connection: Connection = field(
        default=None, metadata={"name": "Connection", "type": "Element"}
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    vendor_code: str = field(
        default=None, metadata={"name": "VendorCode", "type": "Attribute"}
    )
    flight_number: TypeFlightNumber = field(
        default=None, metadata={"name": "FlightNumber", "type": "Attribute"}
    )
    origin: TypeAirport = field(
        default=None, metadata={"name": "Origin", "type": "Attribute"}
    )
    destination: TypeAirport = field(
        default=None, metadata={"name": "Destination", "type": "Attribute"}
    )
    departure_time: str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "help": "Flight departure time",
        },
    )
    arrival_time: str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
            "help": "Flight arrival time",
        },
    )
    stop_count: int = field(
        default=None, metadata={"name": "StopCount", "type": "Attribute"}
    )
    equipment: TypeEquipment = field(
        default=None, metadata={"name": "Equipment", "type": "Attribute"}
    )
    schedule_start_date: str = field(
        default=None,
        metadata={
            "name": "ScheduleStartDate",
            "type": "Attribute",
            "help": "Flight time table search start date",
        },
    )
    schedule_end_date: str = field(
        default=None,
        metadata={
            "name": "ScheduleEndDate",
            "type": "Attribute",
            "help": "Flight time table search end date",
        },
    )
    display_option: bool = field(
        default=None,
        metadata={
            "name": "DisplayOption",
            "type": "Attribute",
            "help": "Indicates if carrier has link (carrier specific) display option.",
        },
    )
    on_time_performance: int = field(
        default=None,
        metadata={
            "name": "OnTimePerformance",
            "type": "Attribute",
            "help": "On time performance indicator in percentage.",
        },
    )
    day_change: int = field(
        default=None,
        metadata={
            "name": "DayChange",
            "type": "Attribute",
            "help": "Indicates if flight arrives on same day as departure, previous day, or next day. Like values 00 means Same day , 01 means next day, -1 mean Previous day etc.",
        },
    )
    journey_time: int = field(
        default=None,
        metadata={
            "name": "JourneyTime",
            "type": "Attribute",
            "help": "Indicates total journey time in minutes.",
        },
    )
    flight_time: int = field(
        default=None,
        metadata={
            "name": "FlightTime",
            "type": "Attribute",
            "help": "Indicates total flight time in minutes.",
        },
    )
    start_terminal: str = field(
        default=None,
        metadata={
            "name": "StartTerminal",
            "type": "Attribute",
            "help": "Flight start terminal code.",
        },
    )
    end_terminal: str = field(
        default=None,
        metadata={
            "name": "EndTerminal",
            "type": "Attribute",
            "help": "Flight end terminal code.",
        },
    )
    first_intermediate_stop: TypeIatacode = field(
        default=None,
        metadata={
            "name": "FirstIntermediateStop",
            "type": "Attribute",
            "help": "First intermediate stop after board point.",
        },
    )
    last_intermediate_stop: TypeIatacode = field(
        default=None,
        metadata={
            "name": "LastIntermediateStop",
            "type": "Attribute",
            "help": "Last intermediate stop before off point.",
        },
    )
    inside_availability: str = field(
        default=None,
        metadata={"name": "InsideAvailability", "type": "Attribute"},
    )
    secure_sell: str = field(
        default=None, metadata={"name": "SecureSell", "type": "Attribute"}
    )
    availability_source: TypeAvailabilitySource = field(
        default=None,
        metadata={"name": "AvailabilitySource", "type": "Attribute"},
    )


@dataclass
class FlightTimeTableCriteria:
    """
    Flight Time Table Search Criteria
    """

    general_time_table: GeneralTimeTable = field(
        default=None,
        metadata={
            "required": True,
            "name": "GeneralTimeTable",
            "type": "Element",
        },
    )
    specific_time_table: SpecificTimeTable = field(
        default=None,
        metadata={
            "required": True,
            "name": "SpecificTimeTable",
            "type": "Element",
        },
    )


@dataclass
class Option:
    """
    List of segment and fare available for the search air leg.
    """

    booking_info: List[BookingInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BookingInfo",
            "type": "Element",
        },
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Connection",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    travel_time: str = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
            "help": "Total traveling time that is difference between the departure time of the first segment and the arrival time of the last segments for that particular entire set of connection.",
        },
    )


@dataclass
class PassengerType(TypePassengerType):
    """
    The passenger type details associated to a fare.
    """

    fare_guarantee_info: FareGuaranteeInfo = field(
        default=None, metadata={"name": "FareGuaranteeInfo", "type": "Element"}
    )


@dataclass
class PrePayAccount:
    """
    PrePay Account associated with the customer
    """

    credit_summary: CreditSummary = field(
        default=None, metadata={"name": "CreditSummary", "type": "Element"}
    )
    pre_pay_price_info: PrePayPriceInfo = field(
        default=None, metadata={"name": "PrePayPriceInfo", "type": "Element"}
    )
    program_title: str = field(
        default=None,
        metadata={
            "name": "ProgramTitle",
            "type": "Attribute",
            "help": "Pre pay program title",
        },
    )
    certificate_number: str = field(
        default=None,
        metadata={"name": "CertificateNumber", "type": "Attribute"},
    )
    program_name: str = field(
        default=None,
        metadata={
            "name": "ProgramName",
            "type": "Attribute",
            "help": "Pre pay program name",
        },
    )
    effective_date: str = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "help": "Effective date for the pre pay account",
        },
    )
    expire_date: str = field(
        default=None,
        metadata={
            "name": "ExpireDate",
            "type": "Attribute",
            "help": "Expiry date for the pre pay account",
        },
    )


@dataclass
class PrePayCustomer:
    """
    Detailed customer information for searching pre pay profiles
    """

    person_name: PersonName = field(
        default=None, metadata={"name": "PersonName", "type": "Element"}
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Email",
            "type": "Element",
            "help": "Customer email detail",
        },
    )
    address: List[TypeStructuredAddress] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Address",
            "type": "Element",
            "help": "Customer address detail",
        },
    )
    related_traveler: List[RelatedTraveler] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RelatedTraveler",
            "type": "Element",
            "help": "Travelers related to this pre pay id",
        },
    )
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "LoyaltyCard",
            "type": "Element",
            "help": "Customer loyalty card detail",
        },
    )


@dataclass
class RepricingModifiers:
    """
    Used for rapid reprice to provide additional options for the reprice. Providers: 1G/1V/1P/1S/1A
    """

    fare_type: List[FareType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 100,
            "name": "FareType",
            "type": "Element",
        },
    )
    fare_ticket_designator: FareTicketDesignator = field(
        default=None,
        metadata={"name": "FareTicketDesignator", "type": "Element"},
    )
    override_currency: "RepricingModifiers.OverrideCurrency" = field(
        default=None, metadata={"name": "OverrideCurrency", "type": "Element"}
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
        },
    )
    price_class_of_service: TypePriceClassOfService = field(
        default=None,
        metadata={
            "name": "PriceClassOfService",
            "type": "Attribute",
            "help": "Values allowed are ClassBooked or LowestClass. This tells how to price the new itinerary.",
        },
    )
    create_date: str = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
            "help": "This is either today’s date or the date the repriced itinerary was created",
        },
    )
    reissue_loc_city_code: TypeCity = field(
        default=None,
        metadata={
            "name": "ReissueLocCityCode",
            "type": "Attribute",
            "help": "This is the city code of the reissue location",
        },
    )
    reissue_loc_country_code: TypeCountry = field(
        default=None,
        metadata={
            "name": "ReissueLocCountryCode",
            "type": "Attribute",
            "help": "This is the country code of the reissue location",
        },
    )
    bulk_ticket: bool = field(
        default="false",
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
            "help": "Set to true and the itinerary is/will be a bulk ticket. Set to false and the itinerary being repriced will not be a bulk ticket.",
        },
    )
    account_code: str = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
            "help": "May be used in conjunction with PrivateFareOptions",
        },
    )
    penalty_as_tax_code: str = field(
        default=None,
        metadata={
            "name": "PenaltyAsTaxCode",
            "type": "Attribute",
            "help": "Used to request that the penalty be applied as a tax, to the tax code specified. Providers supported 1G/1P",
        },
    )
    air_pricing_solution_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "AirPricingSolutionRef",
            "type": "Attribute",
            "help": "A reference to a AirPricingSolution. Providers: 1G, 1V, 1P, 1J.",
        },
    )
    penalty_to_fare: bool = field(
        default=None,
        metadata={
            "name": "PenaltyToFare",
            "type": "Attribute",
            "help": "Will add the change fee/penalty amount to the total fare amount. Supported Providers: 1P",
        },
    )
    price_ptconly: bool = field(
        default="false",
        metadata={
            "name": "PricePTCOnly",
            "type": "Attribute",
            "help": "A value of true forces the price for the PTC even if that fare is not the lowest fare for the passenger.",
        },
    )
    brand_details: bool = field(
        default="false",
        metadata={
            "name": "BrandDetails",
            "type": "Attribute",
            "help": "Set to true full brand details will be returned.",
        },
    )
    brand_modifier: str = field(
        default=None,
        metadata={
            "name": "BrandModifier",
            "type": "Attribute",
            "help": "A value of MaintainBrand will maintain the brand from the original ticket if applicable.",
        },
    )
    jet_service_only: bool = field(
        default="false",
        metadata={
            "name": "JetServiceOnly",
            "type": "Attribute",
            "help": "Request flights that are jet service only. Available in AirExchangeMultiQuoteReq only.",
        },
    )
    time_window: int = field(
        default=None,
        metadata={
            "name": "TimeWindow",
            "type": "Attribute",
            "help": "A value of Time Window is optional. Available in AirExchangeMultiQuoteReq only.",
        },
    )
    flight_type: str = field(
        default="Direct",
        metadata={
            "name": "FlightType",
            "type": "Attribute",
            "help": "Type of flights to be returned. Values are 'NonStop', 'Direct', 'SingleConnection' and 'NoRestrictions'. Available in AirExchangeMultiQuoteReq only.",
        },
    )
    multi_airport_search: bool = field(
        default="true",
        metadata={
            "name": "MultiAirportSearch",
            "type": "Attribute",
            "help": "A value of Multi Airport Search Indicator is optional. Available in AirExchangeMultiQuoteReq only.",
        },
    )
    connection_point: TypeIatacode = field(
        default=None,
        metadata={
            "name": "ConnectionPoint",
            "type": "Attribute",
            "help": "A value of Connection City Code is optional. Available in AirExchangeMultiQuoteReq only.",
        },
    )

    @dataclass
    class OverrideCurrency:
        currency_code: TypeCurrency = field(
            default=None,
            metadata={"name": "CurrencyCode", "type": "Attribute"},
        )
        country_code: TypeCountry = field(
            default=None, metadata={"name": "CountryCode", "type": "Attribute"}
        )


@dataclass
class Route:
    """
    Information about this Route component
    """

    leg: List[Leg] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "Leg",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )


@dataclass
class RuleLengthOfStay:
    """
    Container for rules providing minimum and maximum stay requirements.
    """

    minimum_stay: TypeRestrictionLengthOfStay = field(
        default=None, metadata={"name": "MinimumStay", "type": "Element"}
    )
    maximum_stay: TypeRestrictionLengthOfStay = field(
        default=None, metadata={"name": "MaximumStay", "type": "Element"}
    )


@dataclass
class ServiceAssociations:
    applicable_segment: List["ServiceAssociations.ApplicableSegment"] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "ApplicableSegment",
            "type": "Element",
            "help": "Applicable air segment associated with this brand.",
        },
    )

    @dataclass
    class ApplicableSegment:
        response_message: ResponseMessage = field(
            default=None,
            metadata={"name": "ResponseMessage", "type": "Element"},
        )
        optional_service_ref: OptionalServiceRef = field(
            default=None,
            metadata={"name": "OptionalServiceRef", "type": "Element"},
        )
        key: TypeRef = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "help": "Applicable air segment key",
            },
        )


@dataclass
class TypeDefaultBrandDetail:
    text: List[Text] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 4,
            "name": "Text",
            "type": "Element",
            "help": "Text associated to the brand",
        },
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "ImageLocation",
            "type": "Element",
            "help": "Images associated to the brand",
        },
    )
    applicable_segment: List[ApplicableSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "ApplicableSegment",
            "type": "Element",
            "help": "Defines for which air segment the brand is applicable.",
        },
    )
    brand_id: TypeBrandId = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "help": "The unique identifier of the brand",
        },
    )


@dataclass
class AccountRelatedRules:
    booking_rules: List[BookingRules] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BookingRules",
            "type": "Element",
        },
    )
    routing_rules: RoutingRules = field(
        default=None, metadata={"name": "RoutingRules", "type": "Element"}
    )


@dataclass
class AirPricingCommand:
    """
    A containter to identify individual pricing events. A pricing result will be returned for each pricing command according to its parameters.
    """

    air_pricing_modifiers: AirPricingModifiers = field(
        default=None,
        metadata={"name": "AirPricingModifiers", "type": "Element"},
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
        },
    )
    command_key: str = field(
        default=None,
        metadata={
            "name": "CommandKey",
            "type": "Attribute",
            "help": "An identifier to link the pricing responses to the pricing commands. The value passed here will be returned in the resulting AirPricingInfo(s) from this command.",
        },
    )
    cabin_class: str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "help": "Specify the cabin type to price the entire itinerary in. If segment level cabin selection is required, this attribute should not be used.",
        },
    )


@dataclass
class AlternateRouteList:
    """
    Identifies the alternate routes for the request
    """

    alternate_route: List[AlternateRoute] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AlternateRoute",
            "type": "Element",
        },
    )


@dataclass
class AutoPricingInfo:
    """
    Auto Pricing based on Segment and Traveler Association.
    """

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 100,
            "name": "AirSegmentRef",
            "type": "Element",
        },
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 100,
            "name": "BookingTravelerRef",
            "type": "Element",
        },
    )
    air_pricing_modifiers: AirPricingModifiers = field(
        default=None,
        metadata={"name": "AirPricingModifiers", "type": "Element"},
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 100,
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    pricing_type: str = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Attribute",
            "help": "Indicates the Pricing Type used. The possible values are TicketRecord, StoredFare, PricingInstruction.",
        },
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "help": "The Plating Carrier for this journey",
        },
    )


@dataclass
class BagDetails:
    """
    Information related to Bag details .
    """

    baggage_restriction: List[BaggageRestriction] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BaggageRestriction",
            "type": "Element",
        },
    )
    available_discount: List[AvailableDiscount] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AvailableDiscount",
            "type": "Element",
        },
    )
    applicable_bags: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "ApplicableBags",
            "type": "Attribute",
            "help": "Applicable baggage like Carry-On,1st Check-in,2nd Check -in etc.",
        },
    )
    base_price: TypeMoney = field(
        default=None, metadata={"name": "BasePrice", "type": "Attribute"}
    )
    approximate_base_price: TypeMoney = field(
        default=None,
        metadata={"name": "ApproximateBasePrice", "type": "Attribute"},
    )
    taxes: TypeMoney = field(
        default=None, metadata={"name": "Taxes", "type": "Attribute"}
    )
    total_price: TypeMoney = field(
        default=None, metadata={"name": "TotalPrice", "type": "Attribute"}
    )
    approximate_total_price: TypeMoney = field(
        default=None,
        metadata={"name": "ApproximateTotalPrice", "type": "Attribute"},
    )


@dataclass
class CarryOnAllowanceInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Carry-On allowance like URL, pricing etc
    """

    carry_on_details: List["CarryOnAllowanceInfo.CarryOnDetails"] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "CarryOnDetails",
            "type": "Element",
            "help": "Information related to Carry-On Bag details .",
        },
    )

    @dataclass
    class CarryOnDetails:
        baggage_restriction: List[BaggageRestriction] = field(
            default_factory=list,
            metadata={
                "min_occurs": 0,
                "max_occurs": 99,
                "name": "BaggageRestriction",
                "type": "Element",
            },
        )
        applicable_carry_on_bags: str = field(
            default=None,
            metadata={
                "name": "ApplicableCarryOnBags",
                "type": "Attribute",
                "help": 'Applicable Carry-On baggage "First", "Second", "Third" etc',
            },
        )
        base_price: TypeMoney = field(
            default=None, metadata={"name": "BasePrice", "type": "Attribute"}
        )
        approximate_base_price: TypeMoney = field(
            default=None,
            metadata={"name": "ApproximateBasePrice", "type": "Attribute"},
        )
        taxes: TypeMoney = field(
            default=None, metadata={"name": "Taxes", "type": "Attribute"}
        )
        total_price: TypeMoney = field(
            default=None, metadata={"name": "TotalPrice", "type": "Attribute"}
        )
        approximate_total_price: TypeMoney = field(
            default=None,
            metadata={"name": "ApproximateTotalPrice", "type": "Attribute"},
        )


@dataclass
class DefaultBrandDetail(TypeDefaultBrandDetail):
    """
    Applicable air segment.
    """

    pass


@dataclass
class ExpertSolutionList:
    """
    Identifies the Expert Solutions retrieved from the Knowledge Base.
    """

    expert_solution: List[ExpertSolution] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "ExpertSolution",
            "type": "Element",
        },
    )


@dataclass
class FareDisplayRule:
    """
    Fare Display Rule Container
    """

    rule_advanced_purchase: RuleAdvancedPurchase = field(
        default=None,
        metadata={"name": "RuleAdvancedPurchase", "type": "Element"},
    )
    rule_length_of_stay: RuleLengthOfStay = field(
        default=None, metadata={"name": "RuleLengthOfStay", "type": "Element"}
    )
    rule_charges: RuleCharges = field(
        default=None, metadata={"name": "RuleCharges", "type": "Element"}
    )
    rule_number: str = field(
        default=None, metadata={"name": "RuleNumber", "type": "Attribute"}
    )
    source: str = field(
        default=None, metadata={"name": "Source", "type": "Attribute"}
    )
    tariff_number: str = field(
        default=None, metadata={"name": "TariffNumber", "type": "Attribute"}
    )


@dataclass
class FaxDetailsInformation:
    """
    Container to send Fax details Information for ticketing
    """

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirPricingInfoRef",
            "type": "Element",
            "help": "Returns related air pricing infos.",
        },
    )
    fax_details: FaxDetails = field(
        default=None,
        metadata={"required": True, "name": "FaxDetails", "type": "Element"},
    )


@dataclass
class FlightDetailsList:
    """
    The shared object list of FlightDetails
    """

    flight_details: List[FlightDetails] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "FlightDetails",
            "type": "Element",
        },
    )


@dataclass
class FlightInfo:
    flight_info_detail: List[FlightInfoDetail] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FlightInfoDetail",
            "type": "Element",
        },
    )
    flight_info_error_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FlightInfoErrorMessage",
            "type": "Element",
            "help": "Errors, Warnings and informational messages for the Flight referenced above.",
        },
    )
    criteria_key: TypeRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "CriteriaKey",
            "type": "Attribute",
            "help": "An identifier to link the flightinfo responses to the criteria in request. The value populated here is passed in request.",
        },
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata={
            "required": True,
            "name": "Carrier",
            "type": "Attribute",
            "help": "The carrier that is marketing this segment",
        },
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "FlightNumber",
            "type": "Attribute",
            "help": "The flight number under which the marketing carrier is marketing this flight",
        },
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "help": "The IATA location code for this origination of this entity.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "help": "The IATA location code for this destination of this entity.",
        },
    )
    departure_date: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "DepartureDate",
            "type": "Attribute",
            "help": "The date at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
        },
    )
    class_of_service: TypeClassOfService = field(
        default=None, metadata={"name": "ClassOfService", "type": "Attribute"}
    )


@dataclass
class FlightOption:
    """
    List of Options available for any search air leg.
    """

    option: List[Option] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "Option",
            "type": "Element",
            "help": "List of BookingInfo available for the search air leg.",
        },
    )
    leg_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "LegRef",
            "type": "Attribute",
            "help": "Identifies the Leg Reference for this Flight Option.",
        },
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Origin",
            "type": "Attribute",
            "help": "The IATA location code for this origination of this entity.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Destination",
            "type": "Attribute",
            "help": "The IATA location code for this destination of this entity.",
        },
    )


@dataclass
class MerchandisingAvailabilityDetails:
    """
    Rich Content and Branding for an air segment
    """

    air_itinerary_details: AirItineraryDetails = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirItineraryDetails",
            "type": "Element",
        },
    )
    account_code: AccountCode = field(
        default=None, metadata={"name": "AccountCode", "type": "Element"}
    )


@dataclass
class MerchandisingDetails:
    """
    Rich Content and Branding for a fare brand.
    """

    air_itinerary_details: List[AirItineraryDetails] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 99,
            "name": "AirItineraryDetails",
            "type": "Element",
        },
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 10,
            "name": "AccountCode",
            "type": "Element",
        },
    )


@dataclass
class OptionalService:
    service_data: List[ServiceData] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ServiceData",
            "type": "Element",
        },
    )
    service_info: ServiceInfo = field(
        default=None, metadata={"name": "ServiceInfo", "type": "Element"}
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Remark",
            "type": "Element",
            "help": "Information regarding any specific for this service.",
        },
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
        },
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FeeInfo",
            "type": "Element",
        },
    )
    emd: Emd = field(default=None, metadata={"name": "EMD", "type": "Element"})
    bundled_services: BundledServices = field(
        default=None, metadata={"name": "BundledServices", "type": "Element"}
    )
    additional_info: List[AdditionalInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 16,
            "name": "AdditionalInfo",
            "type": "Element",
        },
    )
    fee_application: FeeApplication = field(
        default=None,
        metadata={
            "name": "FeeApplication",
            "type": "Element",
            "help": "Specifies how the Optional Service fee is to be applied. The choices are Per One Way, Per Round Trip, Per Item (Per Piece), Per Travel, Per Ticket, Per 1 Kilo, Per 5 Kilos. Provider: 1G, 1V, 1P, 1J",
        },
    )
    text: List[Text] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 4,
            "name": "Text",
            "type": "Element",
        },
    )
    price_range: List[PriceRange] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "PriceRange",
            "type": "Element",
        },
    )
    tour_code: TourCode = field(
        default=None, metadata={"name": "TourCode", "type": "Element"}
    )
    branding_info: BrandingInfo = field(
        default=None, metadata={"name": "BrandingInfo", "type": "Element"}
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "Title",
            "type": "Element",
        },
    )
    optional_services_rule_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "OptionalServicesRuleRef",
            "type": "Attribute",
            "help": "UniqueID to associate a rule to the Optional Service",
        },
    )
    type: TypeMerchandisingService = field(
        default=None,
        metadata={
            "required": True,
            "name": "Type",
            "type": "Attribute",
            "help": "Specify the type of service offered (e.g. seats, baggage, etc.)",
        },
    )
    confirmation: str = field(
        default=None,
        metadata={
            "name": "Confirmation",
            "type": "Attribute",
            "help": "Confirmation number provided by the supplier",
        },
    )
    secondary_type: str = field(
        default=None,
        metadata={
            "name": "SecondaryType",
            "type": "Attribute",
            "help": "The secondary option code type required for certain options",
        },
    )
    purchase_window: TypePurchaseWindow = field(
        default=None,
        metadata={
            "name": "PurchaseWindow",
            "type": "Attribute",
            "help": "Describes when the Service is available for confirmation or purchase (e.g. Booking Only, Check-in Only, Anytime, etc.)",
        },
    )
    priority: int = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Attribute",
            "help": "Numeric value that represents the priority order of the Service",
        },
    )
    available: bool = field(
        default=None,
        metadata={
            "name": "Available",
            "type": "Attribute",
            "help": "Boolean to describe whether the Service is available for sale or not",
        },
    )
    entitled: bool = field(
        default=None,
        metadata={
            "name": "Entitled",
            "type": "Attribute",
            "help": "Boolean to describe whether the passenger is entitled for the service without charge or not",
        },
    )
    per_traveler: bool = field(
        default="true",
        metadata={
            "name": "PerTraveler",
            "type": "Attribute",
            "help": "Boolean to describe whether the Amount on the Service is charged per traveler.",
        },
    )
    create_date: str = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
            "help": "Timestamp when this service/offer got created.",
        },
    )
    payment_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "PaymentRef",
            "type": "Attribute",
            "help": "Reference to a payment for merchandising services.",
        },
    )
    service_status: str = field(
        default=None,
        metadata={
            "name": "ServiceStatus",
            "type": "Attribute",
            "help": "Specify the service status (e.g. active, canceled, etc.)",
        },
    )
    quantity: int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
            "help": "The number of units availed for each optional service (e.g. 2 baggage availed will be specified as 2 in quantity for optional service BAGGAGE)",
        },
    )
    sequence_number: int = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Attribute",
            "help": "The sequence number associated with the OptionalService",
        },
    )
    service_sub_code: str = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "help": "The service subcode associated with the OptionalService",
        },
    )
    ssrcode: TypeSsrcode = field(
        default=None,
        metadata={
            "name": "SSRCode",
            "type": "Attribute",
            "help": "The SSR Code associated with the OptionalService",
        },
    )
    issuance_reason: str = field(
        default=None,
        metadata={
            "name": "IssuanceReason",
            "type": "Attribute",
            "help": "A one-letter code specifying the reason for issuance of the OptionalService",
        },
    )
    provider_defined_type: str = field(
        default=None,
        metadata={
            "name": "ProviderDefinedType",
            "type": "Attribute",
            "help": "Original Type as sent by the provider",
        },
    )
    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )
    assess_indicator: TypeAssessIndicator = field(
        default=None,
        metadata={
            "name": "AssessIndicator",
            "type": "Attribute",
            "help": "Indicates whether price is assessed by mileage or currency or both",
        },
    )
    mileage: int = field(
        default=None,
        metadata={
            "name": "Mileage",
            "type": "Attribute",
            "help": "Indicates mileage fee/amount",
        },
    )
    applicable_fflevel: int = field(
        default=None,
        metadata={
            "name": "ApplicableFFLevel",
            "type": "Attribute",
            "help": "Numerical value of the loyalty card level for which this service is available.",
        },
    )
    private: bool = field(
        default=None,
        metadata={
            "name": "Private",
            "type": "Attribute",
            "help": "Describes if service is private or not.",
        },
    )
    ssrfree_text: TypeSsrfreeText = field(
        default=None,
        metadata={
            "name": "SSRFreeText",
            "type": "Attribute",
            "help": "Certain SSR types sent in OptionalService SSRCode require a free text message. For example, PETC Pet in Cabin.",
        },
    )
    is_pricing_approximate: bool = field(
        default=None,
        metadata={
            "name": "IsPricingApproximate",
            "type": "Attribute",
            "help": "When set to True indicates that the pricing returned is approximate. Supported providers are MCH/ACH",
        },
    )
    chargeable: str = field(
        default=None,
        metadata={
            "name": "Chargeable",
            "type": "Attribute",
            "help": "Indicates if the optional service is not offered, is available for a charge, or is included in the brand",
        },
    )
    inclusive_of_tax: bool = field(
        default=None,
        metadata={
            "name": "InclusiveOfTax",
            "type": "Attribute",
            "help": "Identifies if the service was filed with a fee that is inclusive of tax.",
        },
    )
    interline_settlement_allowed: bool = field(
        default=None,
        metadata={
            "name": "InterlineSettlementAllowed",
            "type": "Attribute",
            "help": "Identifies if the interline settlement is allowed in service .",
        },
    )
    geography_specification: str = field(
        default=None,
        metadata={
            "name": "GeographySpecification",
            "type": "Attribute",
            "help": "Sector, Portion, Journey.",
        },
    )
    excess_weight_rate: str = field(
        default=None,
        metadata={
            "name": "ExcessWeightRate",
            "type": "Attribute",
            "help": "The cost of the bag per unit weight.",
        },
    )
    source: str = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "help": "The Source of the optional service. The source can be ACH, MCE, or MCH.",
        },
    )
    viewable_only: bool = field(
        default=None,
        metadata={
            "name": "ViewableOnly",
            "type": "Attribute",
            "help": "Describes if the OptionalService is viewable only or not. If viewable only then the service cannot be sold.",
        },
    )
    display_text: str = field(
        default=None,
        metadata={
            "name": "DisplayText",
            "type": "Attribute",
            "help": "Title of the Optional Service. Provider: ACH",
        },
    )
    weight_in_excess: str = field(
        default=None,
        metadata={
            "name": "WeightInExcess",
            "type": "Attribute",
            "help": "The excess weight of a bag. Providers: 1G, 1V, 1P, 1J",
        },
    )
    total_weight: str = field(
        default=None,
        metadata={
            "name": "TotalWeight",
            "type": "Attribute",
            "help": "The total weight of a bag. Providers: 1G, 1V, 1P, 1J",
        },
    )
    baggage_unit_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "BaggageUnitPrice",
            "type": "Attribute",
            "help": "The per unit price of baggage. Providers: 1G, 1V, 1P, 1J",
        },
    )
    first_piece: int = field(
        default=None,
        metadata={
            "name": "FirstPiece",
            "type": "Attribute",
            "help": "Indicates the minimum occurrence of excess baggage.Provider: 1G, 1V, 1P, 1J.",
        },
    )
    last_piece: int = field(
        default=None,
        metadata={
            "name": "LastPiece",
            "type": "Attribute",
            "help": "Indicates the maximum occurrence of excess baggage. Provider: 1G, 1V, 1P, 1J.",
        },
    )
    restricted: bool = field(
        default="false",
        metadata={
            "name": "Restricted",
            "type": "Attribute",
            "help": "When set to “true”, the Optional Service is restricted by an embargo. Provider: 1G, 1V, 1P, 1J",
        },
    )
    is_reprice_required: bool = field(
        default="false",
        metadata={
            "name": "IsRepriceRequired",
            "type": "Attribute",
            "help": "When set to “true”, the Optional Service must be re-priced. Provider: 1G, 1V, 1P, 1J",
        },
    )
    booked_quantity: str = field(
        default=None,
        metadata={
            "name": "BookedQuantity",
            "type": "Attribute",
            "help": "Indicates the Optional Service quantity already booked. Provider: 1G, 1V, 1P, 1J",
        },
    )
    group: str = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Attribute",
            "help": "Associates Optional Services with the same ServiceSub Code, Air Segment, Passenger, and EMD Associated Item. Provider:1G, 1V, 1P, 1J",
        },
    )
    pseudo_city_code: TypePcc = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "help": "The PCC or SID that booked the Optional Service.",
        },
    )
    tag: str = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Attribute",
            "help": "Optional service group name.",
        },
    )
    display_order: int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
            "help": "Optional service group display order.",
        },
    )


@dataclass
class RouteList:
    """
    Identifies the routes and sub-routes that were requested
    """

    route: List[Route] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "Route",
            "type": "Element",
        },
    )


@dataclass
class Row:
    """
    Identifies the row of in a seat map
    """

    facility: List[Facility] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Facility",
            "type": "Element",
        },
    )
    characteristic: List[Characteristic] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Characteristic",
            "type": "Element",
        },
    )
    number: int = field(
        default=None,
        metadata={"required": True, "name": "Number", "type": "Attribute"},
    )
    search_traveler_ref: TypeRef = field(
        default=None,
        metadata={"name": "SearchTravelerRef", "type": "Attribute"},
    )


@dataclass
class SearchAirLeg:
    """
    Search version of AirLeg used to specify search criteria
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
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SearchDestination",
            "type": "Element",
        },
    )
    air_leg_modifiers: AirLegModifiers = field(
        default=None, metadata={"name": "AirLegModifiers", "type": "Element"}
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
            "help": "Specifies the preferred time within the time range. For 1G, 1V, 1P, 1J, it is supported for AvailabilitySearchReq (TimeRange must also be specified) and not supported for LowFareSearchReq. ACH does not support search by arrival time.",
        },
    )


@dataclass
class SegmentModifiers:
    """
    To be used to modify the ticket modifiers for air segment
    """

    air_segment_ref: AirSegmentRef = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirSegmentRef",
            "type": "Element",
        },
    )
    ticket_validity: TicketValidity = field(
        default=None,
        metadata={
            "name": "TicketValidity",
            "type": "Element",
            "help": "To be used to pass the ticket validity dates",
        },
    )
    baggage_allowance: BaggageAllowance = field(
        default=None, metadata={"name": "BaggageAllowance", "type": "Element"}
    )
    ticket_designator: TypeTicketDesignator = field(
        default=None, metadata={"name": "TicketDesignator", "type": "Element"}
    )


@dataclass
class StructuredFareRulesType:
    fare_rule_category_type: List[FareRuleCategoryTypes] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "FareRuleCategoryType",
            "type": "Element",
            "help": "For FareRulesType element",
        },
    )


@dataclass
class Ticket:
    """
    The ticket that resulted from an air booking
    """

    coupon: List[Coupon] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 4,
            "name": "Coupon",
            "type": "Element",
        },
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 6,
            "name": "TicketEndorsement",
            "type": "Element",
        },
    )
    tour_code: List[TourCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TourCode",
            "type": "Element",
        },
    )
    exchanged_ticket_info: List[ExchangedTicketInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ExchangedTicketInfo",
            "type": "Element",
        },
    )
    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )
    ticket_number: TypeTicketNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "TicketNumber",
            "type": "Attribute",
        },
    )
    ticket_status: TypeTicketStatus = field(
        default=None, metadata={"name": "TicketStatus", "type": "Attribute"}
    )


@dataclass
class TypeBaseAirSegment(Segment):
    sponsored_flt_info: SponsoredFltInfo = field(
        default=None, metadata={"name": "SponsoredFltInfo", "type": "Element"}
    )
    codeshare_info: CodeshareInfo = field(
        default=None, metadata={"name": "CodeshareInfo", "type": "Element"}
    )
    air_avail_info: List[AirAvailInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirAvailInfo",
            "type": "Element",
        },
    )
    flight_details: List[FlightDetails] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FlightDetails",
            "type": "Element",
        },
    )
    flight_details_ref: List[FlightDetailsRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FlightDetailsRef",
            "type": "Element",
        },
    )
    alternate_location_distance_ref: List[
        AlternateLocationDistanceRef
    ] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AlternateLocationDistanceRef",
            "type": "Element",
        },
    )
    connection: Connection = field(
        default=None, metadata={"name": "Connection", "type": "Element"}
    )
    sell_message: List[SellMessage] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SellMessage",
            "type": "Element",
        },
    )
    rail_coach_details: List[RailCoachDetails] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailCoachDetails",
            "type": "Element",
        },
    )
    open_segment: bool = field(
        default=None,
        metadata={
            "name": "OpenSegment",
            "type": "Attribute",
            "help": "Indicates OpenSegment when True",
        },
    )
    group: int = field(
        default=None,
        metadata={
            "required": True,
            "name": "Group",
            "type": "Attribute",
            "help": "The Origin Destination Grouping of this segment.",
        },
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "help": "The carrier that is marketing this segment",
        },
    )
    cabin_class: str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "help": "Specifies Cabin class for a group of class of services. Cabin class is not identified if it is not present.",
        },
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "help": "The flight number under which the marketing carrier is marketing this flight",
        },
    )
    class_of_service: TypeClassOfService = field(
        default=None, metadata={"name": "ClassOfService", "type": "Attribute"}
    )
    eticketability: TypeEticketability = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
            "help": "Identifies if this particular segment is E-Ticketable",
        },
    )
    equipment: TypeEquipment = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Attribute",
            "help": "Identifies the equipment that this segment is operating under.",
        },
    )
    marriage_group: int = field(
        default=None,
        metadata={
            "name": "MarriageGroup",
            "type": "Attribute",
            "help": "Identifies this segment as being a married segment. It is paired with other segments of the same value.",
        },
    )
    number_of_stops: int = field(
        default=None,
        metadata={
            "name": "NumberOfStops",
            "type": "Attribute",
            "help": "Identifies the number of stops for each within the segment.",
        },
    )
    seamless: bool = field(
        default=None,
        metadata={
            "name": "Seamless",
            "type": "Attribute",
            "help": "Identifies that this segment was sold via a direct access channel to the marketing carrier.",
        },
    )
    change_of_plane: bool = field(
        default="false",
        metadata={
            "name": "ChangeOfPlane",
            "type": "Attribute",
            "help": "Indicates the traveler must change planes between flights.",
        },
    )
    guaranteed_payment_carrier: str = field(
        default=None,
        metadata={
            "name": "GuaranteedPaymentCarrier",
            "type": "Attribute",
            "help": "Identifies that this segment has Guaranteed Payment Carrier.",
        },
    )
    host_token_ref: str = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
            "help": "Identifies that this segment has Guaranteed Payment Carrier.",
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
            "help": "Provider reservation reference key.",
        },
    )
    optional_services_indicator: bool = field(
        default=None,
        metadata={
            "name": "OptionalServicesIndicator",
            "type": "Attribute",
            "help": "Indicates true if flight provides optional services.",
        },
    )
    availability_source: TypeAvailabilitySource = field(
        default=None,
        metadata={
            "name": "AvailabilitySource",
            "type": "Attribute",
            "help": "Indicates Availability source of AirSegment.",
        },
    )
    apisrequirements_ref: str = field(
        default=None,
        metadata={
            "name": "APISRequirementsRef",
            "type": "Attribute",
            "help": "Reference to the APIS Requirements for this AirSegment.",
        },
    )
    black_listed: bool = field(
        default=None,
        metadata={
            "name": "BlackListed",
            "type": "Attribute",
            "help": "Indicates blacklisted carriers which are banned from servicing points to, from and within the European Community.",
        },
    )
    operational_status: str = field(
        default=None,
        metadata={
            "name": "OperationalStatus",
            "type": "Attribute",
            "help": "Refers to the flight operational status for the segment. This attribute will only be returned in the AvailabilitySearchRsp and not used/returned in any other request/responses. If this attribute is not returned back in the response, it means the flight is operational and not past scheduled departure.",
        },
    )
    number_in_party: int = field(
        default=None,
        metadata={
            "name": "NumberInParty",
            "type": "Attribute",
            "help": "Number of person traveling in this air segment excluding the number of infants on lap.",
        },
    )
    rail_coach_number: str = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
            "help": "Coach number for which rail seatmap/coachmap is returned.",
        },
    )
    booking_date: str = field(
        default=None,
        metadata={
            "name": "BookingDate",
            "type": "Attribute",
            "help": "Used for rapid reprice. The date the booking was made. Providers: 1G/1V/1P/1S/1A",
        },
    )
    flown_segment: bool = field(
        default="false",
        metadata={
            "name": "FlownSegment",
            "type": "Attribute",
            "help": "Used for rapid reprice. Tells whether or not the air segment has been flown. Providers: 1G/1V/1P/1S/1A",
        },
    )
    schedule_change: bool = field(
        default="false",
        metadata={
            "name": "ScheduleChange",
            "type": "Attribute",
            "help": "Used for rapid reprice. Tells whether or not the air segment had a schedule change by the carrier. This tells rapid reprice that the change in the air segment was involuntary and because of a schedule change, not because the user is changing the segment. Providers: 1G/1V/1P/1S/1A",
        },
    )
    brand_indicator: str = field(
        default=None,
        metadata={
            "name": "BrandIndicator",
            "type": "Attribute",
            "help": "Value “B” specifies that the carrier supports Rich Content and Branding. The Brand Indicator is only returned in the availability search response. Provider: 1G, 1V, 1P, 1J, ACH",
        },
    )


@dataclass
class AirSegment(TypeBaseAirSegment):
    """
    An Air marketable travel segment.
    """

    pass


@dataclass
class BaggageAllowanceInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Baggage allowance like URL,Height,Weight etc.
    """

    bag_details: List[BagDetails] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BagDetails",
            "type": "Element",
        },
    )
    traveler_type: TypePtc = field(
        default=None, metadata={"name": "TravelerType", "type": "Attribute"}
    )
    fare_info_ref: TypeRef = field(
        default=None, metadata={"name": "FareInfoRef", "type": "Attribute"}
    )


@dataclass
class FareDisplay:
    """
    Fare/Tariff Display
    """

    fare_display_rule: FareDisplayRule = field(
        default=None,
        metadata={
            "required": True,
            "name": "FareDisplayRule",
            "type": "Element",
        },
    )
    fare_pricing: List[FarePricing] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "FarePricing",
            "type": "Element",
        },
    )
    fare_restriction: List[FareRestriction] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "FareRestriction",
            "type": "Element",
        },
    )
    fare_routing_information: FareRoutingInformation = field(
        default=None,
        metadata={"name": "FareRoutingInformation", "type": "Element"},
    )
    fare_mileage_information: FareMileageInformation = field(
        default=None,
        metadata={"name": "FareMileageInformation", "type": "Element"},
    )
    air_fare_display_rule_key: AirFareDisplayRuleKey = field(
        default=None,
        metadata={"name": "AirFareDisplayRuleKey", "type": "Element"},
    )
    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BookingCode",
            "type": "Element",
        },
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AccountCode",
            "type": "Element",
        },
    )
    addl_booking_code_information: AddlBookingCodeInformation = field(
        default=None,
        metadata={"name": "AddlBookingCodeInformation", "type": "Element"},
    )
    fare_rule_failure_info: FareRuleFailureInfo = field(
        default=None,
        metadata={
            "name": "FareRuleFailureInfo",
            "type": "Element",
            "help": "Returns fare rule failure info for Non Valid fares.",
        },
    )
    price_change: List[PriceChangeType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "PriceChange",
            "type": "Element",
            "help": "Indicates a price change is found in Fare Control Manager",
        },
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata={"required": True, "name": "Carrier", "type": "Attribute"},
    )
    fare_basis: str = field(
        default=None,
        metadata={"required": True, "name": "FareBasis", "type": "Attribute"},
    )
    amount: TypeMoney = field(
        default=None,
        metadata={"required": True, "name": "Amount", "type": "Attribute"},
    )
    trip_type: TypeFareTripType = field(
        default=None, metadata={"name": "TripType", "type": "Attribute"}
    )
    fare_type_code: TypeFareTypeCode = field(
        default=None, metadata={"name": "FareTypeCode", "type": "Attribute"}
    )
    special_fare: bool = field(
        default=None, metadata={"name": "SpecialFare", "type": "Attribute"}
    )
    instant_purchase: bool = field(
        default=None, metadata={"name": "InstantPurchase", "type": "Attribute"}
    )
    eligibility_restricted: bool = field(
        default=None,
        metadata={"name": "EligibilityRestricted", "type": "Attribute"},
    )
    flight_restricted: bool = field(
        default=None,
        metadata={"name": "FlightRestricted", "type": "Attribute"},
    )
    stopovers_restricted: bool = field(
        default=None,
        metadata={"name": "StopoversRestricted", "type": "Attribute"},
    )
    transfers_restricted: bool = field(
        default=None,
        metadata={"name": "TransfersRestricted", "type": "Attribute"},
    )
    blackouts_exist: bool = field(
        default=None, metadata={"name": "BlackoutsExist", "type": "Attribute"}
    )
    accompanied_travel: bool = field(
        default=None,
        metadata={"name": "AccompaniedTravel", "type": "Attribute"},
    )
    mile_or_route_based_fare: TypeMileOrRouteBasedFare = field(
        default=None,
        metadata={"name": "MileOrRouteBasedFare", "type": "Attribute"},
    )
    global_indicator: TypeAtpcoglobalIndicator = field(
        default=None, metadata={"name": "GlobalIndicator", "type": "Attribute"}
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "help": "Returns the origin airport or city code for which this tariff is applicable.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "help": "Returns the destination airport or city code for which this tariff is applicable.",
        },
    )
    fare_ticketing_code: str = field(
        default=None,
        metadata={
            "name": "FareTicketingCode",
            "type": "Attribute",
            "help": "Returns the ticketing code for which this tariff is applicable.",
        },
    )
    fare_ticketing_designator: TypeTicketDesignator = field(
        default=None,
        metadata={
            "name": "FareTicketingDesignator",
            "type": "Attribute",
            "help": "Returns the ticketing designator for which this tariff is applicable.",
        },
    )


@dataclass
class FareRule:
    """
    Fare Rule Container
    """

    fare_rule_long: List[FareRuleLong] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareRuleLong",
            "type": "Element",
        },
    )
    fare_rule_short: List[FareRuleShort] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareRuleShort",
            "type": "Element",
        },
    )
    rule_advanced_purchase: RuleAdvancedPurchase = field(
        default=None,
        metadata={"name": "RuleAdvancedPurchase", "type": "Element"},
    )
    rule_length_of_stay: RuleLengthOfStay = field(
        default=None, metadata={"name": "RuleLengthOfStay", "type": "Element"}
    )
    rule_charges: RuleCharges = field(
        default=None, metadata={"name": "RuleCharges", "type": "Element"}
    )
    fare_rule_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareRuleResultMessage",
            "type": "Element",
        },
    )
    structured_fare_rules: StructuredFareRulesType = field(
        default=None,
        metadata={"name": "StructuredFareRules", "type": "Element"},
    )
    fare_info_ref: str = field(
        default=None, metadata={"name": "FareInfoRef", "type": "Attribute"}
    )
    rule_number: str = field(
        default=None, metadata={"name": "RuleNumber", "type": "Attribute"}
    )
    source: str = field(
        default=None, metadata={"name": "Source", "type": "Attribute"}
    )
    tariff_number: str = field(
        default=None, metadata={"name": "TariffNumber", "type": "Attribute"}
    )


@dataclass
class FlightOptionsList:
    """
    List of Flight Options for the itinerary.
    """

    flight_option: List[FlightOption] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FlightOption",
            "type": "Element",
        },
    )


@dataclass
class OptionalServices:
    """
    A wrapper for all the information regarding each of the Optional services
    """

    optional_services_total: "OptionalServices.OptionalServicesTotal" = field(
        default=None,
        metadata={
            "name": "OptionalServicesTotal",
            "type": "Element",
            "help": "The total fares, fees and taxes associated with the Optional Services",
        },
    )
    optional_service: List[OptionalService] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "OptionalService",
            "type": "Element",
        },
    )
    grouped_option_info: List[GroupedOptionInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "GroupedOptionInfo",
            "type": "Element",
            "help": 'Details about an unselected or "other" option when optional services are grouped together.',
        },
    )
    optional_service_rules: List[ServiceRuleType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "OptionalServiceRules",
            "type": "Element",
            "help": "Holds the rules for selecting the optional service in the itinerary",
        },
    )

    @dataclass
    class OptionalServicesTotal:
        tax_info: List[TaxInfo] = field(
            default_factory=list,
            metadata={
                "min_occurs": 0,
                "max_occurs": 999,
                "name": "TaxInfo",
                "type": "Element",
            },
        )
        fee_info: List[FeeInfo] = field(
            default_factory=list,
            metadata={
                "min_occurs": 0,
                "max_occurs": 999,
                "name": "FeeInfo",
                "type": "Element",
            },
        )


@dataclass
class PrePayProfileInfo:
    """
    PrePay Profile associated with the customer
    """

    pre_pay_id: PrePayId = field(
        default=None,
        metadata={
            "required": True,
            "name": "PrePayId",
            "type": "Element",
            "help": "Pre pay unique identifier detail.This information block is returned both in list and detail retrieve transactions.Example flight pass number",
        },
    )
    pre_pay_customer: PrePayCustomer = field(
        default=None,
        metadata={
            "name": "PrePayCustomer",
            "type": "Element",
            "help": "Pre pay customer detail.This information block is returned both in list and detail retrieve transactions.",
        },
    )
    pre_pay_account: PrePayAccount = field(
        default=None,
        metadata={
            "name": "PrePayAccount",
            "type": "Element",
            "help": "Pre pay account detail.This information block is returned both in list and detail retrieve transactions.",
        },
    )
    affiliations: Affiliations = field(
        default=None,
        metadata={
            "name": "Affiliations",
            "type": "Element",
            "help": "Pre pay affiliations detail.This information block is returned only in detail retrieve transactions.",
        },
    )
    account_related_rules: AccountRelatedRules = field(
        default=None,
        metadata={
            "name": "AccountRelatedRules",
            "type": "Element",
            "help": "Pre pay account related rules.This information block is returned only in detail retrieve transactions.",
        },
    )
    status_code: str = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Attribute",
            "help": "Customer pre pay profile status code(One of Marked for deletion,Lapsed,Terminated,Active,Inactive)",
        },
    )
    creator_id: TypeCardNumber = field(
        default=None,
        metadata={
            "name": "CreatorID",
            "type": "Attribute",
            "help": "This is the loyalty card number of the person who originally purchased/setup the flight pass",
        },
    )


@dataclass
class Rows:
    """
    A wrapper for all the information regarding each of the rows. Providers: ACH, 1G, 1V, 1P, 1J
    """

    row: List[Row] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Row",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH,MCH.",
        },
    )
    segment_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
            "help": "Specifies the AirSegment the seat map is for. Providers: ACH, 1G, 1V, 1P, 1J",
        },
    )


@dataclass
class TicketingModifiers:
    """
    A container to identify individual ticketing modifiers.
    """

    booking_traveler_ref: List[TypeRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BookingTravelerRef",
            "type": "Element",
            "help": "Reference to a booking traveler for which ticketing modifier is applied.",
        },
    )
    net_remit: TypeTicketModifierAmountType = field(
        default=None,
        metadata={
            "name": "NetRemit",
            "type": "Element",
            "help": "Allows an agency to override the net remittance amount - varies by BSP agreement",
        },
    )
    net_fare: TypeTicketModifierAmountType = field(
        default=None,
        metadata={
            "name": "NetFare",
            "type": "Element",
            "help": "Net Fare amount for a ticketed fare",
        },
    )
    actual_selling_fare: TypeTicketModifierAmountType = field(
        default=None,
        metadata={
            "name": "ActualSellingFare",
            "type": "Element",
            "help": "Allows an agency to report an Actual Selling Fare as part of the net remittance BSP agreement",
        },
    )
    invoice_fare: TypeTicketModifierAccountingType = field(
        default=None,
        metadata={
            "name": "InvoiceFare",
            "type": "Element",
            "help": "Allows an agency to report an Invoice Fare as part of the net remittance BSP agreement",
        },
    )
    corporate_discount: TypeTicketModifierAccountingType = field(
        default=None,
        metadata={
            "name": "CorporateDiscount",
            "type": "Element",
            "help": "Allows an agency to add a corporate discount to the itinerary to be ticketed",
        },
    )
    accounting_info: TypeTicketModifierAccountingType = field(
        default=None,
        metadata={
            "name": "AccountingInfo",
            "type": "Element",
            "help": "Allows an agency to report Accounting Information as part of the net remittance BSP agreement",
        },
    )
    bulk_ticket: "TicketingModifiers.BulkTicket" = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Element",
            "help": "Allows an agency to update the fare as a Bulk ticket - Optional SuppressOnFareCalc attribute will control how fare calculation is printed on the ticket",
        },
    )
    group_tour: TypeBulkTicketModifierType = field(
        default=None,
        metadata={
            "name": "GroupTour",
            "type": "Element",
            "help": "Allows an agency to update the fare as a Group Tour (inclusive tour) ticket - Optional SuppressOnFareCalc attribute will control how fare calculation is printed on the ticket",
        },
    )
    commission: Commission = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "help": "Allows an agency to update the commission to a new or different commission rate which will be applied at time of ticketing. The commission Modifier allows the user specify how the commission change is to applied",
        },
    )
    tour_code: TourCode = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Element",
            "help": "Allows an agency to modify the tour code information on the ticket",
        },
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "TicketEndorsement",
            "type": "Element",
            "help": "Allows an agency to add user defined ticketing endorsements the ticket",
        },
    )
    value_modifier: TypeTicketModifierValueType = field(
        default=None,
        metadata={
            "name": "ValueModifier",
            "type": "Element",
            "help": "Allows an agency to modify value or commission of the ticket. The modifier is generic and depends on the specific GDS and BSP implementation",
        },
    )
    document_select: DocumentSelect = field(
        default=None, metadata={"name": "DocumentSelect", "type": "Element"}
    )
    document_options: DocumentOptions = field(
        default=None, metadata={"name": "DocumentOptions", "type": "Element"}
    )
    segment_select: SegmentSelect = field(
        default=None, metadata={"name": "SegmentSelect", "type": "Element"}
    )
    segment_modifiers: List[SegmentModifiers] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SegmentModifiers",
            "type": "Element",
        },
    )
    supplier_locator: SupplierLocator = field(
        default=None, metadata={"name": "SupplierLocator", "type": "Element"}
    )
    destination_purpose_code: DestinationPurposeCode = field(
        default=None,
        metadata={"name": "DestinationPurposeCode", "type": "Element"},
    )
    language_option: List[LanguageOption] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "LanguageOption",
            "type": "Element",
        },
    )
    land_charges: LandCharges = field(
        default=None, metadata={"name": "LandCharges", "type": "Element"}
    )
    print_blank_form_itinerary: PrintBlankFormItinerary = field(
        default=None,
        metadata={"name": "PrintBlankFormItinerary", "type": "Element"},
    )
    exclude_ticketing: ExcludeTicketing = field(
        default=None, metadata={"name": "ExcludeTicketing", "type": "Element"}
    )
    exempt_obfee: ExemptObfee = field(
        default=None, metadata={"name": "ExemptOBFee", "type": "Element"}
    )
    is_primary_di: bool = field(
        default="false",
        metadata={
            "name": "IsPrimaryDI",
            "type": "Attribute",
            "help": "Indicates if the DI is Primary DI. 1P only",
        },
    )
    document_instruction_number: str = field(
        default=None,
        metadata={
            "name": "DocumentInstructionNumber",
            "type": "Attribute",
            "help": "The Document Instruction line number. 1P only",
        },
    )
    reference: StringLength1to30 = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Attribute",
            "help": "Identifies if TicketingModifiers contains DI line information. 1P only.",
        },
    )
    status: str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "help": "DI line status - ex:Ticketed",
        },
    )
    free_text: str = field(
        default=None,
        metadata={
            "name": "FreeText",
            "type": "Attribute",
            "help": "DI line information shown as free text as in Host. 1P only",
        },
    )
    name_number: str = field(
        default=None,
        metadata={
            "name": "NameNumber",
            "type": "Attribute",
            "help": "Host Name Number",
        },
    )
    ticket_record: str = field(
        default=None,
        metadata={
            "name": "TicketRecord",
            "type": "Attribute",
            "help": "Ticket Record Number",
        },
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "help": "Allows an agency to specify the Plating Carrier for ticketing",
        },
    )
    exempt_vat: bool = field(
        default=None,
        metadata={
            "name": "ExemptVAT",
            "type": "Attribute",
            "help": "Allows an agency to update if VAT is Exemtped on the fare.",
        },
    )
    net_remit_applied: bool = field(
        default=None,
        metadata={
            "name": "NetRemitApplied",
            "type": "Attribute",
            "help": "Indicator to the BSP net remittance scheme applies to ticketed fare.",
        },
    )
    free_ticket: bool = field(
        default=None,
        metadata={
            "name": "FreeTicket",
            "type": "Attribute",
            "help": "Indicates free ticket.",
        },
    )
    currency_override_code: str = field(
        default=None,
        metadata={
            "name": "CurrencyOverrideCode",
            "type": "Attribute",
            "help": "This modifier allows an agency to specify the currency like L for Local, E for Euro, U for USD, C for CAD (Canadian dollars).",
        },
    )
    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )

    @dataclass
    class BulkTicket(TypeBulkTicketModifierType):
        non_refundable: bool = field(
            default=None,
            metadata={
                "name": "NonRefundable",
                "type": "Attribute",
                "help": "Indicates bulk ticket being non-refundable",
            },
        )


@dataclass
class AirItinerary:
    """
    A container for an Air only travel itinerary.
    """

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirSegment",
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
    apisrequirements: List[Apisrequirements] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "APISRequirements",
            "type": "Element",
        },
    )


@dataclass
class AirPricingTicketingModifiers:
    """
    AirPricing TicketingModifier information - used to associate Ticketing Modifiers with one or more AirPricingInfos/ProviderReservationInfo
    """

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingInfoRef",
            "type": "Element",
        },
    )
    ticketing_modifiers: TicketingModifiers = field(
        default=None,
        metadata={
            "required": True,
            "name": "TicketingModifiers",
            "type": "Element",
        },
    )


@dataclass
class AirSegmentError:
    """
    Container to return error messages corresponding to AirSegment
    """

    air_segment: AirSegment = field(
        default=None,
        metadata={"required": True, "name": "AirSegment", "type": "Element"},
    )
    error_message: str = field(
        default=None,
        metadata={"required": True, "name": "ErrorMessage", "type": "Element"},
    )


@dataclass
class AirSegmentList:
    """
    The shared object list of AirSegments
    """

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirSegment",
            "type": "Element",
        },
    )


@dataclass
class AirSolution:
    """
    Defines an air solution that is comprised of an itinerary (the segments) along with the passengers.
    """

    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "SearchTraveler",
            "type": "Element",
        },
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 16,
            "name": "AirSegment",
            "type": "Element",
        },
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 16,
            "name": "HostToken",
            "type": "Element",
        },
    )
    fare_basis: List[FareBasis] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 16,
            "name": "FareBasis",
            "type": "Element",
        },
    )


@dataclass
class BaggageAllowances:
    """
    Details of Baggage allowance
    """

    baggage_allowance_info: List[BaggageAllowanceInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "BaggageAllowanceInfo",
            "type": "Element",
        },
    )
    carry_on_allowance_info: List[CarryOnAllowanceInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "CarryOnAllowanceInfo",
            "type": "Element",
        },
    )
    embargo_info: List[EmbargoInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "EmbargoInfo",
            "type": "Element",
        },
    )


@dataclass
class Brand:
    """
    Commercially recognized product offered by an airline
    """

    title: List[Title] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "Title",
            "type": "Element",
            "help": "The additional titles associated to the brand",
        },
    )
    text: List[Text] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "Text",
            "type": "Element",
            "help": "Text associated to the brand",
        },
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 3,
            "name": "ImageLocation",
            "type": "Element",
            "help": "Images associated to the brand",
        },
    )
    optional_services: OptionalServices = field(
        default=None, metadata={"name": "OptionalServices", "type": "Element"}
    )
    rules: List[Rules] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "Rules",
            "type": "Element",
            "help": "Brand rules",
        },
    )
    service_associations: ServiceAssociations = field(
        default=None,
        metadata={
            "name": "ServiceAssociations",
            "type": "Element",
            "help": "Service associated with this brand",
        },
    )
    upsell_brand: UpsellBrand = field(
        default=None,
        metadata={
            "name": "UpsellBrand",
            "type": "Element",
            "help": "The unique identifier of the Upsell brand",
        },
    )
    applicable_segment: List[TypeApplicableSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "ApplicableSegment",
            "type": "Element",
        },
    )
    default_brand_detail: List[DefaultBrandDetail] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "DefaultBrandDetail",
            "type": "Element",
            "help": "Default brand details.",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"name": "Key", "type": "Attribute", "help": "Brand Key"},
    )
    brand_id: TypeBrandId = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "help": "The unique identifier of the brand",
        },
    )
    name: str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "help": "The Title of the brand",
        },
    )
    air_itinerary_details_ref: TypeRef = field(
        default=None,
        metadata={
            "name": "AirItineraryDetailsRef",
            "type": "Attribute",
            "help": "AirItinerary associated with this brand",
        },
    )
    up_sell_brand_id: TypeBrandId = field(
        default=None, metadata={"name": "UpSellBrandID", "type": "Attribute"}
    )
    brand_found: bool = field(
        default=None,
        metadata={
            "name": "BrandFound",
            "type": "Attribute",
            "help": "Indicates whether brand for the fare was found for carrier or not",
        },
    )
    up_sell_brand_found: bool = field(
        default=None,
        metadata={
            "name": "UpSellBrandFound",
            "type": "Attribute",
            "help": "Indicates whether upsell brand for the fare was found for carrier or not",
        },
    )
    branded_details_available: bool = field(
        default=None,
        metadata={
            "name": "BrandedDetailsAvailable",
            "type": "Attribute",
            "help": "Indicates if full details of the brand is available",
        },
    )
    carrier: TypeCarrier = field(
        default=None, metadata={"name": "Carrier", "type": "Attribute"}
    )
    brand_tier: StringLength1to10 = field(
        default=None,
        metadata={
            "name": "BrandTier",
            "type": "Attribute",
            "help": "Modifier to price by specific brand tier number.",
        },
    )
    brand_maintained: StringLength1to99 = field(
        default=None,
        metadata={
            "name": "BrandMaintained",
            "type": "Attribute",
            "help": "Indicates whether the brand was maintained from the original ticket.",
        },
    )


@dataclass
class ExchangeAirSegment:
    """
    A container to define segment and cabin class in order to process an exchange
    """

    air_segment: AirSegment = field(
        default=None,
        metadata={"required": True, "name": "AirSegment", "type": "Element"},
    )
    cabin_class: CabinClass = field(
        default=None,
        metadata={"required": True, "name": "CabinClass", "type": "Element"},
    )
    fare_basis_code: str = field(
        default=None,
        metadata={
            "name": "FareBasisCode",
            "type": "Attribute",
            "help": "The fare basis code to be used for exchange of this segment.",
        },
    )


@dataclass
class JourneyData:
    """
    Performs journey aware air availability
    """

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 99,
            "name": "AirSegment",
            "type": "Element",
        },
    )


@dataclass
class TcrrefundBundle:
    """
    Used both in request and response
    """

    air_refund_info: AirRefundInfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirRefundInfo",
            "type": "Element",
        },
    )
    waiver_code: WaiverCode = field(
        default=None, metadata={"name": "WaiverCode", "type": "Element"}
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegment",
            "type": "Element",
        },
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FeeInfo",
            "type": "Element",
        },
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
            "help": "Itinerary level taxes",
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
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "TCRNumber",
            "type": "Attribute",
            "help": "The identifying number for a Ticketless Air Reservation.",
        },
    )
    refund_type: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "RefundType",
            "type": "Attribute",
            "help": "Specifies whether this bundle was auto or manually generated",
        },
    )
    refund_access_code: RefundAccessCode = field(
        default=None,
        metadata={"name": "RefundAccessCode", "type": "Attribute"},
    )


@dataclass
class AirSegmentData:
    """
    The shared object list of AirsegmentData
    """

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentRef",
            "type": "Element",
        },
    )
    baggage_allowance: List[BaggageAllowance] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BaggageAllowance",
            "type": "Element",
        },
    )
    brand: List[Brand] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "Brand",
            "type": "Element",
        },
    )
    cabin_class: str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "help": "Specifies Cabin class for a group of class of services. Cabin class is not identified if it is not present.",
        },
    )
    class_of_service: TypeClassOfService = field(
        default=None, metadata={"name": "ClassOfService", "type": "Attribute"}
    )


@dataclass
class AirSegmentSellFailureInfo:
    """
    Container to return air segment sell failures.
    """

    air_segment_error: List[AirSegmentError] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirSegmentError",
            "type": "Element",
        },
    )


@dataclass
class AvailabilityErrorInfo(TypeErrorInfo):
    air_segment_error: List[AirSegmentError] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirSegmentError",
            "type": "Element",
        },
    )


@dataclass
class FareInfo:
    """
    Information about this fare component
    """

    fare_ticket_designator: List[FareTicketDesignator] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareTicketDesignator",
            "type": "Element",
        },
    )
    fare_surcharge: List[FareSurcharge] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareSurcharge",
            "type": "Element",
        },
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AccountCode",
            "type": "Element",
        },
    )
    contract_code: List[ContractCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ContractCode",
            "type": "Element",
        },
    )
    endorsement: List[Endorsement] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Endorsement",
            "type": "Element",
        },
    )
    baggage_allowance: BaggageAllowance = field(
        default=None, metadata={"name": "BaggageAllowance", "type": "Element"}
    )
    fare_rule_key: FareRuleKey = field(
        default=None, metadata={"name": "FareRuleKey", "type": "Element"}
    )
    fare_rule_failure_info: FareRuleFailureInfo = field(
        default=None,
        metadata={"name": "FareRuleFailureInfo", "type": "Element"},
    )
    fare_remark_ref: List[FareRemarkRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareRemarkRef",
            "type": "Element",
        },
    )
    brand: Brand = field(
        default=None, metadata={"name": "Brand", "type": "Element"}
    )
    commission: Commission = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "help": "Specifies the Commission for Agency for a particular Fare component. Apllicable Providers are 1G and 1V.",
        },
    )
    fare_attributes: str = field(
        default=None,
        metadata={
            "name": "FareAttributes",
            "type": "Element",
            "help": "Returns all fare attributes separated by pipe ‘|’. Attribute information is returned by comma separated values for each attribute. These information include attribute number, chargeable indicator and supplementary info. Attribute numbers: 1 - Checked Bag, 2 - Carry On, 3 - Rebooking, 4 - Refund, 5 - Seats, 6 - Meals, 7 - WiFi. Chargeable Indicator: Y - Chargeable, N - Not Chargeable. Supplementary Information that will be returned is : For 1 and 2 - Baggage weights. For 3 – Changeable Info. For 4 – Refundable Info. For 5 - Seat description. For 6 – Meal description. For 7 – WiFi description. Example: 1,Y,23|1,N,50|2,N,8|3,N,CHANGEABLE|4,Y,REFUNDABLE|5,N,SEATING|5,N,MIDDLE|6,Y,SOFT DRINK|6,N,ALCOHOLIC DRINK|6,Y,SNACK|7,X,WIFI",
        },
    )
    change_penalty: TypeFarePenalty = field(
        default=None,
        metadata={
            "name": "ChangePenalty",
            "type": "Element",
            "help": "The penalty (if any) to change the itinerary",
        },
    )
    cancel_penalty: TypeFarePenalty = field(
        default=None,
        metadata={
            "name": "CancelPenalty",
            "type": "Element",
            "help": "The penalty (if any) to cancel the fare",
        },
    )
    fare_rules_filter: FareRulesFilter = field(
        default=None, metadata={"name": "FareRulesFilter", "type": "Element"}
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    fare_basis: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "FareBasis",
            "type": "Attribute",
            "help": "The fare basis code for this fare",
        },
    )
    passenger_type_code: TypePtc = field(
        default=None,
        metadata={
            "required": True,
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "help": "The PTC that is associated with this fare.",
        },
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Origin",
            "type": "Attribute",
            "help": "Returns the airport or city code that defines the origin market for this fare.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
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
            "help": "Returns the date on which this fare was quoted",
        },
    )
    travel_date: str = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Attribute",
            "help": "Returns the departure date of the first segment that uses this fare.",
        },
    )
    departure_date: str = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
            "help": "Returns the departure date of the first segment of the journey.",
        },
    )
    amount: TypeMoney = field(
        default=None, metadata={"name": "Amount", "type": "Attribute"}
    )
    private_fare: TypePrivateFare = field(
        default=None, metadata={"name": "PrivateFare", "type": "Attribute"}
    )
    negotiated_fare: bool = field(
        default=None,
        metadata={
            "name": "NegotiatedFare",
            "type": "Attribute",
            "help": "Identifies the fare as a Negotiated Fare.",
        },
    )
    tour_code: TypeTourCode = field(
        default=None, metadata={"name": "TourCode", "type": "Attribute"}
    )
    waiver_code: str = field(
        default=None, metadata={"name": "WaiverCode", "type": "Attribute"}
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
    pseudo_city_code: TypePcc = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "help": "Provider PseudoCityCode associated with private fare.",
        },
    )
    fare_family: TypeFareFamily = field(
        default=None,
        metadata={
            "name": "FareFamily",
            "type": "Attribute",
            "help": "An alpha-numeric string which denotes fare family. Some carriers may return this in lieu of or in addition to the CabinClass.",
        },
    )
    promotional_fare: bool = field(
        default=None,
        metadata={
            "name": "PromotionalFare",
            "type": "Attribute",
            "help": "Boolean to describe whether the Fare is Promotional fare or not.",
        },
    )
    car_code: TypeCarCode = field(
        default=None, metadata={"name": "CarCode", "type": "Attribute"}
    )
    value_code: TypeValueCode = field(
        default=None, metadata={"name": "ValueCode", "type": "Attribute"}
    )
    bulk_ticket: bool = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
            "help": "Whether the ticket can be issued as bulk for this fare. Providers supported: Worldspan and JAL",
        },
    )
    inclusive_tour: bool = field(
        default=None,
        metadata={
            "name": "InclusiveTour",
            "type": "Attribute",
            "help": "Whether the ticket can be issued as part of included package for this fare. Providers supported: Worldspan and JAL",
        },
    )
    value: str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "help": "Used in rapid reprice",
        },
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "help": "Code of the provider returning this fare info",
        },
    )
    tax_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "TaxAmount",
            "type": "Attribute",
            "help": "Currency code and value for the approximate tax amount for this fare component.",
        },
    )


@dataclass
class AirExchangeMultiQuoteOption:
    """
    The shared object list of AirExchangeMultiQuoteOptions
    """

    air_segment_data: List[AirSegmentData] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentData",
            "type": "Element",
        },
    )
    air_exchange_bundle_total: AirExchangeBundleTotal = field(
        default=None,
        metadata={"name": "AirExchangeBundleTotal", "type": "Element"},
    )
    air_exchange_bundle_list: List[AirExchangeBundleList] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirExchangeBundleList",
            "type": "Element",
        },
    )


@dataclass
class AirPricingInfo:
    """
    Per traveler type pricing breakdown. This will reflect the pricing for all travelers of the specified type.
    """

    fare_info: List[FareInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareInfo",
            "type": "Element",
        },
    )
    fare_status: FareStatus = field(
        default=None, metadata={"name": "FareStatus", "type": "Element"}
    )
    fare_info_ref: List[FareInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareInfoRef",
            "type": "Element",
        },
    )
    booking_info: List[BookingInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BookingInfo",
            "type": "Element",
        },
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
        },
    )
    fare_calc: FareCalc = field(
        default=None, metadata={"name": "FareCalc", "type": "Element"}
    )
    passenger_type: List[PassengerType] = field(
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
    waiver_code: WaiverCode = field(
        default=None, metadata={"name": "WaiverCode", "type": "Element"}
    )
    payment_ref: List[PaymentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "PaymentRef",
            "type": "Element",
            "help": "The reference to the Payment if Air Pricing is charged",
        },
    )
    change_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ChangePenalty",
            "type": "Element",
            "help": "The penalty (if any) to change the itinerary",
        },
    )
    cancel_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "CancelPenalty",
            "type": "Element",
            "help": "The penalty (if any) to cancel the fare",
        },
    )
    no_show_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "NoShowPenalty",
            "type": "Element",
            "help": "The NoShow penalty (if any)",
        },
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FeeInfo",
            "type": "Element",
        },
    )
    adjustment: List[Adjustment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Adjustment",
            "type": "Element",
        },
    )
    yield_value: List[Yield] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Yield",
            "type": "Element",
        },
    )
    air_pricing_modifiers: AirPricingModifiers = field(
        default=None,
        metadata={"name": "AirPricingModifiers", "type": "Element"},
    )
    ticketing_modifiers_ref: List[TicketingModifiersRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketingModifiersRef",
            "type": "Element",
        },
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
        },
    )
    flight_options_list: FlightOptionsList = field(
        default=None, metadata={"name": "FlightOptionsList", "type": "Element"}
    )
    baggage_allowances: BaggageAllowances = field(
        default=None, metadata={"name": "BaggageAllowances", "type": "Element"}
    )
    fare_rules_filter: FareRulesFilter = field(
        default=None, metadata={"name": "FareRulesFilter", "type": "Element"}
    )
    policy_codes_list: PolicyCodesList = field(
        default=None,
        metadata={
            "name": "PolicyCodesList",
            "type": "Element",
            "help": "A list of codes that indicate why an item was determined to be ‘out of policy’",
        },
    )
    price_change: List[PriceChangeType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "PriceChange",
            "type": "Element",
            "help": "Indicates a price change is found in Fare Control Manager",
        },
    )
    action_details: ActionDetails = field(
        default=None, metadata={"name": "ActionDetails", "type": "Element"}
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Commission",
            "type": "Element",
            "help": "Allows an agency to update the commission to a new or different commission rate which will be applied at time of ticketing. The commission Modifier allows the user specify how the commission change is to applied",
        },
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "help": "The IATA location code for this origination of this entity.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "help": "The IATA location code for this destination of this entity.",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    command_key: str = field(
        default=None,
        metadata={
            "name": "CommandKey",
            "type": "Attribute",
            "help": "The command identifier used when this is in response to an AirPricingCommand. Not used in any request processing.",
        },
    )
    amount_type: StringLength1to32 = field(
        default=None,
        metadata={
            "name": "AmountType",
            "type": "Attribute",
            "help": 'This field displays type of payment amount when it is non-monetary. Presently available/supported value is "Flight Pass Credits".',
        },
    )
    includes_vat: bool = field(
        default=None,
        metadata={
            "name": "IncludesVAT",
            "type": "Attribute",
            "help": "Indicates whether the Base Price includes VAT.",
        },
    )
    exchange_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
            "help": "The amount to pay to cover the exchange of the fare (includes penalties).",
        },
    )
    forfeit_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "ForfeitAmount",
            "type": "Attribute",
            "help": "The amount forfeited when the fare is exchanged.",
        },
    )
    refundable: bool = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
            "help": "Indicates whether the fare is refundable",
        },
    )
    exchangeable: bool = field(
        default=None,
        metadata={
            "name": "Exchangeable",
            "type": "Attribute",
            "help": "Indicates whether the fare is exchangeable",
        },
    )
    latest_ticketing_time: str = field(
        default=None,
        metadata={
            "name": "LatestTicketingTime",
            "type": "Attribute",
            "help": "The latest date/time at which this pricing information is valid",
        },
    )
    pricing_method: TypePricingMethod = field(
        default=None,
        metadata={
            "required": True,
            "name": "PricingMethod",
            "type": "Attribute",
        },
    )
    checksum: str = field(
        default=None,
        metadata={
            "name": "Checksum",
            "type": "Attribute",
            "help": "A security value used to guarantee that the pricing data sent in matches the pricing data previously returned",
        },
    )
    eticketability: TypeEticketability = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
            "help": "The E-Ticketability of this AirPricing",
        },
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "help": "The Plating Carrier for this journey",
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
    air_pricing_info_group: int = field(
        default=None,
        metadata={
            "name": "AirPricingInfoGroup",
            "type": "Attribute",
            "help": "This attribute is added to support multiple store fare in Host. All AirPricingInfo with same group number will be stored together.",
        },
    )
    total_net_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "TotalNetPrice",
            "type": "Attribute",
            "help": "The total price of a negotiated fare.",
        },
    )
    ticketed: bool = field(
        default=None,
        metadata={
            "name": "Ticketed",
            "type": "Attribute",
            "help": "Indicates if the associated stored fare is ticketed or not.",
        },
    )
    pricing_type: str = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Attribute",
            "help": "Indicates the Pricing Type used. The possible values are TicketRecord, StoredFare, PricingInstruction.",
        },
    )
    true_last_date_to_ticket: str = field(
        default=None,
        metadata={
            "name": "TrueLastDateToTicket",
            "type": "Attribute",
            "help": "This date indicates the true last date/time to ticket for the fare. This date comes from the filed fare . There is no guarantee the fare will still be available on that date or that the fare amount may change. It is merely the last date to purchase a ticket based on the carriers fare rules at the time the itinerary was quoted and stored",
        },
    )
    fare_calculation_ind: str = field(
        default=None,
        metadata={
            "name": "FareCalculationInd",
            "type": "Attribute",
            "help": "Fare calculation that was used to price the itinerary.",
        },
    )
    cat35_indicator: bool = field(
        default=None,
        metadata={
            "name": "Cat35Indicator",
            "type": "Attribute",
            "help": "A true value indicates that the fare has a Cat35 rule. A false valud indicates that the fare does not have a Cat35 rule",
        },
    )


@dataclass
class FareInfoList:
    """
    The shared object list of FareInfos
    """

    fare_info: List[FareInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "FareInfo",
            "type": "Element",
        },
    )


@dataclass
class AirExchangeMulitQuoteList:
    """
    The shared object list of AirExchangeMultiQuotes
    """

    air_exchange_multi_quote_option: List[AirExchangeMultiQuoteOption] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirExchangeMultiQuoteOption",
            "type": "Element",
        },
    )


@dataclass
class AirPricePoint:
    """
    The container which holds the Non Solutioned result.
    """

    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingInfo",
            "type": "Element",
        },
    )
    air_pricing_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingResultMessage",
            "type": "Element",
        },
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FeeInfo",
            "type": "Element",
            "help": "Supported by ACH only",
        },
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "FareNote",
            "type": "Element",
        },
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
            "help": "Itinerary level taxes",
        },
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    complete_itinerary: bool = field(
        default="true",
        metadata={
            "name": "CompleteItinerary",
            "type": "Attribute",
            "help": "This attribute is used to return whether complete Itinerary is present in the AirPricePoint structure or not. If set to true means AirPricePoint contains the result for full requested itinerary.",
        },
    )


@dataclass
class AirPricingInfoList:
    """
    The shared object list of AirSegments
    """

    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingInfo",
            "type": "Element",
        },
    )


@dataclass
class AirPricingSolution:
    """
    The pricing container for an air travel itinerary
    """

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegment",
            "type": "Element",
        },
    )
    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentRef",
            "type": "Element",
        },
    )
    journey: List[Journey] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Journey",
            "type": "Element",
        },
    )
    leg_ref: List[LegRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "LegRef",
            "type": "Element",
        },
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingInfo",
            "type": "Element",
        },
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareNote",
            "type": "Element",
        },
    )
    fare_note_ref: List[FareNoteRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareNoteRef",
            "type": "Element",
        },
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Connection",
            "type": "Element",
        },
    )
    meta_data: List[MetaData] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "MetaData",
            "type": "Element",
        },
    )
    air_pricing_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingResultMessage",
            "type": "Element",
        },
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FeeInfo",
            "type": "Element",
        },
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
            "help": "Itinerary level taxes",
        },
    )
    air_itinerary_solution_ref: List[AirItinerarySolutionRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirItinerarySolutionRef",
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
    optional_services: OptionalServices = field(
        default=None, metadata={"name": "OptionalServices", "type": "Element"}
    )
    available_ssr: AvailableSsr = field(
        default=None, metadata={"name": "AvailableSSR", "type": "Element"}
    )
    pricing_details: PricingDetails = field(
        default=None, metadata={"name": "PricingDetails", "type": "Element"}
    )
    key: TypeRef = field(
        default=None,
        metadata={"required": True, "name": "Key", "type": "Attribute"},
    )
    complete_itinerary: bool = field(
        default="true",
        metadata={
            "name": "CompleteItinerary",
            "type": "Attribute",
            "help": "This attribute is used to return whether complete Itinerary is present in the AirPricingSolution structure or not. If set to true means AirPricingSolution contains the result for full requested itinerary.",
        },
    )
    quote_date: str = field(
        default=None,
        metadata={
            "name": "QuoteDate",
            "type": "Attribute",
            "help": "This date will be equal to the date of the transaction unless the request included a modified ticket date.",
        },
    )
    itinerary: str = field(
        default=None,
        metadata={
            "name": "Itinerary",
            "type": "Attribute",
            "help": "For an exchange request this tells if the itinerary is the original one or new one. A value of Original will only apply to 1G/1V/1P/1S/1A. A value of New will apply to 1G/1V/1P/1S/1A/ACH.",
        },
    )


@dataclass
class Etr:
    """
    Result of ticketing request
    """

    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata={"name": "AirReservationLocatorCode", "type": "Element"},
    )
    agency_info: AgencyInfo = field(
        default=None, metadata={"name": "AgencyInfo", "type": "Element"}
    )
    booking_traveler: BookingTraveler = field(
        default=None,
        metadata={
            "required": True,
            "name": "BookingTraveler",
            "type": "Element",
        },
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FormOfPayment",
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
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "CreditCardAuth",
            "type": "Element",
            "help": "This is a container to display detail information of credit card auth. Providers supported: Worldspan and JAL.",
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
    fare_calc: FareCalc = field(
        default=None,
        metadata={"required": True, "name": "FareCalc", "type": "Element"},
    )
    ticket: List[Ticket] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "Ticket",
            "type": "Element",
        },
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Commission",
            "type": "Element",
        },
    )
    air_pricing_info: AirPricingInfo = field(
        default=None, metadata={"name": "AirPricingInfo", "type": "Element"}
    )
    audit_data: AuditData = field(
        default=None, metadata={"name": "AuditData", "type": "Element"}
    )
    restriction: List[Restriction] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "Restriction",
            "type": "Element",
        },
    )
    waiver_code: WaiverCode = field(
        default=None, metadata={"name": "WaiverCode", "type": "Element"}
    )
    baggage_allowances: BaggageAllowances = field(
        default=None,
        metadata={
            "name": "BaggageAllowances",
            "type": "Element",
            "help": "Baggage Allowance Info after Ticketing",
        },
    )
    key: TypeRef = field(
        default=None, metadata={"name": "Key", "type": "Attribute"}
    )
    refundable: bool = field(
        default=None, metadata={"name": "Refundable", "type": "Attribute"}
    )
    exchangeable: bool = field(
        default=None, metadata={"name": "Exchangeable", "type": "Attribute"}
    )
    tour_code: TypeTourCode = field(
        default=None, metadata={"name": "TourCode", "type": "Attribute"}
    )
    issued_date: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "IssuedDate",
            "type": "Attribute",
            "help": "Ticket issue date.",
        },
    )
    bulk_ticket: bool = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
            "help": "Whether the ticket was issued as bulk.",
        },
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "help": "Contains the Provider Code of the provider that houses this ETR.",
        },
    )
    provider_locator_code: TypeProviderLocatorCode = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "help": "Contains the Locator Code of the Provider Reservation that houses this ETR.",
        },
    )
    iatanumber: TypeIata = field(
        default=None,
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "help": "Contains the IATA Number of the agent initiating the request.",
        },
    )
    pseudo_city_code: TypePcc = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "help": "Contain Pseudo City, city/office number, branch ID, etc.",
        },
    )
    country_code: TypeCountry = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "help": "Contains Ticketed PCC’s Country code.",
        },
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "help": "Contains the Plating Carrier of this ETR.",
        },
    )


@dataclass
class Tcr:
    """
    Information related to Ticketless carriers
    """

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FormOfPayment",
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
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "BookingTraveler",
            "type": "Element",
        },
    )
    passenger_ticket_number: List[PassengerTicketNumber] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "PassengerTicketNumber",
            "type": "Element",
        },
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingInfo",
            "type": "Element",
        },
    )
    agency_info: AgencyInfo = field(
        default=None, metadata={"name": "AgencyInfo", "type": "Element"}
    )
    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata={"name": "AirReservationLocatorCode", "type": "Element"},
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
    refund_remark: List[RefundRemark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RefundRemark",
            "type": "Element",
        },
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "TCRNumber",
            "type": "Attribute",
            "help": "The identifying number for a Ticketless Air Reservation.",
        },
    )
    status: TypeTcrstatus = field(
        default=None,
        metadata={
            "required": True,
            "name": "Status",
            "type": "Attribute",
            "help": "The current status of this TCR. Some status values are not applicable by some Airlines.",
        },
    )
    modified_date: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "ModifiedDate",
            "type": "Attribute",
            "help": "The date at which the status was changed on this TCR due to an action event (itemized from the booleans below).",
        },
    )
    confirmed_date: str = field(
        default=None,
        metadata={
            "name": "ConfirmedDate",
            "type": "Attribute",
            "help": "The date at which this TCR was confirmed (not created). This mean the payment was approved and processed and travel for this TCR is confirmed.",
        },
    )
    base_price: TypeMoney = field(
        default=None,
        metadata={
            "required": True,
            "name": "BasePrice",
            "type": "Attribute",
            "help": "The base price of this TCR as a whole as it was when it was first booked.",
        },
    )
    taxes: TypeMoney = field(
        default=None,
        metadata={
            "required": True,
            "name": "Taxes",
            "type": "Attribute",
            "help": "The taxes of this TCR as a whole as it was when it was first booked.",
        },
    )
    fees: TypeMoney = field(
        default=None,
        metadata={
            "required": True,
            "name": "Fees",
            "type": "Attribute",
            "help": "The fees of this TCR as a whole as it was when it was first booked.",
        },
    )
    refundable: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "Refundable",
            "type": "Attribute",
            "help": "Is it possible to perform a Refund for this TCR.",
        },
    )
    exchangeable: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "Exchangeable",
            "type": "Attribute",
            "help": "Is it possible to perform an Exchange for this TCR.",
        },
    )
    voidable: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "Voidable",
            "type": "Attribute",
            "help": "Is it possible to perform a Void on this TCR.",
        },
    )
    modifiable: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "Modifiable",
            "type": "Attribute",
            "help": "Is it possible to modify this TCR (opposed to Refund/Exchange/Void).",
        },
    )
    refund_access_code: RefundAccessCode = field(
        default=None,
        metadata={"name": "RefundAccessCode", "type": "Attribute"},
    )
    refund_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
            "help": "Total Amount refunded to the customer.",
        },
    )
    refund_fee: TypeMoney = field(
        default=None,
        metadata={
            "name": "RefundFee",
            "type": "Attribute",
            "help": "Charges incurred for processing refund.",
        },
    )
    forfeit_amount: TypeMoney = field(
        default=None,
        metadata={
            "name": "ForfeitAmount",
            "type": "Attribute",
            "help": "Amount forfeited as a result of refund.",
        },
    )


@dataclass
class TypeBaseAirReservation(BaseReservation):
    """
    Parent Container for Air Reservation
    """

    optional_services: OptionalServices = field(
        default=None, metadata={"name": "OptionalServices", "type": "Element"}
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
    third_party_information: List[ThirdPartyInformation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ThirdPartyInformation",
            "type": "Element",
        },
    )
    document_info: DocumentInfo = field(
        default=None, metadata={"name": "DocumentInfo", "type": "Element"}
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
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ProviderReservationInfoRef",
            "type": "Element",
        },
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegment",
            "type": "Element",
        },
    )
    svc_segment: List[SvcSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SvcSegment",
            "type": "Element",
            "help": "Service segment added to collect additional fee. 1P only",
        },
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingInfo",
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
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "CreditCardAuth",
            "type": "Element",
        },
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareNote",
            "type": "Element",
        },
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FeeInfo",
            "type": "Element",
        },
    )
    tax_info: List[TypeTaxInfoWithPaymentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TaxInfo",
            "type": "Element",
            "help": "Itinerary level taxes",
        },
    )
    ticketing_modifiers: List[TicketingModifiers] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketingModifiers",
            "type": "Element",
        },
    )
    associated_remark: List[AssociatedRemark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AssociatedRemark",
            "type": "Element",
        },
    )
    pocket_itinerary_remark: List[PocketItineraryRemark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "PocketItineraryRemark",
            "type": "Element",
        },
    )
    air_exchange_bundle_total: AirExchangeBundleTotal = field(
        default=None,
        metadata={"name": "AirExchangeBundleTotal", "type": "Element"},
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirExchangeBundle",
            "type": "Element",
            "help": "Bundle exchange, pricing, and penalty information. Providers ACH/1G/1V/1P",
        },
    )


@dataclass
class AirPricePointList:
    """
    Provides the list of AirPricePoint (Non Solutioned Result)
    """

    air_price_point: List[AirPricePoint] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricePoint",
            "type": "Element",
            "help": "The container which holds the Non Solutioned result. Different options for each search leg requested will be returned and one option for each search leg can be selected.",
        },
    )


@dataclass
class AirPriceResult:
    """
    A solution will be returned if one exists. Otherwise an error will be present
    """

    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "AirPricingSolution",
            "type": "Element",
        },
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareRule",
            "type": "Element",
        },
    )
    air_price_error: TypeResultMessage = field(
        default=None, metadata={"name": "AirPriceError", "type": "Element"}
    )
    command_key: str = field(
        default=None,
        metadata={
            "name": "CommandKey",
            "type": "Attribute",
            "help": "The command identifier used when this is in response to an AirPricingCommand. Not used in any request processing.",
        },
    )


@dataclass
class AirReservation(TypeBaseAirReservation):
    """
    The parent container for all booking data
    """

    pass


@dataclass
class AirScheduleChangedInfo:
    """
    Contents will be a new AirPricingSolution that contains all the new schedule information as well as the pricing information.
    """

    air_pricing_solution: AirPricingSolution = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirPricingSolution",
            "type": "Element",
        },
    )


@dataclass
class AirSolutionChangedInfo:
    """
    If RetainReservation is None, this will contain the new values returned from the provider. If RetainReservation is Price, Schedule, or Both and there is a price/schedule change, this will contain the new values that were returned from the provider. If RetainReservation is Price, Schedule, or Both and there isn’t a price/schedule change, this element will not be returned.
    """

    air_pricing_solution: AirPricingSolution = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirPricingSolution",
            "type": "Element",
        },
    )
    reason_code: str = field(
        default=None,
        metadata={"required": True, "name": "ReasonCode", "type": "Attribute"},
    )


@dataclass
class OptionalServicesInfo:
    air_pricing_solution: AirPricingSolution = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirPricingSolution",
            "type": "Element",
        },
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FormOfPayment",
            "type": "Element",
        },
    )
    form_of_payment_ref: List[FormOfPaymentRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FormOfPaymentRef",
            "type": "Element",
        },
    )


@dataclass
class TypeAirReservationWithFop(TypeBaseAirReservation):
    """
    Air Reservation With Form Of Payment.
    """

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FormOfPayment",
            "type": "Element",
        },
    )
