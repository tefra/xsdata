from dataclasses import dataclass, field
from typing import List

from ..common_v48_0.common_req_rsp import *
from ..rail_v48_0.rail import *
from .air import *


@dataclass
class AirBaseReq(BaseReq):
    """
    Context for Requests and Responses
    """

    pass


@dataclass
class AirExchangeEligibilityReq(BaseReq):
    """
    Request to determine if the fares in an itinerary are exchangeable
    """

    provider_reservation_info: "AirExchangeEligibilityReq.str" = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element",
            help="Provider:1P - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged",
            required=True
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Type choices are 'Detail' or 'Summary' Default will be Summary",
        )
    )

    @dataclass
    class ProviderReservationInfo(ProviderReservation):
        pass


@dataclass
class AirExchangeEligibilityRsp(BaseRsp):
    exchange_eligibility_info: str = field(
        default=None,
        metadata=dict(
            name="ExchangeEligibilityInfo",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class AirExchangeMultiQuoteRsp(BaseRsp):
    air_segment_list: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentList",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    brand_list: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BrandList",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_exchange_mulit_quote_list: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeMulitQuoteList",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeQuoteRsp(BaseRsp):
    ticket_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_solution: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help="Provider: 1G/1V/1P/1S/1A.",
            min_occurs=1,
            max_occurs=999
        )
    )
    air_exchange_bundle_total: str = field(
        default=None,
        metadata=dict(
            name="AirExchangeBundleTotal",
            type="Element",
            help=None,
        )
    )
    air_exchange_bundle: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundle",
            type="Element",
            help="Bundle exchange, pricing, and penalty information. Providers ACH/1G/1V/1P",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help="Encrypted data from the host. Required to send the HostToken from the AirExchangeQuoteRsp in the AirExchangeReq. Providers ACH/1G/1V/1P.",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: str = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            help="Provider: ACH.",
        )
    )
    fare_rule: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeReq(BaseReq):
    """
    Request to exchange an itinerary
    """

    air_reservation_locator_code: str = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            help="Identifies the PNR locator code. Providers ACH/1G/1V/1P",
            required=True
        )
    )
    ticket_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    specific_seat_assignment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SpecificSeatAssignment",
            type="Element",
            help="Identifies the standard seat. Providers ACH/1G/1V/1P",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_solution: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help="Providers ACH/1G/1V/1P.",
            min_occurs=1,
            max_occurs=999
        )
    )
    air_exchange_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirExchangeModifiers",
            type="Element",
            help="Provider: ACH.",
        )
    )
    air_exchange_bundle_total: str = field(
        default=None,
        metadata=dict(
            name="AirExchangeBundleTotal",
            type="Element",
            help="Provider: 1G/1V/1P/1S/1A.",
        )
    )
    air_exchange_bundle: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundle",
            type="Element",
            help="Bundle exchange, pricing, and penalty information. Providers ACH/1G/1V/1P.",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help="Encrypted data from the host. Required to send the HostToken from the AirExchangeQuoteRsp in the AirExchangeReq. Providers ACH/1G/1V/1P",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: str = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            help="Provider: ACH.",
        )
    )
    form_of_payment: str = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help="Form of Payment for any additional collection charges for the Exchange. For ACH, most carriers will only allow refund amounts to the original form of payment. Providers ACH/1G/1V/1P",
        )
    )
    form_of_payment_ref: str = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            help="Provider: ACH-Universal Record reference to Form of Payment for any Additional Collection charges or Refund due for the itinerary exchange",
        )
    )
    ssrinfo: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SSRInfo",
            type="Element",
            help="Providers ACH, 1G, 1V, 1P.",
            min_occurs=0,
            max_occurs=999
        )
    )
    add_svc: str = field(
        default=None,
        metadata=dict(
            name="AddSvc",
            type="Element",
            help="1P - Add SVC segments to collect additional fee",
        )
    )
    return_reservation: str = field(
        default="false",
        metadata=dict(
            name="ReturnReservation",
            type="Attribute",
            help="Provider: ACH.",
        )
    )


@dataclass
class AirExchangeRsp(BaseRsp):
    ticket_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_traveler: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTraveler",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_reservation: str = field(
        default=None,
        metadata=dict(
            name="AirReservation",
            type="Element",
            help="Provider: ACH.",
        )
    )
    exchange_failure_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangeFailureInfo",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeTicketingReq(BaseReq):
    """
    Request to ticket an exchanged itinerary. Providers 1G, 1V, 1P.
    """

    air_reservation_locator_code: str = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            help="Identifies the PNR to ticket. Providers 1G, 1V, 1P.",
            required=True
        )
    )
    ticket_number: str = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help="Ticket number to reissue. Providers 1G, 1V, 1P.",
            required=True
        )
    )
    ticketing_modifiers_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketingModifiersRef",
            type="Element",
            help="Provider: 1P-Reference to a shared list of Ticketing Modifiers. This is supported for Worldspan provider only. When AirPricingInfoRef is used along with TicketingModifiersRef means that particular TicketingModifiers will to be applied while ticketing the Stored fare corresponding to the AirPricingInfo. Absence of AirPricingInfoRef means that particular TicketingModifiers will be applied to all Stored fares which are requested to be ticketed.",
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_code: str = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element",
            help=None,
        )
    )
    detailed_billing_information: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element",
            help="Providers 1G, 1V, 1P.",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_ticketing_modifiers: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirTicketingModifiers",
            type="Element",
            help="Provider: 1G,1V,1P.",
            min_occurs=0,
            max_occurs=999
        )
    )
    bulk_ticket: str = field(
        default="false",
        metadata=dict(
            name="BulkTicket",
            type="Attribute",
            help="Providers 1G, 1V, 1P.",
        )
    )
    change_fee_on_ticket: str = field(
        default="true",
        metadata=dict(
            name="ChangeFeeOnTicket",
            type="Attribute",
            help="Applies the change fee/penalty to the original form of payment. Providers: 1V",
        )
    )


@dataclass
class AirExchangeTicketingRsp(BaseRsp):
    """
    Response to reissue a ticket.
    """

    air_solution_changed_info: str = field(
        default=None,
        metadata=dict(
            name="AirSolutionChangedInfo",
            type="Element",
            help=None,
        )
    )
    etr: str = field(
        default=None,
        metadata=dict(
            name="ETR",
            type="Element",
            help="Provider 1G, 1V, 1P.",
        )
    )
    ticket_failure_info: str = field(
        default=None,
        metadata=dict(
            name="TicketFailureInfo",
            type="Element",
            help="Provider 1G, 1V, 1P.",
        )
    )
    detailed_billing_information: str = field(
        default=None,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element",
            help="Providers 1G, 1V, 1P.",
        )
    )


