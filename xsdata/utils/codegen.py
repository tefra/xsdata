from typing import List
from typing import Optional

from xsdata.models.codegen import Attr
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.models.codegen import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import TagType
from xsdata.utils import text


class ClassUtils:

    INCLUDES_NONE = 0
    INCLUDES_SOME = 1
    INCLUDES_ALL = 2

    @classmethod
    def compare_attributes(cls, source: Class, target: Class):
        if source is target:
            return cls.INCLUDES_ALL
        elif not target.attrs:
            return cls.INCLUDES_NONE

        source_attrs = {attr.name for attr in source.attrs}
        target_attrs = {attr.name for attr in target.attrs}
        difference = source_attrs - target_attrs

        if not difference:
            return cls.INCLUDES_ALL
        elif len(difference) != len(source_attrs):
            return cls.INCLUDES_SOME
        else:
            return cls.INCLUDES_NONE

    @classmethod
    def sanitize_properties(cls, target: Class):
        if not target.attrs:
            return

        cls.sanitize_restrictions(target)
        cls.unset_sequential_attributes(target)

        for inner in target.inner:
            cls.sanitize_properties(inner)

    @classmethod
    def sanitize_restrictions(cls, target: Class):
        for attr in target.attrs:
            res = attr.restrictions
            min_occurs = res.min_occurs or 0
            max_occurs = res.max_occurs or 0

            if min_occurs == 0 and max_occurs <= 1:
                res.required = None
                res.min_occurs = None
                res.max_occurs = None
            if min_occurs == 1 and max_occurs == 1:
                res.required = True
                res.min_occurs = None
                res.max_occurs = None
            elif res.max_occurs and max_occurs > 1:
                res.min_occurs = min_occurs
                res.required = None

    @classmethod
    def unset_sequential_attributes(cls, target: Class):
        """
        Reset the class attributes sequential flags where needed.

        Reasons:
            1. Attribute not a list
            2. Attribute siblings are not sequential.
        """

        for attr in target.attrs:
            if not attr.is_list:
                attr.restrictions.sequential = False

        total = len(target.attrs)
        for idx, attr in enumerate(target.attrs):
            if not attr.restrictions.sequential:
                continue

            siblings = False
            if idx - 1 >= 0 and target.attrs[idx - 1].restrictions.sequential:
                siblings = True
            elif idx + 1 < total and target.attrs[idx + 1].restrictions.sequential:
                siblings = True
            if not siblings:
                attr.restrictions.sequential = False

    @classmethod
    def merge_duplicate_attributes(cls, target: Class):
        """
        Flatten duplicate attributes.

        Remove duplicate fields in case of attributes or enumerations
        otherwise convert fields to lists.
        """

        if not target.attrs:
            return

        result: List[Attr] = []
        for attr in target.attrs:
            existing = next((item for item in result if attr == item), None)

            if not existing:
                result.append(attr)
            elif not (attr.is_attribute or attr.is_enumeration):
                min_occurs = existing.restrictions.min_occurs or 0
                max_occurs = existing.restrictions.max_occurs or 1
                attr_min_occurs = attr.restrictions.min_occurs or 0
                attr_max_occurs = attr.restrictions.max_occurs or 1

                existing.restrictions.min_occurs = min(min_occurs, attr_min_occurs)
                existing.restrictions.max_occurs = max_occurs + attr_max_occurs
                existing.fixed = False
                existing.restrictions.sequential = (
                    existing.restrictions.sequential or attr.restrictions.sequential
                )

        target.attrs = result

    @classmethod
    def copy_attributes(cls, source: Class, target: Class, extension: Extension):
        prefix = text.prefix(extension.type.name)
        target.extensions.remove(extension)
        target_attr_names = {text.suffix(attr.name) for attr in target.attrs}

        index = 0
        for attr in source.attrs:
            if text.suffix(attr.name) not in target_attr_names:
                clone = cls.clone_attribute(attr, extension.restrictions, prefix)
                target.attrs.insert(index, clone)
            index += 1

        cls.copy_inner_classes(source, target)

    @classmethod
    def clone_attribute(
        cls, attr: Attr, restrictions: Restrictions, prefix: Optional[str] = None
    ):
        clone = attr.clone()
        clone.restrictions.merge(restrictions)
        if prefix:
            for attr_type in clone.types:
                if not attr_type.native and attr_type.name.find(":") == -1:
                    attr_type.name = f"{prefix}:{attr_type.name}"

        return clone

    @classmethod
    def copy_inner_classes(cls, source: Class, target: Class):
        for inner in source.inner:
            exists = next(
                (found for found in target.inner if found.name == inner.name), None
            )
            if not exists:
                target.inner.append(inner)

    @classmethod
    def create_default_attribute(cls, item: Class, extension: Extension):
        if extension.type.native_code == DataType.ANY_TYPE.code:
            attr = Attr(
                name="##any_element",
                index=0,
                wildcard=True,
                default=list if extension.restrictions.is_list else None,
                types=[extension.type.clone()],
                local_type=TagType.ANY,
                restrictions=extension.restrictions.clone(),
            )
        else:
            attr = Attr(
                name="value",
                index=0,
                default=None,
                types=[extension.type.clone()],
                local_type=TagType.EXTENSION,
                restrictions=extension.restrictions.clone(),
            )

        item.attrs.insert(0, attr)
        item.extensions.remove(extension)
