# Configuration

The command line tool includes most but not all available options. The most advanced
settings can be enabled through a project configuration file.

## Create or Update

You can create a default one with the command:

```console exec="1" source="console"
$ xsdata init-config --help
```

**Output:** `.xsdata.xml `

```python exec="true" result="xml"
from io import StringIO
from xsdata.models.config import GeneratorConfig

config = GeneratorConfig.create()
output = StringIO()
config.write(output, config)
print(output.getvalue())
```

**Usage**

```console
$ xsdata --config project/.xsdata.xml
```

!!! Info "CLI options override the project configuration settings."

## Output Settings

Configuration settings related to output generation.

### `maxLineLength`

The maximum line length of the generated code.

**Default Value:** `79`

**CLI Option:** `-mll, --max-line-length INTEGER`

### `subscriptableTypes`

Use [PEP-585](https://peps.python.org/pep-0585/) type hinting generics in standard
collections.

```
tuple # typing.Tuple
list # typing.List
dict # typing.Dict
set # typing.Set
type # typing.Type
```

**Default Value:** `False`

**CLI Option:** `--subscriptable-types / --no-subscriptable-types`

**Requirements:** `python>=3.9`

### `unionType`

Use [PEP-604](https://peps.python.org/pep-0585/), allow writing union types as X | Y.

```
str | None # Optional[str]
str | int # Union[str, int]
```

**Default Value:** `False`

**CLI Option:** `--union-type / --no-union-type`

**Requirements:** `python>=3.10`

### Package

The output package for the generated code, e.g. `code.models`

**Default Value:** `generated`

**CLI Option:** `-p, --package TEXT`

### Format

The output format for the generated code, e.g. `code.models`

**Default Value:** `dataclasses`

**CLI Option:** `-o, --output TEXT`

**Attributes**

The [dataclass][dataclasses.dataclass] parameters.

- `repr`: Generate the [**repr**][object.__repr__] method.
- `eq`: Generate the [**eq**][object.__eq__] method.
- `order`: Generates the [**lt**][object.__lt__], [**le**][object.__le__],
  [**gt**][object.__gt__], [**ge**][object.__ge__] methods.
- `frozen`: This emulates read-only frozen instances.
- `unsafeHash`: Generates a [**hash**][object.__hash__] method according to how `eq` and
  `frozen` are set.
- `slots`: Generates the class [**slots**][object.__slots__] attribute. `python >= 3.10`
- `kwOnly`: All fields will be marked as keyword-only. `python >= 3.10`

!!! Warning

    A TypeError is raised if a field without a default value follows a field with a default value.
    This is true whether this occurs in a single class, or as a result of class inheritance. If
    this option is not enabled, the generator will mark all required fields without default values
    as optional with.

### Structure

The file structure style to create.

| Style                | Description                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `filenames`          | Group classes by the resource file location.                                                                              |
| `namespaces`         | Group classes by the target namespace.                                                                                    |
| `clusters`           | Group classes by strongly connected dependencies. The closest thing to one-class-per-package, safe from circular imports. |
| `single-package`     | Group classes in a single package. Safe from circular imports, but can create some huge files.                            |
| `namespace-clusters` | Group classes by strongly connected dependencies and target namespaces.                                                   |

**Default Value:** `filenames`

**CLI Option:**
`-ss, --structure-style [filenames|namespaces|clusters|single-package|namespace-clusters]`

### DocstringStyle

The style of docstrings to create.

**Default Value:** `reStructuredText`

**CLI Option:**
`-ds, --docstring-style [reStructuredText|NumPy|Google|Accessible|Blank]`

### FilterStrategy

When the class analyzer runs, a lot of types, base classes are flattened, leaving a lot
of orphan classes. The filter strategy can be used to remove unused classes.

| Style             | Description                                                                 |
| ----------------- | --------------------------------------------------------------------------- |
| `all`             | Generate all simple and complex types.                                      |
| `allGlobals`      | Generate global elements and complex types and all referenced simple types. |
| `referredGlobals` | Generate global elements and all referenced simple and complex types.       |

**Default Value:** `allGlobals`

**CLI Option:** `-fs, --filter-strategy [all|allGlobals|referredGlobals]`

### RelativeImports

Generate relative instead of absolute imports.

**Default Value:** `False`

**CLI Option:** `--relative-imports / --no-relative-imports`

### CompoundFields

xsdata relies on the field ordering for serialization. This process fails for repeating
choice or complex sequence elements. When you enable compound fields, these elements are
grouped into a single field.

```xml show_lines="2:9"
--8<-- "tests/fixtures/compound/schema.xsd"
```

**Default Value:** `False`

**CLI Option:** `--compound-fields / --no-compound-fields`

**Sub Settings**

- `defaultName`: The default compound field name, default: `choice`
- `forceDefaultName`: Force the default name in all compound fields, default: `False`
- `useSubstitutionGroups`: When all elements are part of a substitution, use the group
  name as the field name, default: `False`
- `maxNameParts`: The maximum length of elements names allowed before using the default
  name, default: `3`

**Examples:**

```python
# Force default name or max name parts > 3
choice: list[str | int | float | bool] = field(...)

# max name parts <= 3
hat_or_bat_cat: list[str | int | float] = field(...)

# All types belong to the same substitution group `product`
product: list[Shoe | Shirt | Hat] = field(...)
```

### PostponedAnnotations

Use [PEP-563](https://peps.python.org/pep-0563/), postponed evaluation of annotations.

This will add this import `from __future__ import annotations` in all generated files,
in order to avoid forward references.

**Default Value:** `False`

**CLI Option:** `--postponed-annotations / --no-postponed-annotations`

### UnnestClasses

The generator creates inner classes for `xs:complexContent`. This option allows to
unnest all inner classes.

**Default Value:** `False`

**CLI Option:** `--unnest-classes / --no-unnest-classes`

### IgnorePatterns

The generator will create a field metadata property for `xs:pattern` elements. This
property is not used during parsing, it's only informative for the developer, if you
want to reduce the noise in the generated code you can enable this option.

**Default Value:** `False`

**CLI Option:** `--ignore-patterns / --no-ignore-patterns`

### IncludeHeader

The generator will add a module docstring in all the output files.

**Example**

```python
"""This file was generated by xsdata, v24.1, on 2024-01-22 10:20:25

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
```

**Default Value:** `False`

**CLI Option:** `--include-header / --no-include-header`

## Convention Settings

Apply different naming convention per identifier.

| Element        | Default Case         | Default Safe Prefix |
| -------------- | -------------------- | ------------------- |
| `ClassName`    | `pascalCase`         | `type`              |
| `FieldName`    | `snakeCase`          | `value`             |
| `ConstantName` | `screamingSnakeCase` | `value`             |
| `ModuleName`   | `snakeCase`          | `mod`               |
| `PackageName`  | `snakeCase`          | `pkg`               |

**Attributes**

- `case`: The naming class to apply
- `safePrefix`: A prefix to add when the output name is reserved

**Cases**

| Case                 | Input     | Output    |
| -------------------- | --------- | --------- |
| `originalCase`       | `aBBc`    | `aBBc`    |
| `pascalCase`         | `my_type` | `MyType`  |
| `camelCase`          | `my_type` | `myType`  |
| `snakeCase`          | `MyType`  | `my_type` |
| `screamingSnakeCase` | `MyType`  | `My_Type` |
| `mixedCase`          | `MY_TyPE` | `MYTyPE`  |
| `mixedSnakeCase`     | `MyType`  | `My_Type` |
| `mixedPascalCase`    | `my_TYPE` | `MyTYPE`  |

## Substitution Settings

A list of search and replace patterns for identifier names, the substitutions run
**before** and **after** the naming conventions.

**Attributes**

- `type`: The identifier type `[class|field|module|package]`
- `search`: Search Pattern
- `replace`: Replace Pattern

**Defaults**

```xml
<Substitutions>
    <Substitution type="package" search="http://www.w3.org/2001/XMLSchema" replace="xs"/>
    <Substitution type="package" search="http://www.w3.org/XML/1998/namespace" replace="xml"/>
    <Substitution type="package" search="http://www.w3.org/2001/XMLSchema-instance" replace="xsi"/>
    <Substitution type="package" search="http://www.w3.org/1998/Math/MathML" replace="mathml3"/>
    <Substitution type="package" search="http://www.w3.org/1999/xlink" replace="xlink"/>
    <Substitution type="package" search="http://www.w3.org/1999/xhtml" replace="xhtml"/>
    <Substitution type="package" search="http://schemas.xmlsoap.org/wsdl/soap/" replace="soap"/>
    <Substitution type="package" search="http://schemas.xmlsoap.org/wsdl/soap12/" replace="soap12"/>
    <Substitution type="package" search="http://schemas.xmlsoap.org/soap/envelope/" replace="soapenv"/>
    <Substitution type="class" search="(.*)Class$" replace="\1Type"/>
</Substitutions>
```

## Extension Settings

Though extensions you can add base classes, mixins or decorators to the generated
classes. This way you can enhance the models functionality and add any custom business
logic.

The following configuration will add a base class and a decorator to all the generated
classes.

**Attributes**

- `type`: The extension type `[class|decorator]`
- `class`: The class name search pattern
- `import`: The absolute import of the base class or decorator object
- `prepend` Specify if you want the base class or decorator to added before all other
- `apply_if_derived` Specify if you want to add the extension if the class already
  extends another class.

!!! Warning

    If there are two extensions of the same type for the same class with the `prepend==True`,
    the base classes or decorators are added in the reverse order they are defined in the
    configuration.

**Example:**

```xml
<Extensions>
    <Extension type="class" class=".*" import="dataclasses_jsonschema.JsonSchemaMixin" prepend="false" applyIfDerived="false"/>
    <Extension type="decorator" class=".*" import="typed_dataclass.typed_dataclass" prepend="false" applyIfDerived="false"/>
</Extensions>
```

```python
from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin
from typed_dataclass import typed_dataclass

@dataclass
@typed_dataclass
class Cores(JsonSchemaMixin):
    ...
```
