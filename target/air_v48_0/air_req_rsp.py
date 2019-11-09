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

    provider_reservation_info: "AirExchangeEligibilityReq.ProviderReservationInfo" = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderReservationInfo",
            "type": "Element",
            "help": "Provider:1P - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged",
        },
    )
    type: str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "help": 'Type choices are "Detail" or "Summary" Default will be Summary',
        },
    )

    @dataclass
    class ProviderReservationInfo:
        pass


@dataclass
class AirExchangeEligibilityRsp(BaseRsp):
    exchange_eligibility_info: ExchangeEligibilityInfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "ExchangeEligibilityInfo",
            "type": "Element",
        },
    )


@dataclass
class AirExchangeQuoteRsp(BaseRsp):
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketNumber",
            "type": "Element",
        },
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirPricingSolution",
            "type": "Element",
            "help": "Provider: 1G/1V/1P/1S/1A.",
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
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "HostToken",
            "type": "Element",
            "help": "Encrypted data from the host. Required to send the HostToken from the AirExchangeQuoteRsp in the AirExchangeReq. Providers ACH/1G/1V/1P.",
        },
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareRule",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )


@dataclass
class AirExchangeReq(BaseReq):
    """
    Request to exchange an itinerary
    """

    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "help": "Identifies the PNR locator code. Providers ACH/1G/1V/1P",
        },
    )
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketNumber",
            "type": "Element",
        },
    )
    specific_seat_assignment: List[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "help": "Identifies the standard seat. Providers ACH/1G/1V/1P",
        },
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirPricingSolution",
            "type": "Element",
            "help": "Providers ACH/1G/1V/1P.",
        },
    )
    air_exchange_modifiers: AirExchangeModifiers = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    air_exchange_bundle_total: AirExchangeBundleTotal = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
            "help": "Provider: 1G/1V/1P/1S/1A.",
        },
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirExchangeBundle",
            "type": "Element",
            "help": "Bundle exchange, pricing, and penalty information. Providers ACH/1G/1V/1P.",
        },
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "HostToken",
            "type": "Element",
            "help": "Encrypted data from the host. Required to send the HostToken from the AirExchangeQuoteRsp in the AirExchangeReq. Providers ACH/1G/1V/1P",
        },
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    form_of_payment: FormOfPayment = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "help": "Form of Payment for any additional collection charges for the Exchange. For ACH, most carriers will only allow refund amounts to the original form of payment. Providers ACH/1G/1V/1P",
        },
    )
    form_of_payment_ref: FormOfPaymentRef = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "help": "Provider: ACH-Universal Record reference to Form of Payment for any Additional Collection charges or Refund due for the itinerary exchange",
        },
    )
    ssrinfo: List[Ssrinfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SSRInfo",
            "type": "Element",
            "help": "Providers ACH, 1G, 1V, 1P.",
        },
    )
    add_svc: AddSvc = field(
        default=None,
        metadata={
            "name": "AddSvc",
            "type": "Element",
            "help": "1P - Add SVC segments to collect additional fee",
        },
    )
    return_reservation: bool = field(
        default="false",
        metadata={
            "name": "ReturnReservation",
            "type": "Attribute",
            "help": "Provider: ACH.",
        },
    )


@dataclass
class AirExchangeRsp(BaseRsp):
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketNumber",
            "type": "Element",
        },
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BookingTraveler",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    air_reservation: TypeAirReservationWithFop = field(
        default=None,
        metadata={
            "name": "AirReservation",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    exchange_failure_info: List[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ExchangeFailureInfo",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )


@dataclass
class AirExchangeTicketingReq(BaseReq):
    """
    Request to ticket an exchanged itinerary. Providers 1G, 1V, 1P.
    """

    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "help": "Identifies the PNR to ticket. Providers 1G, 1V, 1P.",
        },
    )
    ticket_number: TicketNumber = field(
        default=None,
        metadata={
            "required": True,
            "name": "TicketNumber",
            "type": "Element",
            "help": "Ticket number to reissue. Providers 1G, 1V, 1P.",
        },
    )
    ticketing_modifiers_ref: List[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketingModifiersRef",
            "type": "Element",
            "help": "Provider: 1P-Reference to a shared list of Ticketing Modifiers. This is supported for Worldspan provider only. When AirPricingInfoRef is used along with TicketingModifiersRef means that particular TicketingModifiers will to be applied while ticketing the Stored fare corresponding to the AirPricingInfo. Absence of AirPricingInfoRef means that particular TicketingModifiers will be applied to all Stored fares which are requested to be ticketed.",
        },
    )
    waiver_code: WaiverCode = field(
        default=None, metadata={"name": "WaiverCode", "type": "Element"}
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "DetailedBillingInformation",
            "type": "Element",
            "help": "Providers 1G, 1V, 1P.",
        },
    )
    air_ticketing_modifiers: List[AirTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirTicketingModifiers",
            "type": "Element",
            "help": "Provider: 1G,1V,1P.",
        },
    )
    bulk_ticket: bool = field(
        default="false",
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
            "help": "Providers 1G, 1V, 1P.",
        },
    )
    change_fee_on_ticket: bool = field(
        default="true",
        metadata={
            "name": "ChangeFeeOnTicket",
            "type": "Attribute",
            "help": "Applies the change fee/penalty to the original form of payment. Providers: 1V",
        },
    )


@dataclass
class AirExchangeTicketingRsp(BaseRsp):
    """
    Response to reissue a ticket.
    """

    air_solution_changed_info: AirSolutionChangedInfo = field(
        default=None,
        metadata={"name": "AirSolutionChangedInfo", "type": "Element"},
    )
    etr: Etr = field(
        default=None,
        metadata={
            "name": "ETR",
            "type": "Element",
            "help": "Provider 1G, 1V, 1P.",
        },
    )
    ticket_failure_info: TicketFailureInfo = field(
        default=None,
        metadata={
            "name": "TicketFailureInfo",
            "type": "Element",
            "help": "Provider 1G, 1V, 1P.",
        },
    )
    detailed_billing_information: DetailedBillingInformation = field(
        default=None,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
            "help": "Providers 1G, 1V, 1P.",
        },
    )


