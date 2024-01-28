from dataclasses import dataclass, field
from typing import Any, Dict, NamedTuple, Optional, Type, Union

from xsdata.exceptions import ClientValueError
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.json import DictConverter
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.transports import DefaultTransport, Transport


class Config(NamedTuple):
    """Service configuration class.

    Args:
        style: The binding style
        location: The service endpoint url
        transport: The transport namespace
        soap_action: The soap action
        input: The input class
        output: The output class
    """

    style: str
    location: str
    transport: str
    soap_action: str
    input: Type
    output: Type
    encoding: Optional[str] = None

    @classmethod
    def from_service(cls, obj: Any, **kwargs: Any) -> "Config":
        """Instantiate from a generated service class.

        Args:
            obj: The service class
            **kwargs: Override the service class properties
                style: The binding style
                location: The service endpoint url
                transport: The transport namespace
                soap_action: The soap action
                input: The input class
                output: The output class

        Returns:
            A new config instance.
        """
        params = {
            key: kwargs[key] if key in kwargs else getattr(obj, key, None)
            for key in cls._fields
        }

        return cls(**params)


class TransportTypes:
    """Transport types."""

    SOAP = "http://schemas.xmlsoap.org/soap/http"


@dataclass
class Client:
    """A wsdl client.

    Args:
        config: The service config instance
        transport: The transport instance
        parser: The xml parser instance
        serializer: The xml serializer instance
    """

    config: Config
    transport: Transport = field(default_factory=DefaultTransport)
    parser: XmlParser = field(default_factory=XmlParser)
    serializer: XmlSerializer = field(default_factory=XmlSerializer)
    dict_converter: DictConverter = field(init=False, default_factory=DictConverter)

    @classmethod
    def from_service(cls, obj: Type, **kwargs: Any) -> "Client":
        """Instantiate client from a service class.

        Args:
            obj: The service class
            **kwargs: Override the service class properties
                style: The binding style
                location: The service endpoint url
                transport: The transport namespace
                soap_action: The soap action
                input: The input class
                output: The output class

        Returns:
            A new client instance.
        """
        return cls(config=Config.from_service(obj, **kwargs))

    def send(self, obj: Any, headers: Optional[Dict] = None) -> Any:
        """Build and send a request for the input object.

        >>> params = {"body": {"add": {"int_a": 3, "int_b": 4}}}
        >>> res = client.send(params)

        Is equivalent with:

        >>> req = CalculatorSoapAddInput(
        >>> body=CalculatorSoapAddInput.Body(add=Add(3, 4)))
        >>> res = client.send(req)

        Args:
            obj: The request model instance or a pure dictionary
            headers: Additional headers to pass to the transport

        Returns:
            The response model instance.
        """
        data = self.prepare_payload(obj)
        headers = self.prepare_headers(headers or {})
        response = self.transport.post(self.config.location, data=data, headers=headers)
        return self.parser.from_bytes(response, self.config.output)

    def prepare_headers(self, headers: Dict) -> Dict:
        """Prepare the request headers.

        It merges the custom user headers with the necessary headers
        to accommodate the service class configuration.

        Raises:
            ClientValueError: If the service transport type is not supported.
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

    def prepare_payload(self, obj: Any) -> Union[str, bytes]:
        """Prepare and serialize the payload to be sent.

        If the obj is a pure dictionary, it will be converted
        first to a request model instance.

        Args:
            obj: The request model instance or a pure dictionary

        Returns:
            The serialized request body content as string or bytes.

        Raises:
            ClientValueError: If the config input type doesn't match the given object.
        """
        if isinstance(obj, Dict):
            obj = self.dict_converter.convert(obj, self.config.input)

        if not isinstance(obj, self.config.input):
            raise ClientValueError(
                f"Invalid input service type, "
                f"expected `{self.config.input.__name__}` "
                f"got `{type(obj).__name__}`"
            )

        result = self.serializer.render(obj)
        if self.config.encoding:
            return result.encode(self.config.encoding)

        return result
