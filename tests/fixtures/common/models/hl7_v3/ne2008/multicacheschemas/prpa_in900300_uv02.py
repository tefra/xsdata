from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    ActClassControlAct,
    NullFlavor,
    XActMoodIntentEvent,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Cd,
    Ce,
    Cs,
    EdExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    St,
    TsExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.mcci_mt000100_uv01 import (
    McciMt000100Uv01AttentionLine,
    McciMt000100Uv01Receiver,
    McciMt000100Uv01RespondTo,
    McciMt000100Uv01Sender,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_mt900300_uv02 import (
    PrpaMt900300Uv02QueryByParameterPayload,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.quqi_mt021001_uv01 import (
    QuqiMt021001Uv01AuthorOrPerformer,
    QuqiMt021001Uv01DataEnterer,
    QuqiMt021001Uv01InformationRecipient,
    QuqiMt021001Uv01Overseer,
    QuqiMt021001Uv01Reason,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PrpaIn900300Uv02QuqiMt021001Uv01ControlActProcess:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar effective_time:
    :ivar priority_code:
    :ivar reason_code:
    :ivar language_code:
    :ivar overseer:
    :ivar author_or_performer:
    :ivar data_enterer:
    :ivar information_recipient:
    :ivar reason_of:
    :ivar query_by_parameter_payload:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "PRPA_IN900300UV02.QUQI_MT021001UV01.ControlActProcess"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata=dict(
            name="realmCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            name="typeId",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            name="templateId",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: Optional[Cd] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    reason_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="reasonCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    language_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="languageCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    overseer: List[QuqiMt021001Uv01Overseer] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    author_or_performer: List[QuqiMt021001Uv01AuthorOrPerformer] = field(
        default_factory=list,
        metadata=dict(
            name="authorOrPerformer",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    data_enterer: List[QuqiMt021001Uv01DataEnterer] = field(
        default_factory=list,
        metadata=dict(
            name="dataEnterer",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    information_recipient: List[QuqiMt021001Uv01InformationRecipient] = field(
        default_factory=list,
        metadata=dict(
            name="informationRecipient",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason_of: List[QuqiMt021001Uv01Reason] = field(
        default_factory=list,
        metadata=dict(
            name="reasonOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    query_by_parameter_payload: Optional[PrpaMt900300Uv02QueryByParameterPayload] = field(
        default=None,
        metadata=dict(
            name="queryByParameterPayload",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )
    class_code: Optional[ActClassControlAct] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: Optional[XActMoodIntentEvent] = field(
        default=None,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class PrpaIn900300Uv02McciMt000100Uv01Message:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar creation_time:
    :ivar security_text:
    :ivar version_code:
    :ivar interaction_id:
    :ivar profile_id:
    :ivar processing_code:
    :ivar processing_mode_code:
    :ivar accept_ack_code:
    :ivar sequence_number:
    :ivar attachment_text:
    :ivar receiver:
    :ivar respond_to:
    :ivar sender:
    :ivar attention_line:
    :ivar control_act_process:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_IN900300UV02.MCCI_MT000100UV01.Message"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata=dict(
            name="realmCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            name="typeId",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            name="templateId",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    creation_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="creationTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    security_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="securityText",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    version_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="versionCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    interaction_id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            name="interactionId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    profile_id: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            name="profileId",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    processing_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="processingCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    processing_mode_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="processingModeCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    accept_ack_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="acceptAckCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="sequenceNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    attachment_text: List[EdExplicit] = field(
        default_factory=list,
        metadata=dict(
            name="attachmentText",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    receiver: List[McciMt000100Uv01Receiver] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    respond_to: List[McciMt000100Uv01RespondTo] = field(
        default_factory=list,
        metadata=dict(
            name="respondTo",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    sender: Optional[McciMt000100Uv01Sender] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    attention_line: List[McciMt000100Uv01AttentionLine] = field(
        default_factory=list,
        metadata=dict(
            name="attentionLine",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    control_act_process: Optional[PrpaIn900300Uv02QuqiMt021001Uv01ControlActProcess] = field(
        default=None,
        metadata=dict(
            name="controlActProcess",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaIn900300Uv02(PrpaIn900300Uv02McciMt000100Uv01Message):
    """
    :ivar itsversion:
    """
    class Meta:
        name = "PRPA_IN900300UV02"
        namespace = "urn:hl7-org:v3"

    itsversion: str = field(
        init=False,
        default="XML_1.0",
        metadata=dict(
            name="ITSVersion",
            type="Attribute",
            required=True
        )
    )
