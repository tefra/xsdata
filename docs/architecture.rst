Architecture
============

Concept
-------

xsData is trying to convert schema definitions by making a few assumptions about them:

* They are opinionated
* They are too abstract
* There are more than one way to achieve the same result
* There are no best practices
* In the end Elements are classes and Attributes are class fields
* The rest is noise or metadata :)


Schema Parser
-------------

:class:`xsdata.codegen.parsers.schema.SchemaParser`

The schema parser objectifies the xml data to simple python dataclass instances that
are easy to work and extract all the relevant information.



Schema Mapper
-------------

:class:`xsdata.codegen.mappers.schema.SchemaMapper`

The builder goes through all the root elements of a schema to create a list of class
candidates.

* All root elements are considered class candidates
* Traverse the root elements object tree
* Detect fields and extensions
* Detect inner classes
* Assign namespaces and default ``value`` fields

**Root elements**: ``simpleType``, ``attributeGroup``, ``group``, ``attribute``,
``complexType``, ``element``

**Field elements**: ``attribute``, ``enumeration``, ``restiction``, ``element``

**Extension elements**: ``union``, ``attributeGroup``, ``group``, ``extension``,
``restriction``


Class Analyzer
--------------

:class:`xsdata.codegen.analyzer.ClassAnalyzer`

The analyzer goes through all class candidates and flattens attributes and extensions
based on certain criteria.

Promote for generation:

* Classes derived from xsd ``element`` with ``abstract`` flag set to ``False``
* Classes derived from xsd ``complexType`` with ``abstract`` flag set to ``False``
* Classes derived from xsd ``restiction`` with ``enumeration`` fields


Code Writer
------------

:class:`xsdata.codegen.writer.CodeWriter`

Code writer is a factory that delegates the code generation to the formats with their
language conventions.
