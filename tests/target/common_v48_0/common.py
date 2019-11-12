from dataclasses import dataclass, field
from typing import List




@dataclass
class CustomProfileInformation:
    """
    Custom Profile Field Data required for File Finishing
    """

    pass


@dataclass
class Location:
    """
    Used during search to specify an origin or destination location
    """

    pass


@dataclass
class TypeAgentInfo:
    pass


@dataclass
class TypeSearchTimeSpec:
    pass


@dataclass
class AccountInformation:
    """
    Account Information required for File Finishing
    """

    address: str = field(
        default=None,
        metadata=dict(
            name="Address",
            type="Element",
            help=None,
        )
    )
    phone_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    account_name: str = field(
        default=None,
        metadata=dict(
            name="AccountName",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AddSvc:
    """
    1P - Add SVC segments to collect additional fee
    """

    rfic: str = field(
        default=None,
        metadata=dict(
            name="RFIC",
            type="Attribute",
            help="1P - Reason for issuance",
        )
    )
    rfisc: str = field(
        default=None,
        metadata=dict(
            name="RFISC",
            type="Attribute",
            help="1P - Resaon for issuance sub-code",
        )
    )
    svc_description: str = field(
        default=None,
        metadata=dict(
            name="SvcDescription",
            type="Attribute",
            help="1P - SVC fee description",
        )
    )
    origin: str = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="Origin location - Airport code. If this value not provided, the last air segment arrival location is taken as default. 1P only.",
            length=3,
            white_space="collapse"
        )
    )
    destination: str = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="Destination location - Airport code.",
            length=3,
            white_space="collapse"
        )
    )
    start_date: str = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute",
            help="The start date of the SVC segment. If the value not specified, the default value is set as the date next to the last airsegment arrival date. 1P only",
        )
    )


@dataclass
class AddressRestriction:
    required_field: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="RequiredField",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AgencyContactInfo:
    """
    Generic agency contact information container. It must contain at least one phone number to be used by an agency
    """

    phone_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AgencyInfo:
    """
    Tracks the various agent/agency information
    """

    agent_action: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AgentAction",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AgencyInformation:
    """
    Agency Information required for File Finishing
    """

    address: str = field(
        default=None,
        metadata=dict(
            name="Address",
            type="Element",
            help=None,
        )
    )
    email: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Email",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    phone_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AgencySellInfo:
    """
    Information about the agency selling the reservation
    """

    iata_code: str = field(
        default=None,
        metadata=dict(
            name="IataCode",
            type="Attribute",
            help="The IATA code that pertains to this Agency and Branch.",
            max_length=8.0
        )
    )
    country: str = field(
        default=None,
        metadata=dict(
            name="Country",
            type="Attribute",
            help="The country code of the requesting agency.",
            length=2
        )
    )
    currency_code: str = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            help="The currency code in which the reservation will be ticketed.",
            length=3
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="The IATA assigned airline/GDS code.",
            min_length=2.0,
            max_length=5.0
        )
    )
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            help="The PCC in the host system.",
            min_length=2.0,
            max_length=10.0
        )
    )
    city_code: str = field(
        default=None,
        metadata=dict(
            name="CityCode",
            type="Attribute",
            help="IATA code of 'home' city or airport.",
            length=3,
            white_space="collapse"
        )
    )


@dataclass
class AgentIdoverride:
    """
    Vendor specific agent identifier overrides to be used to access vendor systems.
    """

    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help="Supplier code to determine which vendor this AgentId belongs to.",
            min_length=1.0,
            max_length=5.0
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Provider code to route the AgentId to proper provider.",
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
            help="The Agent ID for the applicable supplier/vendor",
            required=True,
            min_length=1.0,
            max_length=32.0
        )
    )


@dataclass
class AgentVoucher:
    """
    Agent Voucher Form of Payments
    """

    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class AirExchangeInfo:
    """
    Provides results of a exchange quote
    """

    total_penalty_tax_info: "AirExchangeInfo.str" = field(
        default=None,
        metadata=dict(
            name="TotalPenaltyTaxInfo",
            type="Element",
            help=None,
        )
    )
    paid_tax: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PaidTax",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    ticket_fee_info: List["AirExchangeInfo.str"] = field(
        default_factory=list,
        metadata=dict(
            name="TicketFeeInfo",
            type="Element",
            help="Used for rapid reprice. Providers: 1G/1V/1P/1S/1A",
            min_occurs=0,
            max_occurs=999
        )
    )
    reason: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Reason",
            type="Element",
            help="Used for rapid reprice. The reason code or text is returned if the PricingTag is not equal to A, and explains why A was not returned. Providers: 1G/1V/1P/1S/1A",
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help="Itinerary level taxes",
            min_occurs=0,
            max_occurs=999
        )
    )
    exchange_amount: str = field(
        default=None,
        metadata=dict(
            name="ExchangeAmount",
            type="Attribute",
            help=None,
            required=True
        )
    )
    base_fare: str = field(
        default=None,
        metadata=dict(
            name="BaseFare",
            type="Attribute",
            help=None,
        )
    )
    equivalent_base_fare: str = field(
        default=None,
        metadata=dict(
            name="EquivalentBaseFare",
            type="Attribute",
            help=None,
        )
    )
    taxes: str = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute",
            help=None,
        )
    )
    change_fee: str = field(
        default=None,
        metadata=dict(
            name="ChangeFee",
            type="Attribute",
            help=None,
        )
    )
    forfeit_amount: str = field(
        default=None,
        metadata=dict(
            name="ForfeitAmount",
            type="Attribute",
            help=None,
        )
    )
    refundable: str = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute",
            help=None,
        )
    )
    exchangeable: str = field(
        default=None,
        metadata=dict(
            name="Exchangeable",
            type="Attribute",
            help=None,
        )
    )
    first_class_upgrade: str = field(
        default=None,
        metadata=dict(
            name="FirstClassUpgrade",
            type="Attribute",
            help=None,
        )
    )
    ticket_by_date: str = field(
        default=None,
        metadata=dict(
            name="TicketByDate",
            type="Attribute",
            help=None,
        )
    )
    pricing_tag: str = field(
        default=None,
        metadata=dict(
            name="PricingTag",
            type="Attribute",
            help=None,
        )
    )
    equivalent_change_fee: str = field(
        default=None,
        metadata=dict(
            name="EquivalentChangeFee",
            type="Attribute",
            help=None,
        )
    )
    equivalent_exchange_amount: str = field(
        default=None,
        metadata=dict(
            name="EquivalentExchangeAmount",
            type="Attribute",
            help=None,
        )
    )
    add_collection: str = field(
        default=None,
        metadata=dict(
            name="AddCollection",
            type="Attribute",
            help=None,
        )
    )
    residual_value: str = field(
        default=None,
        metadata=dict(
            name="ResidualValue",
            type="Attribute",
            help=None,
        )
    )
    total_residual_value: str = field(
        default=None,
        metadata=dict(
            name="TotalResidualValue",
            type="Attribute",
            help=None,
        )
    )
    original_flight_value: str = field(
        default=None,
        metadata=dict(
            name="OriginalFlightValue",
            type="Attribute",
            help=None,
        )
    )
    flown_segment_value: str = field(
        default=None,
        metadata=dict(
            name="FlownSegmentValue",
            type="Attribute",
            help=None,
        )
    )
    bulk_ticket_advisory: str = field(
        default=None,
        metadata=dict(
            name="BulkTicketAdvisory",
            type="Attribute",
            help=None,
        )
    )
    fare_pull: str = field(
        default=None,
        metadata=dict(
            name="FarePull",
            type="Attribute",
            help=None,
        )
    )
    passenger_type_code: str = field(
        default=None,
        metadata=dict(
            name="PassengerTypeCode",
            type="Attribute",
            help=None,
            min_length=3.0,
            max_length=5.0
        )
    )
    passenger_count: str = field(
        default=None,
        metadata=dict(
            name="PassengerCount",
            type="Attribute",
            help=None,
        )
    )
    form_of_refund: str = field(
        default=None,
        metadata=dict(
            name="FormOfRefund",
            type="Attribute",
            help="How the refund will be issued. Values will be MCO or FormOfPayment",
        )
    )
    refund: str = field(
        default=None,
        metadata=dict(
            name="Refund",
            type="Attribute",
            help="Total refund amount.",
        )
    )

    @dataclass
    class TotalPenaltyTaxInfo:
        penalty_tax_info: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="PenaltyTaxInfo",
                type="Element",
                help=None,
                min_occurs=0,
                max_occurs=999
            )
        )
        total_penalty_tax: str = field(
            default=None,
            metadata=dict(
                name="TotalPenaltyTax",
                type="Attribute",
                help=None,
            )
        )

    @dataclass
    class TicketFeeInfo:
        base: str = field(
            default=None,
            metadata=dict(
                name="Base",
                type="Attribute",
                help=None,
            )
        )
        tax: str = field(
            default=None,
            metadata=dict(
                name="Tax",
                type="Attribute",
                help=None,
            )
        )
        total: str = field(
            default=None,
            metadata=dict(
                name="Total",
                type="Attribute",
                help=None,
            )
        )


