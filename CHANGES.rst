23.7 (2023-07-23)
-----------------
- Fixed decimal converter to avoid scientific notations (`#826 <https://github.com/tefra/xsdata/pull/826>`_)
- Fixed nympy paramater docstring format  (`#827 <https://github.com/tefra/xsdata/pull/827>`_)
- Fixed optional/required override validation (`#820 <https://github.com/tefra/xsdata/pull/820>`_)
- Fixed WSDL mapper to respect the elements original location (`#832 <https://github.com/tefra/xsdata/pull/832>`_)
- Added Python 3.12 support


23.6 (2023-06-24)
-----------------
- Fixed conflicting enum values leading to wrong default values (`#806 <https://github.com/tefra/xsdata/pull/806>`_)
- Added support for custom decorators and base classes (`#793 <https://github.com/tefra/xsdata/pull/793>`_)
- Added parser config to load external dtd to resolve entities (`#797 <https://github.com/tefra/xsdata/pull/797>`_)
- Added requests sessions on the wsdl client transport (`#798 <https://github.com/tefra/xsdata/pull/798>`_)
- Added support subscriptable types and UnionType (`#801 <https://github.com/tefra/xsdata/pull/801>`_)
- Added option to restrict models package for auto-locator (`#809 <https://github.com/tefra/xsdata/pull/809>`_)
- Updated context to only cache supported classes (`#796 <https://github.com/tefra/xsdata/pull/796>`_)
- Removed tox requirement (`#800 <https://github.com/tefra/xsdata/pull/800>`_)
- Converted to pyproject.toml (`#802 <https://github.com/tefra/xsdata/pull/802>`_)

23.5 (2023-05-21)
------------------
- Fixed XML meta var index conflicts.
- Fixed mixed content handling for DTD elements. (`#749 <https://github.com/tefra/xsdata/pull/749>`_, `#762 <https://github.com/tefra/xsdata/pull/762>`_)
- Fixed an issue with required attributes turning into optional ones.
- Fixed calculation of min/max occurs when parsing XML/JSON documents. (`#756 <https://github.com/tefra/xsdata/pull/756>`_)
- Fixed calculation of min/max occurs when parsing DTD choice content types. (`#760 <https://github.com/tefra/xsdata/pull/760>`_)
- Fixed an issue when parsing tail content for compound wildcard elements.
- Fixed an issue with the code analyzer not fully processing some classes.
- Fixed an issue with the code analyzer taking forever to process very large enumerations. (`#776 <https://github.com/tefra/xsdata/issue/776>`_)
- Fixed an issue in the JSON parser with optional choice elements.
- Updated the transformer to silently ignore malformed JSON files. (`#750 <https://github.com/tefra/xsdata/pull/750>`_)
- Updated the override attribute handler to fix naming conflicts.
- Updated the override attribute handler to allow wildcard overrides.
- Updated conditions on extensions flattening (over-flattening). (`#754 <https://github.com/tefra/xsdata/pull/754>`_)
- Updated Group, AttributeGroup handling, skipping a few cases.
- Updated how min/max occurs are calculated with nested containers.
- Updated handling of element substitutions to treat them as choices. (`#786 <https://github.com/tefra/xsdata/pull/786>`_)
- Updated Pycodeserializer to skip default field values.
- Updated flattening restriction base classes when sequence elements are out of order.
- Updated docformatter to v1.6.5.
- Added support to override compound fields.
- Added support for multiple sequential groups in a class.
- Added support for non-list compound fields.
- Added support to mix list and non-list fields with sequence groups.
- Added an option to include headers in generated files. (`#746 <https://github.com/tefra/xsdata/pull/746>`_)
- Added an option to cache the initial load and mapping of resources.
- Added support for regular expressions in config substitutions. (`#755 <https://github.com/tefra/xsdata/pull/755>`_)
- Added a pretty print indentation option in the serializer config. (`#780 <https://github.com/tefra/xsdata/pull/780>`_)
- Added an option to set the encoding in the SOAP Client. (`#773 <https://github.com/tefra/xsdata/pull/773>`_)
- Added a CLI flag to show debug messages.
- Added a debug message for possible circular references during code generation.
- Added support to generate prohibited fields when they restrict parent fields. (`#781 <https://github.com/tefra/xsdata/pull/781>`_)

