W3C XML Schema Suite
====================

xsdata is constantly tested and measured against the `W3C XML Schema 1.1 test suite <https://github.com/w3c/xsdtests>`_.

The suite is quite extensible and consist of more than 26k tests cases for both XML Schema 1.0 and 1.1.

.. hint::

    Because of the size and time it takes to run the test runner is on it's own `repo <https://github.com/tefra/xsdata-w3c-tests>`_.

    At least until I can manage to reduce the total run time which is about 9 minutes without coverage.


Report
------

**55** failed, **14517** passed, **103** skipped @ `travis-ci <https://travis-ci.com/tefra/xsdata-w3c-tests>`_

✨✨✨✨

Methodology
-----------

- Invalid schema tests or no schema tests are ignored (~12k tests)
- Generate dataclasses for given schema.
  - **Fail** when cli raises exception or expected module::class is not found.
- Parse the given xml instance.
  - **Fail** when parser raises exception.
- Serialize to xml and validate against the schema.
  - **Fail** if final output is invalid.
  - **Skip** if original instance or schema also fail validation.


For all XML Schema definitions we use the `xmlschema <https://pypi.org/project/xmlschema/>`_ to validate results.


.. hint::

    xsdata is an xml binding library not a schema validator.


**Try it out**

.. code-block:: console

    git clone git@github.com:tefra/xsdata-w3c-tests.git
    cd xsdata-w3c-tests
    pip install -r requirements.txt
    pytest -n 4 --tb short tests/  # | tee pytest.log