@dataclass
class AirSearchParameters:
    """
    Search Parameters
    """

    no_advance_purchase: str = field(
        default=None,
        metadata=dict(
            name="NoAdvancePurchase",
            type="Attribute",
            help=None,
        )
    )
    refundable_fares: str = field(
        default=None,
        metadata=dict(
            name="RefundableFares",
            type="Attribute",
            help=None,
        )
    )
    non_penalty_fares: str = field(
        default=None,
        metadata=dict(
            name="NonPenaltyFares",
            type="Attribute",
            help=None,
        )
    )
    un_restricted_fares: str = field(
        default=None,
        metadata=dict(
            name="UnRestrictedFares",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class Airport(Location):
    """
    Airport identifier
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True,
            length=3,
            white_space="collapse"
        )
    )


@dataclass
class Apiprovider:
    transaction_type: str = field(
        default=None,
        metadata=dict(
            name="TransactionType",
            type="Element",
            help=None,
        )
    )
    available_pseudo_city_code: List["Apiprovider.str"] = field(
        default_factory=list,
        metadata=dict(
            name="AvailablePseudoCityCode",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="The Provider Code of the host",
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
            help="The Supplier Code of the host",
            min_length=1.0,
            max_length=5.0
        )
    )
    iatacode: str = field(
        default=None,
        metadata=dict(
            name="IATACode",
            type="Attribute",
            help="Agency IATA or ARC code, used as an ID with airlines.",
            max_length=8.0
        )
    )

    @dataclass
    class AvailablePseudoCityCode:
        pseudo_city_code: str = field(
            default=None,
            metadata=dict(
                name="PseudoCityCode",
                type="Attribute",
                help="The PseudoCityCode used to connect to the host.",
                min_length=2.0,
                max_length=10.0
            )
        )


@dataclass
class Arcpayment:
    """
    ARC form of payment.ACH Only
    """

    arcidentifier: str = field(
        default=None,
        metadata=dict(
            name="ARCIdentifier",
            type="Attribute",
            help="Value of the ARC Direct Bill id",
            required=True,
            max_length=128.0
        )
    )
    arcpassword: str = field(
        default=None,
        metadata=dict(
            name="ARCPassword",
            type="Attribute",
            help="Value of the ARC Direct Bill id password",
            max_length=128.0
        )
    )


@dataclass
class AttrAgentOverride:
    agent_override: str = field(
        default=None,
        metadata=dict(
            name="AgentOverride",
            type="Attribute",
            help="AgentSine value that was used during PNR creation or End Transact.",
            min_length=1.0,
            max_length=32.0
        )
    )


@dataclass
class AttrAmountPercent:
    """
    Amount or Percentage
    """

    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="The monetary amount.",
        )
    )
    percentage: str = field(
        default=None,
        metadata=dict(
            name="Percentage",
            type="Attribute",
            help="The percentage.",
            pattern="([0-9]{1,2}|100)\.[0-9]{1,2}"
        )
    )


@dataclass
class AttrAppliedProfilePaymentInfo:
    """
    ProfileID and Key are required in order to reference a payment method from a profile.
    """

    profile_id: str = field(
        default=None,
        metadata=dict(
            name="ProfileID",
            type="Attribute",
            help="The unique ID of the profile that contains the payment details to use.",
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="The Key assigned to the payment details value from the specified profile.",
        )
    )


@dataclass
class AttrBookingTravelerGrp:
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    traveler_type: str = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            help="Defines the type of traveler used for booking which could be a non-defining type (Companion, Web-fare, etc), or a standard type (Adult, Child, etc).",
            min_length=3.0,
            max_length=5.0
        )
    )
    age: str = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute",
            help="BookingTraveler age",
        )
    )
    vip: str = field(
        default="false",
        metadata=dict(
            name="VIP",
            type="Attribute",
            help="When set to True indicates that the Booking Traveler is a VIP based on agency/customer criteria",
        )
    )
    dob: str = field(
        default=None,
        metadata=dict(
            name="DOB",
            type="Attribute",
            help="Traveler Date of Birth",
        )
    )
    gender: str = field(
        default=None,
        metadata=dict(
            name="Gender",
            type="Attribute",
            help="The BookingTraveler gender type",
            min_length=1.0,
            max_length=2.0
        )
    )
    nationality: str = field(
        default=None,
        metadata=dict(
            name="Nationality",
            type="Attribute",
            help="Specify ISO country code for nationality of the Booking Traveler",
            length=2
        )
    )


@dataclass
class AttrBookingTravelerName:
    """
    Details of Booking Traveler Name
    """

    prefix: str = field(
        default=None,
        metadata=dict(
            name="Prefix",
            type="Attribute",
            help="Name prefix.",
            min_length=1.0,
            max_length=20.0
        )
    )
    first: str = field(
        default=None,
        metadata=dict(
            name="First",
            type="Attribute",
            help="First Name.",
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
            help="Midle name.",
            min_length=1.0,
            max_length=256.0
        )
    )
    last: str = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            help="Last Name.",
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
            help="Name suffix.",
            min_length=1.0,
            max_length=256.0
        )
    )


@dataclass
class AttrCommissionRemark:
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="The monetary amount of the commission.",
        )
    )
    percentage: str = field(
        default=None,
        metadata=dict(
            name="Percentage",
            type="Attribute",
            help="The percent of the commission.",
            pattern="([0-9]{1,2}|100)\.[0-9]{1,2}"
        )
    )
    commission_cap: str = field(
        default=None,
        metadata=dict(
            name="CommissionCap",
            type="Attribute",
            help="Commission cap for the Airline.",
        )
    )


@dataclass
class AttrDocument:
    """
    Containing all document information
    """

    document_number: str = field(
        default=None,
        metadata=dict(
            name="DocumentNumber",
            type="Attribute",
            help="Identifies the document number to be voided.",
            min_length=1.0,
            max_length=13.0
        )
    )
    document_type: str = field(
        default=None,
        metadata=dict(
            name="DocumentType",
            type="Attribute",
            help="Identifies the document type to be voided, Document Type can have four values like Service Fee, Paper Ticket , MCO and E-Ticket.",
        )
    )


@dataclass
class AttrDow:
    """
    Basic attributes used to describe day of week
    """

    mon: str = field(
        default=None,
        metadata=dict(
            name="Mon",
            type="Attribute",
            help=None,
        )
    )
    tue: str = field(
        default=None,
        metadata=dict(
            name="Tue",
            type="Attribute",
            help=None,
        )
    )
    wed: str = field(
        default=None,
        metadata=dict(
            name="Wed",
            type="Attribute",
            help=None,
        )
    )
    thu: str = field(
        default=None,
        metadata=dict(
            name="Thu",
            type="Attribute",
            help=None,
        )
    )
    fri: str = field(
        default=None,
        metadata=dict(
            name="Fri",
            type="Attribute",
            help=None,
        )
    )
    sat: str = field(
        default=None,
        metadata=dict(
            name="Sat",
            type="Attribute",
            help=None,
        )
    )
    sun: str = field(
        default=None,
        metadata=dict(
            name="Sun",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AttrElementKeyResults:
    """
    ElementStatus and KeyOverride to show the changes in the element keys
    """

    el_stat: str = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute",
            help="This attribute is used to show the action results of an element. Possible values are 'A' (when elements have been added to the UR) and 'M' (when existing elements have been modified). Response only.",
        )
    )
    key_override: str = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute",
            help="If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.",
        )
    )


@dataclass
class AttrFlexShopping:
    tier: str = field(
        default=None,
        metadata=dict(
            name="Tier",
            type="Attribute",
            help="Indicate the Tier Level",
        )
    )
    days_enabled: str = field(
        default=None,
        metadata=dict(
            name="DaysEnabled",
            type="Attribute",
            help="Allow or prohibit Flexible Days (within a date range) shopping option",
        )
    )
    weekends_enabled: str = field(
        default=None,
        metadata=dict(
            name="WeekendsEnabled",
            type="Attribute",
            help="Allow or prohibit Flexible Weekends shopping option",
        )
    )
    airports_enabled: str = field(
        default=None,
        metadata=dict(
            name="AirportsEnabled",
            type="Attribute",
            help="Allow or prohibit Flexible Airport (choice of Origin and Destination airports) shopping option",
        )
    )
    odenabled: str = field(
        default=None,
        metadata=dict(
            name="ODEnabled",
            type="Attribute",
            help="Allow or prohibit Flexible Origin and Destination (choice of airports within a radius) shopping option",
        )
    )


@dataclass
class AttrFlightTimes:
    """
    Basic attributes used to describe flight time information
    """

    flight_time: str = field(
        default=None,
        metadata=dict(
            name="FlightTime",
            type="Attribute",
            help="Time spent (minutes) traveling in flight, including airport taxi time.",
        )
    )
    travel_time: str = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute",
            help="Total time spent (minutes) traveling including flight time and ground time.",
        )
    )
    distance: str = field(
        default=None,
        metadata=dict(
            name="Distance",
            type="Attribute",
            help="The distance traveled. Units are specified in the parent response element.",
        )
    )


@dataclass
class AttrLocatorInfo:
    """
    Holds the Universal Record and Provider Reservation Locators for an individual product.
    """

    universal_record_locator_code: str = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            help="Contains the Locator Code of the Universal Record that houses this reservation.",
            min_length=5.0,
            max_length=8.0
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Contains the Provider Code of the provider that houses this reservation.",
            min_length=2.0,
            max_length=5.0
        )
    )
    provider_locator_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            help="Contains the Locator Code of the Provider Reservation that houses this reservation.",
            max_length=15.0
        )
    )


@dataclass
class AttrLoyalty:
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help="The code used to identify the Loyalty supplier, e.g. AA, ZE, MC",
            required=True,
            length=2
        )
    )
    alliance_level: str = field(
        default=None,
        metadata=dict(
            name="AllianceLevel",
            type="Attribute",
            help=None,
        )
    )
    membership_program: str = field(
        default=None,
        metadata=dict(
            name="MembershipProgram",
            type="Attribute",
            help="Loyalty Program membership Id of the traveler specific to Amtrak(2V) Guest Rewards",
            min_length=1.0,
            max_length=32.0
        )
    )


@dataclass
class AttrName:
    """
    Basic attributes used to describe a name
    """

    prefix: str = field(
        default=None,
        metadata=dict(
            name="Prefix",
            type="Attribute",
            help=None,
        )
    )
    first: str = field(
        default=None,
        metadata=dict(
            name="First",
            type="Attribute",
            help=None,
        )
    )
    middle: str = field(
        default=None,
        metadata=dict(
            name="Middle",
            type="Attribute",
            help=None,
        )
    )
    last: str = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            help=None,
            required=True,
            min_length=1.0
        )
    )
    suffix: str = field(
        default=None,
        metadata=dict(
            name="Suffix",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AttrOrigDestDepatureInfo:
    """
    Basic attributes used to describe an origin destination pair
    """

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
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            help="The date and time at which this entity departs. Date and time are represented as Airport Local Time at the place of departure. The correct time zone offset is also included.",
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute",
            help="The date and time at which this entity arrives at the destination. Date and time are represented as Airport Local Time at the place of arrival. The correct time zone offset is also included.",
        )
    )


@dataclass
class AttrOrigDestInfo:
    """
    Basic attributes used to describe an origin destination pair
    """

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
class AttrPolicyMarking:
    in_policy: str = field(
        default=None,
        metadata=dict(
            name="InPolicy",
            type="Attribute",
            help="This attribute will be used to indicate if a fare or rate has been determined to be ‘in policy’ based on the associated policy settings.",
        )
    )
    policy_code: str = field(
        default=None,
        metadata=dict(
            name="PolicyCode",
            type="Attribute",
            help="This attribute is used to provide a code that can be used to determine why an item was determined to be ‘out of policy’.",
            min_inclusive=1.0,
            max_inclusive=9999.0
        )
    )
    preferred_option: str = field(
        default=None,
        metadata=dict(
            name="PreferredOption",
            type="Attribute",
            help="This attribute is used to indicate if the vendors responsible for the fare or rate being returned have been determined to be ‘preferred’ based on the associated policy settings.",
        )
    )


@dataclass
class AttrPrices:
    """
    Basic monetary value for Air pricing structures
    """

    total_price: str = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute",
            help="The total price for this entity including base price and all taxes.",
        )
    )
    base_price: str = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute",
            help="Represents the base price for this entity. This does not include any taxes or surcharges.",
        )
    )
    approximate_total_price: str = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute",
            help="The Converted total price in Default Currency for this entity including base price and all taxes.",
        )
    )
    approximate_base_price: str = field(
        default=None,
        metadata=dict(
            name="ApproximateBasePrice",
            type="Attribute",
            help="The Converted base price in Default Currency for this entity. This does not include any taxes or surcharges.",
        )
    )
    equivalent_base_price: str = field(
        default=None,
        metadata=dict(
            name="EquivalentBasePrice",
            type="Attribute",
            help="Represents the base price in the related currency for this entity. This does not include any taxes or surcharges.",
        )
    )
    taxes: str = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute",
            help="The aggregated amount of all the taxes that are associated with this entity. See the associated TaxInfo array for a breakdown of the individual taxes.",
        )
    )
    fees: str = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Attribute",
            help="The aggregated amount of all the fees that are associated with this entity. See the associated FeeInfo array for a breakdown of the individual fees.",
        )
    )
    services: str = field(
        default=None,
        metadata=dict(
            name="Services",
            type="Attribute",
            help="The total cost for all optional services.",
        )
    )
    approximate_taxes: str = field(
        default=None,
        metadata=dict(
            name="ApproximateTaxes",
            type="Attribute",
            help="The Converted tax amount in Default Currency.",
        )
    )
    approximate_fees: str = field(
        default=None,
        metadata=dict(
            name="ApproximateFees",
            type="Attribute",
            help="The Converted fee amount in Default Currency.",
        )
    )


@dataclass
class AttrProviderSupplier:
    """
    Attributes used to uniquely describe a content source
    """

    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
            min_length=2.0,
            max_length=5.0
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help=None,
            min_length=1.0,
            max_length=5.0
        )
    )


@dataclass
class AttrQueueInfo:
    """
    Attributes related to queue information
    """

    queue: str = field(
        default=None,
        metadata=dict(
            name="Queue",
            type="Attribute",
            help="Queue Number . Possible values are 01, AA , A1 etc.",
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="If using for Sabre is mandatory and is Prefatory Instruction Code value of 0-999.",
        )
    )
    date_range: str = field(
        default=None,
        metadata=dict(
            name="DateRange",
            type="Attribute",
            help="Date range number where the PNR should be queued. Possible values are 1,2,1-4 etc.",
        )
    )


@dataclass
class AttrReqRspInfo:
    """
    Basic information on all request response pairs.
    """

    transaction_id: str = field(
        default=None,
        metadata=dict(
            name="TransactionId",
            type="Attribute",
            help="Unique identifier for this atomic transaction. Use is optional.",
        )
    )


@dataclass
class AttrTaxDetail:
    """
    Holds fare quote tax information.
    """

    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
            required=True
        )
    )
    origin_airport: str = field(
        default=None,
        metadata=dict(
            name="OriginAirport",
            type="Attribute",
            help=None,
            length=3
        )
    )
    destination_airport: str = field(
        default=None,
        metadata=dict(
            name="DestinationAirport",
            type="Attribute",
            help=None,
            length=3
        )
    )
    country_code: str = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Attribute",
            help=None,
        )
    )
    fare_info_ref: str = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AttrTicketNumberStatus:
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help=None,
            required=True
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help=None,
            required=True,
            length=1
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class Auxdata:
    entry: List["Auxdata.str"] = field(
        default_factory=list,
        metadata=dict(
            name="Entry",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )

    @dataclass
    class Entry:
        reason: str = field(
            default=None,
            metadata=dict(
                name="Reason",
                type="Element",
                help=None,
                required=True
            )
        )
        description: str = field(
            default=None,
            metadata=dict(
                name="Description",
                type="Element",
                help=None,
                required=True
            )
        )


@dataclass
class BaseAsyncProviderSpecificResponse:
    """
    Identifies pending responses from a specific provider using MoreResults attribute
    """

    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Provider code of a specific host",
            required=True,
            min_length=2.0,
            max_length=5.0
        )
    )
    more_results: str = field(
        default=None,
        metadata=dict(
            name="MoreResults",
            type="Attribute",
            help="Identifies whether more results are available for specific host or not.",
            required=True
        )
    )


@dataclass
class BaseReservation:
    accounting_remark: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AccountingRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    general_remark: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="GeneralRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    restriction: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Restriction",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    passive_info: str = field(
        default=None,
        metadata=dict(
            name="PassiveInfo",
            type="Element",
            help=None,
        )
    )
    locator_code: str = field(
        default=None,
        metadata=dict(
            name="LocatorCode",
            type="Attribute",
            help="The unique identifier for this reservation. If this is this View Only UR LocatorCode is '999999'.",
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
            help="The date and time that this reservation was created.",
            required=True
        )
    )
    modified_date: str = field(
        default=None,
        metadata=dict(
            name="ModifiedDate",
            type="Attribute",
            help="The date and time that this reservation was last modified for any reason.",
            required=True
        )
    )
    customer_number: str = field(
        default=None,
        metadata=dict(
            name="CustomerNumber",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class BillingPointOfSaleInfo:
    """
    Point of Sale information for Billing
    """

    origin_application: str = field(
        default=None,
        metadata=dict(
            name="OriginApplication",
            type="Attribute",
            help="Name of the Point of Sale application which initiated the Request.This information will be provided as part of the provisioning of the user.",
            required=True
        )
    )
    cidbnumber: str = field(
        default=None,
        metadata=dict(
            name="CIDBNumber",
            type="Attribute",
            help="A 10 Digit customer number generated by CIDB system.",
            pattern="\d{10}"
        )
    )


@dataclass
class BookingDates:
    """
    Check in and Check out Date information
    """

    check_in_date: str = field(
        default=None,
        metadata=dict(
            name="CheckInDate",
            type="Attribute",
            help=None,
            pattern="[^:Z].*"
        )
    )
    check_out_date: str = field(
        default=None,
        metadata=dict(
            name="CheckOutDate",
            type="Attribute",
            help=None,
            pattern="[^:Z].*"
        )
    )


@dataclass
class BookingSource:
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="Alternate booking source code or number.",
            required=True,
            min_length=1.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Type of booking source sent in the Code attribute. Possible values are “PseudoCityCode”,” ArcNumber”,” IataNumber”, “CustomerId” and “BookingSourceOverrride”. “BookingSourceOverrride” is only applicable in VehicleCreateReservationReq. 1P/1J.",
            required=True
        )
    )


@dataclass
class BookingTravelerInfo:
    """
    Container that will allow modifying Universal record data that is not product specific.
    """

    booking_traveler_name: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerName",
            type="Element",
            help=None,
        )
    )
    name_remark: str = field(
        default=None,
        metadata=dict(
            name="NameRemark",
            type="Element",
            help=None,
        )
    )
    dob: str = field(
        default=None,
        metadata=dict(
            name="DOB",
            type="Element",
            help="Traveler Date of Birth",
        )
    )
    travel_info: str = field(
        default=None,
        metadata=dict(
            name="TravelInfo",
            type="Element",
            help=None,
        )
    )
    email: str = field(
        default=None,
        metadata=dict(
            name="Email",
            type="Element",
            help=None,
        )
    )
    phone_number: str = field(
        default=None,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            help=None,
        )
    )
    address: str = field(
        default=None,
        metadata=dict(
            name="Address",
            type="Element",
            help=None,
        )
    )
    emergency_info: str = field(
        default=None,
        metadata=dict(
            name="EmergencyInfo",
            type="Element",
            help=None,
        )
    )
    delivery_info: str = field(
        default=None,
        metadata=dict(
            name="DeliveryInfo",
            type="Element",
            help=None,
        )
    )
    age: str = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Element",
            help=None,
        )
    )
    customized_name_data: str = field(
        default=None,
        metadata=dict(
            name="CustomizedNameData",
            type="Element",
            help=None,
        )
    )
    applied_profile: str = field(
        default=None,
        metadata=dict(
            name="AppliedProfile",
            type="Element",
            help=None,
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    traveler_type: str = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            help=None,
            min_length=3.0,
            max_length=5.0
        )
    )
    gender: str = field(
        default=None,
        metadata=dict(
            name="Gender",
            type="Attribute",
            help=None,
            min_length=1.0,
            max_length=2.0
        )
    )


@dataclass
class BookingTravelerInformation:
    """
    Booking Traveler information tied to invoice
    """

    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            help=None,
            required=True
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="A reference to a passenger related to a ticket.",
        )
    )


@dataclass
class BookingTravelerRef:
    """
    Reference Element for Booking Traveler and Loyalty cards
    """

    loyalty_card_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyCardRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    drivers_license_ref: str = field(
        default=None,
        metadata=dict(
            name="DriversLicenseRef",
            type="Element",
            help=None,
        )
    )
    discount_card_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="DiscountCardRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=9
        )
    )
    payment_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PaymentRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=3
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class Bsppayment:
    """
    BSP form of payment.ACH Only
    """

    bspidentifier: str = field(
        default=None,
        metadata=dict(
            name="BSPIdentifier",
            type="Attribute",
            help="Value of the BSP Direct Bill id",
            required=True,
            max_length=128.0
        )
    )
    bsppassword: str = field(
        default=None,
        metadata=dict(
            name="BSPPassword",
            type="Attribute",
            help="Value of the BSP Direct Bill id password",
            max_length=128.0
        )
    )


@dataclass
class CabinClass:
    """
    Requests cabin class (First, Business and Economy, etc.) as supported by the provider or supplier.
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class CardRestriction:
    required_field: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="RequiredField",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="2 letter Credit/Debit Card merchant type",
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
            help="Card merchant description",
            required=True
        )
    )


@dataclass
class Carrier:
    """
    Carrier identifier
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True,
            length=2
        )
    )


@dataclass
class Certificate:
    """
    Certificate Form of Payment
    """

    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="The Certificate number",
            required=True
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="The monetary value of the certificate.",
        )
    )
    discount_amount: str = field(
        default=None,
        metadata=dict(
            name="DiscountAmount",
            type="Attribute",
            help="The monetary discount amount of this certificate.",
        )
    )
    discount_percentage: str = field(
        default=None,
        metadata=dict(
            name="DiscountPercentage",
            type="Attribute",
            help="The percentage discount value of this certificate.",
        )
    )
    not_valid_before: str = field(
        default=None,
        metadata=dict(
            name="NotValidBefore",
            type="Attribute",
            help="The date that this certificate becomes valid.",
        )
    )
    not_valid_after: str = field(
        default=None,
        metadata=dict(
            name="NotValidAfter",
            type="Attribute",
            help="The date that this certificate expires.",
        )
    )


@dataclass
class Characteristic:
    """
    Identifies the characteristics of the seat with seat type, value and description.
    """

    seat_type: str = field(
        default=None,
        metadata=dict(
            name="SeatType",
            type="Attribute",
            help="Indicates codeset of values such as Seat Type like Place,Position, Smoking Choice, Place Arrangement, Place Direction, Compartment.",
            min_length=0.0,
            max_length=255.0
        )
    )
    seat_description: str = field(
        default=None,
        metadata=dict(
            name="SeatDescription",
            type="Attribute",
            help="Description of the seat type.",
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
            min_length=0.0,
            max_length=255.0
        )
    )
    seat_value_description: str = field(
        default=None,
        metadata=dict(
            name="SeatValueDescription",
            type="Attribute",
            help="Description of the seat value.",
            min_length=0.0,
            max_length=255.0
        )
    )


@dataclass
class Check:
    """
    Check Form of Payment
    """

    micrnumber: str = field(
        default=None,
        metadata=dict(
            name="MICRNumber",
            type="Attribute",
            help="Magnetic Ink Character Reader Number of check.",
            max_length=29.0
        )
    )
    routing_number: str = field(
        default=None,
        metadata=dict(
            name="RoutingNumber",
            type="Attribute",
            help="The bank routing number of the check.",
        )
    )
    account_number: str = field(
        default=None,
        metadata=dict(
            name="AccountNumber",
            type="Attribute",
            help="The account number of the check",
        )
    )
    check_number: str = field(
        default=None,
        metadata=dict(
            name="CheckNumber",
            type="Attribute",
            help="The sequential check number of the check.",
        )
    )


@dataclass
class City(Location):
    """
    City identifier
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True,
            length=3,
            white_space="collapse"
        )
    )


@dataclass
class CityOrAirport(Location):
    """
    This element can be used when it is not known whether the value is an airport or a city code.
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The airport or city IATA code.",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    prefer_city: str = field(
        default="false",
        metadata=dict(
            name="PreferCity",
            type="Attribute",
            help="Indicates that the search should prefer city results over airport results.",
        )
    )


@dataclass
class Commission:
    """
    Identifies the agency commission
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    level: str = field(
        default=None,
        metadata=dict(
            name="Level",
            type="Attribute",
            help="The commission percentage level.",
            required=True
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="The commission type.",
            required=True
        )
    )
    modifier: str = field(
        default=None,
        metadata=dict(
            name="Modifier",
            type="Attribute",
            help="Optional commission modifier.",
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="The monetary amount of the commission.",
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help="Contains alphanumeric or alpha characters intended as 1G Value Code as applicable by BSP of client.",
            min_length=0.0,
            max_length=15.0
        )
    )
    percentage: str = field(
        default=None,
        metadata=dict(
            name="Percentage",
            type="Attribute",
            help="The percent of the commission.",
            pattern="([0-9]{1,2}|100)\.[0-9]{1,2}"
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="A reference to a passenger.",
        )
    )
    commission_override: str = field(
        default="false",
        metadata=dict(
            name="CommissionOverride",
            type="Attribute",
            help="This is enabled to override CAT-35 commission error during air ticketing. PROVIDER SUPPORTED:Worldspan and JAL",
        )
    )


@dataclass
class ContinuityCheckOverride:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            white_space="collapse"
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Will use key to map continuity remark to a particular segment",
        )
    )


@dataclass
class CoordinateLocation(Location):
    """
    Specific lat/long location, usually associated with a Distance
    """

    latitude: str = field(
        default=None,
        metadata=dict(
            name="latitude",
            type="Attribute",
            help=None,
            required=True
        )
    )
    longitude: str = field(
        default=None,
        metadata=dict(
            name="longitude",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class CorporateDiscountId(str):
    """
    These are zero or more negotiated rate codes
    """

    negotiated_rate_code: str = field(
        default=None,
        metadata=dict(
            name="NegotiatedRateCode",
            type="Attribute",
            help="When set to true, the data in the CorporateDiscountID is a negotiated rate code. Otherwise, this data is a Corporate Discount ID rate.",
        )
    )


@dataclass
class Credentials:
    """
    Container to send login id and password on each request
    """

    user_id: str = field(
        default=None,
        metadata=dict(
            name="UserId",
            type="Attribute",
            help="The UserID associated with the entity using this request withing this BranchCode.",
            required=True,
            max_length=36.0
        )
    )


@dataclass
class CreditCardAuth:
    """
    The result of a Credit Auth Request. Will contain all the authorization info and result codes.
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    payment_ref: str = field(
        default=None,
        metadata=dict(
            name="PaymentRef",
            type="Attribute",
            help=None,
        )
    )
    trans_id: str = field(
        default=None,
        metadata=dict(
            name="TransId",
            type="Attribute",
            help="The transaction id from the credit processing system",
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help=None,
            min_length=13.0,
            max_length=128.0
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="The amount that was authorized.",
            required=True
        )
    )
    auth_code: str = field(
        default=None,
        metadata=dict(
            name="AuthCode",
            type="Attribute",
            help="The authorization code to confirm card acceptance",
        )
    )
    auth_result_code: str = field(
        default=None,
        metadata=dict(
            name="AuthResultCode",
            type="Attribute",
            help="The result code of the authorization command.",
            required=True
        )
    )
    avsresult_code: str = field(
        default=None,
        metadata=dict(
            name="AVSResultCode",
            type="Attribute",
            help="The address verification result code (if AVS was requested)",
        )
    )
    message: str = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute",
            help="The message explains the result of the authorization command.",
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help=None,
        )
    )
    form_of_payment_ref: str = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class CustomizedNameData(str):
    """
    Customized Name Data is used to print customized name on the different documents.
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class DirectPayment:
    """
    Direct Payment Form of Payments
    """

    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class DiscountCardRef:
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
class Distance:
    """
    Container to encapsulate the a distance value with its unit of measure.
    """

    units: str = field(
        default="MI",
        metadata=dict(
            name="Units",
            type="Attribute",
            help=None,
            length=2
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True
        )
    )
    direction: str = field(
        default=None,
        metadata=dict(
            name="Direction",
            type="Attribute",
            help="Directions: S, N, E, W, SE, NW, ...",
            max_length=2.0
        )
    )


@dataclass
class DriversLicenseRef:
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
class EmailNotification:
    """
    Send Email Notification to the emails specified in Booking Traveler. Supported Provider : 1G/1V
    """

    email_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="EmailRef",
            type="Element",
            help="Reference to Booking Traveler Email.",
            min_occurs=0,
            max_occurs=999
        )
    )
    recipients: str = field(
        default=None,
        metadata=dict(
            name="Recipients",
            type="Attribute",
            help="Indicates the recipients of the mail addresses for which the user requires the system to send the itinerary.List of Possible Values: All = Send Email to All addresses Default = Send Email to Primary Booking Traveler Specific = Send Email to specific address Referred in EmailRef.",
            required=True
        )
    )


