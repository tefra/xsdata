from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.common.models.nhinc.common.nhinc_common import (
    AssertionType,
    NhinTargetSystemType,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201301_uv02 import (
    PrpaIn201301Uv02,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201302_uv02 import (
    PrpaIn201302Uv02,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201304_uv02 import (
    PrpaIn201304Uv02,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201309_uv02 import (
    PrpaIn201309Uv02,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201301UvproxyRequestType:
    """
    :ivar prpa_in201301_uv02:
    :ivar assertion:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVProxyRequestType"

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
class PixconsumerPrpaIn201301UvproxySecuredRequestType:
    """
    :ivar prpa_in201301_uv02:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVProxySecuredRequestType"

    prpa_in201301_uv02: Optional[PrpaIn201301Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201301UV02",
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
class PixconsumerPrpaIn201302UvproxyRequestType:
    """
    :ivar prpa_in201302_uv02:
    :ivar assertion:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVProxyRequestType"

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
class PixconsumerPrpaIn201302UvproxySecuredRequestType:
    """
    :ivar prpa_in201302_uv02:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVProxySecuredRequestType"

    prpa_in201302_uv02: Optional[PrpaIn201302Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201302UV02",
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
class PixconsumerPrpaIn201304UvproxyRequestType:
    """
    :ivar prpa_in201304_uv02:
    :ivar assertion:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVProxyRequestType"

    prpa_in201304_uv02: Optional[PrpaIn201304Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201304UV02",
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
class PixconsumerPrpaIn201304UvproxySecuredRequestType:
    """
    :ivar prpa_in201304_uv02:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVProxySecuredRequestType"

    prpa_in201304_uv02: Optional[PrpaIn201304Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201304UV02",
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
class PixconsumerPrpaIn201309UvproxyRequestType:
    """
    :ivar prpa_in201309_uv02:
    :ivar assertion:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVProxyRequestType"

    prpa_in201309_uv02: Optional[PrpaIn201309Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201309UV02",
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
class PixconsumerPrpaIn201309UvproxySecuredRequestType:
    """
    :ivar prpa_in201309_uv02:
    :ivar nhin_target_system:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVProxySecuredRequestType"

    prpa_in201309_uv02: Optional[PrpaIn201309Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201309UV02",
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
class PixconsumerPrpaIn201301UvproxyRequest(PixconsumerPrpaIn201301UvproxyRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVProxyRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201301UvproxySecuredRequest(PixconsumerPrpaIn201301UvproxySecuredRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVProxySecuredRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201302UvproxyRequest(PixconsumerPrpaIn201302UvproxyRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVProxyRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201302UvproxySecuredRequest(PixconsumerPrpaIn201302UvproxySecuredRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVProxySecuredRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201304UvproxyRequest(PixconsumerPrpaIn201304UvproxyRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVProxyRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201304UvproxySecuredRequest(PixconsumerPrpaIn201304UvproxySecuredRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVProxySecuredRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201309UvproxyRequest(PixconsumerPrpaIn201309UvproxyRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVProxyRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201309UvproxySecuredRequest(PixconsumerPrpaIn201309UvproxySecuredRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVProxySecuredRequest"
        namespace = "urn:hl7-org:v3"
