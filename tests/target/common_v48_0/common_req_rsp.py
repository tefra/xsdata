from dataclasses import dataclass, field
from typing import List

from .common import *


@dataclass
class BaseRsp:
    """
    The base type for all responses.
    """

    response_message: List[ResponseMessage] = field(
        default_factory=list,
        metadata=dict(
            name="ResponseMessage",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    trace_id: str = field(
        default=None,
        metadata=dict(
            name="TraceId",
            type="Attribute",
            help="Unique identifier for this atomic transaction traced by the user. Use is optional.",
        )
    )
    transaction_id: str = field(
        default=None,
        metadata=dict(
            name="TransactionId",
            type="Attribute",
            help="System generated unique identifier for this atomic transaction.",
        )
    )
    response_time: int = field(
        default=None,
        metadata=dict(
            name="ResponseTime",
            type="Attribute",
            help="The time (in ms) the system spent processing this request, not including transmission times.",
        )
    )
    command_history: str = field(
        default=None,
        metadata=dict(
            name="CommandHistory",
            type="Attribute",
            help="HTTP link to download command history and debugging information of the request that generated this response. Must be enabled on the system.",
        )
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
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class BaseCoreReq:
    billing_point_of_sale_info: BillingPointOfSaleInfo = field(
        default=None,
        metadata=dict(
            name="BillingPointOfSaleInfo",
            type="Element",
            help=None,
            required=True
        )
    )
    agent_idoverride: List[AgentIdoverride] = field(
        default_factory=list,
        metadata=dict(
            name="AgentIDOverride",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    terminal_session_info: TerminalSessionInfo = field(
        default=None,
        metadata=dict(
            name="TerminalSessionInfo",
            type="Element",
            help=None,
        )
    )
    trace_id: str = field(
        default=None,
        metadata=dict(
            name="TraceId",
            type="Attribute",
            help="Unique identifier for this atomic transaction traced by the user. Use is optional.",
        )
    )
    token_id: str = field(
        default=None,
        metadata=dict(
            name="TokenId",
            type="Attribute",
            help="Authentication Token ID used when running in statefull operation. Obtained from the LoginRsp. Use is optional.",
        )
    )
    authorized_by: str = field(
        default=None,
        metadata=dict(
            name="AuthorizedBy",
            type="Attribute",
            help="Used in showing who authorized the request. Use is optional.",
        )
    )
    target_branch: TypeBranchCode = field(
        default=None,
        metadata=dict(
            name="TargetBranch",
            type="Attribute",
            help="Used for Emulation - If authorised will execute the request as if the agent's parent branch is the TargetBranch specified.",
        )
    )
    override_logging: TypeLoggingLevel = field(
        default=None,
        metadata=dict(
            name="OverrideLogging",
            type="Attribute",
            help="Use to override the default logging level",
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
class BaseSearchRsp(BaseRsp):
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata=dict(
            name="NextResultReference",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class BaseCoreSearchReq(BaseCoreReq):
    """
    Base Request for Air Search
    """

    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata=dict(
            name="NextResultReference",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class BaseReq(BaseCoreReq):
    override_pcc: OverridePcc = field(
        default=None,
        metadata=dict(
            name="OverridePCC",
            type="Element",
            help=None,
        )
    )
    retrieve_provider_reservation_details: bool = field(
        default="false",
        metadata=dict(
            name="RetrieveProviderReservationDetails",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class BaseCreateReservationReq(BaseReq):
    linked_universal_record: List[LinkedUniversalRecord] = field(
        default_factory=list,
        metadata=dict(
            name="LinkedUniversalRecord",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTraveler",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    osi: List[Osi] = field(
        default_factory=list,
        metadata=dict(
            name="OSI",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata=dict(
            name="AccountingRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata=dict(
            name="GeneralRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    xmlremark: List[Xmlremark] = field(
        default_factory=list,
        metadata=dict(
            name="XMLRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    unassociated_remark: List[UnassociatedRemark] = field(
        default_factory=list,
        metadata=dict(
            name="UnassociatedRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    postscript: Postscript = field(
        default=None,
        metadata=dict(
            name="Postscript",
            type="Element",
            help=None,
        )
    )
    passive_info: PassiveInfo = field(
        default=None,
        metadata=dict(
            name="PassiveInfo",
            type="Element",
            help=None,
        )
    )
    continuity_check_override: ContinuityCheckOverride = field(
        default=None,
        metadata=dict(
            name="ContinuityCheckOverride",
            type="Element",
            help="This element will be used if user wants to override segment continuity check.",
        )
    )
    agency_contact_info: AgencyContactInfo = field(
        default=None,
        metadata=dict(
            name="AgencyContactInfo",
            type="Element",
            help=None,
        )
    )
    customer_id: CustomerId = field(
        default=None,
        metadata=dict(
            name="CustomerID",
            type="Element",
            help=None,
        )
    )
    file_finishing_info: FileFinishingInfo = field(
        default=None,
        metadata=dict(
            name="FileFinishingInfo",
            type="Element",
            help=None,
        )
    )
    commission_remark: CommissionRemark = field(
        default=None,
        metadata=dict(
            name="CommissionRemark",
            type="Element",
            help=None,
        )
    )
    consolidator_remark: ConsolidatorRemark = field(
        default=None,
        metadata=dict(
            name="ConsolidatorRemark",
            type="Element",
            help=None,
        )
    )
    invoice_remark: List[InvoiceRemark] = field(
        default_factory=list,
        metadata=dict(
            name="InvoiceRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata=dict(
            name="SSR",
            type="Element",
            help="SSR element outside Booking Traveler without any Segment Ref or Booking Traveler Ref.",
            min_occurs=0,
            max_occurs=999
        )
    )
    email_notification: EmailNotification = field(
        default=None,
        metadata=dict(
            name="EmailNotification",
            type="Element",
            help=None,
        )
    )
    queue_place: QueuePlace = field(
        default=None,
        metadata=dict(
            name="QueuePlace",
            type="Element",
            help="Allow queue placement of a PNR at the time of booking in AirCreateReservationReq,HotelCreateReservationReq,PassiveCreateReservationReq and VehicleCreateReservationReq for providers 1G,1V,1P and 1J.",
        )
    )
    rule_name: str = field(
        default=None,
        metadata=dict(
            name="RuleName",
            type="Attribute",
            help="This attribute is meant to attach a mandatory custom check rule name to a PNR. A non-mandatory custom check rule too can be attached to a PNR.",
            max_length=10.0
        )
    )
    universal_record_locator_code: TypeLocatorCode = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            help="Which UniversalRecord should this new reservation be applied to. If blank, then a new one is created.",
        )
    )
    provider_locator_code: TypeLocatorCode = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            help="Which Provider reservation does this reservation get added to.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="To be used with ProviderLocatorCode, which host the reservation being added to belongs to.",
        )
    )
    customer_number: str = field(
        default=None,
        metadata=dict(
            name="CustomerNumber",
            type="Attribute",
            help="Optional client centric customer identifier",
        )
    )
    version: int = field(
        default=None,
        metadata=dict(
            name="Version",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class BaseSearchReq(BaseReq):
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata=dict(
            name="NextResultReference",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class BaseCreateWithFormOfPaymentReq(BaseCreateReservationReq):
    """
    Container for BaseCreateReservation along with Form Of Payment
    """

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help="Provider:1G,1V,1P,1J,ACH,SDK.",
            min_occurs=0,
            max_occurs=999
        )
    )