@dataclass
class Endorsement:
    """
    Restrictions or instructions about the fare or ticket
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True,
            min_length=1.0,
            max_length=256.0
        )
    )


@dataclass
class EnettVan:
    """
    Container for all eNett Van information.
    """

    min_percentage: str = field(
        default=None,
        metadata=dict(
            name="MinPercentage",
            type="Attribute",
            help="The minimum percentage that will be applied on the Total price and sent to enett,which will denote the minimum authorized amount approved by eNett.uApi will default this to zero for multi-use Van's.",
            min_inclusive=0.0,
            max_inclusive=100.0
        )
    )
    max_percentage: str = field(
        default=None,
        metadata=dict(
            name="MaxPercentage",
            type="Attribute",
            help="The maximum percentage that will be applied on the Total price and sent to enett, which will denote the maximum authorized amount as approved by eNett. This value will be ignored and not used for Multi-Use VAN’s.",
            min_inclusive=0.0,
            max_inclusive=100.0
        )
    )
    expiry_days: str = field(
        default=None,
        metadata=dict(
            name="ExpiryDays",
            type="Attribute",
            help="The number of days from the VAN generation date that the VAN will be active for, after which the VAN cannot be used.",
            min_inclusive="P1D",
            max_inclusive="P366D"
        )
    )
    multi_use: str = field(
        default="true",
        metadata=dict(
            name="MultiUse",
            type="Attribute",
            help="Acceptable values are true or false. If set to true it will denote that the VAN being requested is multi-use else it will indicate a single -use VAN.A Single use VAN can only be debited once while the multiple use VAN's can be debited multiple times subjected to the maximum value it has been authorized for. The default value will be TRUE to indicate a multi-use VAN is being issued.",
        )
    )


@dataclass
class ExchangedCoupon:
    """
    The coupon numbers that were used in the exchange process to create the MCO.
    """

    ticket_number: str = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            help="The ticket number for which the exchange coupons are present.",
            required=True,
            length=13
        )
    )
    coupon_number: str = field(
        default=None,
        metadata=dict(
            name="CouponNumber",
            type="Attribute",
            help="Coupon numbers that were exchanged specific to this ticket",
        )
    )


@dataclass
class FileFinishingInfo:
    """
    Misc Data required for File Finishing. This data is transient and not saved in database.
    """

    shop_information: str = field(
        default=None,
        metadata=dict(
            name="ShopInformation",
            type="Element",
            help=None,
        )
    )
    policy_information: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PolicyInformation",
            type="Element",
            help="Policy Information required for File Finishing. Would repeat per Policy Type",
            min_occurs=0,
            max_occurs=999
        )
    )
    account_information: str = field(
        default=None,
        metadata=dict(
            name="AccountInformation",
            type="Element",
            help=None,
        )
    )
    agency_information: str = field(
        default=None,
        metadata=dict(
            name="AgencyInformation",
            type="Element",
            help=None,
        )
    )
    traveler_information: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TravelerInformation",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    custom_profile_information: str = field(
        default=None,
        metadata=dict(
            name="CustomProfileInformation",
            type="Element",
            help=None,
        )
    )


@dataclass
class FormOfPaymentRef:
    """
    A reference to a Form of Payment in the existing UR
    """

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
class FormattedTextTextType(str):
    """
    Provides text and indicates whether it is formatted or not.
    """

    formatted: str = field(
        default=None,
        metadata=dict(
            name="Formatted",
            type="Attribute",
            help="Textual information, which may be formatted as a line of information, or unformatted, as a paragraph of text.",
        )
    )
    text_format: str = field(
        default=None,
        metadata=dict(
            name="TextFormat",
            type="Attribute",
            help="Indicates the format of text used in the description e.g. unformatted or html.",
        )
    )


@dataclass
class GuaranteeType:
    """
    A type of guarantee i.e
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            max_length=250.0
        )
    )


@dataclass
class HostToken(str):
    """
    one or more hosts
    """

    host: str = field(
        default=None,
        metadata=dict(
            name="Host",
            type="Attribute",
            help="The host associated with this token",
            min_length=2.0,
            max_length=5.0
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Unique identifier for this token - use this key when a single HostToken is shared by multiple elements.",
        )
    )


@dataclass
class HostTokenList:
    """
    The shared object list of Host Tokens
    """

    host_token: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class IncludedInBase:
    """
    Shows the taxes and fees included in the base fare. (ACH only)
    """

    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="this attribute shows the amount included in the base fare for the specific fee or tax",
        )
    )


@dataclass
class IndustryStandardSsr:
    """
    Indicates Carrier Supports this industry standard.
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="This code indicates which Standard of SSR's they support. Sucha as the 'AIRIMP' standard identified by 'IATA.org'",
        )
    )


@dataclass
class InvoiceData:
    """
    List of invoices only for 1G/1V
    """

    booking_traveler_information: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerInformation",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=9
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    invoice_number: str = field(
        default=None,
        metadata=dict(
            name="InvoiceNumber",
            type="Attribute",
            help="Invoice number",
            required=True
        )
    )
    issue_date: str = field(
        default=None,
        metadata=dict(
            name="IssueDate",
            type="Attribute",
            help="Invoice issue date",
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
            required=True
        )
    )


@dataclass
class KeyMapping:
    """
    Element for which mapping key sent in the request is different from the mapping key comes in the response.
    """

    element_name: str = field(
        default=None,
        metadata=dict(
            name="ElementName",
            type="Attribute",
            help="Name of the element.",
            required=True
        )
    )
    original_key: str = field(
        default=None,
        metadata=dict(
            name="OriginalKey",
            type="Attribute",
            help="The mapping key which is sent in the request.",
            required=True
        )
    )
    new_key: str = field(
        default=None,
        metadata=dict(
            name="NewKey",
            type="Attribute",
            help="The mapping key that comes in the response.",
            required=True
        )
    )


@dataclass
class LanguageGroup:
    """
    Identifies language.
    """

    language: str = field(
        default=None,
        metadata=dict(
            name="Language",
            type="Attribute",
            help="Language identification.",
        )
    )


@dataclass
class LocatorCode:
    """
    A locator code that identifies a PNR or searches for one.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0
        )
    )


@dataclass
class LoyaltyCardRef:
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
class MarketingInformation:
    """
    Marketing text or Notices for Suppliers
    """

    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class McoexchangeInfo:
    """
    Information related to the exchange tickets available for the MCO
    """

    form_of_payment: str = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help=None,
        )
    )
    exchanged_coupon: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangedCoupon",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=4
        )
    )
    original_ticket_number: str = field(
        default=None,
        metadata=dict(
            name="OriginalTicketNumber",
            type="Attribute",
            help="Airline form and serial number of the original ticket issued.",
            length=13
        )
    )
    original_city_code: str = field(
        default=None,
        metadata=dict(
            name="OriginalCityCode",
            type="Attribute",
            help="Location of honoring carrier or operator.",
            length=3
        )
    )
    original_ticket_date: str = field(
        default=None,
        metadata=dict(
            name="OriginalTicketDate",
            type="Attribute",
            help="Date that the Original ticket was issued.",
            pattern="[^:Z].*"
        )
    )
    iatacode: str = field(
        default=None,
        metadata=dict(
            name="IATACode",
            type="Attribute",
            help="IATA code of the issuing agency.",
            max_length=8.0
        )
    )


@dataclass
class Mcoinformation:
    passenger_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    mconumber: str = field(
        default=None,
        metadata=dict(
            name="MCONumber",
            type="Attribute",
            help="The unique MCO number",
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help="Current status of the MCO",
        )
    )
    mcotype: str = field(
        default=None,
        metadata=dict(
            name="MCOType",
            type="Attribute",
            help="The Type of MCO. Once of Agency Fee, Airline Service Fee, or Residual value from an Exchange.",
        )
    )


@dataclass
class Mcoremark(str):
    """
    Information related to fare construction, free form text etc. of the MCO
    """

    additional_rmk: str = field(
        default=None,
        metadata=dict(
            name="AdditionalRmk",
            type="Attribute",
            help="Indicates if the remark is additional remark or not.",
        )
    )


@dataclass
class MealRequest:
    """
    Special meal requests like Vegetarian
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help=None,
            required=True,
            length=4
        )
    )


@dataclass
class MediaItem:
    """
    Photos and other media urls for the property referenced above.
    """

    caption: str = field(
        default=None,
        metadata=dict(
            name="caption",
            type="Attribute",
            help=None,
        )
    )
    height: str = field(
        default=None,
        metadata=dict(
            name="height",
            type="Attribute",
            help=None,
        )
    )
    width: str = field(
        default=None,
        metadata=dict(
            name="width",
            type="Attribute",
            help=None,
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute",
            help=None,
        )
    )
    url: str = field(
        default=None,
        metadata=dict(
            name="url",
            type="Attribute",
            help=None,
        )
    )
    icon: str = field(
        default=None,
        metadata=dict(
            name="icon",
            type="Attribute",
            help=None,
        )
    )
    size_code: str = field(
        default=None,
        metadata=dict(
            name="sizeCode",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class MetaData:
    """
    Extra data to elaborate the parent element. This data is primarily informative and is not persisted.
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
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
            help=None,
            required=True,
            min_length=1.0,
            max_length=50.0
        )
    )


@dataclass
class MiscFormOfPayment:
    """
    Miscellaneous Form of Payments
    """

    credit_card_type: str = field(
        default=None,
        metadata=dict(
            name="CreditCardType",
            type="Attribute",
            help="The 2 letter credit/ debit card type or code which may not have been issued using the standard bank card types - i.e. an airline issued card",
            length=2
        )
    )
    credit_card_number: str = field(
        default=None,
        metadata=dict(
            name="CreditCardNumber",
            type="Attribute",
            help=None,
            min_length=13.0,
            max_length=128.0
        )
    )
    exp_date: str = field(
        default=None,
        metadata=dict(
            name="ExpDate",
            type="Attribute",
            help="The Expiration date of this card in YYYY-MM format.",
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            help="Any free form text which may be associated with the Miscellaneous Form of Payment. This text may be provider or GDS specific",
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="Allowable values are 'Text' 'Credit' 'CreditCard' 'FreeFormCreditCard' 'Invoice' 'NonRefundable' 'MultipleReceivables' 'Exchange' 'Cash'",
            required=True
        )
    )
    acceptance_override: str = field(
        default=None,
        metadata=dict(
            name="AcceptanceOverride",
            type="Attribute",
            help="Override airline restriction on the credit card.",
        )
    )


@dataclass
class ModificationRulesGroup:
    """
    Groups the rules for handling options when modifying an itinerary. One attribute group repreents the rules for a particular type of modification supported by the adapter for a single modification type.
    """

    modification: str = field(
        default=None,
        metadata=dict(
            name="Modification",
            type="Attribute",
            help="The modificaiton for which this rule group applies.",
            required=True
        )
    )
    automatically_applied_on_add: str = field(
        default="false",
        metadata=dict(
            name="AutomaticallyAppliedOnAdd",
            type="Attribute",
            help="Indicates if the option will be automatically added to new segments / passengers in the itinerary.",
        )
    )
    can_delete: str = field(
        default=None,
        metadata=dict(
            name="CanDelete",
            type="Attribute",
            help="Indicates if the option can be deleted from the itinerary without segment or passenger modifications",
        )
    )
    can_add: str = field(
        default=None,
        metadata=dict(
            name="CanAdd",
            type="Attribute",
            help="Indicates if the option can be added to the itinerary without segment or passenger modification",
        )
    )
    refundable: str = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute",
            help="Indicates if the price of the option is refundable.",
        )
    )
    provider_defined_modification_type: str = field(
        default=None,
        metadata=dict(
            name="ProviderDefinedModificationType",
            type="Attribute",
            help="Indicates the actual provider defined modification type which is mapped to Other",
        )
    )


@dataclass
class Name:
    """
    Complete name fields
    """

    prefix: str = field(
        default=None,
        metadata=dict(
            name="Prefix",
            type="Attribute",
            help="Name prefix. Size can be up to 20 characters",
            min_length=1.0,
            max_length=20.0
        )
    )
    first: str = field(
        default=None,
        metadata=dict(
            name="First",
            type="Attribute",
            help="First Name. Size can be up to 256 characters",
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
            help="Midle name. Size can be up to 256 characters",
            min_length=1.0,
            max_length=256.0
        )
    )
    last: str = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            help="Last Name. Size can be up to 256 characters",
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
            help="Name suffix. Size can be up to 256 characters",
            min_length=1.0,
            max_length=256.0
        )
    )
    traveler_profile_id: str = field(
        default=None,
        metadata=dict(
            name="TravelerProfileId",
            type="Attribute",
            help="Traveler Applied Profile ID.",
        )
    )


@dataclass
class NameOverride:
    """
    To be used if the name is different from booking travelers in the PNR
    """

    first: str = field(
        default=None,
        metadata=dict(
            name="First",
            type="Attribute",
            help="First Name.",
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
            help="Last Name.",
            required=True,
            min_length=1.0,
            max_length=256.0
        )
    )
    age: str = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute",
            help="Age.",
        )
    )


@dataclass
class NextResultReference:
    """
    Container to return/send additional retrieve/request additional search results
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            white_space="collapse"
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="The code of the Provider (e.g 1G,1S)",
            min_length=2.0,
            max_length=5.0
        )
    )


@dataclass
class OperatedBy:
    """
    This is the carrier code to support Cross Accrual
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            white_space="collapse"
        )
    )


@dataclass
class OptionalServiceApplicabilityLimitGroup:
    """
    Holds the limits on how many options of the particular type can be applied.
    """

    applicable_level: str = field(
        default=None,
        metadata=dict(
            name="ApplicableLevel",
            type="Attribute",
            help="Indicates the applicable level for the option",
            required=True
        )
    )
    provider_defined_applicable_levels: str = field(
        default=None,
        metadata=dict(
            name="ProviderDefinedApplicableLevels",
            type="Attribute",
            help="Indicates the actual provider defined ApplicableLevels which is mapped to Other",
        )
    )
    maximum_quantity: str = field(
        default=None,
        metadata=dict(
            name="MaximumQuantity",
            type="Attribute",
            help="The maximum quantity allowed for the type",
            required=True
        )
    )
    minimum_quantity: str = field(
        default=None,
        metadata=dict(
            name="MinimumQuantity",
            type="Attribute",
            help="Indicates the minimum number of the option that can be selected.",
        )
    )


@dataclass
class OptionalServicesTypeCodeGroup:
    """
    Holds the attributes to identify an option
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The ACH code for the OptionalService",
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
            help="The vendor specific code for the OptionalService",
            min_length=1.0,
            max_length=64.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="The type of the option",
        )
    )
    secondary_code: str = field(
        default=None,
        metadata=dict(
            name="SecondaryCode",
            type="Attribute",
            help="An additional code for the option required when the option identifies a larger type and specific codes are required by the vendor. For example, sports equipment may be a Code, and the secondary code could be SKIS or BIKE.",
            min_length=1.0,
            max_length=32.0
        )
    )
    selected_by_default: str = field(
        default=None,
        metadata=dict(
            name="SelectedByDefault",
            type="Attribute",
            help="Flag to indicate if the option has been selected by default",
        )
    )


@dataclass
class OtherGuaranteeInfo(str):
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="1) IATA/ARC Number 2) Agency Address 2) Deposit Taken 3) Others",
            required=True
        )
    )


@dataclass
class OverridePcc:
    """
    Used to emulate to another PCC or SID. Providers: 1G, 1V, 1P, 1J.
    """

    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="The code of the provider (e.g. 1G, 1S)",
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
            help="The PCC in the host system.",
            required=True,
            min_length=2.0,
            max_length=10.0
        )
    )


@dataclass
class OwnershipChange:
    """
    Element to change the ownership of the PNR in the UR. PROVIDER SUPPORTED: Worldspan and JAL.
    """

    owning_pcc: str = field(
        default=None,
        metadata=dict(
            name="OwningPCC",
            type="Attribute",
            help="New owning PCC of the PNR.",
            required=True
        )
    )


@dataclass
class PageAttributes:
    """
    Attributes to control pagination.
    """

    max_results: str = field(
        default=None,
        metadata=dict(
            name="MaxResults",
            type="Attribute",
            help=None,
            min_inclusive=1.0,
            max_inclusive=200.0
        )
    )
    start_from_result: str = field(
        default=None,
        metadata=dict(
            name="StartFromResult",
            type="Attribute",
            help=None,
            min_inclusive=1.0
        )
    )


@dataclass
class PassengerInfo:
    """
    Booking Traveler information tied to invoice
    """

    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            help=None,
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="A reference to a passenger related to a ticket.",
        )
    )
    passenger_type: str = field(
        default=None,
        metadata=dict(
            name="PassengerType",
            type="Attribute",
            help="Passenger Type Code.",
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class PassiveInfo:
    """
    Used by CreateReservationReq for passing in elements normally found post-booking
    """

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
    confirmation_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ConfirmationNumber",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    commission: str = field(
        default=None,
        metadata=dict(
            name="Commission",
            type="Element",
            help=None,
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
        )
    )
    provider_locator_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            help=None,
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help=None,
        )
    )
    supplier_locator_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierLocatorCode",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class PaymentAdvice:
    """
    Contains other form of payment for Cruise Reservations
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Other Payment Yype. Possible Values: AGC - Agency Check, AGG - Agency Guarantee, AWC - Award Check, CSH - Cash Equivalent, DBC - Denied Boarding Compensation, MCO - Miscellaneous Charge Order, TOO - Tour Order, TOV - Tour Voucher",
            required=True,
            max_length=3.0
        )
    )
    document_number: str = field(
        default=None,
        metadata=dict(
            name="DocumentNumber",
            type="Attribute",
            help="Payment Document Number Examples: 1234567890, R7777",
            required=True,
            max_length=22.0
        )
    )
    issue_date: str = field(
        default=None,
        metadata=dict(
            name="IssueDate",
            type="Attribute",
            help="Document Issuance date",
            required=True
        )
    )
    issue_city: str = field(
        default=None,
        metadata=dict(
            name="IssueCity",
            type="Attribute",
            help="City code of document issuance",
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
            help="Original form of payment Examples: CHECK 3500",
            max_length=19.0
        )
    )


