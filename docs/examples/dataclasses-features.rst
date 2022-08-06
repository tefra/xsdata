====================
Dataclasses Features
====================

The code generator uses the default :mod:`python:dataclasses` options but you can
toggle all of them through the cli flags or a :ref:`generator config <Generator Config>`


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
        print(root.pending[0])
        print(root.pending[1])

    .. testoutput::

        Pending(amount=835408472, currency='usd', source_types=SourceTypes(bank_account=0, card=835408472))
        Pending(amount=-22251, currency='eur', source_types=SourceTypes(bank_account=0, card=-22251))
