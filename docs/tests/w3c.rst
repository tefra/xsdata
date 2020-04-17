W3C XML Schema Suite
====================

xsdata is constantly tested and measured against the `W3C XML Schema 1.1 test suite <https://github.com/w3c/xsdtests>`_.

The suite is quite extensible and consist of more than 26k tests cases for both XML Schema 1.0 and 1.1.

.. hint::

    Because of the size and time it takes to run the test runner is on it's own `repo <https://github.com/tefra/xsdata-w3c-tests>`_.

    At least until I can manage to reduce the total run time which is about 9 minutes without coverage.


Report
------
**60** failed, **26102** passed, **162** skipped @ `travis-ci <https://travis-ci.com/tefra/xsdata-w3c-tests>`_

✨✨✨✨

Methodology
-----------

For all XML Schema definitions we use the `xmlschema <https://pypi.org/project/xmlschema/>`_ to validate results.

The definitions that failed to be parsed by are automatically skipped.

The known invalid schemas are also skipped alongside the test cases that come without any xml instance tests.

.. hint::

    xsdata is an xml binding library not a schema validator.

**Steps**

- Generate dataclasses for given schema.
- **Fail** when cli raises exception or expected module::class is not found.
- Parse the given xml instance.
- **Fail** when parser raises exception and xml instance is valid.
- Serialize to xml and validate against the schema.
- **Fail** if xml instance is valid and final output is invalid.

**Test runner info**

- Generate tests instead of using pytest parametrizing.
- Use pytest cache to generate the xfail decorators for ci.
- Cache code generation runs.
- Cache xml validator instances.
- Output directory remains after each build.


**Try it out**

.. code-block:: console

    git clone git@github.com:tefra/xsdata-w3c-tests.git
    cd xsdata-w3c-tests
    pip install -r requirements.txt
    pytest -n 4 --tb short tests/  # | tee pytest.log