@dataclass
class AirFareDisplayReq(BaseReq):
    """
    Request to display a tariff for based on origin, destination, and other options
    """

    fare_type: List[FareType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "FareType",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    passenger_type: List[TypePassengerType] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "PassengerType",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "BookingCode",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    include_addl_booking_code_info: IncludeAddlBookingCodeInfo = field(
        default=None,
        metadata={
            "name": "IncludeAddlBookingCodeInfo",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    fare_basis: FareBasis = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 10,
            "name": "Carrier",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "AccountCode",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    contract_code: ContractCode = field(
        default=None,
        metadata={
            "name": "ContractCode",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )
    air_fare_display_modifiers: AirFareDisplayModifiers = field(
        default=None,
        metadata={
            "name": "AirFareDisplayModifiers",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "PointOfSale",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )
    air_fare_display_rule_key: AirFareDisplayRuleKey = field(
        default=None,
        metadata={
            "name": "AirFareDisplayRuleKey",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    origin: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Origin",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    destination: TypeIatacode = field(
        default=None,
        metadata={
            "required": True,
            "name": "Destination",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderCode",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    include_mile_route_information: TypeMileOrRouteBasedFare = field(
        default=None,
        metadata={
            "name": "IncludeMileRouteInformation",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J-Used to request Mile/Route Information in follow on (Mile, Route, Both)",
        },
    )
    un_saleable_fares_only: bool = field(
        default=None,
        metadata={
            "name": "UnSaleableFaresOnly",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J-Used to request unsaleable fares only also known as place of sale fares.",
        },
    )
    channel_id: str = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "help": "A Channel ID is 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.",
        },
    )
    nscc: str = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "help": "1 to 3 numeric that define a Search Control Console filter.This attribute is used to override that filter.",
        },
    )
    return_mm: bool = field(
        default="false",
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
            "help": "If this attribute is set to true, Fare Control Manager processing will be invoked.",
        },
    )


@dataclass
class AirFareDisplayRsp(BaseRsp):
    """
    Response to an AirFareDisplayReq
    """

    fare_display: List[FareDisplay] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareDisplay",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )


@dataclass
class AirFareRulesReq(BaseReq):
    """
    Request to display the full text fare rules.
    """

    air_fare_rules_modifier: AirFareRulesModifier = field(
        default=None,
        metadata={
            "name": "AirFareRulesModifier",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )
    fare_rules_filter_category: List[
        "AirFareRulesReq.FareRulesFilterCategory"
    ] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 16,
            "name": "FareRulesFilterCategory",
            "type": "Element",
            "help": "Structured Fare Rules Filter if requested will return rules for requested categories in the response. Applicable for providers 1G, 1V.",
        },
    )
    air_reservation_selector: "AirFareRulesReq.AirReservationSelector" = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirReservationSelector",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH-Parameters to use for a fare rule lookup associated with an Air Reservation Locator Code",
        },
    )
    fare_rule_lookup: FareRuleLookup = field(
        default=None,
        metadata={
            "name": "FareRuleLookup",
            "type": "Element",
            "help": "Used to look up fare rules based on the origin, destination, and carrier of the air segment, the fare basis code and the provider code. Providers: 1P, 1J.",
        },
    )
    fare_rule_key: List[FareRuleKey] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "FareRuleKey",
            "type": "Element",
            "help": "Used to look up fare rules based on a fare rule key. Providers: 1G, 1V, 1P, 1J, ACH.",
        },
    )
    air_fare_display_rule_key: AirFareDisplayRuleKey = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirFareDisplayRuleKey",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    fare_rule_type: TypeFareRuleType = field(
        default="long",
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )

    @dataclass
    class AirReservationSelector:
        fare_info_ref: List[FareInfoRef] = field(
            default_factory=list,
            metadata={
                "min_occurs": 0,
                "max_occurs": 999,
                "name": "FareInfoRef",
                "type": "Element",
            },
        )
        air_reservation_locator_code: TypeLocatorCode = field(
            default=None,
            metadata={
                "required": True,
                "name": "AirReservationLocatorCode",
                "type": "Attribute",
                "help": "The Air Reservation locator code which is an unique identifier for the reservation",
            },
        )

    @dataclass
    class FareRulesFilterCategory:
        fare_info_ref: str = field(
            default=None,
            metadata={
                "name": "FareInfoRef",
                "type": "Attribute",
                "help": "Key reference for multiple fare rule",
            },
        )


@dataclass
class AirFareRulesRsp(BaseRsp):
    """
    Response to an AirFareRuleReq.
    """

    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FareRule",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )


@dataclass
class AirMerchandisingDetailsReq(BaseReq):
    """
    Request to retrieve brand details and optional services included in the brand
    """

    merchandising_details: MerchandisingDetails = field(
        default=None,
        metadata={
            "required": True,
            "name": "MerchandisingDetails",
            "type": "Element",
        },
    )
    optional_service_modifiers: OptionalServiceModifiers = field(
        default=None,
        metadata={
            "required": True,
            "name": "OptionalServiceModifiers",
            "type": "Element",
        },
    )
    merchandising_availability_details: MerchandisingAvailabilityDetails = field(
        default=None,
        metadata={
            "required": True,
            "name": "MerchandisingAvailabilityDetails",
            "type": "Element",
        },
    )