@dataclass
class PaymentRef:
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
class PaymentRestriction:
    card_restriction: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="CardRestriction",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    address_restriction: str = field(
        default=None,
        metadata=dict(
            name="AddressRestriction",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class Penalty:
    """
    Exchange penalty information
    """

    cancel_refund: str = field(
        default=None,
        metadata=dict(
            name="CancelRefund",
            type="Attribute",
            help=None,
        )
    )
    non_refundable: str = field(
        default=None,
        metadata=dict(
            name="NonRefundable",
            type="Attribute",
            help=None,
        )
    )
    non_exchangeable: str = field(
        default=None,
        metadata=dict(
            name="NonExchangeable",
            type="Attribute",
            help=None,
        )
    )
    cancelation_penalty: str = field(
        default=None,
        metadata=dict(
            name="CancelationPenalty",
            type="Attribute",
            help=None,
        )
    )
    reissue_penalty: str = field(
        default=None,
        metadata=dict(
            name="ReissuePenalty",
            type="Attribute",
            help=None,
        )
    )
    non_reissue_penalty: str = field(
        default=None,
        metadata=dict(
            name="NonReissuePenalty",
            type="Attribute",
            help=None,
        )
    )
    ticket_refund_penalty: str = field(
        default=None,
        metadata=dict(
            name="TicketRefundPenalty",
            type="Attribute",
            help=None,
        )
    )
    charge_applicable: str = field(
        default=None,
        metadata=dict(
            name="ChargeApplicable",
            type="Attribute",
            help=None,
        )
    )
    charge_portion: str = field(
        default=None,
        metadata=dict(
            name="ChargePortion",
            type="Attribute",
            help=None,
        )
    )
    penalty_amount: str = field(
        default=None,
        metadata=dict(
            name="PenaltyAmount",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class PermittedProviders:
    provider: str = field(
        default=None,
        metadata=dict(
            name="Provider",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class PersonalGeography:
    """
    Personal geography details of the associated passenger.
    """

    country_code: str = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Element",
            help="Passenger country code.",
            length=2
        )
    )
    state_province_code: str = field(
        default=None,
        metadata=dict(
            name="StateProvinceCode",
            type="Element",
            help="Passenger state/province code.",
            max_length=6.0
        )
    )
    city_code: str = field(
        default=None,
        metadata=dict(
            name="CityCode",
            type="Element",
            help="Passenger city code.",
            length=3
        )
    )


@dataclass
class PointOfCommencement:
    """
    Point of Commencement is optional. CityOrAirportCode and date portion of the Time attribute is mandatory.
    """

    city_or_airport_code: str = field(
        default=None,
        metadata=dict(
            name="CityOrAirportCode",
            type="Attribute",
            help="Three digit Airport or City code that would be the Point of Commencement location for the trips/legs mentioned.",
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
            help="Specify a date or date and time",
            required=True
        )
    )


@dataclass
class PointOfSale:
    """
    User can use this node to send a specific PCC to access fares allowed only for that PCC. This node gives the capability for fare redistribution at UR level. For fare redistribution at the stored fare level see AirPricingSolution/AirPricingInfo/AirPricingModifiers/PointOfSale.
    """

    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="The provider in which the PCC is defined.",
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
            help="The PCC in the host system.",
            required=True,
            min_length=2.0,
            max_length=10.0
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    iata: str = field(
        default=None,
        metadata=dict(
            name="IATA",
            type="Attribute",
            help="Used for rapid reprice. This field is the IATA associated to this Point of Sale PCC. Providers: 1G/1V",
            max_length=8.0
        )
    )


@dataclass
class PolicyInformation:
    """
    Policy Information required for File Finishing
    """

    reason_code: "PolicyInformation.str" = field(
        default=None,
        metadata=dict(
            name="ReasonCode",
            type="Element",
            help="Reason Code",
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Policy Type - Air, Hotel, Car, Rail, Ticketing",
            required=True
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="Policy Name",
        )
    )
    out_of_policy: str = field(
        default=None,
        metadata=dict(
            name="OutOfPolicy",
            type="Attribute",
            help="In Policy / Out of Policy Indicator",
        )
    )
    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help=None,
        )
    )

    @dataclass
    class ReasonCode:
        out_of_policy: str = field(
            default=None,
            metadata=dict(
                name="OutOfPolicy",
                type="Element",
                help="Reason Code - Out of Policy",
            )
        )
        purpose_of_trip: str = field(
            default=None,
            metadata=dict(
                name="PurposeOfTrip",
                type="Element",
                help="Reason Code -Purpose of Trip",
            )
        )
        remark: str = field(
            default=None,
            metadata=dict(
                name="Remark",
                type="Element",
                help=None,
            )
        )


@dataclass
class PriceMatchError:
    error_message: str = field(
        default=None,
        metadata=dict(
            name="ErrorMessage",
            type="Element",
            help=None,
            required=True
        )
    )
    vendor_code: str = field(
        default=None,
        metadata=dict(
            name="VendorCode",
            type="Attribute",
            help="The code of the vendor (e.g. HZ, etc.)",
            min_length=1.0,
            max_length=5.0
        )
    )
    hotel_chain: str = field(
        default=None,
        metadata=dict(
            name="HotelChain",
            type="Attribute",
            help="2 Letter Hotel Chain Code",
            length=2
        )
    )
    hotel_code: str = field(
        default=None,
        metadata=dict(
            name="HotelCode",
            type="Attribute",
            help="Unique hotel identifier for the channel.",
            max_length=32.0
        )
    )
    req_base: str = field(
        default=None,
        metadata=dict(
            name="ReqBase",
            type="Attribute",
            help="BaseRate in the request.",
        )
    )
    rsp_base: str = field(
        default=None,
        metadata=dict(
            name="RspBase",
            type="Attribute",
            help="BaseRate retruned from the supplier.",
        )
    )
    base_diff: str = field(
        default=None,
        metadata=dict(
            name="BaseDiff",
            type="Attribute",
            help="BaseRate Difference.",
        )
    )
    req_total: str = field(
        default=None,
        metadata=dict(
            name="ReqTotal",
            type="Attribute",
            help="Estimated Total Amount in the request.",
        )
    )
    rsp_total: str = field(
        default=None,
        metadata=dict(
            name="RspTotal",
            type="Attribute",
            help="Estimated Total Amount returned from the supplier.",
        )
    )
    total_diff: str = field(
        default=None,
        metadata=dict(
            name="TotalDiff",
            type="Attribute",
            help="Estimated Total Amount difference.",
        )
    )


@dataclass
class Provider:
    """
    Provider identifier
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True,
            min_length=2.0,
            max_length=5.0
        )
    )


@dataclass
class ProviderArnksegment:
    """
    Represents host ARNK segments.
    """

    previous_segment: "ProviderArnksegment.str" = field(
        default=None,
        metadata=dict(
            name="PreviousSegment",
            type="Element",
            help=None,
        )
    )
    next_segment: "ProviderArnksegment.str" = field(
        default=None,
        metadata=dict(
            name="NextSegment",
            type="Element",
            help=None,
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    provider_segment_order: str = field(
        default=None,
        metadata=dict(
            name="ProviderSegmentOrder",
            type="Attribute",
            help="To identify the appropriate travel sequence for Air/Car/Hotel/Rail segments/reservations in the provider reservation.",
            max_inclusive=999.0
        )
    )

    @dataclass
    class PreviousSegment:
        air_segment_ref: str = field(
            default=None,
            metadata=dict(
                name="AirSegmentRef",
                type="Element",
                help="Reference to AirSegment from an Air Reservation.",
            )
        )
        hotel_reservation_ref: str = field(
            default=None,
            metadata=dict(
                name="HotelReservationRef",
                type="Element",
                help="Specify the locator code of Hotel reservation.",
            )
        )
        vehicle_reservation_ref: str = field(
            default=None,
            metadata=dict(
                name="VehicleReservationRef",
                type="Element",
                help="Specify the locator code of Vehicle reservation.",
            )
        )
        passive_segment_ref: str = field(
            default=None,
            metadata=dict(
                name="PassiveSegmentRef",
                type="Element",
                help="Reference to PassiveSegment from a Passive Reservation.",
            )
        )

    @dataclass
    class NextSegment:
        air_segment_ref: str = field(
            default=None,
            metadata=dict(
                name="AirSegmentRef",
                type="Element",
                help="Reference to AirSegment from an Air Reservation.",
            )
        )
        hotel_reservation_ref: str = field(
            default=None,
            metadata=dict(
                name="HotelReservationRef",
                type="Element",
                help="Specify the locator code of Hotel reservation.",
            )
        )
        vehicle_reservation_ref: str = field(
            default=None,
            metadata=dict(
                name="VehicleReservationRef",
                type="Element",
                help="Specify the locator code of Vehicle reservation.",
            )
        )
        passive_segment_ref: str = field(
            default=None,
            metadata=dict(
                name="PassiveSegmentRef",
                type="Element",
                help="Reference to PassiveSegment from a Passive Reservation.",
            )
        )


@dataclass
class ProviderReservation:
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
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
            help=None,
            required=True,
            max_length=15.0
        )
    )


@dataclass
class ProviderReservationInfoRef:
    """
    Container for Provider reservation reference key.
    """

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
class PseudoCityCode:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=2.0,
            max_length=10.0
        )
    )


@dataclass
class QueuePlace:
    """
    Allow queue placement of a PNR at the time of booking to be used for Providers 1G,1V,1P and 1J.
    """

    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Element",
            help="Pseudo City Code",
            min_length=2.0,
            max_length=10.0
        )
    )
    queue_selector: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="QueueSelector",
            type="Element",
            help="Identifies the Queue Information to be selected for placing the UR",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class RailLocation(Location):
    """
    RCH specific location code (a.k.a UCodes) which uniquely identifies a train station.
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True,
            min_length=3.0,
            max_length=8.0,
            white_space="collapse"
        )
    )


@dataclass
class ReferencePoint:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            max_length=30.0
        )
    )


@dataclass
class RefundRemark:
    """
    A textual remark displayed in Refund Quote and Refund response.
    """

    remark_data: str = field(
        default=None,
        metadata=dict(
            name="RemarkData",
            type="Element",
            help="Actual remark data.",
            required=True
        )
    )


@dataclass
class Remark(str):
    """
    A textual remark container to hold any printable text. (max 512 chars)
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class RequestKeyMappings:
    """
    All the elements for which mapping key sent in the request is different from the mapping key comes in the response.
    """

    key_mapping: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="KeyMapping",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class RequiredField:
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="The name of the required field",
            required=True
        )
    )


@dataclass
class Requisition:
    """
    Requisition Form of Payment
    """

    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="Requisition number used for accounting",
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="Classification Category for the requisition payment",
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Type can be Cash or Credit for category as Government",
        )
    )


@dataclass
class ReservationName:
    """
    Container to represent reservation name as appears in GDS booking
    """

    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help=None,
            required=True
        )
    )
    name_override: str = field(
        default=None,
        metadata=dict(
            name="NameOverride",
            type="Element",
            help="To be used if the reservation name is other than booking travelers in the PNR",
            required=True
        )
    )


@dataclass
class ResponseMessage(str):
    """
    A simple textual fare note. Used within several other objects.
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Indicates the type of message (Warning, Error, Info)",
        )
    )


@dataclass
class Restriction:
    """
    Which activities are supported for a particular element
    """

    operation: str = field(
        default=None,
        metadata=dict(
            name="Operation",
            type="Attribute",
            help="The operation that is restricted",
            required=True
        )
    )
    reason: str = field(
        default=None,
        metadata=dict(
            name="Reason",
            type="Attribute",
            help="The reason it is restricted",
        )
    )


@dataclass
class RoleInfo:
    """
    Container to specify the role of the agent
    """

    id: str = field(
        default=None,
        metadata=dict(
            name="Id",
            type="Attribute",
            help="Unique identifier of the role.",
            required=True,
            max_length=19.0
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="Agent's role name",
            required=True,
            max_length=128.0
        )
    )
    source: str = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute",
            help="Role inheritance level. Needed in the response, not in the request",
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            help="Description of role",
            max_length=1024.0
        )
    )


@dataclass
class SearchTicketing:
    """
    Search restriction by Agent
    """

    ticket_status: str = field(
        default="Both",
        metadata=dict(
            name="TicketStatus",
            type="Attribute",
            help="Return only PNRs with ticketed, non-ticketed or both",
        )
    )
    reservation_status: str = field(
        default="Both",
        metadata=dict(
            name="ReservationStatus",
            type="Attribute",
            help="Used only if 'TicketStatus' set to 'No' or 'Both'. Return only PNRs with specific reservation status or both statuses.",
        )
    )
    ticket_date: str = field(
        default=None,
        metadata=dict(
            name="TicketDate",
            type="Attribute",
            help="Identifies when this reservation was ticketed, or when it should be ticketed by (in the event of a TTL)",
        )
    )


@dataclass
class SeatAttribute:
    """
    Identifies the seat attribute of the service.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True,
            min_length=1.0,
            max_length=2.0
        )
    )


@dataclass
class SeatAttributes:
    """
    Identifies the seat attribute of the service.
    """

    seat_attribute: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SeatAttribute",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class SegmentRemark(str):
    """
    A textual remark container to hold any printable text. (max 512 chars)
    """

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
class SellMessage(str):
    """
    Sell Message from Vendor. This is applicable in response messages only, any input in request message will be ignored.
    """

    pass


@dataclass
class ServiceData:
    seat_attributes: str = field(
        default=None,
        metadata=dict(
            name="SeatAttributes",
            type="Element",
            help=None,
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element",
            help=None,
        )
    )
    ssrref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SSRRef",
            type="Element",
            help="References to the related SSRs. At present, only reference to ASVC SSR is supported. Supported providers are 1G/1V/1P/1J",
            min_occurs=0,
            max_occurs=999
        )
    )
    data: str = field(
        default=None,
        metadata=dict(
            name="Data",
            type="Attribute",
            help="Data that specifies the details of the merchandising offering (e.g. seat number for seat service)",
        )
    )
    air_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Attribute",
            help="Reference to a segment if the merchandising offering only pertains to that segment. If no segment reference is present this means this offering is for the whole itinerary.",
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="Reference to a passenger if the merchandising offering only pertains to that passenger. If no passenger reference is present this means this offering is for all passengers.",
        )
    )
    stop_over: str = field(
        default="false",
        metadata=dict(
            name="StopOver",
            type="Attribute",
            help="Indicates that there is a significant delay between flights (usually 12 hours or more)",
        )
    )
    traveler_type: str = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            help="Passenger Type Code.",
            min_length=3.0,
            max_length=5.0
        )
    )
    emdsummary_ref: str = field(
        default=None,
        metadata=dict(
            name="EMDSummaryRef",
            type="Attribute",
            help="Reference to the corresponding EMD issued. Supported providers are 1G/1V/1P/1J",
        )
    )
    emdcoupon_ref: str = field(
        default=None,
        metadata=dict(
            name="EMDCouponRef",
            type="Attribute",
            help="Reference to the corresponding EMD coupon issued. Supported providers are 1G/1V/1P/1J",
        )
    )


@dataclass
class ServiceFeeTaxInfo:
    """
    The taxes associated to a particular Service Fee.
    """

    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="The tax category represents a valid IATA tax code.",
            required=True
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class ServiceInfo:
    description: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Description",
            type="Element",
            help="Description of the Service. Usually used in tandem with one or more media items.",
            min_occurs=1,
            max_occurs=999
        )
    )
    media_item: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="MediaItem",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=3
        )
    )


@dataclass
class ShopInformation:
    """
    Shopping Information required for File Finishing
    """

    search_request: List["ShopInformation.str"] = field(
        default_factory=list,
        metadata=dict(
            name="SearchRequest",
            type="Element",
            help="Search parameters that were used in LFS request",
            min_occurs=0,
            max_occurs=999
        )
    )
    flights_offered: List["ShopInformation.str"] = field(
        default_factory=list,
        metadata=dict(
            name="FlightsOffered",
            type="Element",
            help="Flights with lowest logical airfare returned as response to LFS request",
            min_occurs=0,
            max_occurs=999
        )
    )
    cabin_shopped: str = field(
        default=None,
        metadata=dict(
            name="CabinShopped",
            type="Attribute",
            help=None,
        )
    )
    cabin_selected: str = field(
        default=None,
        metadata=dict(
            name="CabinSelected",
            type="Attribute",
            help=None,
        )
    )
    lowest_fare_offered: str = field(
        default=None,
        metadata=dict(
            name="LowestFareOffered",
            type="Attribute",
            help=None,
        )
    )

    @dataclass
    class SearchRequest:
        origin: str = field(
            default=None,
            metadata=dict(
                name="Origin",
                type="Attribute",
                help=None,
                length=3,
                white_space="collapse"
            )
        )
        destination: str = field(
            default=None,
            metadata=dict(
                name="Destination",
                type="Attribute",
                help=None,
                length=3,
                white_space="collapse"
            )
        )
        departure_time: str = field(
            default=None,
            metadata=dict(
                name="DepartureTime",
                type="Attribute",
                help="Date and Time at which this entity departs. This does not include Time Zone information since it can be derived from origin location",
            )
        )
        class_of_service: str = field(
            default=None,
            metadata=dict(
                name="ClassOfService",
                type="Attribute",
                help=None,
                min_length=1.0,
                max_length=2.0
            )
        )

    @dataclass
    class FlightsOffered:
        origin: str = field(
            default=None,
            metadata=dict(
                name="Origin",
                type="Attribute",
                help=None,
                length=3,
                white_space="collapse"
            )
        )
        destination: str = field(
            default=None,
            metadata=dict(
                name="Destination",
                type="Attribute",
                help=None,
                length=3,
                white_space="collapse"
            )
        )
        departure_time: str = field(
            default=None,
            metadata=dict(
                name="DepartureTime",
                type="Attribute",
                help="Date and Time at which this entity departs. This does not include Time Zone information since it can be derived from origin location",
            )
        )
        travel_order: str = field(
            default=None,
            metadata=dict(
                name="TravelOrder",
                type="Attribute",
                help=None,
            )
        )
        carrier: str = field(
            default=None,
            metadata=dict(
                name="Carrier",
                type="Attribute",
                help=None,
                length=2
            )
        )
        flight_number: str = field(
            default=None,
            metadata=dict(
                name="FlightNumber",
                type="Attribute",
                help=None,
                max_length=5.0
            )
        )
        class_of_service: str = field(
            default=None,
            metadata=dict(
                name="ClassOfService",
                type="Attribute",
                help=None,
                min_length=1.0,
                max_length=2.0
            )
        )
        stop_over: str = field(
            default="false",
            metadata=dict(
                name="StopOver",
                type="Attribute",
                help=None,
            )
        )
        connection: str = field(
            default="false",
            metadata=dict(
                name="Connection",
                type="Attribute",
                help=None,
            )
        )


@dataclass
class SimpleName(str):
    """
    Free text name
    """

    pass


@dataclass
class Ssrinfo:
    """
    Bundle SSR with BookingTraveler reference in order to add SSR post booking
    """

    ssr: str = field(
        default=None,
        metadata=dict(
            name="SSR",
            type="Element",
            help=None,
            required=True
        )
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help="Reference to Booking Traveler.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class State(str):
    """
    Container to house the state code for an address
    """

    pass


@dataclass
class StockControl:
    """
    The Stock Control Numbers related details of the MCO.
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Stock control type valid options include: Pending, Failed, Plain Paper, Blank, Suppressed.",
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="Stock control number.",
        )
    )