This release is bigger than intended and includes many major changes,
that's why it took so long.


22.12 (2022-12-17)
------------------
- Added option to ignore xml pattern restrictions `#727 <https://github.com/tefra/xsdata/pull/727>`_
- Added globalns support via SerializerConfig `#724 <https://github.com/tefra/xsdata/pull/724>`_
- Pinned docformatter version to v1.5.0 `#729 <https://github.com/tefra/xsdata/pull/729>`_

22.11 (2022-11-06)
------------------
- Added list wrapper for elements and primitive nodes `#710 <https://github.com/tefra/xsdata/pull/710>`_

22.9 (2022-09-24)
-----------------
- Fixed code generation inconsistencies in different operating systems.
- Fixed circular imports error `#706 <https://github.com/tefra/xsdata/pull/706>`_
- Fixed naming conflicts in imports `#706 <https://github.com/tefra/xsdata/pull/706>`_
- Fixed issue with wrong occurrences in DTD code generation  `#705 <https://github.com/tefra/xsdata/pull/705>`_
- Fixed xs:group and xs:attrGroup name conflicts `#702 <https://github.com/tefra/xsdata/pull/702>`_
- Added mathml3 in standard schemas

22.8 (2022-08-21)
-----------------
- Added pycode serializer `#626 <https://github.com/tefra/xsdata/issues/626>`_
- Added option to filter out unused global types `#691 <https://github.com/tefra/xsdata/issues/691>`_
- Avoid using generics for mixed content when possible `#696 <https://github.com/tefra/xsdata/pull/696>`_
- Removed support for python 3.6 `#671 <https://github.com/tefra/xsdata/pull/671>`_


22.7 (2022-07-22)
-----------------
- Fix empty lists do not get serialized `#686 <https://github.com/tefra/xsdata/issues/686>`_
- Added external DTD code generator `#688 <https://github.com/tefra/xsdata/pull/688>`_
- Added support for python 3.11

In the next release we will drop python 3.6 support!!!


22.5 (2022-05-08)
-----------------
- Added support for xml date/time nanoseconds `#679 <https://github.com/tefra/xsdata/pull/679>`_


22.4 (2022-04-10)
-----------------
- Added config option to unnest classes
- Added new class meta option global_type, to hide classes from discovery
- Removed min/max length restrictions for enum type fields
- Allow builtin xml types to be fully extended `#672 <https://github.com/tefra/xsdata/pull/672>`_


22.3 (2022-03-20)
-----------------
- Added official support for python 3.11
- Fixed enumerations restricting complex types `#659 <https://github.com/tefra/xsdata/issues/659>`_
- Fixed attribute name duplicate check to avoid invalid slugs

22.2 (2022-02-06)
-----------------
- Fixed substitution groups on duplicate global types `#648 <https://github.com/tefra/xsdata/issues/648>`_
- Added Postponed Annotations config option `#646 <https://github.com/tefra/xsdata/issues/646>`_
- Added support for subclasses with different namespaces `#654 <https://github.com/tefra/xsdata/issues/654>`_

22.1 (2022-01-23)
-----------------
- Added recursive glob for cli dir source `#643 <https://github.com/tefra/xsdata/issues/643>`_
- Added cfg options to change/force compound field names `#639 <https://github.com/tefra/xsdata/issues/639>`_

21.12 (2021-12-05)
------------------
- Fixed wsdl generator to use operation name for rpc input messages `#609 <https://github.com/tefra/xsdata/issues/609>`_
- Fixed wsdl generator to check for qualified elements for message part types `#612 <https://github.com/tefra/xsdata/issues/612>`_
- Fixed compound field matcher to prefer exact types over derived `#617 <https://github.com/tefra/xsdata/issues/617>`_
- Added async to the reserved keywords `#600 <https://github.com/tefra/xsdata/issues/600>`_
- Added generator config for search & replace substitutions `#624 <https://github.com/tefra/xsdata/issues/624>`_
- Updated code generator to remove abstract elements from class attrs `#627 <https://github.com/tefra/xsdata/issues/627>`_
- Updated code generator to filter out all unused types `#629 <https://github.com/tefra/xsdata/issues/629>`_


