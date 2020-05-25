from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    ActClass,
    ActClassObservation,
    ActClassRoot,
    ActMood,
    ActRelationshipCostTracking,
    ActRelationshipFulfills,
    ActRelationshipHasSupport,
    ActRelationshipPosting,
    ActRelationshipTemporallyPertains,
    EntityClass,
    EntityDeterminer,
    NullFlavor,
    ParticipationTargetLocation,
    ParticipationType,
    XActMoodIntentEvent,
    XRoleClassAccommodationRequestor,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt240003_uv02 import (
    CoctMt240003Uv02ServiceDeliveryLocation,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Cs,
    Ii,
    IvlTsExplicit,
    PnExplicit,
    TsExplicit,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt310000Uv04AcommodationRequestor:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar name:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.AcommodationRequestor"

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
    name: Optional[PnExplicit] = field(
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
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.PSN,
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
class CoctMt310000Uv04Location:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar service_delivery_location:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.Location"

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
    service_delivery_location: Optional[CoctMt240003Uv02ServiceDeliveryLocation] = field(
        default=None,
        metadata=dict(
            name="serviceDeliveryLocation",
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
    type_code: Optional[ParticipationTargetLocation] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt310000Uv04MedicalService:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.MedicalService"

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
    code: Optional[Cs] = field(
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
        default=ActMood.EVN,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt310000Uv04MinimumAvailableAccommodation:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.MinimumAvailableAccommodation"

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
    code: Optional[Cs] = field(
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
class CoctMt310000Uv04AccommodationRequestorRole:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar accommodation_requestor:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.AccommodationRequestorRole"

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
    code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    accommodation_requestor: Optional[CoctMt310000Uv04AcommodationRequestor] = field(
        default=None,
        metadata=dict(
            name="accommodationRequestor",
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
    class_code: Optional[XRoleClassAccommodationRequestor] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt310000Uv04PertinentInformation1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar minimum_available_accommodation:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.PertinentInformation1"

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
    minimum_available_accommodation: Optional[CoctMt310000Uv04MinimumAvailableAccommodation] = field(
        default=None,
        metadata=dict(
            name="minimumAvailableAccommodation",
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
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "CoctMt310000Uv04PertinentInformation1.Value"]] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
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
class CoctMt310000Uv04PertinentInformation3:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar medical_service:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.PertinentInformation3"

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
    medical_service: Optional[CoctMt310000Uv04MedicalService] = field(
        default=None,
        metadata=dict(
            name="medicalService",
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
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "CoctMt310000Uv04PertinentInformation3.Value"]] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
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
class CoctMt310000Uv04Author:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar accommodation_requestor_role:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.Author"

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
    accommodation_requestor_role: Optional[CoctMt310000Uv04AccommodationRequestorRole] = field(
        default=None,
        metadata=dict(
            name="accommodationRequestorRole",
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
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.AUT,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt310000Uv04Encounter:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar effective_time:
    :ivar pertinent_information:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.Encounter"

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
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    pertinent_information: Optional[CoctMt310000Uv04PertinentInformation3] = field(
        default=None,
        metadata=dict(
            name="pertinentInformation",
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
        default=ActMood.EVN,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt310000Uv04AccommodationRequested:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar effective_time:
    :ivar author:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.AccommodationRequested"

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
    code: Optional[Cs] = field(
        default=None,
        metadata=dict(
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
            namespace="urn:hl7-org:v3"
        )
    )
    author: Optional[CoctMt310000Uv04Author] = field(
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
        default=ActMood.RQO,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt310000Uv04PertinentInformation2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar encounter:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.PertinentInformation2"

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
    encounter: Optional[CoctMt310000Uv04Encounter] = field(
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
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "CoctMt310000Uv04PertinentInformation2.Value"]] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
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
class CoctMt310000Uv04InFulfillmentOf:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar accommodation_requested:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.InFulfillmentOf"

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
    accommodation_requested: Optional[CoctMt310000Uv04AccommodationRequested] = field(
        default=None,
        metadata=dict(
            name="accommodationRequested",
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
    type_code: Optional[ActRelationshipFulfills] = field(
        default=None,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt310000Uv04AccomodationSupplied:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar effective_time:
    :ivar reason_code:
    :ivar location:
    :ivar in_fulfillment_of:
    :ivar pertinent_information1:
    :ivar pertinent_information2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT310000UV04.AccomodationSupplied"

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
    code: Optional[Cs] = field(
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
    reason_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="reasonCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    location: Optional[CoctMt310000Uv04Location] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    in_fulfillment_of: Optional[CoctMt310000Uv04InFulfillmentOf] = field(
        default=None,
        metadata=dict(
            name="inFulfillmentOf",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    pertinent_information1: Optional[CoctMt310000Uv04PertinentInformation1] = field(
        default=None,
        metadata=dict(
            name="pertinentInformation1",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    pertinent_information2: Optional[CoctMt310000Uv04PertinentInformation2] = field(
        default=None,
        metadata=dict(
            name="pertinentInformation2",
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
    class_code: ActClass = field(
        init=False,
        default=ActClass.ACCM,
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
