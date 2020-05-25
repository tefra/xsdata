from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Cs,
    Ii,
    St,
    TsExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    NullFlavor,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PrpaMt201307UvDataSource:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201307UV.DataSource"

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
class PrpaMt201307UvPatientIdentifier:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar semantics_text:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201307UV.PatientIdentifier"

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
class PrpaMt201307UvParameterList:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar data_source:
    :ivar patient_identifier:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201307UV.ParameterList"

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
    data_source: List[PrpaMt201307UvDataSource] = field(
        default_factory=list,
        metadata=dict(
            name="dataSource",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    patient_identifier: List[PrpaMt201307UvPatientIdentifier] = field(
        default_factory=list,
        metadata=dict(
            name="patientIdentifier",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
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
class PrpaMt201307UvQueryByParameter:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar query_id:
    :ivar status_code:
    :ivar modify_code:
    :ivar response_element_group_id:
    :ivar response_priority_code:
    :ivar execution_and_delivery_time:
    :ivar parameter_list:
    :ivar null_flavor:
    """
    class Meta:
        name = "PRPA_MT201307UV.QueryByParameter"

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
    response_priority_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="responsePriorityCode",
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
    parameter_list: Optional[PrpaMt201307UvParameterList] = field(
        default=None,
        metadata=dict(
            name="parameterList",
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
