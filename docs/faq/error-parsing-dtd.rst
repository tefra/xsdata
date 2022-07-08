DTDParseError: error parsing DTD
================================

xsdata works only with **external** document type definitions
and relies on `lxml <https://lxml.de/>`_ exclusively to parse
the dtd tree.

Try to remove the `DOCTYPE` wrapper if you are sure the rest of
the definition is correct.