@dataclass
class AirMerchandisingDetailsRsp(BaseRsp):
    """
    Response for retrieved brand details and optional services included in them
    """

    optional_services: OptionalServices = field(
        default=None, metadata={"name": "OptionalServices", "type": "Element"}
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
    unassociated_booking_code_list: "AirMerchandisingDetailsRsp.UnassociatedBookingCodeList" = field(
        default=None,
        metadata={
            "name": "UnassociatedBookingCodeList",
            "type": "Element",
            "help": "Lists classes of service by segment sent in the request which are not associated to a brand.",
        },
    )

    @dataclass
    class UnassociatedBookingCodeList:
        applicable_segment: List[TypeApplicableSegment] = field(
            default_factory=list,
            metadata={
                "min_occurs": 0,
                "max_occurs": 99,
                "name": "ApplicableSegment",
                "type": "Element",
            },
        )


@dataclass
class AirMerchandisingOfferAvailabilityReq(BaseReq):
    """
    Check with the supplier whether or not the reservation or air solution supports any merchandising offerings.
    """

    agency_sell_info: AgencySellInfo = field(
        default=None,
        metadata={
            "name": "AgencySellInfo",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    air_solution: AirSolution = field(
        default=None,
        metadata={
            "name": "AirSolution",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    host_reservation: List[HostReservation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "HostReservation",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    offer_availability_modifiers: List[OfferAvailabilityModifiers] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "OfferAvailabilityModifiers",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    merchandising_pricing_modifiers: MerchandisingPricingModifiers = field(
        default=None,
        metadata={
            "name": "MerchandisingPricingModifiers",
            "type": "Element",
            "help": "Used to provide additional pricing modifiers. Provider:ACH.",
        },
    )


@dataclass
class AirMerchandisingOfferAvailabilityRsp(BaseRsp):
    """
    Contains the merchandising offerings for the given passenger and itinerary.
    """

    air_solution: AirSolution = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirSolution",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    remark: Remark = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    optional_services: OptionalServices = field(
        default=None, metadata={"name": "OptionalServices", "type": "Element"}
    )
    embargo_list: EmbargoList = field(
        default=None, metadata={"name": "EmbargoList", "type": "Element"}
    )


@dataclass
class AirPrePayReq(BaseReq):
    """
    Flight Pass Request.
    """

    list_search: "AirPrePayReq.ListSearch" = field(
        default=None,
        metadata={
            "required": True,
            "name": "ListSearch",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    pre_pay_retrieve: "AirPrePayReq.PrePayRetrieve" = field(
        default=None,
        metadata={
            "required": True,
            "name": "PrePayRetrieve",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )

    @dataclass
    class PrePayRetrieve:
        id: TypeCardNumber = field(
            default=None,
            metadata={
                "required": True,
                "name": "Id",
                "type": "Attribute",
                "help": "Pre pay id to retrieved,example flight pass number",
            },
        )
        type: str = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "help": "Pre pay id type,example 'FlightPass'",
            },
        )

    @dataclass
    class ListSearch:
        person_name_search: PersonNameSearch = field(
            default=None,
            metadata={
                "required": True,
                "name": "PersonNameSearch",
                "type": "Element",
                "help": "Customer name detail for searching flight pass content.",
            },
        )
        loyalty_card: List[LoyaltyCard] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "LoyaltyCard",
                "type": "Element",
                "help": "Customer loyalty card for searching flight pass content.",
            },
        )
        start_from_result: TypeStartFromResult = field(
            default=None,
            metadata={
                "required": True,
                "name": "StartFromResult",
                "type": "Attribute",
                "help": "Start index of the section of flight pass numbers that is being requested.",
            },
        )
        max_results: TypeMaxResults = field(
            default=None,
            metadata={
                "required": True,
                "name": "MaxResults",
                "type": "Attribute",
                "help": "Max Number of Flight Passes being requested for.",
            },
        )


@dataclass
class AirPrePayRsp(BaseRsp):
    """
    Flight Pass Response.
    """

    pre_pay_profile_info: List[PrePayProfileInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "PrePayProfileInfo",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    max_results: TypeMaxResults = field(
        default=None,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "help": "Provider: ACH-Max Number of Flight Passes being returned.",
        },
    )
    more_indicator: bool = field(
        default=None,
        metadata={
            "name": "MoreIndicator",
            "type": "Attribute",
            "help": "Provider: ACH-Indicates if there are more flight passes to be offered",
        },
    )
    more_data_start_index: str = field(
        default=None,
        metadata={
            "name": "MoreDataStartIndex",
            "type": "Attribute",
            "help": "Provider: ACH-Indicates start index of the next flight Passes",
        },
    )


@dataclass
class AirRefundQuoteReq(BaseReq):
    """
    Request to quote a refund for an itinerary
    """

    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketNumber",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    tcrnumber: List[TypeTcrnumber] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TCRNumber",
            "type": "Element",
            "help": "Provider: ACH-The identifying number for a Ticketless Air Reservation",
        },
    )
    air_refund_modifiers: AirRefundModifiers = field(
        default=None,
        metadata={
            "name": "AirRefundModifiers",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "HostToken",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    provider_reservation_info: List[
        "AirRefundQuoteReq.ProviderReservationInfo"
    ] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ProviderReservationInfo",
            "type": "Element",
            "help": "Provider: 1P - Represents a valid Provider Reservation/PNR whose itinerary is to be requested",
        },
    )
    ignore: bool = field(
        default="false",
        metadata={
            "name": "Ignore",
            "type": "Attribute",
            "help": "Provider: ACH.",
        },
    )

    @dataclass
    class ProviderReservationInfo:
        pass


@dataclass
class AirRefundQuoteRsp(BaseRsp):
    air_refund_bundle: List[AirRefundBundle] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirRefundBundle",
            "type": "Element",
        },
    )
    tcrrefund_bundle: List[TcrrefundBundle] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TCRRefundBundle",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )


@dataclass
class AirRefundReq(BaseReq):
    """
    Request to refund an itinerary for the amount previously quoted
    """

    air_refund_bundle: List[AirRefundBundle] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirRefundBundle",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    tcrrefund_bundle: List[TcrrefundBundle] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TCRRefundBundle",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    air_refund_modifiers: AirRefundModifiers = field(
        default=None,
        metadata={"name": "AirRefundModifiers", "type": "Element"},
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 9,
            "name": "Commission",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    form_of_payment: FormOfPayment = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "help": "Provider: ACH-Form of Payment for any Additional Collection charges for the Refund.",
        },
    )


@dataclass
class AirRefundRsp(BaseRsp):
    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ETR",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    tcr: List[Tcr] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TCR",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    refund_failure_info: List[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RefundFailureInfo",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )


@dataclass
class AirRepriceRsp(BaseRsp):
    air_pricing_solution: AirPricingSolution = field(
        default=None,
        metadata={
            "required": True,
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


@dataclass
class AirRetrieveDocumentReq(BaseReq):
    """
    Retrieve the post booking information for a PNR. ETRs will be returned for standard carriers. TCRs will be returned for Ticketless carriers. If the locator is send on a standard carrier, all ETRs will be retrieved.
    """

    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketNumber",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    tcrnumber: List[TypeTcrnumber] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TCRNumber",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J-The identifying number for a Ticketless Air Reservation.",
        },
    )
    return_restrictions: bool = field(
        default=None,
        metadata={
            "name": "ReturnRestrictions",
            "type": "Attribute",
            "help": "Will return a response which includes a set of restrictions associated with the document.",
        },
    )
    return_pricing: bool = field(
        default=None,
        metadata={
            "name": "ReturnPricing",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J-Will return a response which includes the pricing associated with the ETR.",
        },
    )
    retrieve_mco: bool = field(
        default=None,
        metadata={
            "name": "RetrieveMCO",
            "type": "Attribute",
            "help": "When true, returns MCO Information. The default value is false.",
        },
    )


@dataclass
class AirRetrieveDocumentRsp(BaseRsp):
    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ETR",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    mco: List[Mco] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "MCO",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    tcr: List[Tcr] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TCR",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    document_failure_info: List[TypeFailureInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "DocumentFailureInfo",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J-Will be optionally returned if there are duplicate ticket numbers.",
        },
    )
    service_fee_info: List[ServiceFeeInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "ServiceFeeInfo",
            "type": "Element",
            "help": "Provider: 1G,1V",
        },
    )
    universal_record_locator_code: TypeLocatorCode = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J-Represents a valid Universal Record locator code.",
        },
    )


@dataclass
class AirTicketingRsp(BaseRsp):
    """
    Response to ticket a previously stored reservation.
    """

    air_solution_changed_info: AirSolutionChangedInfo = field(
        default=None,
        metadata={"name": "AirSolutionChangedInfo", "type": "Element"},
    )
    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ETR",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    ticket_failure_info: List[TicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketFailureInfo",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "DetailedBillingInformation",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )


