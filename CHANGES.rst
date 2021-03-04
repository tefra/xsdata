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
