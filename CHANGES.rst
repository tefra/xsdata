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
