from .add_attribute_substitutions import AddAttributeSubstitutions
from .calculate_attribute_paths import CalculateAttributePaths
from .create_compound_fields import CreateCompoundFields
from .designate_class_packages import DesignateClassPackages
from .detect_circular_references import DetectCircularReferences
from .disambiguate_choices import DisambiguateChoices
from .filter_classes import FilterClasses
from .flatten_attribute_groups import FlattenAttributeGroups
from .flatten_class_extensions import FlattenClassExtensions
from .merge_attributes import MergeAttributes
from .process_attributes_types import ProcessAttributeTypes
from .process_mixed_content_class import ProcessMixedContentClass
from .rename_duplicate_attributes import RenameDuplicateAttributes
from .rename_duplicate_classes import RenameDuplicateClasses
from .reset_attribute_sequence_numbers import ResetAttributeSequenceNumbers
from .reset_attribute_sequences import ResetAttributeSequences
from .sanitize_attributes_default_value import SanitizeAttributesDefaultValue
from .sanitize_enumeration_class import SanitizeEnumerationClass
from .unnest_inner_classes import UnnestInnerClasses
from .update_attributes_effective_choice import UpdateAttributesEffectiveChoice
from .vacuum_inner_classes import VacuumInnerClasses
from .validate_attributes_overrides import ValidateAttributesOverrides
from .validate_references import ValidateReferences

__all__ = [
    "AddAttributeSubstitutions",
    "CalculateAttributePaths",
    "CreateCompoundFields",
    "DesignateClassPackages",
    "DetectCircularReferences",
    "DisambiguateChoices",
    "FilterClasses",
    "FlattenAttributeGroups",
    "FlattenClassExtensions",
    "MergeAttributes",
    "ProcessAttributeTypes",
    "ProcessMixedContentClass",
    "RenameDuplicateAttributes",
    "RenameDuplicateClasses",
    "ResetAttributeSequenceNumbers",
    "ResetAttributeSequences",
    "SanitizeAttributesDefaultValue",
    "SanitizeEnumerationClass",
    "UnnestInnerClasses",
    "UpdateAttributesEffectiveChoice",
    "VacuumInnerClasses",
    "ValidateAttributesOverrides",
    "ValidateReferences",
]
