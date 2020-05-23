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

    def test_update(self):
        source = Restrictions(min_length=2, max_length=10)
        target = Restrictions(min_length=1, pattern=r"[A-Z]")

        target.merge(source)

        self.assertEqual(2, target.min_length)
        self.assertEqual(10, target.max_length)
        self.assertEqual(r"[A-Z]", target.pattern)

    def test_asdict(self):
        restrictions = Restrictions(
            required=True,
            prohibited=None,
            min_occurs=1,
            max_occurs=1,
            min_exclusive=1.1,
            min_inclusive=1,
            min_length=1,
            max_exclusive=1,
            max_inclusive=1.1,
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
            "max_exclusive": 1,
            "max_inclusive": 1.1,
            "max_length": 10,
            "max_occurs": 1,
            "min_exclusive": 1.1,
            "min_inclusive": 1,
            "min_length": 1,
            "min_occurs": 1,
            "nillable": True,
            "pattern": "[A-Z]",
            "required": True,
            "total_digits": 333,
            "white_space": "collapse",
        }
        self.assertEqual(expected, restrictions.asdict())

    def test_clone(self):
        restrictions = Restrictions(max_occurs=2)
        clone = restrictions.clone()

        self.assertEqual(clone, restrictions)
        self.assertIsNot(clone, restrictions)
