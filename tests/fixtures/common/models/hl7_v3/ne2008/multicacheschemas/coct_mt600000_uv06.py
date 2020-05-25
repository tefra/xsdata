from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Any,
    Cd,
    Ce,
    Cs,
    EnExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    PnExplicit,
    St,
    TsExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    ActClass,
    ActClassObservation,
    ActClassSupply,
    ActMood,
    ActMoodIntent,
    ActRelationshipCostTracking,
    ActRelationshipFulfills,
    ActRelationshipHasSupport,
    ActRelationshipPosting,
    ActRelationshipTemporallyPertains,
    EntityClass,
    EntityClassMaterial,
    EntityDeterminer,
    NullFlavor,
    ParticipationPhysicalPerformer,
    ParticipationTargetLocation,
    ParticipationType,
    RoleClassManufacturedProduct,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    XAccommodationRequestorRole,
    XDocumentEntrySubject,
    XDocumentSubject,
    XInformationRecipientRole,
    XRoleClassAccommodationRequestor,
    XRoleClassCoverage,
    XRoleClassCoverageInvoice,
    XRoleClassCredentialedEntity,
    XRoleClassPayeePolicyRelationship,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt240000_uv01 import (
    CoctMt240000Uv01ServiceDeliveryLocation,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt240003_uv02 import (
    CoctMt240003Uv02ServiceDeliveryLocation,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt600000Uv06Destination:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar service_delivery_location:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.Destination"

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
        default=ParticipationType.DST,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt600000Uv06Diagnosis:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar text:
    :ivar effective_time:
    :ivar value:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.Diagnosis"

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
    text: Optional[St] = field(
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
    value: Optional[Cd] = field(
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
class CoctMt600000Uv06Location:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar service_delivery_location:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.Location"

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
    service_delivery_location: Optional[CoctMt240000Uv01ServiceDeliveryLocation] = field(
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
class CoctMt600000Uv06Origin:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar service_delivery_location:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.Origin"

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
        default=ParticipationType.ORG,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt600000Uv06ProviderPerson:
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
        name = "COCT_MT600000UV06.ProviderPerson"

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
class CoctMt600000Uv06SupplyObservationEvent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar target_site_code:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.SupplyObservationEvent"

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
    target_site_code: Optional[Cd] = field(
        default=None,
        metadata=dict(
            name="targetSiteCode",
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
class CoctMt600000Uv06VisionPrescriptionObservationEvent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar value:
    :ivar target_site_code:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.VisionPrescriptionObservationEvent"

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
    value: Optional[Any] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    target_site_code: Optional[Cd] = field(
        default=None,
        metadata=dict(
            name="targetSiteCode",
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
class CoctMt600000Uv06VisionProduct:
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
        name = "COCT_MT600000UV06.VisionProduct"

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
    name: Optional[EnExplicit] = field(
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
class CoctMt600000Uv06HealthCareProvider:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar health_care_provider_person:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.HealthCareProvider"

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
    code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    health_care_provider_person: Optional[CoctMt600000Uv06ProviderPerson] = field(
        default=None,
        metadata=dict(
            name="healthCareProviderPerson",
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
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, "CoctMt600000Uv06HealthCareProvider.Value", XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassMutualRelationship.PROV,
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
class CoctMt600000Uv06PertinentInformation:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar diagnosis:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.PertinentInformation"

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
    diagnosis: Optional[CoctMt600000Uv06Diagnosis] = field(
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
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "CoctMt600000Uv06PertinentInformation.Value"]] = field(
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
class CoctMt600000Uv06PertinentInformation1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar vision_prescription_observation_event:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.PertinentInformation1"

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
    vision_prescription_observation_event: Optional[CoctMt600000Uv06VisionPrescriptionObservationEvent] = field(
        default=None,
        metadata=dict(
            name="visionPrescriptionObservationEvent",
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
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "CoctMt600000Uv06PertinentInformation1.Value"]] = field(
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
class CoctMt600000Uv06Product2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar supply_observation_event:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.Product2"

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
    supply_observation_event: Optional[CoctMt600000Uv06SupplyObservationEvent] = field(
        default=None,
        metadata=dict(
            name="supplyObservationEvent",
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
        default=ParticipationType.PRD,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt600000Uv06Author:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar health_care_provider:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.Author"

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
    health_care_provider: Optional[CoctMt600000Uv06HealthCareProvider] = field(
        default=None,
        metadata=dict(
            name="healthCareProvider",
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


@dataclass
class CoctMt600000Uv06ManufacturedProduct:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar manufactured_vision_product:
    :ivar product_of:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.ManufacturedProduct"

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
    manufactured_vision_product: Optional[CoctMt600000Uv06VisionProduct] = field(
        default=None,
        metadata=dict(
            name="manufacturedVisionProduct",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    product_of: List[CoctMt600000Uv06Product2] = field(
        default_factory=list,
        metadata=dict(
            name="productOf",
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
    class_code: Optional[RoleClassManufacturedProduct] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt600000Uv06Performer:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar health_care_provider:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.Performer"

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
    health_care_provider: Optional[CoctMt600000Uv06HealthCareProvider] = field(
        default=None,
        metadata=dict(
            name="healthCareProvider",
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


@dataclass
class CoctMt600000Uv06PrescriptionOrder:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar effective_time:
    :ivar author:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.PrescriptionOrder"

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
    effective_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    author: Optional[CoctMt600000Uv06Author] = field(
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
        default=ActMood.RQO,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt600000Uv06Product:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar manufactured_product:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.Product"

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
    manufactured_product: Optional[CoctMt600000Uv06ManufacturedProduct] = field(
        default=None,
        metadata=dict(
            name="manufacturedProduct",
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
        default=ParticipationType.PRD,
        metadata=dict(
            name="typeCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CoctMt600000Uv06InFulfillmentOf:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar prescription_order:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.InFulfillmentOf"

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
    prescription_order: Optional[CoctMt600000Uv06PrescriptionOrder] = field(
        default=None,
        metadata=dict(
            name="prescriptionOrder",
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
class CoctMt600000Uv06PrescriptionIntent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar in_fulfillment_of:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.PrescriptionIntent"

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
    in_fulfillment_of: Optional[CoctMt600000Uv06InFulfillmentOf] = field(
        default=None,
        metadata=dict(
            name="inFulfillmentOf",
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


@dataclass
class CoctMt600000Uv06PertinentInformation2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar prescription_intent:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.PertinentInformation2"

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
    prescription_intent: Optional[CoctMt600000Uv06PrescriptionIntent] = field(
        default=None,
        metadata=dict(
            name="prescriptionIntent",
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
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "CoctMt600000Uv06PertinentInformation2.Value"]] = field(
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
class CoctMt600000Uv06SupplyEvent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar effective_time:
    :ivar priority_code:
    :ivar product:
    :ivar performer:
    :ivar origin:
    :ivar destination:
    :ivar location:
    :ivar pertinent_information1:
    :ivar pertinent_information2:
    :ivar pertinent_information3:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT600000UV06.SupplyEvent"

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
    product: List[CoctMt600000Uv06Product] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=2
        )
    )
    performer: Optional[CoctMt600000Uv06Performer] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    origin: Optional[CoctMt600000Uv06Origin] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    destination: Optional[CoctMt600000Uv06Destination] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    location: Optional[CoctMt600000Uv06Location] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    pertinent_information1: List[CoctMt600000Uv06PertinentInformation1] = field(
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
    pertinent_information2: Optional[CoctMt600000Uv06PertinentInformation2] = field(
        default=None,
        metadata=dict(
            name="pertinentInformation2",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True,
            nillable=True
        )
    )
    pertinent_information3: List[CoctMt600000Uv06PertinentInformation] = field(
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
