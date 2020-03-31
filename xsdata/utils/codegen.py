from typing import List
from typing import Optional

from lxml.etree import QName

from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
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
    def sanitize_attributes(cls, target: Class):
        for attr in target.attrs:
            cls.sanitize_attribute(attr)
            cls.sanitize_restrictions(attr.restrictions)

        for i in range(len(target.attrs)):
            cls.sanitize_sequential(target.attrs, i)

        for inner in target.inner:
            cls.sanitize_attributes(inner)

    @classmethod
    def sanitize_attribute(cls, attr: Attr):
        if attr.is_list:
            attr.fixed = False
        else:
            attr.restrictions.sequential = False

        if attr.is_optional:
            attr.fixed = False
            attr.default = None

    @classmethod
    def sanitize_restrictions(cls, restrictions: Restrictions):
        min_occurs = restrictions.min_occurs or 0
        max_occurs = restrictions.max_occurs or 0

        if min_occurs == 0 and max_occurs <= 1:
            restrictions.required = None
            restrictions.min_occurs = None
            restrictions.max_occurs = None
        if min_occurs == 1 and max_occurs == 1:
            restrictions.required = True
            restrictions.min_occurs = None
            restrictions.max_occurs = None
        elif restrictions.max_occurs and max_occurs > 1:
            restrictions.min_occurs = min_occurs
            restrictions.required = None

    @classmethod
    def sanitize_sequential(cls, attrs: List[Attr], index: int):
        """Reset the attribute at the given index if it has no siblings with
        the sequential restriction."""

        if (
            not attrs[index].restrictions.sequential
            or (index - 1 >= 0 and attrs[index - 1].restrictions.sequential)
            or (index + 1 < len(attrs) and attrs[index + 1].restrictions.sequential)
        ):
            return

        attrs[index].restrictions.sequential = False

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
            pos = cls.find_attribute(result, attr)
            existing = result[pos] if pos > -1 else None

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
                local_name="##any_element",
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
                local_name="value",
                index=0,
                default=None,
                types=[extension.type.clone()],
                local_type=TagType.EXTENSION,
                restrictions=extension.restrictions.clone(),
            )

        item.attrs.insert(0, attr)
        item.extensions.remove(extension)

    @classmethod
    def create_reference_attribute(cls, source: Class, qname: QName):
        prefix = None
        if qname.namespace != source.source_namespace:
            prefix = source.source_prefix

        reference = f"{prefix}:{source.name}" if prefix else source.name
        return Attr(
            name=source.name,
            local_name=source.name,
            index=0,
            default=None,
            types=[AttrType(name=reference)],
            local_type=source.type.__name__,
            namespace=source.namespace,
        )

    @classmethod
    def find_attribute(cls, attrs: List[Attr], attr: Attr):
        try:
            return attrs.index(attr)
        except ValueError:
            return -1
