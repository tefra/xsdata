from dataclasses import dataclass, field
from typing import List




@dataclass
class CustomProfileInformation:
    """Custom Profile Field Data required for File Finishing."""
    pass


@dataclass
class Location:
    """Used during search to specify an origin or destination location."""
    pass


@dataclass
class TypeAgentInfo:
    
    pass


@dataclass
class TypeSearchTimeSpec:
    
    pass


@dataclass
class AddSvc:
    """
    1P - Add SVC segments to collect additional fee
    :ivar rfic: 1P - Reason for issuance
    :ivar rfisc: 1P - Resaon for issuance sub-code
    :ivar svc_description: 1P - SVC fee description
    :ivar origin: Origin location - Airport code. If this value not provided, the last air segment arrival location is taken as default. 1P only.
    :ivar destination: Destination location - Airport code.
    :ivar start_date: The start date of the SVC segment. If the value not specified, the default value is set as the date next to the last airsegment arrival date. 1P only
    """
    rfic: str = field(
        default=None,
        metadata=dict(
            name="RFIC",
            type="Attribute"
        )
    )
    rfisc: str = field(
        default=None,
        metadata=dict(
            name="RFISC",
            type="Attribute"
        )
    )
    svc_description: str = field(
        default=None,
        metadata=dict(
            name="SvcDescription",
            type="Attribute"
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
    start_date: str = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute"
        )
    )


@dataclass
class AgencySellInfo:
    """Information about the agency selling the reservation.

    :ivar iata_code: The IATA code that pertains to this Agency and Branch.
    :ivar country: The country code of the requesting agency.
    :ivar currency_code: The currency code in which the reservation will be ticketed.
    :ivar provider_code: The IATA assigned airline/GDS code.
    :ivar pseudo_city_code: The PCC in the host system.
    :ivar city_code: IATA code of "home" city or airport.
    """
    iata_code: str = field(
        default=None,
        metadata=dict(
            name="IataCode",
            type="Attribute",
            max_length=8.0
        )
    )
    country: str = field(
        default=None,
        metadata=dict(
            name="Country",
            type="Attribute",
            length=2
        )
    )
    currency_code: str = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            length=3
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
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=2.0,
            max_length=10.0
        )
    )
    city_code: str = field(
        default=None,
        metadata=dict(
            name="CityCode",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )


@dataclass
class AgentIdoverride:
    """Vendor specific agent identifier overrides to be used to access vendor
    systems.

    :ivar supplier_code: Supplier code to determine which vendor this AgentId belongs to.
    :ivar provider_code: Provider code to route the AgentId to proper provider.
    :ivar agent_id: The Agent ID for the applicable supplier/vendor
    """
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            min_length=1.0,
            max_length=5.0
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
    agent_id: str = field(
        default=None,
        metadata=dict(
            name="AgentID",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=32.0
        )
    )


@dataclass
class AgentVoucher:
    """Agent Voucher Form of Payments.

    :ivar number:
    """
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AirSearchParameters:
    """Search Parameters.

    :ivar no_advance_purchase:
    :ivar refundable_fares:
    :ivar non_penalty_fares:
    :ivar un_restricted_fares:
    """
    no_advance_purchase: bool = field(
        default=None,
        metadata=dict(
            name="NoAdvancePurchase",
            type="Attribute"
        )
    )
    refundable_fares: bool = field(
        default=None,
        metadata=dict(
            name="RefundableFares",
            type="Attribute"
        )
    )
    non_penalty_fares: bool = field(
        default=None,
        metadata=dict(
            name="NonPenaltyFares",
            type="Attribute"
        )
    )
    un_restricted_fares: bool = field(
        default=None,
        metadata=dict(
            name="UnRestrictedFares",
            type="Attribute"
        )
    )


@dataclass
class Airport(Location):
    """Airport identifier.

    :ivar code:
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )


@dataclass
class Arcpayment:
    """ARC form of payment.ACH Only.

    :ivar arcidentifier: Value of the ARC Direct Bill id
    :ivar arcpassword: Value of the ARC Direct Bill id password
    """
    arcidentifier: str = field(
        default=None,
        metadata=dict(
            name="ARCIdentifier",
            type="Attribute",
            required=True,
            max_length=128.0
        )
    )
    arcpassword: str = field(
        default=None,
        metadata=dict(
            name="ARCPassword",
            type="Attribute",
            max_length=128.0
        )
    )


@dataclass
class AttrAgentOverride:
    """
    :ivar agent_override: AgentSine value that was used during PNR creation or End Transact.
    """
    agent_override: str = field(
        default=None,
        metadata=dict(
            name="AgentOverride",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )


@dataclass
class AttrAmountPercent:
    """Amount or Percentage.

    :ivar amount: The monetary amount.
    :ivar percentage: The percentage.
    """
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    percentage: str = field(
        default=None,
        metadata=dict(
            name="Percentage",
            type="Attribute",
            pattern="([0-9]{1,2}|100)\.[0-9]{1,2}"
        )
    )


@dataclass
class AttrAppliedProfilePaymentInfo:
    """ProfileID and Key are required in order to reference a payment method from a
    profile.

    :ivar profile_id: The unique ID of the profile that contains the payment details to use.
    :ivar key: The Key assigned to the payment details value from the specified profile.
    """
    profile_id: str = field(
        default=None,
        metadata=dict(
            name="ProfileID",
            type="Attribute"
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
class AttrBookingTravelerGrp:
    """
    :ivar key:
    :ivar traveler_type: Defines the type of traveler used for booking which could be a non-defining type (Companion, Web-fare, etc), or a standard type (Adult, Child, etc).
    :ivar age: BookingTraveler age
    :ivar vip: When set to True indicates that the Booking Traveler is a VIP based on agency/customer criteria
    :ivar dob: Traveler Date of Birth
    :ivar gender: The BookingTraveler gender type
    :ivar nationality: Specify ISO country code for nationality of the Booking Traveler
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    traveler_type: str = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            min_length=3.0,
            max_length=5.0
        )
    )
    age: int = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute"
        )
    )
    vip: bool = field(
        default="false",
        metadata=dict(
            name="VIP",
            type="Attribute"
        )
    )
    dob: str = field(
        default=None,
        metadata=dict(
            name="DOB",
            type="Attribute"
        )
    )
    gender: str = field(
        default=None,
        metadata=dict(
            name="Gender",
            type="Attribute",
            min_length=1.0,
            max_length=2.0
        )
    )
    nationality: str = field(
        default=None,
        metadata=dict(
            name="Nationality",
            type="Attribute",
            length=2
        )
    )


@dataclass
class AttrBookingTravelerName:
    """Details of Booking Traveler Name.

    :ivar prefix: Name prefix.
    :ivar first: First Name.
    :ivar middle: Midle name.
    :ivar last: Last Name.
    :ivar suffix: Name suffix.
    """
    prefix: str = field(
        default=None,
        metadata=dict(
            name="Prefix",
            type="Attribute",
            min_length=1.0,
            max_length=20.0
        )
    )
    first: str = field(
        default=None,
        metadata=dict(
            name="First",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=256.0
        )
    )
    middle: str = field(
        default=None,
        metadata=dict(
            name="Middle",
            type="Attribute",
            min_length=1.0,
            max_length=256.0
        )
    )
    last: str = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=256.0
        )
    )
    suffix: str = field(
        default=None,
        metadata=dict(
            name="Suffix",
            type="Attribute",
            min_length=1.0,
            max_length=256.0
        )
    )


@dataclass
class AttrCommissionRemark:
    """
    :ivar amount: The monetary amount of the commission.
    :ivar percentage: The percent of the commission.
    :ivar commission_cap: Commission cap for the Airline.
    """
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    percentage: str = field(
        default=None,
        metadata=dict(
            name="Percentage",
            type="Attribute",
            pattern="([0-9]{1,2}|100)\.[0-9]{1,2}"
        )
    )
    commission_cap: str = field(
        default=None,
        metadata=dict(
            name="CommissionCap",
            type="Attribute"
        )
    )


@dataclass
class AttrDocument:
    """Containing all document information.

    :ivar document_number: Identifies the document number to be voided.
    :ivar document_type: Identifies the document type to be voided, Document Type can have four values like Service Fee, Paper Ticket , MCO and E-Ticket.
    """
    document_number: str = field(
        default=None,
        metadata=dict(
            name="DocumentNumber",
            type="Attribute",
            min_length=1.0,
            max_length=13.0
        )
    )
    document_type: str = field(
        default=None,
        metadata=dict(
            name="DocumentType",
            type="Attribute"
        )
    )


@dataclass
class AttrDow:
    """Basic attributes used to describe day of week.

    :ivar mon:
    :ivar tue:
    :ivar wed:
    :ivar thu:
    :ivar fri:
    :ivar sat:
    :ivar sun:
    """
    mon: bool = field(
        default=None,
        metadata=dict(
            name="Mon",
            type="Attribute"
        )
    )
    tue: bool = field(
        default=None,
        metadata=dict(
            name="Tue",
            type="Attribute"
        )
    )
    wed: bool = field(
        default=None,
        metadata=dict(
            name="Wed",
            type="Attribute"
        )
    )
    thu: bool = field(
        default=None,
        metadata=dict(
            name="Thu",
            type="Attribute"
        )
    )
    fri: bool = field(
        default=None,
        metadata=dict(
            name="Fri",
            type="Attribute"
        )
    )
    sat: bool = field(
        default=None,
        metadata=dict(
            name="Sat",
            type="Attribute"
        )
    )
    sun: bool = field(
        default=None,
        metadata=dict(
            name="Sun",
            type="Attribute"
        )
    )


@dataclass
class AttrElementKeyResults:
    """ElementStatus and KeyOverride to show the changes in the element keys.

    :ivar el_stat: This attribute is used to show the action results of an element. Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    el_stat: str = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: bool = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class AttrFlexShopping:
    """
    :ivar tier: Indicate the Tier Level
    :ivar days_enabled: Allow or prohibit Flexible Days (within a date range) shopping option
    :ivar weekends_enabled: Allow or prohibit Flexible Weekends shopping option
    :ivar airports_enabled: Allow or prohibit Flexible Airport (choice of Origin and Destination airports) shopping option
    :ivar odenabled: Allow or prohibit Flexible Origin and Destination (choice of airports within a radius) shopping option
    """
    tier: int = field(
        default=None,
        metadata=dict(
            name="Tier",
            type="Attribute"
        )
    )
    days_enabled: bool = field(
        default=None,
        metadata=dict(
            name="DaysEnabled",
            type="Attribute"
        )
    )
    weekends_enabled: bool = field(
        default=None,
        metadata=dict(
            name="WeekendsEnabled",
            type="Attribute"
        )
    )
    airports_enabled: bool = field(
        default=None,
        metadata=dict(
            name="AirportsEnabled",
            type="Attribute"
        )
    )
    odenabled: bool = field(
        default=None,
        metadata=dict(
            name="ODEnabled",
            type="Attribute"
        )
    )


@dataclass
class AttrFlightTimes:
    """Basic attributes used to describe flight time information.

    :ivar flight_time: Time spent (minutes) traveling in flight, including airport taxi time.
    :ivar travel_time: Total time spent (minutes) traveling including flight time and ground time.
    :ivar distance: The distance traveled. Units are specified in the parent response element.
    """
    flight_time: int = field(
        default=None,
        metadata=dict(
            name="FlightTime",
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
    distance: int = field(
        default=None,
        metadata=dict(
            name="Distance",
            type="Attribute"
        )
    )


@dataclass
class AttrLocatorInfo:
    """Holds the Universal Record and Provider Reservation Locators for an
    individual product.

    :ivar universal_record_locator_code: Contains the Locator Code of the Universal Record that houses this reservation.
    :ivar provider_code: Contains the Provider Code of the provider that houses this reservation.
    :ivar provider_locator_code: Contains the Locator Code of the Provider Reservation that houses this reservation.
    """
    universal_record_locator_code: str = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            min_length=5.0,
            max_length=8.0
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
            type="Attribute",
            max_length=15.0
        )
    )


@dataclass
class AttrLoyalty:
    """
    :ivar key:
    :ivar supplier_code: The code used to identify the Loyalty supplier, e.g. AA, ZE, MC
    :ivar alliance_level:
    :ivar membership_program: Loyalty Program membership Id of the traveler specific to Amtrak(2V) Guest Rewards
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            required=True,
            length=2
        )
    )
    alliance_level: str = field(
        default=None,
        metadata=dict(
            name="AllianceLevel",
            type="Attribute"
        )
    )
    membership_program: str = field(
        default=None,
        metadata=dict(
            name="MembershipProgram",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )


@dataclass
class AttrName:
    """Basic attributes used to describe a name.

    :ivar prefix:
    :ivar first:
    :ivar middle:
    :ivar last:
    :ivar suffix:
    """
    prefix: str = field(
        default=None,
        metadata=dict(
            name="Prefix",
            type="Attribute"
        )
    )
    first: str = field(
        default=None,
        metadata=dict(
            name="First",
            type="Attribute"
        )
    )
    middle: str = field(
        default=None,
        metadata=dict(
            name="Middle",
            type="Attribute"
        )
    )
    last: str = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            required=True,
            min_length=1.0
        )
    )
    suffix: str = field(
        default=None,
        metadata=dict(
            name="Suffix",
            type="Attribute"
        )
    )


@dataclass
class AttrOrigDestDepatureInfo:
    """Basic attributes used to describe an origin destination pair.

    :ivar origin: The IATA location code for this origination of this entity.
    :ivar destination: The IATA location code for this destination of this entity.
    :ivar departure_time: The date and time at which this entity departs. Date and time are represented as Airport Local Time at the place of departure. The correct time zone offset is also included.
    :ivar arrival_time: The date and time at which this entity arrives at the destination. Date and time are represented as Airport Local Time at the place of arrival. The correct time zone offset is also included.
    """
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
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute"
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
class AttrOrigDestInfo:
    """Basic attributes used to describe an origin destination pair.

    :ivar origin: The IATA location code for this origination of this entity.
    :ivar destination: The IATA location code for this destination of this entity.
    :ivar departure_time: The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.
    :ivar arrival_time: The date and time at which this entity arrives at the destination. This does not include time zone information since it can be derived from the origin location.
    """
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
class AttrPolicyMarking:
    """
    :ivar in_policy: This attribute will be used to indicate if a fare or rate has been determined to be ‘in policy’ based on the associated policy settings.
    :ivar policy_code: This attribute is used to provide a code that can be used to determine why an item was determined to be ‘out of policy’.
    :ivar preferred_option: This attribute is used to indicate if the vendors responsible for the fare or rate being returned have been determined to be ‘preferred’ based on the associated policy settings.
    """
    in_policy: bool = field(
        default=None,
        metadata=dict(
            name="InPolicy",
            type="Attribute"
        )
    )
    policy_code: int = field(
        default=None,
        metadata=dict(
            name="PolicyCode",
            type="Attribute",
            min_inclusive=1.0,
            max_inclusive=9999.0
        )
    )
    preferred_option: bool = field(
        default=None,
        metadata=dict(
            name="PreferredOption",
            type="Attribute"
        )
    )


@dataclass
class AttrPrices:
    """Basic monetary value for Air pricing structures.

    :ivar total_price: The total price for this entity including base price and all taxes.
    :ivar base_price: Represents the base price for this entity. This does not include any taxes or surcharges.
    :ivar approximate_total_price: The Converted total price in Default Currency for this entity including base price and all taxes.
    :ivar approximate_base_price: The Converted base price in Default Currency for this entity. This does not include any taxes or surcharges.
    :ivar equivalent_base_price: Represents the base price in the related currency for this entity. This does not include any taxes or surcharges.
    :ivar taxes: The aggregated amount of all the taxes that are associated with this entity. See the associated TaxInfo array for a breakdown of the individual taxes.
    :ivar fees: The aggregated amount of all the fees that are associated with this entity. See the associated FeeInfo array for a breakdown of the individual fees.
    :ivar services: The total cost for all optional services.
    :ivar approximate_taxes: The Converted tax amount in Default Currency.
    :ivar approximate_fees: The Converted fee amount in Default Currency.
    """
    total_price: str = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute"
        )
    )
    base_price: str = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute"
        )
    )
    approximate_total_price: str = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute"
        )
    )
    approximate_base_price: str = field(
        default=None,
        metadata=dict(
            name="ApproximateBasePrice",
            type="Attribute"
        )
    )
    equivalent_base_price: str = field(
        default=None,
        metadata=dict(
            name="EquivalentBasePrice",
            type="Attribute"
        )
    )
    taxes: str = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    fees: str = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Attribute"
        )
    )
    services: str = field(
        default=None,
        metadata=dict(
            name="Services",
            type="Attribute"
        )
    )
    approximate_taxes: str = field(
        default=None,
        metadata=dict(
            name="ApproximateTaxes",
            type="Attribute"
        )
    )
    approximate_fees: str = field(
        default=None,
        metadata=dict(
            name="ApproximateFees",
            type="Attribute"
        )
    )


@dataclass
class AttrProviderSupplier:
    """Attributes used to uniquely describe a content source.

    :ivar provider_code:
    :ivar supplier_code:
    """
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2.0,
            max_length=5.0
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


@dataclass
class AttrQueueInfo:
    """Attributes related to queue information.

    :ivar queue: Queue Number . Possible values are 01, AA , A1 etc.
    :ivar category: Queue Category Number. 2 Character Alpha or Numeric Number.
    Either Alpha or Numeric Number is allowed.
    If using for Sabre is mandatory and is Prefatory Instruction Code value of 0-999.
    :ivar date_range: Date range number where the PNR should be queued. Possible values are 1,2,1-4 etc.
    """
    queue: str = field(
        default=None,
        metadata=dict(
            name="Queue",
            type="Attribute"
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute"
        )
    )
    date_range: str = field(
        default=None,
        metadata=dict(
            name="DateRange",
            type="Attribute"
        )
    )


@dataclass
class AttrReqRspInfo:
    """Basic information on all request response pairs.

    :ivar transaction_id: Unique identifier for this atomic transaction. Use is optional.
    """
    transaction_id: str = field(
        default=None,
        metadata=dict(
            name="TransactionId",
            type="Attribute"
        )
    )


@dataclass
class AttrTaxDetail:
    """Holds fare quote tax information.

    :ivar amount:
    :ivar origin_airport:
    :ivar destination_airport:
    :ivar country_code:
    :ivar fare_info_ref:
    """
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True
        )
    )
    origin_airport: str = field(
        default=None,
        metadata=dict(
            name="OriginAirport",
            type="Attribute",
            length=3
        )
    )
    destination_airport: str = field(
        default=None,
        metadata=dict(
            name="DestinationAirport",
            type="Attribute",
            length=3
        )
    )
    country_code: str = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Attribute"
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
class AttrTicketNumberStatus:
    """
    :ivar number:
    :ivar status:
    :ivar name:
    """
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            required=True,
            length=1
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute"
        )
    )


