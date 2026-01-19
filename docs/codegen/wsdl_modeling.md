# WSDL Modeling

The implementation is experimental and currently only **WSDL 1.1 and SOAP 1.1** bindings
have been implemented.

In addition to models derived from XML schemas, the code generator also generates
dataclasses for messages and simple classes to describe the unique operations.

Make sure you install both the CLI and SOAP requirements.

```console
$ pip install xsdata[cli,soap]
```

```console
$ xsdata generate --package calculator http://www.dneonline.com/calculator.asmx?WSDL
```

## Message Model

The message models are no different from XSD-derived classes and include the complete
structure of the `Envelope` wrapper.

```python show_lines="148:169"
--8<-- "tests/fixtures/calculator/services.py"
```

## Operation Class

The [DefinitionsMapper][xsdata.codegen.mappers.DefinitionsMapper] will generate simple
static classes to describe all the unique operations and the binding procedure.

```python show_lines="488:494"
--8<-- "tests/fixtures/calculator/services.py"
```

## Client

The [Client][xsdata.formats.dataclass.client.Client] is a proxy for consuming web
services. The client needs a web service
[Config][xsdata.formats.dataclass.client.Config] with the directives to process requests
and responses.

**You can also optionally provide and override:**

- A [Transport][xsdata.formats.dataclass.transports.Transport] implementation
- An [XmlParser][xsdata.formats.dataclass.parsers.XmlParser] instance
- An [XmlSerializer][xsdata.formats.dataclass.serializers.XmlSerializer] instance

### Creating instances

The client can be initialized from the operation class directly:

```python
>>> from xsdata.formats.dataclass.client import Client
>>> from tests.fixtures.calculator import CalculatorSoapAdd
>>> client = Client.from_service(CalculatorSoapAdd)
>>> client.config
Config(style='document', location='http://www.dneonline.com/calculator.asmx', transport='http://schemas.xmlsoap.org/soap/http', soap_action='http://tempuri.org/Add', input=<class 'tests.fixtures.calculator.services.CalculatorSoapAddInput'>, output=<class 'tests.fixtures.calculator.services.CalculatorSoapAddOutput'>, encoding=None)

```

You can also override any properties as needed:

```python
>>> client = Client.from_service(CalculatorSoapAdd, location="http://testurl.com")
>>> client.config
Config(style='document', location='http://testurl.com', transport='http://schemas.xmlsoap.org/soap/http', soap_action='http://tempuri.org/Add', input=<class 'tests.fixtures.calculator.services.CalculatorSoapAddInput'>, output=<class 'tests.fixtures.calculator.services.CalculatorSoapAddOutput'>, encoding=None)

```

Or you can configure the client manually:

```python
config = Config(
    style="document",
    location="",
    transport=TransportTypes.SOAP,
    soap_action="",
    input=None,
    output=None,
)
client = Client(config=config)
```

### Override transport

Initialize the transport with a custom requests session instance:

```python
from requests import Session

transport = DefaultTransport(session=Session())
client = Client(config=config, transport=transport)
```

### Performing Requests

The send method requires either an object that matches the config input type or a
dictionary with raw values that matches the input dataclass field names and structure.

```python
request = CalculatorSoapAddInput(body=CalculatorSoapAddInput.Body(add=Add(10, 2)))
client.send(request)
# CalculatorSoapAddOutput(body=CalculatorSoapAddOutput.Body(add_response=AddResponse(add_result=12)))
```

```python
client = Client.from_service(CalculatorSoapAdd)
params = {"body": {"add": {"int_a": 3, "int_b": 4}}}
client.send(params)
# CalculatorSoapAddOutput(body=CalculatorSoapAddOutput.Body(add_response=AddResponse(add_result=7)))
```

You can also provide a dictionary of custom headers, although headers required for the
web service to function cannot be overwritten:

```python
client.send(params, headers={"User-Agent": "xsdata"})
```

You need to specify an encoding if you intend to send non-ASCII characters:

```python
client = Client.from_service(encoding="utf-8")
```