@dataclass
class AirFareDisplayReq(BaseReq):
    """
    Request to display a tariff for based on origin, destination, and other options
    """

    fare_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FareType",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=5
        )
    )
    passenger_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerType",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingCode",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=5
        )
    )
    include_addl_booking_code_info: str = field(
        default=None,
        metadata=dict(
            name="IncludeAddlBookingCodeInfo",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
        )
    )
    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
        )
    )
    carrier: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=10
        )
    )
    account_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=5
        )
    )
    contract_code: str = field(
        default=None,
        metadata=dict(
            name="ContractCode",
            type="Element",
            help="Provider: 1G,1V.",
        )
    )
    air_fare_display_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayModifiers",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
        )
    )
    point_of_sale: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            help="Provider: 1G,1V.",
            min_occurs=0,
            max_occurs=5
        )
    )
    air_fare_display_rule_key: str = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayRuleKey",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
        )
    )
    origin: str = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J.",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: str = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J.",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J.",
            required=True,
            min_length=2.0,
            max_length=5.0
        )
    )
    include_mile_route_information: str = field(
        default=None,
        metadata=dict(
            name="IncludeMileRouteInformation",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J-Used to request Mile/Route Information in follow on (Mile, Route, Both)",
        )
    )
    un_saleable_fares_only: str = field(
        default=None,
        metadata=dict(
            name="UnSaleableFaresOnly",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J-Used to request unsaleable fares only also known as place of sale fares.",
        )
    )
    channel_id: str = field(
        default=None,
        metadata=dict(
            name="ChannelId",
            type="Attribute",
            help="A Channel ID is 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.",
            min_length=2.0,
            max_length=4.0
        )
    )
    nscc: str = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            help="1 to 3 numeric that define a Search Control Console filter.This attribute is used to override that filter.",
            min_length=1.0,
            max_length=3.0
        )
    )
    return_mm: str = field(
        default="false",
        metadata=dict(
            name="ReturnMM",
            type="Attribute",
            help="If this attribute is set to true, Fare Control Manager processing will be invoked.",
        )
    )


@dataclass
class AirFareDisplayRsp(BaseRsp):
    """
    Response to an AirFareDisplayReq
    """

    fare_display: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FareDisplay",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirFareRulesReq(BaseReq):
    """
    Request to display the full text fare rules.
    """

    air_fare_rules_modifier: str = field(
        default=None,
        metadata=dict(
            name="AirFareRulesModifier",
            type="Element",
            help="Provider: 1G,1V.",
        )
    )
    fare_rules_filter_category: List["AirFareRulesReq.str"] = field(
        default_factory=list,
        metadata=dict(
            name="FareRulesFilterCategory",
            type="Element",
            help="Structured Fare Rules Filter if requested will return rules for requested categories in the response. Applicable for providers 1G, 1V.",
            min_occurs=0,
            max_occurs=16
        )
    )
    air_reservation_selector: "AirFareRulesReq.str" = field(
        default=None,
        metadata=dict(
            name="AirReservationSelector",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH-Parameters to use for a fare rule lookup associated with an Air Reservation Locator Code",
            required=True
        )
    )
    fare_rule_lookup: str = field(
        default=None,
        metadata=dict(
            name="FareRuleLookup",
            type="Element",
            help="Used to look up fare rules based on the origin, destination, and carrier of the air segment, the fare basis code and the provider code. Providers: 1P, 1J.",
        )
    )
    fare_rule_key: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleKey",
            type="Element",
            help="Used to look up fare rules based on a fare rule key. Providers: 1G, 1V, 1P, 1J, ACH.",
            min_occurs=1,
            max_occurs=999
        )
    )
    air_fare_display_rule_key: str = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayRuleKey",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            required=True
        )
    )
    fare_rule_type: str = field(
        default="long",
        metadata=dict(
            name="FareRuleType",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH.",
        )
    )

    @dataclass
    class FareRulesFilterCategory:
        category_code: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="CategoryCode",
                type="Element",
                help="Structured Fare Rules can be requested for 'ADV', 'MIN', 'MAX', 'STP', and 'CHG'.",
                min_occurs=1,
                max_occurs=35
            )
        )
        fare_info_ref: str = field(
            default=None,
            metadata=dict(
                name="FareInfoRef",
                type="Attribute",
                help="Key reference for multiple fare rule",
            )
        )

    @dataclass
    class AirReservationSelector:
        fare_info_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="FareInfoRef",
                type="Element",
                help=None,
                min_occurs=0,
                max_occurs=999
            )
        )
        air_reservation_locator_code: str = field(
            default=None,
            metadata=dict(
                name="AirReservationLocatorCode",
                type="Attribute",
                help="The Air Reservation locator code which is an unique identifier for the reservation",
                required=True,
                min_length=5.0,
                max_length=8.0
            )
        )


@dataclass
class AirFareRulesRsp(BaseRsp):
    """
    Response to an AirFareRuleReq.
    """

    fare_rule: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirMerchandisingDetailsReq(BaseReq):
    """
    Request to retrieve brand details and optional services included in the brand
    """

    merchandising_details: str = field(
        default=None,
        metadata=dict(
            name="MerchandisingDetails",
            type="Element",
            help=None,
            required=True
        )
    )
    optional_service_modifiers: str = field(
        default=None,
        metadata=dict(
            name="OptionalServiceModifiers",
            type="Element",
            help=None,
            required=True
        )
    )
    merchandising_availability_details: str = field(
        default=None,
        metadata=dict(
            name="MerchandisingAvailabilityDetails",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class AirMerchandisingDetailsRsp(BaseRsp):
    """
    Response for retrieved brand details and optional services included in them
    """

    optional_services: str = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            help=None,
        )
    )
    brand: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Brand",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    unassociated_booking_code_list: "AirMerchandisingDetailsRsp.str" = field(
        default=None,
        metadata=dict(
            name="UnassociatedBookingCodeList",
            type="Element",
            help="Lists classes of service by segment sent in the request which are not associated to a brand.",
        )
    )

    @dataclass
    class UnassociatedBookingCodeList:
        applicable_segment: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ApplicableSegment",
                type="Element",
                help=None,
                min_occurs=0,
                max_occurs=99
            )
        )


@dataclass
class AirMerchandisingOfferAvailabilityReq(BaseReq):
    """
    Check with the supplier whether or not the reservation or air solution supports any merchandising offerings.
    """

    agency_sell_info: str = field(
        default=None,
        metadata=dict(
            name="AgencySellInfo",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
        )
    )
    air_solution: str = field(
        default=None,
        metadata=dict(
            name="AirSolution",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
        )
    )
    host_reservation: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="HostReservation",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    offer_availability_modifiers: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="OfferAvailabilityModifiers",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    merchandising_pricing_modifiers: str = field(
        default=None,
        metadata=dict(
            name="MerchandisingPricingModifiers",
            type="Element",
            help="Used to provide additional pricing modifiers. Provider:ACH.",
        )
    )


@dataclass
class AirMerchandisingOfferAvailabilityRsp(BaseRsp):
    """
    Contains the merchandising offerings for the given passenger and itinerary.
    """

    air_solution: str = field(
        default=None,
        metadata=dict(
            name="AirSolution",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
            required=True
        )
    )
    remark: str = field(
        default=None,
        metadata=dict(
            name="Remark",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
        )
    )
    optional_services: str = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            help=None,
        )
    )
    embargo_list: str = field(
        default=None,
        metadata=dict(
            name="EmbargoList",
            type="Element",
            help=None,
        )
    )


