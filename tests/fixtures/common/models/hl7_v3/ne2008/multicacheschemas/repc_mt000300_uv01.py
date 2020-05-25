from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    Cv,
    EdExplicit,
    EnExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    OnExplicit,
    St,
    TelExplicit,
    TsExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    ActClassControlAct,
    ActClassRoot,
    ActMood,
    ActRelationshipConditional,
    ActRelationshipCostTracking,
    ActRelationshipHasComponent,
    ActRelationshipHasSupport,
    ActRelationshipOutcome,
    ActRelationshipPosting,
    ActRelationshipReason,
    ActRelationshipSequel,
    ActRelationshipTemporallyPertains,
    ContextControl,
    EntityClassOrganization,
    EntityClassPlace,
    EntityDeterminer,
    NullFlavor,
    ParticipationPhysicalPerformer,
    ParticipationTargetLocation,
    ParticipationTargetSubject,
    ParticipationType,
    ParticipationVerifier,
    RoleClassServiceDeliveryLocation,
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
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt040200_uv01 import (
    CoctMt040200Uv01ResponsibleParty,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt050000_uv01 import (
    CoctMt050000Uv01Patient,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt090102_uv02 import (
    CoctMt090102Uv02AssignedPerson,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt910000_uv import (
    CoctMt910000UvCareGiver,
    CoctMt910000UvEmployee,
    CoctMt910000UvPersonalRelationship,
    CoctMt910000UvStudent,
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
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.repc_mt000700_uv01 import (
    RepcMt000700Uv01MaintainedEntity,
)

__NAMESPACE__ = "urn:hl7-org:v3"


class RepcMt000300Uv01LinksValue(Enum):
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


class RepcMt000300Uv01ReferenceValue(Enum):
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


class RepcMt000300Uv01Subject3Value(Enum):
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


class RepcMt000300Uv01Subject4Value(Enum):
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


class RepcMt000300Uv01Subject5Value(Enum):
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
class RepcMt000300Uv01Author:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar note_text:
    :ivar time:
    :ivar mode_code:
    :ivar signature_code:
    :ivar signature_text:
    :ivar patient1:
    :ivar employee:
    :ivar student:
    :ivar personal_relationship:
    :ivar care_giver:
    :ivar responsible_party:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.Author"

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
    patient1: Optional[CoctMt050000Uv01Patient] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    employee: Optional[CoctMt910000UvEmployee] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    student: Optional[CoctMt910000UvStudent] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    personal_relationship: Optional[CoctMt910000UvPersonalRelationship] = field(
        default=None,
        metadata=dict(
            name="personalRelationship",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    care_giver: Optional[CoctMt910000UvCareGiver] = field(
        default=None,
        metadata=dict(
            name="careGiver",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    responsible_party: Optional[CoctMt040200Uv01ResponsibleParty] = field(
        default=None,
        metadata=dict(
            name="responsibleParty",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    assigned_person: Optional[CoctMt090102Uv02AssignedPerson] = field(
        default=None,
        metadata=dict(
            name="assignedPerson",
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
class RepcMt000300Uv01DataEnterer:
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
        name = "REPC_MT000300UV01.DataEnterer"

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
    mode_code: Optional[Cv] = field(
        default=None,
        metadata=dict(
            name="modeCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    signature_code: Optional[Cv] = field(
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
    assigned_person: Optional[CoctMt090102Uv02AssignedPerson] = field(
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
            type="Attribute"
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
class RepcMt000300Uv01Informant:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar mode_code:
    :ivar patient1:
    :ivar employee:
    :ivar student:
    :ivar personal_relationship:
    :ivar care_giver:
    :ivar responsible_party:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.Informant"

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
    mode_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="modeCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    patient1: Optional[CoctMt050000Uv01Patient] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    employee: Optional[CoctMt910000UvEmployee] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    student: Optional[CoctMt910000UvStudent] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    personal_relationship: Optional[CoctMt910000UvPersonalRelationship] = field(
        default=None,
        metadata=dict(
            name="personalRelationship",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    care_giver: Optional[CoctMt910000UvCareGiver] = field(
        default=None,
        metadata=dict(
            name="careGiver",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    responsible_party: Optional[CoctMt040200Uv01ResponsibleParty] = field(
        default=None,
        metadata=dict(
            name="responsibleParty",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    assigned_person: Optional[CoctMt090102Uv02AssignedPerson] = field(
        default=None,
        metadata=dict(
            name="assignedPerson",
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
        default=ParticipationType.INF,
        metadata=dict(
            name="typeCode",
            type="Attribute"
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
class RepcMt000300Uv01Links:
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
        name = "REPC_MT000300UV01.Links"

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
    concern: Optional["RepcMt000300Uv01Concern"] = field(
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, RepcMt000300Uv01LinksValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=RepcMt000300Uv01LinksValue.ELNK,
        metadata=dict(
            name="typeCode",
            type="Attribute",
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
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000300Uv01Organization:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar name:
    :ivar telecom:
    :ivar addr:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.Organization"

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
    name: List[OnExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    telecom: List[TelExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    addr: List[AdExplicit] = field(
        default_factory=list,
        metadata=dict(
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
    class_code: Optional[EntityClassOrganization] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata=dict(
            name="determinerCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000300Uv01Performer:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar mode_code:
    :ivar patient1:
    :ivar employee:
    :ivar student:
    :ivar personal_relationship:
    :ivar care_giver:
    :ivar responsible_party:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.Performer"

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
    patient1: Optional[CoctMt050000Uv01Patient] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    employee: Optional[CoctMt910000UvEmployee] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    student: Optional[CoctMt910000UvStudent] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    personal_relationship: Optional[CoctMt910000UvPersonalRelationship] = field(
        default=None,
        metadata=dict(
            name="personalRelationship",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    care_giver: Optional[CoctMt910000UvCareGiver] = field(
        default=None,
        metadata=dict(
            name="careGiver",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    responsible_party: Optional[CoctMt040200Uv01ResponsibleParty] = field(
        default=None,
        metadata=dict(
            name="responsibleParty",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    assigned_person: Optional[CoctMt090102Uv02AssignedPerson] = field(
        default=None,
        metadata=dict(
            name="assignedPerson",
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
class RepcMt000300Uv01Place:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar name:
    :ivar addr:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.Place"

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
    name: List[EnExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    addr: Optional[AdExplicit] = field(
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
    class_code: Optional[EntityClassPlace] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata=dict(
            name="determinerCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000300Uv01Reason:
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
        name = "REPC_MT000300UV01.Reason"

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
        default="false",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000300Uv01RecordTarget:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar patient:
    :ivar maintained_entity:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.RecordTarget"

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
    patient: Optional[CoctMt050000Uv01Patient] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    maintained_entity: Optional[RepcMt000700Uv01MaintainedEntity] = field(
        default=None,
        metadata=dict(
            name="maintainedEntity",
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
        default=ParticipationType.RCT,
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
class RepcMt000300Uv01Reference:
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
        name = "REPC_MT000300UV01.Reference"

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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, RepcMt000300Uv01ReferenceValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=RepcMt000300Uv01ReferenceValue.REFR,
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
class RepcMt000300Uv01ReplacementOf:
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
        name = "REPC_MT000300UV01.ReplacementOf"

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
    concern: Optional["RepcMt000300Uv01Concern"] = field(
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "RepcMt000300Uv01ReplacementOf.Value", ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=ActRelationshipSequel.RPLC,
        metadata=dict(
            name="typeCode",
            type="Attribute",
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
class RepcMt000300Uv01ResponsibleParty:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.ResponsibleParty"

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
    assigned_person: Optional[CoctMt090102Uv02AssignedPerson] = field(
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
        default=ParticipationType.RESP,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000300Uv01ResponsibleParty2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.ResponsibleParty2"

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
    assigned_person: Optional[CoctMt090102Uv02AssignedPerson] = field(
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
        default=ParticipationType.RESP,
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
class RepcMt000300Uv01SequelTo:
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
        name = "REPC_MT000300UV01.SequelTo"

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
    concern: Optional["RepcMt000300Uv01Concern"] = field(
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
    type_code: Optional[ActRelationshipSequel] = field(
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
class RepcMt000300Uv01Subject2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar awareness_code:
    :ivar patient1:
    :ivar maintained_entity1:
    :ivar employee:
    :ivar student:
    :ivar personal_relationship:
    :ivar care_giver:
    :ivar responsible_party:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.Subject2"

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
    awareness_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="awarenessCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    patient1: Optional[CoctMt050000Uv01Patient] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    maintained_entity1: Optional[RepcMt000700Uv01MaintainedEntity] = field(
        default=None,
        metadata=dict(
            name="maintainedEntity1",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    employee: Optional[CoctMt910000UvEmployee] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    student: Optional[CoctMt910000UvStudent] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    personal_relationship: Optional[CoctMt910000UvPersonalRelationship] = field(
        default=None,
        metadata=dict(
            name="personalRelationship",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    care_giver: Optional[CoctMt910000UvCareGiver] = field(
        default=None,
        metadata=dict(
            name="careGiver",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    responsible_party: Optional[CoctMt040200Uv01ResponsibleParty] = field(
        default=None,
        metadata=dict(
            name="responsibleParty",
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
    type_code: ParticipationTargetSubject = field(
        init=False,
        default=ParticipationTargetSubject.SBJ,
        metadata=dict(
            name="typeCode",
            type="Attribute"
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
class RepcMt000300Uv01Subject4:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar priority_number:
    :ivar conjunction_code:
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
        name = "REPC_MT000300UV01.Subject4"

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
    priority_number: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="priorityNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
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
    act_reference1: Optional[RepcMt000100Uv01ActReference] = field(
        default=None,
        metadata=dict(
            name="actReference1",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    act: Optional[RepcMt000100Uv01Act] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    encounter: Optional[RepcMt000100Uv01Encounter] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    observation: Optional[RepcMt000100Uv01Observation] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    organizer: Optional[RepcMt000100Uv01Organizer] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    procedure: Optional[RepcMt000100Uv01Procedure] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    substance_administration: Optional[RepcMt000100Uv01SubstanceAdministration] = field(
        default=None,
        metadata=dict(
            name="substanceAdministration",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    supply: Optional[RepcMt000100Uv01Supply] = field(
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, RepcMt000300Uv01Subject4Value, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=RepcMt000300Uv01Subject4Value.SUBJ,
        metadata=dict(
            name="typeCode",
            type="Attribute",
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
class RepcMt000300Uv01Verifier:
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
        name = "REPC_MT000300UV01.Verifier"

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
    assigned_person: Optional[CoctMt090102Uv02AssignedPerson] = field(
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
class RepcMt000300Uv01Annotation:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar text:
    :ivar status_code:
    :ivar confidentiality_code:
    :ivar author:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.Annotation"

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
    confidentiality_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    author: List[RepcMt000300Uv01Author] = field(
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
    class_code: ActClassRoot = field(
        init=False,
        default=ActClassRoot.ACT,
        metadata=dict(
            name="classCode",
            type="Attribute"
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata=dict(
            name="moodCode",
            type="Attribute"
        )
    )


@dataclass
class RepcMt000300Uv01ControlActEvent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar status_code:
    :ivar effective_time:
    :ivar reason_code:
    :ivar responsible_party:
    :ivar author:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.ControlActEvent"

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
            namespace="urn:hl7-org:v3"
        )
    )
    code: Optional[Cv] = field(
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
    effective_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    reason_code: Optional[Cv] = field(
        default=None,
        metadata=dict(
            name="reasonCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    responsible_party: Optional[RepcMt000300Uv01ResponsibleParty] = field(
        default=None,
        metadata=dict(
            name="responsibleParty",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    author: List[RepcMt000300Uv01Author] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
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
    class_code: ActClassControlAct = field(
        init=False,
        default=ActClassControlAct.CACT,
        metadata=dict(
            name="classCode",
            type="Attribute"
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata=dict(
            name="moodCode",
            type="Attribute"
        )
    )


@dataclass
class RepcMt000300Uv01HealthCareFacility:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar location:
    :ivar service_provider_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.HealthCareFacility"

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
            namespace="urn:hl7-org:v3"
        )
    )
    code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    location: Optional[RepcMt000300Uv01Place] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    service_provider_organization: Optional[RepcMt000300Uv01Organization] = field(
        default=None,
        metadata=dict(
            name="serviceProviderOrganization",
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
    class_code: Optional[RoleClassServiceDeliveryLocation] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000300Uv01Location:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar health_care_facility:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.Location"

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
    health_care_facility: Optional[RepcMt000300Uv01HealthCareFacility] = field(
        default=None,
        metadata=dict(
            name="healthCareFacility",
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
    type_code: Optional[ParticipationTargetLocation] = field(
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
class RepcMt000300Uv01Subject3:
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
        name = "REPC_MT000300UV01.Subject3"

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
    annotation: Optional[RepcMt000300Uv01Annotation] = field(
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, RepcMt000300Uv01Subject3Value, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=RepcMt000300Uv01Subject3Value.SUBJ,
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
        init=False,
        default="false",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000300Uv01Subject5:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar control_act_event:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT000300UV01.Subject5"

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
    control_act_event: Optional[RepcMt000300Uv01ControlActEvent] = field(
        default=None,
        metadata=dict(
            name="controlActEvent",
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, RepcMt000300Uv01Subject5Value, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=RepcMt000300Uv01Subject5Value.SUBJ,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            pattern=r"[^\s]+"
        )
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.ON,
        metadata=dict(
            name="contextControlCode",
            type="Attribute"
        )
    )
    context_conduction_ind: str = field(
        init=False,
        default="false",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )


@dataclass
class RepcMt000300Uv01Concern:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar status_code:
    :ivar effective_time:
    :ivar confidentiality_code:
    :ivar subject1:
    :ivar record_target:
    :ivar responsible_party:
    :ivar performer:
    :ivar author:
    :ivar data_enterer:
    :ivar informant:
    :ivar verifier:
    :ivar location:
    :ivar links:
    :ivar replacement_of:
    :ivar sequel_to:
    :ivar subject2:
    :ivar reference:
    :ivar component:
    :ivar reason_of:
    :ivar subject_of1:
    :ivar subject_of2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT000300UV01.Concern"

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
    confidentiality_code: Optional[Cv] = field(
        default=None,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    subject1: Optional[RepcMt000300Uv01Subject2] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    record_target: Optional[RepcMt000300Uv01RecordTarget] = field(
        default=None,
        metadata=dict(
            name="recordTarget",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    responsible_party: Optional[RepcMt000300Uv01ResponsibleParty2] = field(
        default=None,
        metadata=dict(
            name="responsibleParty",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    performer: List[RepcMt000300Uv01Performer] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    author: List[RepcMt000300Uv01Author] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    data_enterer: Optional[RepcMt000300Uv01DataEnterer] = field(
        default=None,
        metadata=dict(
            name="dataEnterer",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    informant: List[RepcMt000300Uv01Informant] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    verifier: List[RepcMt000300Uv01Verifier] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    location: List[RepcMt000300Uv01Location] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    links: List[RepcMt000300Uv01Links] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    replacement_of: Optional[RepcMt000300Uv01ReplacementOf] = field(
        default=None,
        metadata=dict(
            name="replacementOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    sequel_to: List[RepcMt000300Uv01SequelTo] = field(
        default_factory=list,
        metadata=dict(
            name="sequelTo",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    subject2: List[RepcMt000300Uv01Subject4] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    reference: List[RepcMt000300Uv01Reference] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component: List["RepcMt000300Uv01Component"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reason_of: List[RepcMt000300Uv01Reason] = field(
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
    subject_of1: Optional[RepcMt000300Uv01Subject5] = field(
        default=None,
        metadata=dict(
            name="subjectOf1",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    subject_of2: List[RepcMt000300Uv01Subject3] = field(
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
    mood_code: Optional[ActMood] = field(
        default=None,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt000300Uv01Component:
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
        name = "REPC_MT000300UV01.Component"

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
        init=False,
        default="true",
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            pattern=r"true|false"
        )
    )
