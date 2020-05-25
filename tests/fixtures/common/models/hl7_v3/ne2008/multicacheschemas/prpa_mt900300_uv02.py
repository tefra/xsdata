from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Cd,
    Ce,
    Cs,
    Cv,
    Ii,
    IntType,
    IvlTsExplicit,
    Sc,
    St,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    NullFlavor,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PrpaMt900300Uv02CareEventId:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT900300UV02.CareEventID"

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
    value: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
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


@dataclass
class PrpaMt900300Uv02EncounterStatus:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT900300UV02.EncounterStatus"

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
    value: List[Cv] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
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


@dataclass
class PrpaMt900300Uv02EncounterTimeframe:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT900300UV02.EncounterTimeframe"

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
    value: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    semantics_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
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


@dataclass
class PrpaMt900300Uv02PatientId:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT900300UV02.PatientId"

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
    value: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
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


@dataclass
class PrpaMt900300Uv02ResponsibleOrganization:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT900300UV02.ResponsibleOrganization"

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
    value: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
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


@dataclass
class PrpaMt900300Uv02SortControl:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar element_name:
    :ivar direction_code:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT900300UV02.SortControl"

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
    element_name: Optional[Sc] = field(
        default=None,
        metadata=dict(
            name="elementName",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    direction_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="directionCode",
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


@dataclass
class PrpaMt900300Uv02TypeOfEncounter:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT900300UV02.TypeOfEncounter"

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
    value: Optional[Cd] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    semantics_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
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


@dataclass
class PrpaMt900300Uv02QueryByParameterPayload:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar query_id:
    :ivar status_code:
    :ivar modify_code:
    :ivar response_element_group_id:
    :ivar response_modality_code:
    :ivar response_priority_code:
    :ivar initial_quantity:
    :ivar initial_quantity_code:
    :ivar care_event_id:
    :ivar encounter_status:
    :ivar encounter_timeframe:
    :ivar patient_id:
    :ivar responsible_organization:
    :ivar sort_control:
    :ivar type_of_encounter:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT900300UV02.QueryByParameterPayload"

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
    query_id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            name="queryId",
            type="Element",
            namespace="urn:hl7-org:v3"
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
    modify_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="modifyCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    response_element_group_id: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            name="responseElementGroupId",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    response_modality_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="responseModalityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    response_priority_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="responsePriorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    initial_quantity: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="initialQuantity",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    initial_quantity_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="initialQuantityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    care_event_id: Optional[PrpaMt900300Uv02CareEventId] = field(
        default=None,
        metadata=dict(
            name="careEventID",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    encounter_status: Optional[PrpaMt900300Uv02EncounterStatus] = field(
        default=None,
        metadata=dict(
            name="encounterStatus",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    encounter_timeframe: Optional[PrpaMt900300Uv02EncounterTimeframe] = field(
        default=None,
        metadata=dict(
            name="encounterTimeframe",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    patient_id: Optional[PrpaMt900300Uv02PatientId] = field(
        default=None,
        metadata=dict(
            name="patientId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    responsible_organization: Optional[PrpaMt900300Uv02ResponsibleOrganization] = field(
        default=None,
        metadata=dict(
            name="responsibleOrganization",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    sort_control: List[PrpaMt900300Uv02SortControl] = field(
        default_factory=list,
        metadata=dict(
            name="sortControl",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    type_of_encounter: Optional[PrpaMt900300Uv02TypeOfEncounter] = field(
        default=None,
        metadata=dict(
            name="typeOfEncounter",
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