21.11 (2021-11-02)
------------------
- Fixed unescaped quotes in regex pattern `#592 <https://github.com/tefra/xsdata/issues/592>`_
- Added config option fail_on_unknown_attributes `#597 <https://github.com/tefra/xsdata/issues/597>`_
- Fixed build for python 3.10

21.9 (2021-09-04)
-----------------
- Automate cli generate options `#578 <https://github.com/tefra/xsdata/pull/578>`_

  - Generate cli options by the config model
  - Allow to enable/disable any flag
  - Allow to bypass any value from the config
  - Removed -cf/-ri as we can't have switches with short names

- Fixed generator not cascading default values to inner classes `#579 <https://github.com/tefra/xsdata/issues/579>`_
- Re-raise xml syntax errors as xsdata.exceptions.ParserError `#571 <https://github.com/tefra/xsdata/issues/571>`_
- Added cli summary with recovered warnings and issues `#583 <https://github.com/tefra/xsdata/pull/583>`_
- Removed the native and lxml SAX handlers `#582 <https://github.com/tefra/xsdata/issues/582>`_

21.8 (2021-08-03)
-----------------
- Deprecated JsonSerializer indent property, use SerializerConfig instead
- Fixed SchemaMapper assigning wrong namespace for imported unqualified elements
- Fixed AttributeTypeHandler to maintain occurs between any flattening
- Fixed missing required field metadata property
- Fixed nillable fields not being marked as optional
- Fixed fields ordering during class reduce process (Codegen from xml/json)
- Added support for xs:defaultOpenContent:appliesToEmpty attribute
- Added ParserConfig class factory option `#549 <https://github.com/tefra/xsdata/pull/549>`_
- Added SerializerConfig option to ignore optional default attributes `#555 <https://github.com/tefra/xsdata/pull/555>`_
- Added warning on unexpected duplicate types `#564 <https://github.com/tefra/xsdata/pull/564>`_
- Added GeneratorConfig support for kw_only and slots for python >= 3.10
- Added structure style namespace-clusters `#573 <https://github.com/tefra/xsdata/pull/573>`_
- Updated text fields default value to empty string and marked as required `#570 <https://github.com/tefra/xsdata/pull/570>`_
- Updated fields derived from xs:substitutionGroups to optional
- Updated fields derived from xs:any to optional
- Updated AttributeDefaultValueHandler to preserve acceptable default values
- Updated AttributeDefaultValueHandler to mark as optional any xsi:type attribute
- Updated xs:alternative handling to resemble xs:choice
- Updated mixed content handler to group all elements under wildcard
- Updated ElementMapper to detect nillable types
- Updated DictMapper to generate list of xs:anySimpleType for empty list nodes
- Updated the compatibility layer for dataclass style plugins
- Updated namespaces structure style to convert namespaces similar to jaxb

  - `http://www.w3.org/XML/1998/namespace` to `org.w3.XML.1998.namespace`

- Update binding process for nillable types and fields

  - nillable types can be initialized
  - nillable fields are initialized with None values

21.7 (2021-07-01)
-----------------
- Fixed docstrings backslash escaping `#518 <https://github.com/tefra/xsdata/pull/518>`_
- Fixed analyzer flattening bare types `#541 <https://github.com/tefra/xsdata/pull/541>`_
- Fixed multiple issues with compound fields and override fields `#533 <https://github.com/tefra/xsdata/pull/533>`_
- Fixed missing derived elements types during xml parsing `#541 <https://github.com/tefra/xsdata/pull/541>`_
- Added structure style: clusters for smaller packages `#509 <https://github.com/tefra/xsdata/pull/509>`_
- Added configuration to generate relative imports `#519 <https://github.com/tefra/xsdata/pull/519>`_
- Added configuration to toggle all dataclasses features `#529 <https://github.com/tefra/xsdata/pull/529>`_
- Added binding support for tuple typing annotations (frozen dataclasses) `#529 <https://github.com/tefra/xsdata/pull/529>`_
- Added support to bind data directly from xml/lxml Element and ElementTree `#531 <https://github.com/tefra/xsdata/pull/531>`_ `#546 <https://github.com/tefra/xsdata/pull/546>`_
- Updated analyzer to avoid same name for outer-inner classes `#511 <https://github.com/tefra/xsdata/pull/511>`_
- Updated cli to fail early if config file is invalid `#514 <https://github.com/tefra/xsdata/pull/514>`_
- Updated cli to remove setuptools from runtime dependencies `#515 <https://github.com/tefra/xsdata/pull/515>`_
- Updated analyzer to relax override field validations completely `#516 <https://github.com/tefra/xsdata/pull/516>`_
- Updated analyzer to sort classes before class name conflict resolution `#517 <https://github.com/tefra/xsdata/pull/517>`_
- Updated JSON parser to attempt binding against subclasses `#527 <https://github.com/tefra/xsdata/pull/527>`_
- Updated analyzer to guard against multiple substitution group runs `#538 <https://github.com/tefra/xsdata/pull/538>`_
- Updated code generation to use case sensitive reserved words `#545 <https://github.com/tefra/xsdata/pull/545>`_


