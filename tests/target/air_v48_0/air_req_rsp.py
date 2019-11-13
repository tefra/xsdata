from dataclasses import dataclass, field
from typing import List

from ..common_v48_0.common_req_rsp import *
from ..rail_v48_0.rail import *
from .air import *


@dataclass
class AirBaseReq(BaseReq):
    """Context for Requests and Responses."""
    pass


@dataclass
class AirExchangeEligibilityReq(BaseReq):
    """Request to determine if the fares in an itinerary are exchangeable.

    :ivar provider_reservation_info: Provider:1P - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged
    :ivar type: Type choices are "Detail" or "Summary" Default will be Summary
    """
    provider_reservation_info: "AirExchangeEligibilityReq.ProviderReservationInfo" = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element",
            required=True
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )

    @dataclass
    class ProviderReservationInfo(ProviderReservation):
        
        pass


@dataclass
class AirExchangeEligibilityRsp(BaseRsp):
    """
    :ivar exchange_eligibility_info:
    """
    exchange_eligibility_info: ExchangeEligibilityInfo = field(
        default=None,
        metadata=dict(
            name="ExchangeEligibilityInfo",
            type="Element",
            required=True
        )
    )


@dataclass
class AirExchangeQuoteRsp(BaseRsp):
    """
    :ivar ticket_number:
    :ivar air_pricing_solution: Provider: 1G/1V/1P/1S/1A.
    :ivar air_exchange_bundle_total:
    :ivar air_exchange_bundle: Bundle exchange, pricing, and penalty information. Providers ACH/1G/1V/1P
    :ivar host_token: Encrypted data from the host. Required to send the HostToken from the AirExchangeQuoteRsp in the AirExchangeReq. Providers ACH/1G/1V/1P.
    :ivar optional_services: Provider: ACH.
    :ivar fare_rule: Provider: ACH.
    """
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    air_exchange_bundle_total: AirExchangeBundleTotal = field(
        default=None,
        metadata=dict(
            name="AirExchangeBundleTotal",
            type="Element"
        )
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundle",
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
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeReq(BaseReq):
    """Request to exchange an itinerary.

    :ivar air_reservation_locator_code: Identifies the PNR locator code. Providers ACH/1G/1V/1P
    :ivar ticket_number:
    :ivar specific_seat_assignment: Identifies the standard seat. Providers ACH/1G/1V/1P
    :ivar air_pricing_solution: Providers ACH/1G/1V/1P.
    :ivar air_exchange_modifiers: Provider: ACH.
    :ivar air_exchange_bundle_total: Provider: 1G/1V/1P/1S/1A.
    :ivar air_exchange_bundle: Bundle exchange, pricing, and penalty information. Providers ACH/1G/1V/1P.
    :ivar host_token: Encrypted data from the host. Required to send the HostToken from the AirExchangeQuoteRsp in the AirExchangeReq. Providers ACH/1G/1V/1P
    :ivar optional_services: Provider: ACH.
    :ivar form_of_payment: Form of Payment for any additional collection charges for the Exchange. For ACH, most carriers will only allow refund amounts to the original form of payment. Providers ACH/1G/1V/1P
    :ivar form_of_payment_ref: Provider: ACH-Universal Record reference to Form of Payment for any Additional Collection charges or Refund due for the itinerary exchange
    :ivar ssrinfo: Providers ACH, 1G, 1V, 1P.
    :ivar add_svc: 1P - Add SVC segments to collect additional fee
    :ivar return_reservation: Provider: ACH.
    """
    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            required=True
        )
    )
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    specific_seat_assignment: List[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata=dict(
            name="SpecificSeatAssignment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    air_exchange_modifiers: AirExchangeModifiers = field(
        default=None,
        metadata=dict(
            name="AirExchangeModifiers",
            type="Element"
        )
    )
    air_exchange_bundle_total: AirExchangeBundleTotal = field(
        default=None,
        metadata=dict(
            name="AirExchangeBundleTotal",
            type="Element"
        )
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundle",
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
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    form_of_payment: FormOfPayment = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element"
        )
    )
    form_of_payment_ref: FormOfPaymentRef = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element"
        )
    )
    ssrinfo: List[Ssrinfo] = field(
        default_factory=list,
        metadata=dict(
            name="SSRInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    add_svc: AddSvc = field(
        default=None,
        metadata=dict(
            name="AddSvc",
            type="Element"
        )
    )
    return_reservation: bool = field(
        default="false",
        metadata=dict(
            name="ReturnReservation",
            type="Attribute"
        )
    )


@dataclass
class AirExchangeRsp(BaseRsp):
    """
    :ivar ticket_number:
    :ivar booking_traveler: Provider: ACH.
    :ivar air_reservation: Provider: ACH.
    :ivar exchange_failure_info: Provider: ACH.
    """
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTraveler",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_reservation: TypeAirReservationWithFop = field(
        default=None,
        metadata=dict(
            name="AirReservation",
            type="Element"
        )
    )
    exchange_failure_info: List[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangeFailureInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeTicketingReq(BaseReq):
    """Request to ticket an exchanged itinerary. Providers 1G, 1V, 1P.

    :ivar air_reservation_locator_code: Identifies the PNR to ticket. Providers 1G, 1V, 1P.
    :ivar ticket_number: Ticket number to reissue. Providers 1G, 1V, 1P.
    :ivar ticketing_modifiers_ref: Provider: 1P-Reference to a shared list of Ticketing Modifiers. This is supported for Worldspan provider only. When AirPricingInfoRef is used along with TicketingModifiersRef means that particular TicketingModifiers will to be applied while ticketing the Stored fare corresponding to the AirPricingInfo. Absence of AirPricingInfoRef means that particular TicketingModifiers will be applied to all Stored fares which are requested to be ticketed.
    :ivar waiver_code:
    :ivar detailed_billing_information: Providers 1G, 1V, 1P.
    :ivar air_ticketing_modifiers: Provider: 1G,1V,1P.
    :ivar bulk_ticket: Providers 1G, 1V, 1P.
    :ivar change_fee_on_ticket: Applies the change fee/penalty to the original form of payment. Providers: 1V
    """
    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            required=True
        )
    )
    ticket_number: TicketNumber = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            required=True
        )
    )
    ticketing_modifiers_ref: List[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata=dict(
            name="TicketingModifiersRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_code: WaiverCode = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element"
        )
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_ticketing_modifiers: List[AirTicketingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirTicketingModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    bulk_ticket: bool = field(
        default="false",
        metadata=dict(
            name="BulkTicket",
            type="Attribute"
        )
    )
    change_fee_on_ticket: bool = field(
        default="true",
        metadata=dict(
            name="ChangeFeeOnTicket",
            type="Attribute"
        )
    )


@dataclass
class AirExchangeTicketingRsp(BaseRsp):
    """Response to reissue a ticket.

    :ivar air_solution_changed_info:
    :ivar etr: Provider 1G, 1V, 1P.
    :ivar ticket_failure_info: Provider 1G, 1V, 1P.
    :ivar detailed_billing_information: Providers 1G, 1V, 1P.
    """
    air_solution_changed_info: AirSolutionChangedInfo = field(
        default=None,
        metadata=dict(
            name="AirSolutionChangedInfo",
            type="Element"
        )
    )
    etr: Etr = field(
        default=None,
        metadata=dict(
            name="ETR",
            type="Element"
        )
    )
    ticket_failure_info: TicketFailureInfo = field(
        default=None,
        metadata=dict(
            name="TicketFailureInfo",
            type="Element"
        )
    )
    detailed_billing_information: DetailedBillingInformation = field(
        default=None,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element"
        )
    )


@dataclass
class AirFareDisplayReq(BaseReq):
    """Request to display a tariff for based on origin, destination, and other
    options.

    :ivar fare_type: Provider: 1G,1V,1P,1J.
    :ivar passenger_type: Provider: 1G,1V,1P,1J.
    :ivar booking_code: Provider: 1G,1V,1P,1J.
    :ivar include_addl_booking_code_info: Provider: 1G,1V,1P,1J.
    :ivar fare_basis: Provider: 1G,1V,1P,1J.
    :ivar carrier: Provider: 1G,1V,1P,1J.
    :ivar account_code: Provider: 1G,1V,1P,1J.
    :ivar contract_code: Provider: 1G,1V.
    :ivar air_fare_display_modifiers: Provider: 1G,1V,1P,1J.
    :ivar point_of_sale: Provider: 1G,1V.
    :ivar air_fare_display_rule_key: Provider: 1G,1V,1P,1J.
    :ivar origin: Provider: 1G,1V,1P,1J.
    :ivar destination: Provider: 1G,1V,1P,1J.
    :ivar provider_code: Provider: 1G,1V,1P,1J.
    :ivar include_mile_route_information: Provider: 1G,1V,1P,1J-Used to request Mile/Route Information in follow on (Mile, Route, Both)
    :ivar un_saleable_fares_only: Provider: 1G,1V,1P,1J-Used to request unsaleable fares only also known as place of sale fares.
    :ivar channel_id: A Channel ID is 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.
    :ivar nscc: 1 to 3 numeric that define a Search Control Console filter.This attribute is used to override that filter.
    :ivar return_mm: If this attribute is set to true, Fare Control Manager processing will be invoked.
    """
    fare_type: List[FareType] = field(
        default_factory=list,
        metadata=dict(
            name="FareType",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    passenger_type: List[TypePassengerType] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerType",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata=dict(
            name="BookingCode",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    include_addl_booking_code_info: IncludeAddlBookingCodeInfo = field(
        default=None,
        metadata=dict(
            name="IncludeAddlBookingCodeInfo",
            type="Element"
        )
    )
    fare_basis: FareBasis = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Element"
        )
    )
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    contract_code: ContractCode = field(
        default=None,
        metadata=dict(
            name="ContractCode",
            type="Element"
        )
    )
    air_fare_display_modifiers: AirFareDisplayModifiers = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayModifiers",
            type="Element"
        )
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    air_fare_display_rule_key: AirFareDisplayRuleKey = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayRuleKey",
            type="Element"
        )
    )
    origin: str = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
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
            required=True,
            min_length=2.0,
            max_length=5.0
        )
    )
    include_mile_route_information: str = field(
        default=None,
        metadata=dict(
            name="IncludeMileRouteInformation",
            type="Attribute"
        )
    )
    un_saleable_fares_only: bool = field(
        default=None,
        metadata=dict(
            name="UnSaleableFaresOnly",
            type="Attribute"
        )
    )
    channel_id: str = field(
        default=None,
        metadata=dict(
            name="ChannelId",
            type="Attribute",
            min_length=2.0,
            max_length=4.0
        )
    )
    nscc: str = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            min_length=1.0,
            max_length=3.0
        )
    )
    return_mm: bool = field(
        default="false",
        metadata=dict(
            name="ReturnMM",
            type="Attribute"
        )
    )


