from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.common.models.nhinc.common.nhinc_common import (
    AssertionType,
    NhinTargetCommunitiesType,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201301_uv02 import (
    PrpaIn201301Uv02,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201302_uv02 import (
    PrpaIn201302Uv02,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201301UvrequestType:
    """
    :ivar prpa_in201301_uv02:
    :ivar assertion:
    :ivar nhin_target_communities:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVRequestType"

    prpa_in201301_uv02: Optional[PrpaIn201301Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201301UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    assertion: Optional[AssertionType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    nhin_target_communities: Optional[NhinTargetCommunitiesType] = field(
        default=None,
        metadata=dict(
            name="NhinTargetCommunities",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )


@dataclass
class PixconsumerPrpaIn201301UvsecuredRequestType:
    """
    :ivar prpa_in201301_uv02:
    :ivar nhin_target_communities:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVSecuredRequestType"

    prpa_in201301_uv02: Optional[PrpaIn201301Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201301UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    nhin_target_communities: Optional[NhinTargetCommunitiesType] = field(
        default=None,
        metadata=dict(
            name="NhinTargetCommunities",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )


@dataclass
class PixconsumerPrpaIn201302UvrequestType:
    """
    :ivar prpa_in201302_uv02:
    :ivar assertion:
    :ivar nhin_target_communities:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVRequestType"

    prpa_in201302_uv02: Optional[PrpaIn201302Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201302UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    assertion: Optional[AssertionType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    nhin_target_communities: Optional[NhinTargetCommunitiesType] = field(
        default=None,
        metadata=dict(
            name="NhinTargetCommunities",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )


@dataclass
class PixconsumerPrpaIn201302UvsecuredRequestType:
    """
    :ivar prpa_in201302_uv02:
    :ivar nhin_target_communities:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVSecuredRequestType"

    prpa_in201302_uv02: Optional[PrpaIn201302Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201302UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    nhin_target_communities: Optional[NhinTargetCommunitiesType] = field(
        default=None,
        metadata=dict(
            name="NhinTargetCommunities",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )


@dataclass
class PixconsumerPrpaIn201301Uvrequest(PixconsumerPrpaIn201301UvrequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201301UvsecuredRequest(PixconsumerPrpaIn201301UvsecuredRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVSecuredRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201302Uvrequest(PixconsumerPrpaIn201302UvrequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201302UvsecuredRequest(PixconsumerPrpaIn201302UvsecuredRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVSecuredRequest"
        namespace = "urn:hl7-org:v3"
