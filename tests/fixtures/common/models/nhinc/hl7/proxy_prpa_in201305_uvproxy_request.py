from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.common.models.nhinc.common.nhinc_common import (
    AssertionType,
    NhinTargetSystemType,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201305_uv02 import (
    PrpaIn201305Uv02,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ProxyPrpaIn201305UvproxyRequestType:
    """
    :ivar prpa_in201305_uv02:
    :ivar assertion:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "Proxy_PRPA_IN201305UVProxyRequestType"

    prpa_in201305_uv02: Optional[PrpaIn201305Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201305UV02",
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
class ProxyPrpaIn201305UvproxySecuredRequestType:
    """
    :ivar prpa_in201305_uv02:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "Proxy_PRPA_IN201305UVProxySecuredRequestType"

    prpa_in201305_uv02: Optional[PrpaIn201305Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201305UV02",
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
class ProxyPrpaIn201305UvproxyRequest(ProxyPrpaIn201305UvproxyRequestType):
    class Meta:
        name = "Proxy_PRPA_IN201305UVProxyRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class ProxyPrpaIn201305UvproxySecuredRequest(ProxyPrpaIn201305UvproxySecuredRequestType):
    class Meta:
        name = "Proxy_PRPA_IN201305UVProxySecuredRequest"
        namespace = "urn:hl7-org:v3"