21.6 (2021-06-01)
-----------------
- Fixed no args Dict annotation, raising an exception `#494 <https://github.com/tefra/xsdata/issues/494>`_
- Fixed original name case not working for field names `#498 <https://github.com/tefra/xsdata/issues/498>`_
- Fixed element type resolution with duplicate name conflicts `#503 <https://github.com/tefra/xsdata/issues/503>`_
- Added handler to flatten bare inner classes
- Added the ability for custom types to subclass named tuples
- Added keyword meta in the reserved words `#491 <https://github.com/tefra/xsdata/issues/491>`_
- Added new xml type `Ignore` to skip fields during binding `#504 <https://github.com/tefra/xsdata/issues/504>`_
- Updated generic model DerivedElement.substituted flag with xsi:type
- Updated core components to improve binding performance

  - Converted almost all internal dataclasses to simple objects with __slots__
  - Converted the internal xml date/time types to named tuples
  - Reduced models metadata lookup times and memory footprint

- Updated JSON parser `#495 <https://github.com/tefra/xsdata/issues/495>`_

  - Support failing on unknown properties
  - Support required properties
  - Support parser config
  - Stricter binding process
  - Enhance DerivedElement support
- Moved Definitive XML Schema tests to the samples repository


21.5 (2021-05-07)
-----------------
- Added output structure style single-package `#469 <https://github.com/tefra/xsdata/issues/469>`_
- Added support for marshalling array of objects for json `#448 <https://github.com/tefra/xsdata/issues/448>`_
- Added support to generate code from raw json documents `#445 <https://github.com/tefra/xsdata/issues/445>`_
- Added docstring style Blank to avoid generating them `#460 <https://github.com/tefra/xsdata/issues/460>`_
- Added validations for non supported type hints
- Added support for python 3.10
- Generate package __all__ lists `#459 <https://github.com/tefra/xsdata/issues/459>`_
- Generate factory for xs:list enumeration default values `#471 <https://github.com/tefra/xsdata/issues/471>`_
- Avoid generating prohibited elements with maxOccurs==0 `#478 <https://github.com/tefra/xsdata/issues/478>`_
- Avoid generating identical overriding fields `#466 <https://github.com/tefra/xsdata/issues/466>`_
- Fixed flattening base classes if they are also subclasses `#473 <https://github.com/tefra/xsdata/issues/473>`_
- Fixed unchecked class name conflict resolution `#457 <https://github.com/tefra/xsdata/issues/457>`_
- Refactored context components to improve binding performance `#476 <https://github.com/tefra/xsdata/issues/476>`_


21.4 (2021-04-02)
-----------------
- Split requirements to extras cli, soap and lxml `#419 <https://github.com/tefra/xsdata/issues/419>`_
- Fixed parser conflict when an attribute and element field have the same qualified name
- Added cli auto detection for source types, removed cli flag `--wsdl`
- Added cli support to generate code from raw xml documents
- Added cli entry point to allow pluggable output formats `#429 <https://github.com/tefra/xsdata/issues/429>`_
- Added cli short flags for all options and flags
- Added handler to set effective choice groups `#433 <https://github.com/tefra/xsdata/issues/433>`_
- Moved plantUML output format to a standalone `plugin <https://github.com/tefra/xsdata-plantuml>`_
- Updated xml parser to allow unions of primitive and class types
- Updated XmlDateTime parser to catch invalid cases with extra leading zeros
- Updated QName converter to validate uri/ncname when parsing string representations
- Updated JsonParser to allow parsing from filename string
- Updated cli option `--compound-fields` to a boolean flag