@dataclass
class AirFareDisplayRsp(BaseRsp):
    """Response to an AirFareDisplayReq.

    :ivar fare_display: Provider: 1G,1V,1P,1J.
    """
    fare_display: List[FareDisplay] = field(
        default_factory=list,
        metadata=dict(
            name="FareDisplay",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirFareRulesReq(BaseReq):
    """Request to display the full text fare rules.

    :ivar air_fare_rules_modifier: Provider: 1G,1V.
    :ivar fare_rules_filter_category: Structured Fare Rules Filter if requested will return rules for requested categories in the response. Applicable for providers 1G, 1V.
    :ivar air_reservation_selector: Provider: 1G,1V,1P,1J,ACH-Parameters to use for a fare rule lookup associated with an Air Reservation Locator Code
    :ivar fare_rule_lookup: Used to look up fare rules based on the origin, destination, and carrier of the air segment, the fare basis code and the provider code. Providers: 1P, 1J.
    :ivar fare_rule_key: Used to look up fare rules based on a fare rule key. Providers: 1G, 1V, 1P, 1J, ACH.
    :ivar air_fare_display_rule_key: Provider: 1G,1V,1P,1J.
    :ivar fare_rule_type: Provider: 1G,1V,1P,1J,ACH.
    """
    air_fare_rules_modifier: AirFareRulesModifier = field(
        default=None,
        metadata=dict(
            name="AirFareRulesModifier",
            type="Element"
        )
    )
    fare_rules_filter_category: List["AirFareRulesReq.FareRulesFilterCategory"] = field(
        default_factory=list,
        metadata=dict(
            name="FareRulesFilterCategory",
            type="Element",
            min_occurs=0,
            max_occurs=16
        )
    )
    air_reservation_selector: "AirFareRulesReq.AirReservationSelector" = field(
        default=None,
        metadata=dict(
            name="AirReservationSelector",
            type="Element",
            required=True
        )
    )
    fare_rule_lookup: FareRuleLookup = field(
        default=None,
        metadata=dict(
            name="FareRuleLookup",
            type="Element"
        )
    )
    fare_rule_key: List[FareRuleKey] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleKey",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    air_fare_display_rule_key: AirFareDisplayRuleKey = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayRuleKey",
            type="Element",
            required=True
        )
    )
    fare_rule_type: str = field(
        default="long",
        metadata=dict(
            name="FareRuleType",
            type="Attribute"
        )
    )

    @dataclass
    class FareRulesFilterCategory:
        """
        :ivar category_code: Structured Fare Rules can be requested for "ADV", "MIN", "MAX", "STP", and "CHG".
        :ivar fare_info_ref: Key reference for multiple fare rule
        """
        category_code: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="CategoryCode",
                type="Element",
                min_occurs=1,
                max_occurs=35
            )
        )
        fare_info_ref: str = field(
            default=None,
            metadata=dict(
                name="FareInfoRef",
                type="Attribute"
            )
        )

    @dataclass
    class AirReservationSelector:
        """
        :ivar fare_info_ref:
        :ivar air_reservation_locator_code: The Air Reservation locator code which is an unique identifier for the reservation
        """
        fare_info_ref: List[FareInfoRef] = field(
            default_factory=list,
            metadata=dict(
                name="FareInfoRef",
                type="Element",
                min_occurs=0,
                max_occurs=999
            )
        )
        air_reservation_locator_code: str = field(
            default=None,
            metadata=dict(
                name="AirReservationLocatorCode",
                type="Attribute",
                required=True,
                min_length=5.0,
                max_length=8.0
            )
        )


@dataclass
class AirFareRulesRsp(BaseRsp):
    """Response to an AirFareRuleReq.

    :ivar fare_rule: Provider: 1G,1V,1P,1J,ACH.
    """
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirMerchandisingDetailsReq(BaseReq):
    """Request to retrieve brand details and optional services included in the
    brand.

    :ivar merchandising_details:
    :ivar optional_service_modifiers:
    :ivar merchandising_availability_details:
    """
    merchandising_details: MerchandisingDetails = field(
        default=None,
        metadata=dict(
            name="MerchandisingDetails",
            type="Element",
            required=True
        )
    )
    optional_service_modifiers: OptionalServiceModifiers = field(
        default=None,
        metadata=dict(
            name="OptionalServiceModifiers",
            type="Element",
            required=True
        )
    )
    merchandising_availability_details: MerchandisingAvailabilityDetails = field(
        default=None,
        metadata=dict(
            name="MerchandisingAvailabilityDetails",
            type="Element",
            required=True
        )
    )


