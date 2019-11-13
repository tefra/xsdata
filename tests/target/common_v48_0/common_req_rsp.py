from dataclasses import dataclass, field
from typing import List

from .common import *


@dataclass
class BaseCoreReq:
    """
    :ivar billing_point_of_sale_info:
    :ivar agent_idoverride:
    :ivar terminal_session_info:
    :ivar trace_id: Unique identifier for this atomic transaction traced by the user. Use is optional.
    :ivar token_id: Authentication Token ID used when running in statefull operation. Obtained from the LoginRsp. Use is optional.
    :ivar authorized_by: Used in showing who authorized the request. Use is optional.
    :ivar target_branch: Used for Emulation - If authorised will execute the request as if the agent's parent branch is the TargetBranch specified.
    :ivar override_logging: Use to override the default logging level
    :ivar language_code: ISO 639 two-character language codes are used to retrieve specific information in the requested language. For Rich Content and Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE, DECH can also be used. Only certain services support this attribute. Providers: ACH, RCH, 1G, 1V, 1P, 1J.
    """
    billing_point_of_sale_info: BillingPointOfSaleInfo = field(
        default=None,
        metadata=dict(
            name="BillingPointOfSaleInfo",
            type="Element",
            required=True
        )
    )
    agent_idoverride: List[AgentIdoverride] = field(
        default_factory=list,
        metadata=dict(
            name="AgentIDOverride",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    terminal_session_info: TerminalSessionInfo = field(
        default=None,
        metadata=dict(
            name="TerminalSessionInfo",
            type="Element"
        )
    )
    trace_id: str = field(
        default=None,
        metadata=dict(
            name="TraceId",
            type="Attribute"
        )
    )
    token_id: str = field(
        default=None,
        metadata=dict(
            name="TokenId",
            type="Attribute"
        )
    )
    authorized_by: str = field(
        default=None,
        metadata=dict(
            name="AuthorizedBy",
            type="Attribute"
        )
    )
    target_branch: str = field(
        default=None,
        metadata=dict(
            name="TargetBranch",
            type="Attribute",
            min_length=1.0,
            max_length=25.0
        )
    )
    override_logging: str = field(
        default=None,
        metadata=dict(
            name="OverrideLogging",
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
class BaseRsp:
    """The base type for all responses.

    :ivar response_message:
    :ivar trace_id: Unique identifier for this atomic transaction traced by the user. Use is optional.
    :ivar transaction_id: System generated unique identifier for this atomic transaction.
    :ivar response_time: The time (in ms) the system spent processing this request, not including transmission times.
    :ivar command_history: HTTP link to download command history and debugging information of the request that generated this response. Must be enabled on the system.
    """
    response_message: List[ResponseMessage] = field(
        default_factory=list,
        metadata=dict(
            name="ResponseMessage",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    trace_id: str = field(
        default=None,
        metadata=dict(
            name="TraceId",
            type="Attribute"
        )
    )
    transaction_id: str = field(
        default=None,
        metadata=dict(
            name="TransactionId",
            type="Attribute"
        )
    )
    response_time: int = field(
        default=None,
        metadata=dict(
            name="ResponseTime",
            type="Attribute"
        )
    )
    command_history: str = field(
        default=None,
        metadata=dict(
            name="CommandHistory",
            type="Attribute"
        )
    )


@dataclass
class ErrorInfo(TypeErrorInfo):
    """Container for error data when there is an application error."""
    pass


@dataclass
class BaseCoreSearchReq(BaseCoreReq):
    """Base Request for Air Search.

    :ivar next_result_reference:
    """
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata=dict(
            name="NextResultReference",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class BaseReq(BaseCoreReq):
    """
    :ivar override_pcc:
    :ivar retrieve_provider_reservation_details:
    """
    override_pcc: OverridePcc = field(
        default=None,
        metadata=dict(
            name="OverridePCC",
            type="Element"
        )
    )
    retrieve_provider_reservation_details: bool = field(
        default="false",
        metadata=dict(
            name="RetrieveProviderReservationDetails",
            type="Attribute"
        )
    )


@dataclass
class BaseSearchRsp(BaseRsp):
    """
    :ivar next_result_reference:
    """
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata=dict(
            name="NextResultReference",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class BaseCreateReservationReq(BaseReq):
    """
    :ivar linked_universal_record:
    :ivar booking_traveler:
    :ivar osi:
    :ivar accounting_remark:
    :ivar general_remark:
    :ivar xmlremark:
    :ivar unassociated_remark:
    :ivar postscript:
    :ivar passive_info:
    :ivar continuity_check_override: This element will be used if user wants to override segment continuity check.
    :ivar agency_contact_info:
    :ivar customer_id:
    :ivar file_finishing_info:
    :ivar commission_remark:
    :ivar consolidator_remark:
    :ivar invoice_remark:
    :ivar ssr: SSR element outside Booking Traveler without any Segment Ref or Booking Traveler Ref.
    :ivar email_notification:
    :ivar queue_place: Allow queue placement of a PNR at the time of booking in AirCreateReservationReq,HotelCreateReservationReq,PassiveCreateReservationReq and VehicleCreateReservationReq for providers 1G,1V,1P and 1J.
    :ivar rule_name: This attribute is meant to attach a mandatory custom check rule name to a PNR. A non-mandatory custom check rule too can be attached to a PNR.
    :ivar universal_record_locator_code: Which UniversalRecord should this new reservation be applied to. If blank, then a new one is created.
    :ivar provider_locator_code: Which Provider reservation does this reservation get added to.
    :ivar provider_code: To be used with ProviderLocatorCode, which host the reservation being added to belongs to.
    :ivar customer_number: Optional client centric customer identifier
    :ivar version:
    """
    linked_universal_record: List[LinkedUniversalRecord] = field(
        default_factory=list,
        metadata=dict(
            name="LinkedUniversalRecord",
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
    osi: List[Osi] = field(
        default_factory=list,
        metadata=dict(
            name="OSI",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
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
    xmlremark: List[Xmlremark] = field(
        default_factory=list,
        metadata=dict(
            name="XMLRemark",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    unassociated_remark: List[UnassociatedRemark] = field(
        default_factory=list,
        metadata=dict(
            name="UnassociatedRemark",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    postscript: Postscript = field(
        default=None,
        metadata=dict(
            name="Postscript",
            type="Element"
        )
    )
    passive_info: PassiveInfo = field(
        default=None,
        metadata=dict(
            name="PassiveInfo",
            type="Element"
        )
    )
    continuity_check_override: ContinuityCheckOverride = field(
        default=None,
        metadata=dict(
            name="ContinuityCheckOverride",
            type="Element"
        )
    )
    agency_contact_info: AgencyContactInfo = field(
        default=None,
        metadata=dict(
            name="AgencyContactInfo",
            type="Element"
        )
    )
    customer_id: CustomerId = field(
        default=None,
        metadata=dict(
            name="CustomerID",
            type="Element"
        )
    )
    file_finishing_info: FileFinishingInfo = field(
        default=None,
        metadata=dict(
            name="FileFinishingInfo",
            type="Element"
        )
    )
    commission_remark: CommissionRemark = field(
        default=None,
        metadata=dict(
            name="CommissionRemark",
            type="Element"
        )
    )
    consolidator_remark: ConsolidatorRemark = field(
        default=None,
        metadata=dict(
            name="ConsolidatorRemark",
            type="Element"
        )
    )
    invoice_remark: List[InvoiceRemark] = field(
        default_factory=list,
        metadata=dict(
            name="InvoiceRemark",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata=dict(
            name="SSR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    email_notification: EmailNotification = field(
        default=None,
        metadata=dict(
            name="EmailNotification",
            type="Element"
        )
    )
    queue_place: QueuePlace = field(
        default=None,
        metadata=dict(
            name="QueuePlace",
            type="Element"
        )
    )
    rule_name: str = field(
        default=None,
        metadata=dict(
            name="RuleName",
            type="Attribute",
            max_length=10.0
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
    provider_locator_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            min_length=5.0,
            max_length=8.0
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute"
        )
    )
    customer_number: str = field(
        default=None,
        metadata=dict(
            name="CustomerNumber",
            type="Attribute"
        )
    )
    version: int = field(
        default=None,
        metadata=dict(
            name="Version",
            type="Attribute"
        )
    )


@dataclass
class BaseSearchReq(BaseReq):
    """
    :ivar next_result_reference:
    """
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata=dict(
            name="NextResultReference",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class BaseCreateWithFormOfPaymentReq(BaseCreateReservationReq):
    """Container for BaseCreateReservation along with Form Of Payment.

    :ivar form_of_payment: Provider:1G,1V,1P,1J,ACH,SDK.
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