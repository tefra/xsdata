from unittest import mock
from unittest import TestCase

from requests import Response

from xsdata.formats.dataclass.transports import DefaultTransport


class DefaultTransportTest(TestCase):
    @mock.patch.object(Response, "content", new_callable=mock.PropertyMock)
    @mock.patch.object(Response, "raise_for_status")
    @mock.patch("xsdata.formats.dataclass.transports.requests.get")
    def test_get(self, mock_get, mock_raise_for_status, mock_content):
        transport = DefaultTransport()
        params = {"a": "b"}
        url = "http://endpoint.stub/action"
        headers = {"content-type": "text/xml"}

        mock_get.return_value = Response()
        mock_content.return_value = b"foobar"

        result = transport.get(url, params, headers)
        self.assertEqual("foobar", result.decode())
        mock_raise_for_status.assert_called_once_with()
        mock_get.assert_called_once_with(
            url, params=params, headers=headers, timeout=transport.timeout
        )

    @mock.patch.object(Response, "content", new_callable=mock.PropertyMock)
    @mock.patch.object(Response, "raise_for_status")
    @mock.patch("xsdata.formats.dataclass.transports.requests.post")
    def test_post(self, mock_post, mock_raise_for_status, mock_content):
        transport = DefaultTransport(timeout=1.0)
        data = {"a": "b"}
        url = "http://endpoint.stub/action"
        headers = {"content-type": "text/xml"}

        mock_post.return_value = Response()
        mock_content.return_value = b"foobar"

        result = transport.post(url, data, headers)
        self.assertEqual("foobar", result.decode())
        mock_raise_for_status.assert_called_once_with()
        mock_post.assert_called_once_with(
            url, data=data, headers=headers, timeout=transport.timeout
        )
