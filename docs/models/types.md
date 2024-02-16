# Types

## Important

Dataclasses don't validate values when creating a new instances or assigning values to
fields. Automatic conversion of values to appropriate python data types occurs only
during the parsing process.

The parser handles value/type discrepancies leniently, potentially ignoring the defined
field type hint. When such an error arises, the converter issues a `ConverterWarning`.

If you prefer to treat conversion warnings as exceptions you need to activate the
[ParserConfig.fail_on_converter_warnings](../data_binding/basics.md#fail_on_converter_warnings)
option.

## Collections

[PEP-585](https://peps.python.org/pep-0585/) type hinting generics in standard
collections are also supported.

### List

`typing.List`

| Case           | Example                                                                           |
| -------------- | --------------------------------------------------------------------------------- |
| List           | `value: List[str] = field(default_factory=list)`                                  |
| Optional List  | `value: Optional[List[str]] = field(default=None)`                                |
| List Union     | `value: List[Union[str, int]] = field(default_factory=list)`                      |
| Tokens List    | `value: List[str] = field(default_factory=list, metadata={"tokens": True})`       |
| List of Tokens | `value: List[List[str]] = field(default_factory=list, metadata={"tokens": True})` |

### Tuple

`typing.Tuple` can be use in `frozen` dataclasses, for immutable instances.

| Case            | Example                                                                             |
| --------------- | ----------------------------------------------------------------------------------- |
| Tuple           | `value: Tuple[str] = field(default_factory=list)`                                   |
| Optional Tuple  | `value: Optional[Tuple[str]] = field(default=None)`                                 |
| Tuple Union     | `value: Tuple[Union[str, int]] = field(default_factory=list)`                       |
| Tokens Tuple    | `value: Tuple[str] = field(default_factory=list, metadata={"tokens": True})`        |
| Tuple of Tokens | `value: Tuple[Tuple[str]] = field(default_factory=list, metadata={"tokens": True})` |

### Dict

`typing.Dict` is reserved for `Attributes` type fields to capture any undefined
attribute.

| Case       | Example                                                                                |
| ---------- | -------------------------------------------------------------------------------------- |
| Attributes | `attrs: Dict[str, str] = field(default_factory=dict, metadata={"type": "Attributes"})` |

### Union

`typing.Union`

| Case           | Example                                                         |
| -------------- | --------------------------------------------------------------- |
| Union          | `value: Union[str, int, float] = field()`                       |
| Optional Union | `value: Optional[Union[str, int, float]] = field(default=None)` |

The order of the types doesn't matter, internally the converter sorts the types by
priority:

1. `int`
2. `bool`
3. `float`
4. `Decimal`
5. `datetime`
6. `date`
7. `time`
8. `XmlTime`
9. `XmlDate`
10. `XmlDateTime`
11. `XmlDuration`
12. `XmlPeriod`
13. `QName`
14. `str`

## Standard Types

This is the list of all the supported primitive types.

### Boolean

| Input     | Python  | XML       | JSON    |
| --------- | ------- | --------- | ------- |
| `"true"`  | `True`  | `"true"`  | `true`  |
| `"1"`     | `True`  | `"true"`  | `true`  |
| `"false"` | `False` | `"false"` | `false` |
| `"1"`     | `False` | `"false"` | `false` |

**Python Type**: [bool][]

**XML Type:** [boolean](https://www.w3.org/TR/xmlschema11-2/#boolean)

### Bytes Array

The fields must provide the `format` metadata property.

- `base16` for hexadecimal string
- `base64` for base64 encoded bytes-like object or ASCII strings

**Python Type**: [bytes][]

**XML Types:** [hexBinary](https://www.w3.org/TR/xmlschema11-2/#hexBinary),
[base64Binary](https://www.w3.org/TR/xmlschema11-2/#base64Binary)

### Decimal

**Python Type**: [decimal.Decimal][]

**XML Type:** [decimal](https://www.w3.org/TR/xmlschema11-2/#decimal)

### Float

**Python Type**: [float][]

**XML Types:** [double](https://www.w3.org/TR/xmlschema11-2/#double),
[float](https://www.w3.org/TR/xmlschema11-2/#float)

### Integer

**Python Type**: [int][]

**XML Types:**

- [int](https://www.w3.org/TR/xmlschema11-2/#int)
- [nonPositiveInteger](https://www.w3.org/TR/xmlschema11-2/#nonPositiveInteger)
- [negativeInteger](https://www.w3.org/TR/xmlschema11-2/#negativeInteger)
- [long](https://www.w3.org/TR/xmlschema11-2/#long)
- [integer](https://www.w3.org/TR/xmlschema11-2/#integer)
- [short](https://www.w3.org/TR/xmlschema11-2/#short)
- [byte](https://www.w3.org/TR/xmlschema11-2/#byte)
- [nonNegativeInteger](https://www.w3.org/TR/xmlschema11-2/#nonNegativeInteger)
- [unsignedLong](https://www.w3.org/TR/xmlschema11-2/#unsignedLong)
- [unsignedInt](https://www.w3.org/TR/xmlschema11-2/#unsignedInt)
- [unsignedShort](https://www.w3.org/TR/xmlschema11-2/#unsignedShort)
- [unsignedByte](https://www.w3.org/TR/xmlschema11-2/#unsignedByte)
- [positiveInteger](https://www.w3.org/TR/xmlschema11-2/#positiveInteger)

### Object

**Python Type**: [object][]

**XML Type:** [anySimpleType](https://www.w3.org/TR/xmlschema11-2/#anySimpleType)

### QName

**Python Type**: [xml.etree.ElementTree.QName][]

**XML Types:** [QName](https://www.w3.org/TR/xmlschema11-2/#QName),
[NOTATION](https://www.w3.org/TR/xmlschema11-2/#NOTATION)

### String

**Python Type**: [str][]

**XML Types:**

- [string](https://www.w3.org/TR/xmlschema11-2/#string)
- [anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI)
- [normalizedString](https://www.w3.org/TR/xmlschema11-2/#normalizedString)
- [token](https://www.w3.org/TR/xmlschema11-2/#token)
- [language](https://www.w3.org/TR/xmlschema11-2/#language)
- [NMTOKEN](https://www.w3.org/TR/xmlschema11-2/#NMTOKEN)
- [NMTOKENS](https://www.w3.org/TR/xmlschema11-2/#NMTOKENS)
- [Name](https://www.w3.org/TR/xmlschema11-2/#Name)
- [NCName](https://www.w3.org/TR/xmlschema11-2/#NCName)
- [ID](https://www.w3.org/TR/xmlschema11-2/#ID)
- [IDREF](https://www.w3.org/TR/xmlschema11-2/#IDREF)
- [IDREFS](https://www.w3.org/TR/xmlschema11-2/#IDREFS)
- [ENTITIES](https://www.w3.org/TR/xmlschema11-2/#ENTITIES)
- [ENTITY](https://www.w3.org/TR/xmlschema11-2/#ENTITY)
- [anyAtomicType](https://www.w3.org/TR/xmlschema11-2/#anyAtomicType)
- [error](https://www.w3.org/TR/xmlschema11-2/#error)

### XmlDate

**Python Type**: [xsdata.models.datatype.XmlDate][]

**XML Type:** [date](https://www.w3.org/TR/xmlschema11-2/#date)

### XmlDateTime

**Python Type**: [xsdata.models.datatype.XmlDateTime][]

**XML Types:** [dateTime](https://www.w3.org/TR/xmlschema11-2/#dateTime),
[dateTimeStamp](https://www.w3.org/TR/xmlschema11-2/#dateTimeStamp)

### XmlDuration

**Python Type**: [xsdata.models.datatype.XmlDuration][]

**XML Types:**

- [duration](https://www.w3.org/TR/xmlschema11-2/#duration)
- [dayTimeDuration](https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration)
- [yearMonthDuration](https://www.w3.org/TR/xmlschema11-2/#yearMonthDuration)

### XmlPeriod

**Python Type**: [xsdata.models.datatype.XmlPeriod][]

**XML Types:**

- [gYearMonth](https://www.w3.org/TR/xmlschema11-2/#gYearMonth)
- [gYear](https://www.w3.org/TR/xmlschema11-2/#gYear)
- [gMonthDay](https://www.w3.org/TR/xmlschema11-2/#gMonthDay)
- [gMonth](https://www.w3.org/TR/xmlschema11-2/#gMonth)
- [gDay](https://www.w3.org/TR/xmlschema11-2/#gDay)

### XmlTime

**Python Type**: [xsdata.models.datatype.XmlTime][]

**XML Type:**: [time](https://www.w3.org/TR/xmlschema11-2/#time)

### Enum

**Python Type**: [enum.Enum][]

**XML Type:**: [enumeration](https://www.w3.org/TR/xmlschema11-2/#rf-enumeration)

## User Types

You can register you own custom types as well as long as they are not dataclasses.

```python
>>> from dataclasses import dataclass, field
>>> from xsdata.formats.converter import Converter, converter
>>> from xsdata.formats.dataclass.parsers import XmlParser
>>> from xsdata.formats.dataclass.serializers import XmlSerializer
...
>>> serializer = XmlSerializer()
>>> serializer.config.indent = "  "
>>> serializer.config.xml_declaration = False
>>>
>>> class TheGoodFloat(float):
...     pass
...
>>> @dataclass
... class Example:
...     good: TheGoodFloat = field(metadata=dict(format="{:.2f}"))
...     bad: float
...
>>> class TheGoodFloatConverter(Converter):
...    def deserialize(self, value: str, **kwargs) -> TheGoodFloat:
...        return round(TheGoodFloat(value), 1)  # Even nicer
...
...    def serialize(self, value: TheGoodFloat, **kwargs) -> str:
...        if kwargs["format"]:
...            return kwargs["format"].format(value)
...        return str(value)
...
>>> converter.register_converter(TheGoodFloat, TheGoodFloatConverter())
>>> output = serializer.render(Example(TheGoodFloat(10.983263748), -9.9827632))
>>> print(output)
<Example>
  <good>10.98</good>
  <bad>-9.9827632</bad>
</Example>
>>> XmlParser().from_string(output)
Example(good=11.0, bad=-9.9827632)

```
