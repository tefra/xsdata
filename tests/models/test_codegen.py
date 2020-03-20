from unittest import mock
from unittest import TestCase

from xsdata.models.codegen import Restrictions


class RestrictionsTests(TestCase):
    @mock.patch.object(Restrictions, "correct_required")
    def test_post_init(self, mock_correct_required):
        Restrictions()
        mock_correct_required.assert_called_once_with()

    def test_property_is_list(self):
        restrictions = Restrictions()
        self.assertFalse(restrictions.is_list)

        restrictions.max_occurs = 1
        self.assertFalse(restrictions.is_list)

        restrictions.max_occurs = 2
        self.assertTrue(restrictions.is_list)

    @mock.patch.object(Restrictions, "correct_required")
    def test_update(self, mock_correct_required):
        source = Restrictions(min_length=2, max_length=10)
        target = Restrictions(min_length=1, pattern=r"[A-Z]")

        target.update(source)

        self.assertEqual(2, target.min_length)
        self.assertEqual(10, target.max_length)
        self.assertEqual(r"[A-Z]", target.pattern)
        self.assertEqual(3, mock_correct_required.call_count)

    def test_correct_required(self):
        restrictions = Restrictions(min_occurs=0, max_occurs=0, required=True)
        self.assertIsNone(restrictions.required)
        self.assertIsNone(restrictions.min_occurs)
        self.assertIsNone(restrictions.max_occurs)

        restrictions = Restrictions(min_occurs=0, max_occurs=1, required=True)
        self.assertIsNone(restrictions.required)
        self.assertIsNone(restrictions.min_occurs)
        self.assertIsNone(restrictions.max_occurs)

        restrictions = Restrictions(min_occurs=1, max_occurs=1, required=False)
        self.assertTrue(restrictions.required)
        self.assertIsNone(restrictions.min_occurs)
        self.assertIsNone(restrictions.max_occurs)

        restrictions = Restrictions(max_occurs=2, required=True)
        self.assertIsNone(restrictions.required)
        self.assertEqual(0, restrictions.min_occurs)
        self.assertEqual(2, restrictions.max_occurs)

        restrictions = Restrictions(min_occurs=2, max_occurs=2, required=True)
        self.assertIsNone(restrictions.required)
        self.assertEqual(2, restrictions.min_occurs)
        self.assertEqual(2, restrictions.max_occurs)

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
            "min_exclusive": 1.1,
            "min_inclusive": 1,
            "min_length": 1,
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