@dataclass
class Auxdata:
    """
    :ivar entry:
    """
    entry: List["Auxdata.Entry"] = field(
        default_factory=list,
        metadata=dict(
            name="Entry",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )

    @dataclass
    class Entry:
        """
        :ivar reason:
        :ivar description:
        """
        reason: str = field(
            default=None,
            metadata=dict(
                name="Reason",
                type="Element",
                required=True
            )
        )
        description: str = field(
            default=None,
            metadata=dict(
                name="Description",
                type="Element",
                required=True
            )
        )


@dataclass
class BaseAsyncProviderSpecificResponse:
    """Identifies pending responses from a specific provider using MoreResults
    attribute.

    :ivar provider_code: Provider code of a specific host
    :ivar more_results: Identifies whether more results are available for specific host or not.
    """
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
    more_results: bool = field(
        default=None,
        metadata=dict(
            name="MoreResults",
            type="Attribute",
            required=True
        )
    )


@dataclass
class BillingPointOfSaleInfo:
    """Point of Sale information for Billing.

    :ivar origin_application: Name of the Point of Sale application which initiated the Request.This information will be provided as part of the provisioning of the user.
    :ivar cidbnumber: A 10 Digit customer number generated by CIDB system.
    """
    origin_application: str = field(
        default=None,
        metadata=dict(
            name="OriginApplication",
            type="Attribute",
            required=True
        )
    )
    cidbnumber: int = field(
        default=None,
        metadata=dict(
            name="CIDBNumber",
            type="Attribute",
            pattern="\d{10}"
        )
    )


@dataclass
class BookingDates:
    """Check in and Check out Date information.

    :ivar check_in_date:
    :ivar check_out_date:
    """
    check_in_date: str = field(
        default=None,
        metadata=dict(
            name="CheckInDate",
            type="Attribute",
            pattern="[^:Z].*"
        )
    )
    check_out_date: str = field(
        default=None,
        metadata=dict(
            name="CheckOutDate",
            type="Attribute",
            pattern="[^:Z].*"
        )
    )


@dataclass
class BookingSource:
    """
    :ivar code: Alternate booking source code or number.
    :ivar type: Type of booking source sent in the Code attribute. Possible values are “PseudoCityCode”,” ArcNumber”,” IataNumber”, “CustomerId” and “BookingSourceOverrride”. “BookingSourceOverrride” is only applicable in VehicleCreateReservationReq. 1P/1J.
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1.0
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
class Bsppayment:
    """BSP form of payment.ACH Only.

    :ivar bspidentifier: Value of the BSP Direct Bill id
    :ivar bsppassword: Value of the BSP Direct Bill id password
    """
    bspidentifier: str = field(
        default=None,
        metadata=dict(
            name="BSPIdentifier",
            type="Attribute",
            required=True,
            max_length=128.0
        )
    )
    bsppassword: str = field(
        default=None,
        metadata=dict(
            name="BSPPassword",
            type="Attribute",
            max_length=128.0
        )
    )


@dataclass
class CabinClass:
    """Requests cabin class (First, Business and Economy, etc.) as supported by the
    provider or supplier.

    :ivar type:
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Carrier:
    """Carrier identifier.

    :ivar code:
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            length=2
        )
    )


@dataclass
class Certificate:
    """Certificate Form of Payment.

    :ivar number: The Certificate number
    :ivar amount: The monetary value of the certificate.
    :ivar discount_amount: The monetary discount amount of this certificate.
    :ivar discount_percentage: The percentage discount value of this certificate.
    :ivar not_valid_before: The date that this certificate becomes valid.
    :ivar not_valid_after: The date that this certificate expires.
    """
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
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
    discount_amount: str = field(
        default=None,
        metadata=dict(
            name="DiscountAmount",
            type="Attribute"
        )
    )
    discount_percentage: int = field(
        default=None,
        metadata=dict(
            name="DiscountPercentage",
            type="Attribute"
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
class Characteristic:
    """Identifies the characteristics of the seat with seat type, value and
    description.

    :ivar seat_type: Indicates codeset of values such as Seat Type like Place,Position, Smoking Choice, Place Arrangement, Place Direction, Compartment.
    :ivar seat_description: Description of the seat type.
    :ivar seat_value: Indicates the value specific to the selected type.
    :ivar seat_value_description: Description of the seat value.
    """
    seat_type: str = field(
        default=None,
        metadata=dict(
            name="SeatType",
            type="Attribute",
            min_length=0.0,
            max_length=255.0
        )
    )
    seat_description: str = field(
        default=None,
        metadata=dict(
            name="SeatDescription",
            type="Attribute",
            min_length=0.0,
            max_length=255.0
        )
    )
    seat_value: str = field(
        default=None,
        metadata=dict(
            name="SeatValue",
            type="Attribute",
            min_length=0.0,
            max_length=255.0
        )
    )
    seat_value_description: str = field(
        default=None,
        metadata=dict(
            name="SeatValueDescription",
            type="Attribute",
            min_length=0.0,
            max_length=255.0
        )
    )


@dataclass
class Check:
    """Check Form of Payment.

    :ivar micrnumber: Magnetic Ink Character Reader Number of check.
    :ivar routing_number: The bank routing number of the check.
    :ivar account_number: The account number of the check
    :ivar check_number: The sequential check number of the check.
    """
    micrnumber: str = field(
        default=None,
        metadata=dict(
            name="MICRNumber",
            type="Attribute",
            max_length=29.0
        )
    )
    routing_number: str = field(
        default=None,
        metadata=dict(
            name="RoutingNumber",
            type="Attribute"
        )
    )
    account_number: str = field(
        default=None,
        metadata=dict(
            name="AccountNumber",
            type="Attribute"
        )
    )
    check_number: str = field(
        default=None,
        metadata=dict(
            name="CheckNumber",
            type="Attribute"
        )
    )


@dataclass
class City(Location):
    """City identifier.

    :ivar code:
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )


@dataclass
class CityOrAirport(Location):
    """This element can be used when it is not known whether the value is an
    airport or a city code.

    :ivar code: The airport or city IATA code.
    :ivar prefer_city: Indicates that the search should prefer city results over airport results.
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    prefer_city: bool = field(
        default="false",
        metadata=dict(
            name="PreferCity",
            type="Attribute"
        )
    )


@dataclass
class Commission:
    """Identifies the agency commission.

    :ivar key:
    :ivar level: The commission percentage level.
    :ivar type: The commission type.
    :ivar modifier: Optional commission modifier.
    :ivar amount: The monetary amount of the commission.
    :ivar value: Contains alphanumeric or alpha characters intended as 1G Value Code as applicable by BSP of client.
    :ivar percentage: The percent of the commission.
    :ivar booking_traveler_ref: A reference to a passenger.
    :ivar commission_override: This is enabled to override CAT-35 commission error during air ticketing. PROVIDER SUPPORTED:Worldspan and JAL
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    level: str = field(
        default=None,
        metadata=dict(
            name="Level",
            type="Attribute",
            required=True
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
    modifier: str = field(
        default=None,
        metadata=dict(
            name="Modifier",
            type="Attribute"
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            min_length=0.0,
            max_length=15.0
        )
    )
    percentage: str = field(
        default=None,
        metadata=dict(
            name="Percentage",
            type="Attribute",
            pattern="([0-9]{1,2}|100)\.[0-9]{1,2}"
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute"
        )
    )
    commission_override: bool = field(
        default="false",
        metadata=dict(
            name="CommissionOverride",
            type="Attribute"
        )
    )


@dataclass
class ContinuityCheckOverride:
    """
    :ivar value:
    :ivar key: Will use key to map continuity remark to a particular segment
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_length=1.0,
            white_space="collapse"
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
class CoordinateLocation(Location):
    """Specific lat/long location, usually associated with a Distance.

    :ivar latitude:
    :ivar longitude:
    """
    latitude: float = field(
        default=None,
        metadata=dict(
            name="latitude",
            type="Attribute",
            required=True
        )
    )
    longitude: float = field(
        default=None,
        metadata=dict(
            name="longitude",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CorporateDiscountId(str):
    """These are zero or more negotiated rate codes.

    :ivar negotiated_rate_code: When set to true, the data in the CorporateDiscountID is a negotiated rate code. Otherwise, this data is a Corporate Discount ID rate.
    """
    negotiated_rate_code: bool = field(
        default=None,
        metadata=dict(
            name="NegotiatedRateCode",
            type="Attribute"
        )
    )


@dataclass
class Credentials:
    """Container to send login id and password on each request.

    :ivar user_id: The UserID associated with the entity using this request withing this BranchCode.
    """
    user_id: str = field(
        default=None,
        metadata=dict(
            name="UserId",
            type="Attribute",
            required=True,
            max_length=36.0
        )
    )


@dataclass
class CreditCardAuth:
    """The result of a Credit Auth Request. Will contain all the authorization info
    and result codes.

    :ivar key:
    :ivar payment_ref:
    :ivar trans_id: The transaction id from the credit processing system
    :ivar number:
    :ivar amount: The amount that was authorized.
    :ivar auth_code: The authorization code to confirm card acceptance
    :ivar auth_result_code: The result code of the authorization command.
    :ivar avsresult_code: The address verification result code (if AVS was requested)
    :ivar message: The message explains the result of the authorization command.
    :ivar provider_reservation_info_ref:
    :ivar form_of_payment_ref:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    payment_ref: str = field(
        default=None,
        metadata=dict(
            name="PaymentRef",
            type="Attribute"
        )
    )
    trans_id: str = field(
        default=None,
        metadata=dict(
            name="TransId",
            type="Attribute"
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            min_length=13.0,
            max_length=128.0
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True
        )
    )
    auth_code: str = field(
        default=None,
        metadata=dict(
            name="AuthCode",
            type="Attribute"
        )
    )
    auth_result_code: str = field(
        default=None,
        metadata=dict(
            name="AuthResultCode",
            type="Attribute",
            required=True
        )
    )
    avsresult_code: str = field(
        default=None,
        metadata=dict(
            name="AVSResultCode",
            type="Attribute"
        )
    )
    message: str = field(
        default=None,
        metadata=dict(
            name="Message",
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
    form_of_payment_ref: str = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Attribute"
        )
    )


@dataclass
class CustomizedNameData(str):
    """Customized Name Data is used to print customized name on the different
    documents.

    :ivar key:
    :ivar provider_reservation_info_ref:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
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


@dataclass
class DirectPayment:
    """Direct Payment Form of Payments.

    :ivar text:
    """
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute"
        )
    )


@dataclass
class DiscountCardRef:
    """
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
class Distance:
    """Container to encapsulate the a distance value with its unit of measure.

    :ivar units:
    :ivar value:
    :ivar direction: Directions: S, N, E, W, SE, NW, ...
    """
    units: str = field(
        default="MI",
        metadata=dict(
            name="Units",
            type="Attribute",
            length=2
        )
    )
    value: int = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True
        )
    )
    direction: str = field(
        default=None,
        metadata=dict(
            name="Direction",
            type="Attribute",
            max_length=2.0
        )
    )


@dataclass
class DriversLicenseRef:
    """
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
class EmailNotification:
    """
    Send Email Notification to the emails specified in Booking Traveler. Supported Provider : 1G/1V
    :ivar email_ref: Reference to Booking Traveler Email.
    :ivar recipients: Indicates the recipients of the mail addresses for which the user requires the system to send the itinerary.List of Possible Values: All = Send Email to All addresses Default = Send Email to Primary Booking Traveler Specific = Send Email to specific address Referred in EmailRef.
    """
    email_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="EmailRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    recipients: str = field(
        default=None,
        metadata=dict(
            name="Recipients",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Endorsement:
    """Restrictions or instructions about the fare or ticket.

    :ivar value:
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=256.0
        )
    )


@dataclass
class EnettVan:
    """Container for all eNett Van information.

    :ivar min_percentage: The minimum percentage that will be applied on the Total price and sent to enett,which will denote the minimum authorized amount approved by eNett.uApi will default this to zero for multi-use Van's.
    :ivar max_percentage: The maximum percentage that will be applied on the Total price and sent to enett, which will denote the maximum authorized amount as approved by eNett. This value will be ignored and not used for Multi-Use VAN’s.
    :ivar expiry_days: The number of days from the VAN generation date that the VAN will be active for, after which the VAN cannot be used.
    :ivar multi_use: Acceptable values are true or false. If set to true it will denote that the VAN being requested is multi-use else it will indicate a single -use VAN.A Single use VAN can only be debited once while the multiple use VAN's can be debited multiple times subjected to the maximum value it has been authorized for. The default value will be TRUE to indicate a multi-use VAN is being issued.
    """
    min_percentage: int = field(
        default=None,
        metadata=dict(
            name="MinPercentage",
            type="Attribute",
            min_inclusive=0.0,
            max_inclusive=100.0
        )
    )
    max_percentage: int = field(
        default=None,
        metadata=dict(
            name="MaxPercentage",
            type="Attribute",
            min_inclusive=0.0,
            max_inclusive=100.0
        )
    )
    expiry_days: str = field(
        default=None,
        metadata=dict(
            name="ExpiryDays",
            type="Attribute",
            min_inclusive="P1D",
            max_inclusive="P366D"
        )
    )
    multi_use: bool = field(
        default="true",
        metadata=dict(
            name="MultiUse",
            type="Attribute"
        )
    )


@dataclass
class ExchangedCoupon:
    """The coupon numbers that were used in the exchange process to create the MCO.

    :ivar ticket_number: The ticket number for which the exchange coupons are present.
    :ivar coupon_number: Coupon numbers that were exchanged specific to this ticket
    """
    ticket_number: str = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            required=True,
            length=13
        )
    )
    coupon_number: str = field(
        default=None,
        metadata=dict(
            name="CouponNumber",
            type="Attribute"
        )
    )


@dataclass
class FormOfPaymentRef:
    """A reference to a Form of Payment in the existing UR.

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
class FormattedTextTextType(str):
    """Provides text and indicates whether it is formatted or not.

    :ivar formatted: Textual information, which may be formatted as a line of information, or unformatted, as a paragraph of text.
    :ivar text_format: Indicates the format of text used in the description e.g. unformatted or html.
    """
    formatted: bool = field(
        default=None,
        metadata=dict(
            name="Formatted",
            type="Attribute"
        )
    )
    text_format: str = field(
        default=None,
        metadata=dict(
            name="TextFormat",
            type="Attribute"
        )
    )


@dataclass
class GuaranteeType:
    """A type of guarantee i.e.

    :ivar value:
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            max_length=250.0
        )
    )


@dataclass
class HostToken(str):
    """This is a host token. It contains some kind of payload we got from a host
    that must be passed in on successive calls they know who you are as our system
    does not maintain state. The format of this string isn't important as long as
    it is not altered in any way between calls. Since a host token is only valid on
    the host it is assocated with, there is also an attribute called Host so we
    know how to route the command(s). You can have multiple active sessions between
    one or more hosts.

    :ivar host: The host associated with this token
    :ivar key: Unique identifier for this token - use this key when a single HostToken is shared by multiple elements.
    """
    host: str = field(
        default=None,
        metadata=dict(
            name="Host",
            type="Attribute",
            min_length=2.0,
            max_length=5.0
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
class IncludedInBase:
    """Shows the taxes and fees included in the base fare. (ACH only)

    :ivar amount: this attribute shows the amount included in the base fare for the specific fee or tax
    """
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )


@dataclass
class IndustryStandardSsr:
    """Indicates Carrier Supports this industry standard.

    :ivar code: This code indicates which Standard of SSR's they support. Sucha as the 'AIRIMP' standard identified by 'IATA.org'
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute"
        )
    )


@dataclass
class KeyMapping:
    """Element for which mapping key sent in the request is different from the
    mapping key comes in the response.

    :ivar element_name: Name of the element.
    :ivar original_key: The mapping key which is sent in the request.
    :ivar new_key: The mapping key that comes in the response.
    """
    element_name: str = field(
        default=None,
        metadata=dict(
            name="ElementName",
            type="Attribute",
            required=True
        )
    )
    original_key: str = field(
        default=None,
        metadata=dict(
            name="OriginalKey",
            type="Attribute",
            required=True
        )
    )
    new_key: str = field(
        default=None,
        metadata=dict(
            name="NewKey",
            type="Attribute",
            required=True
        )
    )


@dataclass
class LanguageGroup:
    """Identifies language.

    :ivar language: Language identification.
    """
    language: str = field(
        default=None,
        metadata=dict(
            name="Language",
            type="Attribute"
        )
    )


@dataclass
class LocatorCode:
    """A locator code that identifies a PNR or searches for one.

    :ivar value:
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_length=1.0
        )
    )


@dataclass
class LoyaltyCardRef:
    """
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
class MarketingInformation:
    """Marketing text or Notices for Suppliers.

    :ivar text:
    """
    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class Mcoremark(str):
    """Information related to fare construction, free form text etc. of the MCO.

    :ivar additional_rmk: Indicates if the remark is additional remark or not.
    """
    additional_rmk: bool = field(
        default=None,
        metadata=dict(
            name="AdditionalRmk",
            type="Attribute"
        )
    )


@dataclass
class MealRequest:
    """Special meal requests like Vegetarian.

    :ivar type:
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True,
            length=4
        )
    )


@dataclass
class MediaItem:
    """Photos and other media urls for the property referenced above.

    :ivar caption:
    :ivar height:
    :ivar width:
    :ivar type:
    :ivar url:
    :ivar icon:
    :ivar size_code:
    """
    caption: str = field(
        default=None,
        metadata=dict(
            name="caption",
            type="Attribute"
        )
    )
    height: int = field(
        default=None,
        metadata=dict(
            name="height",
            type="Attribute"
        )
    )
    width: int = field(
        default=None,
        metadata=dict(
            name="width",
            type="Attribute"
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute"
        )
    )
    url: str = field(
        default=None,
        metadata=dict(
            name="url",
            type="Attribute"
        )
    )
    icon: str = field(
        default=None,
        metadata=dict(
            name="icon",
            type="Attribute"
        )
    )
    size_code: str = field(
        default=None,
        metadata=dict(
            name="sizeCode",
            type="Attribute"
        )
    )


@dataclass
class MetaData:
    """Extra data to elaborate the parent element. This data is primarily
    informative and is not persisted.

    :ivar key:
    :ivar value:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=10.0
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=50.0
        )
    )


@dataclass
class MiscFormOfPayment:
    """Miscellaneous Form of Payments.

    :ivar credit_card_type: The 2 letter credit/ debit card type or code which may not have been issued using the standard bank card types - i.e. an airline issued card
    :ivar credit_card_number:
    :ivar exp_date: The Expiration date of this card in YYYY-MM format.
    :ivar text: Any free form text which may be associated with the Miscellaneous Form of Payment. This text may be provider or GDS specific
    :ivar category: Indicates what Category the Miscellaneous Form Of Payment is being used for payment - The category may vary by GDS.
    Allowable values are "Text" "Credit" "CreditCard" "FreeFormCreditCard" "Invoice" "NonRefundable" "MultipleReceivables" "Exchange" "Cash"
    :ivar acceptance_override: Override airline restriction on the credit card.
    """
    credit_card_type: str = field(
        default=None,
        metadata=dict(
            name="CreditCardType",
            type="Attribute",
            length=2
        )
    )
    credit_card_number: str = field(
        default=None,
        metadata=dict(
            name="CreditCardNumber",
            type="Attribute",
            min_length=13.0,
            max_length=128.0
        )
    )
    exp_date: str = field(
        default=None,
        metadata=dict(
            name="ExpDate",
            type="Attribute"
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute"
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            required=True
        )
    )
    acceptance_override: bool = field(
        default=None,
        metadata=dict(
            name="AcceptanceOverride",
            type="Attribute"
        )
    )


@dataclass
class ModificationRulesGroup:
    """Groups the rules for handling options when modifying an itinerary. One
    attribute group repreents the rules for a particular type of modification
    supported by the adapter for a single modification type.

    :ivar modification: The modificaiton for which this rule group applies.
    :ivar automatically_applied_on_add: Indicates if the option will be automatically added to new segments / passengers in the itinerary.
    :ivar can_delete: Indicates if the option can be deleted from the itinerary without segment or passenger modifications
    :ivar can_add: Indicates if the option can be added to the itinerary without segment or passenger modification
    :ivar refundable: Indicates if the price of the option is refundable.
    :ivar provider_defined_modification_type: Indicates the actual provider defined modification type which is mapped to Other
    """
    modification: str = field(
        default=None,
        metadata=dict(
            name="Modification",
            type="Attribute",
            required=True
        )
    )
    automatically_applied_on_add: bool = field(
        default="false",
        metadata=dict(
            name="AutomaticallyAppliedOnAdd",
            type="Attribute"
        )
    )
    can_delete: bool = field(
        default=None,
        metadata=dict(
            name="CanDelete",
            type="Attribute"
        )
    )
    can_add: bool = field(
        default=None,
        metadata=dict(
            name="CanAdd",
            type="Attribute"
        )
    )
    refundable: bool = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute"
        )
    )
    provider_defined_modification_type: str = field(
        default=None,
        metadata=dict(
            name="ProviderDefinedModificationType",
            type="Attribute"
        )
    )


@dataclass
class Name:
    """Complete name fields.

    :ivar prefix: Name prefix. Size can be up to 20 characters
    :ivar first: First Name. Size can be up to 256 characters
    :ivar middle: Midle name. Size can be up to 256 characters
    :ivar last: Last Name. Size can be up to 256 characters
    :ivar suffix: Name suffix. Size can be up to 256 characters
    :ivar traveler_profile_id: Traveler Applied Profile ID.
    """
    prefix: str = field(
        default=None,
        metadata=dict(
            name="Prefix",
            type="Attribute",
            min_length=1.0,
            max_length=20.0
        )
    )
    first: str = field(
        default=None,
        metadata=dict(
            name="First",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=256.0
        )
    )
    middle: str = field(
        default=None,
        metadata=dict(
            name="Middle",
            type="Attribute",
            min_length=1.0,
            max_length=256.0
        )
    )
    last: str = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=256.0
        )
    )
    suffix: str = field(
        default=None,
        metadata=dict(
            name="Suffix",
            type="Attribute",
            min_length=1.0,
            max_length=256.0
        )
    )
    traveler_profile_id: int = field(
        default=None,
        metadata=dict(
            name="TravelerProfileId",
            type="Attribute"
        )
    )


@dataclass
class NameOverride:
    """To be used if the name is different from booking travelers in the PNR.

    :ivar first: First Name.
    :ivar last: Last Name.
    :ivar age: Age.
    """
    first: str = field(
        default=None,
        metadata=dict(
            name="First",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=256.0
        )
    )
    last: str = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=256.0
        )
    )
    age: int = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute"
        )
    )


@dataclass
class NextResultReference:
    """Container to return/send additional retrieve/request additional search
    results.

    :ivar value:
    :ivar provider_code: The code of the Provider (e.g 1G,1S)
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_length=1.0,
            white_space="collapse"
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


