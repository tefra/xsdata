from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AcknowledgementType:
    """
    :ivar message:
    """
    message: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class AssigningAuthorityType:
    """
    :ivar assigning_authority_id:
    """
    assigning_authority_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="assigningAuthorityId",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class ConnectcustomHttpHeadersType:
    """
    :ivar header_name:
    :ivar header_value:
    """
    class Meta:
        name = "CONNECTCustomHttpHeadersType"

    header_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="headerName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    header_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="headerValue",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class CeType:
    """
    :ivar code:
    :ivar code_system:
    :ivar code_system_name:
    :ivar code_system_version:
    :ivar display_name:
    :ivar original_text:
    :ivar translation:
    """
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    code_system: Optional[str] = field(
        default=None,
        metadata=dict(
            name="codeSystem",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="codeSystemName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="codeSystemVersion",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    display_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="displayName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    original_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="originalText",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    translation: List["CeType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class CreateEprrequestType:
    """
    :ivar endpoint_url:
    :ivar namespace_uri:
    :ivar namespace_prefix:
    :ivar service_name:
    :ivar port_name:
    """
    class Meta:
        name = "CreateEPRRequestType"

    endpoint_url: Optional[str] = field(
        default=None,
        metadata=dict(
            name="endpointURL",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    namespace_uri: Optional[str] = field(
        default=None,
        metadata=dict(
            name="namespaceURI",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    namespace_prefix: Optional[str] = field(
        default=None,
        metadata=dict(
            name="namespacePrefix",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    service_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="serviceName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    port_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="portName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class Epr:
    class Meta:
        name = "EPR"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class HomeCommunityType:
    """
    :ivar description:
    :ivar home_community_id:
    :ivar name:
    """
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    home_community_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="homeCommunityId",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class QualifiedSubjectIdentifierType:
    """
    :ivar subject_identifier:
    :ivar assigning_authority_identifier:
    """
    subject_identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SubjectIdentifier",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    assigning_authority_identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AssigningAuthorityIdentifier",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class ResponseType:
    """
    :ivar status:
    :ivar message:
    """
    status: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    message: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class SamlAuthnStatementType:
    """
    :ivar auth_instant:
    :ivar session_index:
    :ivar auth_context_class_ref:
    :ivar subject_locality_address:
    :ivar subject_locality_dnsname:
    """
    auth_instant: Optional[str] = field(
        default=None,
        metadata=dict(
            name="authInstant",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    session_index: Optional[str] = field(
        default=None,
        metadata=dict(
            name="sessionIndex",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    auth_context_class_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="authContextClassRef",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    subject_locality_address: Optional[str] = field(
        default=None,
        metadata=dict(
            name="subjectLocalityAddress",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    subject_locality_dnsname: Optional[str] = field(
        default=None,
        metadata=dict(
            name="subjectLocalityDNSName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class SamlAuthzDecisionStatementEvidenceConditionsType:
    """
    :ivar not_before:
    :ivar not_on_or_after:
    """
    not_before: Optional[str] = field(
        default=None,
        metadata=dict(
            name="notBefore",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    not_on_or_after: Optional[str] = field(
        default=None,
        metadata=dict(
            name="notOnOrAfter",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class SamlConditionsType:
    """
    :ivar not_before:
    :ivar not_on_or_after:
    """
    not_before: Optional[str] = field(
        default=None,
        metadata=dict(
            name="notBefore",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    not_on_or_after: Optional[str] = field(
        default=None,
        metadata=dict(
            name="notOnOrAfter",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class SamlIssuerType:
    """
    :ivar issuer:
    :ivar issuer_format:
    """
    issuer: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    issuer_format: Optional[str] = field(
        default=None,
        metadata=dict(
            name="issuerFormat",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class SamlSignatureKeyInfoType:
    """
    :ivar rsa_key_value_modulus:
    :ivar rsa_key_value_exponent:
    """
    rsa_key_value_modulus: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rsaKeyValueModulus",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    rsa_key_value_exponent: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rsaKeyValueExponent",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class TokenRetrieveInfoType:
    """
    :ivar request:
    """
    request: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class UrlInfoType:
    """
    :ivar url:
    :ivar id:
    """
    url: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class UrlSetType:
    """
    :ivar url:
    """
    url: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Acknowledgement(AcknowledgementType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AddressType:
    """
    :ivar address_type:
    :ivar city:
    :ivar country:
    :ivar state:
    :ivar street_address:
    :ivar zip_code:
    """
    address_type: Optional[CeType] = field(
        default=None,
        metadata=dict(
            name="addressType",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    city: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    country: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    state: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    street_address: Optional[str] = field(
        default=None,
        metadata=dict(
            name="streetAddress",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    zip_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="zipCode",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class AssigningAuthoritiesType:
    """
    :ivar assigning_authority:
    """
    assigning_authority: List[AssigningAuthorityType] = field(
        default_factory=list,
        metadata=dict(
            name="assigningAuthority",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class AssigningAuthority(AssigningAuthorityType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class ConnectcustomHttpHeaders(ConnectcustomHttpHeadersType):
    class Meta:
        name = "CONNECTCustomHttpHeaders"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Ce(CeType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class CreateEprrequest(CreateEprrequestType):
    class Meta:
        name = "CreateEPRRequest"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class HomeCommunitiesType:
    """
    :ivar home_community:
    """
    home_community: List[HomeCommunityType] = field(
        default_factory=list,
        metadata=dict(
            name="homeCommunity",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class HomeCommunity(HomeCommunityType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class NhinTargetCommunityType:
    """
    :ivar home_community:
    :ivar list_value:
    :ivar region:
    """
    home_community: Optional[HomeCommunityType] = field(
        default=None,
        metadata=dict(
            name="homeCommunity",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    list_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="list",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    region: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class NhinTargetSystemType:
    """
    :ivar epr:
    :ivar home_community:
    :ivar url:
    :ivar exchange_name:
    :ivar use_spec_version:
    """
    epr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    home_community: Optional[HomeCommunityType] = field(
        default=None,
        metadata=dict(
            name="homeCommunity",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    url: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    exchange_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="exchangeName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    use_spec_version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="useSpecVersion",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class PersonNameType:
    """
    :ivar family_name:
    :ivar given_name:
    :ivar name_type:
    :ivar second_name_or_initials:
    :ivar full_name:
    :ivar prefix:
    :ivar suffix:
    """
    family_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="familyName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    given_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="givenName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    name_type: Optional[CeType] = field(
        default=None,
        metadata=dict(
            name="nameType",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    second_name_or_initials: Optional[str] = field(
        default=None,
        metadata=dict(
            name="secondNameOrInitials",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    full_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fullName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    prefix: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    suffix: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class PhoneType:
    """
    :ivar area_code:
    :ivar country_code:
    :ivar extension:
    :ivar local_number:
    :ivar phone_number_type:
    """
    area_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="areaCode",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    country_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="countryCode",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    extension: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    local_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="localNumber",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    phone_number_type: Optional[CeType] = field(
        default=None,
        metadata=dict(
            name="phoneNumberType",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class QualifiedSubjectIdentifier(QualifiedSubjectIdentifierType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class QualifiedSubjectIdentifiersType:
    """
    :ivar qualified_subject_identifier:
    """
    qualified_subject_identifier: List[QualifiedSubjectIdentifierType] = field(
        default_factory=list,
        metadata=dict(
            name="QualifiedSubjectIdentifier",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Response(ResponseType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthnStatement(SamlAuthnStatementType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementEvidenceAssertionType:
    """
    :ivar id:
    :ivar issue_instant:
    :ivar version:
    :ivar issuer:
    :ivar issuer_format:
    :ivar subject:
    :ivar conditions:
    :ivar access_consent_policy:
    :ivar instance_access_consent_policy:
    """
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    issue_instant: Optional[str] = field(
        default=None,
        metadata=dict(
            name="issueInstant",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    version: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    issuer: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    issuer_format: Optional[str] = field(
        default=None,
        metadata=dict(
            name="issuerFormat",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    subject: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    conditions: Optional[SamlAuthzDecisionStatementEvidenceConditionsType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    access_consent_policy: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="accessConsentPolicy",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    instance_access_consent_policy: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="instanceAccessConsentPolicy",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class SamlAuthzDecisionStatementEvidenceConditions(SamlAuthzDecisionStatementEvidenceConditionsType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlConditions(SamlConditionsType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlIssuer(SamlIssuerType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlSignatureKeyInfo(SamlSignatureKeyInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlSignatureType:
    """
    :ivar key_info:
    :ivar signature_value:
    """
    key_info: Optional[SamlSignatureKeyInfoType] = field(
        default=None,
        metadata=dict(
            name="keyInfo",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    signature_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="signatureValue",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class SamlSubjectConfirmationType:
    """
    :ivar method:
    :ivar subject_condition:
    :ivar recipient:
    :ivar in_response_to:
    :ivar address:
    """
    method: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    subject_condition: Optional[SamlConditionsType] = field(
        default=None,
        metadata=dict(
            name="subjectCondition",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    recipient: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    in_response_to: Optional[str] = field(
        default=None,
        metadata=dict(
            name="inResponseTo",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    address: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class TokenRetrieveInfo(TokenRetrieveInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class UrlInfo(UrlInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class UrlSet(UrlSetType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Address(AddressType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AddressesType:
    """
    :ivar address:
    """
    address: List[AddressType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class HomeCommunities(HomeCommunitiesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class NhinTargetCommunitiesType:
    """
    :ivar nhin_target_community:
    :ivar use_spec_version:
    :ivar exchange_name:
    """
    nhin_target_community: List[NhinTargetCommunityType] = field(
        default_factory=list,
        metadata=dict(
            name="nhinTargetCommunity",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    use_spec_version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="useSpecVersion",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    exchange_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="exchangeName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class NhinTargetCommunity(NhinTargetCommunityType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class NhinTargetSystem(NhinTargetSystemType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class PersonName(PersonNameType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Phone(PhoneType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class QualifiedSubjectIdentifiers(QualifiedSubjectIdentifiersType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementEvidenceAssertion(SamlAuthzDecisionStatementEvidenceAssertionType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementEvidenceType:
    """
    :ivar assertion:
    """
    assertion: Optional[SamlAuthzDecisionStatementEvidenceAssertionType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class SamlSignature(SamlSignatureType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class UserType:
    """
    :ivar person_name:
    :ivar user_name:
    :ivar org:
    :ivar role_coded:
    """
    person_name: Optional[PersonNameType] = field(
        default=None,
        metadata=dict(
            name="personName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    user_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="userName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    org: Optional[HomeCommunityType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    role_coded: Optional[CeType] = field(
        default=None,
        metadata=dict(
            name="roleCoded",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class AssigningAuthorites(AssigningAuthoritiesType):
    class Meta:
        name = "assigningAuthorites"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Addresses(AddressesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class ConfigAssertionType:
    """
    :ivar user_info:
    :ivar config_instance:
    :ivar auth_method:
    """
    user_info: Optional[UserType] = field(
        default=None,
        metadata=dict(
            name="userInfo",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    config_instance: Optional[str] = field(
        default=None,
        metadata=dict(
            name="configInstance",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    auth_method: Optional[str] = field(
        default=None,
        metadata=dict(
            name="authMethod",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class NhinTargetCommunities(NhinTargetCommunitiesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementEvidence(SamlAuthzDecisionStatementEvidenceType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementType:
    """
    :ivar decision:
    :ivar resource:
    :ivar action:
    :ivar evidence:
    """
    decision: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    resource: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    action: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    evidence: Optional[SamlAuthzDecisionStatementEvidenceType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class User(UserType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AssertionType:
    """
    :ivar address:
    :ivar date_of_birth:
    :ivar explanation_non_claimant_signature:
    :ivar have_second_witness_signature:
    :ivar have_signature:
    :ivar have_witness_signature:
    :ivar home_community:
    :ivar national_provider_id:
    :ivar person_name:
    :ivar phone_number:
    :ivar second_witness_address:
    :ivar second_witness_name:
    :ivar second_witness_phone:
    :ivar ssn:
    :ivar unique_patient_id:
    :ivar witness_address:
    :ivar witness_name:
    :ivar witness_phone:
    :ivar user_info:
    :ivar authorized:
    :ivar purpose_of_disclosure_coded:
    :ivar acp_attribute:
    :ivar instance_acp_attribute:
    :ivar saml_conditions:
    :ivar saml_authn_statement:
    :ivar saml_authz_decision_statement:
    :ivar saml_signature:
    :ivar saml_issuer:
    :ivar saml_subject_confirmations:
    :ivar message_id:
    :ivar relates_to_list:
    :ivar implements_spec_version:
    :ivar transaction_timeout:
    :ivar keep_alive:
    :ivar connectcustom_http_headers:
    :ivar signature_algorithm:
    :ivar digest_algorithm:
    """
    address: Optional[AddressType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    date_of_birth: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dateOfBirth",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    explanation_non_claimant_signature: Optional[str] = field(
        default=None,
        metadata=dict(
            name="explanationNonClaimantSignature",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    have_second_witness_signature: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="haveSecondWitnessSignature",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    have_signature: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="haveSignature",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    have_witness_signature: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="haveWitnessSignature",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    home_community: Optional[HomeCommunityType] = field(
        default=None,
        metadata=dict(
            name="homeCommunity",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    national_provider_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="nationalProviderId",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    person_name: Optional[PersonNameType] = field(
        default=None,
        metadata=dict(
            name="personName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    phone_number: Optional[PhoneType] = field(
        default=None,
        metadata=dict(
            name="phoneNumber",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    second_witness_address: Optional[AddressType] = field(
        default=None,
        metadata=dict(
            name="secondWitnessAddress",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    second_witness_name: Optional[PersonNameType] = field(
        default=None,
        metadata=dict(
            name="secondWitnessName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    second_witness_phone: Optional[PhoneType] = field(
        default=None,
        metadata=dict(
            name="secondWitnessPhone",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    ssn: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SSN",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    unique_patient_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="uniquePatientId",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    witness_address: Optional[AddressType] = field(
        default=None,
        metadata=dict(
            name="witnessAddress",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    witness_name: Optional[PersonNameType] = field(
        default=None,
        metadata=dict(
            name="witnessName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    witness_phone: Optional[PhoneType] = field(
        default=None,
        metadata=dict(
            name="witnessPhone",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    user_info: Optional[UserType] = field(
        default=None,
        metadata=dict(
            name="userInfo",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    authorized: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    purpose_of_disclosure_coded: Optional[CeType] = field(
        default=None,
        metadata=dict(
            name="purposeOfDisclosureCoded",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    acp_attribute: Optional[str] = field(
        default=None,
        metadata=dict(
            name="acpAttribute",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    instance_acp_attribute: Optional[str] = field(
        default=None,
        metadata=dict(
            name="instanceAcpAttribute",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    saml_conditions: Optional[SamlConditionsType] = field(
        default=None,
        metadata=dict(
            name="samlConditions",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    saml_authn_statement: Optional[SamlAuthnStatementType] = field(
        default=None,
        metadata=dict(
            name="samlAuthnStatement",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    saml_authz_decision_statement: Optional[SamlAuthzDecisionStatementType] = field(
        default=None,
        metadata=dict(
            name="samlAuthzDecisionStatement",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    saml_signature: Optional[SamlSignatureType] = field(
        default=None,
        metadata=dict(
            name="samlSignature",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    saml_issuer: Optional[SamlIssuerType] = field(
        default=None,
        metadata=dict(
            name="samlIssuer",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    saml_subject_confirmations: List[SamlSubjectConfirmationType] = field(
        default_factory=list,
        metadata=dict(
            name="samlSubjectConfirmations",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    message_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="messageId",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    relates_to_list: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="relatesToList",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    implements_spec_version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="implementsSpecVersion",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    transaction_timeout: Optional[int] = field(
        default=None,
        metadata=dict(
            name="transactionTimeout",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    keep_alive: Optional[str] = field(
        default=None,
        metadata=dict(
            name="keepAlive",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    connectcustom_http_headers: List[ConnectcustomHttpHeadersType] = field(
        default_factory=list,
        metadata=dict(
            name="CONNECTCustomHttpHeaders",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    signature_algorithm: Optional[str] = field(
        default=None,
        metadata=dict(
            name="signatureAlgorithm",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )
    digest_algorithm: Optional[str] = field(
        default=None,
        metadata=dict(
            name="digestAlgorithm",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon"
        )
    )


@dataclass
class ConfigAssertion(ConfigAssertionType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatement(SamlAuthzDecisionStatementType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Assertion(AssertionType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class TokenCreationInfoType:
    """
    :ivar assertion:
    :ivar action_name:
    :ivar resource_name:
    """
    assertion: Optional[AssertionType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    action_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="actionName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )
    resource_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="resourceName",
            type="Element",
            namespace="urn:gov:hhs:fha:nhinc:common:nhinccommon",
            required=True
        )
    )


@dataclass
class TokenCreationInfo(TokenCreationInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"
