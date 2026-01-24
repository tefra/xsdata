from collections import defaultdict

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr, Class, get_restriction_choice
from xsdata.utils import collections


class UpdateAttributesEffectiveChoice(HandlerInterface):
    """Detect implied repeated choices and update them.

    valid eg: <a/><b/><a/><c/>
    symmetrical sequence: <a/><b/><a/><b/>
    """

    __slots__ = ()

    def process(self, target: Class) -> None:
        """Process entrypoint for classes.

        Ignore enumerations, for performance reasons.

        Args:
            target: The target class instance
        """
        if target.is_enumeration:
            return

        groups = self.group_repeating_attrs(target)
        if groups:
            groups = list(collections.connected_components(groups))
            target.attrs = self.merge_attrs(target, groups)

            self.reset_symmetrical_choices(target)

    @classmethod
    def reset_symmetrical_choices(cls, target: Class):
        """Mark symmetrical choices as sequences.

        Args:
            target: The target class instance
        """
        groups = collections.group_by(target.attrs, get_restriction_choice)
        for choice, attrs in groups.items():
            if choice is None or choice > 0:
                continue

            min_occurs = set()
            max_occurs = set()
            sequences = set()
            for attr in attrs:
                min_occurs.add(attr.restrictions.min_occurs)
                max_occurs.add(attr.restrictions.max_occurs)

                if attr.restrictions.sequence:
                    sequences.add(attr.restrictions.sequence)

            if len(min_occurs) == len(max_occurs) == len(sequences) == 1:
                for attr in attrs:
                    assert attr.restrictions.max_occurs is not None
                    assert attr.restrictions.sequence is not None

                    attr.restrictions.choice = None
                    cls.reset_effective_choice(
                        attr.restrictions.path,
                        attr.restrictions.sequence,
                        attr.restrictions.max_occurs,
                    )

    @classmethod
    def reset_effective_choice(
        cls,
        paths: list[tuple[str, int, int, int]],
        index: int,
        max_occur: int,
    ):
        """Update an attr path to resemble a repeatable sequence.

        Args:
            paths: The paths of an attr
            index: The sequence index
            max_occur: The new max occurrences
        """
        for i, path in enumerate(paths):
            if path[0] == "s" and path[1] == index and path[3] == 1:
                new_path = (*path[:-1], max_occur)
                paths[i] = new_path
                break

    @classmethod
    def merge_attrs(cls, target: Class, groups: list[list[int]]) -> list[Attr]:
        """Merge same name/tag/namespace attrs.

        Args:
            target: The target class
            groups: The list of connected attr indexes

        Returns:
            The final list of target class attrs
        """
        attrs = []

        for index, attr in enumerate(target.attrs):
            group = collections.find_connected_component(groups, index)

            if group == -1:
                attrs.append(attr)
                continue

            pos = collections.find(attrs, attr)
            if pos == -1:
                attr.restrictions.choice = (group * -1) - 1
                attrs.append(attr)
            else:
                existing = attrs[pos]
                assert existing.restrictions.min_occurs is not None
                assert existing.restrictions.max_occurs is not None

                existing.restrictions.min_occurs += attr.restrictions.min_occurs or 0
                existing.restrictions.max_occurs += attr.restrictions.max_occurs or 0

        return attrs

    @classmethod
    def group_repeating_attrs(cls, target: Class) -> list[list[int]]:
        """Create a list of indexes of the same attrs.

        Example: [
            [0, 1 ,2],
            [3, 4, 6],
            [5,]
        ]

        Args:
            target: The target class instance

        Returns:
            The list of indexes

        """
        counters = defaultdict(list)
        for index, attr in enumerate(target.attrs):
            if not attr.is_attribute:
                counters[attr.key].append(index)

        result = []
        for indices in counters.values():
            if len(indices) > 1:
                # Check if all occurrences have the same choice ID
                # If they have different choice IDs (and both are not None),
                # they're in different choice blocks and shouldn't be merged
                choice_ids = {target.attrs[i].restrictions.choice for i in indices}

                # Also check if all occurrences have the same path length
                # If they have different path lengths within the same choice,
                # they're in different branches (mutually exclusive)
                path_lengths = {len(target.attrs[i].restrictions.path) for i in indices}

                if None in choice_ids:
                    # At least one element is outside a choice, so they can co-exist
                    # (e.g., one in outer sequence, one in inner choice branch)
                    result.append(list(range(indices[0], indices[-1] + 1)))
                elif len(choice_ids) == 1 and len(path_lengths) == 1:
                    # All elements in the same choice at the same nesting level
                    # This is a repeating pattern, group them
                    result.append(list(range(indices[0], indices[-1] + 1)))
                # else: different choices or same choice but different nesting levels
                # = mutually exclusive branches, don't group

        return result
