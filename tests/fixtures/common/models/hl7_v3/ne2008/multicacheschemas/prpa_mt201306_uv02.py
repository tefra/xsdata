from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    AdExplicit,
    Any,
    Ce,
    Cs,
    Cv,
    EnExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    PnExplicit,
    Sc,
    St,
    StExplicit,
    TelExplicit,
    TsExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    NullFlavor,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PrpaMt201306Uv02LivingSubjectAdministrativeGender:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectAdministrativeGender"

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
    value: List[Ce] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02LivingSubjectBirthPlaceAddress:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectBirthPlaceAddress"

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
    value: List[AdExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02LivingSubjectBirthPlaceName:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectBirthPlaceName"

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
    value: List[EnExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02LivingSubjectBirthTime:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectBirthTime"

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
    value: List[IvlTsExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02LivingSubjectDeceasedTime:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectDeceasedTime"

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
    value: List[IvlTsExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02LivingSubjectId:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectId"

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
    value: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02LivingSubjectName:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectName"

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
    value: List[EnExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02MatchAlgorithm:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.MatchAlgorithm"

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
    value: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02MatchWeight:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.MatchWeight"

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
    value: Optional[Any] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    semantics_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02MinimumDegreeMatch:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.MinimumDegreeMatch"

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
    value: Optional[IntType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02MothersMaidenName:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.MothersMaidenName"

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
    value: List[PnExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02OtherIdsScopingOrganization:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.OtherIDsScopingOrganization"

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
    value: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02PatientAddress:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.PatientAddress"

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
    value: List[AdExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02PatientStatusCode:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.PatientStatusCode"

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
    value: Optional[Cv] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    semantics_text: Optional[St] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02PatientTelecom:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.PatientTelecom"

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
    value: List[TelExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02PrincipalCareProviderId:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.PrincipalCareProviderId"

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
    value: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
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


@dataclass
class PrpaMt201306Uv02PrincipalCareProvisionId:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.PrincipalCareProvisionId"

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
    value: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    semantics_text: Optional[StExplicit] = field(
        default=None,
        metadata=dict(
            name="semanticsText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class PrpaMt201306Uv02SortControl:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar element_name:
    :ivar direction_code:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.SortControl"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="sequenceNumber",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    element_name: Optional[Sc] = field(
        default=None,
        metadata=dict(
            name="elementName",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    direction_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="directionCode",
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


@dataclass
class PrpaMt201306Uv02MatchCriterionList:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar match_algorithm:
    :ivar match_weight:
    :ivar minimum_degree_match:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.MatchCriterionList"

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
    id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    match_algorithm: Optional[PrpaMt201306Uv02MatchAlgorithm] = field(
        default=None,
        metadata=dict(
            name="matchAlgorithm",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    match_weight: Optional[PrpaMt201306Uv02MatchWeight] = field(
        default=None,
        metadata=dict(
            name="matchWeight",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    minimum_degree_match: Optional[PrpaMt201306Uv02MinimumDegreeMatch] = field(
        default=None,
        metadata=dict(
            name="minimumDegreeMatch",
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


@dataclass
class PrpaMt201306Uv02ParameterList:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar living_subject_administrative_gender:
    :ivar living_subject_birth_place_address:
    :ivar living_subject_birth_place_name:
    :ivar living_subject_birth_time:
    :ivar living_subject_deceased_time:
    :ivar living_subject_id:
    :ivar living_subject_name:
    :ivar mothers_maiden_name:
    :ivar other_ids_scoping_organization:
    :ivar patient_address:
    :ivar patient_status_code:
    :ivar patient_telecom:
    :ivar principal_care_provider_id:
    :ivar principal_care_provision_id:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.ParameterList"

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
    id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    living_subject_administrative_gender: List[PrpaMt201306Uv02LivingSubjectAdministrativeGender] = field(
        default_factory=list,
        metadata=dict(
            name="livingSubjectAdministrativeGender",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    living_subject_birth_place_address: List[PrpaMt201306Uv02LivingSubjectBirthPlaceAddress] = field(
        default_factory=list,
        metadata=dict(
            name="livingSubjectBirthPlaceAddress",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    living_subject_birth_place_name: List[PrpaMt201306Uv02LivingSubjectBirthPlaceName] = field(
        default_factory=list,
        metadata=dict(
            name="livingSubjectBirthPlaceName",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    living_subject_birth_time: List[PrpaMt201306Uv02LivingSubjectBirthTime] = field(
        default_factory=list,
        metadata=dict(
            name="livingSubjectBirthTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    living_subject_deceased_time: List[PrpaMt201306Uv02LivingSubjectDeceasedTime] = field(
        default_factory=list,
        metadata=dict(
            name="livingSubjectDeceasedTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    living_subject_id: List[PrpaMt201306Uv02LivingSubjectId] = field(
        default_factory=list,
        metadata=dict(
            name="livingSubjectId",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    living_subject_name: List[PrpaMt201306Uv02LivingSubjectName] = field(
        default_factory=list,
        metadata=dict(
            name="livingSubjectName",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    mothers_maiden_name: List[PrpaMt201306Uv02MothersMaidenName] = field(
        default_factory=list,
        metadata=dict(
            name="mothersMaidenName",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    other_ids_scoping_organization: List[PrpaMt201306Uv02OtherIdsScopingOrganization] = field(
        default_factory=list,
        metadata=dict(
            name="otherIDsScopingOrganization",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    patient_address: List[PrpaMt201306Uv02PatientAddress] = field(
        default_factory=list,
        metadata=dict(
            name="patientAddress",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    patient_status_code: List[PrpaMt201306Uv02PatientStatusCode] = field(
        default_factory=list,
        metadata=dict(
            name="patientStatusCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    patient_telecom: List[PrpaMt201306Uv02PatientTelecom] = field(
        default_factory=list,
        metadata=dict(
            name="patientTelecom",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    principal_care_provider_id: List[PrpaMt201306Uv02PrincipalCareProviderId] = field(
        default_factory=list,
        metadata=dict(
            name="principalCareProviderId",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    principal_care_provision_id: List[PrpaMt201306Uv02PrincipalCareProvisionId] = field(
        default_factory=list,
        metadata=dict(
            name="principalCareProvisionId",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
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


@dataclass
class PrpaMt201306Uv02QueryByParameter:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar query_id:
    :ivar status_code:
    :ivar modify_code:
    :ivar response_element_group_id:
    :ivar response_modality_code:
    :ivar response_priority_code:
    :ivar initial_quantity:
    :ivar initial_quantity_code:
    :ivar execution_and_delivery_time:
    :ivar match_criterion_list:
    :ivar parameter_list:
    :ivar sort_control:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201306UV02.QueryByParameter"

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
    query_id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            name="queryId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    modify_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="modifyCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    response_element_group_id: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            name="responseElementGroupId",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    response_modality_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="responseModalityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    response_priority_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="responsePriorityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    initial_quantity: Optional[IntType] = field(
        default=None,
        metadata=dict(
            name="initialQuantity",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    initial_quantity_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="initialQuantityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    execution_and_delivery_time: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            name="executionAndDeliveryTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    match_criterion_list: Optional[PrpaMt201306Uv02MatchCriterionList] = field(
        default=None,
        metadata=dict(
            name="matchCriterionList",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    parameter_list: Optional[PrpaMt201306Uv02ParameterList] = field(
        default=None,
        metadata=dict(
            name="parameterList",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    sort_control: List[PrpaMt201306Uv02SortControl] = field(
        default_factory=list,
        metadata=dict(
            name="sortControl",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
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