@dataclass
class OperatedBy:
    """This is the carrier code to support Cross Accrual.

    :ivar value:
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_length=1.0,
            white_space="collapse"
        )
    )


@dataclass
class OptionalServiceApplicabilityLimitGroup:
    """Holds the limits on how many options of the particular type can be applied.

    :ivar applicable_level: Indicates the applicable level for the option
    :ivar provider_defined_applicable_levels: Indicates the actual provider defined ApplicableLevels which is mapped to Other
    :ivar maximum_quantity: The maximum quantity allowed for the type
    :ivar minimum_quantity: Indicates the minimum number of the option that can be selected.
    """
    applicable_level: str = field(
        default=None,
        metadata=dict(
            name="ApplicableLevel",
            type="Attribute",
            required=True
        )
    )
    provider_defined_applicable_levels: str = field(
        default=None,
        metadata=dict(
            name="ProviderDefinedApplicableLevels",
            type="Attribute"
        )
    )
    maximum_quantity: int = field(
        default=None,
        metadata=dict(
            name="MaximumQuantity",
            type="Attribute",
            required=True
        )
    )
    minimum_quantity: int = field(
        default=None,
        metadata=dict(
            name="MinimumQuantity",
            type="Attribute"
        )
    )


@dataclass
class OptionalServicesTypeCodeGroup:
    """Holds the attributes to identify an option.

    :ivar code: The ACH code for the OptionalService
    :ivar vendor_option_code: The vendor specific code for the OptionalService
    :ivar type: The type of the option
    :ivar secondary_code: An additional code for the option required when the option identifies a larger type and specific codes are required by the vendor. For example, sports equipment may be a Code, and the secondary code could be SKIS or BIKE.
    :ivar selected_by_default: Flag to indicate if the option has been selected by default
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )
    vendor_option_code: str = field(
        default=None,
        metadata=dict(
            name="VendorOptionCode",
            type="Attribute",
            min_length=1.0,
            max_length=64.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )
    secondary_code: str = field(
        default=None,
        metadata=dict(
            name="SecondaryCode",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    selected_by_default: bool = field(
        default=None,
        metadata=dict(
            name="SelectedByDefault",
            type="Attribute"
        )
    )


@dataclass
class OtherGuaranteeInfo(str):
    """
    :ivar type: 1) IATA/ARC Number 2) Agency Address 2) Deposit Taken 3) Others
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )


@dataclass
class OverridePcc:
    """Used to emulate to another PCC or SID. Providers: 1G, 1V, 1P, 1J.

    :ivar provider_code: The code of the provider (e.g. 1G, 1S)
    :ivar pseudo_city_code: The PCC in the host system.
    """
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
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            required=True,
            min_length=2.0,
            max_length=10.0
        )
    )


@dataclass
class OwnershipChange:
    """Element to change the ownership of the PNR in the UR. PROVIDER SUPPORTED:
    Worldspan and JAL.

    :ivar owning_pcc: New owning PCC of the PNR.
    """
    owning_pcc: str = field(
        default=None,
        metadata=dict(
            name="OwningPCC",
            type="Attribute",
            required=True
        )
    )


@dataclass
class PageAttributes:
    """Attributes to control pagination.

    :ivar max_results:
    :ivar start_from_result:
    """
    max_results: int = field(
        default=None,
        metadata=dict(
            name="MaxResults",
            type="Attribute",
            min_inclusive=1.0,
            max_inclusive=200.0
        )
    )
    start_from_result: int = field(
        default=None,
        metadata=dict(
            name="StartFromResult",
            type="Attribute",
            min_inclusive=1.0
        )
    )


@dataclass
class PaymentAdvice:
    """Contains other form of payment for Cruise Reservations.

    :ivar type: Other Payment Yype. Possible Values: AGC - Agency Check, AGG - Agency Guarantee, AWC - Award Check, CSH - Cash Equivalent, DBC - Denied Boarding Compensation, MCO - Miscellaneous Charge Order, TOO - Tour Order, TOV - Tour Voucher
    :ivar document_number: Payment Document Number Examples: 1234567890, R7777
    :ivar issue_date: Document Issuance date
    :ivar issue_city: City code of document issuance
    :ivar original_fop: Original form of payment Examples: CHECK 3500
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True,
            max_length=3.0
        )
    )
    document_number: str = field(
        default=None,
        metadata=dict(
            name="DocumentNumber",
            type="Attribute",
            required=True,
            max_length=22.0
        )
    )
    issue_date: str = field(
        default=None,
        metadata=dict(
            name="IssueDate",
            type="Attribute",
            required=True
        )
    )
    issue_city: str = field(
        default=None,
        metadata=dict(
            name="IssueCity",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    original_fop: str = field(
        default=None,
        metadata=dict(
            name="OriginalFOP",
            type="Attribute",
            max_length=19.0
        )
    )


@dataclass
class PaymentRef:
    """
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
class Penalty:
    """Exchange penalty information.

    :ivar cancel_refund:
    :ivar non_refundable:
    :ivar non_exchangeable:
    :ivar cancelation_penalty:
    :ivar reissue_penalty:
    :ivar non_reissue_penalty:
    :ivar ticket_refund_penalty:
    :ivar charge_applicable:
    :ivar charge_portion:
    :ivar penalty_amount:
    """
    cancel_refund: bool = field(
        default=None,
        metadata=dict(
            name="CancelRefund",
            type="Attribute"
        )
    )
    non_refundable: bool = field(
        default=None,
        metadata=dict(
            name="NonRefundable",
            type="Attribute"
        )
    )
    non_exchangeable: bool = field(
        default=None,
        metadata=dict(
            name="NonExchangeable",
            type="Attribute"
        )
    )
    cancelation_penalty: bool = field(
        default=None,
        metadata=dict(
            name="CancelationPenalty",
            type="Attribute"
        )
    )
    reissue_penalty: bool = field(
        default=None,
        metadata=dict(
            name="ReissuePenalty",
            type="Attribute"
        )
    )
    non_reissue_penalty: bool = field(
        default=None,
        metadata=dict(
            name="NonReissuePenalty",
            type="Attribute"
        )
    )
    ticket_refund_penalty: bool = field(
        default=None,
        metadata=dict(
            name="TicketRefundPenalty",
            type="Attribute"
        )
    )
    charge_applicable: bool = field(
        default=None,
        metadata=dict(
            name="ChargeApplicable",
            type="Attribute"
        )
    )
    charge_portion: bool = field(
        default=None,
        metadata=dict(
            name="ChargePortion",
            type="Attribute"
        )
    )
    penalty_amount: str = field(
        default=None,
        metadata=dict(
            name="PenaltyAmount",
            type="Attribute"
        )
    )


@dataclass
class PersonalGeography:
    """Personal geography details of the associated passenger.

    :ivar country_code: Passenger country code.
    :ivar state_province_code: Passenger state/province code.
    :ivar city_code: Passenger city code.
    """
    country_code: str = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Element",
            length=2
        )
    )
    state_province_code: str = field(
        default=None,
        metadata=dict(
            name="StateProvinceCode",
            type="Element",
            max_length=6.0
        )
    )
    city_code: str = field(
        default=None,
        metadata=dict(
            name="CityCode",
            type="Element",
            length=3
        )
    )


@dataclass
class PointOfCommencement:
    """Point of Commencement is optional. CityOrAirportCode and date portion of the
    Time attribute is mandatory.

    :ivar city_or_airport_code: Three digit Airport or City code that would be the Point of Commencement location for the trips/legs mentioned.
    :ivar time: Specify a date or date and time
    """
    city_or_airport_code: str = field(
        default=None,
        metadata=dict(
            name="CityOrAirportCode",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    time: str = field(
        default=None,
        metadata=dict(
            name="Time",
            type="Attribute",
            required=True
        )
    )


@dataclass
class PointOfSale:
    """User can use this node to send a specific PCC to access fares allowed only
    for that PCC. This node gives the capability for fare redistribution at UR
    level. For fare redistribution at the stored fare level see
    AirPricingSolution/AirPricingInfo/AirPricingModifiers/PointOfSale.

    :ivar provider_code: The provider in which the PCC is defined.
    :ivar pseudo_city_code: The PCC in the host system.
    :ivar key:
    :ivar iata: Used for rapid reprice. This field is the IATA associated to this Point of Sale PCC. Providers: 1G/1V
    """
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
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            required=True,
            min_length=2.0,
            max_length=10.0
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    iata: str = field(
        default=None,
        metadata=dict(
            name="IATA",
            type="Attribute",
            max_length=8.0
        )
    )


@dataclass
class PriceMatchError:
    """
    :ivar error_message:
    :ivar vendor_code: The code of the vendor (e.g. HZ, etc.)
    :ivar hotel_chain: 2 Letter Hotel Chain Code
    :ivar hotel_code: Unique hotel identifier for the channel.
    :ivar req_base: BaseRate in the request.
    :ivar rsp_base: BaseRate retruned from the supplier.
    :ivar base_diff: BaseRate Difference.
    :ivar req_total: Estimated Total Amount in the request.
    :ivar rsp_total: Estimated Total Amount returned from the supplier.
    :ivar total_diff: Estimated Total Amount difference.
    """
    error_message: str = field(
        default=None,
        metadata=dict(
            name="ErrorMessage",
            type="Element",
            required=True
        )
    )
    vendor_code: str = field(
        default=None,
        metadata=dict(
            name="VendorCode",
            type="Attribute",
            min_length=1.0,
            max_length=5.0
        )
    )
    hotel_chain: str = field(
        default=None,
        metadata=dict(
            name="HotelChain",
            type="Attribute",
            length=2
        )
    )
    hotel_code: str = field(
        default=None,
        metadata=dict(
            name="HotelCode",
            type="Attribute",
            max_length=32.0
        )
    )
    req_base: float = field(
        default=None,
        metadata=dict(
            name="ReqBase",
            type="Attribute"
        )
    )
    rsp_base: float = field(
        default=None,
        metadata=dict(
            name="RspBase",
            type="Attribute"
        )
    )
    base_diff: float = field(
        default=None,
        metadata=dict(
            name="BaseDiff",
            type="Attribute"
        )
    )
    req_total: float = field(
        default=None,
        metadata=dict(
            name="ReqTotal",
            type="Attribute"
        )
    )
    rsp_total: float = field(
        default=None,
        metadata=dict(
            name="RspTotal",
            type="Attribute"
        )
    )
    total_diff: float = field(
        default=None,
        metadata=dict(
            name="TotalDiff",
            type="Attribute"
        )
    )


@dataclass
class Provider:
    """Provider identifier.

    :ivar code:
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=2.0,
            max_length=5.0
        )
    )


@dataclass
class ProviderReservation:
    """
    :ivar provider_code:
    :ivar provider_locator_code:
    """
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
    provider_locator_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            required=True,
            max_length=15.0
        )
    )


@dataclass
class ProviderReservationInfoRef:
    """Container for Provider reservation reference key.

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
class PseudoCityCode:
    """
    :ivar value:
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_length=2.0,
            max_length=10.0
        )
    )


@dataclass
class RailLocation(Location):
    """RCH specific location code (a.k.a UCodes) which uniquely identifies a train
    station.

    :ivar code:
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=3.0,
            max_length=8.0,
            white_space="collapse"
        )
    )


@dataclass
class ReferencePoint:
    """
    :ivar value:
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            max_length=30.0
        )
    )


@dataclass
class RefundRemark:
    """A textual remark displayed in Refund Quote and Refund response.

    :ivar remark_data: Actual remark data.
    """
    remark_data: str = field(
        default=None,
        metadata=dict(
            name="RemarkData",
            type="Element",
            required=True
        )
    )


@dataclass
class Remark(str):
    """A textual remark container to hold any printable text. (max 512 chars)

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )


@dataclass
class RequiredField:
    """
    :ivar name: The name of the required field
    """
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Requisition:
    """Requisition Form of Payment.

    :ivar number: Requisition number used for accounting
    :ivar category: Classification Category for the requisition payment
    :ivar type: Type can be Cash or Credit for category as Government
    """
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute"
        )
    )
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
            type="Attribute"
        )
    )


@dataclass
class ResponseMessage(str):
    """A simple textual fare note. Used within several other objects.

    :ivar code:
    :ivar type: Indicates the type of message (Warning, Error, Info)
    """
    code: int = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
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
class Restriction:
    """Which activities are supported for a particular element.

    :ivar operation: The operation that is restricted
    :ivar reason: The reason it is restricted
    """
    operation: str = field(
        default=None,
        metadata=dict(
            name="Operation",
            type="Attribute",
            required=True
        )
    )
    reason: str = field(
        default=None,
        metadata=dict(
            name="Reason",
            type="Attribute"
        )
    )


@dataclass
class RoleInfo:
    """Container to specify the role of the agent.

    :ivar id: Unique identifier of the role.
    :ivar name: Agent's role name
    :ivar source: Role inheritance level. Needed in the response, not in the request
    :ivar description: Description of role
    """
    id: str = field(
        default=None,
        metadata=dict(
            name="Id",
            type="Attribute",
            required=True,
            max_length=19.0
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            required=True,
            max_length=128.0
        )
    )
    source: str = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute"
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            max_length=1024.0
        )
    )


@dataclass
class SearchTicketing:
    """Search restriction by Agent.

    :ivar ticket_status: Return only PNRs with ticketed, non-ticketed or both
    :ivar reservation_status: Used only if "TicketStatus" set to "No" or "Both". Return only PNRs with specific reservation status or both statuses.
    :ivar ticket_date: Identifies when this reservation was ticketed, or when it should be ticketed by (in the event of a TTL)
    """
    ticket_status: str = field(
        default="Both",
        metadata=dict(
            name="TicketStatus",
            type="Attribute"
        )
    )
    reservation_status: str = field(
        default="Both",
        metadata=dict(
            name="ReservationStatus",
            type="Attribute"
        )
    )
    ticket_date: str = field(
        default=None,
        metadata=dict(
            name="TicketDate",
            type="Attribute"
        )
    )


@dataclass
class SeatAttribute:
    """Identifies the seat attribute of the service.

    :ivar value:
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=2.0
        )
    )


@dataclass
class SegmentRemark(str):
    """A textual remark container to hold any printable text. (max 512 chars)

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
class SellMessage(str):
    """Sell Message from Vendor.

    This is applicable in response messages only, any input in request
    message will be ignored.
    """
    pass


@dataclass
class ServiceFeeTaxInfo:
    """The taxes associated to a particular Service Fee.

    :ivar category: The tax category represents a valid IATA tax code.
    :ivar amount:
    """
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            required=True
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True
        )
    )


@dataclass
class ShopInformation:
    """Shopping Information required for File Finishing.

    :ivar search_request: Search parameters that were used in LFS request
    :ivar flights_offered: Flights with lowest logical airfare returned as response to LFS request
    :ivar cabin_shopped:
    :ivar cabin_selected:
    :ivar lowest_fare_offered:
    """
    search_request: List["ShopInformation.SearchRequest"] = field(
        default_factory=list,
        metadata=dict(
            name="SearchRequest",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    flights_offered: List["ShopInformation.FlightsOffered"] = field(
        default_factory=list,
        metadata=dict(
            name="FlightsOffered",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    cabin_shopped: str = field(
        default=None,
        metadata=dict(
            name="CabinShopped",
            type="Attribute"
        )
    )
    cabin_selected: str = field(
        default=None,
        metadata=dict(
            name="CabinSelected",
            type="Attribute"
        )
    )
    lowest_fare_offered: str = field(
        default=None,
        metadata=dict(
            name="LowestFareOffered",
            type="Attribute"
        )
    )

    @dataclass
    class SearchRequest:
        """
        :ivar origin:
        :ivar destination:
        :ivar departure_time: Date and Time at which this entity departs. This does not include Time Zone information since it can be derived from origin location
        :ivar class_of_service:
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
                type="Attribute"
            )
        )
        class_of_service: str = field(
            default=None,
            metadata=dict(
                name="ClassOfService",
                type="Attribute",
                min_length=1.0,
                max_length=2.0
            )
        )

    @dataclass
    class FlightsOffered:
        """
        :ivar origin:
        :ivar destination:
        :ivar departure_time: Date and Time at which this entity departs. This does not include Time Zone information since it can be derived from origin location
        :ivar travel_order:
        :ivar carrier:
        :ivar flight_number:
        :ivar class_of_service:
        :ivar stop_over:
        :ivar connection:
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
        carrier: str = field(
            default=None,
            metadata=dict(
                name="Carrier",
                type="Attribute",
                length=2
            )
        )
        flight_number: str = field(
            default=None,
            metadata=dict(
                name="FlightNumber",
                type="Attribute",
                max_length=5.0
            )
        )
        class_of_service: str = field(
            default=None,
            metadata=dict(
                name="ClassOfService",
                type="Attribute",
                min_length=1.0,
                max_length=2.0
            )
        )
        stop_over: bool = field(
            default="false",
            metadata=dict(
                name="StopOver",
                type="Attribute"
            )
        )
        connection: bool = field(
            default="false",
            metadata=dict(
                name="Connection",
                type="Attribute"
            )
        )


@dataclass
class SimpleName(str):
    """Free text name."""
    pass


@dataclass
class State(str):
    """Container to house the state code for an address."""
    pass


@dataclass
class StockControl:
    """The Stock Control Numbers related details of the MCO.

    :ivar type: Stock control type valid options include: Pending, Failed, Plain Paper, Blank, Suppressed.
    :ivar number: Stock control number.
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute"
        )
    )


@dataclass
class TerminalSessionInfo(str):
    """Travelport use only.

    This element contains CDATA information representing existing GDS
    session data or ACH credentials information of the terminal user
    """
    pass


@dataclass
class TicketNumber:
    """The identifying number for the actual ticket.

    :ivar value:
    """
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_length=1.0,
            max_length=13.0
        )
    )


@dataclass
class TravelInfo:
    """Traveler information details like Travel Purpose and Trip Name.

    :ivar trip_name: Trip Name
    :ivar travel_purpose: Purpose of the trip
    """
    trip_name: str = field(
        default=None,
        metadata=dict(
            name="TripName",
            type="Attribute",
            max_length=50.0
        )
    )
    travel_purpose: str = field(
        default=None,
        metadata=dict(
            name="TravelPurpose",
            type="Attribute",
            max_length=50.0
        )
    )


@dataclass
class TravelerType:
    """The 3-char IATA traveler type code.

    :ivar code:
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class TypeAgencyHierarchyReference:
    """
    :ivar profile_id:
    :ivar profile_type:
    """
    profile_id: int = field(
        default=None,
        metadata=dict(
            name="ProfileID",
            type="Attribute",
            required=True
        )
    )
    profile_type: str = field(
        default=None,
        metadata=dict(
            name="ProfileType",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TypeAgencyPayment:
    """Type for Agency Payment.

    :ivar agency_billing_identifier: Value of the billing id
    :ivar agency_billing_number: Value of billing number
    :ivar agency_billing_password: Value of billing password
    """
    agency_billing_identifier: str = field(
        default=None,
        metadata=dict(
            name="AgencyBillingIdentifier",
            type="Attribute",
            required=True,
            max_length=128.0
        )
    )
    agency_billing_number: str = field(
        default=None,
        metadata=dict(
            name="AgencyBillingNumber",
            type="Attribute",
            max_length=128.0
        )
    )
    agency_billing_password: str = field(
        default=None,
        metadata=dict(
            name="AgencyBillingPassword",
            type="Attribute",
            max_length=128.0
        )
    )


@dataclass
class TypeBookingTransactionsAllowed:
    """
    :ivar booking_enabled: Allow or prohibit booking transaction for the given product type on this Provider/Supplier. Inheritable.
    """
    booking_enabled: bool = field(
        default=None,
        metadata=dict(
            name="BookingEnabled",
            type="Attribute"
        )
    )


@dataclass
class TypeDateRange:
    """Specify a range of dates.

    :ivar start_date:
    :ivar end_date:
    """
    start_date: str = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute",
            required=True
        )
    )
    end_date: str = field(
        default=None,
        metadata=dict(
            name="EndDate",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TypeFormOfPaymentPnrreference:
    """
    :ivar key: Unique ID to identify a ProviderReservationInfo
    :ivar provider_reservation_level: It means that the form of payment is applied at ProviderReservation level.
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    provider_reservation_level: bool = field(
        default="true",
        metadata=dict(
            name="ProviderReservationLevel",
            type="Attribute"
        )
    )


@dataclass
class TypeFreeFormText(str):
    """Free form Text."""
    pass


@dataclass
class TypeGeneralReference:
    """
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
class TypeGuaranteeInformation:
    """Information pertaining to the payment of type Guarantee.

    :ivar type: Guarantee only or Deposit
    :ivar agency_type: Guarantee to Agency IATA or Guarantee to Another Agency IATA
    :ivar iatanumber: Payment IATA number. (ie. IATA of Agency or Other Agency)
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    agency_type: str = field(
        default=None,
        metadata=dict(
            name="AgencyType",
            type="Attribute",
            required=True
        )
    )
    iatanumber: str = field(
        default=None,
        metadata=dict(
            name="IATANumber",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=128.0
        )
    )


