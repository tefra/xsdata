# Docstring styles

xsdata relies on [docformatter](https://pypi.org/project/docformatter/) to follow the
[PEP 257](https://www.python.org/dev/peps/pep-0257/) -- docstring conventions and offers
the ability to switch between the most popular styles or disable them completely.

=== "reStructuredText"

    ```python show_lines="37:"
    --8<-- "tests/fixtures/docstrings/rst/schema.py"
    ```

=== "NumPy"

    ```python show_lines="41:"
    --8<-- "tests/fixtures/docstrings/numpy/schema.py"
    ```

=== "Google"

    ```python show_lines="39:"
    --8<-- "tests/fixtures/docstrings/google/schema.py"
    ```

=== "Accessible"

    ```python show_lines="39:"
    --8<-- "tests/fixtures/docstrings/accessible/schema.py"
    ```

=== "Blank"

    ```python show_lines="23:"
    --8<-- "tests/fixtures/docstrings/blank/schema.py"
    ```