@dataclass
class AirPrePayReq(BaseReq):
    """
    Flight Pass Request.
    """

    list_search: "AirPrePayReq.str" = field(
        default=None,
        metadata=dict(
            name="ListSearch",
            type="Element",
            help="Provider: ACH.",
            required=True
        )
    )
    pre_pay_retrieve: "AirPrePayReq.str" = field(
        default=None,
        metadata=dict(
            name="PrePayRetrieve",
            type="Element",
            help="Provider: ACH.",
            required=True
        )
    )

    @dataclass
    class ListSearch:
        person_name_search: str = field(
            default=None,
            metadata=dict(
                name="PersonNameSearch",
                type="Element",
                help="Customer name detail for searching flight pass content.",
                required=True
            )
        )
        loyalty_card: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="LoyaltyCard",
                type="Element",
                help="Customer loyalty card for searching flight pass content.",
                min_occurs=1,
                max_occurs=999
            )
        )
        start_from_result: str = field(
            default=None,
            metadata=dict(
                name="StartFromResult",
                type="Attribute",
                help="Start index of the section of flight pass numbers that is being requested.",
                required=True,
                min_inclusive=1.0
            )
        )
        max_results: str = field(
            default=None,
            metadata=dict(
                name="MaxResults",
                type="Attribute",
                help="Max Number of Flight Passes being requested for.",
                required=True,
                min_inclusive=1.0,
                max_inclusive=200.0
            )
        )

    @dataclass
    class PrePayRetrieve:
        id: str = field(
            default=None,
            metadata=dict(
                name="Id",
                type="Attribute",
                help="Pre pay id to retrieved,example flight pass number",
                required=True,
                min_length=1.0,
                max_length=36.0
            )
        )
        type: str = field(
            default=None,
            metadata=dict(
                name="Type",
                type="Attribute",
                help="Pre pay id type,example 'FlightPass'",
            )
        )


@dataclass
class AirPrePayRsp(BaseRsp):
    """
    Flight Pass Response.
    """

    pre_pay_profile_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PrePayProfileInfo",
            type="Element",
            help="Provider: ACH.",
            min_occurs=1,
            max_occurs=999
        )
    )
    max_results: str = field(
        default=None,
        metadata=dict(
            name="MaxResults",
            type="Attribute",
            help="Provider: ACH-Max Number of Flight Passes being returned.",
            min_inclusive=1.0,
            max_inclusive=200.0
        )
    )
    more_indicator: str = field(
        default=None,
        metadata=dict(
            name="MoreIndicator",
            type="Attribute",
            help="Provider: ACH-Indicates if there are more flight passes to be offered",
        )
    )
    more_data_start_index: str = field(
        default=None,
        metadata=dict(
            name="MoreDataStartIndex",
            type="Attribute",
            help="Provider: ACH-Indicates start index of the next flight Passes",
        )
    )


@dataclass
class AirRefundQuoteReq(BaseReq):
    """
    Request to quote a refund for an itinerary
    """

    ticket_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TCRNumber",
            type="Element",
            help="Provider: ACH-The identifying number for a Ticketless Air Reservation",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_refund_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirRefundModifiers",
            type="Element",
            help="Provider: ACH.",
        )
    )
    host_token: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info: List["AirRefundQuoteReq.str"] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element",
            help="Provider: 1P - Represents a valid Provider Reservation/PNR whose itinerary is to be requested",
            min_occurs=0,
            max_occurs=999
        )
    )
    ignore: str = field(
        default="false",
        metadata=dict(
            name="Ignore",
            type="Attribute",
            help="Provider: ACH.",
        )
    )

    @dataclass
    class ProviderReservationInfo(ProviderReservation):
        pass


@dataclass
class AirRefundQuoteRsp(BaseRsp):
    air_refund_bundle: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirRefundBundle",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrrefund_bundle: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TCRRefundBundle",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirRefundReq(BaseReq):
    """
    Request to refund an itinerary for the amount previously quoted
    """

    air_refund_bundle: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirRefundBundle",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrrefund_bundle: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TCRRefundBundle",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_refund_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirRefundModifiers",
            type="Element",
            help=None,
        )
    )
    commission: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Commission",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=9
        )
    )
    form_of_payment: str = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help="Provider: ACH-Form of Payment for any Additional Collection charges for the Refund.",
        )
    )


@dataclass
class AirRefundRsp(BaseRsp):
    etr: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcr: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TCR",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    refund_failure_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="RefundFailureInfo",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirRepriceRsp(BaseRsp):
    air_pricing_solution: str = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help=None,
            required=True
        )
    )
    fare_rule: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirRetrieveDocumentReq(BaseReq):
    """
    Retrieve the post booking information for a PNR. ETRs will be returned for standard carriers. TCRs will be returned for Ticketless carriers. If the locator is send on a standard carrier, all ETRs will be retrieved.
    """

    air_reservation_locator_code: str = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
        )
    )
    ticket_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TCRNumber",
            type="Element",
            help="Provider: 1G,1V,1P,1J-The identifying number for a Ticketless Air Reservation.",
            min_occurs=0,
            max_occurs=999
        )
    )
    return_restrictions: str = field(
        default=None,
        metadata=dict(
            name="ReturnRestrictions",
            type="Attribute",
            help="Will return a response which includes a set of restrictions associated with the document.",
        )
    )
    return_pricing: str = field(
        default=None,
        metadata=dict(
            name="ReturnPricing",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J-Will return a response which includes the pricing associated with the ETR.",
        )
    )
    retrieve_mco: str = field(
        default=None,
        metadata=dict(
            name="RetrieveMCO",
            type="Attribute",
            help="When true, returns MCO Information. The default value is false.",
        )
    )


@dataclass
class AirRetrieveDocumentRsp(BaseRsp):
    etr: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )
    mco: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="MCO",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcr: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TCR",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )
    document_failure_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="DocumentFailureInfo",
            type="Element",
            help="Provider: 1G,1V,1P,1J-Will be optionally returned if there are duplicate ticket numbers.",
            min_occurs=0,
            max_occurs=999
        )
    )
    service_fee_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceFeeInfo",
            type="Element",
            help="Provider: 1G,1V",
            min_occurs=0,
            max_occurs=99
        )
    )
    universal_record_locator_code: str = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J-Represents a valid Universal Record locator code.",
            min_length=5.0,
            max_length=8.0
        )
    )


