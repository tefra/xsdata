from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Any,
    Bl,
    Cd,
    Ce,
    Cs,
    EdExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    St,
    SxcmTsExplicit,
    Ts,
    TsExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    ActClass,
    ActClassCareProvision,
    ActClassObservation,
    ActClassProcedure,
    ActClassRoot,
    ActClassSupply,
    ActMood,
    ActMoodIntent,
    ActRelationshipConditional,
    ActRelationshipCostTracking,
    ActRelationshipFulfills,
    ActRelationshipHasComponent,
    ActRelationshipHasSupport,
    ActRelationshipOutcome,
    ActRelationshipPosting,
    ActRelationshipReason,
    ActRelationshipSequel,
    ActRelationshipTemporallyPertains,
    ContextControl,
    EntityClassMaterial,
    EntityDeterminerDetermined,
    NullFlavor,
    ParticipationParticipation,
    ParticipationPhysicalPerformer,
    ParticipationType,
    ParticipationVerifier,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    XAccommodationRequestorRole,
    XActRelationshipDocument,
    XActRelationshipEntry,
    XActRelationshipEntryRelationship,
    XActRelationshipExternalReference,
    XActRelationshipPatientTransport,
    XActRelationshipPertinentInfo,
    XActRelationshipRelatedAuthorizations,
    XActReplaceOrRevise,
    XDocumentEntrySubject,
    XDocumentSubject,
    XInformationRecipientRole,
    XRoleClassAccommodationRequestor,
    XRoleClassCoverage,
    XRoleClassCoverageInvoice,
    XRoleClassCredentialedEntity,
    XRoleClassPayeePolicyRelationship,
    XSuccReplPrev,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt050000_uv01 import (
    CoctMt050000Uv01Patient,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt090000_uv01 import (
    CoctMt090000Uv01AssignedEntity,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt090100_uv01 import (
    CoctMt090100Uv01AssignedPerson,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt090400_uv import (
    CoctMt090400UvAssignedParty,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt230100_uv import (
    CoctMt230100UvMedication,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes import (
    IvlInt,
    IvlPq,
    RtoPqPq,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.repc_mt000100_uv01 import (
    RepcMt000100Uv01Act,
    RepcMt000100Uv01ActReference,
    RepcMt000100Uv01Encounter,
    RepcMt000100Uv01Observation,
    RepcMt000100Uv01Organizer,
    RepcMt000100Uv01Procedure,
    RepcMt000100Uv01SubstanceAdministration,
    RepcMt000100Uv01Supply,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.repc_mt000300_uv01 import (
    RepcMt000300Uv01Concern,
)

__NAMESPACE__ = "urn:hl7-org:v3"


class RepcMt000200UvSubject2Value(Enum):
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


class RepcMt000200UvSubjectValue(Enum):
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
class RepcMt000200UvAuthor:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar note_text:
    :ivar time:
    :ivar mode_code:
    :ivar signature_code:
    :ivar signature_text:
    :ivar assigned_entity:
    :ivar patient:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000200UV.Author"

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
    note_text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            name="noteText",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    mode_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="modeCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    signature_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="signatureCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    signature_text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            name="signatureText",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    assigned_entity: Optional[CoctMt090000Uv01AssignedEntity] = field(
        default=None,
        metadata=dict(
            name="assignedEntity",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    patient: Optional[CoctMt050000Uv01Patient] = field(
        default=None,
        metadata=dict(
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
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.AUT,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )


@dataclass
class RepcMt000200UvAuthor6:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar note_text:
    :ivar time:
    :ivar mode_code:
    :ivar signature_code:
    :ivar signature_text:
    :ivar assigned_party:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000200UV.Author6"

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
    note_text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            name="noteText",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    mode_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="modeCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    signature_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="signatureCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    signature_text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            name="signatureText",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    assigned_party: Optional[CoctMt090400UvAssignedParty] = field(
        default=None,
        metadata=dict(
            name="assignedParty",
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
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.AUT,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )


@dataclass
class RepcMt000200UvComponent2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar guideline:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Component2"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="sequenceNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    guideline: Optional["RepcMt000200UvGuideline"] = field(
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
    type_code: Optional[ActRelationshipHasComponent] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvComponent7:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar care_plan:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Component7"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="sequenceNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    care_plan: Optional["RepcMt000200UvCarePlan"] = field(
        default=None,
        metadata=dict(
            name="carePlan",
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
    type_code: Optional[ActRelationshipHasComponent] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            required=True,
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvCriterionGroup:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.CriterionGroup"

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
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )
    class_code: Optional[ActClassRoot] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN_CRT,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvDataEnterer:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar mode_code:
    :ivar signature_code:
    :ivar signature_text:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000200UV.DataEnterer"

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
    time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    mode_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="modeCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    signature_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="signatureCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    signature_text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            name="signatureText",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    assigned_person: Optional[CoctMt090100Uv01AssignedPerson] = field(
        default=None,
        metadata=dict(
            name="assignedPerson",
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
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.ENT,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )


@dataclass
class RepcMt000200UvInFulfillmentOf:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar act_reference1:
    :ivar act:
    :ivar encounter:
    :ivar observation:
    :ivar organizer:
    :ivar procedure:
    :ivar substance_administration:
    :ivar supply:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.InFulfillmentOf"

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
    act_reference1: Optional[RepcMt000100Uv01ActReference] = field(
        default=None,
        metadata=dict(
            name="actReference1",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    act: Optional[RepcMt000100Uv01Act] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    encounter: Optional[RepcMt000100Uv01Encounter] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    observation: Optional[RepcMt000100Uv01Observation] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    organizer: Optional[RepcMt000100Uv01Organizer] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    procedure: Optional[RepcMt000100Uv01Procedure] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    substance_administration: Optional[RepcMt000100Uv01SubstanceAdministration] = field(
        default=None,
        metadata=dict(
            name="substanceAdministration",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    supply: Optional[RepcMt000100Uv01Supply] = field(
        default=None,
        metadata=dict(
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
    type_code: Optional[ActRelationshipFulfills] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvMaterialKind2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar desc:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "REPC_MT000200UV.MaterialKind2"

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
    code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    desc: Optional[St] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )
    class_code: Optional[EntityClassMaterial] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    determiner_code: Optional[EntityDeterminerDetermined] = field(
        default=None,
        metadata=dict(
            name="determinerCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvObservationGoal:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar effective_time:
    :ivar value:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.ObservationGoal"

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
    code: Optional[Cd] = field(
        default=None,
        metadata=dict(
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
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    value: Optional[Any] = field(
        default=None,
        metadata=dict(
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
    class_code: Optional[ActClassObservation] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.GOL,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvParticipant:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar note_text:
    :ivar mode_code:
    :ivar assigned_party:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000200UV.Participant"

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
    note_text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            name="noteText",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    mode_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="modeCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    assigned_party: Optional[CoctMt090400UvAssignedParty] = field(
        default=None,
        metadata=dict(
            name="assignedParty",
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
    type_code: Optional[ParticipationParticipation] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )


@dataclass
class RepcMt000200UvPerformer:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar function_code:
    :ivar time:
    :ivar mode_code:
    :ivar assigned_party:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000200UV.Performer"

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
    function_code: Optional[Cd] = field(
        default=None,
        metadata=dict(
            name="functionCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    mode_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="modeCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    assigned_party: Optional[CoctMt090400UvAssignedParty] = field(
        default=None,
        metadata=dict(
            name="assignedParty",
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
    type_code: Optional[ParticipationPhysicalPerformer] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )


@dataclass
class RepcMt000200UvPerformer2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000200UV.Performer2"

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
    time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    assigned_person: Optional[CoctMt090100Uv01AssignedPerson] = field(
        default=None,
        metadata=dict(
            name="assignedPerson",
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
    type_code: Optional[ParticipationPhysicalPerformer] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )


@dataclass
class RepcMt000200UvPrecondition2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar conjunction_code:
    :ivar seperatable_ind:
    :ivar criterion:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Precondition2"

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
    conjunction_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="conjunctionCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata=dict(
            name="seperatableInd",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    criterion: Optional["RepcMt000200UvCriterion"] = field(
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "RepcMt000200UvPrecondition2.Value", ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=ActRelationshipConditional.PRCN,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
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

    class Value(Enum):
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
class RepcMt000200UvReason2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar concern:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Reason2"

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
    concern: Optional[RepcMt000300Uv01Concern] = field(
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
    type_code: Optional[ActRelationshipReason] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvVerifier:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar note_text:
    :ivar time:
    :ivar mode_code:
    :ivar signature_code:
    :ivar signature_text:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000200UV.Verifier"

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
    note_text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            name="noteText",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    mode_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="modeCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    signature_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="signatureCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    signature_text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            name="signatureText",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    assigned_person: Optional[CoctMt090100Uv01AssignedPerson] = field(
        default=None,
        metadata=dict(
            name="assignedPerson",
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
    type_code: Optional[ParticipationVerifier] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )


@dataclass
class RepcMt000200UvAnnotation:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar text:
    :ivar status_code:
    :ivar author:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.Annotation"

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
    text: Optional[St] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
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
    author: List[RepcMt000200UvAuthor6] = field(
        default_factory=list,
        metadata=dict(
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
    class_code: Optional[ActClassRoot] = field(
        default=None,
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
class RepcMt000200UvCriterion:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar text:
    :ivar value:
    :ivar interpretation_code:
    :ivar precondition:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Criterion"

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
    value: Optional[Any] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    interpretation_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="interpretationCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    precondition: List[RepcMt000200UvPrecondition2] = field(
        default_factory=list,
        metadata=dict(
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
    class_code: Optional[ActClassObservation] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN_CRT,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )
    negation_ind: str = field(
        default="false",
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvFinalGoal:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar observation_goal:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.FinalGoal"

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
    observation_goal: Optional[RepcMt000200UvObservationGoal] = field(
        default=None,
        metadata=dict(
            name="observationGoal",
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "RepcMt000200UvFinalGoal.Value", ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=ActRelationshipOutcome.OBJF,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )

    class Value(Enum):
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
class RepcMt000200UvGoal:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar observation_goal:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Goal"

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
    observation_goal: Optional[RepcMt000200UvObservationGoal] = field(
        default=None,
        metadata=dict(
            name="observationGoal",
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "RepcMt000200UvGoal.Value", ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=ActRelationshipOutcome.GOAL,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )

    class Value(Enum):
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
class RepcMt000200UvMaterialPart:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar part_material_kind:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "REPC_MT000200UV.MaterialPart"

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
    part_material_kind: Optional[RepcMt000200UvMaterialKind2] = field(
        default=None,
        metadata=dict(
            name="partMaterialKind",
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
    class_code: Optional[RoleClassPartitive] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvPatientInstructions:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar effective_time:
    :ivar performer:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.PatientInstructions"

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
    effective_time: Optional[Ts] = field(
        default=None,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    performer: List[RepcMt000200UvPerformer] = field(
        default_factory=list,
        metadata=dict(
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
    class_code: Optional[ActClassProcedure] = field(
        default=None,
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
class RepcMt000200UvPlannedReview:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar effective_time:
    :ivar performer:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.PlannedReview"

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
    effective_time: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    performer: List[RepcMt000200UvPerformer] = field(
        default_factory=list,
        metadata=dict(
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
        default=ActClass.REV,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: Optional[ActMoodIntent] = field(
        default=None,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvComponent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar patient_instructions:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Component"

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
    patient_instructions: Optional[RepcMt000200UvPatientInstructions] = field(
        default=None,
        metadata=dict(
            name="patientInstructions",
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
    type_code: Optional[ActRelationshipHasComponent] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvConditions:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar conjunction_code:
    :ivar seperatable_ind:
    :ivar criterion:
    :ivar criterion_group:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Conditions"

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
    conjunction_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="conjunctionCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata=dict(
            name="seperatableInd",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    criterion: Optional[RepcMt000200UvCriterion] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    criterion_group: Optional[RepcMt000200UvCriterionGroup] = field(
        default=None,
        metadata=dict(
            name="criterionGroup",
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
    type_code: Optional[ActRelationshipConditional] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
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
class RepcMt000200UvMaterialKind:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar desc:
    :ivar material_part:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "REPC_MT000200UV.MaterialKind"

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
    code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    desc: Optional[St] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    material_part: List[RepcMt000200UvMaterialPart] = field(
        default_factory=list,
        metadata=dict(
            name="materialPart",
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
    class_code: Optional[EntityClassMaterial] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    determiner_code: Optional[EntityDeterminerDetermined] = field(
        default=None,
        metadata=dict(
            name="determinerCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvSubject:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar planned_review:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Subject"

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
    planned_review: Optional[RepcMt000200UvPlannedReview] = field(
        default=None,
        metadata=dict(
            name="plannedReview",
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, RepcMt000200UvSubjectValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=RepcMt000200UvSubjectValue.SUBJ,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvSubject2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar annotation:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Subject2"

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
    annotation: Optional[RepcMt000200UvAnnotation] = field(
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, RepcMt000200UvSubject2Value, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=RepcMt000200UvSubject2Value.SUBJ,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvActDefinition:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar availability_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar uncertainty_code:
    :ivar language_code:
    :ivar goal:
    :ivar reason:
    :ivar conditions:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.ActDefinition"

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
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    code: Optional[Cd] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
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
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="availabilityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    uncertainty_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="uncertaintyCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="languageCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
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
    class_code: Optional[ActClassRoot] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.DEF_VALUE,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvAdministerableMaterial:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar administerable_material_kind:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "REPC_MT000200UV.AdministerableMaterial"

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
    administerable_material_kind: Optional[RepcMt000200UvMaterialKind] = field(
        default=None,
        metadata=dict(
            name="administerableMaterialKind",
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
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, "RepcMt000200UvAdministerableMaterial.Value", XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassPassive.ADMM,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
        )
    )

    class Value(Enum):
        """
        :cvar ROL:
        """
        ROL = "ROL"


@dataclass
class RepcMt000200UvEncounterDefinition:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar availability_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar goal:
    :ivar reason:
    :ivar conditions:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.EncounterDefinition"

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
            min_occurs=1,
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
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
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="availabilityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
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
        default=ActClass.ENC,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.DEF_VALUE,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvObservationDefinition:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar derivation_expr:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar availability_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar repeat_number:
    :ivar uncertainty_code:
    :ivar language_code:
    :ivar value:
    :ivar method_code:
    :ivar target_site_code:
    :ivar goal:
    :ivar reason:
    :ivar conditions:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.ObservationDefinition"

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
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    code: Optional[Cd] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    derivation_expr: Optional[St] = field(
        default=None,
        metadata=dict(
            name="derivationExpr",
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    effective_time: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="availabilityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    repeat_number: Optional[IvlInt] = field(
        default=None,
        metadata=dict(
            name="repeatNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    uncertainty_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="uncertaintyCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="languageCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    value: Optional[Any] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    method_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="methodCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    target_site_code: List[Cd] = field(
        default_factory=list,
        metadata=dict(
            name="targetSiteCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
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
    class_code: Optional[ActClassObservation] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.DEF_VALUE,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvProcedureDefinition:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar availability_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar uncertainty_code:
    :ivar language_code:
    :ivar method_code:
    :ivar approach_site_code:
    :ivar target_site_code:
    :ivar goal:
    :ivar reason:
    :ivar conditions:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.ProcedureDefinition"

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
            min_occurs=1,
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
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
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="availabilityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    uncertainty_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="uncertaintyCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="languageCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    method_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="methodCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    approach_site_code: List[Cd] = field(
        default_factory=list,
        metadata=dict(
            name="approachSiteCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    target_site_code: List[Cd] = field(
        default_factory=list,
        metadata=dict(
            name="targetSiteCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
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
    class_code: Optional[ActClassProcedure] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.DEF_VALUE,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvSupplyEvent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar derivation_expr:
    :ivar goal:
    :ivar reason:
    :ivar conditions:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.SupplyEvent"

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
    code: Optional[Cd] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    derivation_expr: Optional[St] = field(
        default=None,
        metadata=dict(
            name="derivationExpr",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
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
    class_code: Optional[ActClassSupply] = field(
        default=None,
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
    negation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvConsumable:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar administerable_material:
    :ivar medication:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000200UV.Consumable"

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
    administerable_material: Optional[RepcMt000200UvAdministerableMaterial] = field(
        default=None,
        metadata=dict(
            name="administerableMaterial",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    medication: Optional[CoctMt230100UvMedication] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.CSM,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )


@dataclass
class RepcMt000200UvSubstanceAdministrationDefinition:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar availability_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar repeat_number:
    :ivar route_code:
    :ivar approach_site_code:
    :ivar dose_quantity:
    :ivar rate_quantity:
    :ivar max_dose_quantity:
    :ivar administration_unit_code:
    :ivar consumable:
    :ivar goal:
    :ivar reason:
    :ivar conditions:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.SubstanceAdministrationDefinition"

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
            min_occurs=1,
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    effective_time: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="availabilityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    repeat_number: Optional[IvlInt] = field(
        default=None,
        metadata=dict(
            name="repeatNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    route_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="routeCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    approach_site_code: List[Cd] = field(
        default_factory=list,
        metadata=dict(
            name="approachSiteCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dose_quantity: Optional[IvlPq] = field(
        default=None,
        metadata=dict(
            name="doseQuantity",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    rate_quantity: Optional[IvlPq] = field(
        default=None,
        metadata=dict(
            name="rateQuantity",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    max_dose_quantity: Optional[RtoPqPq] = field(
        default=None,
        metadata=dict(
            name="maxDoseQuantity",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    administration_unit_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="administrationUnitCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    consumable: Optional[RepcMt000200UvConsumable] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
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
        default=ActClass.SBADM,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.DEF_VALUE,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvComponent13:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar act_definition:
    :ivar encounter_definition:
    :ivar observation_definition:
    :ivar procedure_definition:
    :ivar substance_administration_definition:
    :ivar supply_event:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Component13"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="sequenceNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    act_definition: Optional[RepcMt000200UvActDefinition] = field(
        default=None,
        metadata=dict(
            name="actDefinition",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    encounter_definition: Optional[RepcMt000200UvEncounterDefinition] = field(
        default=None,
        metadata=dict(
            name="encounterDefinition",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    observation_definition: Optional[RepcMt000200UvObservationDefinition] = field(
        default=None,
        metadata=dict(
            name="observationDefinition",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    procedure_definition: Optional[RepcMt000200UvProcedureDefinition] = field(
        default=None,
        metadata=dict(
            name="procedureDefinition",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    substance_administration_definition: Optional[RepcMt000200UvSubstanceAdministrationDefinition] = field(
        default=None,
        metadata=dict(
            name="substanceAdministrationDefinition",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    supply_event: Optional[RepcMt000200UvSupplyEvent] = field(
        default=None,
        metadata=dict(
            name="supplyEvent",
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
    type_code: Optional[ActRelationshipHasComponent] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
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
class RepcMt000200UvInFulfillmentOf2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar act_definition:
    :ivar encounter_definition:
    :ivar observation_definition:
    :ivar procedure_definition:
    :ivar substance_administration_definition:
    :ivar supply_event:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.InFulfillmentOf2"

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
    act_definition: Optional[RepcMt000200UvActDefinition] = field(
        default=None,
        metadata=dict(
            name="actDefinition",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    encounter_definition: Optional[RepcMt000200UvEncounterDefinition] = field(
        default=None,
        metadata=dict(
            name="encounterDefinition",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    observation_definition: Optional[RepcMt000200UvObservationDefinition] = field(
        default=None,
        metadata=dict(
            name="observationDefinition",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    procedure_definition: Optional[RepcMt000200UvProcedureDefinition] = field(
        default=None,
        metadata=dict(
            name="procedureDefinition",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    substance_administration_definition: Optional[RepcMt000200UvSubstanceAdministrationDefinition] = field(
        default=None,
        metadata=dict(
            name="substanceAdministrationDefinition",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    supply_event: Optional[RepcMt000200UvSupplyEvent] = field(
        default=None,
        metadata=dict(
            name="supplyEvent",
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
    type_code: Optional[ActRelationshipFulfills] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
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
class RepcMt000200UvGuideline:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar title:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar author:
    :ivar final_goal:
    :ivar reason:
    :ivar component1:
    :ivar component2:
    :ivar component3:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.Guideline"

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
    title: Optional[St] = field(
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
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
    author: List[RepcMt000200UvAuthor6] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    final_goal: List[RepcMt000200UvFinalGoal] = field(
        default_factory=list,
        metadata=dict(
            name="finalGoal",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component1: List[RepcMt000200UvComponent] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component2: List[RepcMt000200UvComponent13] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component3: List[RepcMt000200UvComponent2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
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
    class_code: Optional[ActClassCareProvision] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.DEF_VALUE,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvObservationIntent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar derivation_expr:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar availability_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar repeat_number:
    :ivar uncertainty_code:
    :ivar language_code:
    :ivar value:
    :ivar method_code:
    :ivar target_site_code:
    :ivar performer:
    :ivar goal:
    :ivar in_fulfillment_of:
    :ivar reason:
    :ivar conditions:
    :ivar component:
    :ivar fulfillment:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar component_of:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.ObservationIntent"

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
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    code: Optional[Cd] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    derivation_expr: Optional[St] = field(
        default=None,
        metadata=dict(
            name="derivationExpr",
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    effective_time: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="availabilityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    repeat_number: Optional[IvlInt] = field(
        default=None,
        metadata=dict(
            name="repeatNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    uncertainty_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="uncertaintyCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="languageCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    value: Optional[Any] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    method_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="methodCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    target_site_code: List[Cd] = field(
        default_factory=list,
        metadata=dict(
            name="targetSiteCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    performer: List[RepcMt000200UvPerformer2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    in_fulfillment_of: Optional[RepcMt000200UvInFulfillmentOf2] = field(
        default=None,
        metadata=dict(
            name="inFulfillmentOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component: List["RepcMt000200UvComponent4"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    fulfillment: List[RepcMt000200UvInFulfillmentOf] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component_of: List["RepcMt000200UvComponent3"] = field(
        default_factory=list,
        metadata=dict(
            name="componentOf",
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
    class_code: Optional[ActClassObservation] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: Optional[ActMoodIntent] = field(
        default=None,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvProcedureIntent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar availability_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar uncertainty_code:
    :ivar language_code:
    :ivar method_code:
    :ivar approach_site_code:
    :ivar target_site_code:
    :ivar performer:
    :ivar goal:
    :ivar in_fulfillment_of:
    :ivar reason:
    :ivar conditions:
    :ivar component:
    :ivar fulfillment:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar component_of:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.ProcedureIntent"

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
            min_occurs=1,
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
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
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="availabilityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    uncertainty_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="uncertaintyCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="languageCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    method_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="methodCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    approach_site_code: List[Cd] = field(
        default_factory=list,
        metadata=dict(
            name="approachSiteCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    target_site_code: List[Cd] = field(
        default_factory=list,
        metadata=dict(
            name="targetSiteCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    performer: List[RepcMt000200UvPerformer2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    in_fulfillment_of: Optional[RepcMt000200UvInFulfillmentOf2] = field(
        default=None,
        metadata=dict(
            name="inFulfillmentOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component: List["RepcMt000200UvComponent4"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    fulfillment: List[RepcMt000200UvInFulfillmentOf] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component_of: List["RepcMt000200UvComponent3"] = field(
        default_factory=list,
        metadata=dict(
            name="componentOf",
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
    class_code: Optional[ActClassProcedure] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: Optional[ActMoodIntent] = field(
        default=None,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvSubstanceAdministrationIntent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar availability_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar repeat_number:
    :ivar route_code:
    :ivar approach_site_code:
    :ivar dose_quantity:
    :ivar rate_quantity:
    :ivar max_dose_quantity:
    :ivar administration_unit_code:
    :ivar consumable:
    :ivar performer:
    :ivar goal:
    :ivar in_fulfillment_of:
    :ivar reason:
    :ivar conditions:
    :ivar component:
    :ivar fulfillment:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar component_of:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.SubstanceAdministrationIntent"

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
            min_occurs=1,
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    effective_time: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="availabilityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    repeat_number: Optional[IvlInt] = field(
        default=None,
        metadata=dict(
            name="repeatNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    route_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="routeCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    approach_site_code: List[Cd] = field(
        default_factory=list,
        metadata=dict(
            name="approachSiteCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dose_quantity: Optional[IvlPq] = field(
        default=None,
        metadata=dict(
            name="doseQuantity",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    rate_quantity: Optional[IvlPq] = field(
        default=None,
        metadata=dict(
            name="rateQuantity",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    max_dose_quantity: Optional[RtoPqPq] = field(
        default=None,
        metadata=dict(
            name="maxDoseQuantity",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    administration_unit_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="administrationUnitCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    consumable: Optional[RepcMt000200UvConsumable] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    performer: List[RepcMt000200UvPerformer2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    in_fulfillment_of: Optional[RepcMt000200UvInFulfillmentOf2] = field(
        default=None,
        metadata=dict(
            name="inFulfillmentOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component: List["RepcMt000200UvComponent4"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    fulfillment: List[RepcMt000200UvInFulfillmentOf] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component_of: List["RepcMt000200UvComponent3"] = field(
        default_factory=list,
        metadata=dict(
            name="componentOf",
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
        default=ActClass.SBADM,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: Optional[ActMoodIntent] = field(
        default=None,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvComponent3:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar act_intent:
    :ivar encounter_intent:
    :ivar observation_intent:
    :ivar procedure_intent:
    :ivar substance_administration_intent:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Component3"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="sequenceNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    act_intent: Optional["RepcMt000200UvActIntent"] = field(
        default=None,
        metadata=dict(
            name="actIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    encounter_intent: Optional["RepcMt000200UvEncounterIntent"] = field(
        default=None,
        metadata=dict(
            name="encounterIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    observation_intent: Optional[RepcMt000200UvObservationIntent] = field(
        default=None,
        metadata=dict(
            name="observationIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    procedure_intent: Optional[RepcMt000200UvProcedureIntent] = field(
        default=None,
        metadata=dict(
            name="procedureIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    substance_administration_intent: Optional[RepcMt000200UvSubstanceAdministrationIntent] = field(
        default=None,
        metadata=dict(
            name="substanceAdministrationIntent",
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
    type_code: Optional[ActRelationshipHasComponent] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvDefinition1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar guideline:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Definition1"

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
    guideline: Optional[RepcMt000200UvGuideline] = field(
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "RepcMt000200UvDefinition1.Value", ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=ActRelationshipSequel.INST,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
        )
    )
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
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

    class Value(Enum):
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
class RepcMt000200UvEncounterIntent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar availability_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar performer:
    :ivar goal:
    :ivar in_fulfillment_of:
    :ivar reason:
    :ivar conditions:
    :ivar component:
    :ivar fulfillment:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar component_of:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.EncounterIntent"

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
            min_occurs=1,
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
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
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="availabilityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    performer: List[RepcMt000200UvPerformer2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    in_fulfillment_of: Optional[RepcMt000200UvInFulfillmentOf2] = field(
        default=None,
        metadata=dict(
            name="inFulfillmentOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component: List["RepcMt000200UvComponent4"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    fulfillment: List[RepcMt000200UvInFulfillmentOf] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component_of: List[RepcMt000200UvComponent3] = field(
        default_factory=list,
        metadata=dict(
            name="componentOf",
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
        default=ActClass.ENC,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: Optional[ActMoodIntent] = field(
        default=None,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000200UvComponent4:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar act_intent:
    :ivar encounter_intent:
    :ivar observation_intent:
    :ivar procedure_intent:
    :ivar substance_administration_intent:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Component4"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="sequenceNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    act_intent: Optional["RepcMt000200UvActIntent"] = field(
        default=None,
        metadata=dict(
            name="actIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    encounter_intent: Optional[RepcMt000200UvEncounterIntent] = field(
        default=None,
        metadata=dict(
            name="encounterIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    observation_intent: Optional[RepcMt000200UvObservationIntent] = field(
        default=None,
        metadata=dict(
            name="observationIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    procedure_intent: Optional[RepcMt000200UvProcedureIntent] = field(
        default=None,
        metadata=dict(
            name="procedureIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    substance_administration_intent: Optional[RepcMt000200UvSubstanceAdministrationIntent] = field(
        default=None,
        metadata=dict(
            name="substanceAdministrationIntent",
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
    type_code: Optional[ActRelationshipHasComponent] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvActIntent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar availability_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar uncertainty_code:
    :ivar language_code:
    :ivar performer:
    :ivar goal:
    :ivar in_fulfillment_of:
    :ivar reason:
    :ivar conditions:
    :ivar component:
    :ivar fulfillment:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar component_of:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.ActIntent"

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
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    code: Optional[Cd] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    text: Optional[EdExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
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
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="availabilityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    uncertainty_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="uncertaintyCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="languageCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    performer: List[RepcMt000200UvPerformer2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    goal: List[RepcMt000200UvGoal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    in_fulfillment_of: Optional[RepcMt000200UvInFulfillmentOf2] = field(
        default=None,
        metadata=dict(
            name="inFulfillmentOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    conditions: List[RepcMt000200UvConditions] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component: List[RepcMt000200UvComponent4] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    fulfillment: List[RepcMt000200UvInFulfillmentOf] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component_of: List[RepcMt000200UvComponent3] = field(
        default_factory=list,
        metadata=dict(
            name="componentOf",
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
    class_code: Optional[ActClassRoot] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: Optional[ActMoodIntent] = field(
        default=None,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvComponent10:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar act_intent:
    :ivar encounter_intent:
    :ivar observation_intent:
    :ivar procedure_intent:
    :ivar substance_administration_intent:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT000200UV.Component10"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="sequenceNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    act_intent: Optional[RepcMt000200UvActIntent] = field(
        default=None,
        metadata=dict(
            name="actIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    encounter_intent: Optional[RepcMt000200UvEncounterIntent] = field(
        default=None,
        metadata=dict(
            name="encounterIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    observation_intent: Optional[RepcMt000200UvObservationIntent] = field(
        default=None,
        metadata=dict(
            name="observationIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    procedure_intent: Optional[RepcMt000200UvProcedureIntent] = field(
        default=None,
        metadata=dict(
            name="procedureIntent",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    substance_administration_intent: Optional[RepcMt000200UvSubstanceAdministrationIntent] = field(
        default=None,
        metadata=dict(
            name="substanceAdministrationIntent",
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
    type_code: Optional[ActRelationshipHasComponent] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            required=True,
            pattern=r"true|false"
        )
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="negationInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000200UvCarePlan:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar title:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar performer:
    :ivar author:
    :ivar data_enterer:
    :ivar verifier:
    :ivar participant:
    :ivar final_goal:
    :ivar definition:
    :ivar reason:
    :ivar component1:
    :ivar component2:
    :ivar component3:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000200UV.CarePlan"

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
    title: Optional[St] = field(
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
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
    performer: List[RepcMt000200UvPerformer] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    author: List[RepcMt000200UvAuthor] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    data_enterer: List[RepcMt000200UvDataEnterer] = field(
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
    verifier: List[RepcMt000200UvVerifier] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    participant: Optional[RepcMt000200UvParticipant] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    final_goal: List[RepcMt000200UvFinalGoal] = field(
        default_factory=list,
        metadata=dict(
            name="finalGoal",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    definition: List[RepcMt000200UvDefinition1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason: List[RepcMt000200UvReason2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component1: List[RepcMt000200UvComponent] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component2: List[RepcMt000200UvComponent10] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component3: List[RepcMt000200UvComponent7] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of1: List[RepcMt000200UvSubject2] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject_of2: List[RepcMt000200UvSubject] = field(
        default_factory=list,
        metadata=dict(
            name="subjectOf2",
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
    class_code: Optional[ActClassCareProvision] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: Optional[ActMoodIntent] = field(
        default=None,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )
