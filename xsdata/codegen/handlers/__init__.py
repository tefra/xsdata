from xsdata.codegen.handlers.attribute_enum_union import AttributeEnumUnionClassHandler
from xsdata.codegen.handlers.attribute_group import AttributeGroupClassHandler
from xsdata.codegen.handlers.attribute_implied import AttributeImpliedClassHandler
from xsdata.codegen.handlers.attribute_merge import AttributeMergeClassHandler
from xsdata.codegen.handlers.attribute_mismatch import AttributeMismatchClassHandler
from xsdata.codegen.handlers.attribute_substitution import AttributeSubstitutionHandler
from xsdata.codegen.handlers.attribute_type import AttributeTypeClassHandler
from xsdata.codegen.handlers.class_extension import ClassExtensionClassHandler

__all__ = [
    "AttributeGroupClassHandler",
    "AttributeTypeClassHandler",
    "AttributeMergeClassHandler",
    "AttributeEnumUnionClassHandler",
    "ClassExtensionClassHandler",
    "AttributeImpliedClassHandler",
    "AttributeMismatchClassHandler",
    "AttributeSubstitutionHandler",
]