@dataclass
class AirVoidDocumentReq(BaseReq):
    """
    Request to void all previously issued tickets for the PNR.
    """

    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )
    void_document_info: List[VoidDocumentInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "VoidDocumentInfo",
            "type": "Element",
            "help": "Provider: 1G,1V-All tickets that belong to this PNR must be enumerated here. Voiding only some tickets of a multi-ticket PNR not currently supported.",
        },
    )
    show_etr: bool = field(
        default="false",
        metadata={
            "name": "ShowETR",
            "type": "Attribute",
            "help": "Provider: 1G,1V-If set as true, response will display the detailed ETR for successfully voided E-Tickets.",
        },
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "help": "Provider: 1G,1V-Provider code of a specific host.",
        },
    )
    provider_locator_code: str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "help": "Provider: 1G,1V-Contains the locator of the host reservation.",
        },
    )
    validate_spanish_residency: bool = field(
        default="false",
        metadata={
            "name": "ValidateSpanishResidency",
            "type": "Attribute",
            "help": "Provider: 1G - If set as true, Spanish Residency will be validated for Provisioned Customers.",
        },
    )


@dataclass
class AirVoidDocumentRsp(BaseRsp):
    """
    Result of void ticket request. Includes ticket number of voided tickets and air segments with updated status.
    """

    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ETR",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )
    void_result_info: List[VoidResultInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "VoidResultInfo",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )


@dataclass
class BaseAirExchangeMultiQuoteReq(BaseCoreReq):
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketNumber",
            "type": "Element",
        },
    )
    provider_reservation_info: "BaseAirExchangeMultiQuoteReq.ProviderReservationInfo" = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "help": "Provider: 1P - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged",
        },
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "AirPricingSolution",
            "type": "Element",
        },
    )
    repricing_modifiers: RepricingModifiers = field(
        default=None,
        metadata={"name": "RepricingModifiers", "type": "Element"},
    )
    original_itinerary_details: OriginalItineraryDetails = field(
        default=None,
        metadata={"name": "OriginalItineraryDetails", "type": "Element"},
    )
    override_pcc: OverridePcc = field(
        default=None, metadata={"name": "OverridePCC", "type": "Element"}
    )

    @dataclass
    class ProviderReservationInfo:
        pass


@dataclass
class BaseAirExchangeQuoteReq(BaseCoreReq):
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketNumber",
            "type": "Element",
        },
    )
    provider_reservation_info: "BaseAirExchangeQuoteReq.ProviderReservationInfo" = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "help": "Provider: 1G/1V/1P/ACH - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged",
        },
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 2,
            "name": "AirPricingSolution",
            "type": "Element",
        },
    )
    air_exchange_modifiers: AirExchangeModifiers = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "HostToken",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FormOfPayment",
            "type": "Element",
            "help": "Provider: ACH-This would allow a user to see the fees if they are changing from one Form Of Payment to other .",
        },
    )
    repricing_modifiers: RepricingModifiers = field(
        default=None,
        metadata={"name": "RepricingModifiers", "type": "Element"},
    )
    original_itinerary_details: OriginalItineraryDetails = field(
        default=None,
        metadata={"name": "OriginalItineraryDetails", "type": "Element"},
    )
    pcc: Pcc = field(default=None, metadata={"name": "PCC", "type": "Element"})
    fare_rule_type: TypeFareRuleType = field(
        default="none",
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
            "help": "Provider: ACH.",
        },
    )

    @dataclass
    class ProviderReservationInfo:
        pass


@dataclass
class BaseAirPriceReq(BaseCoreReq):
    air_itinerary: AirItinerary = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirItinerary",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    air_pricing_modifiers: AirPricingModifiers = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 18,
            "name": "SearchPassenger",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS passenger",
        },
    )
    air_pricing_command: List[AirPricingCommand] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 16,
            "name": "AirPricingCommand",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "help": "Provider: ACH,1P,1J",
        },
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FormOfPayment",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    pcc: Pcc = field(default=None, metadata={"name": "PCC", "type": "Element"})
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "SSR",
            "type": "Element",
            "help": "Special Service Request for GST tax details. Provider: ACH",
        },
    )
    check_obfees: str = field(
        default=None,
        metadata={
            "name": "CheckOBFees",
            "type": "Attribute",
            "help": "A flag to return fees for ticketing and for various forms of payment. The default is “TicketingOnly” and will return only ticketing fees. The value “All” will return ticketing fees and the applicable form of payment fees for the form of payment information specified in the request. “FOPOnly” will return the applicable form of payment fees for the form of payment information specified in the request. Form of payment fees are never included in the total unless specific card details are in the request.Provider notes:ACH - CheckOBFees is valid only for LowFareSearch. The valid values are “All”, “TicketingOnly” and “None” and the default value is “None”. 1P/1J -The valid values are “All”, “None” and “TicketingOnly”.1G – All four values are supported.1V/RCH – CheckOBFees are not supported.”",
        },
    )
    fare_rule_type: TypeFareRuleType = field(
        default="none",
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "help": "Specifies the supplier/ vendor for vendor specific price requests",
        },
    )
    ticket_date: str = field(
        default=None,
        metadata={
            "name": "TicketDate",
            "type": "Attribute",
            "help": "YYYY-MM-DD Using a date in the past is a request for an historical fare",
        },
    )
    check_flight_details: bool = field(
        default="false",
        metadata={
            "name": "CheckFlightDetails",
            "type": "Attribute",
            "help": "To Include FlightDetails in Response set to “true” the Default value is “false”.",
        },
    )
    return_mm: bool = field(
        default="false",
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
            "help": "If this attribute is set to “true”, Fare Control Manager processing will be invoked.",
        },
    )
    nscc: str = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "help": "1 to 3 numeric that defines a Search Control Console filter.This attribute is used to override that filter.",
        },
    )
    split_pricing: bool = field(
        default="false",
        metadata={
            "name": "SplitPricing",
            "type": "Attribute",
            "help": "Indicates whether the AirSegments should be priced together or separately. Set ‘true’ for split pricing. Set ‘false’ for pricing together.SplitPricing is not supported with post book re-pricing.",
        },
    )
    ignore_availability: bool = field(
        default="false",
        metadata={
            "name": "IgnoreAvailability",
            "type": "Attribute",
            "help": "Provides a method of pricing a book itinerary with the lowest fare regardless of the availability for the class of service. Only for providers 1P/1J.",
        },
    )


@dataclass
class BaseAirPriceRsp(BaseRsp):
    air_itinerary: AirItinerary = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirItinerary",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    air_price_result: List[AirPriceResult] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 16,
            "name": "AirPriceResult",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )


@dataclass
class BaseAvailabilitySearchRsp(BaseSearchRsp):
    """
    Availability Search response
    """

    flight_details_list: FlightDetailsList = field(
        default=None, metadata={"name": "FlightDetailsList", "type": "Element"}
    )
    air_segment_list: AirSegmentList = field(
        default=None, metadata={"name": "AirSegmentList", "type": "Element"}
    )
    fare_info_list: FareInfoList = field(
        default=None, metadata={"name": "FareInfoList", "type": "Element"}
    )
    fare_remark_list: FareRemarkList = field(
        default=None, metadata={"name": "FareRemarkList", "type": "Element"}
    )
    air_itinerary_solution: List[AirItinerarySolution] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirItinerarySolution",
            "type": "Element",
        },
    )
    host_token_list: HostTokenList = field(
        default=None, metadata={"name": "HostTokenList", "type": "Element"}
    )
    apisrequirements_list: ApisrequirementsList = field(
        default=None,
        metadata={"name": "APISRequirementsList", "type": "Element"},
    )
    distance_units: TypeDistance = field(
        default=None, metadata={"name": "DistanceUnits", "type": "Attribute"}
    )


