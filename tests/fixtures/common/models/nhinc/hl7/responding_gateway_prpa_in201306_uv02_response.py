from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.nhinc.common.nhinc_common import (
    NhinTargetCommunityType,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201306_uv02 import (
    PrpaIn201306Uv02,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CommunityPrpaIn201306Uv02ResponseType:
    """
    :ivar prpa_in201306_uv02:
    :ivar nhin_target_community:
    """
    class Meta:
        name = "Community_PRPA_IN201306UV02ResponseType"

    prpa_in201306_uv02: Optional[PrpaIn201306Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201306UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    nhin_target_community: Optional[NhinTargetCommunityType] = field(
        default=None,
        metadata=dict(
            name="nhinTargetCommunity",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class RespondingGatewayPrpaIn201306Uv02ResponseType:
    """
    :ivar community_response:
    """
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02ResponseType"

    community_response: List[CommunityPrpaIn201306Uv02ResponseType] = field(
        default_factory=list,
        metadata=dict(
            name="communityResponse",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class RespondingGatewayPrpaIn201306Uv02Response(RespondingGatewayPrpaIn201306Uv02ResponseType):
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02Response"
        namespace = "urn:hl7-org:v3"