@dataclass
class TypeKeyBasedReference:
    """Generic type to be used for Key based reference.

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
class TypeNonAirReservationRef:
    """
    :ivar locator_code:
    """
    locator_code: str = field(
        default=None,
        metadata=dict(
            name="LocatorCode",
            type="Attribute",
            required=True,
            min_length=5.0,
            max_length=8.0
        )
    )


@dataclass
class TypeOtasubKey:
    """The attributes and elements in a SubKey.

    :ivar text: Information for a sub key.
    :ivar name: A subkey to identify the special equipment codes. Applicable when Policy/@Name is EQUIP. Uses OTA CODE "EQP". 1P/1J.
    :ivar description: A brief description of a subkey.
    """
    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    name: int = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            required=True
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute"
        )
    )


@dataclass
class TypePolicyCodesList:
    """
    :ivar policy_code: A code that indicates why an item was determined to be ‘out of policy’.
    :ivar min_policy_code: A code that indicates why the minimum fare or rate was determined to be ‘out of policy’.
    :ivar max_policy_code: A code that indicates why the maximum fare or rate was determined to be ‘out of policy’.
    """
    policy_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PolicyCode",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )
    min_policy_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="MinPolicyCode",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )
    max_policy_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="MaxPolicyCode",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class TypeProfileRef:
    """ProfileEntityID and ProfileLevel together identity a profile entity.

    :ivar profile_entity_id:
    :ivar profile_level:
    """
    profile_entity_id: str = field(
        default=None,
        metadata=dict(
            name="ProfileEntityID",
            type="Attribute",
            required=True
        )
    )
    profile_level: str = field(
        default=None,
        metadata=dict(
            name="ProfileLevel",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TypeRateDescription:
    """
    :ivar text:
    :ivar name: Optional context name of the text block being returned i.e. Room details
    """
    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute"
        )
    )


@dataclass
class TypeRemark(str):
    """
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar provider_code: Contains the Provider Code of the provider for which this element is used
    """
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
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


@dataclass
class TypeRemarkWithTravelerRef:
    """
    :ivar remark_data: Actual remarks data.
    :ivar booking_traveler_ref: Reference to Booking Traveler.
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar provider_code: Contains the Provider Code of the provider for which this element is used
    """
    remark_data: str = field(
        default=None,
        metadata=dict(
            name="RemarkData",
            type="Element",
            required=True
        )
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
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


@dataclass
class TypeResultMessage(str):
    """Used to identify the results of a requests.

    :ivar code:
    :ivar type: Indicates the type of message (Warning, Error, Info)
    """
    code: int = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
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
class TypeSegmentRef:
    """
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
class TypeSpecificTime:
    """Specify exact times. System will automatically convert to a range according
    to agency configuration.

    :ivar time:
    """
    time: str = field(
        default=None,
        metadata=dict(
            name="Time",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TypeSubKey:
    """The attributes and elements in a SubKey.

    :ivar text: Information for a sub key.
    :ivar name: A subkey to identify the specific information within this keyword
    :ivar description: A brief description of a subkey.
    """
    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=0,
            max_occurs=999
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
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute"
        )
    )


@dataclass
class TypeTax:
    """
    :ivar amount:
    :ivar code:
    """
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute"
        )
    )


