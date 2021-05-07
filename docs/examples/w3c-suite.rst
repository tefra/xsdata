====================
W3C XML Schema Suite
====================

xsdata is constantly tested and measured against the
`W3C XML Schema 1.1 test suite <https://github.com/w3c/xsdtests>`_.

The suite is quite extensible and consist of more than 14k valid tests cases for both
XML and JSON Binding.

.. hint::

    Because of the size and time it takes to run the test runner is on it's own
    `repo <https://github.com/tefra/xsdata-w3c-tests>`_.

    At least until I can manage to reduce the total run time which is about 8 minutes
    without coverage.

✨✨✨✨

.. hint::

    The `xmlschema <https://pypi.org/project/xmlschema/>`_ is used to validate xml
    output.

    The json mode performs roundtrip conversions and compares the initial and final
    outputs

    The xml mode is using the document instances instead of the schemas to generate
    the binding models.
