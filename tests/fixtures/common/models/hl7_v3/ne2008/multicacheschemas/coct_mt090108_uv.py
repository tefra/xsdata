from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    Ii,
    PnExplicit,
    TelExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt150007_uv import (
    CoctMt150007UvOrganization,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    EntityClass,
    EntityDeterminer,
    NullFlavor,
    RoleClassAssignedEntity,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt090108UvPerson:
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
        name = "COCT_MT090108UV.Person"

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
    name: List[PnExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
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
class CoctMt090108UvAssignedPerson:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar addr:
    :ivar telecom:
    :ivar assigned_person:
    :ivar represented_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "COCT_MT090108UV.AssignedPerson"

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
    addr: List[AdExplicit] = field(
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
    assigned_person: Optional[CoctMt090108UvPerson] = field(
        default=None,
        metadata=dict(
            name="assignedPerson",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    represented_organization: Optional[CoctMt150007UvOrganization] = field(
        default=None,
        metadata=dict(
            name="representedOrganization",
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
    class_code: RoleClassAssignedEntity = field(
        default=RoleClassAssignedEntity.ASSIGNED,
        metadata=dict(
            name="classCode",
            type="Attribute"
        )
    )