@dataclass
class AirSearchReq(BaseSearchReq):
    """
    Base Request for Air Search
    """

    point_of_commencement: str = field(
        default=None,
        metadata=dict(
            name="PointOfCommencement",
            type="Element",
            help=None,
        )
    )
    air_search_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirSearchModifiers",
            type="Element",
            help=None,
        )
    )
    journey_data: str = field(
        default=None,
        metadata=dict(
            name="JourneyData",
            type="Element",
            help=None,
        )
    )
    search_air_leg: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SearchAirLeg",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=16
        )
    )
    search_specific_air_segment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SearchSpecificAirSegment",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirTicketingRsp(BaseRsp):
    """
    Response to ticket a previously stored reservation.
    """

    air_solution_changed_info: str = field(
        default=None,
        metadata=dict(
            name="AirSolutionChangedInfo",
            type="Element",
            help=None,
        )
    )
    etr: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticket_failure_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketFailureInfo",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )
    detailed_billing_information: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirVoidDocumentReq(BaseReq):
    """
    Request to void all previously issued tickets for the PNR.
    """

    air_reservation_locator_code: str = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            help="Provider: 1G,1V.",
        )
    )
    void_document_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="VoidDocumentInfo",
            type="Element",
            help="Provider: 1G,1V-All tickets that belong to this PNR must be enumerated here. Voiding only some tickets of a multi-ticket PNR not currently supported.",
            min_occurs=0,
            max_occurs=999
        )
    )
    show_etr: str = field(
        default="false",
        metadata=dict(
            name="ShowETR",
            type="Attribute",
            help="Provider: 1G,1V-If set as true, response will display the detailed ETR for successfully voided E-Tickets.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Provider: 1G,1V-Provider code of a specific host.",
            min_length=2.0,
            max_length=5.0
        )
    )
    provider_locator_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            help="Provider: 1G,1V-Contains the locator of the host reservation.",
        )
    )
    validate_spanish_residency: str = field(
        default="false",
        metadata=dict(
            name="ValidateSpanishResidency",
            type="Attribute",
            help="Provider: 1G - If set as true, Spanish Residency will be validated for Provisioned Customers.",
        )
    )


@dataclass
class AirVoidDocumentRsp(BaseRsp):
    """
    Result of void ticket request. Includes ticket number of voided tickets and air segments with updated status.
    """

    etr: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            help="Provider: 1G,1V.",
            min_occurs=0,
            max_occurs=999
        )
    )
    void_result_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="VoidResultInfo",
            type="Element",
            help="Provider: 1G,1V.",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class BaseAirExchangeMultiQuoteReq(BaseCoreReq):
    ticket_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info: "BaseAirExchangeMultiQuoteReq.str" = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element",
            help="Provider: 1P - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged",
        )
    )
    air_pricing_solution: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=2
        )
    )
    repricing_modifiers: str = field(
        default=None,
        metadata=dict(
            name="RepricingModifiers",
            type="Element",
            help=None,
        )
    )
    original_itinerary_details: str = field(
        default=None,
        metadata=dict(
            name="OriginalItineraryDetails",
            type="Element",
            help=None,
        )
    )
    override_pcc: str = field(
        default=None,
        metadata=dict(
            name="OverridePCC",
            type="Element",
            help=None,
        )
    )

    @dataclass
    class ProviderReservationInfo(ProviderReservation):
        pass


@dataclass
class BaseAirExchangeQuoteReq(BaseCoreReq):
    ticket_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info: "BaseAirExchangeQuoteReq.str" = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element",
            help="Provider: 1G/1V/1P/ACH - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged",
        )
    )
    air_pricing_solution: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=2
        )
    )
    air_exchange_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirExchangeModifiers",
            type="Element",
            help="Provider: ACH.",
        )
    )
    host_token: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: str = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            help="Provider: ACH.",
        )
    )
    form_of_payment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help="Provider: ACH-This would allow a user to see the fees if they are changing from one Form Of Payment to other .",
            min_occurs=0,
            max_occurs=999
        )
    )
    repricing_modifiers: str = field(
        default=None,
        metadata=dict(
            name="RepricingModifiers",
            type="Element",
            help=None,
        )
    )
    original_itinerary_details: str = field(
        default=None,
        metadata=dict(
            name="OriginalItineraryDetails",
            type="Element",
            help=None,
        )
    )
    pcc: str = field(
        default=None,
        metadata=dict(
            name="PCC",
            type="Element",
            help=None,
        )
    )
    fare_rule_type: str = field(
        default="none",
        metadata=dict(
            name="FareRuleType",
            type="Attribute",
            help="Provider: ACH.",
        )
    )

    @dataclass
    class ProviderReservationInfo(ProviderReservation):
        pass


@dataclass
class BaseAirPriceReq(BaseCoreReq):
    air_itinerary: str = field(
        default=None,
        metadata=dict(
            name="AirItinerary",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
            required=True
        )
    )
    air_pricing_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
        )
    )
    search_passenger: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SearchPassenger",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS passenger",
            min_occurs=1,
            max_occurs=18
        )
    )
    air_pricing_command: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingCommand",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
            min_occurs=1,
            max_occurs=16
        )
    )
    air_reservation_locator_code: str = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            help="Provider: ACH,1P,1J",
        )
    )
    optional_services: str = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            help="Provider: ACH.",
        )
    )
    form_of_payment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    pcc: str = field(
        default=None,
        metadata=dict(
            name="PCC",
            type="Element",
            help=None,
        )
    )
    ssr: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SSR",
            type="Element",
            help="Special Service Request for GST tax details. Provider: ACH",
            min_occurs=0,
            max_occurs=99
        )
    )
    check_obfees: str = field(
        default=None,
        metadata=dict(
            name="CheckOBFees",
            type="Attribute",
            help="A flag to return fees for ticketing and for various forms of payment. The default is “TicketingOnly” and will return only ticketing fees. The value “All” will return ticketing fees and the applicable form of payment fees for the form of payment information specified in the request. “FOPOnly” will return the applicable form of payment fees for the form of payment information specified in the request. Form of payment fees are never included in the total unless specific card details are in the request.Provider notes:ACH - CheckOBFees is valid only for LowFareSearch. The valid values are “All”, “TicketingOnly” and “None” and the default value is “None”. 1P/1J -The valid values are “All”, “None” and “TicketingOnly”.1G – All four values are supported.1V/RCH – CheckOBFees are not supported.”",
        )
    )
    fare_rule_type: str = field(
        default="none",
        metadata=dict(
            name="FareRuleType",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH.",
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help="Specifies the supplier/ vendor for vendor specific price requests",
            min_length=1.0,
            max_length=5.0
        )
    )
    ticket_date: str = field(
        default=None,
        metadata=dict(
            name="TicketDate",
            type="Attribute",
            help="YYYY-MM-DD Using a date in the past is a request for an historical fare",
        )
    )
    check_flight_details: str = field(
        default="false",
        metadata=dict(
            name="CheckFlightDetails",
            type="Attribute",
            help="To Include FlightDetails in Response set to “true” the Default value is “false”.",
        )
    )
    return_mm: str = field(
        default="false",
        metadata=dict(
            name="ReturnMM",
            type="Attribute",
            help="If this attribute is set to “true”, Fare Control Manager processing will be invoked.",
        )
    )
    nscc: str = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            help="1 to 3 numeric that defines a Search Control Console filter.This attribute is used to override that filter.",
            min_length=1.0,
            max_length=3.0
        )
    )
    split_pricing: str = field(
        default="false",
        metadata=dict(
            name="SplitPricing",
            type="Attribute",
            help="Indicates whether the AirSegments should be priced together or separately. Set ‘true’ for split pricing. Set ‘false’ for pricing together.SplitPricing is not supported with post book re-pricing.",
        )
    )
    ignore_availability: str = field(
        default="false",
        metadata=dict(
            name="IgnoreAvailability",
            type="Attribute",
            help="Provides a method of pricing a book itinerary with the lowest fare regardless of the availability for the class of service. Only for providers 1P/1J.",
        )
    )