@dataclass
class AirMerchandisingDetailsRsp(BaseRsp):
    """Response for retrieved brand details and optional services included in them.

    :ivar optional_services:
    :ivar brand:
    :ivar unassociated_booking_code_list: Lists classes of service by segment sent in the request which are not associated to a brand.
    """
    optional_services: OptionalServices = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    brand: List[Brand] = field(
        default_factory=list,
        metadata=dict(
            name="Brand",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    unassociated_booking_code_list: "AirMerchandisingDetailsRsp.UnassociatedBookingCodeList" = field(
        default=None,
        metadata=dict(
            name="UnassociatedBookingCodeList",
            type="Element"
        )
    )

    @dataclass
    class UnassociatedBookingCodeList:
        """
        :ivar applicable_segment:
        """
        applicable_segment: List[TypeApplicableSegment] = field(
            default_factory=list,
            metadata=dict(
                name="ApplicableSegment",
                type="Element",
                min_occurs=0,
                max_occurs=99
            )
        )


@dataclass
class AirMerchandisingOfferAvailabilityReq(BaseReq):
    """Check with the supplier whether or not the reservation or air solution
    supports any merchandising offerings.

    :ivar agency_sell_info: Provider: 1G,1V,1P,1J,ACH.
    :ivar air_solution: Provider: 1G,1V,1P,1J,ACH.
    :ivar host_reservation: Provider: 1G,1V,1P,1J,ACH.
    :ivar offer_availability_modifiers: Provider: 1G,1V,1P,1J,ACH.
    :ivar merchandising_pricing_modifiers: Used to provide additional pricing modifiers. Provider:ACH.
    """
    agency_sell_info: AgencySellInfo = field(
        default=None,
        metadata=dict(
            name="AgencySellInfo",
            type="Element"
        )
    )
    air_solution: AirSolution = field(
        default=None,
        metadata=dict(
            name="AirSolution",
            type="Element"
        )
    )
    host_reservation: List[HostReservation] = field(
        default_factory=list,
        metadata=dict(
            name="HostReservation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    offer_availability_modifiers: List[OfferAvailabilityModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="OfferAvailabilityModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    merchandising_pricing_modifiers: MerchandisingPricingModifiers = field(
        default=None,
        metadata=dict(
            name="MerchandisingPricingModifiers",
            type="Element"
        )
    )


@dataclass
class AirMerchandisingOfferAvailabilityRsp(BaseRsp):
    """Contains the merchandising offerings for the given passenger and itinerary.

    :ivar air_solution: Provider: 1G,1V,1P,1J,ACH.
    :ivar remark: Provider: 1G,1V,1P,1J,ACH.
    :ivar optional_services:
    :ivar embargo_list:
    """
    air_solution: AirSolution = field(
        default=None,
        metadata=dict(
            name="AirSolution",
            type="Element",
            required=True
        )
    )
    remark: Remark = field(
        default=None,
        metadata=dict(
            name="Remark",
            type="Element"
        )
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    embargo_list: EmbargoList = field(
        default=None,
        metadata=dict(
            name="EmbargoList",
            type="Element"
        )
    )


@dataclass
class AirPrePayReq(BaseReq):
    """Flight Pass Request.

    :ivar list_search: Provider: ACH.
    :ivar pre_pay_retrieve: Provider: ACH.
    """
    list_search: "AirPrePayReq.ListSearch" = field(
        default=None,
        metadata=dict(
            name="ListSearch",
            type="Element",
            required=True
        )
    )
    pre_pay_retrieve: "AirPrePayReq.PrePayRetrieve" = field(
        default=None,
        metadata=dict(
            name="PrePayRetrieve",
            type="Element",
            required=True
        )
    )

    @dataclass
    class ListSearch:
        """
        :ivar person_name_search: Customer name detail for searching flight pass content.
        :ivar loyalty_card: Customer loyalty card for searching flight pass content.
        :ivar start_from_result: Start index of the section of flight pass numbers that is being requested.
        :ivar max_results: Max Number of Flight Passes being requested for.
        """
        person_name_search: PersonNameSearch = field(
            default=None,
            metadata=dict(
                name="PersonNameSearch",
                type="Element",
                required=True
            )
        )
        loyalty_card: List[LoyaltyCard] = field(
            default_factory=list,
            metadata=dict(
                name="LoyaltyCard",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )
        start_from_result: int = field(
            default=None,
            metadata=dict(
                name="StartFromResult",
                type="Attribute",
                required=True,
                min_inclusive=1.0
            )
        )
        max_results: int = field(
            default=None,
            metadata=dict(
                name="MaxResults",
                type="Attribute",
                required=True,
                min_inclusive=1.0,
                max_inclusive=200.0
            )
        )

    @dataclass
    class PrePayRetrieve:
        """
        :ivar id: Pre pay id to retrieved,example flight pass number
        :ivar type: Pre pay id type,example 'FlightPass'
        """
        id: str = field(
            default=None,
            metadata=dict(
                name="Id",
                type="Attribute",
                required=True,
                min_length=1.0,
                max_length=36.0
            )
        )
        type: str = field(
            default=None,
            metadata=dict(
                name="Type",
                type="Attribute"
            )
        )


@dataclass
class AirPrePayRsp(BaseRsp):
    """Flight Pass Response.

    :ivar pre_pay_profile_info: Provider: ACH.
    :ivar max_results: Provider: ACH-Max Number of Flight Passes being returned.
    :ivar more_indicator: Provider: ACH-Indicates if there are more flight passes to be offered
    :ivar more_data_start_index: Provider: ACH-Indicates start index of the next flight Passes
    """
    pre_pay_profile_info: List[PrePayProfileInfo] = field(
        default_factory=list,
        metadata=dict(
            name="PrePayProfileInfo",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    max_results: int = field(
        default=None,
        metadata=dict(
            name="MaxResults",
            type="Attribute",
            min_inclusive=1.0,
            max_inclusive=200.0
        )
    )
    more_indicator: bool = field(
        default=None,
        metadata=dict(
            name="MoreIndicator",
            type="Attribute"
        )
    )
    more_data_start_index: str = field(
        default=None,
        metadata=dict(
            name="MoreDataStartIndex",
            type="Attribute"
        )
    )


@dataclass
class AirRefundQuoteReq(BaseReq):
    """Request to quote a refund for an itinerary.

    :ivar ticket_number: Provider: ACH.
    :ivar tcrnumber: Provider: ACH-The identifying number for a Ticketless Air Reservation
    :ivar air_refund_modifiers: Provider: ACH.
    :ivar host_token: Provider: ACH.
    :ivar provider_reservation_info: Provider: 1P - Represents a valid Provider Reservation/PNR whose itinerary is to be requested
    :ivar ignore: Provider: ACH.
    """
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TCRNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_refund_modifiers: AirRefundModifiers = field(
        default=None,
        metadata=dict(
            name="AirRefundModifiers",
            type="Element"
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info: List["AirRefundQuoteReq.ProviderReservationInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ignore: bool = field(
        default="false",
        metadata=dict(
            name="Ignore",
            type="Attribute"
        )
    )

    @dataclass
    class ProviderReservationInfo(ProviderReservation):
        
        pass


@dataclass
class AirRefundQuoteRsp(BaseRsp):
    """
    :ivar air_refund_bundle:
    :ivar tcrrefund_bundle: Provider: ACH.
    """
    air_refund_bundle: List[AirRefundBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirRefundBundle",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrrefund_bundle: List[TcrrefundBundle] = field(
        default_factory=list,
        metadata=dict(
            name="TCRRefundBundle",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirRefundReq(BaseReq):
    """Request to refund an itinerary for the amount previously quoted.

    :ivar air_refund_bundle: Provider: ACH.
    :ivar tcrrefund_bundle: Provider: ACH.
    :ivar air_refund_modifiers:
    :ivar commission: Provider: ACH.
    :ivar form_of_payment: Provider: ACH-Form of Payment for any Additional Collection charges for the Refund.
    """
    air_refund_bundle: List[AirRefundBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirRefundBundle",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrrefund_bundle: List[TcrrefundBundle] = field(
        default_factory=list,
        metadata=dict(
            name="TCRRefundBundle",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_refund_modifiers: AirRefundModifiers = field(
        default=None,
        metadata=dict(
            name="AirRefundModifiers",
            type="Element"
        )
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata=dict(
            name="Commission",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    form_of_payment: FormOfPayment = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element"
        )
    )


@dataclass
class AirRefundRsp(BaseRsp):
    """
    :ivar etr: Provider: ACH.
    :ivar tcr: Provider: ACH.
    :ivar refund_failure_info: Provider: ACH.
    """
    etr: List[Etr] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcr: List[Tcr] = field(
        default_factory=list,
        metadata=dict(
            name="TCR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    refund_failure_info: List[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RefundFailureInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirRepriceRsp(BaseRsp):
    """
    :ivar air_pricing_solution:
    :ivar fare_rule:
    """
    air_pricing_solution: AirPricingSolution = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            required=True
        )
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirRetrieveDocumentReq(BaseReq):
    """Retrieve the post booking information for a PNR. ETRs will be returned for
    standard carriers. TCRs will be returned for Ticketless carriers. If the
    locator is send on a standard carrier, all ETRs will be retrieved.

    :ivar air_reservation_locator_code: Provider: 1G,1V,1P,1J.
    :ivar ticket_number: Provider: 1G,1V,1P,1J.
    :ivar tcrnumber: Provider: 1G,1V,1P,1J-The identifying number for a Ticketless Air Reservation.
    :ivar return_restrictions: Will return a response which includes a set of restrictions associated with the document.
    :ivar return_pricing: Provider: 1G,1V,1P,1J-Will return a response which includes the pricing associated with the ETR.
    :ivar retrieve_mco: When true, returns MCO Information. The default value is false.
    """
    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element"
        )
    )
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TCRNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    return_restrictions: bool = field(
        default=None,
        metadata=dict(
            name="ReturnRestrictions",
            type="Attribute"
        )
    )
    return_pricing: bool = field(
        default=None,
        metadata=dict(
            name="ReturnPricing",
            type="Attribute"
        )
    )
    retrieve_mco: bool = field(
        default=None,
        metadata=dict(
            name="RetrieveMCO",
            type="Attribute"
        )
    )


@dataclass
class AirRetrieveDocumentRsp(BaseRsp):
    """
    :ivar etr: Provider: 1G,1V,1P,1J.
    :ivar mco: Provider: 1G,1V,1P,1J.
    :ivar tcr: Provider: 1G,1V,1P,1J.
    :ivar document_failure_info: Provider: 1G,1V,1P,1J-Will be optionally returned if there are duplicate ticket numbers.
    :ivar service_fee_info: Provider: 1G,1V
    :ivar universal_record_locator_code: Provider: 1G,1V,1P,1J-Represents a valid Universal Record locator code.
    """
    etr: List[Etr] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    mco: List[Mco] = field(
        default_factory=list,
        metadata=dict(
            name="MCO",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcr: List[Tcr] = field(
        default_factory=list,
        metadata=dict(
            name="TCR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    document_failure_info: List[TypeFailureInfo] = field(
        default_factory=list,
        metadata=dict(
            name="DocumentFailureInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    service_fee_info: List[ServiceFeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceFeeInfo",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    universal_record_locator_code: str = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            min_length=5.0,
            max_length=8.0
        )
    )


@dataclass
class AirTicketingRsp(BaseRsp):
    """Response to ticket a previously stored reservation.

    :ivar air_solution_changed_info:
    :ivar etr: Provider: 1G,1V,1P,1J.
    :ivar ticket_failure_info: Provider: 1G,1V,1P,1J.
    :ivar detailed_billing_information: Provider: 1G,1V,1P,1J.
    """
    air_solution_changed_info: AirSolutionChangedInfo = field(
        default=None,
        metadata=dict(
            name="AirSolutionChangedInfo",
            type="Element"
        )
    )
    etr: List[Etr] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticket_failure_info: List[TicketFailureInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TicketFailureInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirVoidDocumentReq(BaseReq):
    """Request to void all previously issued tickets for the PNR.

    :ivar air_reservation_locator_code: Provider: 1G,1V.
    :ivar void_document_info: Provider: 1G,1V-All tickets that belong to this PNR must be enumerated here. Voiding only some tickets of a multi-ticket PNR not currently supported.
    :ivar show_etr: Provider: 1G,1V-If set as true, response will display the detailed ETR for successfully voided E-Tickets.
    :ivar provider_code: Provider: 1G,1V-Provider code of a specific host.
    :ivar provider_locator_code: Provider: 1G,1V-Contains the locator of the host reservation.
    :ivar validate_spanish_residency: Provider: 1G - If set as true, Spanish Residency will be validated for Provisioned Customers.
    """
    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element"
        )
    )
    void_document_info: List[VoidDocumentInfo] = field(
        default_factory=list,
        metadata=dict(
            name="VoidDocumentInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    show_etr: bool = field(
        default="false",
        metadata=dict(
            name="ShowETR",
            type="Attribute"
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2.0,
            max_length=5.0
        )
    )
    provider_locator_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute"
        )
    )
    validate_spanish_residency: bool = field(
        default="false",
        metadata=dict(
            name="ValidateSpanishResidency",
            type="Attribute"
        )
    )


@dataclass
class AirVoidDocumentRsp(BaseRsp):
    """Result of void ticket request. Includes ticket number of voided tickets and
    air segments with updated status.

    :ivar etr: Provider: 1G,1V.
    :ivar void_result_info: Provider: 1G,1V.
    """
    etr: List[Etr] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    void_result_info: List[VoidResultInfo] = field(
        default_factory=list,
        metadata=dict(
            name="VoidResultInfo",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class BaseAirExchangeMultiQuoteReq(BaseCoreReq):
    """
    :ivar ticket_number:
    :ivar provider_reservation_info: Provider: 1P - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged
    :ivar air_pricing_solution:
    :ivar repricing_modifiers:
    :ivar original_itinerary_details:
    :ivar override_pcc:
    """
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info: "BaseAirExchangeMultiQuoteReq.ProviderReservationInfo" = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element"
        )
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )
    repricing_modifiers: RepricingModifiers = field(
        default=None,
        metadata=dict(
            name="RepricingModifiers",
            type="Element"
        )
    )
    original_itinerary_details: OriginalItineraryDetails = field(
        default=None,
        metadata=dict(
            name="OriginalItineraryDetails",
            type="Element"
        )
    )
    override_pcc: OverridePcc = field(
        default=None,
        metadata=dict(
            name="OverridePCC",
            type="Element"
        )
    )

    @dataclass
    class ProviderReservationInfo(ProviderReservation):
        
        pass


@dataclass
class BaseAirExchangeQuoteReq(BaseCoreReq):
    """
    :ivar ticket_number:
    :ivar provider_reservation_info: Provider: 1G/1V/1P/ACH - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged
    :ivar air_pricing_solution:
    :ivar air_exchange_modifiers: Provider: ACH.
    :ivar host_token: Provider: ACH.
    :ivar optional_services: Provider: ACH.
    :ivar form_of_payment: Provider: ACH-This would allow a user to see the fees if they are changing from one Form Of Payment to other .
    :ivar repricing_modifiers:
    :ivar original_itinerary_details:
    :ivar pcc:
    :ivar fare_rule_type: Provider: ACH.
    """
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info: "BaseAirExchangeQuoteReq.ProviderReservationInfo" = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element"
        )
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )
    air_exchange_modifiers: AirExchangeModifiers = field(
        default=None,
        metadata=dict(
            name="AirExchangeModifiers",
            type="Element"
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    repricing_modifiers: RepricingModifiers = field(
        default=None,
        metadata=dict(
            name="RepricingModifiers",
            type="Element"
        )
    )
    original_itinerary_details: OriginalItineraryDetails = field(
        default=None,
        metadata=dict(
            name="OriginalItineraryDetails",
            type="Element"
        )
    )
    pcc: Pcc = field(
        default=None,
        metadata=dict(
            name="PCC",
            type="Element"
        )
    )
    fare_rule_type: str = field(
        default="none",
        metadata=dict(
            name="FareRuleType",
            type="Attribute"
        )
    )

    @dataclass
    class ProviderReservationInfo(ProviderReservation):
        
        pass


@dataclass
class BaseAirPriceReq(BaseCoreReq):
    """
    :ivar air_itinerary: Provider: 1G,1V,1P,1J,ACH.
    :ivar air_pricing_modifiers: Provider: 1G,1V,1P,1J,ACH.
    :ivar search_passenger: Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS passenger
    :ivar air_pricing_command: Provider: 1G,1V,1P,1J,ACH.
    :ivar air_reservation_locator_code: Provider: ACH,1P,1J
    :ivar optional_services: Provider: ACH.
    :ivar form_of_payment: Provider: 1G,1V,1P,1J,ACH.
    :ivar pcc:
    :ivar ssr: Special Service Request for GST tax details. Provider: ACH
    :ivar check_obfees: A flag to return fees for ticketing and for various forms of payment. The default is “TicketingOnly” and will return only ticketing fees. The value “All” will return ticketing fees and the applicable form of payment fees for the form of payment information specified in the request. “FOPOnly” will return the applicable form of payment fees for the form of payment information specified in the request. Form of payment fees are never included in the total unless specific card details are in the request.Provider notes:ACH - CheckOBFees is valid only for LowFareSearch. The valid values are “All”, “TicketingOnly” and “None” and the default value is “None”. 1P/1J -The valid values are “All”, “None” and “TicketingOnly”.1G – All four values are supported.1V/RCH – CheckOBFees are not supported.”
    :ivar fare_rule_type: Provider: 1G,1V,1P,1J,ACH.
    :ivar supplier_code: Specifies the supplier/ vendor for vendor specific price requests
    :ivar ticket_date: YYYY-MM-DD Using a date in the past is a request for an historical fare
    :ivar check_flight_details: To Include FlightDetails in Response set to “true” the Default value is “false”.
    :ivar return_mm: If this attribute is set to “true”, Fare Control Manager processing will be invoked.
    :ivar nscc: 1 to 3 numeric that defines a Search Control Console filter.This attribute is used to override that filter.
    :ivar split_pricing: Indicates whether the AirSegments should be priced together or separately. Set ‘true’ for split pricing. Set ‘false’ for pricing together.SplitPricing is not supported with post book re-pricing.
    :ivar ignore_availability: Provides a method of pricing a book itinerary with the lowest fare regardless of the availability for the class of service. Only for providers 1P/1J.
    """
    air_itinerary: AirItinerary = field(
        default=None,
        metadata=dict(
            name="AirItinerary",
            type="Element",
            required=True
        )
    )
    air_pricing_modifiers: AirPricingModifiers = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element"
        )
    )
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata=dict(
            name="SearchPassenger",
            type="Element",
            min_occurs=1,
            max_occurs=18
        )
    )
    air_pricing_command: List[AirPricingCommand] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingCommand",
            type="Element",
            min_occurs=1,
            max_occurs=16
        )
    )
    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element"
        )
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    pcc: Pcc = field(
        default=None,
        metadata=dict(
            name="PCC",
            type="Element"
        )
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata=dict(
            name="SSR",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    check_obfees: str = field(
        default=None,
        metadata=dict(
            name="CheckOBFees",
            type="Attribute"
        )
    )
    fare_rule_type: str = field(
        default="none",
        metadata=dict(
            name="FareRuleType",
            type="Attribute"
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            min_length=1.0,
            max_length=5.0
        )
    )
    ticket_date: str = field(
        default=None,
        metadata=dict(
            name="TicketDate",
            type="Attribute"
        )
    )
    check_flight_details: bool = field(
        default="false",
        metadata=dict(
            name="CheckFlightDetails",
            type="Attribute"
        )
    )
    return_mm: bool = field(
        default="false",
        metadata=dict(
            name="ReturnMM",
            type="Attribute"
        )
    )
    nscc: str = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            min_length=1.0,
            max_length=3.0
        )
    )
    split_pricing: bool = field(
        default="false",
        metadata=dict(
            name="SplitPricing",
            type="Attribute"
        )
    )
    ignore_availability: bool = field(
        default="false",
        metadata=dict(
            name="IgnoreAvailability",
            type="Attribute"
        )
    )


@dataclass
class BaseAirPriceRsp(BaseRsp):
    """
    :ivar air_itinerary: Provider: 1G,1V,1P,1J,ACH.
    :ivar air_price_result: Provider: 1G,1V,1P,1J,ACH.
    """
    air_itinerary: AirItinerary = field(
        default=None,
        metadata=dict(
            name="AirItinerary",
            type="Element",
            required=True
        )
    )
    air_price_result: List[AirPriceResult] = field(
        default_factory=list,
        metadata=dict(
            name="AirPriceResult",
            type="Element",
            min_occurs=1,
            max_occurs=16
        )
    )


@dataclass
class BaseAvailabilitySearchRsp(BaseSearchRsp):
    """Availability Search response.

    :ivar flight_details_list:
    :ivar air_segment_list:
    :ivar fare_info_list:
    :ivar fare_remark_list:
    :ivar air_itinerary_solution:
    :ivar host_token_list:
    :ivar apisrequirements_list:
    :ivar distance_units:
    """
    flight_details_list: FlightDetailsList = field(
        default=None,
        metadata=dict(
            name="FlightDetailsList",
            type="Element"
        )
    )
    air_segment_list: AirSegmentList = field(
        default=None,
        metadata=dict(
            name="AirSegmentList",
            type="Element"
        )
    )
    fare_info_list: FareInfoList = field(
        default=None,
        metadata=dict(
            name="FareInfoList",
            type="Element"
        )
    )
    fare_remark_list: FareRemarkList = field(
        default=None,
        metadata=dict(
            name="FareRemarkList",
            type="Element"
        )
    )
    air_itinerary_solution: List[AirItinerarySolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirItinerarySolution",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token_list: HostTokenList = field(
        default=None,
        metadata=dict(
            name="HostTokenList",
            type="Element"
        )
    )
    apisrequirements_list: ApisrequirementsList = field(
        default=None,
        metadata=dict(
            name="APISRequirementsList",
            type="Element"
        )
    )
    distance_units: str = field(
        default=None,
        metadata=dict(
            name="DistanceUnits",
            type="Attribute",
            length=2
        )
    )


@dataclass
class BrandList:
    """
    :ivar brand:
    """
    brand: List[Brand] = field(
        default_factory=list,
        metadata=dict(
            name="Brand",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class EmdissuanceReq(BaseReq):
    """Electronic Miscellaneous Document issuance request.Supported providers are
    1V/1G/1P/1J.

    :ivar provider_reservation_detail: PNR information for which EMD is going to be issued.
    :ivar ticket_number: Ticket number for which EMD is going to be issued.Required for EMD-A issuance.
    :ivar issuance_modifiers: General modifiers related to EMD issuance.
    :ivar selection_modifiers: Modifiers related to selection of services during EMD issuance.
    :ivar universal_record_locator_code: Represents a valid Universal Record locator code.
    :ivar show_details: This attribute gives the control to request for complete information on Issued EMDs or minimal information.Requesting complete information leads to possible multiple supplier calls for fetching all the details.
    :ivar issue_all_open_svc: Issues EMDS to all SVC segments. If it is true, TicketNumber and SVC segment reference need not be provided. Supported provider 1P.
    """
    provider_reservation_detail: ProviderReservationDetail = field(
        default=None,
        metadata=dict(
            name="ProviderReservationDetail",
            type="Element",
            required=True
        )
    )
    ticket_number: TicketNumber = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element"
        )
    )
    issuance_modifiers: IssuanceModifiers = field(
        default=None,
        metadata=dict(
            name="IssuanceModifiers",
            type="Element"
        )
    )
    selection_modifiers: SelectionModifiers = field(
        default=None,
        metadata=dict(
            name="SelectionModifiers",
            type="Element"
        )
    )
    universal_record_locator_code: str = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            required=True,
            min_length=5.0,
            max_length=8.0
        )
    )
    show_details: bool = field(
        default="false",
        metadata=dict(
            name="ShowDetails",
            type="Attribute"
        )
    )
    issue_all_open_svc: bool = field(
        default="false",
        metadata=dict(
            name="IssueAllOpenSVC",
            type="Attribute"
        )
    )


@dataclass
class EmdissuanceRsp(BaseRsp):
    """Electronic Miscellaneous Document issuance response.Supported providers are
    1V/1G/1P/1J.

    :ivar emdsummary_info: List of EMDSummaryInfo elements to show minimal information in issuance response. Appears for ShowDetails=false in the request.This is the default behaviour.
    :ivar emdinfo: List of EMDInfo elements to show detailoed information in issuance response. Appears for ShowDetails=true in the request.
    """
    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata=dict(
            name="EMDSummaryInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    emdinfo: List[Emdinfo] = field(
        default_factory=list,
        metadata=dict(
            name="EMDInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class EmdretrieveReq(BaseReq):
    """Electronic Miscellaneous Document retrieve request.Supported providers are
    1G/1V/1P/1J.

    :ivar list_retrieve: Provider: 1G/1V/1P/1J-Information required for retrieval of list of EMDs
    :ivar detail_retrieve: Provider: 1G/1V/1P/1J-Information required for a detailed EMD retrieve
    """
    list_retrieve: "EmdretrieveReq.ListRetrieve" = field(
        default=None,
        metadata=dict(
            name="ListRetrieve",
            type="Element",
            required=True
        )
    )
    detail_retrieve: "EmdretrieveReq.DetailRetrieve" = field(
        default=None,
        metadata=dict(
            name="DetailRetrieve",
            type="Element",
            required=True
        )
    )

    @dataclass
    class ListRetrieve:
        """
        :ivar provider_reservation_detail: Provider reservation details to be provided to fetch list of EMDs associated with it.
        """
        provider_reservation_detail: ProviderReservationDetail = field(
            default=None,
            metadata=dict(
                name="ProviderReservationDetail",
                type="Element",
                required=True
            )
        )

    @dataclass
    class DetailRetrieve:
        """
        :ivar provider_reservation_detail: Provider reservation locator to be specified for display operation, if mentioned along woth the EMD number then synchronization of that EMD is performed considering the same to be associated with the mentioned PNR.
        :ivar emdnumber: EMD number to be specified for display operation. If mentioned along with provider reservation detail then synchronization of that EMD is performed considering the same to be associated with the mentioned PNR.
        """
        provider_reservation_detail: ProviderReservationDetail = field(
            default=None,
            metadata=dict(
                name="ProviderReservationDetail",
                type="Element"
            )
        )
        emdnumber: str = field(
            default=None,
            metadata=dict(
                name="EMDNumber",
                type="Element",
                required=True,
                length=13
            )
        )


@dataclass
class EmdretrieveRsp(BaseRsp):
    """Electronic Miscellaneous Document list and detail retrieve
    response.Supported providers are 1G/1V/1P/1J.

    :ivar emdinfo: Provider: 1G/1V/1P/1J.
    :ivar emdsummary_info: Provider: 1G/1V/1P/1J.
    """
    emdinfo: Emdinfo = field(
        default=None,
        metadata=dict(
            name="EMDInfo",
            type="Element",
            required=True
        )
    )
    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata=dict(
            name="EMDSummaryInfo",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightDetailsReq(BaseReq):
    """Request for the Flight Details of segments.

    :ivar air_segment: Provider: 1G,1V,1P,1J.
    """
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightDetailsRsp(BaseRsp):
    """
    :ivar air_segment: Provider: 1G,1V,1P,1J.
    :ivar co2_emissions:
    """
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    co2_emissions: List[Co2Emissions] = field(
        default_factory=list,
        metadata=dict(
            name="CO2Emissions",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class FlightInformationReq(BaseReq):
    """Request for the Flight Info of segments.

    :ivar flight_info_criteria: Provider: 1G,1V.
    """
    flight_info_criteria: List[FlightInfoCriteria] = field(
        default_factory=list,
        metadata=dict(
            name="FlightInfoCriteria",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightInformationRsp(BaseRsp):
    """
    :ivar flight_info: Provider: 1G,1V.
    """
    flight_info: List[FlightInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FlightInfo",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightTimeTableReq(BaseSearchReq):
    """Request for Flight Time Table.

    :ivar flight_time_table_criteria: Provider: 1G,1V.
    """
    flight_time_table_criteria: FlightTimeTableCriteria = field(
        default=None,
        metadata=dict(
            name="FlightTimeTableCriteria",
            type="Element",
            required=True
        )
    )


@dataclass
class FlightTimeTableRsp(BaseSearchRsp):
    """Response for Flight Time Table.

    :ivar flight_time_table_list: Provider: 1G,1V.
    """
    flight_time_table_list: "FlightTimeTableRsp.FlightTimeTableList" = field(
        default=None,
        metadata=dict(
            name="FlightTimeTableList",
            type="Element"
        )
    )

    @dataclass
    class FlightTimeTableList:
        """
        :ivar flight_time_detail:
        """
        flight_time_detail: List[FlightTimeDetail] = field(
            default_factory=list,
            metadata=dict(
                name="FlightTimeDetail",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class RetrieveLowFareSearchReq(BaseReq):
    """Retrieve low fare search responses that were initiated by an asynchronous
    request.

    :ivar search_id: Provider: 1G,1V,1P,1J,ACH-SearchID to be used for Asynchronous LowFareSearch Request
    :ivar provider_code: Provider: 1G,1V,1P,1J,ACH-Provider code of a specific host
    """
    search_id: str = field(
        default=None,
        metadata=dict(
            name="SearchId",
            type="Attribute",
            required=True
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


@dataclass
class SearchSpecificAirSegment:
    """
    :ivar departure_time: The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.
    :ivar carrier: The carrier that is marketing this segment
    :ivar flight_number: The flight number under which the marketing carrier is marketing this flight
    :ivar origin: The IATA location code for this origination of this entity.
    :ivar destination: The IATA location code for this destination of this entity.
    :ivar segment_index: The sequential AirSegment number that this segment connected to.
    """
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            required=True
        )
    )
    carrier: str = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            length=2
        )
    )
    flight_number: str = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            required=True,
            max_length=5.0
        )
    )
    origin: str = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
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
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    segment_index: int = field(
        default=None,
        metadata=dict(
            name="SegmentIndex",
            type="Attribute"
        )
    )


@dataclass
class SeatMapReq(BaseReq):
    """Request a seat map for the give flight information.

    :ivar agency_sell_info: Provider: ACH-Required if the user requesting the seat map is not the same agent authenticated in the request.
    :ivar air_segment: Provider: 1G,1V,1P,1J,ACH,MCH.
    :ivar host_token: Provider: ACH-Required if the carrier has multiple adapters.
    :ivar search_traveler: Provider: 1G,1V,ACH,MCH.
    :ivar host_reservation: Provider: ACH,MCH-Required when seat price is requested.
    :ivar merchandising_pricing_modifiers: Used to provide additional pricing options. Provider:ACH.
    :ivar return_seat_pricing: Provider: 1G,1V,1P,1J,ACH-When set to true the price of the seat will be returned if it exists.
    :ivar return_branding_info: A value of true will return the BrandingInfo block in the response if applicable. A value of false will not return the BrandingInfo block in the response. Providers: 1G, 1V, 1P, 1J, ACH
    """
    agency_sell_info: AgencySellInfo = field(
        default=None,
        metadata=dict(
            name="AgencySellInfo",
            type="Element"
        )
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="SearchTraveler",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_reservation: HostReservation = field(
        default=None,
        metadata=dict(
            name="HostReservation",
            type="Element"
        )
    )
    merchandising_pricing_modifiers: MerchandisingPricingModifiers = field(
        default=None,
        metadata=dict(
            name="MerchandisingPricingModifiers",
            type="Element"
        )
    )
    return_seat_pricing: bool = field(
        default=None,
        metadata=dict(
            name="ReturnSeatPricing",
            type="Attribute",
            required=True
        )
    )
    return_branding_info: bool = field(
        default="false",
        metadata=dict(
            name="ReturnBrandingInfo",
            type="Attribute"
        )
    )


@dataclass
class SeatMapRsp(BaseRsp):
    """
    :ivar host_token: Provider: ACH,MCH.
    :ivar cabin_class: Provider: 1G,1V,1P,1J,ACH,MCH.
    :ivar air_segment: Provider: ACH,MCH.
    :ivar search_traveler: Provider: ACH,MCH.
    :ivar optional_services: A wrapper for all the information regarding each of the Optional Services. Provider: 1G,1V,1P,1J,ACH.
    :ivar remark: Provider: 1G,1V,1P,1J,ACH,MCH.
    :ivar rows:
    :ivar payment_restriction: Provider: MCH-Information regarding valid payment types, if restrictions apply(supplier specific)
    :ivar seat_information:
    :ivar copyright: Copyright text applicable for some seat content. Providers: 1G, 1V, 1P, 1J,ACH
    :ivar group_seat_price: Provider: 1G,1V-Seat price for the all passengers traveling together only when supplier provides group flat fee.
    """
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    cabin_class: CabinClass = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element"
        )
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="SearchTraveler",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    remark: Remark = field(
        default=None,
        metadata=dict(
            name="Remark",
            type="Element"
        )
    )
    rows: List[Rows] = field(
        default_factory=list,
        metadata=dict(
            name="Rows",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    payment_restriction: List[PaymentRestriction] = field(
        default_factory=list,
        metadata=dict(
            name="PaymentRestriction",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    seat_information: List[SeatInformation] = field(
        default_factory=list,
        metadata=dict(
            name="SeatInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    copyright: str = field(
        default=None,
        metadata=dict(
            name="Copyright",
            type="Element"
        )
    )
    group_seat_price: str = field(
        default=None,
        metadata=dict(
            name="GroupSeatPrice",
            type="Attribute"
        )
    )


@dataclass
class AirExchangeMultiQuoteReq(BaseAirExchangeMultiQuoteReq):
    """Request multiple quotes for the exchange of an itinerary. 1P transactions
    only.

    :ivar type: Type choices are "Detail" or "Summary" Default will be Summary
    """
    type: str = field(
        default="Summary",
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )


@dataclass
class AirExchangeMultiQuoteRsp(BaseRsp):
    """
    :ivar air_segment_list:
    :ivar brand_list:
    :ivar air_exchange_mulit_quote_list:
    """
    air_segment_list: List[AirSegmentList] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentList",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    brand_list: List[BrandList] = field(
        default_factory=list,
        metadata=dict(
            name="BrandList",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_exchange_mulit_quote_list: List[AirExchangeMulitQuoteList] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeMulitQuoteList",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeQuoteReq(BaseAirExchangeQuoteReq):
    """Request to quote the exchange of an itinerary."""
    pass


@dataclass
class AirPriceReq(BaseAirPriceReq):
    """Request to price an itinerary in one to many ways.

    Pricing commands can be specified globally, or specifically per command.
    """
    pass


@dataclass
class AirPriceRsp(BaseAirPriceRsp):
    
    pass


@dataclass
class AirRepriceReq(AirBaseReq):
    """Request to reprice a solution.

    :ivar air_reservation_locator_code:
    :ivar air_pricing_solution:
    :ivar fare_rule_type:
    :ivar ignore_availability:
    """
    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element"
        )
    )
    air_pricing_solution: AirPricingSolution = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            required=True
        )
    )
    fare_rule_type: str = field(
        default="none",
        metadata=dict(
            name="FareRuleType",
            type="Attribute"
        )
    )
    ignore_availability: bool = field(
        default="false",
        metadata=dict(
            name="IgnoreAvailability",
            type="Attribute"
        )
    )


@dataclass
class AirSearchReq(BaseSearchReq):
    """Base Request for Air Search.

    :ivar point_of_commencement:
    :ivar air_search_modifiers:
    :ivar journey_data:
    :ivar search_air_leg:
    :ivar search_specific_air_segment:
    """
    point_of_commencement: PointOfCommencement = field(
        default=None,
        metadata=dict(
            name="PointOfCommencement",
            type="Element"
        )
    )
    air_search_modifiers: AirSearchModifiers = field(
        default=None,
        metadata=dict(
            name="AirSearchModifiers",
            type="Element"
        )
    )
    journey_data: JourneyData = field(
        default=None,
        metadata=dict(
            name="JourneyData",
            type="Element"
        )
    )
    search_air_leg: List[SearchAirLeg] = field(
        default_factory=list,
        metadata=dict(
            name="SearchAirLeg",
            type="Element",
            min_occurs=1,
            max_occurs=16
        )
    )
    search_specific_air_segment: List[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="SearchSpecificAirSegment",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirSearchRsp(BaseAvailabilitySearchRsp):
    """Base Response for Air Search.

    :ivar fare_note_list:
    :ivar expert_solution_list:
    :ivar route_list:
    :ivar alternate_route_list:
    :ivar alternate_location_distance_list:
    :ivar fare_info_message:
    :ivar rail_segment_list:
    :ivar rail_journey_list:
    :ivar rail_fare_note_list:
    :ivar rail_fare_idlist:
    :ivar rail_fare_list:
    :ivar rail_pricing_solution:
    :ivar air_pricing_solution:
    :ivar air_price_point_list:
    """
    fare_note_list: FareNoteList = field(
        default=None,
        metadata=dict(
            name="FareNoteList",
            type="Element"
        )
    )
    expert_solution_list: ExpertSolutionList = field(
        default=None,
        metadata=dict(
            name="ExpertSolutionList",
            type="Element"
        )
    )
    route_list: RouteList = field(
        default=None,
        metadata=dict(
            name="RouteList",
            type="Element"
        )
    )
    alternate_route_list: AlternateRouteList = field(
        default=None,
        metadata=dict(
            name="AlternateRouteList",
            type="Element"
        )
    )
    alternate_location_distance_list: AlternateLocationDistanceList = field(
        default=None,
        metadata=dict(
            name="AlternateLocationDistanceList",
            type="Element"
        )
    )
    fare_info_message: List[FareInfoMessage] = field(
        default_factory=list,
        metadata=dict(
            name="FareInfoMessage",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    rail_segment_list: RailSegmentList = field(
        default=None,
        metadata=dict(
            name="RailSegmentList",
            type="Element"
        )
    )
    rail_journey_list: RailJourneyList = field(
        default=None,
        metadata=dict(
            name="RailJourneyList",
            type="Element"
        )
    )
    rail_fare_note_list: RailFareNoteList = field(
        default=None,
        metadata=dict(
            name="RailFareNoteList",
            type="Element"
        )
    )
    rail_fare_idlist: RailFareIdlist = field(
        default=None,
        metadata=dict(
            name="RailFareIDList",
            type="Element"
        )
    )
    rail_fare_list: RailFareList = field(
        default=None,
        metadata=dict(
            name="RailFareList",
            type="Element"
        )
    )
    rail_pricing_solution: List[RailPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="RailPricingSolution",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_price_point_list: AirPricePointList = field(
        default=None,
        metadata=dict(
            name="AirPricePointList",
            type="Element"
        )
    )


@dataclass
class AirTicketingReq(AirBaseReq):
    """Request to ticket a previously stored reservation.

    :ivar air_reservation_locator_code: Provider: 1G,1V,1P,1J.
    :ivar air_pricing_info_ref: Provider: 1G,1V,1P,1J-Indicates air pricing infos to be ticketed.
    :ivar ticketing_modifiers_ref: Provider: 1P,1J-Reference to a shared list of Ticketing Modifiers. This is supported for Worldspan and JAL providers only. When AirPricingInfoRef is used along with TicketingModifiersRef means that particular TicketingModifiers will to be applied while ticketing the Stored fare corresponding to the AirPricingInfo. Absence of AirPricingInfoRef means that particular TicketingModifiers will be applied to all Stored fares which are requested to be ticketed.
    :ivar waiver_code:
    :ivar commission:
    :ivar detailed_billing_information: Provider: 1G,1V.
    :ivar fax_details_information: Provider: 1V.
    :ivar air_ticketing_modifiers: Provider: 1G,1V,1P,1J.
    :ivar air_segment_ticketing_modifiers: Provider: 1P,1J.
    :ivar return_info_on_fail:
    :ivar bulk_ticket: Provider: 1G,1V,1P,1J.
    :ivar validate_spanish_residency: Provider: 1G - If set as true, Spanish Residency will be validated for Provisioned Customers.
    """
    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            required=True
        )
    )
    air_pricing_info_ref: List["AirTicketingReq.AirPricingInfoRef"] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticketing_modifiers_ref: List[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata=dict(
            name="TicketingModifiersRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_code: WaiverCode = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element"
        )
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata=dict(
            name="Commission",
            type="Element",
            min_occurs=0,
            max_occurs=18
        )
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fax_details_information: FaxDetailsInformation = field(
        default=None,
        metadata=dict(
            name="FaxDetailsInformation",
            type="Element"
        )
    )
    air_ticketing_modifiers: List[AirTicketingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirTicketingModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_segment_ticketing_modifiers: List[AirSegmentTicketingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentTicketingModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    return_info_on_fail: bool = field(
        default="true",
        metadata=dict(
            name="ReturnInfoOnFail",
            type="Attribute"
        )
    )
    bulk_ticket: bool = field(
        default="false",
        metadata=dict(
            name="BulkTicket",
            type="Attribute"
        )
    )
    validate_spanish_residency: bool = field(
        default="false",
        metadata=dict(
            name="ValidateSpanishResidency",
            type="Attribute"
        )
    )

    @dataclass
    class AirPricingInfoRef:
        """
        :ivar booking_traveler_ref:
        :ivar key:
        """
        booking_traveler_ref: List[BookingTravelerRef] = field(
            default_factory=list,
            metadata=dict(
                name="BookingTravelerRef",
                type="Element",
                min_occurs=0,
                max_occurs=9
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


@dataclass
class AirUpsellSearchReq(AirBaseReq):
    """Request to search for Upsell Offers based on the Itinerary.

    :ivar air_itinerary: Provider: 1G,1V,1P,1J,ACH-AirItinerary of the pricing request.
    :ivar air_price_result: Provider: 1G,1V,1P,1J,ACH-Result of AirPrice request. Upsell uses this to search for new offer.
    """
    air_itinerary: AirItinerary = field(
        default=None,
        metadata=dict(
            name="AirItinerary",
            type="Element",
            required=True
        )
    )
    air_price_result: List[AirPriceResult] = field(
        default_factory=list,
        metadata=dict(
            name="AirPriceResult",
            type="Element",
            min_occurs=1,
            max_occurs=16
        )
    )


@dataclass
class AirUpsellSearchRsp(BaseAirPriceRsp):
    """Response of Upsell Offers search for the given Itinerary."""
    pass


@dataclass
class AvailabilitySearchRsp(BaseAvailabilitySearchRsp):
    
    pass


@dataclass
class BaseAirSearchReq(BaseCoreSearchReq):
    """Base Request for Low fare air Search.

    :ivar air_search_modifiers:
    :ivar split_ticketing_search:
    :ivar journey_data:
    :ivar search_air_leg:
    :ivar search_specific_air_segment:
    """
    air_search_modifiers: AirSearchModifiers = field(
        default=None,
        metadata=dict(
            name="AirSearchModifiers",
            type="Element"
        )
    )
    split_ticketing_search: SplitTicketingSearch = field(
        default=None,
        metadata=dict(
            name="SplitTicketingSearch",
            type="Element"
        )
    )
    journey_data: JourneyData = field(
        default=None,
        metadata=dict(
            name="JourneyData",
            type="Element"
        )
    )
    search_air_leg: List[SearchAirLeg] = field(
        default_factory=list,
        metadata=dict(
            name="SearchAirLeg",
            type="Element",
            min_occurs=1,
            max_occurs=9
        )
    )
    search_specific_air_segment: List[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="SearchSpecificAirSegment",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AvailabilitySearchReq(AirSearchReq):
    """Availability Search request.

    :ivar search_passenger: Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS passenger
    :ivar point_of_sale: Provider: ACH.
    :ivar return_brand_indicator: When set to “true”, the Brand Indicator can be returned in the availability search response. Provider: 1G, 1V, 1P, 1J, ACH
    :ivar channel_id: A Channel ID is 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.
    :ivar nscc: Allows the agency to bypass/override the Search Control Console rule.
    """
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata=dict(
            name="SearchPassenger",
            type="Element",
            min_occurs=0,
            max_occurs=18
        )
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    return_brand_indicator: bool = field(
        default="false",
        metadata=dict(
            name="ReturnBrandIndicator",
            type="Attribute"
        )
    )
    channel_id: str = field(
        default=None,
        metadata=dict(
            name="ChannelId",
            type="Attribute",
            min_length=2.0,
            max_length=4.0
        )
    )
    nscc: str = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class BaseLowFareSearchReq(BaseAirSearchReq):
    """Base Low Fare Search Request.

    :ivar search_passenger: Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS passenger
    :ivar air_pricing_modifiers: Provider: 1G,1V,1P,1J,ACH.
    :ivar enumeration: Provider: 1G,1V,1P,1J,ACH.
    :ivar air_exchange_modifiers: Provider: ACH.
    :ivar flex_explore_modifiers: This is the container for a set of modifiers which allow the user to perform a special kind of low fare search, depicted as flex explore, based on different parameters like Area, Zone, Country, State, Specific locations, Distance around the actual destination of the itinerary. Applicable for providers 1G,1V,1P.
    :ivar pcc:
    :ivar fare_rules_filter_category:
    :ivar form_of_payment: Provider: 1P,1J
    :ivar enable_point_to_point_search: Provider: 1G,1V,1P,1J,ACH-Indicates that low cost providers should be queried for top connection options and the results returned with the search.
    :ivar enable_point_to_point_alternates: Provider: 1G,1V,1P,1J,ACH-Indicates that suggestions for alternate connection cities for low cost providers should be returned with the search.
    :ivar max_number_of_expert_solutions: Provider: 1G,1V,1P,1J,ACH-Indicates the Maximum Number of Expert Solutions to be returned from the Knowledge Base for the provided search criteria
    :ivar solution_result: Provider: 1G,1V,1P,1J,ACH-Indicates whether the response will contain Solution result (AirPricingSolution) or Non Solution Result (AirPricingPoints). The default value is false. This attribute cannot be combined with EnablePointToPointSearch, EnablePointToPointAlternates and MaxNumberOfExpertSolutions.
    :ivar prefer_complete_itinerary: Provider: ACH-This attribute is only supported for ACH .It works in conjunction with the @SolutionResult flag
    :ivar meta_option_identifier: Invoke Meta Search. Valid values are 00 to 99, or D for the default meta search configuration. When Meta Search not requested, normal LowFareSearch applies. Supported Providers; 1g/1v/1p/1j
    :ivar return_upsell_fare: When set to “true”, Upsell information will be returned in the shop response. Provider supported : 1G, 1V, 1P, 1J
    :ivar include_fare_info_messages: Set to True to return FareInfoMessageList. Providers supported: 1G/1V/1P/1J
    :ivar return_branded_fares: When ReturnBrandedFares is set to “false”, Rich Content and Branding will not be returned in the shop response. When ReturnBrandedFares it is set to “true” or is not sent, Rich Content and Branding will be returned in the shop response. Provider: 1P/1J/ACH.
    :ivar multi_gdssearch: A "true" value indicates MultiGDSSearch. Specific provisioning is required.
    :ivar return_mm: If this attribute is set to “true”, Fare Control Manager processing will be invoked.
    :ivar check_obfees: A flag to return fees for ticketing and for various forms of payment. The default is “TicketingOnly” and will return only ticketing fees. The value “All” will return ticketing fees and the applicable form of payment fees for the form of payment information specified in the request. “FOPOnly” will return the applicable form of payment fees for the form of payment information specified in the request. Form of payment fees are never included in the total unless specific card details are in the request.Provider notes:ACH - CheckOBFees is valid only for LowFareSearch. The valid values are “All”, “TicketingOnly” and “None” and the default value is “None”. 1P/1J -The valid values are “All”, “None” and “TicketingOnly”.1G – All four values are supported.1V/RCH – CheckOBFees are not supported.”
    :ivar nscc: 1 to 3 numeric that defines a Search Control Console filter.This attribute is used to override that filter.
    :ivar fare_info_rules: Returns ChangePenalty and CancelPenalty values at the FareInfo level. If FareRulesFilterCategory is sent FareRulesFilter will be returned at FareInfo level. Provider: 1G/1V.
    """
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata=dict(
            name="SearchPassenger",
            type="Element",
            min_occurs=1,
            max_occurs=18
        )
    )
    air_pricing_modifiers: AirPricingModifiers = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element"
        )
    )
    enumeration: Enumeration = field(
        default=None,
        metadata=dict(
            name="Enumeration",
            type="Element"
        )
    )
    air_exchange_modifiers: AirExchangeModifiers = field(
        default=None,
        metadata=dict(
            name="AirExchangeModifiers",
            type="Element"
        )
    )
    flex_explore_modifiers: FlexExploreModifiers = field(
        default=None,
        metadata=dict(
            name="FlexExploreModifiers",
            type="Element"
        )
    )
    pcc: Pcc = field(
        default=None,
        metadata=dict(
            name="PCC",
            type="Element"
        )
    )
    fare_rules_filter_category: FareRulesFilterCategory = field(
        default=None,
        metadata=dict(
            name="FareRulesFilterCategory",
            type="Element"
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    enable_point_to_point_search: bool = field(
        default="false",
        metadata=dict(
            name="EnablePointToPointSearch",
            type="Attribute"
        )
    )
    enable_point_to_point_alternates: bool = field(
        default="false",
        metadata=dict(
            name="EnablePointToPointAlternates",
            type="Attribute"
        )
    )
    max_number_of_expert_solutions: int = field(
        default="0",
        metadata=dict(
            name="MaxNumberOfExpertSolutions",
            type="Attribute"
        )
    )
    solution_result: bool = field(
        default="false",
        metadata=dict(
            name="SolutionResult",
            type="Attribute"
        )
    )
    prefer_complete_itinerary: bool = field(
        default="true",
        metadata=dict(
            name="PreferCompleteItinerary",
            type="Attribute"
        )
    )
    meta_option_identifier: str = field(
        default=None,
        metadata=dict(
            name="MetaOptionIdentifier",
            type="Attribute",
            min_length=1.0,
            max_length=2.0
        )
    )
    return_upsell_fare: bool = field(
        default="false",
        metadata=dict(
            name="ReturnUpsellFare",
            type="Attribute"
        )
    )
    include_fare_info_messages: bool = field(
        default="false",
        metadata=dict(
            name="IncludeFareInfoMessages",
            type="Attribute"
        )
    )
    return_branded_fares: bool = field(
        default="true",
        metadata=dict(
            name="ReturnBrandedFares",
            type="Attribute"
        )
    )
    multi_gdssearch: bool = field(
        default="false",
        metadata=dict(
            name="MultiGDSSearch",
            type="Attribute"
        )
    )
    return_mm: bool = field(
        default="false",
        metadata=dict(
            name="ReturnMM",
            type="Attribute"
        )
    )
    check_obfees: str = field(
        default=None,
        metadata=dict(
            name="CheckOBFees",
            type="Attribute"
        )
    )
    nscc: str = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            min_length=1.0,
            max_length=3.0
        )
    )
    fare_info_rules: bool = field(
        default="false",
        metadata=dict(
            name="FareInfoRules",
            type="Attribute"
        )
    )


@dataclass
class LowFareSearchAsynchRsp(AirSearchRsp):
    """Asynchronous Low Fare Search Response contains only the 1st Provider
    response unless time out occurs.

    :ivar async_provider_specific_response:
    :ivar brand_list:
    :ivar search_id: Provider: 1G,1V,1P,1J,ACH-Indicates the Search Id of the LFS search
    :ivar currency_type: Provider: 1G,1V,1P,1J,ACH-Specifies the default Currency Type in the response.
    """
    async_provider_specific_response: List[AsyncProviderSpecificResponse] = field(
        default_factory=list,
        metadata=dict(
            name="AsyncProviderSpecificResponse",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    brand_list: BrandList = field(
        default=None,
        metadata=dict(
            name="BrandList",
            type="Element"
        )
    )
    search_id: str = field(
        default=None,
        metadata=dict(
            name="SearchId",
            type="Attribute",
            required=True
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


@dataclass
class LowFareSearchRsp(AirSearchRsp):
    """Low Fare Search Response.

    :ivar brand_list:
    :ivar currency_type: Provider: 1G,1V,1P,1J,ACH.
    """
    brand_list: BrandList = field(
        default=None,
        metadata=dict(
            name="BrandList",
            type="Element"
        )
    )
    currency_type: str = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            required=True,
            length=3
        )
    )


@dataclass
class RetrieveLowFareSearchRsp(AirSearchRsp):
    """Low Fare Search Asynchronous Result response.

    :ivar async_provider_specific_response: Provider: 1G,1V,1P,1J,ACH-Identifies pending responses from a specific provider using MoreResults attribute
    :ivar brand_list:
    :ivar currency_type: Provider: 1G,1V,1P,1J,ACH.
    """
    async_provider_specific_response: List[AsyncProviderSpecificResponse] = field(
        default_factory=list,
        metadata=dict(
            name="AsyncProviderSpecificResponse",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    brand_list: BrandList = field(
        default=None,
        metadata=dict(
            name="BrandList",
            type="Element"
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


@dataclass
class ScheduleSearchReq(AirSearchReq):
    """Schedule Search request."""
    pass


@dataclass
class ScheduleSearchRsp(AirSearchRsp):
    """Schedule Search response."""
    pass


@dataclass
class LowFareSearchAsynchReq(BaseLowFareSearchReq):
    """Asynchronous Low Fare Search request.

    :ivar air_search_asynch_modifiers: Provider: 1G,1V,1P,1J,ACH.
    """
    air_search_asynch_modifiers: AirSearchAsynchModifiers = field(
        default=None,
        metadata=dict(
            name="AirSearchAsynchModifiers",
            type="Element"
        )
    )


@dataclass
class LowFareSearchReq(BaseLowFareSearchReq):
    """Low Fare Search request.

    :ivar policy_reference: This attribute will be used to pass in a value on the request which would be used to link to a ‘Policy Group’ in a policy engine external to UAPI.
    """
    policy_reference: str = field(
        default=None,
        metadata=dict(
            name="PolicyReference",
            type="Attribute",
            min_length=1.0,
            max_length=20.0
        )
    )