21.3 (2021-03-04)
-----------------
- Added constant name convention config `#407 <https://github.com/tefra/xsdata/issues/407>`_
- Added naming schemes screaming snake case and original case
- Updated xsi:lookup on xs:any derived elements `#315 <https://github.com/tefra/xsdata/issues/315>`_
- Updated fields restriction inheritance `#417 <https://github.com/tefra/xsdata/issues/417>`_
- Updated cli to allow package override from arguments `#416 <https://github.com/tefra/xsdata/issues/416>`_
- Updated code generation to merge duplicate global types earlier `#406 <https://github.com/tefra/xsdata/issues/406>`_
- Fixed docstrings issue breaking python syntax `#403 <https://github.com/tefra/xsdata/issues/403>`_
- Fixed bindings for nillable content without workarounds `#408 <https://github.com/tefra/xsdata/issues/408>`_
- Fixed resolver to apply aliases on extensions and choice fields `#414 <https://github.com/tefra/xsdata/issues/414>`_
- Fixed schema models limiting xs:appinfo occurrences `#420 <https://github.com/tefra/xsdata/issues/420>`_
- Decoupled core systems from click and lxml

**Notice**: In the next release installation profiles will be introduced that will turn
the cli, lxml and soap features **optional**.


21.2 (2021-02-02)
-----------------
- Added class name context for user naming schemes `#348 <https://github.com/tefra/xsdata/issues/348>`_
- Added mixed pascal naming scheme `#348 <https://github.com/tefra/xsdata/issues/348>`_
- Added access to element/attribute name generators `#381 <https://github.com/tefra/xsdata/issues/381>`_
- Added XmlHexBinary/XmlBase64Binary builtin data types `#387 <https://github.com/tefra/xsdata/issues/387>`_
- Added support for xs:anyType root elements `#399 <https://github.com/tefra/xsdata/issues/399>`_
- Updated JSON binding modules to use the fields local name `#389 <https://github.com/tefra/xsdata/issues/389>`_
- Updated enum classes generation
   - Promote all inner enums to root `#383 <https://github.com/tefra/xsdata/issues/383>`_
   - Fixed issues with producing invalid members `#385 <https://github.com/tefra/xsdata/issues/385>`_
   - Added support for list/tuple member values
- Updated parsers accuracy for Union types
- Updated dependency resolution accuracy
- Update base classes generation strategies
- Updated builtin data types with helper constructors/methods
- Fixed inner class names conflicts `#375 <https://github.com/tefra/xsdata/issues/375>`_
- Fixed issue not generating fields derived from xs:alternative elements `#393 <https://github.com/tefra/xsdata/issues/393>`_
- Fixed duplicate root class name regression from v20.12
- Fixed issue adding unused lib imports
- Fixed issue adding unused name properties to choice elements

This is a sleeper release ✨✨✨ so many code generation improvements and finally the
JSON binding is aligned with XML.

21.1 (2021-01-08)
-----------------
- Fixed XmlWriter converting attribute keys to QName. `#346 <https://github.com/tefra/xsdata/issues/346>`_
- Set empty complexType base to anySimpleType `#349 <https://github.com/tefra/xsdata/issues/349>`_
- Improve duplicate attr names detection `#351 <https://github.com/tefra/xsdata/issues/351>`_
- Add SerializerConfig::xml_declaration option `#357 <https://github.com/tefra/xsdata/issues/357>`_
- Generate default value/factory for compound fields `#359 <https://github.com/tefra/xsdata/issues/359>`_
- Fixed default value for token fields `#360 <https://github.com/tefra/xsdata/issues/360>`_
- Add doc metadata for compound fields `#362 <https://github.com/tefra/xsdata/issues/362>`_
- JsonParser: handle class and primitive unions `#369 <https://github.com/tefra/xsdata/issues/369>`_
- Update python mappings `#366 <https://github.com/tefra/xsdata/issues/366>`_
   - Map xs:hexBinary and xs:base64Binary to bytes
   - Map xs:date/time types to builtin types XmlDate/Time
   - Map xs:duration to builtin type XmlDuration
   - Map xs:g[Year[Month[Day]]] to builtin type XmlPeriod
   - Map xs:Notation to QName
   - Add converter adapters for datetime.date/time
   - Add fields metadata key 'format' for time/date/binary types
   - Fixed issues with default literal values
   - Fixed issue with random field types order


20.12 (2020-12-10)
------------------
- Added SerializerConfig with new options. `#268 <https://github.com/tefra/xsdata/issues/268>`_, `#320 <https://github.com/tefra/xsdata/issues/320>`_
- Added docstring styles: rst, google, numpy, accessible. `#318 <https://github.com/tefra/xsdata/issues/318>`_, `#340 <https://github.com/tefra/xsdata/issues/340>`_
- Added `max line length` generator configuration. `#342 <https://github.com/tefra/xsdata/issues/342>`_
- Added dynamic type locator for parsers. `#332 <https://github.com/tefra/xsdata/issues/332>`_
- Fixed multiple issues with json binding. `98.7% <https://github.com/tefra/xsdata-w3c-tests/actions>`_ successful roundtrips


20.11.1 (2020-11-13)
--------------------
- Catch all type errors on xsi cache build `#316 <https://github.com/tefra/xsdata/issues/316>`_

20.11 (2020-11-10)
------------------
- Added sub command to download remote schemas and definitions. `#279 <https://github.com/tefra/xsdata/issues/279>`_
- Added new optional xml type `Elements` to maintain ordering for repeatable choices. `#296 <https://github.com/tefra/xsdata/issues/296>`_
- Added xsi:type lookup procedure for xs:anyType derived elements. `#306 <https://github.com/tefra/xsdata/issues/306>`_
- Updated simple type flattening detection. `#286 <https://github.com/tefra/xsdata/issues/286>`_
- Updated generator to allow namespace structure on schemas without target namespace.
- Updated generator to avoid writing min/max occurs metadata for implied values. `#297 <https://github.com/tefra/xsdata/issues/297>`_
- Update generator to use literal dictionary initialization.
- Updated parser security, disable lxml network and entities resolve.
- Fixed field types detection for elements with xs:alternative children. `#284 <https://github.com/tefra/xsdata/issues/284>`_
- Fixed file generation to enforce default charset UTF-8. `#302 <https://github.com/tefra/xsdata/issues/302>`_
- Fixed jinja2 undefined namespace var collision. `#298 <https://github.com/tefra/xsdata/issues/298>`_
- Fixed import class name collision. `#300 <https://github.com/tefra/xsdata/issues/300>`_
- Fixed restriction inheritance on xs:group elements. `#301 <https://github.com/tefra/xsdata/issues/301>`_


20.10 (2020-10-02)
------------------
- Fixed generator adding multiple default value fields. `#249 <https://github.com/tefra/xsdata/issues/249>`_
- Fixed generator not applying nested container restrictions. `#263 <https://github.com/tefra/xsdata/issues/253>`_
- Fixed generator to avoid case insensitive class name conflicts. `#269 <https://github.com/tefra/xsdata/issues/269>`_
- Fixed generator rendering unused simple types.
- Fixed generator unsorted libraries imports.
- Fixed JsonParser trying to parse init=False fields. `#253 <https://github.com/tefra/xsdata/issues/253>`_
- Fixed NodeParser binding tail content more than once with mixed vars. `#256 <https://github.com/tefra/xsdata/issues/256>`_
- Added XmlWriter interface to decouple serialize from lxml. `#247 <https://github.com/tefra/xsdata/issues/247>`_
- Added native python xml content writer XmlEventWriter. ✨✨✨
- Added lxml based content writer LxmlEventWriter.
- Added generator config with options to control naming cases and aliases. `#265 <https://github.com/tefra/xsdata/issues/265>`_
- Updated field xml type auto detection to be more flexible. `#246 <https://github.com/tefra/xsdata/issues/246>`_
- Updated EnumConverter to resort to canonical form matching as last resort. `#273 <https://github.com/tefra/xsdata/issues/273>`_
- Updated support for derived elements. `#267 <https://github.com/tefra/xsdata/issues/267>`_


This is my favorite release so far, maybe because xsdata reached one year of development
✨✨✨ or maybe because some of the last original components finally got the rewrite they
deserved.