@dataclass
class BrandList:
    brand: List[Brand] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "Brand",
            "type": "Element",
        },
    )


@dataclass
class EmdissuanceReq(BaseReq):
    """
    Electronic Miscellaneous Document issuance request.Supported providers are 1V/1G/1P/1J
    """

    provider_reservation_detail: ProviderReservationDetail = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderReservationDetail",
            "type": "Element",
            "help": "PNR information for which EMD is going to be issued.",
        },
    )
    ticket_number: TicketNumber = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "help": "Ticket number for which EMD is going to be issued.Required for EMD-A issuance.",
        },
    )
    issuance_modifiers: IssuanceModifiers = field(
        default=None,
        metadata={
            "name": "IssuanceModifiers",
            "type": "Element",
            "help": "General modifiers related to EMD issuance.",
        },
    )
    selection_modifiers: SelectionModifiers = field(
        default=None,
        metadata={
            "name": "SelectionModifiers",
            "type": "Element",
            "help": "Modifiers related to selection of services during EMD issuance.",
        },
    )
    universal_record_locator_code: TypeLocatorCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "help": "Represents a valid Universal Record locator code.",
        },
    )
    show_details: bool = field(
        default="false",
        metadata={
            "name": "ShowDetails",
            "type": "Attribute",
            "help": "This attribute gives the control to request for complete information on Issued EMDs or minimal information.Requesting complete information leads to possible multiple supplier calls for fetching all the details.",
        },
    )
    issue_all_open_svc: bool = field(
        default="false",
        metadata={
            "name": "IssueAllOpenSVC",
            "type": "Attribute",
            "help": "Issues EMDS to all SVC segments. If it is true, TicketNumber and SVC segment reference need not be provided. Supported provider 1P.",
        },
    )


@dataclass
class EmdissuanceRsp(BaseRsp):
    """
    Electronic Miscellaneous Document issuance response.Supported providers are 1V/1G/1P/1J
    """

    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "EMDSummaryInfo",
            "type": "Element",
            "help": "List of EMDSummaryInfo elements to show minimal information in issuance response. Appears for ShowDetails=false in the request.This is the default behaviour.",
        },
    )
    emdinfo: List[Emdinfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "EMDInfo",
            "type": "Element",
            "help": "List of EMDInfo elements to show detailoed information in issuance response. Appears for ShowDetails=true in the request.",
        },
    )


@dataclass
class EmdretrieveReq(BaseReq):
    """
    Electronic Miscellaneous Document retrieve request.Supported providers are 1G/1V/1P/1J
    """

    list_retrieve: "EmdretrieveReq.ListRetrieve" = field(
        default=None,
        metadata={
            "required": True,
            "name": "ListRetrieve",
            "type": "Element",
            "help": "Provider: 1G/1V/1P/1J-Information required for retrieval of list of EMDs",
        },
    )
    detail_retrieve: "EmdretrieveReq.DetailRetrieve" = field(
        default=None,
        metadata={
            "required": True,
            "name": "DetailRetrieve",
            "type": "Element",
            "help": "Provider: 1G/1V/1P/1J-Information required for a detailed EMD retrieve",
        },
    )

    @dataclass
    class DetailRetrieve:
        provider_reservation_detail: ProviderReservationDetail = field(
            default=None,
            metadata={
                "name": "ProviderReservationDetail",
                "type": "Element",
                "help": "Provider reservation locator to be specified for display operation, if mentioned along woth the EMD number then synchronization of that EMD is performed considering the same to be associated with the mentioned PNR.",
            },
        )
        emdnumber: TypeEmdnumber = field(
            default=None,
            metadata={
                "required": True,
                "name": "EMDNumber",
                "type": "Element",
                "help": "EMD number to be specified for display operation. If mentioned along with provider reservation detail then synchronization of that EMD is performed considering the same to be associated with the mentioned PNR.",
            },
        )

    @dataclass
    class ListRetrieve:
        provider_reservation_detail: ProviderReservationDetail = field(
            default=None,
            metadata={
                "required": True,
                "name": "ProviderReservationDetail",
                "type": "Element",
                "help": "Provider reservation details to be provided to fetch list of EMDs associated with it.",
            },
        )


@dataclass
class EmdretrieveRsp(BaseRsp):
    """
    Electronic Miscellaneous Document list and detail retrieve response.Supported providers are 1G/1V/1P/1J
    """

    emdinfo: Emdinfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "EMDInfo",
            "type": "Element",
            "help": "Provider: 1G/1V/1P/1J.",
        },
    )
    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "EMDSummaryInfo",
            "type": "Element",
            "help": "Provider: 1G/1V/1P/1J.",
        },
    )


@dataclass
class FlightDetailsReq(BaseReq):
    """
    Request for the Flight Details of segments.
    """

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirSegment",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )


@dataclass
class FlightDetailsRsp(BaseRsp):
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "AirSegment",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    co2_emissions: List[Co2Emissions] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "CO2Emissions",
            "type": "Element",
        },
    )


@dataclass
class FlightInformationReq(BaseReq):
    """
    Request for the Flight Info of segments.
    """

    flight_info_criteria: List[FlightInfoCriteria] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "FlightInfoCriteria",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )


@dataclass
class FlightInformationRsp(BaseRsp):
    flight_info: List[FlightInfo] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "FlightInfo",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )


