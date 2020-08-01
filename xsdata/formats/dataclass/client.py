from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import Optional
from typing import Type

from xsdata.exceptions import ClientValueError
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.json import DictConverter
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.transports import DefaultTransport
from xsdata.formats.dataclass.transports import Transport


@dataclass(frozen=True)
class Config:
    """
    Service configuration class.

    :param style: binding style
    :param location: service endpoint url
    :param transport: transport namespace
    :param soap_action: soap action
    :param input: input object type
    :param output: output object type
    """

    style: str
    location: str
    transport: str
    soap_action: str
    input: Type
    output: Type

    @classmethod
    def from_service(cls, obj: Any, **kwargs: Any) -> "Config":
        """Instantiate from a generated service class."""

        keys = ["style", "location", "transport", "soap_action", "input", "output"]
        return cls(**{key: kwargs.get(key) or getattr(obj, key, None) for key in keys})


class TransportTypes:
    SOAP = "http://schemas.xmlsoap.org/soap/http"


@dataclass
class Client:
    """
    :param config: service configuration
    :param transport: transport instance to handle requests
    :param parser: xml parser instance to handle xml response parsing
    :param serializer: xml serializer instance to handle xml response parsing
    """

    config: Config
    transport: Transport = field(default_factory=DefaultTransport)
    parser: XmlParser = field(default_factory=XmlParser)
    serializer: XmlSerializer = field(default_factory=XmlSerializer)
    dict_converter: DictConverter = field(init=False, default_factory=DictConverter)

    @classmethod
    def from_service(cls, obj: Type, **kwargs: str) -> "Client":
        """Instantiate client from a service definition."""
        return cls(config=Config.from_service(obj, **kwargs))

    def send(self, obj: Any, headers: Optional[Dict] = None) -> Any:
        """
        Send a request and parse the response according to the service
        configuration.

        The input object can be a dictionary, or the input type instance directly

        >>> params = {"body": {"add": {"int_a": 3, "int_b": 4}}}
        >>> res = client.send(params)

        Is equivalent with:

        >>> req = CalculatorSoapAddInput(
        >>> body=CalculatorSoapAddInput.Body(add=Add(3, 4)))
        >>> res = client.send(req)

        :param obj: a params dictionary or the input type instance
        :param headers: a dictionary of any additional headers.
        """
        data = self.prepare_payload(obj)
        headers = self.prepare_headers(headers or {})
        response = self.transport.post(self.config.location, data=data, headers=headers)
        return self.parser.from_bytes(response, self.config.output)

    def prepare_headers(self, headers: Dict) -> Dict:
        """
        Prepare request headers according to the service configuration.

        Don't mutate input headers dictionary.

        :raises ClientValueError: If the service transport type is unsupported.
        """
        result = headers.copy()
        if self.config.transport == TransportTypes.SOAP:
            result["content-type"] = "text/xml"
            if self.config.soap_action:
                result["SOAPAction"] = self.config.soap_action
        else:
            raise ClientValueError(
                f"Unsupported binding transport: `{self.config.transport}`"
            )

        return result

    def prepare_payload(self, obj: Any) -> Any:
        """
        Prepare and serialize payload to be sent.

        :raises ClientValueError: If the config input type doesn't match the given
            input.
        """
        if isinstance(obj, Dict):
            obj = self.dict_converter.convert(obj, self.config.input)

        if not isinstance(obj, self.config.input):
            raise ClientValueError(
                f"Invalid input service type, "
                f"expected `{self.config.input.__name__}` "
                f"got `{type(obj).__name__}`"
            )

        return self.serializer.render(obj)