20.9 (2020-09-03)
-----------------
- Added field metadata key `tokens` for xs:list or xs:NMTOKENS derived elements.
- Added datatype factory to register custom converters.
- Added XmlHandler interface to decouple parsing from lxml.
- Added lxml based content handlers: LxmlEventHandler, LxmlSaxHandler
- Added native python xml content handlers: XmlEventHandler, XmlSaxHandler
- Added support for python >= 3.6 `#241 <https://github.com/tefra/xsdata/issues/241>`_
- Added codegen for soap 1.1 fault messages.
- Fixed converting to enum members derived from xs:NMTOKENS.
- Fixed package level import naming conflicts. `#228 <https://github.com/tefra/xsdata/issues/206>`_
- Fixed xml serializing to allow empty strings in attribute values. `#230 <https://github.com/tefra/xsdata/issues/230>`_
- Fixed xml serializing for mixed content with non generics. `#238 <https://github.com/tefra/xsdata/issues/238>`_


20.8 (2020-08-01)
-----------------
- Added codegen support for **WSDL 1.1 and SOAP 1.1** bindings.
- Added experimental web services client.
- Added cli flag ``--ns-struct`` to group classes by target namespaces. `#206 <https://github.com/tefra/xsdata/issues/206>`_
- Added parser config to support xinclude statements. `#207 <https://github.com/tefra/xsdata/issues/207>`_
- Added new xml union node to improve bindings for fields with union type. `#207 <https://github.com/tefra/xsdata/issues/207>`_
- Fixed class resolve issue with mixed namespaces. `#204 <https://github.com/tefra/xsdata/issues/204>`_
- Fixed attribute comparison issue. `#209 <https://github.com/tefra/xsdata/issues/209>`_
- Fixed data type mapping for various schema elements. `#221 <https://github.com/tefra/xsdata/issues/221>`_
- Fixed mixed content handling. `#213 <https://github.com/tefra/xsdata/issues/213>`_
- Code cleanup & 100% coverage.


20.7 (2020-07-04)
-----------------
- Updated analyzer to allow abstract types to be generated. `#199 <https://github.com/tefra/xsdata/issues/199>`_
- Removed support to generate code from multiple sources. `#172 <https://github.com/tefra/xsdata/issues/172>`_
- Fixed naming conflict with AttributeGroup analyzer handler. `#194 <https://github.com/tefra/xsdata/issues/194>`_
- Fixed analyzer to merge redefined attribute groups. `#196 <https://github.com/tefra/xsdata/issues/196>`_
- Fixed analyzer to block inheritance on xs:override derived types. `#198 <https://github.com/tefra/xsdata/issues/198>`_
- Refactored code to prepare for wsdl support.


20.6 (2020-06-01)
-----------------
- Updated XmlSerializer to render default namespace whenever possible.
- Fixed issue generating modules outside the target package.
- Fixed issue not creating nested package __init__ files.
- Code cleanup & docstrings

20.5.5 (2020-05-23)
-------------------
- Added version option in the xsdata cli.
- Added generation of missing python __init__ files.
- Added support for default values to inner enum classes.
- Fixed multiple issues with abstract classes and attributes/extension flattening.
- Fixed instance cross references causing codegen unpredictable results.
- Fixed xml serialization of wildcard attributes with user defined model values.
- Fixed issue with redefined/override elements with annotations.
- Fixed expand attribute groups recursively.
- Fixed false positive circular references.
- Fixed enumeration unions detection.
- Refactored ClassAnalyzer to smaller components.

20.5.4 (2020-05-15)
-------------------
- Fix flattening enumeration unions.
- Fix generation for enum fields with default/fixed value.
- Fix duplicate attribute names handler to be case insensitive.

20.5.1 (2020-05-14)
-------------------
- Added support to fetch remote schemas.
- Updated duplicate attribute names handling.
- Updated code generation for enum type fields and default values.
- Fixed issue not generating classes derived from simple types.
- Fixed analyzer reaching the maximum recursion depth.
- Fixed analyzer to flatten properly inner self referencing classes.
- Moved dataclasses python conventions to jinja filters.

