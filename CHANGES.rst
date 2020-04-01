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
