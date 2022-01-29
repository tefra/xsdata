Why non-nullable fields are marked as optional?
===============================================

We rely on the fields ordering for all binding procedures and due to the following
limitation we have to mark even required fields as optional.

..

    TypeError will be raised if a field without a default value follows a field
    with a default value. This is true whether this occurs in a single class, or as
    a result of class inheritance.

    Source: :mod:`python:dataclasses`

In Python 3.10 dataclasses introduced a new directive `kw_only` that resolves the above
limitation and xsdata handling. Read :ref:`more <Dataclasses Features>`

If you can't update just yet please check the `attrs <https://pypi.org/project/xsdata-attrs/>`_ plugin!