@dataclass
class SupplierLocator:
    """
    Locator code on the host carrier system
    """

    segment_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SegmentRef",
            type="Element",
            help="Air/Passive Segment Reference",
            min_occurs=0,
            max_occurs=999
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help="Carrier Code",
            required=True,
            length=2
        )
    )
    supplier_locator_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierLocatorCode",
            type="Attribute",
            help="Carrier reservation locator code",
            required=True
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider Reservation reference",
        )
    )
    create_date_time: str = field(
        default=None,
        metadata=dict(
            name="CreateDateTime",
            type="Attribute",
            help="The Date and Time which the reservation is received from the Vendor as a SupplierLocator creation Date.",
        )
    )


@dataclass
class TerminalSessionInfo(str):
    """
    Travelport use only. This element contains CDATA information representing existing GDS session data or ACH credentials information of the terminal user
    """

    pass


@dataclass
class TicketNumber:
    """
    The identifying number for the actual ticket
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            max_length=13.0
        )
    )


@dataclass
class TravelInfo:
    """
    Traveler information details like Travel Purpose and Trip Name
    """

    trip_name: str = field(
        default=None,
        metadata=dict(
            name="TripName",
            type="Attribute",
            help="Trip Name",
            max_length=50.0
        )
    )
    travel_purpose: str = field(
        default=None,
        metadata=dict(
            name="TravelPurpose",
            type="Attribute",
            help="Purpose of the trip",
            max_length=50.0
        )
    )


@dataclass
class TravelerInformation:
    """
    Traveler Information required for File Finishing
    """

    emergency_contact: "TravelerInformation.str" = field(
        default=None,
        metadata=dict(
            name="EmergencyContact",
            type="Element",
            help=None,
        )
    )
    home_airport: str = field(
        default=None,
        metadata=dict(
            name="HomeAirport",
            type="Attribute",
            help=None,
            length=3
        )
    )
    visa_expiration_date: str = field(
        default=None,
        metadata=dict(
            name="VisaExpirationDate",
            type="Attribute",
            help=None,
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="A reference to a passenger.",
            required=True
        )
    )

    @dataclass
    class EmergencyContact:
        phone_number: str = field(
            default=None,
            metadata=dict(
                name="PhoneNumber",
                type="Element",
                help=None,
            )
        )
        name: str = field(
            default=None,
            metadata=dict(
                name="Name",
                type="Attribute",
                help="Name of Emergency Contact Person",
            )
        )
        relationship: str = field(
            default=None,
            metadata=dict(
                name="Relationship",
                type="Attribute",
                help="Relationship between Traveler and Emergency Contact Person",
            )
        )


@dataclass
class TravelerType:
    """
    The 3-char IATA traveler type code
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True,
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class TypeAgencyHierarchyReference:
    profile_id: str = field(
        default=None,
        metadata=dict(
            name="ProfileID",
            type="Attribute",
            help=None,
            required=True
        )
    )
    profile_type: str = field(
        default=None,
        metadata=dict(
            name="ProfileType",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TypeAgencyPayment:
    """
    Type for Agency Payment.
    """

    agency_billing_identifier: str = field(
        default=None,
        metadata=dict(
            name="AgencyBillingIdentifier",
            type="Attribute",
            help="Value of the billing id",
            required=True,
            max_length=128.0
        )
    )
    agency_billing_number: str = field(
        default=None,
        metadata=dict(
            name="AgencyBillingNumber",
            type="Attribute",
            help="Value of billing number",
            max_length=128.0
        )
    )
    agency_billing_password: str = field(
        default=None,
        metadata=dict(
            name="AgencyBillingPassword",
            type="Attribute",
            help="Value of billing password",
            max_length=128.0
        )
    )


@dataclass
class TypeBookingTransactionsAllowed:
    booking_enabled: str = field(
        default=None,
        metadata=dict(
            name="BookingEnabled",
            type="Attribute",
            help="Allow or prohibit booking transaction for the given product type on this Provider/Supplier. Inheritable.",
        )
    )


@dataclass
class TypeDateRange:
    """
    Specify a range of dates
    """

    start_date: str = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute",
            help=None,
            required=True
        )
    )
    end_date: str = field(
        default=None,
        metadata=dict(
            name="EndDate",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TypeErrorInfo:
    """
    Container for error data when there is an application error.
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Element",
            help=None,
            required=True
        )
    )
    service: str = field(
        default=None,
        metadata=dict(
            name="Service",
            type="Element",
            help=None,
            required=True
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Element",
            help=None,
            required=True
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Element",
            help=None,
            required=True
        )
    )
    transaction_id: str = field(
        default=None,
        metadata=dict(
            name="TransactionId",
            type="Element",
            help=None,
            required=True
        )
    )
    trace_id: str = field(
        default=None,
        metadata=dict(
            name="TraceId",
            type="Element",
            help=None,
        )
    )
    command_history: str = field(
        default=None,
        metadata=dict(
            name="CommandHistory",
            type="Element",
            help=None,
        )
    )
    auxdata: str = field(
        default=None,
        metadata=dict(
            name="Auxdata",
            type="Element",
            help=None,
        )
    )
    stack_trace: str = field(
        default=None,
        metadata=dict(
            name="StackTrace",
            type="Element",
            help=None,
        )
    )


@dataclass
class TypeFormOfPaymentPnrreference:
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Unique ID to identify a ProviderReservationInfo",
        )
    )
    provider_reservation_level: str = field(
        default="true",
        metadata=dict(
            name="ProviderReservationLevel",
            type="Attribute",
            help="It means that the form of payment is applied at ProviderReservation level.",
        )
    )


@dataclass
class TypeFreeFormText(str):
    """
    Free form Text
    """

    pass


@dataclass
class TypeGeneralReference:
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
class TypeGuaranteeInformation:
    """
    Information pertaining to the payment of type Guarantee.
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Guarantee only or Deposit",
            required=True
        )
    )
    agency_type: str = field(
        default=None,
        metadata=dict(
            name="AgencyType",
            type="Attribute",
            help="Guarantee to Agency IATA or Guarantee to Another Agency IATA",
            required=True
        )
    )
    iatanumber: str = field(
        default=None,
        metadata=dict(
            name="IATANumber",
            type="Attribute",
            help="Payment IATA number. (ie. IATA of Agency or Other Agency)",
            required=True,
            min_length=1.0,
            max_length=128.0
        )
    )


@dataclass
class TypeKeyBasedReference:
    """
    Generic type to be used for Key based reference
    """

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
class TypeKeyword:
    """
    A complexType for keyword information.
    """

    sub_key: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SubKey",
            type="Element",
            help="A further breakdown of a keyword.",
            min_occurs=0,
            max_occurs=99
        )
    )
    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help="Information for a keyword.",
            min_occurs=0,
            max_occurs=999
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="The keyword name.",
            required=True,
            max_length=12.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="The number for this keyword.",
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            help="A brief description of the keyword",
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
class TypeLocation:
    airport: str = field(
        default=None,
        metadata=dict(
            name="Airport",
            type="Element",
            help=None,
        )
    )
    city: str = field(
        default=None,
        metadata=dict(
            name="City",
            type="Element",
            help=None,
        )
    )
    city_or_airport: str = field(
        default=None,
        metadata=dict(
            name="CityOrAirport",
            type="Element",
            help=None,
        )
    )


@dataclass
class TypeNonAirReservationRef:
    locator_code: str = field(
        default=None,
        metadata=dict(
            name="LocatorCode",
            type="Attribute",
            help=None,
            required=True,
            min_length=5.0,
            max_length=8.0
        )
    )


@dataclass
class TypeOtakeyword:
    """
    A complexType for keyword information.
    """

    sub_key: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SubKey",
            type="Element",
            help="A further breakdown of a keyword.",
            min_occurs=0,
            max_occurs=99
        )
    )
    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help="Information for a keyword.",
            min_occurs=0,
            max_occurs=999
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="The keyword name.",
            required=True,
            max_length=6.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="The number for this keyword.",
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            help="A brief description of the keyword",
        )
    )


@dataclass
class TypeOtasubKey:
    """
    The attributes and elements in a SubKey.
    """

    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help="Information for a sub key.",
            min_occurs=0,
            max_occurs=999
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="A subkey to identify the special equipment codes. Applicable when Policy/@Name is EQUIP. Uses OTA CODE 'EQP'. 1P/1J.",
            required=True
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            help="A brief description of a subkey.",
        )
    )


@dataclass
class TypePassengerType:
    """
    Passenger type code with optional age information
    """

    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            help="Optional passenger Name with associated LoyaltyCard may provide benefit when pricing itineraries using Low Cost Carriers. In general, most carriers do not consider passenger LoyalyCard information when initially pricing itineraries.",
        )
    )
    loyalty_card: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyCard",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    discount_card: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="DiscountCard",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=9
        )
    )
    personal_geography: str = field(
        default=None,
        metadata=dict(
            name="PersonalGeography",
            type="Element",
            help="Passenger personal geography detail to be sent to Host for accessing location specific fares",
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The 3-char IATA passenger type code",
            required=True,
            min_length=3.0,
            max_length=5.0
        )
    )
    age: str = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute",
            help=None,
        )
    )
    dob: str = field(
        default=None,
        metadata=dict(
            name="DOB",
            type="Attribute",
            help="Passenger Date of Birth",
        )
    )
    gender: str = field(
        default=None,
        metadata=dict(
            name="Gender",
            type="Attribute",
            help="The passenger gender type",
            min_length=1.0,
            max_length=2.0
        )
    )
    price_ptconly: str = field(
        default=None,
        metadata=dict(
            name="PricePTCOnly",
            type="Attribute",
            help=None,
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="This value should be set for Multiple Passengers in the request.",
        )
    )
    accompanied_passenger: str = field(
        default="false",
        metadata=dict(
            name="AccompaniedPassenger",
            type="Attribute",
            help="Container to identify accompanied passenger. Set true means this passenger is accompanied",
        )
    )
    residency_type: str = field(
        default=None,
        metadata=dict(
            name="ResidencyType",
            type="Attribute",
            help="The passenger residence type.",
        )
    )


@dataclass
class TypePaymentCard:
    """
    Container for all credit and debit card information.
    """

    phone_number: str = field(
        default=None,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            help=None,
        )
    )
    billing_address: str = field(
        default=None,
        metadata=dict(
            name="BillingAddress",
            type="Element",
            help="The address to where the billing statements for this card are sent. Used for address verification purposes.",
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="The 2 letter credit/ debit card type.",
            min_length=2.0,
            max_length=2.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help=None,
            min_length=13.0,
            max_length=128.0
        )
    )
    exp_date: str = field(
        default=None,
        metadata=dict(
            name="ExpDate",
            type="Attribute",
            help="The Expiration date of this card in YYYY-MM format.",
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="The name as it appears on the card.",
            max_length=128.0
        )
    )
    cvv: str = field(
        default=None,
        metadata=dict(
            name="CVV",
            type="Attribute",
            help="Card Verification Code",
            max_length=4.0
        )
    )
    approval_code: str = field(
        default=None,
        metadata=dict(
            name="ApprovalCode",
            type="Attribute",
            help="This code is required for an authorization process from the Credit Card company directly,required for some of the CCH carriers.This attribute is also used for EMD retrieve and issuance transactions.",
            min_length=1.0,
            max_length=16.0
        )
    )


@dataclass
class TypePolicyCodesList:
    policy_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PolicyCode",
            type="Element",
            help="A code that indicates why an item was determined to be ‘out of policy’.",
            min_occurs=0,
            max_occurs=10
        )
    )
    min_policy_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="MinPolicyCode",
            type="Element",
            help="A code that indicates why the minimum fare or rate was determined to be ‘out of policy’.",
            min_occurs=0,
            max_occurs=10
        )
    )
    max_policy_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="MaxPolicyCode",
            type="Element",
            help="A code that indicates why the maximum fare or rate was determined to be ‘out of policy’.",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class TypeProfileRef:
    """
    ProfileEntityID and ProfileLevel together identity a profile entity.
    """

    profile_entity_id: str = field(
        default=None,
        metadata=dict(
            name="ProfileEntityID",
            type="Attribute",
            help=None,
            required=True
        )
    )
    profile_level: str = field(
        default=None,
        metadata=dict(
            name="ProfileLevel",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TypeProviderReservationSpecificInfo:
    operated_by: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="OperatedBy",
            type="Element",
            help="Cross accrual carrier info",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            help="Tagging provider reservation info with LoyaltyCard.",
        )
    )
    provider_reservation_level: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationLevel",
            type="Attribute",
            help="If true means Loyalty card is applied at ProviderReservation level.",
        )
    )
    reservation_level: str = field(
        default=None,
        metadata=dict(
            name="ReservationLevel",
            type="Attribute",
            help="If true means Loyalty card is applied at Universal Record Reservation level e.g. Hotel Reservation, Vehicle Reservation etc.",
        )
    )


@dataclass
class TypeRateDescription:
    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="Optional context name of the text block being returned i.e. Room details",
        )
    )


@dataclass
class TypeRemark(str):
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Contains the Provider Code of the provider for which this element is used",
            min_length=2.0,
            max_length=5.0
        )
    )


@dataclass
class TypeRemarkWithTravelerRef:
    remark_data: str = field(
        default=None,
        metadata=dict(
            name="RemarkData",
            type="Element",
            help="Actual remarks data.",
            required=True
        )
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help="Reference to Booking Traveler.",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Contains the Provider Code of the provider for which this element is used",
            min_length=2.0,
            max_length=5.0
        )
    )


@dataclass
class TypeResultMessage(str):
    """
    Used to identify the results of a requests
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Indicates the type of message (Warning, Error, Info)",
        )
    )


@dataclass
class TypeSearchLocation:
    distance: str = field(
        default=None,
        metadata=dict(
            name="Distance",
            type="Element",
            help=None,
        )
    )
    airport: str = field(
        default=None,
        metadata=dict(
            name="Airport",
            type="Element",
            help=None,
        )
    )
    city: str = field(
        default=None,
        metadata=dict(
            name="City",
            type="Element",
            help=None,
        )
    )
    city_or_airport: str = field(
        default=None,
        metadata=dict(
            name="CityOrAirport",
            type="Element",
            help=None,
        )
    )
    coordinate_location: str = field(
        default=None,
        metadata=dict(
            name="CoordinateLocation",
            type="Element",
            help=None,
        )
    )
    rail_location: str = field(
        default=None,
        metadata=dict(
            name="RailLocation",
            type="Element",
            help=None,
        )
    )


@dataclass
class TypeSegmentRef:
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
class TypeSpecificTime:
    """
    Specify exact times. System will automatically convert to a range according to agency configuration.
    """

    time: str = field(
        default=None,
        metadata=dict(
            name="Time",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TypeSubKey:
    """
    The attributes and elements in a SubKey.
    """

    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help="Information for a sub key.",
            min_occurs=0,
            max_occurs=999
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="A subkey to identify the specific information within this keyword",
            required=True
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            help="A brief description of a subkey.",
        )
    )


@dataclass
class TypeTax:
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class TypeTimeRange:
    """
    Specify a range of times.
    """

    earliest_time: str = field(
        default=None,
        metadata=dict(
            name="EarliestTime",
            type="Attribute",
            help=None,
            required=True
        )
    )
    latest_time: str = field(
        default=None,
        metadata=dict(
            name="LatestTime",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TypeTimeSpec:
    """
    Specifies times as either specific times, or a time range
    """

    time_range: str = field(
        default=None,
        metadata=dict(
            name="TimeRange",
            type="Element",
            help=None,
        )
    )
    specific_time: str = field(
        default=None,
        metadata=dict(
            name="SpecificTime",
            type="Element",
            help=None,
        )
    )
    preferred_time: str = field(
        default=None,
        metadata=dict(
            name="PreferredTime",
            type="Attribute",
            help="Specifies a time that would be preferred within the time range specified.",
        )
    )


@dataclass
class TypeVendorLocation:
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="The code of the provider (e.g. 1G, 1S)",
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
            help="The code of the vendor (e.g. HZ, etc.)",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    preferred_option: str = field(
        default=None,
        metadata=dict(
            name="PreferredOption",
            type="Attribute",
            help="Preferred Option marker for Location.",
        )
    )
    vendor_location_id: str = field(
        default=None,
        metadata=dict(
            name="VendorLocationID",
            type="Attribute",
            help="Location identifier",
            min_length=1.0,
            white_space="collapse"
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Key which maps vendor location with vehicles",
        )
    )
    more_rates_token: str = field(
        default=None,
        metadata=dict(
            name="MoreRatesToken",
            type="Attribute",
            help="Enter the Token when provided by hotel property, more rates exist. HADS/HSS support only.",
            min_length=1.0,
            max_length=30.0
        )
    )


@dataclass
class TypeVoucherInformation:
    """
    Information pertaining to the payment of a Vehicle Rental.
    """

    voucher_type: str = field(
        default=None,
        metadata=dict(
            name="VoucherType",
            type="Attribute",
            help="Specifies if the Voucher is for Full Credit or a Group/Day or a Monetary Amount or RegularVoucher.",
            required=True
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="Amount associated with the Voucher.",
        )
    )
    confirmation_number: str = field(
        default=None,
        metadata=dict(
            name="ConfirmationNumber",
            type="Attribute",
            help="Confirmation from the vendor for the voucher",
        )
    )
    account_name: str = field(
        default=None,
        metadata=dict(
            name="AccountName",
            type="Attribute",
            help="Associated account name for the voucher",
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="To advise car associates of the voucher number and store in the car segment. It is required when VoucherType selected as 'RegularVoucher' for 1P, 1J only.",
            min_length=1.0,
            max_length=16.0
        )
    )


@dataclass
class UnitedNations:
    """
    United Nations Form of Payments
    """

    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class Xmlremark(str):
    """
    A remark container to hold an XML document. (max 1024 chars) This will be encoded with xml encoding.
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="A category to group and organize the various remarks. This is not required, but it is recommended.",
            max_length=10.0
        )
    )


