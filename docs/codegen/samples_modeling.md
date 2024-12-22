# Samples Modeling

The code generator supports processing xml/json documents directly. That means even
without a schema you can easily create at the very least an initial draft of your models
just from samples. If you use a directory with multiple samples the transformer will
merge and flatten duplicate classes, fields and field types.

## XML Documents

```console
$ xsdata generate --package tests.fixtures.artists tests/fixtures/artists
```

=== "Sample #1"

    ```xml
    --8<-- "tests/fixtures/artists/art001.xml"
    ```

=== "Sample #2"

    ```xml
    --8<-- "tests/fixtures/artists/art002.xml"
    ```

=== "Sample #3"

    ```xml
    --8<-- "tests/fixtures/artists/art003.xml"
    ```

=== "Output"

    ```python
    --8<-- "tests/fixtures/artists/metadata.py"
    ```

## JSON Documents

```console
$ xsdata generate --package tests.fixtures.series tests/fixtures/series/samples
```

=== "Sample #1"

    ```json
    --8<-- "tests/fixtures/series/samples/show1.json"
    ```

=== "Sample #2"

    ```json
    --8<-- "tests/fixtures/series/samples/show2.json"
    ```

=== "Output"

    ```python
    --8<-- "tests/fixtures/series/series.py"
    ```
