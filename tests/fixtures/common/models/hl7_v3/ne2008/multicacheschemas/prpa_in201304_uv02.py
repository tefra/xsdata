from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    ActClass,
    ActClassControlAct,
    ActMood,
    ActRelationshipConditional,
    ActRelationshipCostTracking,
    ActRelationshipHasComponent,
    ActRelationshipHasSupport,
    ActRelationshipOutcome,
    ActRelationshipPosting,
    ActRelationshipSequel,
    ActRelationshipTemporallyPertains,
    NullFlavor,
    ParticipationTargetSubject,
    XActMoodIntentEvent,
    XActRelationshipDocument,
    XActRelationshipEntry,
    XActRelationshipEntryRelationship,
    XActRelationshipExternalReference,
    XActRelationshipPatientTransport,
    XActRelationshipPertinentInfo,
    XActRelationshipRelatedAuthorizations,
    XActReplaceOrRevise,
    XSuccReplPrev,
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
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.mfmi_mt700701_uv01 import (
    MfmiMt700701Uv01Author2,
    MfmiMt700701Uv01AuthorOrPerformer,
    MfmiMt700701Uv01Custodian,
    MfmiMt700701Uv01DataEnterer,
    MfmiMt700701Uv01Definition,
    MfmiMt700701Uv01InFulfillmentOf,
    MfmiMt700701Uv01InformationRecipient,
    MfmiMt700701Uv01Overseer,
    MfmiMt700701Uv01Reason,
    MfmiMt700701Uv01ReplacementOf,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_mt201303_uv02 import (
    PrpaMt201303Uv02Patient,
)

__NAMESPACE__ = "urn:hl7-org:v3"


class PrpaIn201304Uv02MfmiMt700701Uv01Subject1Value(Enum):
    """
    :cvar PERT:
    :cvar NAME:
    :cvar AUTH:
    :cvar COVBY:
    :cvar ELNK:
    :cvar EXPL:
    :cvar PREV:
    :cvar REFV:
    :cvar SUBJ:
    :cvar DRIV:
    :cvar CAUS:
    :cvar MFST:
    :cvar ITEMSLOC:
    :cvar LIMIT:
    :cvar EVID:
    :cvar REFR:
    :cvar SUMM:
    """
    PERT = "PERT"
    NAME = "NAME"
    AUTH = "AUTH"
    COVBY = "COVBY"
    ELNK = "ELNK"
    EXPL = "EXPL"
    PREV = "PREV"
    REFV = "REFV"
    SUBJ = "SUBJ"
    DRIV = "DRIV"
    CAUS = "CAUS"
    MFST = "MFST"
    ITEMSLOC = "ITEMSLOC"
    LIMIT = "LIMIT"
    EVID = "EVID"
    REFR = "REFR"
    SUMM = "SUMM"


@dataclass
class PrpaIn201304Uv02MfmiMt700701Uv01Subject2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar patient:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "PRPA_IN201304UV02.MFMI_MT700701UV01.Subject2"

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
    patient: Optional[PrpaMt201303Uv02Patient] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True,
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
    type_code: Optional[ParticipationTargetSubject] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class PrpaIn201304Uv02MfmiMt700701Uv01RegistrationEvent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar status_code:
    :ivar effective_time:
    :ivar subject1:
    :ivar author:
    :ivar custodian:
    :ivar in_fulfillment_of:
    :ivar definition:
    :ivar replacement_of:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "PRPA_IN201304UV02.MFMI_MT700701UV01.RegistrationEvent"

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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
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
    subject1: Optional[PrpaIn201304Uv02MfmiMt700701Uv01Subject2] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    author: Optional[MfmiMt700701Uv01Author2] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    custodian: Optional[MfmiMt700701Uv01Custodian] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True,
            nillable=True
        )
    )
    in_fulfillment_of: List[MfmiMt700701Uv01InFulfillmentOf] = field(
        default_factory=list,
        metadata=dict(
            name="inFulfillmentOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    definition: List[MfmiMt700701Uv01Definition] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    replacement_of: List[MfmiMt700701Uv01ReplacementOf] = field(
        default_factory=list,
        metadata=dict(
            name="replacementOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
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
    class_code: ActClass = field(
        init=False,
        default=ActClass.REG,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class PrpaIn201304Uv02MfmiMt700701Uv01Subject1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar registration_event:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "PRPA_IN201304UV02.MFMI_MT700701UV01.Subject1"

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
    registration_event: Optional[PrpaIn201304Uv02MfmiMt700701Uv01RegistrationEvent] = field(
        default=None,
        metadata=dict(
            name="registrationEvent",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True,
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, PrpaIn201304Uv02MfmiMt700701Uv01Subject1Value, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=PrpaIn201304Uv02MfmiMt700701Uv01Subject1Value.SUBJ,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
        )
    )
    context_conduction_ind: str = field(
        default="false",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class PrpaIn201304Uv02MfmiMt700701Uv01ControlActProcess:
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
    :ivar subject:
    :ivar reason_of:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "PRPA_IN201304UV02.MFMI_MT700701UV01.ControlActProcess"

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
    overseer: List[MfmiMt700701Uv01Overseer] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    author_or_performer: List[MfmiMt700701Uv01AuthorOrPerformer] = field(
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
    data_enterer: List[MfmiMt700701Uv01DataEnterer] = field(
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
    information_recipient: List[MfmiMt700701Uv01InformationRecipient] = field(
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
    subject: List[PrpaIn201304Uv02MfmiMt700701Uv01Subject1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason_of: List[MfmiMt700701Uv01Reason] = field(
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
class PrpaIn201304Uv02McciMt000100Uv01Message:
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
        name = "PRPA_IN201304UV02.MCCI_MT000100UV01.Message"

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
    control_act_process: Optional[PrpaIn201304Uv02MfmiMt700701Uv01ControlActProcess] = field(
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
class PrpaIn201304Uv02(PrpaIn201304Uv02McciMt000100Uv01Message):
    """
    :ivar itsversion:
    """
    class Meta:
        name = "PRPA_IN201304UV02"
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