@dataclass
class AccountCode(AttrProviderSupplier):
    """
    it will be considered a default AccounCode to be sent to all the Providers or Suppliers.
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            max_length=36.0
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="An identifier to categorize this account code. For example, FlightPass for AC Flight Pass or RFB for AC corporate Rewards for Business.",
        )
    )


@dataclass
class AccountingRemark(AttrElementKeyResults):
    """
    An accounting remark container to hold any printable text.
    """

    remark_data: str = field(
        default=None,
        metadata=dict(
            name="RemarkData",
            type="Element",
            help="Actual remarks data.",
            required=True
        )
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help="Reference to Booking Traveler.",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="A category to group and organize the various remarks. This is not required, but it is recommended.",
            max_length=14.0
        )
    )
    type_in_gds: str = field(
        default=None,
        metadata=dict(
            name="TypeInGds",
            type="Attribute",
            help=None,
            max_length=30.0
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Contains the Provider Code of the provider for which this accounting remark is used",
            min_length=2.0,
            max_length=5.0
        )
    )
    use_provider_native_mode: str = field(
        default="false",
        metadata=dict(
            name="UseProviderNativeMode",
            type="Attribute",
            help="Will be true when terminal process required, else false",
        )
    )


@dataclass
class ActionStatus(AttrProviderSupplier, AttrElementKeyResults):
    """
    Status of the action that will happen or has happened to the air reservation. One Action status for each provider reservation
    """

    remark: str = field(
        default=None,
        metadata=dict(
            name="Remark",
            type="Element",
            help=None,
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Identifies the type of action (if any) to take on this air reservation. Only TTL, TAU, TAX and TAW can be set by the user.",
            required=True
        )
    )
    ticket_date: str = field(
        default=None,
        metadata=dict(
            name="TicketDate",
            type="Attribute",
            help="Identifies when the action type will happen, or has happened according to the type.",
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Identifies when the action type will happen, or has happened according to the type.",
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    queue_category: str = field(
        default=None,
        metadata=dict(
            name="QueueCategory",
            type="Attribute",
            help="Add Category placement to ticketing queue (required in 1P - default is 00)",
            min_length=1.0,
            white_space="collapse"
        )
    )
    airport_code: str = field(
        default=None,
        metadata=dict(
            name="AirportCode",
            type="Attribute",
            help="Used with Time Limit to specify the airport location where the ticket is to be issued.",
            length=3
        )
    )
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            help="The Branch PCC in the host system where PNR can be queued for ticketing. When used with TAU it will auto queue to Q10. When used with TAW agent performs manual move to Q.",
            min_length=2.0,
            max_length=10.0
        )
    )
    account_code: str = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute",
            help="Used with TAW. Used to specify a corporate or in house account code to the PNR as part of ticketing arrangement field.",
        )
    )


@dataclass
class AgencyPayment(TypeAgencyPayment):
    """
    Container for Agency Payment
    """

    pass


@dataclass
class AgentAction(AttrAgentOverride):
    """
    Depending on context, this will represent information about which agent perform different actions.
    """

    action_type: str = field(
        default=None,
        metadata=dict(
            name="ActionType",
            type="Attribute",
            help="The type of action the agent performed.",
            required=True
        )
    )
    agent_code: str = field(
        default=None,
        metadata=dict(
            name="AgentCode",
            type="Attribute",
            help="The AgenctCode who performed the action.",
            required=True
        )
    )
    branch_code: str = field(
        default=None,
        metadata=dict(
            name="BranchCode",
            type="Attribute",
            help="The BranchCode of the branch (working branch, branchcode used for the request. If nothing specified, branchcode for the agent) who performed the action.",
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
            help="The AgencyCode of the agent who performed the action.",
            required=True
        )
    )
    agent_sine: str = field(
        default=None,
        metadata=dict(
            name="AgentSine",
            type="Attribute",
            help="The sign in user name of the agent logged into the terminal. PROVIDER SUPPORTED: ACH",
        )
    )
    event_time: str = field(
        default=None,
        metadata=dict(
            name="EventTime",
            type="Attribute",
            help="Date and time at which this event took place.",
            required=True
        )
    )


@dataclass
class AppliedProfile(AttrElementKeyResults):
    """
    A simple container to specify the profiles that were applied to a reservation.
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Key for update/delete of the element",
        )
    )
    traveler_id: str = field(
        default=None,
        metadata=dict(
            name="TravelerID",
            type="Attribute",
            help="The ID of the TravelerProfile that was applied",
        )
    )
    traveler_name: str = field(
        default=None,
        metadata=dict(
            name="TravelerName",
            type="Attribute",
            help="The name from the TravelerProfile that was applied",
        )
    )
    account_id: str = field(
        default=None,
        metadata=dict(
            name="AccountID",
            type="Attribute",
            help="The ID of the AccountProfile that was applied",
        )
    )
    account_name: str = field(
        default=None,
        metadata=dict(
            name="AccountName",
            type="Attribute",
            help="The name from the AccountProfile that was applied",
        )
    )
    immediate_parent_id: str = field(
        default=None,
        metadata=dict(
            name="ImmediateParentID",
            type="Attribute",
            help="The ID of the immediate parent that was applied",
        )
    )
    immediate_parent_name: str = field(
        default=None,
        metadata=dict(
            name="ImmediateParentName",
            type="Attribute",
            help="The name of the immediate parent that was applied",
        )
    )


@dataclass
class BookingTraveler(AttrBookingTravelerGrp, AttrElementKeyResults):
    """
    A traveler and all their accompanying data.
    """

    ssr: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SSR",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    name_remark: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="NameRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_seat_assignment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AirSeatAssignment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_seat_assignment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="RailSeatAssignment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    name_number: str = field(
        default=None,
        metadata=dict(
            name="NameNumber",
            type="Attribute",
            help="Host Name Number",
        )
    )


@dataclass
class BookingTravelerName(AttrBookingTravelerName):
    """
    Complete name fields
    """

    pass


@dataclass
class CommissionRemark(AttrElementKeyResults):
    """
    Identifies the agency commision remarks. Specifically used for Worldspan.
    """

    provider_reservation_level: "CommissionRemark.str" = field(
        default=None,
        metadata=dict(
            name="ProviderReservationLevel",
            type="Element",
            help="Specify commission which is applicable to PNR level.",
            required=True
        )
    )
    passenger_type_level: List["CommissionRemark.str"] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerTypeLevel",
            type="Element",
            help="Specify commission which is applicable to per PTC level.",
            min_occurs=1,
            max_occurs=4
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Key to be used for internal processing.",
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Contains the Provider Code of the provider for which this accounting remark is used",
            min_length=2.0,
            max_length=5.0
        )
    )

    @dataclass
    class ProviderReservationLevel(AttrCommissionRemark):
        pass

    @dataclass
    class PassengerTypeLevel(AttrCommissionRemark):
        traveler_type: str = field(
            default=None,
            metadata=dict(
                name="TravelerType",
                type="Attribute",
                help=None,
                required=True,
                min_length=3.0,
                max_length=5.0
            )
        )


@dataclass
class ConnectionPoint(TypeLocation):
    """
    A connection point can be eith an IATA airport or cir city code.
    """

    pass


@dataclass
class ConsolidatorRemark(AttrElementKeyResults):
    """
    Authorization remark for Consolidator access to a PNR . Contains PCC information created by retail agent to allow a consolidator or other Axess users to service their PNR. PROVIDER SUPPORTED: Worldspan and JAL.
    """

    pseudo_city_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PseudoCityCode",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=5
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Key to be used for internal processing.",
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Contains the Provider Code of the provider for which this element is used",
            min_length=2.0,
            max_length=5.0
        )
    )


@dataclass
class CustomerId(TypeRemark):
    """
    A provider reservation field used to store customer information. It may be used to identify reservations which will/will not be available for access.
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class DebitCard(TypePaymentCard):
    """
    Container for all debit card information.
    """

    issue_number: str = field(
        default=None,
        metadata=dict(
            name="IssueNumber",
            type="Attribute",
            help="Verification number for Debit Cards",
            max_length=8.0
        )
    )


@dataclass
class DiscountCard(AttrElementKeyResults):
    """
    Rail Discount Card Information
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
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
            help=None,
            min_length=1.0,
            max_length=255.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help=None,
            min_length=1.0,
            max_length=36.0
        )
    )


@dataclass
class DriversLicense(AttrElementKeyResults):
    """
    Details of drivers license
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    license_number: str = field(
        default=None,
        metadata=dict(
            name="LicenseNumber",
            type="Attribute",
            help="The driving license number of the booking traveler.",
            required=True
        )
    )


@dataclass
class Email(AttrElementKeyResults):
    """
    Container for an email address with a type specifier (max 128 chars)
    """

    provider_reservation_info_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            help="Tagging provider reservation info with Email.",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help=None,
            min_length=1.0,
            max_length=128.0
        )
    )
    comment: str = field(
        default=None,
        metadata=dict(
            name="Comment",
            type="Attribute",
            help=None,
            min_length=1.0
        )
    )
    email_id: str = field(
        default=None,
        metadata=dict(
            name="EmailID",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FormOfPayment(AttrElementKeyResults):
    """
    A Form of Payment used to purchase all or part of a booking.
    """

    provider_reservation_info_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    segment_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SegmentRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    bsppayment: str = field(
        default=None,
        metadata=dict(
            name="BSPPayment",
            type="Element",
            help=None,
        )
    )
    arcpayment: str = field(
        default=None,
        metadata=dict(
            name="ARCPayment",
            type="Element",
            help=None,
        )
    )
    credit_card: str = field(
        default=None,
        metadata=dict(
            name="CreditCard",
            type="Element",
            help=None,
        )
    )
    debit_card: str = field(
        default=None,
        metadata=dict(
            name="DebitCard",
            type="Element",
            help=None,
        )
    )
    enett_van: str = field(
        default=None,
        metadata=dict(
            name="EnettVan",
            type="Element",
            help=None,
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help=None,
            required=True,
            max_length=25.0
        )
    )
    fulfillment_type: str = field(
        default=None,
        metadata=dict(
            name="FulfillmentType",
            type="Attribute",
            help="Collect booking ticket at a Kiosk, print in agency.",
        )
    )
    fulfillment_location: str = field(
        default=None,
        metadata=dict(
            name="FulfillmentLocation",
            type="Attribute",
            help="Information about the location of the printer.",
        )
    )
    fulfillment_idtype: str = field(
        default=None,
        metadata=dict(
            name="FulfillmentIDType",
            type="Attribute",
            help="Identification type, e.g. credit card, to define how the customer will identify himself when collecting the ticket",
        )
    )
    fulfillment_idnumber: str = field(
        default=None,
        metadata=dict(
            name="FulfillmentIDNumber",
            type="Attribute",
            help="Identification number, e.g. card number, to define how the customer will identify himself when collecting the ticket",
        )
    )
    is_agent_type: str = field(
        default="false",
        metadata=dict(
            name="IsAgentType",
            type="Attribute",
            help="If this is true then FormOfPayment mention in Type is anAgent type FormOfPayment.",
        )
    )
    agent_text: str = field(
        default=None,
        metadata=dict(
            name="AgentText",
            type="Attribute",
            help="This is only relevent when IsAgentType is specified as true. Otherwise this will be ignored.",
        )
    )
    reuse_fop: str = field(
        default=None,
        metadata=dict(
            name="ReuseFOP",
            type="Attribute",
            help="Key of the FOP Key to be reused as this Form of Payment.Only Credit and Debit Card will be supported for FOP Reuse.",
        )
    )
    external_reference: str = field(
        default=None,
        metadata=dict(
            name="ExternalReference",
            type="Attribute",
            help=None,
            max_length=32.0
        )
    )
    reusable: str = field(
        default="false",
        metadata=dict(
            name="Reusable",
            type="Attribute",
            help="Indicates whether the form of payment can be reused or not. Currently applicable for Credit and Debit form of payment",
        )
    )
    profile_id: str = field(
        default=None,
        metadata=dict(
            name="ProfileID",
            type="Attribute",
            help="The unique ID of the profile that contains the payment details to use.",
        )
    )
    profile_key: str = field(
        default=None,
        metadata=dict(
            name="ProfileKey",
            type="Attribute",
            help="The Key assigned to the payment details value from the specified profile.",
        )
    )


@dataclass
class GeneralRemark(AttrProviderSupplier, AttrElementKeyResults):
    """
    A textual remark container to hold any printable text. (max 512 chars)
    """

    remark_data: str = field(
        default=None,
        metadata=dict(
            name="RemarkData",
            type="Element",
            help="Actual remarks data.",
            required=True
        )
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help="Reference to Booking Traveler.",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="A category to group and organize the various remarks. This is not required, but it is recommended.",
            max_length=20.0
        )
    )
    type_in_gds: str = field(
        default=None,
        metadata=dict(
            name="TypeInGds",
            type="Attribute",
            help=None,
            max_length=30.0
        )
    )
    supplier_type: str = field(
        default=None,
        metadata=dict(
            name="SupplierType",
            type="Attribute",
            help="The type of product this reservation is relative to",
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    direction: str = field(
        default=None,
        metadata=dict(
            name="Direction",
            type="Attribute",
            help="Direction Incoming or Outgoing of the GeneralRemark.",
        )
    )
    create_date: str = field(
        default=None,
        metadata=dict(
            name="CreateDate",
            type="Attribute",
            help="The date and time that this GeneralRemark was created.",
        )
    )
    use_provider_native_mode: str = field(
        default="false",
        metadata=dict(
            name="UseProviderNativeMode",
            type="Attribute",
            help="Will be true when terminal process required, else false",
        )
    )


@dataclass
class Group(AttrElementKeyResults):
    """
    Represents a traveler group for Group booking and all their accompanying data. SUPPORTED PROVIDER: Worldspan and JAL.
    """

    name: "Group.str" = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            help="Name of the group in group booking.",
            required=True
        )
    )
    delivery_info: str = field(
        default=None,
        metadata=dict(
            name="DeliveryInfo",
            type="Element",
            help=None,
        )
    )
    phone_number: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    ssrref: List["Group.str"] = field(
        default_factory=list,
        metadata=dict(
            name="SSRRef",
            type="Element",
            help="Reference Element for SSR.",
            min_occurs=0,
            max_occurs=999
        )
    )
    address: str = field(
        default=None,
        metadata=dict(
            name="Address",
            type="Element",
            help=None,
        )
    )
    booking_traveler_ref: List["Group.str"] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help="Reference Element for Booking Traveler.",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    traveler_type: str = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            help="Defines the type of traveler used for booking which could be a non-defining type (Companion, Web-fare, etc), or a standard type (Adult, Child, etc).",
            min_length=3.0,
            max_length=5.0
        )
    )
    group_size: str = field(
        default=None,
        metadata=dict(
            name="GroupSize",
            type="Attribute",
            help="Represents size of the group",
            required=True
        )
    )

    @dataclass
    class Name:
        value: str = field(
            default=None,
            metadata=dict(
                name="value",
                type="Restriction",
                help=None,
                min_length=1.0,
                white_space="collapse"
            )
        )

    @dataclass
    class Ssrref:
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
    class BookingTravelerRef:
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
class Guarantee(AttrElementKeyResults):
    """
    Guarantee, Deposit or PrePayment
    """

    credit_card: str = field(
        default=None,
        metadata=dict(
            name="CreditCard",
            type="Element",
            help=None,
        )
    )
    other_guarantee_info: str = field(
        default=None,
        metadata=dict(
            name="OtherGuaranteeInfo",
            type="Element",
            help=None,
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Guarantee, Deposit for 1G/1V/1P/1J and PrePayment for 1P/1J only",
            required=True
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Key for update/delete of the element",
        )
    )
    reuse_fop: str = field(
        default=None,
        metadata=dict(
            name="ReuseFOP",
            type="Attribute",
            help="Key of the FOP Key to be reused as this Form of Payment.Only Credit and Debit Card will be supported for FOP Reuse.",
        )
    )
    external_reference: str = field(
        default=None,
        metadata=dict(
            name="ExternalReference",
            type="Attribute",
            help=None,
            max_length=32.0
        )
    )
    reusable: str = field(
        default="false",
        metadata=dict(
            name="Reusable",
            type="Attribute",
            help="Indicates whether the form of payment can be reused or not. Currently applicable for Credit and Debit form of payment",
        )
    )


@dataclass
class Keyword(TypeKeyword):
    """
    Detail information of keywords.
    """

    pass


@dataclass
class LinkedUniversalRecord(AttrElementKeyResults):
    locator_code: str = field(
        default=None,
        metadata=dict(
            name="LocatorCode",
            type="Attribute",
            help="A Universal Record that need to be linked to the current Universal Record.",
            required=True,
            min_length=5.0,
            max_length=8.0
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class LoyaltyCard(AttrLoyalty):
    """
    Provider loyalty card information
    """

    provider_reservation_specific_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationSpecificInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    card_number: str = field(
        default=None,
        metadata=dict(
            name="CardNumber",
            type="Attribute",
            help=None,
            required=True,
            min_length=1.0,
            max_length=36.0
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help=None,
        )
    )
    membership_status: str = field(
        default=None,
        metadata=dict(
            name="MembershipStatus",
            type="Attribute",
            help=None,
        )
    )
    free_text: str = field(
        default=None,
        metadata=dict(
            name="FreeText",
            type="Attribute",
            help=None,
        )
    )
    supplier_type: str = field(
        default=None,
        metadata=dict(
            name="SupplierType",
            type="Attribute",
            help=None,
        )
    )
    level: str = field(
        default=None,
        metadata=dict(
            name="Level",
            type="Attribute",
            help=None,
            pattern="[a-zA-Z0-9]{1,1}"
        )
    )
    priority_code: str = field(
        default=None,
        metadata=dict(
            name="PriorityCode",
            type="Attribute",
            help=None,
            pattern="[a-zA-Z0-9]{1,1}"
        )
    )
    vendor_location_ref: str = field(
        default=None,
        metadata=dict(
            name="VendorLocationRef",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class LoyaltyProgram(AttrLoyalty):
    level: str = field(
        default=None,
        metadata=dict(
            name="Level",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class Mco(Mcoinformation):
    form_of_payment: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    endorsement: str = field(
        default=None,
        metadata=dict(
            name="Endorsement",
            type="Element",
            help=None,
        )
    )
    mcoexchange_info: str = field(
        default=None,
        metadata=dict(
            name="MCOExchangeInfo",
            type="Element",
            help=None,
        )
    )
    mcofee_info: str = field(
        default=None,
        metadata=dict(
            name="MCOFeeInfo",
            type="Element",
            help=None,
        )
    )
    mcoremark: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="MCORemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    mcoprice_data: str = field(
        default=None,
        metadata=dict(
            name="MCOPriceData",
            type="Element",
            help=None,
        )
    )
    stock_control: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="StockControl",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    mcotext: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="MCOText",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    ticket_type: str = field(
        default=None,
        metadata=dict(
            name="TicketType",
            type="Attribute",
            help="Ticket issue indicator. Possible values 'Pre-paid ticket advice', 'Ticket on departure' and 'Other' .",
        )
    )
    ticket_number: str = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            help="The ticket that this MCO was issued in connection with. Could be the ticket that caused the fee, a residual from an exchange, or an airline service fee.",
        )
    )
    mcoissued: str = field(
        default=None,
        metadata=dict(
            name="MCOIssued",
            type="Attribute",
            help="Set to true when the MCO is to be issued and set to false if it is stored for issue at a later time.",
            required=True
        )
    )
    mcoissue_date: str = field(
        default=None,
        metadata=dict(
            name="MCOIssueDate",
            type="Attribute",
            help="Date and time in which the MCO was issued.",
        )
    )
    mcodoc_num: str = field(
        default=None,
        metadata=dict(
            name="MCODocNum",
            type="Attribute",
            help="MCO document number.",
        )
    )
    issue_reason_code: str = field(
        default=None,
        metadata=dict(
            name="IssueReasonCode",
            type="Attribute",
            help="O - Other, P thru Z - airline specific, 1 thru 9 - market specific",
        )
    )
    plating_carrier: str = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            help="The Plating Carrier for this MCO",
            length=2
        )
    )
    tour_operator: str = field(
        default=None,
        metadata=dict(
            name="TourOperator",
            type="Attribute",
            help="Tour Operator - name of honoring carrier or operator.",
        )
    )
    location: str = field(
        default=None,
        metadata=dict(
            name="Location",
            type="Attribute",
            help="Location of honoring carrier or operator.",
        )
    )
    tour_code: str = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Attribute",
            help="The Tour Code of the MCO.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Contains the Provider Code of the provider that houses this MCO.",
            min_length=2.0,
            max_length=5.0
        )
    )
    provider_locator_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            help="Contains the Provider Locator Code of the Provider Reservation that houses this MCO.",
            max_length=15.0
        )
    )
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            help="The PCC in the host system.",
            min_length=2.0,
            max_length=10.0
        )
    )
    expiry_date: str = field(
        default=None,
        metadata=dict(
            name="ExpiryDate",
            type="Attribute",
            help="E-Voucher’s Expiry Date. This expiry date is specific to Rail product",
        )
    )


@dataclass
class McofeeInfo(AttrAmountPercent):
    """
    Information related to the PTA/TOD (Prepaid Ticket Advice / Ticket on Departure) related to the MCO
    """

    fee_applies_to_ind: str = field(
        default=None,
        metadata=dict(
            name="FeeAppliesToInd",
            type="Attribute",
            help="Indicates if PTA/TOD fee is for the entire MCO or is per person.",
        )
    )


@dataclass
class McopriceData:
    tax_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    commission: "McopriceData.str" = field(
        default=None,
        metadata=dict(
            name="Commission",
            type="Element",
            help=None,
        )
    )
    mcoamount: str = field(
        default=None,
        metadata=dict(
            name="MCOAmount",
            type="Attribute",
            help="The total value of the MCO including any processing fees.",
            required=True
        )
    )
    mcoequivalent_fare: str = field(
        default=None,
        metadata=dict(
            name="MCOEquivalentFare",
            type="Attribute",
            help="Exchange value of the currency actually collected.",
        )
    )
    mcototal_amount: str = field(
        default=None,
        metadata=dict(
            name="MCOTotalAmount",
            type="Attribute",
            help="The Total amount for the MCO.",
        )
    )

    @dataclass
    class Commission(AttrAmountPercent):
        pass


@dataclass
class Mcotext(TypeFreeFormText):
    """
    All type of free format text messages related to MCO like - Command Text, Agent Entry, MCO Modifiers, Text Message
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="The type of text. Possible values: Command Text, Agent Entry, MCO Modifiers, Text Message",
        )
    )


