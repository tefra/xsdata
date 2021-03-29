===============
Compound Fields
===============

For repeating choice elements or complicated sequence elements you can use compound
fields in order to preserve the elements ordering during roundtrip conversions.


.. code-block:: console

    $ xsdata tests/fixtures/defxmlschema/chapter12.xsd  --compound-fields --package tests.fixtures.defxmlschema

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter12.xsd
       :language: xml
       :lines: 22-35

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter12.py
        :language: python
        :emphasize-lines: 19
        :lines: 44-98


All choice elements are grouped into a single list field.

.. testcode::

    from pathlib import Path
    from tests.fixtures.defxmlschema.chapter12 import Items
    from tests import fixtures_dir
    from xsdata.formats.dataclass.parsers import XmlParser

    xml_string = fixtures_dir.joinpath("defxmlschema/chapter12.xml").read_text()
    parser = XmlParser()
    items = parser.from_string(xml_string, Items)
    print(items.shirt_or_hat_or_umbrella[0].size_or_color_or_description)

.. testoutput::

    [SizeType(value=10, system='US-DRESS'), ColorType(value='blue'), DescriptionType(w3_org_1999_xhtml_element=['\n      This shirt is the ', AnyElement(qname='{http://www.w3.org/1999/xhtml}b', text='best-selling', tail=' shirt in\n      our catalog! ', children=[], attributes={}), AnyElement(qname='{http://www.w3.org/1999/xhtml}br', text='', tail=' Note: runs large.\n    ', children=[], attributes={})])]