@dataclass
class BaseAirPriceRsp(BaseRsp):
    air_itinerary: str = field(
        default=None,
        metadata=dict(
            name="AirItinerary",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
            required=True
        )
    )
    air_price_result: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirPriceResult",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
            min_occurs=1,
            max_occurs=16
        )
    )


@dataclass
class BaseAirSearchReq(BaseCoreSearchReq):
    """
    Base Request for Low fare air Search
    """

    air_search_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirSearchModifiers",
            type="Element",
            help=None,
        )
    )
    split_ticketing_search: str = field(
        default=None,
        metadata=dict(
            name="SplitTicketingSearch",
            type="Element",
            help=None,
        )
    )
    journey_data: str = field(
        default=None,
        metadata=dict(
            name="JourneyData",
            type="Element",
            help=None,
        )
    )
    search_air_leg: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SearchAirLeg",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=9
        )
    )
    search_specific_air_segment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SearchSpecificAirSegment",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class BaseAvailabilitySearchRsp(BaseSearchRsp):
    """
    Availability Search response
    """

    flight_details_list: str = field(
        default=None,
        metadata=dict(
            name="FlightDetailsList",
            type="Element",
            help=None,
        )
    )
    air_segment_list: str = field(
        default=None,
        metadata=dict(
            name="AirSegmentList",
            type="Element",
            help=None,
        )
    )
    fare_info_list: str = field(
        default=None,
        metadata=dict(
            name="FareInfoList",
            type="Element",
            help=None,
        )
    )
    fare_remark_list: str = field(
        default=None,
        metadata=dict(
            name="FareRemarkList",
            type="Element",
            help=None,
        )
    )
    air_itinerary_solution: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirItinerarySolution",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token_list: str = field(
        default=None,
        metadata=dict(
            name="HostTokenList",
            type="Element",
            help=None,
        )
    )
    apisrequirements_list: str = field(
        default=None,
        metadata=dict(
            name="APISRequirementsList",
            type="Element",
            help=None,
        )
    )
    distance_units: str = field(
        default=None,
        metadata=dict(
            name="DistanceUnits",
            type="Attribute",
            help=None,
            length=2
        )
    )


@dataclass
class BrandList:
    brand: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Brand",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class EmdissuanceReq(BaseReq):
    """
    Electronic Miscellaneous Document issuance request.Supported providers are 1V/1G/1P/1J
    """

    provider_reservation_detail: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationDetail",
            type="Element",
            help="PNR information for which EMD is going to be issued.",
            required=True
        )
    )
    ticket_number: str = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help="Ticket number for which EMD is going to be issued.Required for EMD-A issuance.",
        )
    )
    issuance_modifiers: str = field(
        default=None,
        metadata=dict(
            name="IssuanceModifiers",
            type="Element",
            help="General modifiers related to EMD issuance.",
        )
    )
    selection_modifiers: str = field(
        default=None,
        metadata=dict(
            name="SelectionModifiers",
            type="Element",
            help="Modifiers related to selection of services during EMD issuance.",
        )
    )
    universal_record_locator_code: str = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            help="Represents a valid Universal Record locator code.",
            required=True,
            min_length=5.0,
            max_length=8.0
        )
    )
    show_details: str = field(
        default="false",
        metadata=dict(
            name="ShowDetails",
            type="Attribute",
            help="This attribute gives the control to request for complete information on Issued EMDs or minimal information.Requesting complete information leads to possible multiple supplier calls for fetching all the details.",
        )
    )
    issue_all_open_svc: str = field(
        default="false",
        metadata=dict(
            name="IssueAllOpenSVC",
            type="Attribute",
            help="Issues EMDS to all SVC segments. If it is true, TicketNumber and SVC segment reference need not be provided. Supported provider 1P.",
        )
    )


@dataclass
class EmdissuanceRsp(BaseRsp):
    """
    Electronic Miscellaneous Document issuance response.Supported providers are 1V/1G/1P/1J
    """

    emdsummary_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="EMDSummaryInfo",
            type="Element",
            help="List of EMDSummaryInfo elements to show minimal information in issuance response. Appears for ShowDetails=false in the request.This is the default behaviour.",
            min_occurs=0,
            max_occurs=999
        )
    )
    emdinfo: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="EMDInfo",
            type="Element",
            help="List of EMDInfo elements to show detailoed information in issuance response. Appears for ShowDetails=true in the request.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class EmdretrieveReq(BaseReq):
    """
    Electronic Miscellaneous Document retrieve request.Supported providers are 1G/1V/1P/1J
    """

    list_retrieve: "EmdretrieveReq.str" = field(
        default=None,
        metadata=dict(
            name="ListRetrieve",
            type="Element",
            help="Provider: 1G/1V/1P/1J-Information required for retrieval of list of EMDs",
            required=True
        )
    )
    detail_retrieve: "EmdretrieveReq.str" = field(
        default=None,
        metadata=dict(
            name="DetailRetrieve",
            type="Element",
            help="Provider: 1G/1V/1P/1J-Information required for a detailed EMD retrieve",
            required=True
        )
    )

    @dataclass
    class ListRetrieve:
        provider_reservation_detail: str = field(
            default=None,
            metadata=dict(
                name="ProviderReservationDetail",
                type="Element",
                help="Provider reservation details to be provided to fetch list of EMDs associated with it.",
                required=True
            )
        )

    @dataclass
    class DetailRetrieve:
        provider_reservation_detail: str = field(
            default=None,
            metadata=dict(
                name="ProviderReservationDetail",
                type="Element",
                help="Provider reservation locator to be specified for display operation, if mentioned along woth the EMD number then synchronization of that EMD is performed considering the same to be associated with the mentioned PNR.",
            )
        )
        emdnumber: str = field(
            default=None,
            metadata=dict(
                name="EMDNumber",
                type="Element",
                help="EMD number to be specified for display operation. If mentioned along with provider reservation detail then synchronization of that EMD is performed considering the same to be associated with the mentioned PNR.",
                required=True,
                length=13
            )
        )


