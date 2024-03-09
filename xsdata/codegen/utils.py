import sys
from typing import Iterator, List, Optional, Set

from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.models import (
    Attr,
    AttrType,
    Class,
    Extension,
    Restrictions,
    Status,
    get_qname,
    get_slug,
)
from xsdata.models.enums import DataType
from xsdata.utils import collections, namespaces, text


class ClassUtils:
    """General reusable utils methods that didn't fit anywhere else."""

    @classmethod
    def find_value_attr(cls, source: Class) -> Attr:
        """Find the text attribute of the class.

        Args:
            source: The source class instance

        Returns:
            The matched attr instance.

        Raises:
             CodeGenerationError: If no text node/attribute exists
        """
        for attr in source.attrs:
            if not attr.xml_type:
                return attr

        raise CodegenError("Class has no value attr", type=source.qname)

    @classmethod
    def remove_attribute(cls, target: Class, attr: Attr):
        """Safely remove the given attr from the target class.

        Make sure you match the attr by the reference id,
        simple comparison might remove a duplicate attr
        with the same tag/namespace/name.

        Args:
            target: The target class instance
            attr: The attr instance to remove

        """
        target.attrs = [at for at in target.attrs if id(at) != id(attr)]

    @classmethod
    def clean_inner_classes(cls, target: Class):
        """Check if there are orphan inner classes and remove them.

        Args:
            target: The target class instance to inspect.
        """
        for inner in list(target.inner):
            if cls.is_orphan_inner(target, inner):
                target.inner.remove(inner)

    @classmethod
    def is_orphan_inner(cls, target: Class, inner: Class) -> bool:
        """Check if the inner class is references in the target class.

        Args:
            target: The target class instance
            inner: The inner class instance

        Returns:
            The bool result.
        """
        for attr in target.attrs:
            for attr_type in attr.types:
                if attr_type.forward and attr_type.qname == inner.qname:
                    return False

        return True

    @classmethod
    def copy_attributes(cls, source: Class, target: Class, extension: Extension):
        """Copy the attrs from the source to the target class.

        Remove the extension instance that connects the two classes.
        The new attrs are prepended in the list unless if they are
        supposed to be last in a sequence.

        Args:
            source: The source/parent class instance
            target: The target/child class instance
            extension: The extension instance that connects the classes
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
        """Copy the attrs of the source class to the target class.

        The attr represents a reference to the source class which is
        derived from xs:group or xs:attributeGroup and wil be removed.

        Args:
            source: The source class instance
            target: The target class instance
            attr: The group attr instance
        """
        index = target.attrs.index(attr)
        target.attrs.pop(index)

        for source_attr in source.attrs:
            clone = cls.clone_attribute(source_attr, attr.restrictions)
            target.attrs.insert(index, clone)
            index += 1

            cls.copy_inner_classes(source, target, clone)

    @classmethod
    def copy_extensions(cls, source: Class, target: Class, extension: Extension):
        """Copy the source class extensions to the target class instance.

        Merge the extension restrictions with the source class extensions
        restrictions.

        Args:
            source: The source class instance
            target: The target class instance
            extension: The extension instance that links the two classes together
        """
        for ext in source.extensions:
            clone = ext.clone()
            clone.restrictions.merge(extension.restrictions)
            target.extensions.append(clone)

    @classmethod
    def clone_attribute(cls, attr: Attr, restrictions: Restrictions) -> Attr:
        """Clone the given attr and merge its restrictions with the given.

        Args:
            attr: The source attr instance
            restrictions: The additional restrictions, originated from
                a substitution or another attr.
        """
        clone = attr.clone()
        clone.restrictions.merge(restrictions)
        return clone

    @classmethod
    def copy_inner_classes(cls, source: Class, target: Class, attr: Attr):
        """Copy inner classes from source to the target class instance.

        Args:
            source: The source class instance
            target: The target class instance
            attr: The attr with the possible forward references
        """
        for attr_type in attr.types:
            cls.copy_inner_class(source, target, attr_type)

    @classmethod
    def copy_inner_class(cls, source: Class, target: Class, attr_type: AttrType):
        """Find and copy the inner class from source to the target class instance.

        Steps:
            - Skip If the attr type is not a forward reference
            - Validate the inner class is not a circular reference to the target
            - Otherwise copy the inner class, and make sure it is re-sent for
                processing

        Args:
            source: The source class instance
            target: The target class instance
            attr_type: The attr type with the possible forward reference
        """
        if not attr_type.forward:
            return

        inner = ClassUtils.find_inner(source, attr_type.qname)
        if inner is target:
            attr_type.circular = True
            attr_type.reference = target.ref
        else:
            # In extreme cases this adds duplicate inner classes
            clone = inner.clone()
            clone.package = target.package
            clone.module = target.module
            clone.status = Status.RAW
            attr_type.reference = clone.ref
            target.inner.append(clone)

    @classmethod
    def find_inner(cls, source: Class, qname: str) -> Class:
        """Find an inner class in the source class by its qualified name.

        Args:
            source: The parent class instance
            qname: The inner class qualified name

        Returns:
            The inner class instance

        Raises:
            CodeGenerationError: If no inner class matched.
        """
        for inner in source.inner:
            if inner.qname == qname:
                return inner

        raise CodegenError("Missing inner class", parent=source, qname=qname)

    @classmethod
    def find_attr(cls, source: Class, name: str) -> Optional[Attr]:
        """Find an attr in the source class by its name.

        Args:
            source: The source class instance
            name: The attr name to lookup

        Returns:
            An attr instance or None if no attr matched.
        """
        for attr in source.attrs:
            if attr.name == name:
                return attr

        return None

    @classmethod
    def flatten(cls, target: Class, location: str) -> Iterator[Class]:
        """Flatten the target class instance and its inner classes.

        The inner classes are removed from target instance!

        Args:
            target: The target class instance
            location: The source location of the target class

        Yields:
            An iterator over all the found classes.
        """
        target.location = location

        while target.inner:
            yield from cls.flatten(target.inner.pop(), location)

        for attr in target.attrs:
            attr.types = collections.unique_sequence(attr.types, key="qname")
            for tp in attr.types:
                tp.forward = False

        yield target

    @classmethod
    def reduce_classes(cls, classes: List[Class]) -> List[Class]:
        """Find duplicate classes and attrs and reduce them.

        Args:
            classes: A list of classes

        Returns:
            A list of unique classes with no duplicate attrs.
        """
        result = []
        for group in collections.group_by(classes, key=get_qname).values():
            target = group[0].clone()
            target.attrs = cls.reduce_attributes(group)
            target.mixed = any(x.mixed for x in group)

            cls.cleanup_class(target)
            result.append(target)

        return result

    @classmethod
    def reduce_attributes(cls, classes: List[Class]) -> List[Attr]:
        """Find and merge duplicate attrs from the given class list.

        Args:
            classes: A list of class instances

        Returns:
            A list of unique attr instances.
        """
        result = []
        for attr in cls.sorted_attrs(classes):
            added = False
            optional = False
            for obj in classes:
                pos = collections.find(obj.attrs, attr)
                if pos == -1:
                    optional = True
                elif not added:
                    added = True
                    result.append(obj.attrs.pop(pos))
                else:
                    cls.merge_attributes(result[-1], obj.attrs.pop(pos))

            if optional:
                result[-1].restrictions.min_occurs = 0

        return result

    @classmethod
    def sorted_attrs(cls, classes: List[Class]) -> List[Attr]:
        """Sort and return the attrs from all the class list.

        The list contains duplicate classes, the method tries
        to find all the attrs and sorts them by first occurrence.

        Args:
            classes: A list of duplicate class instances.

        Returns:
            A list of sorted duplicate attr instances.
        """
        attrs: List[Attr] = []
        classes.sort(key=lambda x: len(x.attrs), reverse=True)

        for obj in classes:
            i = 0
            obj_attrs = obj.attrs.copy()

            while obj_attrs:
                pos = collections.find(attrs, obj_attrs[i])
                i += 1

                if pos > -1:
                    insert = obj_attrs[: i - 1]
                    del obj_attrs[:i]
                    while insert:
                        attrs.insert(pos, insert.pop())

                    i = 0
                elif i == len(obj_attrs):
                    attrs.extend(obj_attrs)
                    obj_attrs.clear()

        return attrs

    @classmethod
    def merge_attributes(cls, target: Attr, source: Attr):
        """Merge the source attr into the target instance.

        Merge the types, select the min min_occurs and the max max_occurs
        from the two instances and copy the source sequence number
        to the target if it's currently not set.

        Args:
            target: The target attr instance which will be updated
            source: The source attr instance
        """
        target.types.extend(tp for tp in source.types if tp not in target.types)

        target.restrictions.min_occurs = min(
            target.restrictions.min_occurs or 0,
            source.restrictions.min_occurs or 0,
        )

        target.restrictions.max_occurs = max(
            target.restrictions.max_occurs or 1,
            source.restrictions.max_occurs or 1,
        )

        if source.restrictions.sequence is not None:
            target.restrictions.sequence = source.restrictions.sequence

    @classmethod
    def rename_attribute_by_preference(cls, a: Attr, b: Attr):
        """Decide and rename one of the two given attributes.

        When both attributes are derived from the same xs:tag and one of
        the two fields has a specific namespace prepend it to the name.
        Preferable rename the second attribute.

        Otherwise, append the derived from tag to the name of one of the
        two attributes. Preferably rename the second field or the field
        derived from xs:attribute.

        Args:
            a: The first attr instance
            b: The second attr instance
        """
        if a.tag == b.tag and (a.namespace or b.namespace):
            change = b if b.namespace else a
            assert change.namespace is not None
            change.name = f"{namespaces.clean_uri(change.namespace)}_{change.name}"
        else:
            change = b if b.is_attribute else a
            change.name = f"{change.name}_{change.tag}"

    @classmethod
    def rename_attributes_by_index(cls, attrs: List[Attr], rename: List[Attr]):
        """Append the next available index number to all the rename attr names.

        Args:
            attrs: A list of attr instances whose names must be protected
            rename: A list of attr instances that need to be renamed
        """
        for index in range(1, len(rename)):
            reserved = set(map(get_slug, attrs))
            name = rename[index].name
            rename[index].name = cls.unique_name(name, reserved)

    @classmethod
    def unique_name(cls, name: str, reserved: Set[str]) -> str:
        """Append the next available index number to the name.

        Args:
            name: An object name
            reserved: A set of reserved names

        Returns:
            The new name with the index suffix
        """
        if text.alnum(name) in reserved:
            index = 1
            while text.alnum(f"{name}_{index}") in reserved:
                index += 1

            return f"{name}_{index}"

        return name

    @classmethod
    def cleanup_class(cls, target: Class):
        """Go through the target class attrs and filter their types.

        Removes duplicate and invalid types.

        Args:
            target: The target class instance to inspect
        """
        for attr in target.attrs:
            attr.types = cls.filter_types(attr.types)

    @classmethod
    def filter_types(cls, types: List[AttrType]) -> List[AttrType]:
        """Remove duplicate and invalid types.

        Invalid:
            1. xs:error
            2. xs:anyType and xs:anySimpleType when there are other types present

        Args:
            types: A list of attr type instances

        Returns:
            The new list of unique and valid attr type instances.
        """
        types = collections.unique_sequence(types, key="qname")
        types = collections.remove(types, lambda x: x.datatype == DataType.ERROR)

        if len(types) > 1:
            types = collections.remove(
                types,
                lambda x: x.datatype in (DataType.ANY_TYPE, DataType.ANY_SIMPLE_TYPE),
            )

        if not types:
            types.append(AttrType(qname=str(DataType.STRING), native=True))

        return types
