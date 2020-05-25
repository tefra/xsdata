from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.common.models.nhinc.common.nhinc_common import (
    AssertionType,
    NhinTargetSystemType,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201306_uv02 import (
    PrpaIn201306Uv02,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ProxyPrpaIn201306UvproxyRequestType:
    """
    :ivar prpa_in201306_uv02:
    :ivar assertion:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "Proxy_PRPA_IN201306UVProxyRequestType"

    prpa_in201306_uv02: Optional[PrpaIn201306Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201306UV02",
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
    nhin_target_system: Optional[NhinTargetSystemType] = field(
        default=None,
        metadata=dict(
            name="nhinTargetSystem",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class ProxyPrpaIn201306UvproxySecuredRequestType:
    """
    :ivar prpa_in201306_uv02:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "Proxy_PRPA_IN201306UVProxySecuredRequestType"

    prpa_in201306_uv02: Optional[PrpaIn201306Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201306UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    nhin_target_system: Optional[NhinTargetSystemType] = field(
        default=None,
        metadata=dict(
            name="nhinTargetSystem",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class ProxyPrpaIn201306UvproxyRequest(ProxyPrpaIn201306UvproxyRequestType):
    class Meta:
        name = "Proxy_PRPA_IN201306UVProxyRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class ProxyPrpaIn201306UvproxySecuredRequest(ProxyPrpaIn201306UvproxySecuredRequestType):
    class Meta:
        name = "Proxy_PRPA_IN201306UVProxySecuredRequest"
        namespace = "urn:hl7-org:v3"
