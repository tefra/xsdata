import os
from unittest import TestCase, mock

from click.testing import CliRunner

from tests import fixtures_dir, root
from tests.fixtures.calculator import CalculatorSoapAdd, CalculatorSoapAddOutput
from xsdata.cli import cli
from xsdata.formats.dataclass.client import Client, Config
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.transports import DefaultTransport
from xsdata.utils.testing import load_class

os.chdir(root)


class CalculatorServiceTests(TestCase):
    def test_wsdl_codegen(self) -> None:
        schema = fixtures_dir.joinpath("calculator/services.wsdl")
        package = "tests.fixtures.calculator"
        runner = CliRunner()
        result = runner.invoke(cli, ["generate", str(schema), "--package", package])

        if result.exception:
            raise result.exception

        clazz = load_class(result.output, "CalculatorSoapMultiplyOutput")
        self.assertEqual("Envelope", clazz.Meta.name)

    @mock.patch.object(DefaultTransport, "post")
    def test_client(self, mock_most) -> None:
        url = "http://www.dneonline.com/calculator.asmx"
        request = fixtures_dir.joinpath("calculator/AddRQ.xml").read_text()
        response = fixtures_dir.joinpath("calculator/AddRS.xml").read_bytes()
        headers = {"content-type": "text/xml", "SOAPAction": "http://tempuri.org/Add"}
        mock_most.return_value = response

        config = Config.from_service(CalculatorSoapAdd)
        serializer = XmlSerializer(config=SerializerConfig(indent="  "))
        client = Client(config=config, serializer=serializer)
        result = client.send({"Body": {"Add": {"intA": 1, "intB": 3}}})

        self.assertIsInstance(result, CalculatorSoapAddOutput)

        mock_most.assert_called_once_with(url, data=request, headers=headers)
