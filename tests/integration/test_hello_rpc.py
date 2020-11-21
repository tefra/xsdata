import os
from unittest import mock
from unittest import TestCase

import pytest
from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from tests.fixtures.hello import GetHelloAsStringResponse
from tests.fixtures.hello import HelloError
from tests.fixtures.hello import HelloGetHelloAsString
from tests.fixtures.hello import HelloGetHelloAsStringOutput
from xsdata.cli import cli
from xsdata.formats.dataclass.client import Client
from xsdata.formats.dataclass.client import Config
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.transports import DefaultTransport
from xsdata.utils.testing import load_class

os.chdir(root)


class HelloRpcServiceTests(TestCase):
    def test_wsdl_codegen(self):
        schema = fixtures_dir.joinpath("hello/hello.wsdl")
        package = "tests.fixtures.hello"
        runner = CliRunner()
        result = runner.invoke(cli, [str(schema), "--package", package, "--wsdl"])

        if result.exception:
            raise result.exception

        clazz = load_class(result.output, "HelloGetHelloAsStringOutput")
        self.assertEqual("Envelope", clazz.Meta.name)

    @mock.patch.object(DefaultTransport, "post")
    def test_client(self, mock_most):
        url = "http://localhost:9999/ws/hello"
        request = fixtures_dir.joinpath("hello/HelloRQ.xml").read_text()
        response = fixtures_dir.joinpath("hello/HelloRS.xml").read_bytes()
        headers = {"content-type": "text/xml"}
        mock_most.return_value = response

        config = Config.from_service(HelloGetHelloAsString)
        client = Client(config=config, serializer=XmlSerializer(pretty_print=True))
        result = client.send({"body": {"get_hello_as_string": {"arg0": "chris"}}})

        self.assertIsInstance(result, HelloGetHelloAsString.output)

        body = HelloGetHelloAsStringOutput.Body(
            get_hello_as_string_response=GetHelloAsStringResponse(
                return_value="Hello chris"
            )
        )
        self.assertEqual(body, result.body)

        mock_most.assert_called_once_with(url, data=request, headers=headers)

    @mock.patch.object(DefaultTransport, "post")
    def test_client_with_soap_fault(self, mock_most):
        url = "http://localhost:9999/ws/hello"
        request = fixtures_dir.joinpath("hello/HelloRQ.xml").read_text()
        response = fixtures_dir.joinpath("hello/HelloRS_SoapFault.xml").read_bytes()
        headers = {"content-type": "text/xml"}
        mock_most.return_value = response

        config = Config.from_service(HelloGetHelloAsString)
        client = Client(config=config, serializer=XmlSerializer(pretty_print=True))
        result = client.send({"body": {"get_hello_as_string": {"arg0": "chris"}}})

        self.assertIsInstance(result, HelloGetHelloAsString.output)

        fault = HelloGetHelloAsStringOutput.Body.Fault(
            faultcode="S:Server",
            faultstring="foobar",
            detail=HelloGetHelloAsStringOutput.Body.Fault.Detail(
                hello_error=HelloError(message="foobar")
            ),
        )
        self.assertEqual(fault, result.body.fault)

        mock_most.assert_called_once_with(url, data=request, headers=headers)

    @pytest.mark.skip
    def test_live(self):
        config = Config.from_service(HelloGetHelloAsString)
        client = Client(config=config, serializer=XmlSerializer(pretty_print=True))
        result = client.send({"body": {"get_hello_as_string": {"arg0": "chris"}}})
        print(result)
