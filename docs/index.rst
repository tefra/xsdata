.. include:: ../README.rst
    :start-line: 3

.. admonition:: Why naive?

    The W3C XML Schema is too complicated but with good reason. It needs to support any
    api design. On the other hand when you consume xml you don't necessarily care about
    any of that. This is where xsData comes in, to simplify things by making a lot of
    assumptions like the following one that started everything:


        All xs:schema elements are classes everything else is either noise or class
        properties


.. toctree::
    :glob:
    :maxdepth: 1

    installation
    codegen
    models
    xml
    json
    wsdl
    examples
    data-types
    api
    faq
    changelog

.. toctree::
    :caption: Links

    PyPI <https://pypi.org/project/xsdata/>
    Conda <https://anaconda.org/conda-forge/xsdata>
    Github <https://github.com/tefra/xsdata>


.. meta::
   :google-site-verification: VSyrlSSIOrwnZhhAo3dS6hf1efs-8FxF3KezQ-bH_js
