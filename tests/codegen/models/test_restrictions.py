import sys
from unittest import TestCase

from xsdata.codegen.models import Restrictions


class RestrictionsTests(TestCase):
    def setUp(self) -> None:
        self.restrictions = Restrictions(
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
            path=[("s", 0, 1, 1)],
        )

    def test_property_is_list(self):
        restrictions = Restrictions()
        self.assertFalse(restrictions.is_list)

        restrictions.max_occurs = 1
        self.assertFalse(restrictions.is_list)

        restrictions.max_occurs = 2
        self.assertTrue(restrictions.is_list)

    def test_property_is_prohibited(self):
        self.assertFalse(Restrictions().is_prohibited)
        self.assertTrue(Restrictions(max_occurs=0).is_prohibited)

    def test_merge(self):
        source = Restrictions(min_length=2, max_length=10, format="base16")
        target = Restrictions(min_length=1, pattern=r"[A-Z]")

        target.merge(source)

        self.assertEqual(2, target.min_length)
        self.assertEqual(10, target.max_length)
        self.assertEqual(r"[A-Z]", target.pattern)
        self.assertEqual("base16", target.format)

    def test_merge_ignore_nillable(self):
        parent = Restrictions(nillable=True)
        child = Restrictions()

        child.merge(parent)
        self.assertIsNone(child.nillable)

        child.nillable = False
        child.merge(parent)
        self.assertFalse(child.nillable)

    def test_merge_occurs(self):
        a = Restrictions()
        b = Restrictions()

        a.merge(b)

        self.assertIsNone(a.min_occurs)
        self.assertIsNone(a.max_occurs)

        b.min_occurs = 0
        b.max_occurs = 1
        a.merge(b)
        self.assertEqual(0, a.min_occurs)
        self.assertEqual(1, a.max_occurs)

    def test_asdict(self):
        expected = {
            "explicit_timezone": "+1",
            "fraction_digits": 2,
            "length": 5,
            "max_exclusive": "1",
            "max_inclusive": "1.1",
            "max_length": 10,
            "min_exclusive": "1.1",
            "min_inclusive": "1",
            "min_length": 1,
            "nillable": True,
            "pattern": "[A-Z]",
            "total_digits": 333,
            "white_space": "collapse",
        }
        self.assertEqual(expected, self.restrictions.asdict())

        self.restrictions.nillable = None

        del expected["nillable"]
        expected["required"] = True
        self.assertEqual(expected, self.restrictions.asdict())

    def test_asdict_with_types(self):
        expected = {
            "explicit_timezone": "+1",
            "fraction_digits": 2,
            "length": 5,
            "max_exclusive": 1.0,  # str -> float
            "max_inclusive": 1.1,  # str -> float
            "max_length": 10,
            "min_exclusive": 1.1,  # str -> float
            "min_inclusive": 1.0,  # str -> float
            "min_length": 1,
            "nillable": True,
            "pattern": "[A-Z]",
            "total_digits": 333,
            "white_space": "collapse",
        }
        self.assertEqual(expected, self.restrictions.asdict(types=[float]))

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
