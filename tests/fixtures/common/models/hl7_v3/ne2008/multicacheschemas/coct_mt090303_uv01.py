from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    Ii,
    Sc,
    TelExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt150003_uv03 import (
    CoctMt150003Uv03Organization,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    EntityClassDevice,
    EntityDeterminer,
    NullFlavor,
    RoleClassAssignedEntity,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt090303Uv01Device:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar manufacturer_model_name:
    :ivar software_name:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "COCT_MT090303UV01.Device"

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
    manufacturer_model_name: Optional[Sc] = field(
        default=None,
        metadata=dict(
            name="manufacturerModelName",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    software_name: Optional[Sc] = field(
        default=None,
        metadata=dict(
            name="softwareName",
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
    class_code: Optional[EntityClassDevice] = field(
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
class CoctMt090303Uv01AssignedDevice:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar addr:
    :ivar telecom:
    :ivar assigned_device:
    :ivar represented_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "COCT_MT090303UV01.AssignedDevice"

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
    assigned_device: Optional[CoctMt090303Uv01Device] = field(
        default=None,
        metadata=dict(
            name="assignedDevice",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    represented_organization: Optional[CoctMt150003Uv03Organization] = field(
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
    class_code: Optional[RoleClassAssignedEntity] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
