from dataclasses import asdict
from dataclasses import replace
from unittest import mock
from unittest import TestCase

from tests.fixtures.calculator import Add
from tests.fixtures.calculator import CalculatorSoapAdd
from tests.fixtures.calculator import CalculatorSoapAddInput
from tests.fixtures.calculator import CalculatorSoapAddOutput
from xsdata.exceptions import ClientValueError
from xsdata.formats.dataclass.client import Client
from xsdata.formats.dataclass.client import Config
from xsdata.formats.dataclass.client import TransportTypes
from xsdata.formats.dataclass.transports import DefaultTransport

response = """
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <AddResponse xmlns="http://tempuri.org/">
            <AddResult>7</AddResult>
        </AddResponse>
    </soap:Body>
</soap:Envelope>"""


class ClientTests(TestCase):
    def test_from_service(self):
        client = Client.from_service(CalculatorSoapAdd, location="http://testurl.com")

        actual = asdict(client.config)
        expected = {
            "style": "document",
            "input": CalculatorSoapAddInput,
            "location": "http://testurl.com",
            "soap_action": "http://tempuri.org/Add",
            "output": CalculatorSoapAddOutput,
            "transport": "http://schemas.xmlsoap.org/soap/http",
        }

        self.assertEqual(expected, actual)

    @mock.patch.object(DefaultTransport, "post")
    def test_send_with_dict_params(self, mock_post):
        mock_post.return_value = response.encode()

        client = Client.from_service(CalculatorSoapAdd)
        params = {"body": {"add": {"int_a": 3, "int_b": 4}}}

        result = client.send(params, headers={"User-Agent": "xsdata"})

        self.assertIsInstance(result, CalculatorSoapAddOutput)
        self.assertEqual(7, result.body.add_response.add_result)

        obj = CalculatorSoapAddInput(body=CalculatorSoapAddInput.Body(add=Add(3, 4)))
        request = client.serializer.render(obj)

        mock_post.assert_called_once_with(
            "http://www.dneonline.com/calculator.asmx",
            data=request,
            headers={
                "User-Agent": "xsdata",
                "content-type": "text/xml",
                "SOAPAction": "http://tempuri.org/Add",
            },
        )

    @mock.patch.object(DefaultTransport, "post")
    def test_send_with_instance_object(self, mock_post):
        mock_post.return_value = response.encode()

        client = Client.from_service(CalculatorSoapAdd)
        obj = CalculatorSoapAddInput(body=CalculatorSoapAddInput.Body(add=Add(3, 4)))
        result = client.send(obj)

        self.assertIsInstance(result, CalculatorSoapAddOutput)
        self.assertEqual(7, result.body.add_response.add_result)

        request = client.serializer.render(obj)

        mock_post.assert_called_once_with(
            "http://www.dneonline.com/calculator.asmx",
            data=request,
            headers={
                "content-type": "text/xml",
                "SOAPAction": "http://tempuri.org/Add",
            },
        )

    def test_prepare_payload_raises_error_with_type_mismatch(self):
        client = Client.from_service(CalculatorSoapAdd)

        with self.assertRaises(ClientValueError) as cm:
            client.prepare_payload(CalculatorSoapAddOutput())

        self.assertEqual(
            "Invalid input service type, expected "
            "`CalculatorSoapAddInput` got `CalculatorSoapAddOutput`",
            str(cm.exception),
        )

    def test_prepare_headers(self):
        config = Config(
            style="document",
            location="",
            transport=TransportTypes.SOAP,
            soap_action="",
            input=None,
            output=None,
        )
        client = Client(config=config)

        headers = {"foo": "bar"}
        result = client.prepare_headers(headers)
        self.assertEqual({"content-type": "text/xml", "foo": "bar"}, result)
        self.assertEqual(1, len(headers))

        config = replace(config, soap_action="add")
        client = Client(config=config)
        result = client.prepare_headers({})
        self.assertEqual({"SOAPAction": "add", "content-type": "text/xml"}, result)

    def test_prepare_headers_raises_error_with_unsupported_binding_transport(self):
        config = Config.from_service(CalculatorSoapAdd, transport="foobar")
        client = Client(config=config)

        with self.assertRaises(ClientValueError) as cm:
            client.prepare_headers({})

        self.assertEqual("Unsupported binding transport: `foobar`", str(cm.exception))