@dataclass
class NameRemark(AttrElementKeyResults):
    """
    Text that support Name Remarks.
    """

    remark_data: str = field(
        default=None,
        metadata=dict(
            name="RemarkData",
            type="Element",
            help="Actual remarks data.",
            required=True
        )
    )
    provider_reservation_info_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            help="Tagging provider reservation info with NameRemark.",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="A category to group and organize the various remarks. This is not required, but it is recommended.",
        )
    )


@dataclass
class OptionalServiceApplicationLimitType(OptionalServiceApplicabilityLimitGroup):
    """
    The optional service application limit
    """

    pass


@dataclass
class Osi(AttrElementKeyResults):
    """
    Other Service information sent to the carriers during air bookings
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    carrier: str = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help=None,
            required=True,
            length=2
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            max_length=4.0
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            help=None,
            required=True,
            max_length=256.0
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Contains the Provider Code of the provider for which this OSI is used",
            min_length=2.0,
            max_length=5.0
        )
    )


@dataclass
class Payment(AttrElementKeyResults):
    """
    Payment information - must be used in conjunction with credit card info
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Identifies the type of payment. This can be for an itinerary, a traveler, or a service fee for example.",
            required=True
        )
    )
    form_of_payment_ref: str = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Attribute",
            help="The credit card that is will be used to make this payment.",
            required=True
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="If the type represents a per traveler payment, then this will reference the traveler this payment refers to.",
        )
    )
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
            required=True
        )
    )
    amount_type: str = field(
        default=None,
        metadata=dict(
            name="AmountType",
            type="Attribute",
            help="This field displays type of payment amount when it is non-monetary. Presently available/supported value is 'Flight Pass Credits'.",
            min_length=1.0,
            max_length=32.0
        )
    )
    approximate_amount: str = field(
        default=None,
        metadata=dict(
            name="ApproximateAmount",
            type="Attribute",
            help="It stores the converted payment amount in agency's default currency",
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help="Status to indicate the business association of the payment element.",
        )
    )


@dataclass
class PhoneNumber(AttrElementKeyResults):
    """
    Consists of type (office, home, fax), location (city code), the country code, the number, and an extension.
    """

    provider_reservation_info_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help=None,
        )
    )
    location: str = field(
        default=None,
        metadata=dict(
            name="Location",
            type="Attribute",
            help="IATA code for airport or city",
            max_length=10.0
        )
    )
    country_code: str = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Attribute",
            help="Hosts/providers will expect this to be international dialing digits",
            max_length=5.0
        )
    )
    area_code: str = field(
        default=None,
        metadata=dict(
            name="AreaCode",
            type="Attribute",
            help=None,
            max_length=10.0
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="The local phone number",
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
            help=None,
            max_length=10.0
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            help=None,
            max_length=1024.0
        )
    )


@dataclass
class Postscript(TypeRemark):
    """
    Postscript Notes
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class QueueSelector(AttrQueueInfo):
    """
    Identifies the Queue with Queue Number , Category and Date Range.
    """

    pass


@dataclass
class RailSeatAssignment(AttrElementKeyResults):
    """
    Identifies the seat assignment for a passenger on RailSegment.
    """

    characteristic: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Characteristic",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help=None,
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
            help=None,
            required=True
        )
    )
    rail_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="RailSegmentRef",
            type="Attribute",
            help=None,
        )
    )
    coach_number: str = field(
        default=None,
        metadata=dict(
            name="CoachNumber",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class ReviewBooking(AttrElementKeyResults):
    """
    Review Booking or Queue Minders is to add the reminders in the Provider Reservation along with the date time and Queue details. On the date time defined in reminders, the message along with the PNR goes to the desired Queue.
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Returned in response. Use it for update of saved review booking.",
        )
    )
    queue: str = field(
        default=None,
        metadata=dict(
            name="Queue",
            type="Attribute",
            help="Queue number, Must be numeric and less than 100.",
            required=True,
            max_inclusive=99.0
        )
    )
    queue_category: str = field(
        default=None,
        metadata=dict(
            name="QueueCategory",
            type="Attribute",
            help="Queue Category, 2 Character Alpha or Numeric.",
            max_length=2.0
        )
    )
    date_time: str = field(
        default=None,
        metadata=dict(
            name="DateTime",
            type="Attribute",
            help="Date and Time to place message on designated Queue, Should be prior to the last segment date in the PNR.",
            required=True
        )
    )
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            help="Input PCC optional value for placing the PNR into Queue. If not passed, will add as default PNR's Pseudo.",
            min_length=2.0,
            max_length=10.0
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="The code of the Provider (e.g 1G,1V).",
            min_length=2.0,
            max_length=5.0
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider Reservation reference. Returned in the response. Use it for update of saved Review Booking.",
        )
    )
    remarks: str = field(
        default=None,
        metadata=dict(
            name="Remarks",
            type="Attribute",
            help="Remark or reminder message. It can be truncated depending on the provider.",
            required=True,
            max_length=300.0
        )
    )


@dataclass
class SearchEvent(TypeTimeRange):
    """
    Search for various reservation events
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class SearchPassenger(TypePassengerType):
    """
    Passenger type with code and optional age information
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class SeatAssignment(AttrElementKeyResults):
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help=None,
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
            help=None,
            required=True
        )
    )
    seat_type_code: str = field(
        default=None,
        metadata=dict(
            name="SeatTypeCode",
            type="Attribute",
            help="The 4 letter SSR code like SMSW,NSSW,SMST etc.",
            length=4,
            white_space="collapse"
        )
    )
    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help=None,
        )
    )
    flight_details_ref: str = field(
        default=None,
        metadata=dict(
            name="FlightDetailsRef",
            type="Attribute",
            help=None,
        )
    )
    rail_coach_number: str = field(
        default=None,
        metadata=dict(
            name="RailCoachNumber",
            type="Attribute",
            help="Coach number for which rail seatmap/coachmap is returned.",
        )
    )


@dataclass
class Segment(AttrElementKeyResults):
    """
    The base segment type
    """

    segment_remark: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SegmentRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
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
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help="Status of this segment.",
        )
    )
    passive: str = field(
        default=None,
        metadata=dict(
            name="Passive",
            type="Attribute",
            help=None,
        )
    )
    travel_order: str = field(
        default=None,
        metadata=dict(
            name="TravelOrder",
            type="Attribute",
            help="To identify the appropriate travel sequence for Air/Car/Hotel segments/reservations based on travel dates. This ordering is applicable across the UR not provider or traveler specific",
        )
    )
    provider_segment_order: str = field(
        default=None,
        metadata=dict(
            name="ProviderSegmentOrder",
            type="Attribute",
            help="To identify the appropriate travel sequence for Air/Car/Hotel/Rail segments/reservations in the provider reservation.",
            max_inclusive=999.0
        )
    )


@dataclass
class ServiceFeeInfo(AttrElementKeyResults):
    """
    Travel Agency Service Fees (TASF) are charged by the agency through BSP or Airline Reporting Corporation (ARC).
    """

    form_of_payment: str = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help=None,
        )
    )
    service_fee_tax_info: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceFeeTaxInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    credit_card_auth: str = field(
        default=None,
        metadata=dict(
            name="CreditCardAuth",
            type="Element",
            help=None,
        )
    )
    payment: str = field(
        default=None,
        metadata=dict(
            name="Payment",
            type="Element",
            help=None,
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help="Status of the service fee. Possible Values – Issued, ReadyToIssue, IssueLater.",
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            help="The description of the service fee.",
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    confirmation: str = field(
        default=None,
        metadata=dict(
            name="Confirmation",
            type="Attribute",
            help="The confirmation number of the service fee in the merchant host system.",
        )
    )
    ticket_number: str = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            help="The ticket that this fee was issued in connection with.",
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="A reference to a passenger.",
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="A reference to the provider reservation info to which the service is tied.",
        )
    )
    passive_provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="PassiveProviderReservationInfoRef",
            type="Attribute",
            help="A reference to the passive provider reservation info to which the service is tied.",
        )
    )
    total_amount: str = field(
        default=None,
        metadata=dict(
            name="TotalAmount",
            type="Attribute",
            help="The total amount for this Service Fee including base amount and all taxes.",
        )
    )
    base_amount: str = field(
        default=None,
        metadata=dict(
            name="BaseAmount",
            type="Attribute",
            help="Represents the base price for this entity. This does not include any taxes.",
        )
    )
    taxes: str = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute",
            help="The aggregated amount of all the taxes that are associated with this entity. See the associated Service Fee TaxInfo array for a breakdown of the individual taxes.",
        )
    )
    booking_traveler_name: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerName",
            type="Attribute",
            help="The name of the passenger.",
        )
    )


@dataclass
class ServiceRuleType:
    """
    Contains the rules for applying service rules
    """

    application_rules: "ServiceRuleType.str" = field(
        default=None,
        metadata=dict(
            name="ApplicationRules",
            type="Element",
            help="The rules to apply the rule to the itinerary",
        )
    )
    application_level: "ServiceRuleType.str" = field(
        default=None,
        metadata=dict(
            name="ApplicationLevel",
            type="Element",
            help="Lists the levels where the option is applied in the itinerary. Some options are applied for the entire itinerary, some for entire segments, etc.",
        )
    )
    modify_rules: "ServiceRuleType.str" = field(
        default=None,
        metadata=dict(
            name="ModifyRules",
            type="Element",
            help="Groups the modification rules for the Option",
        )
    )
    secondary_type_rules: "ServiceRuleType.str" = field(
        default=None,
        metadata=dict(
            name="SecondaryTypeRules",
            type="Element",
            help="Lists the supported Secondary Codes for the optional / additional service.",
        )
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Remarks",
            type="Element",
            help="Adds text remarks / rules for the optional / additional service",
            min_occurs=0,
            max_occurs=99
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Unique ID to identify an optional service rule",
            required=True
        )
    )

    @dataclass
    class ApplicationRules:
        required_for_all_travelers: str = field(
            default=None,
            metadata=dict(
                name="RequiredForAllTravelers",
                type="Attribute",
                help="Indicates if the option needs to be applied to all travelers in the itinerary if selected",
            )
        )
        required_for_all_segments: str = field(
            default=None,
            metadata=dict(
                name="RequiredForAllSegments",
                type="Attribute",
                help="Indicates if the option needs to be applied to all segments in the itinerary if selected",
            )
        )
        required_for_all_segments_in_od: str = field(
            default=None,
            metadata=dict(
                name="RequiredForAllSegmentsInOD",
                type="Attribute",
                help="Indicates if the option needs to be applied to all segments in a origin / destination (connection flights) if selected for one segment in the OD",
            )
        )
        unselected_option_required: str = field(
            default=None,
            metadata=dict(
                name="UnselectedOptionRequired",
                type="Attribute",
                help="If an UnselectedOption is present in the option, then the Unselected option needs to be selected even if the option is not selected when this flag is set to true",
            )
        )
        secondary_option_code_required: str = field(
            default=None,
            metadata=dict(
                name="SecondaryOptionCodeRequired",
                type="Attribute",
                help="If set to true, the secondary option code is required for this option",
            )
        )

    @dataclass
    class ApplicationLevel:
        application_limits: "ServiceRuleType.ApplicationLevel.str" = field(
            default=None,
            metadata=dict(
                name="ApplicationLimits",
                type="Element",
                help="Adds the limits on the number of options that can be selected for a particular type",
            )
        )
        service_data: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ServiceData",
                type="Element",
                help=None,
                min_occurs=0,
                max_occurs=999
            )
        )
        applicable_levels: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ApplicableLevels",
                type="Attribute",
                help="Indicates the level in the itinerary when the option is applied.",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        provider_defined_applicable_levels: str = field(
            default=None,
            metadata=dict(
                name="ProviderDefinedApplicableLevels",
                type="Attribute",
                help="Indicates the actual provider defined ApplicableLevels which is mapped to Other",
            )
        )

        @dataclass
        class ApplicationLimits:
            application_limit: List[str] = field(
                default_factory=list,
                metadata=dict(
                    name="ApplicationLimit",
                    type="Element",
                    help="The application limits for a particular level",
                    min_occurs=1,
                    max_occurs=10
                )
            )

    @dataclass
    class ModifyRules:
        modify_rule: List["ServiceRuleType.ModifyRules.str"] = field(
            default_factory=list,
            metadata=dict(
                name="ModifyRule",
                type="Element",
                help="Indicates modification rules for the particular modification type.",
                min_occurs=1,
                max_occurs=999
            )
        )
        supported_modifications: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="SupportedModifications",
                type="Attribute",
                help="Lists the supported modifications for the itinerary.",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        provider_defined_modification_type: str = field(
            default=None,
            metadata=dict(
                name="ProviderDefinedModificationType",
                type="Attribute",
                help="Indicates the actual provider defined modification type which is mapped to Other",
            )
        )

        @dataclass
        class ModifyRule(ModificationRulesGroup):
            pass

    @dataclass
    class SecondaryTypeRules:
        secondary_type_rule: List["ServiceRuleType.SecondaryTypeRules.str"] = field(
            default_factory=list,
            metadata=dict(
                name="SecondaryTypeRule",
                type="Element",
                help="Lists a single secondary code for the optional / additional service.",
                min_occurs=1,
                max_occurs=999
            )
        )

        @dataclass
        class SecondaryTypeRule:
            application_limit: List[str] = field(
                default_factory=list,
                metadata=dict(
                    name="ApplicationLimit",
                    type="Element",
                    help=None,
                    min_occurs=0,
                    max_occurs=10
                )
            )
            secondary_type: str = field(
                default=None,
                metadata=dict(
                    name="SecondaryType",
                    type="Attribute",
                    help="The unique type to associate a secondary type in an optional service",
                    required=True
                )
            )


@dataclass
class SpecialEquipment(AttrElementKeyResults):
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Special equipment associated with a specific vehicle",
            required=True
        )
    )


