import re
import sys
from collections import defaultdict
from typing import Dict
from typing import List
from typing import Optional

from lxml.etree import QName

from xsdata.logger import logger
from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.models.codegen import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import NamespaceType
from xsdata.models.enums import Tag
from xsdata.utils import text


class ClassUtils:

    INCLUDES_NONE = 0
    INCLUDES_SOME = 1
    INCLUDES_ALL = 2

    @classmethod
    def compare_attributes(cls, source: Class, target: Class) -> int:
        if source is target:
            return cls.INCLUDES_ALL

        if not target.attrs:
            return cls.INCLUDES_NONE

        source_attrs = {attr.name for attr in source.attrs}
        target_attrs = {attr.name for attr in target.attrs}
        difference = source_attrs - target_attrs

        if not difference:
            return cls.INCLUDES_ALL
        if len(difference) != len(source_attrs):
            return cls.INCLUDES_SOME

        return cls.INCLUDES_NONE

    @classmethod
    def sanitize_attribute_restrictions(cls, attr: Attr):
        restrictions = attr.restrictions
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
    def sanitize_attribute_sequence(cls, attrs: List[Attr], index: int):
        """Reset the attribute at the given index if it has no siblings with
        the sequential restriction."""

        attr = attrs[index]
        before = attrs[index - 1] if index - 1 >= 0 else None
        after = attrs[index + 1] if index + 1 < len(attrs) else None

        if not attr.is_list:
            attr.restrictions.sequential = False

        if (
            not attr.restrictions.sequential
            or (before and before.restrictions.sequential)
            or (after and after.restrictions.sequential and after.is_list)
        ):
            return

        attr.restrictions.sequential = False

    @classmethod
    def sanitize_attribute_name(cls, attr: Attr):
        if attr.is_enumeration:
            attr.name = attr.default
            if re.match(r"^-\d*\.?\d+$", attr.name):
                attr.name = f"value_minus_{attr.name}"
            else:
                attr.name = re.sub("[^0-9a-zA-Z]", " ", attr.name).strip()
        else:
            attr.name = re.sub("[^0-9a-zA-Z]", " ", text.suffix(attr.name)).strip()

        if not attr.name:
            attr.name = "value"
        elif not attr.name[0].isalpha():
            attr.name = f"value_{attr.name}"

    @classmethod
    def sanitize_duplicate_attribute_names(cls, attrs: List[Attr]) -> None:
        grouped: Dict[str, List[Attr]] = dict()
        for attr in attrs:
            grouped.setdefault(attr.name.lower(), []).append(attr)

        for items in grouped.values():
            if len(items) == 1:
                continue

            if len(items) > 2 or items[0].is_enumeration:
                for index in range(1, len(items)):
                    num = 1
                    name = items[index].name

                    while any(attr for attr in attrs if attr.name == f"{name}_{num}"):
                        num += 1

                    items[index].name = f"{name}_{num}"
            else:
                first, second = items
                if first.tag == second.tag and any((first.namespace, second.namespace)):
                    change = second if second.namespace else first
                    change.name = f"{change.namespace}_{change.name}"
                else:
                    change = second if second.is_attribute else first
                    change.name = f"{change.name}_{change.tag}"

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

                if attr.index == sys.maxsize:
                    target.attrs.append(clone)
                    continue

                target.attrs.insert(index, clone)
            index += 1

        cls.copy_inner_classes(source, target)

    @classmethod
    def clone_attribute(
        cls, attr: Attr, restrictions: Restrictions, prefix: Optional[str] = None
    ) -> Attr:
        clone = attr.clone()
        clone.restrictions.merge(restrictions)
        if prefix:
            for attr_type in clone.types:
                if not attr_type.native and attr_type.name.find(":") == -1:
                    attr_type.name = f"{prefix}:{attr_type.name}"

        return clone

    @classmethod
    def merge_attribute_type(
        cls, source: Class, target: Class, attr: Attr, attr_type: AttrType
    ):
        if len(source.attrs) != 1:
            logger.warning("Missing implementation: %s", source.type.__name__)
            cls.reset_attribute_type(attr_type)
        else:
            source_attr = source.attrs[0]
            index = attr.types.index(attr_type)
            attr.types.pop(index)

            for source_attr_type in source_attr.types:
                clone_type = source_attr_type.clone()
                attr.types.insert(index, clone_type)
                index += 1

            restrictions = source_attr.restrictions.clone()
            restrictions.merge(attr.restrictions)
            attr.restrictions = restrictions
            cls.copy_inner_classes(source, target)

    @classmethod
    def copy_inner_classes(cls, source: Class, target: Class):
        """
        Copy safely inner classes from source to target class.

        Checks:
            1. Inner is the target class, skip and mark as self reference
            2. Inner with same name exists, skip
        """
        for inner in source.inner:
            if inner is target:
                for attr in target.attrs:
                    for attr_type in attr.types:
                        if attr_type.forward_ref and attr_type.name == inner.name:
                            attr_type.self_ref = True
            elif not any(existing.name == inner.name for existing in target.inner):
                target.inner.append(inner)

    @classmethod
    def merge_redefined_classes(cls, classes: List[Class]):
        """Merge original and redefined classes."""
        grouped: Dict[str, List[Class]] = defaultdict(list)
        for item in classes:
            grouped[f"{item.type.__name__}{item.source_qname()}"].append(item)

        for items in grouped.values():
            if len(items) == 1:
                continue

            winner: Class = items.pop()
            for item in items:
                classes.remove(item)

                self_extension = next(
                    (
                        ext
                        for ext in winner.extensions
                        if text.suffix(ext.type.name) == winner.name
                    ),
                    None,
                )

                if not self_extension:
                    continue

                cls.copy_attributes(item, winner, self_extension)
                for looser_ext in item.extensions:
                    new_ext = looser_ext.clone()
                    new_ext.restrictions.merge(self_extension.restrictions)
                    winner.extensions.append(new_ext)

    @classmethod
    def update_abstract_classes(cls, classes: List[Class]):
        """
        Update classes with the same qualified name to set implied abstract
        flags.

        If a non abstract xs:element exists in the list mark the rest
        xs:complexType(s) as abstract.
        """

        element = next((obj for obj in classes if obj.is_element), None)
        if element:
            for obj in classes:
                if obj is not element and obj.is_complex:
                    obj.abstract = True

    @classmethod
    def create_mixed_attribute(cls, target: Class):
        if not target.mixed or target.has_wild_attr:
            return

        attr = Attr(
            name="content",
            local_name="content",
            index=0,
            types=[AttrType(name=DataType.ANY_TYPE.code, native=True)],
            tag=Tag.ANY,
            namespace=NamespaceType.ANY.value,
        )
        target.attrs.insert(0, attr)

    @classmethod
    def create_default_attribute(cls, item: Class, extension: Extension):
        if extension.type.native_code == DataType.ANY_TYPE.code:
            attr = Attr(
                name="any_element",
                local_name="any_element",
                index=0,
                default=list if extension.restrictions.is_list else None,
                types=[extension.type.clone()],
                tag=Tag.ANY,
                namespace=NamespaceType.ANY.value,
                restrictions=extension.restrictions.clone(),
            )
        else:
            attr = Attr(
                name="value",
                local_name="value",
                index=0,
                default=None,
                types=[extension.type.clone()],
                tag=Tag.EXTENSION,
                restrictions=extension.restrictions.clone(),
            )

        item.attrs.insert(0, attr)
        item.extensions.remove(extension)

    @classmethod
    def create_reference_attribute(cls, source: Class, qname: QName) -> Attr:
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
            tag=source.type.__name__,
            namespace=source.namespace,
        )

    @classmethod
    def find_attribute(cls, attrs: List[Attr], attr: Attr) -> int:
        try:
            return attrs.index(attr)
        except ValueError:
            return -1

    @classmethod
    def reset_attribute_type(cls, attr_type: AttrType):
        attr_type.name = DataType.STRING.code
        attr_type.native = True
        attr_type.self_ref = False
        attr_type.forward_ref = False