@dataclass
class EmdretrieveRsp(BaseRsp):
    """
    Electronic Miscellaneous Document list and detail retrieve response.Supported providers are 1G/1V/1P/1J
    """

    emdinfo: str = field(
        default=None,
        metadata=dict(
            name="EMDInfo",
            type="Element",
            help="Provider: 1G/1V/1P/1J.",
            required=True
        )
    )
    emdsummary_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="EMDSummaryInfo",
            type="Element",
            help="Provider: 1G/1V/1P/1J.",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightDetailsReq(BaseReq):
    """
    Request for the Flight Details of segments.
    """

    air_segment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightDetailsRsp(BaseRsp):
    air_segment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=1,
            max_occurs=999
        )
    )
    co2_emissions: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="CO2Emissions",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class FlightInformationReq(BaseReq):
    """
    Request for the Flight Info of segments.
    """

    flight_info_criteria: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FlightInfoCriteria",
            type="Element",
            help="Provider: 1G,1V.",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightInformationRsp(BaseRsp):
    flight_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FlightInfo",
            type="Element",
            help="Provider: 1G,1V.",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightTimeTableReq(BaseSearchReq):
    """
    Request for Flight Time Table.
    """

    flight_time_table_criteria: str = field(
        default=None,
        metadata=dict(
            name="FlightTimeTableCriteria",
            type="Element",
            help="Provider: 1G,1V.",
            required=True
        )
    )


@dataclass
class FlightTimeTableRsp(BaseSearchRsp):
    """
    Response for Flight Time Table.
    """

    flight_time_table_list: "FlightTimeTableRsp.str" = field(
        default=None,
        metadata=dict(
            name="FlightTimeTableList",
            type="Element",
            help="Provider: 1G,1V.",
        )
    )

    @dataclass
    class FlightTimeTableList:
        flight_time_detail: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="FlightTimeDetail",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class RetrieveLowFareSearchReq(BaseReq):
    """
    Retrieve low fare search responses that were initiated by an asynchronous request.
    """

    search_id: str = field(
        default=None,
        metadata=dict(
            name="SearchId",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH-SearchID to be used for Asynchronous LowFareSearch Request",
            required=True
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH-Provider code of a specific host",
            required=True,
            min_length=2.0,
            max_length=5.0
        )
    )


@dataclass
class SearchSpecificAirSegment:
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            help="The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
            required=True
        )
    )
    carrier: str = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help="The carrier that is marketing this segment",
            required=True,
            length=2
        )
    )
    flight_number: str = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            help="The flight number under which the marketing carrier is marketing this flight",
            required=True,
            max_length=5.0
        )
    )
    origin: str = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="The IATA location code for this origination of this entity.",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: str = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="The IATA location code for this destination of this entity.",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    segment_index: str = field(
        default=None,
        metadata=dict(
            name="SegmentIndex",
            type="Attribute",
            help="The sequential AirSegment number that this segment connected to.",
        )
    )


@dataclass
class SeatMapReq(BaseReq):
    """
    Request a seat map for the give flight information
    """

    agency_sell_info: str = field(
        default=None,
        metadata=dict(
            name="AgencySellInfo",
            type="Element",
            help="Provider: ACH-Required if the user requesting the seat map is not the same agent authenticated in the request.",
        )
    )
    air_segment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH,MCH.",
            min_occurs=0,
            max_occurs=99
        )
    )
    host_token: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help="Provider: ACH-Required if the carrier has multiple adapters.",
            min_occurs=0,
            max_occurs=99
        )
    )
    search_traveler: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SearchTraveler",
            type="Element",
            help="Provider: 1G,1V,ACH,MCH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_reservation: str = field(
        default=None,
        metadata=dict(
            name="HostReservation",
            type="Element",
            help="Provider: ACH,MCH-Required when seat price is requested.",
        )
    )
    merchandising_pricing_modifiers: str = field(
        default=None,
        metadata=dict(
            name="MerchandisingPricingModifiers",
            type="Element",
            help="Used to provide additional pricing options. Provider:ACH.",
        )
    )
    return_seat_pricing: str = field(
        default=None,
        metadata=dict(
            name="ReturnSeatPricing",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH-When set to true the price of the seat will be returned if it exists.",
            required=True
        )
    )
    return_branding_info: str = field(
        default="false",
        metadata=dict(
            name="ReturnBrandingInfo",
            type="Attribute",
            help="A value of true will return the BrandingInfo block in the response if applicable. A value of false will not return the BrandingInfo block in the response. Providers: 1G, 1V, 1P, 1J, ACH",
        )
    )


@dataclass
class SeatMapRsp(BaseRsp):
    host_token: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help="Provider: ACH,MCH.",
            min_occurs=0,
            max_occurs=99
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH,MCH.",
        )
    )
    air_segment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help="Provider: ACH,MCH.",
            min_occurs=0,
            max_occurs=99
        )
    )
    search_traveler: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SearchTraveler",
            type="Element",
            help="Provider: ACH,MCH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: str = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            help="A wrapper for all the information regarding each of the Optional Services. Provider: 1G,1V,1P,1J,ACH.",
        )
    )
    remark: str = field(
        default=None,
        metadata=dict(
            name="Remark",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH,MCH.",
        )
    )
    rows: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Rows",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    payment_restriction: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PaymentRestriction",
            type="Element",
            help="Provider: MCH-Information regarding valid payment types, if restrictions apply(supplier specific)",
            min_occurs=0,
            max_occurs=999
        )
    )
    seat_information: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SeatInformation",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    copyright: str = field(
        default=None,
        metadata=dict(
            name="Copyright",
            type="Element",
            help="Copyright text applicable for some seat content. Providers: 1G, 1V, 1P, 1J,ACH",
        )
    )
    group_seat_price: str = field(
        default=None,
        metadata=dict(
            name="GroupSeatPrice",
            type="Attribute",
            help="Provider: 1G,1V-Seat price for the all passengers traveling together only when supplier provides group flat fee.",
        )
    )


@dataclass
class AirExchangeMultiQuoteReq(BaseAirExchangeMultiQuoteReq):
    """
    Request multiple quotes for the exchange of an itinerary. 1P transactions only
    """

    type: str = field(
        default="Summary",
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Type choices are 'Detail' or 'Summary' Default will be Summary",
        )
    )


@dataclass
class AirExchangeQuoteReq(BaseAirExchangeQuoteReq):
    """
    Request to quote the exchange of an itinerary
    """

    pass


@dataclass
class AirPriceReq(BaseAirPriceReq):
    """
    Request to price an itinerary in one to many ways. Pricing commands can be specified globally, or specifically per command.
    """

    pass


@dataclass
class AirPriceRsp(BaseAirPriceRsp):
    pass


