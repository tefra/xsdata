====================
Dataclasses Features
====================

By default xsdata with generate
`dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ with the default
features on but you can use a :ref:`generator config <Generator Config>` to toggle
almost all of them.


.. literalinclude:: /../tests/fixtures/stripe/.xsdata.xml
   :language: xml
   :lines: 2-6


.. tab:: Frozen Model

    The code generator will use tuples instead of lists as well.

    .. literalinclude:: /../tests/fixtures/stripe/models/balance.py
       :language: python
       :lines: 93-127

.. tab:: Frozen Bindings

    .. testcode::

        import pprint
        from tests import fixtures_dir
        from tests.fixtures.stripe.models import Balance
        from xsdata.formats.dataclass.parsers import JsonParser

        xml_path = fixtures_dir.joinpath("stripe/samples/balance.json")
        parser = JsonParser()
        root = parser.from_path(xml_path, Balance)
        pprint.pprint(root.pending)

    .. testoutput::

        (Pending(amount=835408472, currency='usd', source_types=SourceTypes(bank_account=0, card=835408472)),
         Pending(amount=-22251, currency='eur', source_types=SourceTypes(bank_account=0, card=-22251)))