@dataclass
class Ssr(AttrElementKeyResults):
    """
    Special serivces like wheel chair, or pet carrier.
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help="Reference to the air segment. May be required for some Types.",
        )
    )
    passive_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="PassiveSegmentRef",
            type="Attribute",
            help="Reference to the passive segment.",
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Programmatic SSRs use codes recognized by the provider/supplier (example, VGML=vegetarian meal code). Manual SSRs do not have an associated programmatic code.",
            required=True,
            min_length=4.0,
            max_length=4.0
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help=None,
        )
    )
    free_text: str = field(
        default=None,
        metadata=dict(
            name="FreeText",
            type="Attribute",
            help="Certain SSR types will require a free text message. For example MAAS (Meet and assist).",
        )
    )
    carrier: str = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help=None,
            length=2
        )
    )
    carrier_specific_text: str = field(
        default=None,
        metadata=dict(
            name="CarrierSpecificText",
            type="Attribute",
            help="Carrier specific information which are not captured in the FreeText field(not present in IATA's standard SSR DOCO format). An example is VISA Expiration Date.",
            min_length=1.0,
            max_length=64.0
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            help=None,
        )
    )
    provider_defined_type: str = field(
        default=None,
        metadata=dict(
            name="ProviderDefinedType",
            type="Attribute",
            help="Original Type as sent by the provider",
            min_length=1.0,
            max_length=16.0
        )
    )
    ssrrule_ref: str = field(
        default=None,
        metadata=dict(
            name="SSRRuleRef",
            type="Attribute",
            help="UniqueID to associate a rule to the SSR",
        )
    )
    url: str = field(
        default=None,
        metadata=dict(
            name="URL",
            type="Attribute",
            help=None,
        )
    )
    profile_id: str = field(
        default=None,
        metadata=dict(
            name="ProfileID",
            type="Attribute",
            help="Key assigned for Secure Flight Document value from the specified profile",
        )
    )
    profile_secure_flight_doc_key: str = field(
        default=None,
        metadata=dict(
            name="ProfileSecureFlightDocKey",
            type="Attribute",
            help="Unique ID of Booking Traveler's Profile that contains the Secure flight Detail",
        )
    )


@dataclass
class TaxDetail(AttrTaxDetail):
    """
    The tax idetail nformation for a fare quote tax.
    """

    pass


@dataclass
class ThirdPartyInformation(AttrElementKeyResults):
    """
    Third party supplier locator information. Specifically applicable for SDK booking.
    """

    segment_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SegmentRef",
            type="Element",
            help="Air/Passive Segment Reference",
            min_occurs=0,
            max_occurs=999
        )
    )
    third_party_code: str = field(
        default=None,
        metadata=dict(
            name="ThirdPartyCode",
            type="Attribute",
            help="Third party supplier code.",
            min_length=2.0,
            max_length=5.0
        )
    )
    third_party_locator_code: str = field(
        default=None,
        metadata=dict(
            name="ThirdPartyLocatorCode",
            type="Attribute",
            help="Confirmation number for third party supplier.",
            max_length=36.0
        )
    )
    third_party_name: str = field(
        default=None,
        metadata=dict(
            name="ThirdPartyName",
            type="Attribute",
            help="Third party supplier name.",
            max_length=64.0
        )
    )
    provider_reservation_info_ref: str = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider Reservation reference",
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Unique identifier of the third party supplier. Key can be used to modify or delete saved third party information.",
        )
    )


@dataclass
class TravelComplianceData(AttrElementKeyResults):
    """
    Travel Compliance and Preferred Supplier information of the traveler specific to a segment.
    """

    policy_compliance: List["TravelComplianceData.str"] = field(
        default_factory=list,
        metadata=dict(
            name="PolicyCompliance",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=2
        )
    )
    contract_compliance: List["TravelComplianceData.str"] = field(
        default_factory=list,
        metadata=dict(
            name="ContractCompliance",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=2
        )
    )
    preferred_supplier: List["TravelComplianceData.str"] = field(
        default_factory=list,
        metadata=dict(
            name="PreferredSupplier",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="System generated key, returned back in the response. This can be used to modify or delete a saved TravelComplianceData.",
        )
    )
    air_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Attribute",
            help="Refers to Air Segment. Applicable only for Air. Ignored for others.",
        )
    )
    passive_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="PassiveSegmentRef",
            type="Attribute",
            help="Refers to Passive Segment. Applicable only for Passive. Ignored for others.",
        )
    )
    rail_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="RailSegmentRef",
            type="Attribute",
            help="Refers to Rail Segment. Applicable only for Rail. Ignored for others.",
        )
    )
    reservation_locator_ref: str = field(
        default=None,
        metadata=dict(
            name="ReservationLocatorRef",
            type="Attribute",
            help="This is returned in the response. Any input will be ignored for this attribute. This represents the association of Travel Compliance Data with the uAPI reservation locator code, mainly relevant to Hotel and Vehicle.",
            min_length=5.0,
            max_length=8.0
        )
    )

    @dataclass
    class PolicyCompliance:
        in_policy: str = field(
            default=None,
            metadata=dict(
                name="InPolicy",
                type="Attribute",
                help="Policy Compliance Indicator. For In-Policy set to 'true', For Out-Of-Policy set to 'false''.",
                required=True
            )
        )
        policy_token: str = field(
            default=None,
            metadata=dict(
                name="PolicyToken",
                type="Attribute",
                help="Optional text message to set the rule or token for which it's In Policy or Out Of Policy.",
                min_length=1.0,
                max_length=128.0
            )
        )

    @dataclass
    class ContractCompliance:
        in_contract: str = field(
            default=None,
            metadata=dict(
                name="InContract",
                type="Attribute",
                help="Contract Compliance Indicator. For In-Contract set to 'true', For Out-Of-Contract set to 'false'.",
                required=True
            )
        )
        contract_token: str = field(
            default=None,
            metadata=dict(
                name="ContractToken",
                type="Attribute",
                help="Optional text message to set the rule or token for which it's In Contract or Out Of Contract.",
                min_length=1.0,
                max_length=128.0
            )
        )

    @dataclass
    class PreferredSupplier:
        preferred: str = field(
            default=None,
            metadata=dict(
                name="Preferred",
                type="Attribute",
                help="Preferred Supplier - 'true', 'false'.",
                required=True
            )
        )
        profile_type: str = field(
            default=None,
            metadata=dict(
                name="ProfileType",
                type="Attribute",
                help="Indicate profile type. e.g. if Agency Preferred then pass Agency, if Traveler Preferred then pass Traveler.",
                required=True
            )
        )


@dataclass
class TypeAgencyHierarchyLongReference(TypeAgencyHierarchyReference):
    profile_version: str = field(
        default=None,
        metadata=dict(
            name="ProfileVersion",
            type="Attribute",
            help=None,
            required=True
        )
    )
    profile_name: str = field(
        default=None,
        metadata=dict(
            name="ProfileName",
            type="Attribute",
            help="Initially: Agent: Last, First, Branch: BranchCode, Agency: Name. After new profile implementation: Agent: UserName, others levels: Name.",
            required=True,
            max_length=102.0
        )
    )


@dataclass
class TypeAssociatedRemark(TypeRemarkWithTravelerRef):
    """
    A textual remark container to hold Associated itinerary remarks
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class TypeCreditCardType(TypePaymentCard):
    extended_payment: str = field(
        default=None,
        metadata=dict(
            name="ExtendedPayment",
            type="Attribute",
            help="Used for American Express cards.",
        )
    )
    customer_reference: str = field(
        default=None,
        metadata=dict(
            name="CustomerReference",
            type="Attribute",
            help="Agencies use this to pass the traveler information to the credit card company.",
        )
    )
    acceptance_override: str = field(
        default=None,
        metadata=dict(
            name="AcceptanceOverride",
            type="Attribute",
            help="Override airline restriction on the credit card.",
        )
    )
    third_party_payment: str = field(
        default="false",
        metadata=dict(
            name="ThirdPartyPayment",
            type="Attribute",
            help="If true, this indicates that the credit card holder is not one of the passengers.",
        )
    )
    bank_name: str = field(
        default=None,
        metadata=dict(
            name="BankName",
            type="Attribute",
            help="Issuing bank name for this credit card",
        )
    )
    bank_country_code: str = field(
        default=None,
        metadata=dict(
            name="BankCountryCode",
            type="Attribute",
            help="ISO Country code associated with the issuing bank",
            length=2
        )
    )
    bank_state_code: str = field(
        default=None,
        metadata=dict(
            name="BankStateCode",
            type="Attribute",
            help="State code associated with the issuing bank.",
            max_length=6.0
        )
    )
    enett: str = field(
        default="false",
        metadata=dict(
            name="Enett",
            type="Attribute",
            help="Acceptable values are true or false. If set to true it will denote that the credit card used has been issued through Enett. For all other credit card payments this value will be set to false.",
        )
    )


@dataclass
class TypeFeeInfo(AttrProviderSupplier, AttrElementKeyResults):
    """
    A generic type of fee for those charges which are incurred by the passenger, but not necessarily shown on tickets
    """

    tax_info_ref: List["TypeFeeInfo.str"] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfoRef",
            type="Element",
            help="This reference elements will associate relevant taxes to this fee",
            min_occurs=0,
            max_occurs=999
        )
    )
    included_in_base: str = field(
        default=None,
        metadata=dict(
            name="IncludedInBase",
            type="Element",
            help=None,
        )
    )
    base_amount: str = field(
        default=None,
        metadata=dict(
            name="BaseAmount",
            type="Attribute",
            help=None,
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            help=None,
        )
    )
    sub_code: str = field(
        default=None,
        metadata=dict(
            name="SubCode",
            type="Attribute",
            help=None,
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
    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
            required=True
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True
        )
    )
    fee_token: str = field(
        default=None,
        metadata=dict(
            name="FeeToken",
            type="Attribute",
            help=None,
        )
    )
    payment_ref: str = field(
        default=None,
        metadata=dict(
            name="PaymentRef",
            type="Attribute",
            help="The reference to the one of the air reservation payments if fee included in charge",
        )
    )
    booking_traveler_ref: str = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="Reference to booking traveler",
        )
    )
    passenger_type_code: str = field(
        default=None,
        metadata=dict(
            name="PassengerTypeCode",
            type="Attribute",
            help=None,
            min_length=3.0,
            max_length=5.0
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            help="Additional Information returned from Supplier.(ACH only)",
            min_length=1.0,
            max_length=64.0
        )
    )

    @dataclass
    class TaxInfoRef:
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
class TypeFlexibleTimeSpec(TypeTimeSpec):
    """
    A type which can be used for flexible date/time specification -extends the generic type typeTimeSpec to provide extra options for search.
    """

    search_extra_days: "TypeFlexibleTimeSpec.str" = field(
        default=None,
        metadata=dict(
            name="SearchExtraDays",
            type="Element",
            help="Options to search for extra days on top of the specified date",
        )
    )

    @dataclass
    class SearchExtraDays:
        days_before: str = field(
            default=None,
            metadata=dict(
                name="DaysBefore",
                type="Attribute",
                help="Number of days to search before the specified date",
            )
        )
        days_after: str = field(
            default=None,
            metadata=dict(
                name="DaysAfter",
                type="Attribute",
                help="Number of days to search after the specified date",
            )
        )


@dataclass
class TypeProviderReservationDetail(ProviderReservation):
    """
    Details of a provider reservation locator consisting of provider locator code and provider code. To be used as a request element type while accessing a specific PNR
    """

    pass


@dataclass
class TypeStructuredAddress(AttrElementKeyResults):
    """
    A fully structured address
    """

    address_name: str = field(
        default=None,
        metadata=dict(
            name="AddressName",
            type="Element",
            help=None,
            max_length=128.0
        )
    )
    street: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Street",
            type="Element",
            help="The Address street and number, e.g. 105 Main St.",
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
            help="The city name for the requested address, e.g. Atlanta.",
            min_length=2.0,
            max_length=50.0
        )
    )
    state: str = field(
        default=None,
        metadata=dict(
            name="State",
            type="Element",
            help="The State or Province of address requested, e.g. CA, Ontario.",
        )
    )
    postal_code: str = field(
        default=None,
        metadata=dict(
            name="PostalCode",
            type="Element",
            help="The 5-15 alphanumeric postal Code for the requested address, e.g. 90210.",
            min_length=1.0,
            max_length=15.0
        )
    )
    country: str = field(
        default=None,
        metadata=dict(
            name="Country",
            type="Element",
            help="The Full country name or two letter ISO country code e.g. US, France. A two letter country code is required for a Postal Code Searches.",
            length=2
        )
    )
    provider_reservation_info_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            help="Tagging provider reservation info with Address.",
            min_occurs=0,
            max_occurs=99
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Key for update/delete of the element",
        )
    )


@dataclass
class TypeTaxInfo(AttrTaxDetail):
    tax_detail: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TaxDetail",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    included_in_base: str = field(
        default=None,
        metadata=dict(
            name="IncludedInBase",
            type="Element",
            help=None,
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="The tax key represents a valid key of tax",
        )
    )
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="The tax category represents a valid IATA tax code.",
            required=True
        )
    )
    carrier_defined_category: str = field(
        default=None,
        metadata=dict(
            name="CarrierDefinedCategory",
            type="Attribute",
            help="Optional category, where a carrier has used a non-standard IATA tax category. The tax category will be set to 'DU'",
        )
    )
    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help="The segment to which that tax is relative (if applicable)",
        )
    )
    flight_details_ref: str = field(
        default=None,
        metadata=dict(
            name="FlightDetailsRef",
            type="Attribute",
            help="The flight details that this tax is relative to (if applicable)",
        )
    )
    coupon_ref: str = field(
        default=None,
        metadata=dict(
            name="CouponRef",
            type="Attribute",
            help="The coupon to which that tax is relative (if applicable)",
        )
    )
    tax_exempted: str = field(
        default=None,
        metadata=dict(
            name="TaxExempted",
            type="Attribute",
            help="This indicates whether the tax specified by tax category is exempted.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Code of the provider returning this TaxInfo.",
            min_length=2.0,
            max_length=5.0
        )
    )
    supplier_code: str = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help="Code of the supplier returning this TaxInfo.",
            min_length=1.0,
            max_length=5.0
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            help="Additional Information returned from Supplier.(ACH only)",
            min_length=1.0,
            max_length=128.0
        )
    )


@dataclass
class TypeTransactionsAllowed(TypeBookingTransactionsAllowed):
    shopping_enabled: str = field(
        default=None,
        metadata=dict(
            name="ShoppingEnabled",
            type="Attribute",
            help="Allow or prohibit shopping transaction for the given product type on this Provider/Supplier. Inheritable.",
        )
    )
    pricing_enabled: str = field(
        default=None,
        metadata=dict(
            name="PricingEnabled",
            type="Attribute",
            help="Allow or prohibit pricing transaction for the given product type on this Provider/Supplier. Inheritable.",
        )
    )


@dataclass
class UnassociatedRemark(TypeRemarkWithTravelerRef):
    """
    A textual remark container to hold non-associated itinerary remarks
    """

    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class VendorLocation(TypeVendorLocation):
    """
    Location definition specific to a Vendor in a specific provider (e.g. 1G) system.
    """

    pass


@dataclass
class AirSeatAssignment(SeatAssignment):
    """
    Identifies the seat assignment for a passenger.
    """

    pass


@dataclass
class CreditCard(TypeCreditCardType):
    """
    Container for all credit card information.
    """

    pass


@dataclass
class DeliveryInfo:
    """
    Container to encapsulate all delivery related information
    """

    shipping_address: "DeliveryInfo.str" = field(
        default=None,
        metadata=dict(
            name="ShippingAddress",
            type="Element",
            help=None,
        )
    )
    phone_number: str = field(
        default=None,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            help=None,
        )
    )
    email: str = field(
        default=None,
        metadata=dict(
            name="Email",
            type="Element",
            help=None,
        )
    )
    general_remark: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="GeneralRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            help="Tagging provider reservation info with Delivery Info.",
            min_occurs=0,
            max_occurs=999
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="An arbitrary identifier to categorize this delivery info",
        )
    )
    signature_required: str = field(
        default=None,
        metadata=dict(
            name="SignatureRequired",
            type="Attribute",
            help="Indicates whether a signature shoud be required in order to make the delivery.",
            max_length=10.0
        )
    )
    tracking_number: str = field(
        default=None,
        metadata=dict(
            name="TrackingNumber",
            type="Attribute",
            help="The tracking number of the shipping company making the delivery.",
        )
    )

    @dataclass
    class ShippingAddress(TypeStructuredAddress):
        pass


@dataclass
class InvoiceRemark(TypeAssociatedRemark):
    air_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            help="Reference to AirSegment from an Air Reservation.",
        )
    )
    hotel_reservation_ref: str = field(
        default=None,
        metadata=dict(
            name="HotelReservationRef",
            type="Element",
            help="Specify the locator code of Hotel reservation.",
        )
    )
    vehicle_reservation_ref: str = field(
        default=None,
        metadata=dict(
            name="VehicleReservationRef",
            type="Element",
            help="Specify the locator code of Vehicle reservation.",
        )
    )
    passive_segment_ref: str = field(
        default=None,
        metadata=dict(
            name="PassiveSegmentRef",
            type="Element",
            help="Reference to PassiveSegment from a Passive Reservation.",
        )
    )


@dataclass
class LocationAddress(TypeStructuredAddress):
    pass


@dataclass
class ProviderReservationDetail(TypeProviderReservationDetail):
    """
    common element for mentioning provider reservation locator (PNR) details in request.
    """

    pass


@dataclass
class TransactionType:
    """
    Configuration for products by type. Inheritable.
    """

    air: "TransactionType.str" = field(
        default=None,
        metadata=dict(
            name="Air",
            type="Element",
            help=None,
        )
    )
    hotel: str = field(
        default=None,
        metadata=dict(
            name="Hotel",
            type="Element",
            help=None,
        )
    )
    rail: str = field(
        default=None,
        metadata=dict(
            name="Rail",
            type="Element",
            help=None,
        )
    )
    vehicle: str = field(
        default=None,
        metadata=dict(
            name="Vehicle",
            type="Element",
            help=None,
        )
    )
    passive: str = field(
        default=None,
        metadata=dict(
            name="Passive",
            type="Element",
            help="For true passive segments such as ground, cruise etc",
        )
    )
    background_passive: str = field(
        default=None,
        metadata=dict(
            name="BackgroundPassive",
            type="Element",
            help="For behind the scenes or background passives Only",
        )
    )

    @dataclass
    class Air(TypeTransactionsAllowed):
        one_way_shop: str = field(
            default=None,
            metadata=dict(
                name="OneWayShop",
                type="Attribute",
                help="Allows or prohibits one way shopping functionality for the associated provisioning provider configuration",
            )
        )
        flex_explore: str = field(
            default=None,
            metadata=dict(
                name="FlexExplore",
                type="Attribute",
                help="Allows or prohibits flex explore functionality for the associated provisioning provider configuration",
            )
        )
        rapid_reprice_enabled: str = field(
            default=None,
            metadata=dict(
                name="RapidRepriceEnabled",
                type="Attribute",
                help="Allows or prohibits rapid reprice functionality for the associated provisioning provider configuration. Providers: 1G/1V",
            )
        )
        return_upsell_fare: str = field(
            default=None,
            metadata=dict(
                name="ReturnUpsellFare",
                type="Attribute",
                help="When set to “true”, Upsell information will be returned in the shop response. Provider: 1G, 1V, 1P, 1J, ACH",
            )
        )


@dataclass
class TravelSegment(Segment):
    """
    Generic segment used to provide travel information that was not processed by the system
    """

    origin: str = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="The IATA location code for this origination of this entity.",
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
            length=3,
            white_space="collapse"
        )
    )
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            help="The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class TypeAssociatedRemarkWithSegmentRef(TypeAssociatedRemark):
    """
    A textual remark container to hold Associated itinerary remarks with segment association
    """

    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help="Reference to an Air/Passive Segment",
        )
    )