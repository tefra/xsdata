*******************
WSDL (Experimental)
*******************

The implementation is experimental and currently only **WSDL 1.1 and SOAP 1.1** bindings
have been implemented.

The code generator in addition to models derived from xml schemas will also generate
dataclasses for messages and simple classes to describe the unique operations.


Make sure you install both cli and soap requirements.

.. code-block:: console

    $ pip install xsdata[cli,soap]

.. code-block:: console

    $ xsdata --package calculator http://www.dneonline.com/calculator.asmx?WSDL


Message Model
=============

The message models are not any different to xsd derived classes and include the complete
structure of the ``Envelope`` wrapper.

.. literalinclude:: /../tests/fixtures/calculator/services.py
   :language: python
   :lines: 159-182


Operation Class
===============

The :class:`~xsdata.codegen.mappers.definitions.DefinitionsMapper` will generate
simple static classes to describe all the unique operations and the binding procedure.


.. literalinclude:: /../tests/fixtures/calculator/services.py
   :language: python
   :lines: 519-525


Client
======

The :class:`~xsdata.formats.dataclass.client.Client` is a proxy for consuming web
services. The client needs a web service
:class:`~xsdata.formats.dataclass.client.Config` with the directives to process
requests and responses.

**Optionally you can also provide and override**

- the default transport implementation
  :class:`~xsdata.formats.dataclass.transports.Transport`
- the :class:`~xsdata.formats.dataclass.parsers.XmlParser` with your custom config
- the :class:`~xsdata.formats.dataclass.serializers.XmlSerializer` with your custom
  config


Creating instances
------------------

The client can be initialized from the an operation class directly

.. code-block::

    client = Client.from_service(CalculatorSoapAdd)
    client.config
    # Config(style='document', location='http://www.dneonline.com/calculator.asmx', transport='http://schemas.xmlsoap.org/soap/http', soap_action='http://tempuri.org/Add', input=<class 'tests.fixtures.calculator.services.CalculatorSoapAddInput'>, output=<class 'tests.fixtures.calculator.services.CalculatorSoapAddOutput'>, encoding=None)

But you can also override any properties as you see fit

.. code-block::

    client = Client.from_service(CalculatorSoapAdd, location="http://testurl.com")
    client.config
    # Config(style='document', location='http://testurl.com', transport='http://schemas.xmlsoap.org/soap/http', soap_action='http://tempuri.org/Add', input=<class 'tests.fixtures.calculator.services.CalculatorSoapAddInput'>, output=<class 'tests.fixtures.calculator.services.CalculatorSoapAddOutput'>)


Or if you know what you are doing

.. code-block::

    config = Config(
        style="document",
        location="",
        transport=TransportTypes.SOAP,
        soap_action="",
        input=None,
        output=None,
    )
    client = Client(config=config)


Initialize a transport with a custom requests session instance.

.. code-block::

    from requests import Session

    transport = DefaultTransport(session=Session())
    client = Client(config=config, transport=transport)


Performing Requests
-------------------

The send method requires either an object that matches the config input type or a
dictionary with raw values that matches the input dataclass field names and structure.

.. code-block::

    request = CalculatorSoapAddInput(body=CalculatorSoapAddInput.Body(add=Add(10, 2)))
    client.send(request)
    # CalculatorSoapAddOutput(body=CalculatorSoapAddOutput.Body(add_response=AddResponse(add_result=12)))


.. code-block::

    client = Client.from_service(CalculatorSoapAdd)
    params = {"body": {"add": {"int_a": 3, "int_b": 4}}}
    client.send(params)
    # CalculatorSoapAddOutput(body=CalculatorSoapAddOutput.Body(add_response=AddResponse(add_result=7)))


You can also provide a dictionary of custom headers as well, although the headers that
are needed for the webservice to work can not be overwritten.,

.. code-block::

    client.send(params, headers={"User-Agent": "xsdata"})


You will need to encode the payload if you intend to send non-ascii characters.

.. code-block::

    client = Client.from_service(encoding="utf-8")
