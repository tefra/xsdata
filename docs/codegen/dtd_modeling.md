# DTD Modeling

The code generator supports processing **external** document type definitions (DTD),
with `lxml`.

```console
$ pip install xsdata[lxml]
```

!!! Warning "DTDParseError: error parsing DTD"

    Try removing the `DOCTYPE` wrapper if you are sure the rest of
    the definition is correct.

## Example

```console
$ xsdata --package tests.fixtures.dtd.models tests/fixtures/dtd/complete_example.dtd
```

=== "DTD Definition"

    ```dtd
    --8<-- "tests/fixtures/dtd/complete_example.dtd"
    ```

=== "Output"

    ```python
    --8<-- "tests/fixtures/dtd/models/complete_example.py"
    ```