@dataclass
class AirRepriceReq(AirBaseReq):
    """
    Request to reprice a solution.
    """

    air_reservation_locator_code: str = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            help=None,
        )
    )
    air_pricing_solution: str = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help=None,
            required=True
        )
    )
    fare_rule_type: str = field(
        default="none",
        metadata=dict(
            name="FareRuleType",
            type="Attribute",
            help=None,
        )
    )
    ignore_availability: str = field(
        default="false",
        metadata=dict(
            name="IgnoreAvailability",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AirSearchRsp(BaseAvailabilitySearchRsp):
    """
    Base Response for Air Search
    """

    fare_note_list: str = field(
        default=None,
        metadata=dict(
            name="FareNoteList",
            type="Element",
            help=None,
        )
    )
    expert_solution_list: str = field(
        default=None,
        metadata=dict(
            name="ExpertSolutionList",
            type="Element",
            help=None,
        )
    )
    route_list: str = field(
        default=None,
        metadata=dict(
            name="RouteList",
            type="Element",
            help=None,
        )
    )
    alternate_route_list: str = field(
        default=None,
        metadata=dict(
            name="AlternateRouteList",
            type="Element",
            help=None,
        )
    )
    alternate_location_distance_list: str = field(
        default=None,
        metadata=dict(
            name="AlternateLocationDistanceList",
            type="Element",
            help=None,
        )
    )
    fare_info_message: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FareInfoMessage",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    rail_segment_list: str = field(
        default=None,
        metadata=dict(
            name="RailSegmentList",
            type="Element",
            help=None,
        )
    )
    rail_journey_list: str = field(
        default=None,
        metadata=dict(
            name="RailJourneyList",
            type="Element",
            help=None,
        )
    )
    rail_fare_note_list: str = field(
        default=None,
        metadata=dict(
            name="RailFareNoteList",
            type="Element",
            help=None,
        )
    )
    rail_fare_idlist: str = field(
        default=None,
        metadata=dict(
            name="RailFareIDList",
            type="Element",
            help=None,
        )
    )
    rail_fare_list: str = field(
        default=None,
        metadata=dict(
            name="RailFareList",
            type="Element",
            help=None,
        )
    )
    rail_pricing_solution: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="RailPricingSolution",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_solution: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_price_point_list: str = field(
        default=None,
        metadata=dict(
            name="AirPricePointList",
            type="Element",
            help=None,
        )
    )


@dataclass
class AirTicketingReq(AirBaseReq):
    """
    Request to ticket a previously stored reservation.
    """

    air_reservation_locator_code: str = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            required=True
        )
    )
    air_pricing_info_ref: List["AirTicketingReq.str"] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            help="Provider: 1G,1V,1P,1J-Indicates air pricing infos to be ticketed.",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticketing_modifiers_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketingModifiersRef",
            type="Element",
            help="Provider: 1P,1J-Reference to a shared list of Ticketing Modifiers. This is supported for Worldspan and JAL providers only. When AirPricingInfoRef is used along with TicketingModifiersRef means that particular TicketingModifiers will to be applied while ticketing the Stored fare corresponding to the AirPricingInfo. Absence of AirPricingInfoRef means that particular TicketingModifiers will be applied to all Stored fares which are requested to be ticketed.",
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_code: str = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element",
            help=None,
        )
    )
    commission: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Commission",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=18
        )
    )
    detailed_billing_information: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element",
            help="Provider: 1G,1V.",
            min_occurs=0,
            max_occurs=999
        )
    )
    fax_details_information: str = field(
        default=None,
        metadata=dict(
            name="FaxDetailsInformation",
            type="Element",
            help="Provider: 1V.",
        )
    )
    air_ticketing_modifiers: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirTicketingModifiers",
            type="Element",
            help="Provider: 1G,1V,1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_segment_ticketing_modifiers: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentTicketingModifiers",
            type="Element",
            help="Provider: 1P,1J.",
            min_occurs=0,
            max_occurs=999
        )
    )
    return_info_on_fail: str = field(
        default="true",
        metadata=dict(
            name="ReturnInfoOnFail",
            type="Attribute",
            help=None,
        )
    )
    bulk_ticket: str = field(
        default="false",
        metadata=dict(
            name="BulkTicket",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J.",
        )
    )
    validate_spanish_residency: str = field(
        default="false",
        metadata=dict(
            name="ValidateSpanishResidency",
            type="Attribute",
            help="Provider: 1G - If set as true, Spanish Residency will be validated for Provisioned Customers.",
        )
    )

    @dataclass
    class AirPricingInfoRef:
        booking_traveler_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="BookingTravelerRef",
                type="Element",
                help=None,
                min_occurs=0,
                max_occurs=9
            )
        )
        key: str = field(
            default=None,
            metadata=dict(
                name="Key",
                type="Attribute",
                help=None,
                required=True
            )
        )


@dataclass
class AirUpsellSearchReq(AirBaseReq):
    """
    Request to search for Upsell Offers based on the Itinerary.
    """

    air_itinerary: str = field(
        default=None,
        metadata=dict(
            name="AirItinerary",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH-AirItinerary of the pricing request.",
            required=True
        )
    )
    air_price_result: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirPriceResult",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH-Result of AirPrice request. Upsell uses this to search for new offer.",
            min_occurs=1,
            max_occurs=16
        )
    )


@dataclass
class AirUpsellSearchRsp(BaseAirPriceRsp):
    """
    Response of Upsell Offers search for the given Itinerary.
    """

    pass


@dataclass
class AvailabilitySearchReq(AirSearchReq):
    """
    Availability Search request.
    """

    search_passenger: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SearchPassenger",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS passenger",
            min_occurs=0,
            max_occurs=18
        )
    )
    point_of_sale: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            help="Provider: ACH.",
            min_occurs=0,
            max_occurs=5
        )
    )
    return_brand_indicator: str = field(
        default="false",
        metadata=dict(
            name="ReturnBrandIndicator",
            type="Attribute",
            help="When set to “true”, the Brand Indicator can be returned in the availability search response. Provider: 1G, 1V, 1P, 1J, ACH",
        )
    )
    channel_id: str = field(
        default=None,
        metadata=dict(
            name="ChannelId",
            type="Attribute",
            help="A Channel ID is 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.",
            min_length=2.0,
            max_length=4.0
        )
    )
    nscc: str = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            help="Allows the agency to bypass/override the Search Control Console rule.",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class AvailabilitySearchRsp(BaseAvailabilitySearchRsp):
    pass


