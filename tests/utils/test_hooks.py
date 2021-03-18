from unittest import mock
from unittest import TestCase

from xsdata.utils.hooks import load_entry_points


class HooksTests(TestCase):
    @mock.patch("xsdata.utils.hooks.importlib_metadata.entry_points")
    def test_load_entry_points(self, mock_entry_points):
        first_ep = mock.Mock()
        second_ep = mock.Mock()
        third_ep = mock.Mock()

        mock_entry_points.return_value = {
            "foo": [first_ep, second_ep],
            "bar": [third_ep],
        }

        load_entry_points("foo")
        first_ep.load.assert_called_once_with()
        second_ep.load.assert_called_once_with()
        self.assertEqual(0, third_ep.load.call_count)

        load_entry_points("bar")
        third_ep.load.assert_called_once_with()
