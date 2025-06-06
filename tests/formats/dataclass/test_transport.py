from unittest import TestCase, mock

from requests import HTTPError, Response, Session

from xsdata.formats.dataclass.transports import DefaultTransport


class DefaultTransportTest(TestCase):
    @mock.patch.object(Response, "content", new_callable=mock.PropertyMock)
    @mock.patch.object(Response, "raise_for_status")
    @mock.patch.object(Session, "get")
    def test_get(self, mock_get, mock_raise_for_status, mock_content) -> None:
        transport = DefaultTransport()
        params = {"a": "b"}
        url = "http://endpoint.stub/action"
        headers = {"content-type": "text/xml"}

        response = Response()
        response.status_code = 200
        mock_get.return_value = response
        mock_content.return_value = b"foobar"

        result = transport.get(url, params, headers)
        self.assertEqual("foobar", result.decode())
        self.assertEqual(0, mock_raise_for_status.call_count)
        mock_get.assert_called_once_with(
            url, params=params, headers=headers, timeout=transport.timeout
        )

    @mock.patch.object(Response, "content", new_callable=mock.PropertyMock)
    @mock.patch.object(Response, "raise_for_status")
    @mock.patch.object(Session, "post")
    def test_post(self, mock_post, mock_raise_for_status, mock_content) -> None:
        transport = DefaultTransport(timeout=1.0)
        data = {"a": "b"}
        url = "http://endpoint.stub/action"
        headers = {"content-type": "text/xml"}

        response = Response()
        response.status_code = 500
        mock_post.return_value = response
        mock_content.return_value = b"foobar"

        result = transport.post(url, data, headers)
        self.assertEqual("foobar", result.decode())
        self.assertEqual(0, mock_raise_for_status.call_count)

        mock_post.assert_called_once_with(
            url, data=data, headers=headers, timeout=transport.timeout
        )

    @mock.patch.object(Response, "content", new_callable=mock.PropertyMock)
    def test_handle_response(self, mock_content) -> None:
        response = Response()
        response.status_code = 200
        mock_content.return_value = b"foobar"

        transport = DefaultTransport()
        self.assertEqual(b"foobar", transport.handle_response(response))

        response.status_code = 500
        self.assertEqual(b"foobar", transport.handle_response(response))

        response.status_code = 401
        response.reason = "Nope"
        response.url = "xsdata"
        with self.assertRaises(HTTPError) as cm:
            transport.handle_response(response)

        self.assertEqual("401 Client Error: Nope for url: xsdata", str(cm.exception))