@dataclass
class BaseLowFareSearchReq(BaseAirSearchReq):
    """
    Base Low Fare Search Request
    """

    search_passenger: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SearchPassenger",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS passenger",
            min_occurs=1,
            max_occurs=18
        )
    )
    air_pricing_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
        )
    )
    enumeration: str = field(
        default=None,
        metadata=dict(
            name="Enumeration",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
        )
    )
    air_exchange_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirExchangeModifiers",
            type="Element",
            help="Provider: ACH.",
        )
    )
    flex_explore_modifiers: str = field(
        default=None,
        metadata=dict(
            name="FlexExploreModifiers",
            type="Element",
            help="This is the container for a set of modifiers which allow the user to perform a special kind of low fare search, depicted as flex explore, based on different parameters like Area, Zone, Country, State, Specific locations, Distance around the actual destination of the itinerary. Applicable for providers 1G,1V,1P.",
        )
    )
    pcc: str = field(
        default=None,
        metadata=dict(
            name="PCC",
            type="Element",
            help=None,
        )
    )
    fare_rules_filter_category: str = field(
        default=None,
        metadata=dict(
            name="FareRulesFilterCategory",
            type="Element",
            help=None,
        )
    )
    form_of_payment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help="Provider: 1P,1J",
            min_occurs=0,
            max_occurs=99
        )
    )
    enable_point_to_point_search: str = field(
        default="false",
        metadata=dict(
            name="EnablePointToPointSearch",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH-Indicates that low cost providers should be queried for top connection options and the results returned with the search.",
        )
    )
    enable_point_to_point_alternates: str = field(
        default="false",
        metadata=dict(
            name="EnablePointToPointAlternates",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH-Indicates that suggestions for alternate connection cities for low cost providers should be returned with the search.",
        )
    )
    max_number_of_expert_solutions: str = field(
        default="0",
        metadata=dict(
            name="MaxNumberOfExpertSolutions",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH-Indicates the Maximum Number of Expert Solutions to be returned from the Knowledge Base for the provided search criteria",
        )
    )
    solution_result: str = field(
        default="false",
        metadata=dict(
            name="SolutionResult",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH-Indicates whether the response will contain Solution result (AirPricingSolution) or Non Solution Result (AirPricingPoints). The default value is false. This attribute cannot be combined with EnablePointToPointSearch, EnablePointToPointAlternates and MaxNumberOfExpertSolutions.",
        )
    )
    prefer_complete_itinerary: str = field(
        default="true",
        metadata=dict(
            name="PreferCompleteItinerary",
            type="Attribute",
            help="Provider: ACH-This attribute is only supported for ACH .It works in conjunction with the @SolutionResult flag",
        )
    )
    meta_option_identifier: str = field(
        default=None,
        metadata=dict(
            name="MetaOptionIdentifier",
            type="Attribute",
            help="Invoke Meta Search. Valid values are 00 to 99, or D for the default meta search configuration. When Meta Search not requested, normal LowFareSearch applies. Supported Providers; 1g/1v/1p/1j",
            min_length=1.0,
            max_length=2.0
        )
    )
    return_upsell_fare: str = field(
        default="false",
        metadata=dict(
            name="ReturnUpsellFare",
            type="Attribute",
            help="When set to “true”, Upsell information will be returned in the shop response. Provider supported : 1G, 1V, 1P, 1J",
        )
    )
    include_fare_info_messages: str = field(
        default="false",
        metadata=dict(
            name="IncludeFareInfoMessages",
            type="Attribute",
            help="Set to True to return FareInfoMessageList. Providers supported: 1G/1V/1P/1J",
        )
    )
    return_branded_fares: str = field(
        default="true",
        metadata=dict(
            name="ReturnBrandedFares",
            type="Attribute",
            help="When ReturnBrandedFares is set to “false”, Rich Content and Branding will not be returned in the shop response. When ReturnBrandedFares it is set to “true” or is not sent, Rich Content and Branding will be returned in the shop response. Provider: 1P/1J/ACH.",
        )
    )
    multi_gdssearch: str = field(
        default="false",
        metadata=dict(
            name="MultiGDSSearch",
            type="Attribute",
            help="A 'true' value indicates MultiGDSSearch. Specific provisioning is required.",
        )
    )
    return_mm: str = field(
        default="false",
        metadata=dict(
            name="ReturnMM",
            type="Attribute",
            help="If this attribute is set to “true”, Fare Control Manager processing will be invoked.",
        )
    )
    check_obfees: str = field(
        default=None,
        metadata=dict(
            name="CheckOBFees",
            type="Attribute",
            help="A flag to return fees for ticketing and for various forms of payment. The default is “TicketingOnly” and will return only ticketing fees. The value “All” will return ticketing fees and the applicable form of payment fees for the form of payment information specified in the request. “FOPOnly” will return the applicable form of payment fees for the form of payment information specified in the request. Form of payment fees are never included in the total unless specific card details are in the request.Provider notes:ACH - CheckOBFees is valid only for LowFareSearch. The valid values are “All”, “TicketingOnly” and “None” and the default value is “None”. 1P/1J -The valid values are “All”, “None” and “TicketingOnly”.1G – All four values are supported.1V/RCH – CheckOBFees are not supported.”",
        )
    )
    nscc: str = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            help="1 to 3 numeric that defines a Search Control Console filter.This attribute is used to override that filter.",
            min_length=1.0,
            max_length=3.0
        )
    )
    fare_info_rules: str = field(
        default="false",
        metadata=dict(
            name="FareInfoRules",
            type="Attribute",
            help="Returns ChangePenalty and CancelPenalty values at the FareInfo level. If FareRulesFilterCategory is sent FareRulesFilter will be returned at FareInfo level. Provider: 1G/1V.",
        )
    )


@dataclass
class ScheduleSearchReq(AirSearchReq):
    """
    Schedule Search request
    """

    pass


@dataclass
class LowFareSearchAsynchReq(BaseLowFareSearchReq):
    """
    Asynchronous Low Fare Search request.
    """

    air_search_asynch_modifiers: str = field(
        default=None,
        metadata=dict(
            name="AirSearchAsynchModifiers",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH.",
        )
    )


@dataclass
class LowFareSearchAsynchRsp(AirSearchRsp):
    """
    Asynchronous Low Fare Search Response contains only the 1st Provider response unless time out occurs.
    """

    async_provider_specific_response: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AsyncProviderSpecificResponse",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    brand_list: str = field(
        default=None,
        metadata=dict(
            name="BrandList",
            type="Element",
            help=None,
        )
    )
    search_id: str = field(
        default=None,
        metadata=dict(
            name="SearchId",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH-Indicates the Search Id of the LFS search",
            required=True
        )
    )
    currency_type: str = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH-Specifies the default Currency Type in the response.",
            length=3
        )
    )


@dataclass
class LowFareSearchReq(BaseLowFareSearchReq):
    """
    Low Fare Search request.
    """

    policy_reference: str = field(
        default=None,
        metadata=dict(
            name="PolicyReference",
            type="Attribute",
            help="This attribute will be used to pass in a value on the request which would be used to link to a ‘Policy Group’ in a policy engine external to UAPI.",
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class LowFareSearchRsp(AirSearchRsp):
    """
    Low Fare Search Response
    """

    brand_list: str = field(
        default=None,
        metadata=dict(
            name="BrandList",
            type="Element",
            help=None,
        )
    )
    currency_type: str = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH.",
            required=True,
            length=3
        )
    )


@dataclass
class RetrieveLowFareSearchRsp(AirSearchRsp):
    """
    Low Fare Search Asynchronous Result response.
    """

    async_provider_specific_response: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AsyncProviderSpecificResponse",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH-Identifies pending responses from a specific provider using MoreResults attribute",
            min_occurs=0,
            max_occurs=999
        )
    )
    brand_list: str = field(
        default=None,
        metadata=dict(
            name="BrandList",
            type="Element",
            help=None,
        )
    )
    currency_type: str = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            help="Provider: 1G,1V,1P,1J,ACH.",
            length=3
        )
    )


@dataclass
class ScheduleSearchRsp(AirSearchRsp):
    """
    Schedule Search response
    """

    pass