@dataclass
class FlightTimeTableReq(BaseSearchReq):
    """
    Request for Flight Time Table.
    """

    flight_time_table_criteria: FlightTimeTableCriteria = field(
        default=None,
        metadata={
            "required": True,
            "name": "FlightTimeTableCriteria",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )


@dataclass
class FlightTimeTableRsp(BaseSearchRsp):
    """
    Response for Flight Time Table.
    """

    flight_time_table_list: "FlightTimeTableRsp.FlightTimeTableList" = field(
        default=None,
        metadata={
            "name": "FlightTimeTableList",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )

    @dataclass
    class FlightTimeTableList:
        flight_time_detail: List[FlightTimeDetail] = field(
            default_factory=list,
            metadata={
                "min_occurs": 1,
                "max_occurs": 999,
                "name": "FlightTimeDetail",
                "type": "Element",
            },
        )


@dataclass
class RetrieveLowFareSearchReq(BaseReq):
    """
    Retrieve low fare search responses that were initiated by an asynchronous request.
    """

    search_id: TypeLowFareSearchId = field(
        default=None,
        metadata={
            "required": True,
            "name": "SearchId",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH-SearchID to be used for Asynchronous LowFareSearch Request",
        },
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "ProviderCode",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH-Provider code of a specific host",
        },
    )


@dataclass
class SearchSpecificAirSegment:
    departure_time: str = field(
        default=None,
        metadata={
            "required": True,
            "name": "DepartureTime",
            "type": "Attribute",
            "help": "The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
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
    segment_index: int = field(
        default=None,
        metadata={
            "name": "SegmentIndex",
            "type": "Attribute",
            "help": "The sequential AirSegment number that this segment connected to.",
        },
    )


@dataclass
class SeatMapReq(BaseReq):
    """
    Request a seat map for the give flight information
    """

    agency_sell_info: AgencySellInfo = field(
        default=None,
        metadata={
            "name": "AgencySellInfo",
            "type": "Element",
            "help": "Provider: ACH-Required if the user requesting the seat map is not the same agent authenticated in the request.",
        },
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "AirSegment",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH,MCH.",
        },
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "HostToken",
            "type": "Element",
            "help": "Provider: ACH-Required if the carrier has multiple adapters.",
        },
    )
    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SearchTraveler",
            "type": "Element",
            "help": "Provider: 1G,1V,ACH,MCH.",
        },
    )
    host_reservation: HostReservation = field(
        default=None,
        metadata={
            "name": "HostReservation",
            "type": "Element",
            "help": "Provider: ACH,MCH-Required when seat price is requested.",
        },
    )
    merchandising_pricing_modifiers: MerchandisingPricingModifiers = field(
        default=None,
        metadata={
            "name": "MerchandisingPricingModifiers",
            "type": "Element",
            "help": "Used to provide additional pricing options. Provider:ACH.",
        },
    )
    return_seat_pricing: bool = field(
        default=None,
        metadata={
            "required": True,
            "name": "ReturnSeatPricing",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH-When set to true the price of the seat will be returned if it exists.",
        },
    )
    return_branding_info: bool = field(
        default="false",
        metadata={
            "name": "ReturnBrandingInfo",
            "type": "Attribute",
            "help": "A value of true will return the BrandingInfo block in the response if applicable. A value of false will not return the BrandingInfo block in the response. Providers: 1G, 1V, 1P, 1J, ACH",
        },
    )


@dataclass
class SeatMapRsp(BaseRsp):
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "HostToken",
            "type": "Element",
            "help": "Provider: ACH,MCH.",
        },
    )
    cabin_class: CabinClass = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH,MCH.",
        },
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "AirSegment",
            "type": "Element",
            "help": "Provider: ACH,MCH.",
        },
    )
    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SearchTraveler",
            "type": "Element",
            "help": "Provider: ACH,MCH.",
        },
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "help": "A wrapper for all the information regarding each of the Optional Services. Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    remark: Remark = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH,MCH.",
        },
    )
    rows: List[Rows] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "Rows",
            "type": "Element",
        },
    )
    payment_restriction: List[PaymentRestriction] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "PaymentRestriction",
            "type": "Element",
            "help": "Provider: MCH-Information regarding valid payment types, if restrictions apply(supplier specific)",
        },
    )
    seat_information: List[SeatInformation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SeatInformation",
            "type": "Element",
        },
    )
    copyright: str = field(
        default=None,
        metadata={
            "name": "Copyright",
            "type": "Element",
            "help": "Copyright text applicable for some seat content. Providers: 1G, 1V, 1P, 1J,ACH",
        },
    )
    group_seat_price: TypeMoney = field(
        default=None,
        metadata={
            "name": "GroupSeatPrice",
            "type": "Attribute",
            "help": "Provider: 1G,1V-Seat price for the all passengers traveling together only when supplier provides group flat fee.",
        },
    )


@dataclass
class AirExchangeMultiQuoteReq(BaseAirExchangeMultiQuoteReq):
    """
    Request multiple quotes for the exchange of an itinerary. 1P transactions only
    """

    type: str = field(
        default="Summary",
        metadata={
            "name": "Type",
            "type": "Attribute",
            "help": 'Type choices are "Detail" or "Summary" Default will be Summary',
        },
    )


@dataclass
class AirExchangeMultiQuoteRsp(BaseRsp):
    air_segment_list: List[AirSegmentList] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentList",
            "type": "Element",
        },
    )
    brand_list: List[BrandList] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "BrandList",
            "type": "Element",
        },
    )
    air_exchange_mulit_quote_list: List[AirExchangeMulitQuoteList] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirExchangeMulitQuoteList",
            "type": "Element",
        },
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

    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata={"name": "AirReservationLocatorCode", "type": "Element"},
    )
    air_pricing_solution: AirPricingSolution = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirPricingSolution",
            "type": "Element",
        },
    )
    fare_rule_type: TypeFareRuleType = field(
        default="none", metadata={"name": "FareRuleType", "type": "Attribute"}
    )
    ignore_availability: bool = field(
        default="false",
        metadata={"name": "IgnoreAvailability", "type": "Attribute"},
    )


@dataclass
class AirSearchReq(BaseSearchReq):
    """
    Base Request for Air Search
    """

    point_of_commencement: PointOfCommencement = field(
        default=None,
        metadata={"name": "PointOfCommencement", "type": "Element"},
    )
    air_search_modifiers: AirSearchModifiers = field(
        default=None,
        metadata={"name": "AirSearchModifiers", "type": "Element"},
    )
    journey_data: JourneyData = field(
        default=None, metadata={"name": "JourneyData", "type": "Element"}
    )
    search_air_leg: List[SearchAirLeg] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 16,
            "name": "SearchAirLeg",
            "type": "Element",
        },
    )
    search_specific_air_segment: List[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "SearchSpecificAirSegment",
            "type": "Element",
        },
    )


@dataclass
class AirSearchRsp(BaseAvailabilitySearchRsp):
    """
    Base Response for Air Search
    """

    fare_note_list: FareNoteList = field(
        default=None, metadata={"name": "FareNoteList", "type": "Element"}
    )
    expert_solution_list: ExpertSolutionList = field(
        default=None,
        metadata={"name": "ExpertSolutionList", "type": "Element"},
    )
    route_list: RouteList = field(
        default=None, metadata={"name": "RouteList", "type": "Element"}
    )
    alternate_route_list: AlternateRouteList = field(
        default=None,
        metadata={"name": "AlternateRouteList", "type": "Element"},
    )
    alternate_location_distance_list: AlternateLocationDistanceList = field(
        default=None,
        metadata={"name": "AlternateLocationDistanceList", "type": "Element"},
    )
    fare_info_message: List[FareInfoMessage] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "FareInfoMessage",
            "type": "Element",
        },
    )
    rail_segment_list: RailSegmentList = field(
        default=None, metadata={"name": "RailSegmentList", "type": "Element"}
    )
    rail_journey_list: RailJourneyList = field(
        default=None, metadata={"name": "RailJourneyList", "type": "Element"}
    )
    rail_fare_note_list: RailFareNoteList = field(
        default=None, metadata={"name": "RailFareNoteList", "type": "Element"}
    )
    rail_fare_idlist: RailFareIdlist = field(
        default=None, metadata={"name": "RailFareIDList", "type": "Element"}
    )
    rail_fare_list: RailFareList = field(
        default=None, metadata={"name": "RailFareList", "type": "Element"}
    )
    rail_pricing_solution: List[RailPricingSolution] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "RailPricingSolution",
            "type": "Element",
        },
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingSolution",
            "type": "Element",
        },
    )
    air_price_point_list: AirPricePointList = field(
        default=None, metadata={"name": "AirPricePointList", "type": "Element"}
    )


