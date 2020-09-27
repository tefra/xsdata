import os
from unittest import mock
from unittest import TestCase

from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from tests.fixtures.calculator import CalculatorSoapAdd
from tests.fixtures.calculator import CalculatorSoapAddOutput
from xsdata.cli import cli
from xsdata.formats.dataclass.client import Client
from xsdata.formats.dataclass.client import Config
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.transports import DefaultTransport
from xsdata.utils.testing import load_class

os.chdir(root)


class CalculatorServiceTests(TestCase):
    def test_wsdl_codegen(self):
        schema = fixtures_dir.joinpath("calculator/services.wsdl")
        package = "tests.fixtures.calculator"
        runner = CliRunner()
        result = runner.invoke(cli, [str(schema), "--package", package, "--wsdl"])

        if result.exception:
            raise result.exception

        clazz = load_class(result.output, "CalculatorSoapMultiplyOutput")
        self.assertEqual("Envelope", clazz.Meta.name)

    @mock.patch.object(DefaultTransport, "post")
    def test_client(self, mock_most):
        url = "http://www.dneonline.com/calculator.asmx"
        request = fixtures_dir.joinpath("calculator/AddRQ.xml").read_text()
        response = fixtures_dir.joinpath("calculator/AddRS.xml").read_bytes()
        headers = {"content-type": "text/xml", "SOAPAction": "http://tempuri.org/Add"}
        mock_most.return_value = response

        config = Config.from_service(CalculatorSoapAdd)
        client = Client(config=config, serializer=XmlSerializer(pretty_print=True))
        result = client.send({"body": {"add": {"int_a": 1, "int_b": 3}}})

        self.assertIsInstance(result, CalculatorSoapAddOutput)

        mock_most.assert_called_once_with(url, data=request, headers=headers)
