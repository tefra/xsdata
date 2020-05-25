from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Any,
    Ce,
    Cs,
    EdExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    St,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    ActClass,
    ActClassPosition,
    ActMood,
    ActRelationshipHasComponent,
    ContextControl,
    NullFlavor,
    ParticipationTargetDevice,
    ParticipationType,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt090108_uv import (
    CoctMt090108UvAssignedPerson,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt090303_uv01 import (
    CoctMt090303Uv01AssignedDevice,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt960000Uv05Author:
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
        name = "COCT_MT960000UV05.Author"

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
    assigned_person: Optional[CoctMt090108UvAssignedPerson] = field(
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
        default=ParticipationType.AUT,
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
class CoctMt960000Uv05Device1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_device:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.Device1"

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
    assigned_device: Optional[CoctMt090303Uv01AssignedDevice] = field(
        default=None,
        metadata=dict(
            name="assignedDevice",
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
    type_code: Optional[ParticipationTargetDevice] = field(
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


@dataclass
class CoctMt960000Uv05Device2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_device:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.Device2"

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
    assigned_device: Optional[CoctMt090303Uv01AssignedDevice] = field(
        default=None,
        metadata=dict(
            name="assignedDevice",
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
    type_code: Optional[ParticipationTargetDevice] = field(
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


@dataclass
class CoctMt960000Uv05PositionAccuracy:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar value:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.PositionAccuracy"

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
    value: Optional[Ce] = field(
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
    class_code: ActClass = field(
        init=False,
        default=ActClass.POSACC,
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
class CoctMt960000Uv05Component2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar position_accuracy:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "COCT_MT960000UV05.Component2"

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
    position_accuracy: Optional[CoctMt960000Uv05PositionAccuracy] = field(
        default=None,
        metadata=dict(
            name="positionAccuracy",
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
        default=ContextControl.AP,
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
class CoctMt960000Uv05PositionCoordinate:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar text:
    :ivar value:
    :ivar method_code:
    :ivar device:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.PositionCoordinate"

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
    value: Optional[Any] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    method_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="methodCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    device: List[CoctMt960000Uv05Device1] = field(
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
        default=ActClass.POSCOORD,
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
class CoctMt960000Uv05Component1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar position_coordinate:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "COCT_MT960000UV05.Component1"

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
    position_coordinate: Optional[CoctMt960000Uv05PositionCoordinate] = field(
        default=None,
        metadata=dict(
            name="positionCoordinate",
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
class CoctMt960000Uv05Position:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar effective_time:
    :ivar activity_time:
    :ivar value:
    :ivar device:
    :ivar author:
    :ivar component1:
    :ivar component2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.Position"

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
    code: Optional[Ce] = field(
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
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    activity_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            name="activityTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    value: Optional[St] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    device: List[CoctMt960000Uv05Device2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    author: Optional[CoctMt960000Uv05Author] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    component1: List[CoctMt960000Uv05Component1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    component2: Optional[CoctMt960000Uv05Component2] = field(
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
    class_code: Optional[ActClassPosition] = field(
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