@dataclass
class AirTicketingReq(AirBaseReq):
    """
    Request to ticket a previously stored reservation.
    """

    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    air_pricing_info_ref: List["AirTicketingReq.AirPricingInfoRef"] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirPricingInfoRef",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J-Indicates air pricing infos to be ticketed.",
        },
    )
    ticketing_modifiers_ref: List[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "TicketingModifiersRef",
            "type": "Element",
            "help": "Provider: 1P,1J-Reference to a shared list of Ticketing Modifiers. This is supported for Worldspan and JAL providers only. When AirPricingInfoRef is used along with TicketingModifiersRef means that particular TicketingModifiers will to be applied while ticketing the Stored fare corresponding to the AirPricingInfo. Absence of AirPricingInfoRef means that particular TicketingModifiers will be applied to all Stored fares which are requested to be ticketed.",
        },
    )
    waiver_code: WaiverCode = field(
        default=None, metadata={"name": "WaiverCode", "type": "Element"}
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 18,
            "name": "Commission",
            "type": "Element",
        },
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "DetailedBillingInformation",
            "type": "Element",
            "help": "Provider: 1G,1V.",
        },
    )
    fax_details_information: FaxDetailsInformation = field(
        default=None,
        metadata={
            "name": "FaxDetailsInformation",
            "type": "Element",
            "help": "Provider: 1V.",
        },
    )
    air_ticketing_modifiers: List[AirTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirTicketingModifiers",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    air_segment_ticketing_modifiers: List[
        AirSegmentTicketingModifiers
    ] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AirSegmentTicketingModifiers",
            "type": "Element",
            "help": "Provider: 1P,1J.",
        },
    )
    return_info_on_fail: bool = field(
        default="true",
        metadata={"name": "ReturnInfoOnFail", "type": "Attribute"},
    )
    bulk_ticket: bool = field(
        default="false",
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J.",
        },
    )
    validate_spanish_residency: bool = field(
        default="false",
        metadata={
            "name": "ValidateSpanishResidency",
            "type": "Attribute",
            "help": "Provider: 1G - If set as true, Spanish Residency will be validated for Provisioned Customers.",
        },
    )

    @dataclass
    class AirPricingInfoRef:
        booking_traveler_ref: List[BookingTravelerRef] = field(
            default_factory=list,
            metadata={
                "min_occurs": 0,
                "max_occurs": 9,
                "name": "BookingTravelerRef",
                "type": "Element",
            },
        )
        key: TypeRef = field(
            default=None,
            metadata={"required": True, "name": "Key", "type": "Attribute"},
        )


@dataclass
class AirUpsellSearchReq(AirBaseReq):
    """
    Request to search for Upsell Offers based on the Itinerary.
    """

    air_itinerary: AirItinerary = field(
        default=None,
        metadata={
            "required": True,
            "name": "AirItinerary",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH-AirItinerary of the pricing request.",
        },
    )
    air_price_result: List[AirPriceResult] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 16,
            "name": "AirPriceResult",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH-Result of AirPrice request. Upsell uses this to search for new offer.",
        },
    )


@dataclass
class AirUpsellSearchRsp(BaseAirPriceRsp):
    """
    Response of Upsell Offers search for the given Itinerary.
    """

    pass


@dataclass
class AvailabilitySearchRsp(BaseAvailabilitySearchRsp):
    pass


@dataclass
class BaseAirSearchReq(BaseCoreSearchReq):
    """
    Base Request for Low fare air Search
    """

    air_search_modifiers: AirSearchModifiers = field(
        default=None,
        metadata={"name": "AirSearchModifiers", "type": "Element"},
    )
    split_ticketing_search: SplitTicketingSearch = field(
        default=None,
        metadata={"name": "SplitTicketingSearch", "type": "Element"},
    )
    journey_data: JourneyData = field(
        default=None, metadata={"name": "JourneyData", "type": "Element"}
    )
    search_air_leg: List[SearchAirLeg] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 9,
            "name": "SearchAirLeg",
            "type": "Element",
        },
    )
    search_specific_air_segment: List[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 999,
            "name": "SearchSpecificAirSegment",
            "type": "Element",
        },
    )


@dataclass
class AvailabilitySearchReq(AirSearchReq):
    """
    Availability Search request.
    """

    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 18,
            "name": "SearchPassenger",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS passenger",
        },
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 5,
            "name": "PointOfSale",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    return_brand_indicator: bool = field(
        default="false",
        metadata={
            "name": "ReturnBrandIndicator",
            "type": "Attribute",
            "help": "When set to “true”, the Brand Indicator can be returned in the availability search response. Provider: 1G, 1V, 1P, 1J, ACH",
        },
    )
    channel_id: str = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "help": "A Channel ID is 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.",
        },
    )
    nscc: str = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "help": "Allows the agency to bypass/override the Search Control Console rule.",
        },
    )


