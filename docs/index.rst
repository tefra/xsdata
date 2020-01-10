.. include:: ../README.rst

.. admonition:: Why naive?

    The W3C XML Schema offers so much flexibility and abstraction layers and grammatical rules to support practically any xml document definition.

    Itergration teams and clients don't care about any of that, take out abstraction and flexibility and you are left with lean named data structures with typed attributes and a namespace for humans to read!

Roadmap
-------

* Add option to split classes in multiple files
* Python renderers: attrs and pydantic
* Java renderer: JaxB compatible models :)
* Validators

.. toctree::
    :maxdepth: 2
    :caption: Contents

    installation
    codegen
    architecture
    formats
    tests
    changelog
    about
    api
