import sys
from unittest import TestCase

from xsdata.codegen.models import Restrictions


class RestrictionsTests(TestCase):
    def test_property_is_list(self):
        restrictions = Restrictions()
        self.assertFalse(restrictions.is_list)

        restrictions.max_occurs = 1
        self.assertFalse(restrictions.is_list)

        restrictions.max_occurs = 2
        self.assertTrue(restrictions.is_list)

    def test_merge(self):
        source = Restrictions(min_length=2, max_length=10)
        target = Restrictions(min_length=1, pattern=r"[A-Z]")

        target.merge(source)

        self.assertEqual(2, target.min_length)
        self.assertEqual(10, target.max_length)
        self.assertEqual(r"[A-Z]", target.pattern)

    def test_merge_ignore_nillable(self):
        parent = Restrictions(nillable=True)
        child = Restrictions()

        child.merge(parent)
        self.assertIsNone(child.nillable)

        child.nillable = False
        child.merge(parent)
        self.assertFalse(child.nillable)

    def test_asdict(self):
        restrictions = Restrictions(
            required=True,
            prohibited=None,
            min_occurs=1,
            max_occurs=1,
            min_exclusive="1.1",
            min_inclusive="1",
            min_length=1,
            max_exclusive="1",
            max_inclusive="1.1",
            max_length=10,
            total_digits=333,
            fraction_digits=2,
            length=5,
            white_space="collapse",
            pattern=r"[A-Z]",
            explicit_timezone="+1",
            nillable=True,
        )

        expected = {
            "explicit_timezone": "+1",
            "fraction_digits": 2,
            "length": 5,
            "max_exclusive": "1",
            "max_inclusive": "1.1",
            "max_length": 10,
            "max_occurs": 1,
            "min_exclusive": "1.1",
            "min_inclusive": "1",
            "min_length": 1,
            "min_occurs": 1,
            "nillable": True,
            "pattern": "[A-Z]",
            "required": True,
            "total_digits": 333,
            "white_space": "collapse",
        }
        self.assertEqual(expected, restrictions.asdict())

    def test_asdict_with_types(self):
        restrictions = Restrictions(
            required=True,
            prohibited=None,
            min_occurs=1,
            max_occurs=1,
            min_exclusive="1.1",
            min_inclusive="1",
            min_length=1,
            max_exclusive="1",
            max_inclusive="1.1",
            max_length=10,
            total_digits=333,
            fraction_digits=2,
            length=5,
            white_space="collapse",
            pattern=r"[A-Z]",
            explicit_timezone="+1",
            nillable=True,
        )

        expected = {
            "explicit_timezone": "+1",
            "fraction_digits": 2,
            "length": 5,
            "max_exclusive": 1.0,  # str -> float
            "max_inclusive": 1.1,  # str -> float
            "max_length": 10,
            "max_occurs": 1,
            "min_exclusive": 1.1,  # str -> float
            "min_inclusive": 1.0,  # str -> float
            "min_length": 1,
            "min_occurs": 1,
            "nillable": True,
            "pattern": "[A-Z]",
            "required": True,
            "total_digits": 333,
            "white_space": "collapse",
        }
        self.assertEqual(expected, restrictions.asdict(types=[float]))

    def test_asdict_with_implied_types(self):
        restrictions = Restrictions(min_occurs=1, max_occurs=4)
        self.assertEqual({"max_occurs": 4, "min_occurs": 1}, restrictions.asdict())

        restrictions.min_occurs = 0
        self.assertEqual({"max_occurs": 4}, restrictions.asdict())

        restrictions.max_occurs = sys.maxsize
        self.assertEqual({}, restrictions.asdict())

    def test_clone(self):
        restrictions = Restrictions(max_occurs=2)
        clone = restrictions.clone()

        self.assertEqual(clone, restrictions)
        self.assertIsNot(clone, restrictions)
