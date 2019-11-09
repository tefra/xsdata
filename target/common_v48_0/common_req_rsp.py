from dataclasses import dataclass, field
from typing import List


@dataclass
class BaseRsp:
    """
    The base type for all responses.
    """

    response_message: List[ResponseMessage] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "ResponseMessage",
            "type": "Element",
        },
    )
    trace_id: str = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Attribute",
            "help": "Unique identifier for this atomic transaction traced by the user. Use is optional.",
        },
    )
    transaction_id: str = field(
        default=None,
        metadata={
            "name": "TransactionId",
            "type": "Attribute",
            "help": "System generated unique identifier for this atomic transaction.",
        },
    )
    response_time: int = field(
        default=None,
        metadata={
            "name": "ResponseTime",
            "type": "Attribute",
            "help": "The time (in ms) the system spent processing this request, not including transmission times.",
        },
    )
    command_history: str = field(
        default=None,
        metadata={
            "name": "CommandHistory",
            "type": "Attribute",
            "help": "HTTP link to download command history and debugging information of the request that generated this response. Must be enabled on the system.",
        },
    )


@dataclass
class ErrorInfo(TypeErrorInfo):
    """
    Container for error data when there is an application error.
    """

    pass


@dataclass
class TypeLoggingLevel:
    """
    The type of various Logging levels
    """

    value: str = field(
        default=None, metadata={"name": "value", "type": "Restriction"}
    )


@dataclass
class BaseCoreReq:
    billing_point_of_sale_info: BillingPointOfSaleInfo = field(
        default=None,
        metadata={
            "required": True,
            "name": "BillingPointOfSaleInfo",
            "type": "Element",
        },
    )
    agent_idoverride: List[AgentIdoverride] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AgentIDOverride",
            "type": "Element",
        },
    )
    terminal_session_info: TerminalSessionInfo = field(
        default=None,
        metadata={"name": "TerminalSessionInfo", "type": "Element"},
    )
    trace_id: str = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Attribute",
            "help": "Unique identifier for this atomic transaction traced by the user. Use is optional.",
        },
    )
    token_id: str = field(
        default=None,
        metadata={
            "name": "TokenId",
            "type": "Attribute",
            "help": "Authentication Token ID used when running in statefull operation. Obtained from the LoginRsp. Use is optional.",
        },
    )
    authorized_by: str = field(
        default=None,
        metadata={
            "name": "AuthorizedBy",
            "type": "Attribute",
            "help": "Used in showing who authorized the request. Use is optional.",
        },
    )
    target_branch: TypeBranchCode = field(
        default=None,
        metadata={
            "name": "TargetBranch",
            "type": "Attribute",
            "help": "Used for Emulation - If authorised will execute the request as if the agent's parent branch is the TargetBranch specified.",
        },
    )
    override_logging: TypeLoggingLevel = field(
        default=None,
        metadata={
            "name": "OverrideLogging",
            "type": "Attribute",
            "help": "Use to override the default logging level",
        },
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
class BaseSearchRsp(BaseRsp):
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "NextResultReference",
            "type": "Element",
        },
    )


@dataclass
class BaseCoreSearchReq(BaseCoreReq):
    """
    Base Request for Air Search
    """

    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "NextResultReference",
            "type": "Element",
        },
    )


@dataclass
class BaseReq(BaseCoreReq):
    override_pcc: OverridePcc = field(
        default=None, metadata={"name": "OverridePCC", "type": "Element"}
    )
    retrieve_provider_reservation_details: bool = field(
        default=false,
        metadata={
            "name": "RetrieveProviderReservationDetails",
            "type": "Attribute",
        },
    )


@dataclass
class BaseCreateReservationReq(BaseReq):
    linked_universal_record: List[LinkedUniversalRecord] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "LinkedUniversalRecord",
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
        },
    )
    osi: List[Osi] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "OSI",
            "type": "Element",
        },
    )
    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "AccountingRemark",
            "type": "Element",
        },
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "GeneralRemark",
            "type": "Element",
        },
    )
    xmlremark: List[Xmlremark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "XMLRemark",
            "type": "Element",
        },
    )
    unassociated_remark: List[UnassociatedRemark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "UnassociatedRemark",
            "type": "Element",
        },
    )
    postscript: Postscript = field(
        default=None, metadata={"name": "Postscript", "type": "Element"}
    )
    passive_info: PassiveInfo = field(
        default=None, metadata={"name": "PassiveInfo", "type": "Element"}
    )
    continuity_check_override: ContinuityCheckOverride = field(
        default=None,
        metadata={
            "name": "ContinuityCheckOverride",
            "type": "Element",
            "help": "This element will be used if user wants to override segment continuity check.",
        },
    )
    agency_contact_info: AgencyContactInfo = field(
        default=None, metadata={"name": "AgencyContactInfo", "type": "Element"}
    )
    customer_id: CustomerId = field(
        default=None, metadata={"name": "CustomerID", "type": "Element"}
    )
    file_finishing_info: FileFinishingInfo = field(
        default=None, metadata={"name": "FileFinishingInfo", "type": "Element"}
    )
    commission_remark: CommissionRemark = field(
        default=None, metadata={"name": "CommissionRemark", "type": "Element"}
    )
    consolidator_remark: ConsolidatorRemark = field(
        default=None,
        metadata={"name": "ConsolidatorRemark", "type": "Element"},
    )
    invoice_remark: List[InvoiceRemark] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "InvoiceRemark",
            "type": "Element",
        },
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "SSR",
            "type": "Element",
            "help": "SSR element outside Booking Traveler without any Segment Ref or Booking Traveler Ref.",
        },
    )
    email_notification: EmailNotification = field(
        default=None, metadata={"name": "EmailNotification", "type": "Element"}
    )
    queue_place: QueuePlace = field(
        default=None,
        metadata={
            "name": "QueuePlace",
            "type": "Element",
            "help": "Allow queue placement of a PNR at the time of booking in AirCreateReservationReq,HotelCreateReservationReq,PassiveCreateReservationReq and VehicleCreateReservationReq for providers 1G,1V,1P and 1J.",
        },
    )
    rule_name: str = field(
        default=None,
        metadata={
            "name": "RuleName",
            "type": "Attribute",
            "help": "This attribute is meant to attach a mandatory custom check rule name to a PNR. A non-mandatory custom check rule too can be attached to a PNR.",
        },
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
    customer_number: str = field(
        default=None,
        metadata={
            "name": "CustomerNumber",
            "type": "Attribute",
            "help": "Optional client centric customer identifier",
        },
    )
    version: int = field(
        default=None, metadata={"name": "Version", "type": "Attribute"}
    )


@dataclass
class BaseSearchReq(BaseReq):
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "NextResultReference",
            "type": "Element",
        },
    )


@dataclass
class BaseCreateWithFormOfPaymentReq(BaseCreateReservationReq):
    """
    Container for BaseCreateReservation along with Form Of Payment
    """

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "min_occurs": 0,
            "max_occurs": 999,
            "name": "FormOfPayment",
            "type": "Element",
            "help": "Provider:1G,1V,1P,1J,ACH,SDK.",
        },
    )
