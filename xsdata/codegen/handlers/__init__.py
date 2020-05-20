from xsdata.codegen.handlers.attribute_enum_union import AttributeEnumUnionHandler
from xsdata.codegen.handlers.attribute_group import AttributeGroupHandler
from xsdata.codegen.handlers.attribute_implied import AttributeImpliedHandler
from xsdata.codegen.handlers.attribute_merge import AttributeMergeHandler
from xsdata.codegen.handlers.attribute_mismatch import AttributeMismatchHandler
from xsdata.codegen.handlers.attribute_substitution import AttributeSubstitutionHandler
from xsdata.codegen.handlers.attribute_type import AttributeTypeHandler
from xsdata.codegen.handlers.class_extension import ClassExtensionHandler

__all__ = [
    "AttributeGroupHandler",
    "AttributeTypeHandler",
    "AttributeMergeHandler",
    "AttributeEnumUnionHandler",
    "ClassExtensionHandler",
    "AttributeImpliedHandler",
    "AttributeMismatchHandler",
    "AttributeSubstitutionHandler",
]
