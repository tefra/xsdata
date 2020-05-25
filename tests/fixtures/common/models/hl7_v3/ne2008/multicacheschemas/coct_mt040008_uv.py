from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Ce,
    Cs,
    Ii,
    IvlTsExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt030207_uv import (
    CoctMt030207UvPerson,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt140007_uv import (
    CoctMt140007UvDevice,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt150007_uv import (
    CoctMt150007UvOrganization,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    NullFlavor,
    RoleClassAgent,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt040008UvResponsible:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar effective_time:
    :ivar agent_organization:
    :ivar agent_person:
    :ivar agent_device:
    :ivar represented_organization:
    :ivar represented_person:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "COCT_MT040008UV.Responsible"

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
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    agent_organization: Optional[CoctMt150007UvOrganization] = field(
        default=None,
        metadata=dict(
            name="agentOrganization",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    agent_person: Optional[CoctMt030207UvPerson] = field(
        default=None,
        metadata=dict(
            name="agentPerson",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    agent_device: Optional[CoctMt140007UvDevice] = field(
        default=None,
        metadata=dict(
            name="agentDevice",
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
    represented_person: Optional[CoctMt030207UvPerson] = field(
        default=None,
        metadata=dict(
            name="representedPerson",
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
    class_code: RoleClassAgent = field(
        default=RoleClassAgent.AGNT,
        metadata=dict(
            name="classCode",
            type="Attribute"
        )
    )
