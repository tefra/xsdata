from .attribute_compound_choice import AttributeCompoundChoiceHandler
from .attribute_default_value import AttributeDefaultValueHandler
from .attribute_effective_choice import AttributeEffectiveChoiceHandler
from .attribute_group import AttributeGroupHandler
from .attribute_merge import AttributeMergeHandler
from .attribute_mixed_content import AttributeMixedContentHandler
from .attribute_name_conflict import AttributeNameConflictHandler
from .attribute_overrides import AttributeOverridesHandler
from .attribute_substitution import AttributeSubstitutionHandler
from .attribute_type import AttributeTypeHandler
from .class_designate import ClassDesignateHandler
from .class_enumeration import ClassEnumerationHandler
from .class_extension import ClassExtensionHandler
from .class_inners import ClassInnersHandler
from .class_name_conflict import ClassNameConflictHandler
from .class_unnest import ClassUnnestHandler

__all__ = [
    "AttributeCompoundChoiceHandler",
    "AttributeDefaultValueHandler",
    "AttributeEffectiveChoiceHandler",
    "AttributeGroupHandler",
    "AttributeMergeHandler",
    "AttributeMixedContentHandler",
    "AttributeNameConflictHandler",
    "AttributeOverridesHandler",
    "AttributeSubstitutionHandler",
    "AttributeTypeHandler",
    "ClassDesignateHandler",
    "ClassInnersHandler",
    "ClassEnumerationHandler",
    "ClassExtensionHandler",
    "ClassNameConflictHandler",
    "ClassUnnestHandler",
]
