import sys
from typing import Iterator
from typing import List
from typing import Optional

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.models import Restrictions
from xsdata.exceptions import CodeGenerationError
from xsdata.utils import collections
from xsdata.utils.namespaces import build_qname
from xsdata.utils.namespaces import clean_uri
from xsdata.utils.namespaces import split_qname


class ClassUtils:
    """General reusable utils methods that didn't fit anywhere else."""

    @classmethod
    def copy_attributes(cls, source: Class, target: Class, extension: Extension):
        """
        Copy the attributes and inner classes from the source class to the
        target class and remove the extension that links the two classes
        together.

        The new attributes are prepended in the list unless if they are
        supposed to be last in a sequence.
        """
        target.extensions.remove(extension)
        target_attr_names = {attr.name for attr in target.attrs}

        index = 0
        for attr in source.attrs:
            if attr.name not in target_attr_names:
                clone = cls.clone_attribute(attr, extension.restrictions)
                cls.copy_inner_classes(source, target, clone)

                if attr.index == sys.maxsize:
                    target.attrs.append(clone)
                    continue

                target.attrs.insert(index, clone)

            index += 1

    @classmethod
    def copy_group_attributes(cls, source: Class, target: Class, attr: Attr):
        """Copy the attributes and inner classes from the source class to the
        target class and remove the group attribute that links the two classes
        together."""
        index = target.attrs.index(attr)
        target.attrs.pop(index)

        for source_attr in source.attrs:
            clone = cls.clone_attribute(source_attr, attr.restrictions)
            target.attrs.insert(index, clone)
            index += 1

            cls.copy_inner_classes(source, target, clone)

    @classmethod
    def copy_extensions(cls, source: Class, target: Class, extension: Extension):
        """Copy the extensions from the source class to the target class and
        merge the restrictions from the extension that linked the two classes
        together."""
        for ext in source.extensions:
            clone = ext.clone()
            clone.restrictions.merge(extension.restrictions)
            target.extensions.append(clone)

    @classmethod
    def clone_attribute(cls, attr: Attr, restrictions: Restrictions) -> Attr:
        """Clone the given attribute and merge its restrictions with the given
        instance."""
        clone = attr.clone()
        clone.restrictions.merge(restrictions)
        return clone

    @classmethod
    def copy_inner_classes(cls, source: Class, target: Class, attr: Attr):
        """Iterate all attr types and copy any inner classes from source to the
        target class."""
        for attr_type in attr.types:
            cls.copy_inner_class(source, target, attr, attr_type)

    @classmethod
    def copy_inner_class(
        cls, source: Class, target: Class, attr: Attr, attr_type: AttrType
    ):
        """
        Check if the given attr type is a forward reference and copy its inner
        class from the source to the target class.

        Checks:
            1. Update type if inner class in a circular reference
            2. Copy inner class, rename it if source is a simple type.
        """
        if not attr_type.forward:
            return

        # This will fail if no inner class is found, too strict???
        inner = ClassUtils.find_inner(source, attr_type.qname)

        if inner is target:
            attr_type.circular = True
        else:
            clone = inner.clone()
            clone.package = target.package
            clone.module = target.module

            # Simple type, update the name
            if clone.name == "@value":
                namespace, _ = split_qname(clone.qname)
                clone.qname = attr_type.qname = build_qname(namespace, attr.name)

            target.inner.append(clone)

    @classmethod
    def find_inner(cls, source: Class, qname: str) -> Class:
        for inner in source.inner:
            if inner.qname == qname:
                return inner

        raise CodeGenerationError(f"Missing inner class {source.qname}.{qname}")

    @classmethod
    def find_attr(cls, source: Class, name: str) -> Optional[Attr]:
        for attr in source.attrs:
            if attr.name == name:
                return attr

        return None

    @classmethod
    def flatten(cls, target: Class, module: str) -> Iterator[Class]:
        target.module = module

        while target.inner:
            yield from cls.flatten(target.inner.pop(), module)

        for attr in target.attrs:
            attr.types = collections.unique_sequence(attr.types, key="qname")
            for tp in attr.types:
                tp.forward = False

        yield target

    @classmethod
    def reduce(cls, classes: List[Class]) -> List[Class]:
        result = []
        indexed = collections.group_by(classes, key=lambda x: x.qname)
        for group in indexed.values():
            group.sort(key=lambda x: len(x.attrs))
            target = group.pop()

            for source in group:
                target.mixed = target.mixed or source.mixed
                cls.merge_attributes(target, source)

            result.append(target)

        return result

    @classmethod
    def merge_attributes(cls, target: Class, source: Class):
        for attr in source.attrs:

            existing = collections.first(
                x
                for x in target.attrs
                if x.name == attr.name
                and x.tag == attr.tag
                and x.namespace == attr.namespace
            )

            if not existing:
                target.attrs.append(attr)
            else:
                min_occurs = existing.restrictions.min_occurs or 0
                max_occurs = existing.restrictions.max_occurs or 1
                attr_min_occurs = attr.restrictions.min_occurs or 0
                attr_max_occurs = attr.restrictions.max_occurs or 1

                existing.restrictions.min_occurs = min(min_occurs, attr_min_occurs)
                existing.restrictions.max_occurs = max(max_occurs, attr_max_occurs)
                existing.types.extend(attr.types)

        target.attrs.sort(key=lambda x: x.index)

    @classmethod
    def rename_attribute_by_preference(cls, a: Attr, b: Attr):
        """
        Decide and rename one of the two given attributes.

        When both attributes are derived from the same xs:tag and one of the two fields
        has a specific namespace prepend it to the name. Preferable rename the second
        attribute.

        Otherwise append the derived from tag to the name of one of the two attributes.
        Preferably rename the second field or the field derived from xs:attribute.
        """
        if a.tag == b.tag and (a.namespace or b.namespace):
            change = b if b.namespace else a
            assert change.namespace is not None
            change.name = f"{clean_uri(change.namespace)}_{change.name}"
        else:
            change = b if b.is_attribute else a
            change.name = f"{change.name}_{change.tag}"
