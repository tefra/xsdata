from xsdata.codegen.handlers.attribute_group import AttributeGroupHandler
from xsdata.codegen.handlers.attribute_merge import AttributeMergeHandler
from xsdata.codegen.handlers.attribute_mixed_content import AttributeMixedContentHandler
from xsdata.codegen.handlers.attribute_sanitizer import AttributeSanitizerHandler
from xsdata.codegen.handlers.attribute_substitution import AttributeSubstitutionHandler
from xsdata.codegen.handlers.attribute_type import AttributeTypeHandler
from xsdata.codegen.handlers.class_enumeration import ClassEnumerationHandler
from xsdata.codegen.handlers.class_extension import ClassExtensionHandler

__all__ = [
    "ClassEnumerationHandler",
    "AttributeGroupHandler",
    "AttributeMergeHandler",
    "AttributeSanitizerHandler",
    "AttributeMixedContentHandler",
    "AttributeSubstitutionHandler",
    "AttributeTypeHandler",
    "ClassExtensionHandler",
]
