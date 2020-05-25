from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    ActClassCareProvision,
    ActMood,
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
    NullFlavor,
    ParticipationPhysicalPerformer,
    ParticipationTargetSubject,
    ParticipationType,
    ParticipationVerifier,
    XActMoodOrdPrms,
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
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt010000_uv01 import (
    CoctMt010000Uv01Encounter,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt040200_uv01 import (
    CoctMt040200Uv01ResponsibleParty,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt050000_uv01 import (
    CoctMt050000Uv01Patient,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt090100_uv01 import (
    CoctMt090100Uv01AssignedPerson,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt090400_uv import (
    CoctMt090400UvAssignedParty,
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
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.repc_mt000200_uv import (
    RepcMt000200UvCarePlan,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.repc_mt000301_uv import (
    RepcMt000301UvConditionEvent,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.repc_mt000400_uv01 import (
    RepcMt000400Uv01ActCategory,
    RepcMt000400Uv01ActList,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.repc_mt000700_uv01 import (
    RepcMt000700Uv01MaintainedEntity,
)

__NAMESPACE__ = "urn:hl7-org:v3"


class RepcMt004000Uv01ReferenceValue(Enum):
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
class RepcMt004000Uv01Author:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar note_text:
    :ivar time:
    :ivar mode_code:
    :ivar signature_code:
    :ivar signature_text:
    :ivar assigned_party1:
    :ivar patient1:
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
        name = "REPC_MT004000UV01.Author"

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
    note_text: Optional[St] = field(
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
    assigned_party1: Optional[CoctMt090400UvAssignedParty] = field(
        default=None,
        metadata=dict(
            name="assignedParty1",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
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
class RepcMt004000Uv01CareProvisionRequestOrPromise:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "REPC_MT004000UV01.CareProvisionRequestOrPromise"

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
    mood_code: Optional[XActMoodOrdPrms] = field(
        default=None,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RepcMt004000Uv01Component:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar care_plan:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT004000UV01.Component"

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
    care_plan: Optional[RepcMt000200UvCarePlan] = field(
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
class RepcMt004000Uv01DataEnterer:
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
        name = "REPC_MT004000UV01.DataEnterer"

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
class RepcMt004000Uv01Performer:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar function_code:
    :ivar time:
    :ivar mode_code:
    :ivar assigned_party1:
    :ivar patient1:
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
        name = "REPC_MT004000UV01.Performer"

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
    assigned_party1: Optional[CoctMt090400UvAssignedParty] = field(
        default=None,
        metadata=dict(
            name="assignedParty1",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
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
class RepcMt004000Uv01PertinentInformation:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar care_plan:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT004000UV01.PertinentInformation"

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
    care_plan: Optional[RepcMt000200UvCarePlan] = field(
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
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "RepcMt004000Uv01PertinentInformation.Value"]] = field(
        default=None,
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
    context_conduction_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            required=True,
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
class RepcMt004000Uv01PertinentInformation4:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar act_category:
    :ivar act_list:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT004000UV01.PertinentInformation4"

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
    act_category: Optional[RepcMt000400Uv01ActCategory] = field(
        default=None,
        metadata=dict(
            name="actCategory",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    act_list: Optional[RepcMt000400Uv01ActList] = field(
        default=None,
        metadata=dict(
            name="actList",
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
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "RepcMt004000Uv01PertinentInformation4.Value"]] = field(
        default=None,
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
class RepcMt004000Uv01PertinentInformation5:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
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
        name = "REPC_MT004000UV01.PertinentInformation5"

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
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "RepcMt004000Uv01PertinentInformation5.Value"]] = field(
        default=None,
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
    context_conduction_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            required=True,
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
class RepcMt004000Uv01PrimaryInformationRecipient:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_party1:
    :ivar patient1:
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
        name = "REPC_MT004000UV01.PrimaryInformationRecipient"

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
    assigned_party1: Optional[CoctMt090400UvAssignedParty] = field(
        default=None,
        metadata=dict(
            name="assignedParty1",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
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
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.PRCP,
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
class RepcMt004000Uv01Reason:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar condition_event:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT004000UV01.Reason"

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
    condition_event: Optional[RepcMt000301UvConditionEvent] = field(
        default=None,
        metadata=dict(
            name="conditionEvent",
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
class RepcMt004000Uv01RecordTarget:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar maintained_entity:
    :ivar patient:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT004000UV01.RecordTarget"

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
    maintained_entity: Optional[RepcMt000700Uv01MaintainedEntity] = field(
        default=None,
        metadata=dict(
            name="maintainedEntity",
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
class RepcMt004000Uv01Reference:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar encounter:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT004000UV01.Reference"

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
    encounter: Optional[CoctMt010000Uv01Encounter] = field(
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, RepcMt004000Uv01ReferenceValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=RepcMt004000Uv01ReferenceValue.REFR,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
        )
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
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
class RepcMt004000Uv01ReplacementOf:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar care_provision_event:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT004000UV01.ReplacementOf"

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
    care_provision_event: Optional["RepcMt004000Uv01CareProvisionEvent"] = field(
        default=None,
        metadata=dict(
            name="careProvisionEvent",
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "RepcMt004000Uv01ReplacementOf.Value", ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=ActRelationshipSequel.RPLC,
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
    context_conduction_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="contextConductionInd",
            type="Attribute",
            required=True,
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
class RepcMt004000Uv01Subject3:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar maintained_entity:
    :ivar patient:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "REPC_MT004000UV01.Subject3"

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
    maintained_entity: Optional[RepcMt000700Uv01MaintainedEntity] = field(
        default=None,
        metadata=dict(
            name="maintainedEntity",
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
    type_code: Optional[ParticipationTargetSubject] = field(
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
class RepcMt004000Uv01Verifier:
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
        name = "REPC_MT004000UV01.Verifier"

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
class RepcMt004000Uv01InFulfillmentOf2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar care_provision_request_or_promise:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "REPC_MT004000UV01.InFulfillmentOf2"

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
    care_provision_request_or_promise: Optional[RepcMt004000Uv01CareProvisionRequestOrPromise] = field(
        default=None,
        metadata=dict(
            name="careProvisionRequestOrPromise",
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
    type_code: Optional[ActRelationshipFulfills] = field(
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
class RepcMt004000Uv01CareProvisionEvent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar priority_code:
    :ivar confidentiality_code:
    :ivar reason_code:
    :ivar subject:
    :ivar record_target:
    :ivar performer:
    :ivar author:
    :ivar data_enterer:
    :ivar primary_information_recipient:
    :ivar verifier:
    :ivar in_fulfillment_of:
    :ivar replacement_of:
    :ivar reason:
    :ivar reference:
    :ivar pertinent_information1:
    :ivar pertinent_information2:
    :ivar pertinent_information3:
    :ivar component:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "REPC_MT004000UV01.CareProvisionEvent"

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
    subject: List[RepcMt004000Uv01Subject3] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    record_target: Optional[RepcMt004000Uv01RecordTarget] = field(
        default=None,
        metadata=dict(
            name="recordTarget",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    performer: List[RepcMt004000Uv01Performer] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    author: Optional[RepcMt004000Uv01Author] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    data_enterer: Optional[RepcMt004000Uv01DataEnterer] = field(
        default=None,
        metadata=dict(
            name="dataEnterer",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    primary_information_recipient: Optional[RepcMt004000Uv01PrimaryInformationRecipient] = field(
        default=None,
        metadata=dict(
            name="primaryInformationRecipient",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    verifier: List[RepcMt004000Uv01Verifier] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    in_fulfillment_of: List[RepcMt004000Uv01InFulfillmentOf2] = field(
        default_factory=list,
        metadata=dict(
            name="inFulfillmentOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=2,
            nillable=True
        )
    )
    replacement_of: List[RepcMt004000Uv01ReplacementOf] = field(
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
    reason: List[RepcMt004000Uv01Reason] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    reference: List[RepcMt004000Uv01Reference] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    pertinent_information1: List[RepcMt004000Uv01PertinentInformation] = field(
        default_factory=list,
        metadata=dict(
            name="pertinentInformation1",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    pertinent_information2: List[RepcMt004000Uv01PertinentInformation4] = field(
        default_factory=list,
        metadata=dict(
            name="pertinentInformation2",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    pertinent_information3: List[RepcMt004000Uv01PertinentInformation5] = field(
        default_factory=list,
        metadata=dict(
            name="pertinentInformation3",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component: List[RepcMt004000Uv01Component] = field(
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
