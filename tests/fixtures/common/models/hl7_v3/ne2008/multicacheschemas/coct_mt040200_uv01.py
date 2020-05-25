from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    Ii,
    IvlTsExplicit,
    TelExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt030200_uv import (
    CoctMt030200UvPerson,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt150000_uv02 import (
    CoctMt150000Uv02Organization,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    NullFlavor,
    RoleClassAgent,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt040200Uv01ResponsibleParty:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar addr:
    :ivar telecom:
    :ivar status_code:
    :ivar effective_time:
    :ivar agent_organization:
    :ivar agent_person:
    :ivar represented_person:
    :ivar represented_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "COCT_MT040200UV01.ResponsibleParty"

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
    agent_organization: Optional[CoctMt150000Uv02Organization] = field(
        default=None,
        metadata=dict(
            name="agentOrganization",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    agent_person: Optional[CoctMt030200UvPerson] = field(
        default=None,
        metadata=dict(
            name="agentPerson",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    represented_person: Optional[CoctMt030200UvPerson] = field(
        default=None,
        metadata=dict(
            name="representedPerson",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    represented_organization: Optional[CoctMt150000Uv02Organization] = field(
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
    class_code: Optional[RoleClassAgent] = field(
        default=None,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
