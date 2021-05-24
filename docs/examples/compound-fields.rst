===============
Compound Fields
===============

For repeating choice elements or complicated sequence elements you can use compound
fields in order to preserve the elements ordering during roundtrip conversions.


.. code-block:: console

    $ xsdata tests/fixtures/compound/schema.xsd --compound-fields --package tests.fixtures.compound.models --structure-style single-package

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/compound/schema.xsd
       :language: xml

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/compound/models.py
        :language: python
        :lines: 33-53


All choice elements are grouped into a single list field.

.. testcode::

    from pathlib import Path
    from tests.fixtures.compound.models import Root
    from tests import fixtures_dir
    from xsdata.formats.dataclass.parsers import XmlParser

    xml_path = fixtures_dir.joinpath("compound/sample.xml")
    parser = XmlParser()
    root = parser.from_path(xml_path, Root)
    print(root.alpha_or_bravo)

.. testoutput::

    [Alpha(a=True), Alpha(a=True), Bravo(b=True), Bravo(b=True), Alpha(a=True), Bravo(b=True), Alpha(a=True), Bravo(b=True)]