@dataclass
class BaseLowFareSearchReq(BaseAirSearchReq):
    """
    Base Low Fare Search Request
    """

    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata={
            "min_occurs": 1,
            "max_occurs": 18,
            "name": "SearchPassenger",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS passenger",
        },
    )
    air_pricing_modifiers: AirPricingModifiers = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    enumeration: Enumeration = field(
        default=None,
        metadata={
            "name": "Enumeration",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )
    air_exchange_modifiers: AirExchangeModifiers = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
            "help": "Provider: ACH.",
        },
    )
    flex_explore_modifiers: FlexExploreModifiers = field(
        default=None,
        metadata={
            "name": "FlexExploreModifiers",
            "type": "Element",
            "help": "This is the container for a set of modifiers which allow the user to perform a special kind of low fare search, depicted as flex explore, based on different parameters like Area, Zone, Country, State, Specific locations, Distance around the actual destination of the itinerary. Applicable for providers 1G,1V,1P.",
        },
    )
    pcc: Pcc = field(default=None, metadata={"name": "PCC", "type": "Element"})
    fare_rules_filter_category: FareRulesFilterCategory = field(
        default=None,
        metadata={"name": "FareRulesFilterCategory", "type": "Element"},
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 99,
            "name": "FormOfPayment",
            "type": "Element",
            "help": "Provider: 1P,1J",
        },
    )
    enable_point_to_point_search: bool = field(
        default="false",
        metadata={
            "name": "EnablePointToPointSearch",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH-Indicates that low cost providers should be queried for top connection options and the results returned with the search.",
        },
    )
    enable_point_to_point_alternates: bool = field(
        default="false",
        metadata={
            "name": "EnablePointToPointAlternates",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH-Indicates that suggestions for alternate connection cities for low cost providers should be returned with the search.",
        },
    )
    max_number_of_expert_solutions: int = field(
        default="0",
        metadata={
            "name": "MaxNumberOfExpertSolutions",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH-Indicates the Maximum Number of Expert Solutions to be returned from the Knowledge Base for the provided search criteria",
        },
    )
    solution_result: bool = field(
        default="false",
        metadata={
            "name": "SolutionResult",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH-Indicates whether the response will contain Solution result (AirPricingSolution) or Non Solution Result (AirPricingPoints). The default value is false. This attribute cannot be combined with EnablePointToPointSearch, EnablePointToPointAlternates and MaxNumberOfExpertSolutions.",
        },
    )
    prefer_complete_itinerary: bool = field(
        default="true",
        metadata={
            "name": "PreferCompleteItinerary",
            "type": "Attribute",
            "help": "Provider: ACH-This attribute is only supported for ACH .It works in conjunction with the @SolutionResult flag",
        },
    )
    meta_option_identifier: str = field(
        default=None,
        metadata={
            "name": "MetaOptionIdentifier",
            "type": "Attribute",
            "help": "Invoke Meta Search. Valid values are 00 to 99, or D for the default meta search configuration. When Meta Search not requested, normal LowFareSearch applies. Supported Providers; 1g/1v/1p/1j",
        },
    )
    return_upsell_fare: bool = field(
        default="false",
        metadata={
            "name": "ReturnUpsellFare",
            "type": "Attribute",
            "help": "When set to “true”, Upsell information will be returned in the shop response. Provider supported : 1G, 1V, 1P, 1J",
        },
    )
    include_fare_info_messages: bool = field(
        default="false",
        metadata={
            "name": "IncludeFareInfoMessages",
            "type": "Attribute",
            "help": "Set to True to return FareInfoMessageList. Providers supported: 1G/1V/1P/1J",
        },
    )
    return_branded_fares: bool = field(
        default="true",
        metadata={
            "name": "ReturnBrandedFares",
            "type": "Attribute",
            "help": "When ReturnBrandedFares is set to “false”, Rich Content and Branding will not be returned in the shop response. When ReturnBrandedFares it is set to “true” or is not sent, Rich Content and Branding will be returned in the shop response. Provider: 1P/1J/ACH.",
        },
    )
    multi_gdssearch: bool = field(
        default="false",
        metadata={
            "name": "MultiGDSSearch",
            "type": "Attribute",
            "help": 'A "true" value indicates MultiGDSSearch. Specific provisioning is required.',
        },
    )
    return_mm: bool = field(
        default="false",
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
            "help": "If this attribute is set to “true”, Fare Control Manager processing will be invoked.",
        },
    )
    check_obfees: str = field(
        default=None,
        metadata={
            "name": "CheckOBFees",
            "type": "Attribute",
            "help": "A flag to return fees for ticketing and for various forms of payment. The default is “TicketingOnly” and will return only ticketing fees. The value “All” will return ticketing fees and the applicable form of payment fees for the form of payment information specified in the request. “FOPOnly” will return the applicable form of payment fees for the form of payment information specified in the request. Form of payment fees are never included in the total unless specific card details are in the request.Provider notes:ACH - CheckOBFees is valid only for LowFareSearch. The valid values are “All”, “TicketingOnly” and “None” and the default value is “None”. 1P/1J -The valid values are “All”, “None” and “TicketingOnly”.1G – All four values are supported.1V/RCH – CheckOBFees are not supported.”",
        },
    )
    nscc: str = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "help": "1 to 3 numeric that defines a Search Control Console filter.This attribute is used to override that filter.",
        },
    )
    fare_info_rules: bool = field(
        default="false",
        metadata={
            "name": "FareInfoRules",
            "type": "Attribute",
            "help": "Returns ChangePenalty and CancelPenalty values at the FareInfo level. If FareRulesFilterCategory is sent FareRulesFilter will be returned at FareInfo level. Provider: 1G/1V.",
        },
    )


@dataclass
class LowFareSearchAsynchRsp(AirSearchRsp):
    """
    Asynchronous Low Fare Search Response contains only the 1st Provider response unless time out occurs.
    """

    async_provider_specific_response: List[
        AsyncProviderSpecificResponse
    ] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AsyncProviderSpecificResponse",
            "type": "Element",
        },
    )
    brand_list: BrandList = field(
        default=None, metadata={"name": "BrandList", "type": "Element"}
    )
    search_id: TypeLowFareSearchId = field(
        default=None,
        metadata={
            "required": True,
            "name": "SearchId",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH-Indicates the Search Id of the LFS search",
        },
    )
    currency_type: TypeCurrency = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH-Specifies the default Currency Type in the response.",
        },
    )


@dataclass
class LowFareSearchRsp(AirSearchRsp):
    """
    Low Fare Search Response
    """

    brand_list: BrandList = field(
        default=None, metadata={"name": "BrandList", "type": "Element"}
    )
    currency_type: TypeCurrency = field(
        default=None,
        metadata={
            "required": True,
            "name": "CurrencyType",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )


@dataclass
class RetrieveLowFareSearchRsp(AirSearchRsp):
    """
    Low Fare Search Asynchronous Result response.
    """

    async_provider_specific_response: List[
        AsyncProviderSpecificResponse
    ] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AsyncProviderSpecificResponse",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH-Identifies pending responses from a specific provider using MoreResults attribute",
        },
    )
    brand_list: BrandList = field(
        default=None, metadata={"name": "BrandList", "type": "Element"}
    )
    currency_type: TypeCurrency = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )


@dataclass
class ScheduleSearchReq(AirSearchReq):
    """
    Schedule Search request
    """

    pass


@dataclass
class ScheduleSearchRsp(AirSearchRsp):
    """
    Schedule Search response
    """

    pass


@dataclass
class LowFareSearchAsynchReq(BaseLowFareSearchReq):
    """
    Asynchronous Low Fare Search request.
    """

    air_search_asynch_modifiers: AirSearchAsynchModifiers = field(
        default=None,
        metadata={
            "name": "AirSearchAsynchModifiers",
            "type": "Element",
            "help": "Provider: 1G,1V,1P,1J,ACH.",
        },
    )


@dataclass
class LowFareSearchReq(BaseLowFareSearchReq):
    """
    Low Fare Search request.
    """

    policy_reference: TypePolicyReference = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Attribute",
            "help": "This attribute will be used to pass in a value on the request which would be used to link to a ‘Policy Group’ in a policy engine external to UAPI.",
        },
    )