20.5 (2020-05-02)
-----------------
- Updated codegen cli to accept multiple definitions or directories as argument.
- Update ClassBuilder to recursively search for anonymous types.
- Updated XmlParser to be thread-safe.
- Added performance tweaks on XmlParser.
- Added parser config to fail or not on unknown properties.
- Fixed primitive types being marked as forward references.
- Fixed nested restrictions on xs:simpleType.
- Fixed ClassAnalyzer to recover/ignore missing types.

20.4.2 (2020-04-21)
-------------------
- Added support for abstract xsi:types in XmlParser.
- Added cache for event names in XmlParser.
- Added sanitization for generated module names.
- Fixed not flattening abstract extension.
- Fixed extension name conflicts between simple and complex types.
- Fixed possible memory leak in CodeWriter.
- Fixed looping variables twice to find next node in XmlParser.
- Fixed CodeWriter adding unnecessary new lines.


20.4.1 (2020-04-13)
-------------------
- Fixed open content attribute with mode suffix to be generated last.
- Fixed issues with wildcard and mixed content parsing.
- Updated xs:qname mapping to lxml.QName
- Updated support for xs:list.
- Updated parser to ignore xsi:type attributes default/fixed values.
- Refactored code components.
- Pass more than 99% of the `W3C XML Schema 1.1 test cases <https://travis-ci.org/tefra/xsdata-w3c-tests>`_

20.4 (2020-04-01)
-----------------
- Added support for sequential fields.
- Added support for open content.
- Added support multiple redefined elements.
- Updated support for wildcards to be aware of generic namespaces.
- Updated support for wildcards to be aware of non generic objects.
- Updated codegen to run after fully parsing all the definitions.
- Updated codegen to skip unresolved schema locations.
- Updated xml parser to ignore comments.
- Updated xml parser to retain a copy of the input namespaces.
- Fixed issues with nillable fields being ignored.
- Fixed multiple issues with wrong restrictions being applied.
- Fixed binding issues when there are naming conflicts.
- Fixed serialization for inf/nan/exponential float and decimal values.
- Fixed naming conflicts with class/package names.
- Fixed multiple circular import issues during parsing and code generation.
- Pass more than 98% of the `W3C XML Schema 1.1 test cases <https://travis-ci.org/tefra/xsdata-w3c-tests>`_


20.3 (2020-03-01)
-----------------
- Added copies of common schemas xlink, xsi, xml.
- Added XML Schema 1.1 models and properties.
- Added support for redefines, overrides, alternatives and default attributes.
- Added missing xsd data types: dateTimestamp, anyType, anyAtomicType.
- Added protection against duplicate class fields enumerations.
- Added python common types to the stop word list.
- Updated wildcards parsing to avoid duplicate elements.
- Updated native datatype detection made stricter.
- Updated enumerations generation to sort and filter values.
- Updated mapping xs:decimal to python Decimal
- Fixed elements/attribute not inheriting namespaces from references.
- Fixed module names collisions.
- Fixed self referencing classes.
- Fixed class name collisions complexTypes vs elements.
- Fixed parsers not respecting default values.
- Fixed AbstractXmlParser to handle leafless root nodes.
- Pass more than 90% of the `W3C XML Schema 1.1 test cases <https://travis-ci.org/tefra/xsdata-w3c-tests>`_.


20.2 (2020-02-09)
-----------------
- Added support xs:any and xs:anyAttribute elements.
- Added support for auto detecting XML Schema namespace prefix.
- Added support for xml datatypes lang and base.
- Refactored SchemaParser to use the XmlParser.
- Updated XmlParser to bind after elements are fully parsed.


20.1.3 (2020-01-26)
-------------------
- Fixed elements min|man occurs inheritance from their container.
- Fixed global elements and attributes are now always qualified.
- Fixed including no namespace schemas.
- Fixed list elements attribute handling.
- Added support for unqualified elements.
- Added support for qualified attributes.
- Added support for nillable elements.
- Added support for unions of member and simple types.
- Added binding test suite


20.1.2 (2020-01-13)
-------------------
- Generate anonymous Enumerations
- Generate attributes from List and Union elements
- Fix restriction inheritance
- Officially support python 3.8
- Completely migrate to setup.cfg
- Introduce integration test suite


20.1.1 (2020-01-09)
-------------------
- Change print mode to print rendered output
- Added new format PlantUML class diagram to replace the old print/debug mode


20.1 (2020-01-07)
-----------------
- Initial release