@dataclass
class TypeTimeRange:
    """Specify a range of times.

    :ivar earliest_time:
    :ivar latest_time:
    """
    earliest_time: str = field(
        default=None,
        metadata=dict(
            name="EarliestTime",
            type="Attribute",
            required=True
        )
    )
    latest_time: str = field(
        default=None,
        metadata=dict(
            name="LatestTime",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TypeVendorLocation:
    """
    :ivar provider_code: The code of the provider (e.g. 1G, 1S)
    :ivar vendor_code: The code of the vendor (e.g. HZ, etc.)
    :ivar preferred_option: Preferred Option marker for Location.
    :ivar vendor_location_id: Location identifier
    :ivar key: Key which maps vendor location with vehicles
    :ivar more_rates_token: Enter the Token when provided by hotel property, more rates exist. HADS/HSS support only.
    """
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
    vendor_code: str = field(
        default=None,
        metadata=dict(
            name="VendorCode",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    preferred_option: bool = field(
        default=None,
        metadata=dict(
            name="PreferredOption",
            type="Attribute"
        )
    )
    vendor_location_id: str = field(
        default=None,
        metadata=dict(
            name="VendorLocationID",
            type="Attribute",
            min_length=1.0,
            white_space="collapse"
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    more_rates_token: str = field(
        default=None,
        metadata=dict(
            name="MoreRatesToken",
            type="Attribute",
            min_length=1.0,
            max_length=30.0
        )
    )


@dataclass
class TypeVoucherInformation:
    """Information pertaining to the payment of a Vehicle Rental.

    :ivar voucher_type: Specifies if the Voucher is for Full Credit or a Group/Day or a Monetary Amount or RegularVoucher.
    :ivar amount: Amount associated with the Voucher.
    :ivar confirmation_number: Confirmation from the vendor for the voucher
    :ivar account_name: Associated account name for the voucher
    :ivar number: To advise car associates of the voucher number and store in the car segment. It is required when VoucherType selected as "RegularVoucher" for 1P, 1J only.
    """
    voucher_type: str = field(
        default=None,
        metadata=dict(
            name="VoucherType",
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
    confirmation_number: str = field(
        default=None,
        metadata=dict(
            name="ConfirmationNumber",
            type="Attribute"
        )
    )
    account_name: str = field(
        default=None,
        metadata=dict(
            name="AccountName",
            type="Attribute"
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )


@dataclass
class UnitedNations:
    """United Nations Form of Payments.

    :ivar number:
    """
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Xmlremark(str):
    """A remark container to hold an XML document. (max 1024 chars) This will be
    encoded with xml encoding.

    :ivar key:
    :ivar category: A category to group and organize the various remarks. This is not required, but it is recommended.
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            max_length=10.0
        )
    )


@dataclass
class AccountCode(AttrProviderSupplier):
    """Account Code is used to get Private Fares.If ProviderCode or SupplierCode is
    not specified, it will be considered a default AccounCode to be sent to all the
    Providers or Suppliers.

    :ivar code:
    :ivar type: An identifier to categorize this account code. For example, FlightPass for AC Flight Pass or RFB for AC corporate Rewards for Business.
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
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
class AccountingRemark(AttrElementKeyResults):
    """An accounting remark container to hold any printable text.

    :ivar remark_data: Actual remarks data.
    :ivar booking_traveler_ref: Reference to Booking Traveler.
    :ivar key:
    :ivar category: A category to group and organize the various remarks. This is not required, but it is recommended.
    :ivar type_in_gds:
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar provider_code: Contains the Provider Code of the provider for which this accounting remark is used
    :ivar use_provider_native_mode: Will be true when terminal process required, else false
    """
    remark_data: str = field(
        default=None,
        metadata=dict(
            name="RemarkData",
            type="Element",
            required=True
        )
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            max_length=14.0
        )
    )
    type_in_gds: str = field(
        default=None,
        metadata=dict(
            name="TypeInGds",
            type="Attribute",
            max_length=30.0
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
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
    use_provider_native_mode: bool = field(
        default="false",
        metadata=dict(
            name="UseProviderNativeMode",
            type="Attribute"
        )
    )


@dataclass
class ActionStatus(AttrProviderSupplier, AttrElementKeyResults):
    """Status of the action that will happen or has happened to the air
    reservation. One Action status for each provider reservation.

    :ivar remark:
    :ivar type: Identifies the type of action (if any) to take on this air reservation. Only TTL, TAU, TAX and TAW can be set by the user.
    :ivar ticket_date: Identifies when the action type will happen, or has happened according to the type.
    :ivar key: Identifies when the action type will happen, or has happened according to the type.
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar queue_category: Add Category placement to ticketing queue (required in 1P - default is 00)
    :ivar airport_code: Used with Time Limit to specify the airport location where the ticket is to be issued.
    :ivar pseudo_city_code: The Branch PCC in the host system where PNR can be queued for ticketing. When used with TAU it will auto queue to Q10. When used with TAW agent performs manual move to Q.
    :ivar account_code: Used with TAW. Used to specify a corporate or in house account code to the PNR as part of ticketing arrangement field.
    """
    remark: Remark = field(
        default=None,
        metadata=dict(
            name="Remark",
            type="Element"
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
    ticket_date: str = field(
        default=None,
        metadata=dict(
            name="TicketDate",
            type="Attribute"
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
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
    queue_category: str = field(
        default=None,
        metadata=dict(
            name="QueueCategory",
            type="Attribute",
            min_length=1.0,
            white_space="collapse"
        )
    )
    airport_code: str = field(
        default=None,
        metadata=dict(
            name="AirportCode",
            type="Attribute",
            length=3
        )
    )
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=2.0,
            max_length=10.0
        )
    )
    account_code: str = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute"
        )
    )


@dataclass
class AddressRestriction:
    """
    :ivar required_field:
    """
    required_field: List[RequiredField] = field(
        default_factory=list,
        metadata=dict(
            name="RequiredField",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AgencyPayment(TypeAgencyPayment):
    """Container for Agency Payment."""
    pass


@dataclass
class AgentAction(AttrAgentOverride):
    """Depending on context, this will represent information about which agent
    perform different actions.

    :ivar action_type: The type of action the agent performed.
    :ivar agent_code: The AgenctCode who performed the action.
    :ivar branch_code: The BranchCode of the branch (working branch, branchcode used for the request. If nothing specified, branchcode for the agent) who performed the action.
    :ivar agency_code: The AgencyCode of the agent who performed the action.
    :ivar agent_sine: The sign in user name of the agent logged into the terminal. PROVIDER SUPPORTED: ACH
    :ivar event_time: Date and time at which this event took place.
    """
    action_type: str = field(
        default=None,
        metadata=dict(
            name="ActionType",
            type="Attribute",
            required=True
        )
    )
    agent_code: str = field(
        default=None,
        metadata=dict(
            name="AgentCode",
            type="Attribute",
            required=True
        )
    )
    branch_code: str = field(
        default=None,
        metadata=dict(
            name="BranchCode",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=25.0
        )
    )
    agency_code: str = field(
        default=None,
        metadata=dict(
            name="AgencyCode",
            type="Attribute",
            required=True
        )
    )
    agent_sine: str = field(
        default=None,
        metadata=dict(
            name="AgentSine",
            type="Attribute"
        )
    )
    event_time: str = field(
        default=None,
        metadata=dict(
            name="EventTime",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AppliedProfile(AttrElementKeyResults):
    """A simple container to specify the profiles that were applied to a
    reservation.

    :ivar key: Key for update/delete of the element
    :ivar traveler_id: The ID of the TravelerProfile that was applied
    :ivar traveler_name: The name from the TravelerProfile that was applied
    :ivar account_id: The ID of the AccountProfile that was applied
    :ivar account_name: The name from the AccountProfile that was applied
    :ivar immediate_parent_id: The ID of the immediate parent that was applied
    :ivar immediate_parent_name: The name of the immediate parent that was applied
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    traveler_id: str = field(
        default=None,
        metadata=dict(
            name="TravelerID",
            type="Attribute"
        )
    )
    traveler_name: str = field(
        default=None,
        metadata=dict(
            name="TravelerName",
            type="Attribute"
        )
    )
    account_id: str = field(
        default=None,
        metadata=dict(
            name="AccountID",
            type="Attribute"
        )
    )
    account_name: str = field(
        default=None,
        metadata=dict(
            name="AccountName",
            type="Attribute"
        )
    )
    immediate_parent_id: str = field(
        default=None,
        metadata=dict(
            name="ImmediateParentID",
            type="Attribute"
        )
    )
    immediate_parent_name: str = field(
        default=None,
        metadata=dict(
            name="ImmediateParentName",
            type="Attribute"
        )
    )


@dataclass
class BookingTravelerInformation:
    """Booking Traveler information tied to invoice.

    :ivar name:
    :ivar booking_traveler_ref: A reference to a passenger related to a ticket.
    """
    name: Name = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            required=True
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
class BookingTravelerName(AttrBookingTravelerName):
    """Complete name fields."""
    pass


@dataclass
class BookingTravelerRef:
    """Reference Element for Booking Traveler and Loyalty cards.

    :ivar loyalty_card_ref:
    :ivar drivers_license_ref:
    :ivar discount_card_ref:
    :ivar payment_ref:
    :ivar key:
    """
    loyalty_card_ref: List[LoyaltyCardRef] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyCardRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    drivers_license_ref: DriversLicenseRef = field(
        default=None,
        metadata=dict(
            name="DriversLicenseRef",
            type="Element"
        )
    )
    discount_card_ref: List[DiscountCardRef] = field(
        default_factory=list,
        metadata=dict(
            name="DiscountCardRef",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    payment_ref: List[PaymentRef] = field(
        default_factory=list,
        metadata=dict(
            name="PaymentRef",
            type="Element",
            min_occurs=0,
            max_occurs=3
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
class CardRestriction:
    """
    :ivar required_field:
    :ivar code: 2 letter Credit/Debit Card merchant type
    :ivar name: Card merchant description
    """
    required_field: List[RequiredField] = field(
        default_factory=list,
        metadata=dict(
            name="RequiredField",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=2.0,
            max_length=2.0
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
class CommissionRemark(AttrElementKeyResults):
    """Identifies the agency commision remarks. Specifically used for Worldspan.

    :ivar provider_reservation_level: Specify commission which is applicable to PNR level.
    :ivar passenger_type_level: Specify commission which is applicable to per PTC level.
    :ivar key: Key to be used for internal processing.
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar provider_code: Contains the Provider Code of the provider for which this accounting remark is used
    """
    provider_reservation_level: "CommissionRemark.ProviderReservationLevel" = field(
        default=None,
        metadata=dict(
            name="ProviderReservationLevel",
            type="Element",
            required=True
        )
    )
    passenger_type_level: List["CommissionRemark.PassengerTypeLevel"] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerTypeLevel",
            type="Element",
            min_occurs=1,
            max_occurs=4
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
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
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2.0,
            max_length=5.0
        )
    )

    @dataclass
    class ProviderReservationLevel(AttrCommissionRemark):
        
        pass

    @dataclass
    class PassengerTypeLevel(AttrCommissionRemark):
        """
        :ivar traveler_type:
        """
        traveler_type: str = field(
            default=None,
            metadata=dict(
                name="TravelerType",
                type="Attribute",
                required=True,
                min_length=3.0,
                max_length=5.0
            )
        )


@dataclass
class ConsolidatorRemark(AttrElementKeyResults):
    """Authorization remark for Consolidator access to a PNR . Contains PCC
    information created by retail agent to allow a consolidator or other Axess
    users to service their PNR. PROVIDER SUPPORTED: Worldspan and JAL.

    :ivar pseudo_city_code:
    :ivar key: Key to be used for internal processing.
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar provider_code: Contains the Provider Code of the provider for which this element is used
    """
    pseudo_city_code: List[PseudoCityCode] = field(
        default_factory=list,
        metadata=dict(
            name="PseudoCityCode",
            type="Element",
            min_occurs=1,
            max_occurs=5
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
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
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2.0,
            max_length=5.0
        )
    )


@dataclass
class CustomerId(TypeRemark):
    """A provider reservation field used to store customer information. It may be
    used to identify reservations which will/will not be available for access.

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )


@dataclass
class DiscountCard(AttrElementKeyResults):
    """Rail Discount Card Information.

    :ivar key:
    :ivar code:
    :ivar description:
    :ivar number:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            min_length=1.0,
            max_length=255.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            min_length=1.0,
            max_length=36.0
        )
    )


@dataclass
class DriversLicense(AttrElementKeyResults):
    """Details of drivers license.

    :ivar key:
    :ivar license_number: The driving license number of the booking traveler.
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    license_number: str = field(
        default=None,
        metadata=dict(
            name="LicenseNumber",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Email(AttrElementKeyResults):
    """Container for an email address with a type specifier (max 128 chars)

    :ivar provider_reservation_info_ref: Tagging provider reservation info with Email.
    :ivar key:
    :ivar type:
    :ivar comment:
    :ivar email_id:
    """
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            min_length=1.0,
            max_length=128.0
        )
    )
    comment: str = field(
        default=None,
        metadata=dict(
            name="Comment",
            type="Attribute",
            min_length=1.0
        )
    )
    email_id: str = field(
        default=None,
        metadata=dict(
            name="EmailID",
            type="Attribute",
            required=True
        )
    )


@dataclass
class GeneralRemark(AttrProviderSupplier, AttrElementKeyResults):
    """A textual remark container to hold any printable text. (max 512 chars)

    :ivar remark_data: Actual remarks data.
    :ivar booking_traveler_ref: Reference to Booking Traveler.
    :ivar key:
    :ivar category: A category to group and organize the various remarks. This is not required, but it is recommended.
    :ivar type_in_gds:
    :ivar supplier_type: The type of product this reservation is relative to
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar direction: Direction Incoming or Outgoing of the GeneralRemark.
    :ivar create_date: The date and time that this GeneralRemark was created.
    :ivar use_provider_native_mode: Will be true when terminal process required, else false
    """
    remark_data: str = field(
        default=None,
        metadata=dict(
            name="RemarkData",
            type="Element",
            required=True
        )
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            max_length=20.0
        )
    )
    type_in_gds: str = field(
        default=None,
        metadata=dict(
            name="TypeInGds",
            type="Attribute",
            max_length=30.0
        )
    )
    supplier_type: str = field(
        default=None,
        metadata=dict(
            name="SupplierType",
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
    direction: str = field(
        default=None,
        metadata=dict(
            name="Direction",
            type="Attribute"
        )
    )
    create_date: str = field(
        default=None,
        metadata=dict(
            name="CreateDate",
            type="Attribute"
        )
    )
    use_provider_native_mode: bool = field(
        default="false",
        metadata=dict(
            name="UseProviderNativeMode",
            type="Attribute"
        )
    )


@dataclass
class HostTokenList:
    """The shared object list of Host Tokens.

    :ivar host_token:
    """
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class LinkedUniversalRecord(AttrElementKeyResults):
    """
    :ivar locator_code: A Universal Record that need to be linked to the current Universal Record.
    :ivar key:
    """
    locator_code: str = field(
        default=None,
        metadata=dict(
            name="LocatorCode",
            type="Attribute",
            required=True,
            min_length=5.0,
            max_length=8.0
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
class LoyaltyProgram(AttrLoyalty):
    """
    :ivar level:
    """
    level: str = field(
        default=None,
        metadata=dict(
            name="Level",
            type="Attribute"
        )
    )


@dataclass
class McofeeInfo(AttrAmountPercent):
    """Information related to the PTA/TOD (Prepaid Ticket Advice / Ticket on
    Departure) related to the MCO.

    :ivar fee_applies_to_ind: Indicates if PTA/TOD fee is for the entire MCO or is per person.
    """
    fee_applies_to_ind: str = field(
        default=None,
        metadata=dict(
            name="FeeAppliesToInd",
            type="Attribute"
        )
    )


@dataclass
class Mcotext(TypeFreeFormText):
    """
    All type of free format text messages related to MCO like - Command Text, Agent Entry, MCO Modifiers, Text Message
    :ivar type: The type of text. Possible values: Command Text, Agent Entry, MCO Modifiers, Text Message
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )


@dataclass
class NameRemark(AttrElementKeyResults):
    """Text that support Name Remarks.

    :ivar remark_data: Actual remarks data.
    :ivar provider_reservation_info_ref: Tagging provider reservation info with NameRemark.
    :ivar key:
    :ivar category: A category to group and organize the various remarks. This is not required, but it is recommended.
    """
    remark_data: str = field(
        default=None,
        metadata=dict(
            name="RemarkData",
            type="Element",
            required=True
        )
    )
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
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
class OptionalServiceApplicationLimitType(OptionalServiceApplicabilityLimitGroup):
    """The optional service application limit."""
    pass


@dataclass
class Osi(AttrElementKeyResults):
    """Other Service information sent to the carriers during air bookings.

    :ivar key:
    :ivar carrier:
    :ivar code:
    :ivar text:
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar provider_code: Contains the Provider Code of the provider for which this OSI is used
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
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
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            max_length=4.0
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            required=True,
            max_length=256.0
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
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


@dataclass
class PassengerInfo:
    """Booking Traveler information tied to invoice.

    :ivar name:
    :ivar booking_traveler_ref: A reference to a passenger related to a ticket.
    :ivar passenger_type: Passenger Type Code.
    """
    name: Name = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element"
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute"
        )
    )
    passenger_type: str = field(
        default=None,
        metadata=dict(
            name="PassengerType",
            type="Attribute",
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class PassiveInfo:
    """Used by CreateReservationReq for passing in elements normally found post-
    booking.

    :ivar ticket_number:
    :ivar confirmation_number:
    :ivar commission:
    :ivar provider_code:
    :ivar provider_locator_code:
    :ivar supplier_code:
    :ivar supplier_locator_code:
    """
    ticket_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    confirmation_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ConfirmationNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    commission: Commission = field(
        default=None,
        metadata=dict(
            name="Commission",
            type="Element"
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute"
        )
    )
    provider_locator_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute"
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute"
        )
    )
    supplier_locator_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierLocatorCode",
            type="Attribute"
        )
    )


@dataclass
class Payment(AttrElementKeyResults):
    """
    Payment information - must be used in conjunction with credit card info
    :ivar key:
    :ivar type: Identifies the type of payment. This can be for an itinerary, a traveler, or a service fee for example.
    :ivar form_of_payment_ref: The credit card that is will be used to make this payment.
    :ivar booking_traveler_ref: If the type represents a per traveler payment, then this will reference the traveler this payment refers to.
    :ivar amount:
    :ivar amount_type: This field displays type of payment amount when it is non-monetary. Presently available/supported value is "Flight Pass Credits".
    :ivar approximate_amount: It stores the converted payment amount in agency's default currency
    :ivar status: Status to indicate the business association of the payment element.
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
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
    form_of_payment_ref: str = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Attribute",
            required=True
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute"
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True
        )
    )
    amount_type: str = field(
        default=None,
        metadata=dict(
            name="AmountType",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    approximate_amount: str = field(
        default=None,
        metadata=dict(
            name="ApproximateAmount",
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


@dataclass
class PermittedProviders:
    """
    :ivar provider:
    """
    provider: Provider = field(
        default=None,
        metadata=dict(
            name="Provider",
            type="Element",
            required=True
        )
    )


@dataclass
class PhoneNumber(AttrElementKeyResults):
    """Consists of type (office, home, fax), location (city code), the country
    code, the number, and an extension.

    :ivar provider_reservation_info_ref:
    :ivar key:
    :ivar type:
    :ivar location: IATA code for airport or city
    :ivar country_code: Hosts/providers will expect this to be international dialing digits
    :ivar area_code:
    :ivar number: The local phone number
    :ivar extension:
    :ivar text:
    """
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )
    location: str = field(
        default=None,
        metadata=dict(
            name="Location",
            type="Attribute",
            max_length=10.0
        )
    )
    country_code: str = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Attribute",
            max_length=5.0
        )
    )
    area_code: str = field(
        default=None,
        metadata=dict(
            name="AreaCode",
            type="Attribute",
            max_length=10.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=83.0
        )
    )
    extension: str = field(
        default=None,
        metadata=dict(
            name="Extension",
            type="Attribute",
            max_length=10.0
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            max_length=1024.0
        )
    )


@dataclass
class PolicyInformation:
    """Policy Information required for File Finishing.

    :ivar reason_code: Reason Code
    :ivar type: Policy Type - Air, Hotel, Car, Rail, Ticketing
    :ivar name: Policy Name
    :ivar out_of_policy: In Policy / Out of Policy Indicator
    :ivar segment_ref:
    """
    reason_code: "PolicyInformation.ReasonCode" = field(
        default=None,
        metadata=dict(
            name="ReasonCode",
            type="Element"
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
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute"
        )
    )
    out_of_policy: bool = field(
        default=None,
        metadata=dict(
            name="OutOfPolicy",
            type="Attribute"
        )
    )
    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )

    @dataclass
    class ReasonCode:
        """
        :ivar out_of_policy: Reason Code - Out of Policy
        :ivar purpose_of_trip: Reason Code -Purpose of Trip
        :ivar remark:
        """
        out_of_policy: str = field(
            default=None,
            metadata=dict(
                name="OutOfPolicy",
                type="Element"
            )
        )
        purpose_of_trip: str = field(
            default=None,
            metadata=dict(
                name="PurposeOfTrip",
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


@dataclass
class Postscript(TypeRemark):
    """Postscript Notes.

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )


@dataclass
class ProviderArnksegment:
    """Represents host ARNK segments.

    :ivar previous_segment:
    :ivar next_segment:
    :ivar key:
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar provider_segment_order: To identify the appropriate travel sequence for Air/Car/Hotel/Rail segments/reservations in the provider reservation.
    """
    previous_segment: "ProviderArnksegment.PreviousSegment" = field(
        default=None,
        metadata=dict(
            name="PreviousSegment",
            type="Element"
        )
    )
    next_segment: "ProviderArnksegment.NextSegment" = field(
        default=None,
        metadata=dict(
            name="NextSegment",
            type="Element"
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
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
    provider_segment_order: int = field(
        default=None,
        metadata=dict(
            name="ProviderSegmentOrder",
            type="Attribute",
            max_inclusive=999.0
        )
    )

    @dataclass
    class PreviousSegment:
        """
        :ivar air_segment_ref: Reference to AirSegment from an Air Reservation.
        :ivar hotel_reservation_ref: Specify the locator code of Hotel reservation.
        :ivar vehicle_reservation_ref: Specify the locator code of Vehicle reservation.
        :ivar passive_segment_ref: Reference to PassiveSegment from a Passive Reservation.
        """
        air_segment_ref: TypeSegmentRef = field(
            default=None,
            metadata=dict(
                name="AirSegmentRef",
                type="Element"
            )
        )
        hotel_reservation_ref: TypeNonAirReservationRef = field(
            default=None,
            metadata=dict(
                name="HotelReservationRef",
                type="Element"
            )
        )
        vehicle_reservation_ref: TypeNonAirReservationRef = field(
            default=None,
            metadata=dict(
                name="VehicleReservationRef",
                type="Element"
            )
        )
        passive_segment_ref: TypeSegmentRef = field(
            default=None,
            metadata=dict(
                name="PassiveSegmentRef",
                type="Element"
            )
        )

    @dataclass
    class NextSegment:
        """
        :ivar air_segment_ref: Reference to AirSegment from an Air Reservation.
        :ivar hotel_reservation_ref: Specify the locator code of Hotel reservation.
        :ivar vehicle_reservation_ref: Specify the locator code of Vehicle reservation.
        :ivar passive_segment_ref: Reference to PassiveSegment from a Passive Reservation.
        """
        air_segment_ref: TypeSegmentRef = field(
            default=None,
            metadata=dict(
                name="AirSegmentRef",
                type="Element"
            )
        )
        hotel_reservation_ref: TypeNonAirReservationRef = field(
            default=None,
            metadata=dict(
                name="HotelReservationRef",
                type="Element"
            )
        )
        vehicle_reservation_ref: TypeNonAirReservationRef = field(
            default=None,
            metadata=dict(
                name="VehicleReservationRef",
                type="Element"
            )
        )
        passive_segment_ref: TypeSegmentRef = field(
            default=None,
            metadata=dict(
                name="PassiveSegmentRef",
                type="Element"
            )
        )


@dataclass
class QueueSelector(AttrQueueInfo):
    """Identifies the Queue with Queue Number , Category and Date Range."""
    pass


@dataclass
class RailSeatAssignment(AttrElementKeyResults):
    """Identifies the seat assignment for a passenger on RailSegment.

    :ivar characteristic:
    :ivar key:
    :ivar status:
    :ivar seat:
    :ivar rail_segment_ref:
    :ivar coach_number:
    """
    characteristic: List[Characteristic] = field(
        default_factory=list,
        metadata=dict(
            name="Characteristic",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            required=True,
            length=2,
            white_space="collapse"
        )
    )
    seat: str = field(
        default=None,
        metadata=dict(
            name="Seat",
            type="Attribute",
            required=True
        )
    )
    rail_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="RailSegmentRef",
            type="Attribute"
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
class RequestKeyMappings:
    """All the elements for which mapping key sent in the request is different from
    the mapping key comes in the response.

    :ivar key_mapping:
    """
    key_mapping: List[KeyMapping] = field(
        default_factory=list,
        metadata=dict(
            name="KeyMapping",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class ReviewBooking(AttrElementKeyResults):
    """Review Booking or Queue Minders is to add the reminders in the Provider
    Reservation along with the date time and Queue details. On the date time
    defined in reminders, the message along with the PNR goes to the desired Queue.

    :ivar key: Returned in response. Use it for update of saved review booking.
    :ivar queue: Queue number, Must be numeric and less than 100.
    :ivar queue_category: Queue Category, 2 Character Alpha or Numeric.
    :ivar date_time: Date and Time to place message on designated Queue, Should be prior to the last segment date in the PNR.
    :ivar pseudo_city_code: Input PCC optional value for placing the PNR into Queue. If not passed, will add as default PNR's Pseudo.
    :ivar provider_code: The code of the Provider (e.g 1G,1V).
    :ivar provider_reservation_info_ref: Provider Reservation reference. Returned in the response. Use it for update of saved Review Booking.
    :ivar remarks: Remark or reminder message. It can be truncated depending on the provider.
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    queue: int = field(
        default=None,
        metadata=dict(
            name="Queue",
            type="Attribute",
            required=True,
            max_inclusive=99.0
        )
    )
    queue_category: str = field(
        default=None,
        metadata=dict(
            name="QueueCategory",
            type="Attribute",
            max_length=2.0
        )
    )
    date_time: str = field(
        default=None,
        metadata=dict(
            name="DateTime",
            type="Attribute",
            required=True
        )
    )
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=2.0,
            max_length=10.0
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
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute"
        )
    )
    remarks: str = field(
        default=None,
        metadata=dict(
            name="Remarks",
            type="Attribute",
            required=True,
            max_length=300.0
        )
    )


@dataclass
class SearchEvent(TypeTimeRange):
    """Search for various reservation events.

    :ivar type:
    """
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )


@dataclass
class SeatAssignment(AttrElementKeyResults):
    """
    :ivar key:
    :ivar status:
    :ivar seat:
    :ivar seat_type_code: The 4 letter SSR code like SMSW,NSSW,SMST etc.
    :ivar segment_ref:
    :ivar flight_details_ref:
    :ivar rail_coach_number: Coach number for which rail seatmap/coachmap is returned.
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            required=True,
            length=2,
            white_space="collapse"
        )
    )
    seat: str = field(
        default=None,
        metadata=dict(
            name="Seat",
            type="Attribute",
            required=True
        )
    )
    seat_type_code: str = field(
        default=None,
        metadata=dict(
            name="SeatTypeCode",
            type="Attribute",
            length=4,
            white_space="collapse"
        )
    )
    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )
    flight_details_ref: str = field(
        default=None,
        metadata=dict(
            name="FlightDetailsRef",
            type="Attribute"
        )
    )
    rail_coach_number: str = field(
        default=None,
        metadata=dict(
            name="RailCoachNumber",
            type="Attribute"
        )
    )


@dataclass
class SeatAttributes:
    """Identifies the seat attribute of the service.

    :ivar seat_attribute:
    """
    seat_attribute: List[SeatAttribute] = field(
        default_factory=list,
        metadata=dict(
            name="SeatAttribute",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class Segment(AttrElementKeyResults):
    """The base segment type.

    :ivar segment_remark:
    :ivar key:
    :ivar status: Status of this segment.
    :ivar passive:
    :ivar travel_order: To identify the appropriate travel sequence for Air/Car/Hotel segments/reservations based on travel dates. This ordering is applicable across the UR not provider or traveler specific
    :ivar provider_segment_order: To identify the appropriate travel sequence for Air/Car/Hotel/Rail segments/reservations in the provider reservation.
    """
    segment_remark: List[SegmentRemark] = field(
        default_factory=list,
        metadata=dict(
            name="SegmentRemark",
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
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute"
        )
    )
    passive: bool = field(
        default=None,
        metadata=dict(
            name="Passive",
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
    provider_segment_order: int = field(
        default=None,
        metadata=dict(
            name="ProviderSegmentOrder",
            type="Attribute",
            max_inclusive=999.0
        )
    )


@dataclass
class ServiceInfo:
    """
    :ivar description: Description of the Service. Usually used in tandem with one or more media items.
    :ivar media_item:
    """
    description: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Description",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    media_item: List[MediaItem] = field(
        default_factory=list,
        metadata=dict(
            name="MediaItem",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )


@dataclass
class SpecialEquipment(AttrElementKeyResults):
    """
    :ivar key:
    :ivar type: Special equipment associated with a specific vehicle
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
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
class Ssr(AttrElementKeyResults):
    """Special serivces like wheel chair, or pet carrier.

    :ivar key:
    :ivar segment_ref: Reference to the air segment. May be required for some Types.
    :ivar passive_segment_ref: Reference to the passive segment.
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar type: Programmatic SSRs use codes recognized by the provider/supplier (example, VGML=vegetarian meal code). Manual SSRs do not have an associated programmatic code.
    :ivar status:
    :ivar free_text: Certain SSR types will require a free text message. For example MAAS (Meet and assist).
    :ivar carrier:
    :ivar carrier_specific_text: Carrier specific information which are not captured in the FreeText field(not present in IATA's standard SSR DOCO format). An example is VISA Expiration Date.
    :ivar description:
    :ivar provider_defined_type: Original Type as sent by the provider
    :ivar ssrrule_ref: UniqueID to associate a rule to the SSR
    :ivar url:
    :ivar profile_id: Key assigned for Secure Flight Document value from the specified profile
    :ivar profile_secure_flight_doc_key: Unique ID of Booking Traveler's Profile that contains the Secure flight Detail
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )
    passive_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="PassiveSegmentRef",
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
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True,
            min_length=4.0,
            max_length=4.0
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute"
        )
    )
    free_text: str = field(
        default=None,
        metadata=dict(
            name="FreeText",
            type="Attribute"
        )
    )
    carrier: str = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            length=2
        )
    )
    carrier_specific_text: str = field(
        default=None,
        metadata=dict(
            name="CarrierSpecificText",
            type="Attribute",
            min_length=1.0,
            max_length=64.0
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute"
        )
    )
    provider_defined_type: str = field(
        default=None,
        metadata=dict(
            name="ProviderDefinedType",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    ssrrule_ref: str = field(
        default=None,
        metadata=dict(
            name="SSRRuleRef",
            type="Attribute"
        )
    )
    url: str = field(
        default=None,
        metadata=dict(
            name="URL",
            type="Attribute"
        )
    )
    profile_id: str = field(
        default=None,
        metadata=dict(
            name="ProfileID",
            type="Attribute"
        )
    )
    profile_secure_flight_doc_key: str = field(
        default=None,
        metadata=dict(
            name="ProfileSecureFlightDocKey",
            type="Attribute"
        )
    )


@dataclass
class SupplierLocator:
    """Locator code on the host carrier system.

    :ivar segment_ref: Air/Passive Segment Reference
    :ivar supplier_code: Carrier Code
    :ivar supplier_locator_code: Carrier reservation locator code
    :ivar provider_reservation_info_ref: Provider Reservation reference
    :ivar create_date_time: The Date and Time which the reservation is received from the Vendor as a SupplierLocator creation Date.
    """
    segment_ref: List[TypeGeneralReference] = field(
        default_factory=list,
        metadata=dict(
            name="SegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            required=True,
            length=2
        )
    )
    supplier_locator_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierLocatorCode",
            type="Attribute",
            required=True
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute"
        )
    )
    create_date_time: str = field(
        default=None,
        metadata=dict(
            name="CreateDateTime",
            type="Attribute"
        )
    )


@dataclass
class TaxDetail(AttrTaxDetail):
    """The tax idetail nformation for a fare quote tax."""
    pass


@dataclass
class ThirdPartyInformation(AttrElementKeyResults):
    """Third party supplier locator information. Specifically applicable for SDK
    booking.

    :ivar segment_ref: Air/Passive Segment Reference
    :ivar third_party_code: Third party supplier code.
    :ivar third_party_locator_code: Confirmation number for third party supplier.
    :ivar third_party_name: Third party supplier name.
    :ivar provider_reservation_info_ref: Provider Reservation reference
    :ivar key: Unique identifier of the third party supplier. Key can be used to modify or delete saved third party information.
    """
    segment_ref: List[TypeGeneralReference] = field(
        default_factory=list,
        metadata=dict(
            name="SegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    third_party_code: str = field(
        default=None,
        metadata=dict(
            name="ThirdPartyCode",
            type="Attribute",
            min_length=2.0,
            max_length=5.0
        )
    )
    third_party_locator_code: str = field(
        default=None,
        metadata=dict(
            name="ThirdPartyLocatorCode",
            type="Attribute",
            max_length=36.0
        )
    )
    third_party_name: str = field(
        default=None,
        metadata=dict(
            name="ThirdPartyName",
            type="Attribute",
            max_length=64.0
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute"
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
class TravelComplianceData(AttrElementKeyResults):
    """Travel Compliance and Preferred Supplier information of the traveler
    specific to a segment.

    :ivar policy_compliance:
    :ivar contract_compliance:
    :ivar preferred_supplier:
    :ivar key: System generated key, returned back in the response. This can be used to modify or delete a saved TravelComplianceData.
    :ivar air_segment_ref: Refers to Air Segment. Applicable only for Air. Ignored for others.
    :ivar passive_segment_ref: Refers to Passive Segment. Applicable only for Passive. Ignored for others.
    :ivar rail_segment_ref: Refers to Rail Segment. Applicable only for Rail. Ignored for others.
    :ivar reservation_locator_ref: This is returned in the response. Any input will be ignored for this attribute. This represents the association of Travel Compliance Data with the uAPI reservation locator code, mainly relevant to Hotel and Vehicle.
    """
    policy_compliance: List["TravelComplianceData.PolicyCompliance"] = field(
        default_factory=list,
        metadata=dict(
            name="PolicyCompliance",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )
    contract_compliance: List["TravelComplianceData.ContractCompliance"] = field(
        default_factory=list,
        metadata=dict(
            name="ContractCompliance",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )
    preferred_supplier: List["TravelComplianceData.PreferredSupplier"] = field(
        default_factory=list,
        metadata=dict(
            name="PreferredSupplier",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    air_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Attribute"
        )
    )
    passive_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="PassiveSegmentRef",
            type="Attribute"
        )
    )
    rail_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="RailSegmentRef",
            type="Attribute"
        )
    )
    reservation_locator_ref: str = field(
        default=None,
        metadata=dict(
            name="ReservationLocatorRef",
            type="Attribute",
            min_length=5.0,
            max_length=8.0
        )
    )

    @dataclass
    class PolicyCompliance:
        """
        :ivar in_policy: Policy Compliance Indicator. For In-Policy set to 'true', For Out-Of-Policy set to 'false''.
        :ivar policy_token: Optional text message to set the rule or token for which it's In Policy or Out Of Policy.
        """
        in_policy: bool = field(
            default=None,
            metadata=dict(
                name="InPolicy",
                type="Attribute",
                required=True
            )
        )
        policy_token: str = field(
            default=None,
            metadata=dict(
                name="PolicyToken",
                type="Attribute",
                min_length=1.0,
                max_length=128.0
            )
        )

    @dataclass
    class ContractCompliance:
        """
        :ivar in_contract: Contract Compliance Indicator. For In-Contract set to 'true', For Out-Of-Contract set to 'false'.
        :ivar contract_token: Optional text message to set the rule or token for which it's In Contract or Out Of Contract.
        """
        in_contract: bool = field(
            default=None,
            metadata=dict(
                name="InContract",
                type="Attribute",
                required=True
            )
        )
        contract_token: str = field(
            default=None,
            metadata=dict(
                name="ContractToken",
                type="Attribute",
                min_length=1.0,
                max_length=128.0
            )
        )

    @dataclass
    class PreferredSupplier:
        """
        :ivar preferred: Preferred Supplier - 'true', 'false'.
        :ivar profile_type: Indicate profile type. e.g. if Agency Preferred then pass Agency, if Traveler Preferred then pass Traveler.
        """
        preferred: bool = field(
            default=None,
            metadata=dict(
                name="Preferred",
                type="Attribute",
                required=True
            )
        )
        profile_type: str = field(
            default=None,
            metadata=dict(
                name="ProfileType",
                type="Attribute",
                required=True
            )
        )


@dataclass
class TypeAgencyHierarchyLongReference(TypeAgencyHierarchyReference):
    """
    :ivar profile_version:
    :ivar profile_name: Initially: Agent: Last, First, Branch: BranchCode, Agency: Name. After new profile implementation: Agent: UserName, others levels: Name.
    """
    profile_version: int = field(
        default=None,
        metadata=dict(
            name="ProfileVersion",
            type="Attribute",
            required=True
        )
    )
    profile_name: str = field(
        default=None,
        metadata=dict(
            name="ProfileName",
            type="Attribute",
            required=True,
            max_length=102.0
        )
    )


@dataclass
class TypeAssociatedRemark(TypeRemarkWithTravelerRef):
    """A textual remark container to hold Associated itinerary remarks.

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )


@dataclass
class TypeErrorInfo:
    """Container for error data when there is an application error.

    :ivar code:
    :ivar service:
    :ivar type:
    :ivar description:
    :ivar transaction_id:
    :ivar trace_id:
    :ivar command_history:
    :ivar auxdata:
    :ivar stack_trace:
    """
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Element",
            required=True
        )
    )
    service: str = field(
        default=None,
        metadata=dict(
            name="Service",
            type="Element",
            required=True
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Element",
            required=True
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Element",
            required=True
        )
    )
    transaction_id: str = field(
        default=None,
        metadata=dict(
            name="TransactionId",
            type="Element",
            required=True
        )
    )
    trace_id: str = field(
        default=None,
        metadata=dict(
            name="TraceId",
            type="Element"
        )
    )
    command_history: str = field(
        default=None,
        metadata=dict(
            name="CommandHistory",
            type="Element"
        )
    )
    auxdata: Auxdata = field(
        default=None,
        metadata=dict(
            name="Auxdata",
            type="Element"
        )
    )
    stack_trace: str = field(
        default=None,
        metadata=dict(
            name="StackTrace",
            type="Element"
        )
    )


@dataclass
class TypeFeeInfo(AttrProviderSupplier, AttrElementKeyResults):
    """A generic type of fee for those charges which are incurred by the passenger,
    but not necessarily shown on tickets.

    :ivar tax_info_ref: This reference elements will associate relevant taxes to this fee
    :ivar included_in_base:
    :ivar base_amount:
    :ivar description:
    :ivar sub_code:
    :ivar key:
    :ivar amount:
    :ivar code:
    :ivar fee_token:
    :ivar payment_ref: The reference to the one of the air reservation payments if fee included in charge
    :ivar booking_traveler_ref: Reference to booking traveler
    :ivar passenger_type_code:
    :ivar text: Additional Information returned from Supplier.(ACH only)
    """
    tax_info_ref: List["TypeFeeInfo.TaxInfoRef"] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    included_in_base: IncludedInBase = field(
        default=None,
        metadata=dict(
            name="IncludedInBase",
            type="Element"
        )
    )
    base_amount: str = field(
        default=None,
        metadata=dict(
            name="BaseAmount",
            type="Attribute"
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute"
        )
    )
    sub_code: str = field(
        default=None,
        metadata=dict(
            name="SubCode",
            type="Attribute"
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
            type="Attribute",
            required=True
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )
    fee_token: str = field(
        default=None,
        metadata=dict(
            name="FeeToken",
            type="Attribute"
        )
    )
    payment_ref: str = field(
        default=None,
        metadata=dict(
            name="PaymentRef",
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
    passenger_type_code: str = field(
        default=None,
        metadata=dict(
            name="PassengerTypeCode",
            type="Attribute",
            min_length=3.0,
            max_length=5.0
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            min_length=1.0,
            max_length=64.0
        )
    )

    @dataclass
    class TaxInfoRef:
        """
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
class TypeKeyword:
    """A complexType for keyword information.

    :ivar sub_key: A further breakdown of a keyword.
    :ivar text: Information for a keyword.
    :ivar name: The keyword name.
    :ivar number: The number for this keyword.
    :ivar description: A brief description of the keyword
    :ivar language_code: ISO 639 two-character language codes are used to retrieve specific information in the requested language. For Rich Content and Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE, DECH can also be used. Only certain services support this attribute. Providers: ACH, RCH, 1G, 1V, 1P, 1J.
    """
    sub_key: List[TypeSubKey] = field(
        default_factory=list,
        metadata=dict(
            name="SubKey",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            required=True,
            max_length=12.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute"
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
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
class TypeLocation:
    """
    :ivar airport:
    :ivar city:
    :ivar city_or_airport:
    """
    airport: Airport = field(
        default=None,
        metadata=dict(
            name="Airport",
            type="Element"
        )
    )
    city: City = field(
        default=None,
        metadata=dict(
            name="City",
            type="Element"
        )
    )
    city_or_airport: CityOrAirport = field(
        default=None,
        metadata=dict(
            name="CityOrAirport",
            type="Element"
        )
    )


@dataclass
class TypeOtakeyword:
    """A complexType for keyword information.

    :ivar sub_key: A further breakdown of a keyword.
    :ivar text: Information for a keyword.
    :ivar name: The keyword name.
    :ivar number: The number for this keyword.
    :ivar description: A brief description of the keyword
    """
    sub_key: List[TypeOtasubKey] = field(
        default_factory=list,
        metadata=dict(
            name="SubKey",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            required=True,
            max_length=6.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute"
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute"
        )
    )


@dataclass
class TypeProviderReservationDetail(ProviderReservation):
    """Details of a provider reservation locator consisting of provider locator
    code and provider code.

    To be used as a request element type while accessing a specific PNR
    """
    pass


@dataclass
class TypeProviderReservationSpecificInfo:
    """
    :ivar operated_by: Cross accrual carrier info
    :ivar provider_reservation_info_ref: Tagging provider reservation info with LoyaltyCard.
    :ivar provider_reservation_level: If true means Loyalty card is applied at ProviderReservation level.
    :ivar reservation_level: If true means Loyalty card is applied at Universal Record Reservation level e.g. Hotel Reservation, Vehicle Reservation etc.
    """
    operated_by: List[OperatedBy] = field(
        default_factory=list,
        metadata=dict(
            name="OperatedBy",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info_ref: ProviderReservationInfoRef = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element"
        )
    )
    provider_reservation_level: bool = field(
        default=None,
        metadata=dict(
            name="ProviderReservationLevel",
            type="Attribute"
        )
    )
    reservation_level: bool = field(
        default=None,
        metadata=dict(
            name="ReservationLevel",
            type="Attribute"
        )
    )


@dataclass
class TypeSearchLocation:
    """
    :ivar distance:
    :ivar airport:
    :ivar city:
    :ivar city_or_airport:
    :ivar coordinate_location:
    :ivar rail_location:
    """
    distance: Distance = field(
        default=None,
        metadata=dict(
            name="Distance",
            type="Element"
        )
    )
    airport: Airport = field(
        default=None,
        metadata=dict(
            name="Airport",
            type="Element"
        )
    )
    city: City = field(
        default=None,
        metadata=dict(
            name="City",
            type="Element"
        )
    )
    city_or_airport: CityOrAirport = field(
        default=None,
        metadata=dict(
            name="CityOrAirport",
            type="Element"
        )
    )
    coordinate_location: CoordinateLocation = field(
        default=None,
        metadata=dict(
            name="CoordinateLocation",
            type="Element"
        )
    )
    rail_location: RailLocation = field(
        default=None,
        metadata=dict(
            name="RailLocation",
            type="Element"
        )
    )


@dataclass
class TypeStructuredAddress(AttrElementKeyResults):
    """A fully structured address.

    :ivar address_name:
    :ivar street: The Address street and number, e.g. 105 Main St.
    :ivar city: The city name for the requested address, e.g. Atlanta.
    :ivar state: The State or Province of address requested, e.g. CA, Ontario.
    :ivar postal_code: The 5-15 alphanumeric postal Code for the requested address, e.g. 90210.
    :ivar country: The Full country name or two letter ISO country code e.g. US, France. A two letter country code is required for a Postal Code Searches.
    :ivar provider_reservation_info_ref: Tagging provider reservation info with Address.
    :ivar key: Key for update/delete of the element
    """
    address_name: str = field(
        default=None,
        metadata=dict(
            name="AddressName",
            type="Element",
            max_length=128.0
        )
    )
    street: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Street",
            type="Element",
            min_occurs=0,
            max_occurs=5,
            min_length=1.0,
            max_length=255.0
        )
    )
    city: str = field(
        default=None,
        metadata=dict(
            name="City",
            type="Element",
            min_length=2.0,
            max_length=50.0
        )
    )
    state: State = field(
        default=None,
        metadata=dict(
            name="State",
            type="Element"
        )
    )
    postal_code: str = field(
        default=None,
        metadata=dict(
            name="PostalCode",
            type="Element",
            min_length=1.0,
            max_length=15.0
        )
    )
    country: str = field(
        default=None,
        metadata=dict(
            name="Country",
            type="Element",
            length=2
        )
    )
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=99
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
class TypeTimeSpec:
    """Specifies times as either specific times, or a time range.

    :ivar time_range:
    :ivar specific_time:
    :ivar preferred_time: Specifies a time that would be preferred within the time range specified.
    """
    time_range: TypeTimeRange = field(
        default=None,
        metadata=dict(
            name="TimeRange",
            type="Element"
        )
    )
    specific_time: TypeSpecificTime = field(
        default=None,
        metadata=dict(
            name="SpecificTime",
            type="Element"
        )
    )
    preferred_time: str = field(
        default=None,
        metadata=dict(
            name="PreferredTime",
            type="Attribute"
        )
    )


@dataclass
class TypeTransactionsAllowed(TypeBookingTransactionsAllowed):
    """
    :ivar shopping_enabled: Allow or prohibit shopping transaction for the given product type on this Provider/Supplier. Inheritable.
    :ivar pricing_enabled: Allow or prohibit pricing transaction for the given product type on this Provider/Supplier. Inheritable.
    """
    shopping_enabled: bool = field(
        default=None,
        metadata=dict(
            name="ShoppingEnabled",
            type="Attribute"
        )
    )
    pricing_enabled: bool = field(
        default=None,
        metadata=dict(
            name="PricingEnabled",
            type="Attribute"
        )
    )


@dataclass
class UnassociatedRemark(TypeRemarkWithTravelerRef):
    """A textual remark container to hold non-associated itinerary remarks.

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )


@dataclass
class VendorLocation(TypeVendorLocation):
    """Location definition specific to a Vendor in a specific provider (e.g. 1G)
    system."""
    pass


@dataclass
class AccountInformation:
    """Account Information required for File Finishing.

    :ivar address:
    :ivar phone_number:
    :ivar account_name:
    """
    address: TypeStructuredAddress = field(
        default=None,
        metadata=dict(
            name="Address",
            type="Element"
        )
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    account_name: str = field(
        default=None,
        metadata=dict(
            name="AccountName",
            type="Attribute"
        )
    )


@dataclass
class AgencyContactInfo:
    """Generic agency contact information container. It must contain at least one
    phone number to be used by an agency.

    :ivar phone_number:
    :ivar key:
    """
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            min_occurs=1,
            max_occurs=999
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
class AgencyInfo:
    """Tracks the various agent/agency information.

    :ivar agent_action:
    """
    agent_action: List[AgentAction] = field(
        default_factory=list,
        metadata=dict(
            name="AgentAction",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AgencyInformation:
    """Agency Information required for File Finishing.

    :ivar address:
    :ivar email:
    :ivar phone_number:
    """
    address: TypeStructuredAddress = field(
        default=None,
        metadata=dict(
            name="Address",
            type="Element"
        )
    )
    email: List[Email] = field(
        default_factory=list,
        metadata=dict(
            name="Email",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirSeatAssignment(SeatAssignment):
    """Identifies the seat assignment for a passenger."""
    pass


@dataclass
class BaseReservation:
    """
    :ivar accounting_remark:
    :ivar general_remark:
    :ivar restriction:
    :ivar passive_info:
    :ivar locator_code: The unique identifier for this reservation. If this is this View Only UR LocatorCode is '999999'.
    :ivar create_date: The date and time that this reservation was created.
    :ivar modified_date: The date and time that this reservation was last modified for any reason.
    :ivar customer_number:
    """
    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata=dict(
            name="AccountingRemark",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata=dict(
            name="GeneralRemark",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    restriction: List[Restriction] = field(
        default_factory=list,
        metadata=dict(
            name="Restriction",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    passive_info: PassiveInfo = field(
        default=None,
        metadata=dict(
            name="PassiveInfo",
            type="Element"
        )
    )
    locator_code: str = field(
        default=None,
        metadata=dict(
            name="LocatorCode",
            type="Attribute",
            required=True,
            min_length=5.0,
            max_length=8.0
        )
    )
    create_date: str = field(
        default=None,
        metadata=dict(
            name="CreateDate",
            type="Attribute",
            required=True
        )
    )
    modified_date: str = field(
        default=None,
        metadata=dict(
            name="ModifiedDate",
            type="Attribute",
            required=True
        )
    )
    customer_number: str = field(
        default=None,
        metadata=dict(
            name="CustomerNumber",
            type="Attribute"
        )
    )


@dataclass
class ConnectionPoint(TypeLocation):
    """A connection point can be eith an IATA airport or cir city code."""
    pass


@dataclass
class DeliveryInfo:
    """Container to encapsulate all delivery related information.

    :ivar shipping_address:
    :ivar phone_number:
    :ivar email:
    :ivar general_remark:
    :ivar provider_reservation_info_ref: Tagging provider reservation info with Delivery Info.
    :ivar type: An arbitrary identifier to categorize this delivery info
    :ivar signature_required: Indicates whether a signature shoud be required in order to make the delivery.
    :ivar tracking_number: The tracking number of the shipping company making the delivery.
    """
    shipping_address: "DeliveryInfo.ShippingAddress" = field(
        default=None,
        metadata=dict(
            name="ShippingAddress",
            type="Element"
        )
    )
    phone_number: PhoneNumber = field(
        default=None,
        metadata=dict(
            name="PhoneNumber",
            type="Element"
        )
    )
    email: Email = field(
        default=None,
        metadata=dict(
            name="Email",
            type="Element"
        )
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata=dict(
            name="GeneralRemark",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )
    signature_required: str = field(
        default=None,
        metadata=dict(
            name="SignatureRequired",
            type="Attribute",
            max_length=10.0
        )
    )
    tracking_number: str = field(
        default=None,
        metadata=dict(
            name="TrackingNumber",
            type="Attribute"
        )
    )

    @dataclass
    class ShippingAddress(TypeStructuredAddress):
        
        pass


@dataclass
class InvoiceData:
    """List of invoices only for 1G/1V.

    :ivar booking_traveler_information:
    :ivar key:
    :ivar invoice_number: Invoice number
    :ivar issue_date: Invoice issue date
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    """
    booking_traveler_information: List[BookingTravelerInformation] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerInformation",
            type="Element",
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
    invoice_number: str = field(
        default=None,
        metadata=dict(
            name="InvoiceNumber",
            type="Attribute",
            required=True
        )
    )
    issue_date: str = field(
        default=None,
        metadata=dict(
            name="IssueDate",
            type="Attribute"
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            required=True
        )
    )


@dataclass
class InvoiceRemark(TypeAssociatedRemark):
    """
    :ivar air_segment_ref: Reference to AirSegment from an Air Reservation.
    :ivar hotel_reservation_ref: Specify the locator code of Hotel reservation.
    :ivar vehicle_reservation_ref: Specify the locator code of Vehicle reservation.
    :ivar passive_segment_ref: Reference to PassiveSegment from a Passive Reservation.
    """
    air_segment_ref: TypeSegmentRef = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Element"
        )
    )
    hotel_reservation_ref: TypeNonAirReservationRef = field(
        default=None,
        metadata=dict(
            name="HotelReservationRef",
            type="Element"
        )
    )
    vehicle_reservation_ref: TypeNonAirReservationRef = field(
        default=None,
        metadata=dict(
            name="VehicleReservationRef",
            type="Element"
        )
    )
    passive_segment_ref: TypeSegmentRef = field(
        default=None,
        metadata=dict(
            name="PassiveSegmentRef",
            type="Element"
        )
    )


@dataclass
class Keyword(TypeKeyword):
    """Detail information of keywords."""
    pass


@dataclass
class LocationAddress(TypeStructuredAddress):
    
    pass


@dataclass
class LoyaltyCard(AttrLoyalty):
    """Provider loyalty card information.

    :ivar provider_reservation_specific_info:
    :ivar card_number:
    :ivar status:
    :ivar membership_status:
    :ivar free_text:
    :ivar supplier_type:
    :ivar level:
    :ivar priority_code:
    :ivar vendor_location_ref:
    """
    provider_reservation_specific_info: List[TypeProviderReservationSpecificInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationSpecificInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    card_number: str = field(
        default=None,
        metadata=dict(
            name="CardNumber",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=36.0
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute"
        )
    )
    membership_status: str = field(
        default=None,
        metadata=dict(
            name="MembershipStatus",
            type="Attribute"
        )
    )
    free_text: str = field(
        default=None,
        metadata=dict(
            name="FreeText",
            type="Attribute"
        )
    )
    supplier_type: str = field(
        default=None,
        metadata=dict(
            name="SupplierType",
            type="Attribute"
        )
    )
    level: str = field(
        default=None,
        metadata=dict(
            name="Level",
            type="Attribute",
            pattern="[a-zA-Z0-9]{1,1}"
        )
    )
    priority_code: str = field(
        default=None,
        metadata=dict(
            name="PriorityCode",
            type="Attribute",
            pattern="[a-zA-Z0-9]{1,1}"
        )
    )
    vendor_location_ref: str = field(
        default=None,
        metadata=dict(
            name="VendorLocationRef",
            type="Attribute"
        )
    )


@dataclass
class Mcoinformation:
    """
    :ivar passenger_info:
    :ivar mconumber: The unique MCO number
    :ivar status: Current status of the MCO
    :ivar mcotype: The Type of MCO. Once of Agency Fee, Airline Service Fee, or Residual value from an Exchange.
    """
    passenger_info: List[PassengerInfo] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    mconumber: str = field(
        default=None,
        metadata=dict(
            name="MCONumber",
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
    mcotype: str = field(
        default=None,
        metadata=dict(
            name="MCOType",
            type="Attribute"
        )
    )


@dataclass
class PaymentRestriction:
    """
    :ivar card_restriction:
    :ivar address_restriction:
    """
    card_restriction: List[CardRestriction] = field(
        default_factory=list,
        metadata=dict(
            name="CardRestriction",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    address_restriction: AddressRestriction = field(
        default=None,
        metadata=dict(
            name="AddressRestriction",
            type="Element",
            required=True
        )
    )


@dataclass
class ProviderReservationDetail(TypeProviderReservationDetail):
    """common element for mentioning provider reservation locator (PNR) details in
    request."""
    pass


@dataclass
class QueuePlace:
    """Allow queue placement of a PNR at the time of booking to be used for
    Providers 1G,1V,1P and 1J.

    :ivar pseudo_city_code: Pseudo City Code
    :ivar queue_selector: Identifies the Queue Information to be selected for placing the UR
    """
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Element",
            min_length=2.0,
            max_length=10.0
        )
    )
    queue_selector: List[QueueSelector] = field(
        default_factory=list,
        metadata=dict(
            name="QueueSelector",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class ReservationName:
    """Container to represent reservation name as appears in GDS booking.

    :ivar booking_traveler_ref:
    :ivar name_override: To be used if the reservation name is other than booking travelers in the PNR
    """
    booking_traveler_ref: BookingTravelerRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            required=True
        )
    )
    name_override: NameOverride = field(
        default=None,
        metadata=dict(
            name="NameOverride",
            type="Element",
            required=True
        )
    )


@dataclass
class ServiceData:
    """
    :ivar seat_attributes:
    :ivar cabin_class:
    :ivar ssrref: References to the related SSRs. At present, only reference to ASVC SSR is supported. Supported providers are 1G/1V/1P/1J
    :ivar data: Data that specifies the details of the merchandising offering (e.g. seat number for seat service)
    :ivar air_segment_ref: Reference to a segment if the merchandising offering only pertains to that segment. If no segment reference is present this means this offering is for the whole itinerary.
    :ivar booking_traveler_ref: Reference to a passenger if the merchandising offering only pertains to that passenger. If no passenger reference is present this means this offering is for all passengers.
    :ivar stop_over: Indicates that there is a significant delay between flights (usually 12 hours or more)
    :ivar traveler_type: Passenger Type Code.
    :ivar emdsummary_ref: Reference to the corresponding EMD issued. Supported providers are 1G/1V/1P/1J
    :ivar emdcoupon_ref: Reference to the corresponding EMD coupon issued. Supported providers are 1G/1V/1P/1J
    """
    seat_attributes: SeatAttributes = field(
        default=None,
        metadata=dict(
            name="SeatAttributes",
            type="Element"
        )
    )
    cabin_class: CabinClass = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element"
        )
    )
    ssrref: List[TypeKeyBasedReference] = field(
        default_factory=list,
        metadata=dict(
            name="SSRRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    data: str = field(
        default=None,
        metadata=dict(
            name="Data",
            type="Attribute"
        )
    )
    air_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
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
    stop_over: bool = field(
        default="false",
        metadata=dict(
            name="StopOver",
            type="Attribute"
        )
    )
    traveler_type: str = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            min_length=3.0,
            max_length=5.0
        )
    )
    emdsummary_ref: str = field(
        default=None,
        metadata=dict(
            name="EMDSummaryRef",
            type="Attribute"
        )
    )
    emdcoupon_ref: str = field(
        default=None,
        metadata=dict(
            name="EMDCouponRef",
            type="Attribute"
        )
    )


@dataclass
class Ssrinfo:
    """Bundle SSR with BookingTraveler reference in order to add SSR post booking.

    :ivar ssr:
    :ivar booking_traveler_ref: Reference to Booking Traveler.
    """
    ssr: Ssr = field(
        default=None,
        metadata=dict(
            name="SSR",
            type="Element",
            required=True
        )
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class TransactionType:
    """Configuration for products by type. Inheritable.

    :ivar air:
    :ivar hotel:
    :ivar rail:
    :ivar vehicle:
    :ivar passive: For true passive segments such as ground, cruise etc
    :ivar background_passive: For behind the scenes or background passives Only
    """
    air: "TransactionType.Air" = field(
        default=None,
        metadata=dict(
            name="Air",
            type="Element"
        )
    )
    hotel: TypeTransactionsAllowed = field(
        default=None,
        metadata=dict(
            name="Hotel",
            type="Element"
        )
    )
    rail: TypeTransactionsAllowed = field(
        default=None,
        metadata=dict(
            name="Rail",
            type="Element"
        )
    )
    vehicle: TypeTransactionsAllowed = field(
        default=None,
        metadata=dict(
            name="Vehicle",
            type="Element"
        )
    )
    passive: TypeBookingTransactionsAllowed = field(
        default=None,
        metadata=dict(
            name="Passive",
            type="Element"
        )
    )
    background_passive: TypeBookingTransactionsAllowed = field(
        default=None,
        metadata=dict(
            name="BackgroundPassive",
            type="Element"
        )
    )

    @dataclass
    class Air(TypeTransactionsAllowed):
        """
        :ivar one_way_shop: Allows or prohibits one way shopping functionality for the associated provisioning provider configuration
        :ivar flex_explore: Allows or prohibits flex explore functionality for the associated provisioning provider configuration
        :ivar rapid_reprice_enabled: Allows or prohibits rapid reprice functionality for the associated provisioning provider configuration. Providers: 1G/1V
        :ivar return_upsell_fare: When set to “true”, Upsell information will be returned in the shop response. Provider: 1G, 1V, 1P, 1J, ACH
        """
        one_way_shop: bool = field(
            default=None,
            metadata=dict(
                name="OneWayShop",
                type="Attribute"
            )
        )
        flex_explore: bool = field(
            default=None,
            metadata=dict(
                name="FlexExplore",
                type="Attribute"
            )
        )
        rapid_reprice_enabled: bool = field(
            default=None,
            metadata=dict(
                name="RapidRepriceEnabled",
                type="Attribute"
            )
        )
        return_upsell_fare: bool = field(
            default=None,
            metadata=dict(
                name="ReturnUpsellFare",
                type="Attribute"
            )
        )


@dataclass
class TravelSegment(Segment):
    """Generic segment used to provide travel information that was not processed by
    the system.

    :ivar origin: The IATA location code for this origination of this entity.
    :ivar destination: The IATA location code for this destination of this entity.
    :ivar departure_time: The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.
    :ivar arrival_time:
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
            type="Attribute"
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
class TravelerInformation:
    """Traveler Information required for File Finishing.

    :ivar emergency_contact:
    :ivar home_airport:
    :ivar visa_expiration_date:
    :ivar booking_traveler_ref: A reference to a passenger.
    """
    emergency_contact: "TravelerInformation.EmergencyContact" = field(
        default=None,
        metadata=dict(
            name="EmergencyContact",
            type="Element"
        )
    )
    home_airport: str = field(
        default=None,
        metadata=dict(
            name="HomeAirport",
            type="Attribute",
            length=3
        )
    )
    visa_expiration_date: str = field(
        default=None,
        metadata=dict(
            name="VisaExpirationDate",
            type="Attribute"
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
    class EmergencyContact:
        """
        :ivar phone_number:
        :ivar name: Name of Emergency Contact Person
        :ivar relationship: Relationship between Traveler and Emergency Contact Person
        """
        phone_number: PhoneNumber = field(
            default=None,
            metadata=dict(
                name="PhoneNumber",
                type="Element"
            )
        )
        name: str = field(
            default=None,
            metadata=dict(
                name="Name",
                type="Attribute"
            )
        )
        relationship: str = field(
            default=None,
            metadata=dict(
                name="Relationship",
                type="Attribute"
            )
        )


@dataclass
class TypeAssociatedRemarkWithSegmentRef(TypeAssociatedRemark):
    """A textual remark container to hold Associated itinerary remarks with segment
    association.

    :ivar segment_ref: Reference to an Air/Passive Segment
    """
    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )


@dataclass
class TypeFlexibleTimeSpec(TypeTimeSpec):
    """A type which can be used for flexible date/time specification -extends the
    generic type typeTimeSpec to provide extra options for search.

    :ivar search_extra_days: Options to search for extra days on top of the specified date
    """
    search_extra_days: "TypeFlexibleTimeSpec.SearchExtraDays" = field(
        default=None,
        metadata=dict(
            name="SearchExtraDays",
            type="Element"
        )
    )

    @dataclass
    class SearchExtraDays:
        """
        :ivar days_before: Number of days to search before the specified date
        :ivar days_after: Number of days to search after the specified date
        """
        days_before: int = field(
            default=None,
            metadata=dict(
                name="DaysBefore",
                type="Attribute"
            )
        )
        days_after: int = field(
            default=None,
            metadata=dict(
                name="DaysAfter",
                type="Attribute"
            )
        )


@dataclass
class TypePaymentCard:
    """Container for all credit and debit card information.

    :ivar phone_number:
    :ivar billing_address: The address to where the billing statements for this card are sent. Used for address verification purposes.
    :ivar type: The 2 letter credit/ debit card type.
    :ivar number:
    :ivar exp_date: The Expiration date of this card in YYYY-MM format.
    :ivar name: The name as it appears on the card.
    :ivar cvv: Card Verification Code
    :ivar approval_code: This code is required for an authorization process from the Credit Card company directly,required for some of the CCH carriers.This attribute is also used for EMD retrieve and issuance transactions.
    """
    phone_number: PhoneNumber = field(
        default=None,
        metadata=dict(
            name="PhoneNumber",
            type="Element"
        )
    )
    billing_address: TypeStructuredAddress = field(
        default=None,
        metadata=dict(
            name="BillingAddress",
            type="Element"
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            min_length=2.0,
            max_length=2.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            min_length=13.0,
            max_length=128.0
        )
    )
    exp_date: str = field(
        default=None,
        metadata=dict(
            name="ExpDate",
            type="Attribute"
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            max_length=128.0
        )
    )
    cvv: str = field(
        default=None,
        metadata=dict(
            name="CVV",
            type="Attribute",
            max_length=4.0
        )
    )
    approval_code: str = field(
        default=None,
        metadata=dict(
            name="ApprovalCode",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )


@dataclass
class TypeTaxInfo(AttrTaxDetail):
    """
    :ivar tax_detail:
    :ivar included_in_base:
    :ivar key: The tax key represents a valid key of tax
    :ivar category: The tax category represents a valid IATA tax code.
    :ivar carrier_defined_category: Optional category, where a carrier has used a non-standard IATA tax category. The tax category will be set to "DU"
    :ivar segment_ref: The segment to which that tax is relative (if applicable)
    :ivar flight_details_ref: The flight details that this tax is relative to (if applicable)
    :ivar coupon_ref: The coupon to which that tax is relative (if applicable)
    :ivar tax_exempted: This indicates whether the tax specified by tax category is exempted.
    :ivar provider_code: Code of the provider returning this TaxInfo.
    :ivar supplier_code: Code of the supplier returning this TaxInfo.
    :ivar text: Additional Information returned from Supplier.(ACH only)
    """
    tax_detail: List[TaxDetail] = field(
        default_factory=list,
        metadata=dict(
            name="TaxDetail",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    included_in_base: IncludedInBase = field(
        default=None,
        metadata=dict(
            name="IncludedInBase",
            type="Element"
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            required=True
        )
    )
    carrier_defined_category: str = field(
        default=None,
        metadata=dict(
            name="CarrierDefinedCategory",
            type="Attribute"
        )
    )
    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )
    flight_details_ref: str = field(
        default=None,
        metadata=dict(
            name="FlightDetailsRef",
            type="Attribute"
        )
    )
    coupon_ref: str = field(
        default=None,
        metadata=dict(
            name="CouponRef",
            type="Attribute"
        )
    )
    tax_exempted: bool = field(
        default=None,
        metadata=dict(
            name="TaxExempted",
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
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            min_length=1.0,
            max_length=5.0
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            min_length=1.0,
            max_length=128.0
        )
    )


@dataclass
class AirExchangeInfo:
    """Provides results of a exchange quote.

    :ivar total_penalty_tax_info:
    :ivar paid_tax:
    :ivar ticket_fee_info: Used for rapid reprice. Providers: 1G/1V/1P/1S/1A
    :ivar reason: Used for rapid reprice. The reason code or text is returned if the PricingTag is not equal to A, and explains why A was not returned. Providers: 1G/1V/1P/1S/1A
    :ivar fee_info:
    :ivar tax_info: Itinerary level taxes
    :ivar exchange_amount:
    :ivar base_fare:
    :ivar equivalent_base_fare:
    :ivar taxes:
    :ivar change_fee:
    :ivar forfeit_amount:
    :ivar refundable:
    :ivar exchangeable:
    :ivar first_class_upgrade:
    :ivar ticket_by_date:
    :ivar pricing_tag:
    :ivar equivalent_change_fee:
    :ivar equivalent_exchange_amount:
    :ivar add_collection:
    :ivar residual_value:
    :ivar total_residual_value:
    :ivar original_flight_value:
    :ivar flown_segment_value:
    :ivar bulk_ticket_advisory:
    :ivar fare_pull:
    :ivar passenger_type_code:
    :ivar passenger_count:
    :ivar form_of_refund: How the refund will be issued. Values will be MCO or FormOfPayment
    :ivar refund: Total refund amount.
    """
    total_penalty_tax_info: "AirExchangeInfo.TotalPenaltyTaxInfo" = field(
        default=None,
        metadata=dict(
            name="TotalPenaltyTaxInfo",
            type="Element"
        )
    )
    paid_tax: List[TypeTax] = field(
        default_factory=list,
        metadata=dict(
            name="PaidTax",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticket_fee_info: List["AirExchangeInfo.TicketFeeInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="TicketFeeInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    reason: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Reason",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[TypeFeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TypeTaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    exchange_amount: str = field(
        default=None,
        metadata=dict(
            name="ExchangeAmount",
            type="Attribute",
            required=True
        )
    )
    base_fare: str = field(
        default=None,
        metadata=dict(
            name="BaseFare",
            type="Attribute"
        )
    )
    equivalent_base_fare: str = field(
        default=None,
        metadata=dict(
            name="EquivalentBaseFare",
            type="Attribute"
        )
    )
    taxes: str = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    change_fee: str = field(
        default=None,
        metadata=dict(
            name="ChangeFee",
            type="Attribute"
        )
    )
    forfeit_amount: str = field(
        default=None,
        metadata=dict(
            name="ForfeitAmount",
            type="Attribute"
        )
    )
    refundable: bool = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute"
        )
    )
    exchangeable: bool = field(
        default=None,
        metadata=dict(
            name="Exchangeable",
            type="Attribute"
        )
    )
    first_class_upgrade: bool = field(
        default=None,
        metadata=dict(
            name="FirstClassUpgrade",
            type="Attribute"
        )
    )
    ticket_by_date: str = field(
        default=None,
        metadata=dict(
            name="TicketByDate",
            type="Attribute"
        )
    )
    pricing_tag: str = field(
        default=None,
        metadata=dict(
            name="PricingTag",
            type="Attribute"
        )
    )
    equivalent_change_fee: str = field(
        default=None,
        metadata=dict(
            name="EquivalentChangeFee",
            type="Attribute"
        )
    )
    equivalent_exchange_amount: str = field(
        default=None,
        metadata=dict(
            name="EquivalentExchangeAmount",
            type="Attribute"
        )
    )
    add_collection: str = field(
        default=None,
        metadata=dict(
            name="AddCollection",
            type="Attribute"
        )
    )
    residual_value: str = field(
        default=None,
        metadata=dict(
            name="ResidualValue",
            type="Attribute"
        )
    )
    total_residual_value: str = field(
        default=None,
        metadata=dict(
            name="TotalResidualValue",
            type="Attribute"
        )
    )
    original_flight_value: str = field(
        default=None,
        metadata=dict(
            name="OriginalFlightValue",
            type="Attribute"
        )
    )
    flown_segment_value: str = field(
        default=None,
        metadata=dict(
            name="FlownSegmentValue",
            type="Attribute"
        )
    )
    bulk_ticket_advisory: bool = field(
        default=None,
        metadata=dict(
            name="BulkTicketAdvisory",
            type="Attribute"
        )
    )
    fare_pull: str = field(
        default=None,
        metadata=dict(
            name="FarePull",
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
    passenger_count: int = field(
        default=None,
        metadata=dict(
            name="PassengerCount",
            type="Attribute"
        )
    )
    form_of_refund: str = field(
        default=None,
        metadata=dict(
            name="FormOfRefund",
            type="Attribute"
        )
    )
    refund: str = field(
        default=None,
        metadata=dict(
            name="Refund",
            type="Attribute"
        )
    )

    @dataclass
    class TotalPenaltyTaxInfo:
        """
        :ivar penalty_tax_info:
        :ivar total_penalty_tax:
        """
        penalty_tax_info: List[TypeTax] = field(
            default_factory=list,
            metadata=dict(
                name="PenaltyTaxInfo",
                type="Element",
                min_occurs=0,
                max_occurs=999
            )
        )
        total_penalty_tax: str = field(
            default=None,
            metadata=dict(
                name="TotalPenaltyTax",
                type="Attribute"
            )
        )

    @dataclass
    class TicketFeeInfo:
        """
        :ivar base:
        :ivar tax:
        :ivar total:
        """
        base: str = field(
            default=None,
            metadata=dict(
                name="Base",
                type="Attribute"
            )
        )
        tax: str = field(
            default=None,
            metadata=dict(
                name="Tax",
                type="Attribute"
            )
        )
        total: str = field(
            default=None,
            metadata=dict(
                name="Total",
                type="Attribute"
            )
        )


@dataclass
class Apiprovider:
    """
    :ivar transaction_type:
    :ivar available_pseudo_city_code:
    :ivar provider_code: The Provider Code of the host
    :ivar supplier_code: The Supplier Code of the host
    :ivar iatacode: Agency IATA or ARC code, used as an ID with airlines.
    """
    transaction_type: TransactionType = field(
        default=None,
        metadata=dict(
            name="TransactionType",
            type="Element"
        )
    )
    available_pseudo_city_code: List["Apiprovider.AvailablePseudoCityCode"] = field(
        default_factory=list,
        metadata=dict(
            name="AvailablePseudoCityCode",
            type="Element",
            min_occurs=0,
            max_occurs=999
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
            min_length=1.0,
            max_length=5.0
        )
    )
    iatacode: str = field(
        default=None,
        metadata=dict(
            name="IATACode",
            type="Attribute",
            max_length=8.0
        )
    )

    @dataclass
    class AvailablePseudoCityCode:
        """
        :ivar pseudo_city_code: The PseudoCityCode used to connect to the host.
        """
        pseudo_city_code: str = field(
            default=None,
            metadata=dict(
                name="PseudoCityCode",
                type="Attribute",
                min_length=2.0,
                max_length=10.0
            )
        )


@dataclass
class BookingTraveler(AttrBookingTravelerGrp, AttrElementKeyResults):
    """A traveler and all their accompanying data.

    :ivar ssr:
    :ivar name_remark:
    :ivar air_seat_assignment:
    :ivar rail_seat_assignment:
    :ivar name_number: Host Name Number
    """
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata=dict(
            name="SSR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    name_remark: List[NameRemark] = field(
        default_factory=list,
        metadata=dict(
            name="NameRemark",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_seat_assignment: List[AirSeatAssignment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSeatAssignment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_seat_assignment: List[RailSeatAssignment] = field(
        default_factory=list,
        metadata=dict(
            name="RailSeatAssignment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    name_number: str = field(
        default=None,
        metadata=dict(
            name="NameNumber",
            type="Attribute"
        )
    )


@dataclass
class BookingTravelerInfo:
    """Container that will allow modifying Universal record data that is not
    product specific.

    :ivar booking_traveler_name:
    :ivar name_remark:
    :ivar dob: Traveler Date of Birth
    :ivar travel_info:
    :ivar email:
    :ivar phone_number:
    :ivar address:
    :ivar emergency_info:
    :ivar delivery_info:
    :ivar age:
    :ivar customized_name_data:
    :ivar applied_profile:
    :ivar key:
    :ivar traveler_type:
    :ivar gender:
    """
    booking_traveler_name: BookingTravelerName = field(
        default=None,
        metadata=dict(
            name="BookingTravelerName",
            type="Element"
        )
    )
    name_remark: NameRemark = field(
        default=None,
        metadata=dict(
            name="NameRemark",
            type="Element"
        )
    )
    dob: str = field(
        default=None,
        metadata=dict(
            name="DOB",
            type="Element"
        )
    )
    travel_info: TravelInfo = field(
        default=None,
        metadata=dict(
            name="TravelInfo",
            type="Element"
        )
    )
    email: Email = field(
        default=None,
        metadata=dict(
            name="Email",
            type="Element"
        )
    )
    phone_number: PhoneNumber = field(
        default=None,
        metadata=dict(
            name="PhoneNumber",
            type="Element"
        )
    )
    address: TypeStructuredAddress = field(
        default=None,
        metadata=dict(
            name="Address",
            type="Element"
        )
    )
    emergency_info: str = field(
        default=None,
        metadata=dict(
            name="EmergencyInfo",
            type="Element"
        )
    )
    delivery_info: DeliveryInfo = field(
        default=None,
        metadata=dict(
            name="DeliveryInfo",
            type="Element"
        )
    )
    age: int = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Element"
        )
    )
    customized_name_data: CustomizedNameData = field(
        default=None,
        metadata=dict(
            name="CustomizedNameData",
            type="Element"
        )
    )
    applied_profile: AppliedProfile = field(
        default=None,
        metadata=dict(
            name="AppliedProfile",
            type="Element"
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    traveler_type: str = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            min_length=3.0,
            max_length=5.0
        )
    )
    gender: str = field(
        default=None,
        metadata=dict(
            name="Gender",
            type="Attribute",
            min_length=1.0,
            max_length=2.0
        )
    )


@dataclass
class DebitCard(TypePaymentCard):
    """Container for all debit card information.

    :ivar issue_number: Verification number for Debit Cards
    """
    issue_number: str = field(
        default=None,
        metadata=dict(
            name="IssueNumber",
            type="Attribute",
            max_length=8.0
        )
    )


@dataclass
class FileFinishingInfo:
    """Misc Data required for File Finishing. This data is transient and not saved
    in database.

    :ivar shop_information:
    :ivar policy_information: Policy Information required for File Finishing. Would repeat per Policy Type
    :ivar account_information:
    :ivar agency_information:
    :ivar traveler_information:
    :ivar custom_profile_information:
    """
    shop_information: ShopInformation = field(
        default=None,
        metadata=dict(
            name="ShopInformation",
            type="Element"
        )
    )
    policy_information: List[PolicyInformation] = field(
        default_factory=list,
        metadata=dict(
            name="PolicyInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    account_information: AccountInformation = field(
        default=None,
        metadata=dict(
            name="AccountInformation",
            type="Element"
        )
    )
    agency_information: AgencyInformation = field(
        default=None,
        metadata=dict(
            name="AgencyInformation",
            type="Element"
        )
    )
    traveler_information: List[TravelerInformation] = field(
        default_factory=list,
        metadata=dict(
            name="TravelerInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    custom_profile_information: CustomProfileInformation = field(
        default=None,
        metadata=dict(
            name="CustomProfileInformation",
            type="Element"
        )
    )


@dataclass
class Group(AttrElementKeyResults):
    """Represents a traveler group for Group booking and all their accompanying
    data. SUPPORTED PROVIDER: Worldspan and JAL.

    :ivar name: Name of the group in group booking.
    :ivar delivery_info:
    :ivar phone_number:
    :ivar ssrref: Reference Element for SSR.
    :ivar address:
    :ivar booking_traveler_ref: Reference Element for Booking Traveler.
    :ivar key:
    :ivar traveler_type: Defines the type of traveler used for booking which could be a non-defining type (Companion, Web-fare, etc), or a standard type (Adult, Child, etc).
    :ivar group_size: Represents size of the group
    """
    name: "Group.Name" = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            required=True
        )
    )
    delivery_info: DeliveryInfo = field(
        default=None,
        metadata=dict(
            name="DeliveryInfo",
            type="Element"
        )
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ssrref: List["Group.Ssrref"] = field(
        default_factory=list,
        metadata=dict(
            name="SSRRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    address: TypeStructuredAddress = field(
        default=None,
        metadata=dict(
            name="Address",
            type="Element"
        )
    )
    booking_traveler_ref: List["Group.BookingTravelerRef"] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    traveler_type: str = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            min_length=3.0,
            max_length=5.0
        )
    )
    group_size: int = field(
        default=None,
        metadata=dict(
            name="GroupSize",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class Name:
        """
        :ivar value:
        """
        value: str = field(
            default=None,
            metadata=dict(
                name="value",
                type="Restriction",
                min_length=1.0,
                white_space="collapse"
            )
        )

    @dataclass
    class Ssrref:
        """
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
    class BookingTravelerRef:
        """
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
class McopriceData:
    """
    :ivar tax_info:
    :ivar commission:
    :ivar mcoamount: The total value of the MCO including any processing fees.
    :ivar mcoequivalent_fare: Exchange value of the currency actually collected.
    :ivar mcototal_amount: The Total amount for the MCO.
    """
    tax_info: List[TypeTaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    commission: "McopriceData.Commission" = field(
        default=None,
        metadata=dict(
            name="Commission",
            type="Element"
        )
    )
    mcoamount: str = field(
        default=None,
        metadata=dict(
            name="MCOAmount",
            type="Attribute",
            required=True
        )
    )
    mcoequivalent_fare: str = field(
        default=None,
        metadata=dict(
            name="MCOEquivalentFare",
            type="Attribute"
        )
    )
    mcototal_amount: str = field(
        default=None,
        metadata=dict(
            name="MCOTotalAmount",
            type="Attribute"
        )
    )

    @dataclass
    class Commission(AttrAmountPercent):
        
        pass


@dataclass
class ServiceRuleType:
    """Contains the rules for applying service rules.

    :ivar application_rules: The rules to apply the rule to the itinerary
    :ivar application_level: Lists the levels where the option is applied in the itinerary. Some options are applied for the entire itinerary, some for entire segments, etc.
    :ivar modify_rules: Groups the modification rules for the Option
    :ivar secondary_type_rules: Lists the supported Secondary Codes for the optional / additional service.
    :ivar remarks: Adds text remarks / rules for the optional / additional service
    :ivar key: Unique ID to identify an optional service rule
    """
    application_rules: "ServiceRuleType.ApplicationRules" = field(
        default=None,
        metadata=dict(
            name="ApplicationRules",
            type="Element"
        )
    )
    application_level: "ServiceRuleType.ApplicationLevel" = field(
        default=None,
        metadata=dict(
            name="ApplicationLevel",
            type="Element"
        )
    )
    modify_rules: "ServiceRuleType.ModifyRules" = field(
        default=None,
        metadata=dict(
            name="ModifyRules",
            type="Element"
        )
    )
    secondary_type_rules: "ServiceRuleType.SecondaryTypeRules" = field(
        default=None,
        metadata=dict(
            name="SecondaryTypeRules",
            type="Element"
        )
    )
    remarks: List[FormattedTextTextType] = field(
        default_factory=list,
        metadata=dict(
            name="Remarks",
            type="Element",
            min_occurs=0,
            max_occurs=99
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
    class ApplicationRules:
        """
        :ivar required_for_all_travelers: Indicates if the option needs to be applied to all travelers in the itinerary if selected
        :ivar required_for_all_segments: Indicates if the option needs to be applied to all segments in the itinerary if selected
        :ivar required_for_all_segments_in_od: Indicates if the option needs to be applied to all segments in a origin / destination (connection flights) if selected for one segment in the OD
        :ivar unselected_option_required: If an UnselectedOption is present in the option, then the Unselected option needs to be selected even if the option is not selected when this flag is set to true
        :ivar secondary_option_code_required: If set to true, the secondary option code is required for this option
        """
        required_for_all_travelers: bool = field(
            default=None,
            metadata=dict(
                name="RequiredForAllTravelers",
                type="Attribute"
            )
        )
        required_for_all_segments: bool = field(
            default=None,
            metadata=dict(
                name="RequiredForAllSegments",
                type="Attribute"
            )
        )
        required_for_all_segments_in_od: bool = field(
            default=None,
            metadata=dict(
                name="RequiredForAllSegmentsInOD",
                type="Attribute"
            )
        )
        unselected_option_required: bool = field(
            default=None,
            metadata=dict(
                name="UnselectedOptionRequired",
                type="Attribute"
            )
        )
        secondary_option_code_required: bool = field(
            default=None,
            metadata=dict(
                name="SecondaryOptionCodeRequired",
                type="Attribute"
            )
        )

    @dataclass
    class ApplicationLevel:
        """
        :ivar application_limits: Adds the limits on the number of options that can be selected for a particular type
        :ivar service_data:
        :ivar applicable_levels: Indicates the level in the itinerary when the option is applied.
        :ivar provider_defined_applicable_levels: Indicates the actual provider defined ApplicableLevels which is mapped to Other
        """
        application_limits: "ServiceRuleType.ApplicationLevel.ApplicationLimits" = field(
            default=None,
            metadata=dict(
                name="ApplicationLimits",
                type="Element"
            )
        )
        service_data: List[ServiceData] = field(
            default_factory=list,
            metadata=dict(
                name="ServiceData",
                type="Element",
                min_occurs=0,
                max_occurs=999
            )
        )
        applicable_levels: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ApplicableLevels",
                type="Attribute",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        provider_defined_applicable_levels: str = field(
            default=None,
            metadata=dict(
                name="ProviderDefinedApplicableLevels",
                type="Attribute"
            )
        )

        @dataclass
        class ApplicationLimits:
            """
            :ivar application_limit: The application limits for a particular level
            """
            application_limit: List[OptionalServiceApplicationLimitType] = field(
                default_factory=list,
                metadata=dict(
                    name="ApplicationLimit",
                    type="Element",
                    min_occurs=1,
                    max_occurs=10
                )
            )

    @dataclass
    class ModifyRules:
        """
        :ivar modify_rule: Indicates modification rules for the particular modification type.
        :ivar supported_modifications: Lists the supported modifications for the itinerary.
        :ivar provider_defined_modification_type: Indicates the actual provider defined modification type which is mapped to Other
        """
        modify_rule: List["ServiceRuleType.ModifyRules.ModifyRule"] = field(
            default_factory=list,
            metadata=dict(
                name="ModifyRule",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )
        supported_modifications: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="SupportedModifications",
                type="Attribute",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        provider_defined_modification_type: str = field(
            default=None,
            metadata=dict(
                name="ProviderDefinedModificationType",
                type="Attribute"
            )
        )

        @dataclass
        class ModifyRule(ModificationRulesGroup):
            
            pass

    @dataclass
    class SecondaryTypeRules:
        """
        :ivar secondary_type_rule: Lists a single secondary code for the optional / additional service.
        """
        secondary_type_rule: List["ServiceRuleType.SecondaryTypeRules.SecondaryTypeRule"] = field(
            default_factory=list,
            metadata=dict(
                name="SecondaryTypeRule",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

        @dataclass
        class SecondaryTypeRule:
            """
            :ivar application_limit:
            :ivar secondary_type: The unique type to associate a secondary type in an optional service
            """
            application_limit: List[OptionalServiceApplicationLimitType] = field(
                default_factory=list,
                metadata=dict(
                    name="ApplicationLimit",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )
            secondary_type: str = field(
                default=None,
                metadata=dict(
                    name="SecondaryType",
                    type="Attribute",
                    required=True
                )
            )


@dataclass
class TypeCreditCardType(TypePaymentCard):
    """
    :ivar extended_payment: Used for American Express cards.
    :ivar customer_reference: Agencies use this to pass the traveler information to the credit card company.
    :ivar acceptance_override: Override airline restriction on the credit card.
    :ivar third_party_payment: If true, this indicates that the credit card holder is not one of the passengers.
    :ivar bank_name: Issuing bank name for this credit card
    :ivar bank_country_code: ISO Country code associated with the issuing bank
    :ivar bank_state_code: State code associated with the issuing bank.
    :ivar enett: Acceptable values are true or false. If set to true it will denote that the credit card used has been issued through Enett. For all other credit card payments this value will be set to false.
    """
    extended_payment: str = field(
        default=None,
        metadata=dict(
            name="ExtendedPayment",
            type="Attribute"
        )
    )
    customer_reference: str = field(
        default=None,
        metadata=dict(
            name="CustomerReference",
            type="Attribute"
        )
    )
    acceptance_override: bool = field(
        default=None,
        metadata=dict(
            name="AcceptanceOverride",
            type="Attribute"
        )
    )
    third_party_payment: bool = field(
        default="false",
        metadata=dict(
            name="ThirdPartyPayment",
            type="Attribute"
        )
    )
    bank_name: str = field(
        default=None,
        metadata=dict(
            name="BankName",
            type="Attribute"
        )
    )
    bank_country_code: str = field(
        default=None,
        metadata=dict(
            name="BankCountryCode",
            type="Attribute",
            length=2
        )
    )
    bank_state_code: str = field(
        default=None,
        metadata=dict(
            name="BankStateCode",
            type="Attribute",
            max_length=6.0
        )
    )
    enett: bool = field(
        default="false",
        metadata=dict(
            name="Enett",
            type="Attribute"
        )
    )


@dataclass
class TypePassengerType:
    """Passenger type code with optional age information.

    :ivar name: Optional passenger Name with associated LoyaltyCard may provide benefit when pricing itineraries using Low Cost Carriers. In general, most carriers do not consider passenger LoyalyCard information when initially pricing itineraries.
    :ivar loyalty_card:
    :ivar discount_card:
    :ivar personal_geography: Passenger personal geography detail to be sent to Host for accessing location specific fares
    :ivar code: The 3-char IATA passenger type code
    :ivar age:
    :ivar dob: Passenger Date of Birth
    :ivar gender: The passenger gender type
    :ivar price_ptconly:
    :ivar booking_traveler_ref: This value should be set for Multiple Passengers in the request.
    :ivar accompanied_passenger: Container to identify accompanied passenger. Set true means this passenger is accompanied
    :ivar residency_type: The passenger residence type.
    """
    name: Name = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element"
        )
    )
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyCard",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    discount_card: List[DiscountCard] = field(
        default_factory=list,
        metadata=dict(
            name="DiscountCard",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    personal_geography: PersonalGeography = field(
        default=None,
        metadata=dict(
            name="PersonalGeography",
            type="Element"
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=3.0,
            max_length=5.0
        )
    )
    age: int = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute"
        )
    )
    dob: str = field(
        default=None,
        metadata=dict(
            name="DOB",
            type="Attribute"
        )
    )
    gender: str = field(
        default=None,
        metadata=dict(
            name="Gender",
            type="Attribute",
            min_length=1.0,
            max_length=2.0
        )
    )
    price_ptconly: bool = field(
        default=None,
        metadata=dict(
            name="PricePTCOnly",
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
    accompanied_passenger: bool = field(
        default="false",
        metadata=dict(
            name="AccompaniedPassenger",
            type="Attribute"
        )
    )
    residency_type: str = field(
        default=None,
        metadata=dict(
            name="ResidencyType",
            type="Attribute"
        )
    )


@dataclass
class CreditCard(TypeCreditCardType):
    """Container for all credit card information."""
    pass


@dataclass
class SearchPassenger(TypePassengerType):
    """Passenger type with code and optional age information.

    :ivar key:
    """
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )


@dataclass
class FormOfPayment(AttrElementKeyResults):
    """A Form of Payment used to purchase all or part of a booking.

    :ivar provider_reservation_info_ref:
    :ivar segment_ref:
    :ivar bsppayment:
    :ivar arcpayment:
    :ivar credit_card:
    :ivar debit_card:
    :ivar enett_van:
    :ivar key:
    :ivar type:
    :ivar fulfillment_type: Defines how the client wishes to receive travel documents. Type does not define where or how payment is made. The supported values are "Ticket on Departure", "Travel Agency", "Courier", "Standard Mail", "Ticketless", "Ticket Office", "Express Mail", "Corporate Kiosk", "Train Station Service Desk", "Direct Printing of Ticket", "Ticket by Email", "Digital Printing of Ticket at Home", "Retrieve Ticket at Eurostar in London"
    Collect booking ticket at a Kiosk, print in agency.
    :ivar fulfillment_location: Information about the location of the printer.
    :ivar fulfillment_idtype: Identification type, e.g. credit card, to define how the customer will identify himself when collecting the ticket
    :ivar fulfillment_idnumber: Identification number, e.g. card number, to define how the customer will identify himself when collecting the ticket
    :ivar is_agent_type: If this is true then FormOfPayment mention in Type is anAgent type FormOfPayment.
    :ivar agent_text: This is only relevent when IsAgentType is specified as true. Otherwise this will be ignored.
    :ivar reuse_fop: Key of the FOP Key to be reused as this Form of Payment.Only Credit and Debit Card will be supported for FOP Reuse.
    :ivar external_reference:
    :ivar reusable: Indicates whether the form of payment can be reused or not. Currently applicable for Credit and Debit form of payment
    :ivar profile_id: The unique ID of the profile that contains the payment details to use.
    :ivar profile_key: The Key assigned to the payment details value from the specified profile.
    """
    provider_reservation_info_ref: List[TypeFormOfPaymentPnrreference] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    segment_ref: List[TypeGeneralReference] = field(
        default_factory=list,
        metadata=dict(
            name="SegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    bsppayment: Bsppayment = field(
        default=None,
        metadata=dict(
            name="BSPPayment",
            type="Element"
        )
    )
    arcpayment: Arcpayment = field(
        default=None,
        metadata=dict(
            name="ARCPayment",
            type="Element"
        )
    )
    credit_card: CreditCard = field(
        default=None,
        metadata=dict(
            name="CreditCard",
            type="Element"
        )
    )
    debit_card: DebitCard = field(
        default=None,
        metadata=dict(
            name="DebitCard",
            type="Element"
        )
    )
    enett_van: EnettVan = field(
        default=None,
        metadata=dict(
            name="EnettVan",
            type="Element"
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True,
            max_length=25.0
        )
    )
    fulfillment_type: str = field(
        default=None,
        metadata=dict(
            name="FulfillmentType",
            type="Attribute"
        )
    )
    fulfillment_location: str = field(
        default=None,
        metadata=dict(
            name="FulfillmentLocation",
            type="Attribute"
        )
    )
    fulfillment_idtype: str = field(
        default=None,
        metadata=dict(
            name="FulfillmentIDType",
            type="Attribute"
        )
    )
    fulfillment_idnumber: str = field(
        default=None,
        metadata=dict(
            name="FulfillmentIDNumber",
            type="Attribute"
        )
    )
    is_agent_type: bool = field(
        default="false",
        metadata=dict(
            name="IsAgentType",
            type="Attribute"
        )
    )
    agent_text: str = field(
        default=None,
        metadata=dict(
            name="AgentText",
            type="Attribute"
        )
    )
    reuse_fop: str = field(
        default=None,
        metadata=dict(
            name="ReuseFOP",
            type="Attribute"
        )
    )
    external_reference: str = field(
        default=None,
        metadata=dict(
            name="ExternalReference",
            type="Attribute",
            max_length=32.0
        )
    )
    reusable: bool = field(
        default="false",
        metadata=dict(
            name="Reusable",
            type="Attribute"
        )
    )
    profile_id: str = field(
        default=None,
        metadata=dict(
            name="ProfileID",
            type="Attribute"
        )
    )
    profile_key: str = field(
        default=None,
        metadata=dict(
            name="ProfileKey",
            type="Attribute"
        )
    )


@dataclass
class Guarantee(AttrElementKeyResults):
    """Payment Guarantee Guarantee, Deposit or PrePayment.

    :ivar credit_card:
    :ivar other_guarantee_info:
    :ivar type: Guarantee, Deposit for 1G/1V/1P/1J and PrePayment for 1P/1J only
    :ivar key: Key for update/delete of the element
    :ivar reuse_fop: Key of the FOP Key to be reused as this Form of Payment.Only Credit and Debit Card will be supported for FOP Reuse.
    :ivar external_reference:
    :ivar reusable: Indicates whether the form of payment can be reused or not. Currently applicable for Credit and Debit form of payment
    """
    credit_card: CreditCard = field(
        default=None,
        metadata=dict(
            name="CreditCard",
            type="Element"
        )
    )
    other_guarantee_info: OtherGuaranteeInfo = field(
        default=None,
        metadata=dict(
            name="OtherGuaranteeInfo",
            type="Element"
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
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    reuse_fop: str = field(
        default=None,
        metadata=dict(
            name="ReuseFOP",
            type="Attribute"
        )
    )
    external_reference: str = field(
        default=None,
        metadata=dict(
            name="ExternalReference",
            type="Attribute",
            max_length=32.0
        )
    )
    reusable: bool = field(
        default="false",
        metadata=dict(
            name="Reusable",
            type="Attribute"
        )
    )


@dataclass
class McoexchangeInfo:
    """Information related to the exchange tickets available for the MCO.

    :ivar form_of_payment:
    :ivar exchanged_coupon:
    :ivar original_ticket_number: Airline form and serial number of the original ticket issued.
    :ivar original_city_code: Location of honoring carrier or operator.
    :ivar original_ticket_date: Date that the Original ticket was issued.
    :ivar iatacode: IATA code of the issuing agency.
    """
    form_of_payment: FormOfPayment = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element"
        )
    )
    exchanged_coupon: List[ExchangedCoupon] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangedCoupon",
            type="Element",
            min_occurs=0,
            max_occurs=4
        )
    )
    original_ticket_number: str = field(
        default=None,
        metadata=dict(
            name="OriginalTicketNumber",
            type="Attribute",
            length=13
        )
    )
    original_city_code: str = field(
        default=None,
        metadata=dict(
            name="OriginalCityCode",
            type="Attribute",
            length=3
        )
    )
    original_ticket_date: str = field(
        default=None,
        metadata=dict(
            name="OriginalTicketDate",
            type="Attribute",
            pattern="[^:Z].*"
        )
    )
    iatacode: str = field(
        default=None,
        metadata=dict(
            name="IATACode",
            type="Attribute",
            max_length=8.0
        )
    )


@dataclass
class ServiceFeeInfo(AttrElementKeyResults):
    """Travel Agency Service Fees (TASF) are charged by the agency through BSP or
    Airline Reporting Corporation (ARC).

    :ivar form_of_payment:
    :ivar service_fee_tax_info:
    :ivar credit_card_auth:
    :ivar payment:
    :ivar status: Status of the service fee. Possible Values – Issued, ReadyToIssue, IssueLater.
    :ivar description: The description of the service fee.
    :ivar key:
    :ivar confirmation: The confirmation number of the service fee in the merchant host system.
    :ivar ticket_number: The ticket that this fee was issued in connection with.
    :ivar booking_traveler_ref: A reference to a passenger.
    :ivar provider_reservation_info_ref: A reference to the provider reservation info to which the service is tied.
    :ivar passive_provider_reservation_info_ref: A reference to the passive provider reservation info to which the service is tied.
    :ivar total_amount: The total amount for this Service Fee including base amount and all taxes.
    :ivar base_amount: Represents the base price for this entity. This does not include any taxes.
    :ivar taxes: The aggregated amount of all the taxes that are associated with this entity. See the associated Service Fee TaxInfo array for a breakdown of the individual taxes.
    :ivar booking_traveler_name: The name of the passenger.
    """
    form_of_payment: FormOfPayment = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element"
        )
    )
    service_fee_tax_info: List[ServiceFeeTaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceFeeTaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    credit_card_auth: CreditCardAuth = field(
        default=None,
        metadata=dict(
            name="CreditCardAuth",
            type="Element"
        )
    )
    payment: Payment = field(
        default=None,
        metadata=dict(
            name="Payment",
            type="Element"
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute"
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute"
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    confirmation: str = field(
        default=None,
        metadata=dict(
            name="Confirmation",
            type="Attribute"
        )
    )
    ticket_number: str = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
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
    total_amount: str = field(
        default=None,
        metadata=dict(
            name="TotalAmount",
            type="Attribute"
        )
    )
    base_amount: str = field(
        default=None,
        metadata=dict(
            name="BaseAmount",
            type="Attribute"
        )
    )
    taxes: str = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    booking_traveler_name: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerName",
            type="Attribute"
        )
    )


@dataclass
class Mco(Mcoinformation):
    """
    :ivar form_of_payment:
    :ivar endorsement:
    :ivar mcoexchange_info:
    :ivar mcofee_info:
    :ivar mcoremark:
    :ivar mcoprice_data:
    :ivar stock_control:
    :ivar mcotext:
    :ivar ticket_type: Ticket issue indicator. Possible values "Pre-paid ticket advice", "Ticket on departure" and "Other" .
    :ivar ticket_number: The ticket that this MCO was issued in connection with. Could be the ticket that caused the fee, a residual from an exchange, or an airline service fee.
    :ivar mcoissued: Set to true when the MCO is to be issued and set to false if it is stored for issue at a later time.
    :ivar mcoissue_date: Date and time in which the MCO was issued.
    :ivar mcodoc_num: MCO document number.
    :ivar issue_reason_code: MCO issuing reason code. Possible Values (List): A - Air transportation, B - Surface transportation
    C - Bag shipped as cargo, D - Land arrgs for it, E - Car hire, F - Sleeper / berth
    G - Up-grading, H - Under collections, I - Taxes/fees/charges, J - Deposits down payments
    K - Refundable Balances, L - Hotel accommodations, M - Sundry charges, N - Cancellation fee
    O - Other, P thru Z - airline specific, 1 thru 9 - market specific
    :ivar plating_carrier: The Plating Carrier for this MCO
    :ivar tour_operator: Tour Operator - name of honoring carrier or operator.
    :ivar location: Location of honoring carrier or operator.
    :ivar tour_code: The Tour Code of the MCO.
    :ivar provider_code: Contains the Provider Code of the provider that houses this MCO.
    :ivar provider_locator_code: Contains the Provider Locator Code of the Provider Reservation that houses this MCO.
    :ivar pseudo_city_code: The PCC in the host system.
    :ivar expiry_date: E-Voucher’s Expiry Date. This expiry date is specific to Rail product
    """
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    endorsement: Endorsement = field(
        default=None,
        metadata=dict(
            name="Endorsement",
            type="Element"
        )
    )
    mcoexchange_info: McoexchangeInfo = field(
        default=None,
        metadata=dict(
            name="MCOExchangeInfo",
            type="Element"
        )
    )
    mcofee_info: McofeeInfo = field(
        default=None,
        metadata=dict(
            name="MCOFeeInfo",
            type="Element"
        )
    )
    mcoremark: List[Mcoremark] = field(
        default_factory=list,
        metadata=dict(
            name="MCORemark",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    mcoprice_data: McopriceData = field(
        default=None,
        metadata=dict(
            name="MCOPriceData",
            type="Element"
        )
    )
    stock_control: List[StockControl] = field(
        default_factory=list,
        metadata=dict(
            name="StockControl",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    mcotext: List[Mcotext] = field(
        default_factory=list,
        metadata=dict(
            name="MCOText",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticket_type: str = field(
        default=None,
        metadata=dict(
            name="TicketType",
            type="Attribute"
        )
    )
    ticket_number: str = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute"
        )
    )
    mcoissued: bool = field(
        default=None,
        metadata=dict(
            name="MCOIssued",
            type="Attribute",
            required=True
        )
    )
    mcoissue_date: str = field(
        default=None,
        metadata=dict(
            name="MCOIssueDate",
            type="Attribute"
        )
    )
    mcodoc_num: str = field(
        default=None,
        metadata=dict(
            name="MCODocNum",
            type="Attribute"
        )
    )
    issue_reason_code: str = field(
        default=None,
        metadata=dict(
            name="IssueReasonCode",
            type="Attribute"
        )
    )
    plating_carrier: str = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            length=2
        )
    )
    tour_operator: str = field(
        default=None,
        metadata=dict(
            name="TourOperator",
            type="Attribute"
        )
    )
    location: str = field(
        default=None,
        metadata=dict(
            name="Location",
            type="Attribute"
        )
    )
    tour_code: str = field(
        default=None,
        metadata=dict(
            name="TourCode",
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
            type="Attribute",
            max_length=15.0
        )
    )
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=2.0,
            max_length=10.0
        )
    )
    expiry_date: str = field(
        default=None,
        metadata=dict(
            name="ExpiryDate",
            type="Attribute"
        )
    )